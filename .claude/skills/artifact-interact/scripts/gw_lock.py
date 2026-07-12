#!/usr/bin/env python3
"""Concurrency primitives for the gw CLI (DEC-0391; SES-0079,
DEC-0411..DEC-0416). Pure stdlib (DEC-0317).

Three things live here, shared by every family that touches live
corpus files:

- read_lock(root) / write_lock(root): shared/exclusive advisory locks
  (fcntl.flock) on <root>/.groundwork-lock. Context managers — release
  is explicit at block exit; kernel release-on-process-death is only
  the crash fallback (DEC-0411). Acquisition retries non-blocking to a
  deadline (10s shared, 60s exclusive; GW_LOCK_TIMEOUT overrides both),
  then refuses cleanly naming the holder when known. GW_LOCK_BYPASS=1
  skips acquisition entirely — set only by a parent process that
  already holds the lock for a child it runs under it (graph sync,
  DEC-0415) and by tests demonstrating the unlocked baseline.

- Journal: the all-or-nothing apply machinery (DEC-0412). Before a file
  is first mutated, its original bytes are copied under
  <root>/.groundwork-journal/ and the manifest is flushed atomically;
  rollback() restores every original and deletes every created file.
  A leftover journal marks an interrupted apply — the next writer
  calls recover() under the exclusive lock before doing anything else.

- version tokens (DEC-0413): version_token(text) -> "v:<12 hex>" over
  whitespace-normalized text. Derived, never stored; reads emit them,
  content-mutating writes require them back via --if-match.
"""

import contextlib
import fcntl
import hashlib
import json
import os
import shutil
import sys
import time
from pathlib import Path

LOCK_NAME = ".groundwork-lock"
JOURNAL_DIRNAME = ".groundwork-journal"
READ_TIMEOUT = 10.0
WRITE_TIMEOUT = 60.0
_POLL = 0.1


def _timeout(default):
    env = os.environ.get("GW_LOCK_TIMEOUT")
    if not env:
        return default
    try:
        return max(0.0, float(env))
    except ValueError:
        return default


def _bypass():
    return os.environ.get("GW_LOCK_BYPASS") == "1"


def _acquire(root, flags, timeout, label):
    lock_path = Path(root).resolve() / LOCK_NAME
    fd = os.open(lock_path, os.O_RDWR | os.O_CREAT, 0o644)
    deadline = time.monotonic() + timeout
    while True:
        try:
            fcntl.flock(fd, flags | fcntl.LOCK_NB)
            return fd
        except OSError:
            if time.monotonic() >= deadline:
                holder = ""
                try:
                    info = os.pread(fd, 256, 0).decode(errors="replace")
                    if info.strip():
                        holder = f" (held by {info.strip()})"
                except OSError:
                    pass
                os.close(fd)
                print(f"REFUSED: could not acquire the {label} corpus "
                      f"lock on {lock_path} within {timeout:.0f}s"
                      f"{holder} — retry, or raise GW_LOCK_TIMEOUT "
                      "(DEC-0411)", file=sys.stderr)
                raise SystemExit(1)
            time.sleep(_POLL)


@contextlib.contextmanager
def read_lock(root):
    """Shared lock: concurrent readers never block each other; a reader
    never observes a torn mid-apply state (DEC-0391)."""
    if _bypass():
        yield
        return
    fd = _acquire(root, fcntl.LOCK_SH, _timeout(READ_TIMEOUT), "shared")
    try:
        yield
    finally:
        fcntl.flock(fd, fcntl.LOCK_UN)
        os.close(fd)


@contextlib.contextmanager
def write_lock(root):
    """Exclusive lock around the whole apply span: corpus scan, ID
    allocation, edits, reciprocity, recheck, graph sync (DEC-0411)."""
    if _bypass():
        yield
        return
    fd = _acquire(root, fcntl.LOCK_EX, _timeout(WRITE_TIMEOUT),
                  "exclusive")
    try:
        os.ftruncate(fd, 0)
        os.pwrite(fd, f"pid {os.getpid()}".encode(), 0)
        yield
    finally:
        try:
            os.ftruncate(fd, 0)
        except OSError:
            pass
        fcntl.flock(fd, fcntl.LOCK_UN)
        os.close(fd)


# ------------------------------------------------------------- journal

class Journal:
    """All-or-nothing apply journal (DEC-0412). Use under write_lock.

    record()/record_create() are called BEFORE each mutation; the
    manifest on disk therefore always covers every byte already
    changed, so rollback works both in-process (recheck failure, any
    exception) and across a crash (recover() by the next writer).
    """

    def __init__(self, root):
        self.root = Path(root).resolve()
        self.dir = self.root / JOURNAL_DIRNAME
        self.manifest = self.dir / "manifest.json"
        self.entries = {}  # relpath -> backup filename | None (created)

    def _flush(self):
        self.dir.mkdir(exist_ok=True)
        tmp = self.dir / "manifest.json.tmp"
        tmp.write_text(json.dumps({"entries": self.entries}, indent=1),
                       encoding="utf-8")
        os.replace(tmp, self.manifest)

    def record(self, path):
        """Journal an existing file about to be mutated."""
        rel = str(Path(path).resolve().relative_to(self.root))
        if rel in self.entries:
            return
        backup = f"{len(self.entries):04d}-{Path(path).name}"
        self.dir.mkdir(exist_ok=True)
        shutil.copy2(path, self.dir / backup)
        self.entries[rel] = backup
        self._flush()

    def record_create(self, path):
        """Journal a file about to be created (rollback deletes it)."""
        rel = str(Path(path).resolve().relative_to(self.root))
        if rel in self.entries:
            return
        self.entries[rel] = None
        self._flush()

    @property
    def mutated(self):
        return bool(self.entries)

    def rollback(self):
        """Restore originals, delete created files. Returns file count."""
        n = 0
        for rel, backup in self.entries.items():
            target = self.root / rel
            if backup is None:
                if target.exists():
                    target.unlink()
                    n += 1
            elif (self.dir / backup).exists():
                shutil.copy2(self.dir / backup, target)
                n += 1
        self.entries = {}
        if self.dir.exists():
            shutil.rmtree(self.dir)
        return n

    def commit(self):
        self.entries = {}
        if self.dir.exists():
            shutil.rmtree(self.dir)

    def recover(self):
        """Roll back a leftover journal from an interrupted apply.
        Returns the number of files restored (0 = nothing pending)."""
        if self.manifest.exists():
            data = json.loads(self.manifest.read_text(encoding="utf-8"))
            self.entries = data.get("entries", {})
            return self.rollback()
        if self.dir.exists():  # crashed before any mutation was recorded
            shutil.rmtree(self.dir)
        return 0


def journal_pending(root):
    """True when an interrupted apply awaits rollback (readers warn;
    writers recover)."""
    return (Path(root).resolve() / JOURNAL_DIRNAME /
            "manifest.json").exists()


# ------------------------------------------------------- atomic writes

def atomic_write(path, text):
    """tempfile-in-same-dir + os.replace: a file is either its old or
    its new bytes, never torn (DEC-0412)."""
    path = Path(path)
    tmp = path.parent / f".gw-tmp-{os.getpid()}-{path.name}"
    tmp.write_text(text, encoding="utf-8")
    os.replace(tmp, path)
    if os.environ.get("GW_TEST_CRASH") == "after-first-write":
        # Test-only crash hook for the DEC-0416 recovery case: die hard
        # after the first mutation lands, journal intact.
        os.environ["GW_TEST_CRASH"] = "armed-once"
        os._exit(9)


# ------------------------------------------------------ version tokens

def normalize_text(text):
    lines = [ln.rstrip() for ln in text.splitlines()]
    while lines and not lines[0]:
        lines.pop(0)
    while lines and not lines[-1]:
        lines.pop()
    return "\n".join(lines)


def version_token(text):
    """Derived per-section token (DEC-0413): stable across reads of
    unchanged content, never stored in files."""
    digest = hashlib.sha256(normalize_text(text).encode("utf-8"))
    return "v:" + digest.hexdigest()[:12]
