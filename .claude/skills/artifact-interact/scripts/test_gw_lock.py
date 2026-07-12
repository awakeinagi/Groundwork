#!/usr/bin/env python3
"""Tests for the DEC-0391 concurrency machinery (SES-0079,
DEC-0411..DEC-0416): shared/exclusive locking, journal rollback,
crash recovery, version tokens, and turn auto-numbering.

Self-contained: builds a scratch corpus in a temp dir per test class,
drives the real CLI via subprocess like test_gw_guards.py.
Run: python3 test_gw_lock.py
"""

import json
import os
import re
import subprocess
import sys
import tempfile
import threading
import time
import unittest
from pathlib import Path

HERE = Path(__file__).resolve().parent
GW_WRITE = HERE / "gw_write.py"
GW_READ = HERE / "groundwork_read.py"
CHECK = HERE / "check_links.py"

sys.path.insert(0, str(HERE))
import gw_lock  # noqa: E402

FM_TEMPLATE = """---
id: {aid}
type: {atype}
title: "Test {aid}"
status: {status}
owner: t@example.com
created: 2026-07-12
{extra}overview: >-
  Test artifact {aid} for the concurrency tests.
{links}---

{body}"""

SESSION_EXTRA = ("participant: tester\nparticipant-role: sponsor\n"
                 "facilitator: facilitator-agent\n"
                 "transcript-fidelity: reconstructed\n")

DIR_FOR = {"business-goal": "goals", "session": "sessions",
           "decision": "decisions", "spike": "spikes", "idea": "ideas"}


def session_body(aid, decisions_produced="DEC-0001 recorded."):
    return (f"# {aid}: Test session\n\n## Purpose\n\nTesting.\n\n"
            f"## Transcript\n\n### T1 — participant\n\nHello.\n\n"
            f"## Decisions Produced\n\n{decisions_produced}\n\n"
            f"## Conflicts Raised\n\nNone.\n")


def decision_body(aid):
    return (f"# {aid}: Test decision\n\n## Context\n\nCtx.\n\n"
            f"## Decision\n\nDo it.\n\n## Rationale\n\nWhy not.\n\n"
            f"## Alternatives Considered\n\nNone.\n\n"
            f"## Implications\n\nFew.\n")


class Scratch:
    def __init__(self, root):
        self.root = Path(root)

    def write(self, aid, atype, status, body, links="", extra=""):
        d = self.root / "docs" / DIR_FOR[atype]
        d.mkdir(parents=True, exist_ok=True)
        p = d / f"{aid}-test.md"
        p.write_text(FM_TEMPLATE.format(aid=aid, atype=atype,
                                        status=status, body=body,
                                        links=links, extra=extra),
                     encoding="utf-8")
        return p

    def baseline(self):
        self.write("BG-0001", "business-goal", "approved",
                   "# BG-0001: Test goal\n\n## Problem\n\nPain.\n\n"
                   "## Intent\n\nRelief.\n\n"
                   "## Outcomes & Success Criteria\n\nLess pain.\n\n"
                   "## Scope\n\nSmall.\n\n## Constraints\n\nFew.\n\n"
                   "## Stakeholders & Roles\n\nTester.\n\n"
                   "## Conflicts & Tensions\n\nNone.\n\n"
                   "## Derived Work\n\nNothing yet.\n")
        self.write("SES-0001", "session", "open", session_body("SES-0001"),
                   links="links:\n  relates-to: [DEC-0001]\n",
                   extra=SESSION_EXTRA)
        self.write("DEC-0001", "decision", "proposed",
                   decision_body("DEC-0001"),
                   links="links:\n  derives-from: [SES-0001]\n")
        return self


def gw(root, *argv, stdin=None, env=None):
    e = dict(os.environ)
    if env:
        e.update(env)
    return subprocess.run(
        [sys.executable, str(GW_WRITE), "--root", str(root), *argv],
        input=stdin, capture_output=True, text=True, env=e)


def gw_read(root, *argv):
    return subprocess.run(
        [sys.executable, str(GW_READ), "--root", str(root), *argv],
        capture_output=True, text=True)


def check(root):
    return subprocess.run([sys.executable, str(CHECK), str(root)],
                          capture_output=True, text=True)


def corpus_state(root):
    """Byte-level snapshot of every docs/ file for identity compares."""
    out = {}
    for p in sorted(Path(root).rglob("docs/**/*.md")):
        out[str(p.relative_to(root))] = p.read_bytes()
    return out


def token_from_section_read(root, aid, heading):
    r = gw_read(root, "section", aid, heading)
    assert r.returncode == 0, r.stderr
    m = re.search(r"^token: (v:[0-9a-f]{12})$", r.stdout, re.M)
    assert m, f"no token in section read output:\n{r.stdout}"
    return m.group(1)


class ParallelCreateTests(unittest.TestCase):
    """Test-plan item 1: the SES-0078/0079 race, reproduced and fixed."""

    def setUp(self):
        self._tmp = tempfile.TemporaryDirectory()
        self.root = Scratch(self._tmp.name).baseline().root
        self.addCleanup(self._tmp.cleanup)

    def test_parallel_creates_allocate_unique_sequential_ids(self):
        n = 8
        results = [None] * n

        def worker(i):
            results[i] = gw(self.root, "create", "--type", "idea",
                            "--title", f"Race idea {i}",
                            "--overview", f"Idea {i} racing for an ID.")

        threads = [threading.Thread(target=worker, args=(i,))
                   for i in range(n)]
        for t in threads:
            t.start()
        for t in threads:
            t.join()
        for r in results:
            self.assertEqual(r.returncode, 0, r.stderr)
        ids = re.findall(r"OK create (IDEA-\d{4})",
                         "\n".join(r.stdout for r in results))
        self.assertEqual(len(ids), n)
        self.assertEqual(len(set(ids)), n, f"duplicate IDs: {ids}")
        self.assertEqual(sorted(ids),
                         [f"IDEA-{i:04d}" for i in range(1, n + 1)])
        c = check(self.root)
        self.assertEqual(c.returncode, 0, c.stdout + c.stderr)


class LockSemanticsTests(unittest.TestCase):
    """Test-plan items 2 and 7: shared/exclusive semantics, timeouts."""

    def setUp(self):
        self._tmp = tempfile.TemporaryDirectory()
        self.root = Scratch(self._tmp.name).baseline().root
        self.addCleanup(self._tmp.cleanup)

    def test_concurrent_readers_both_proceed(self):
        with gw_lock.read_lock(self.root):
            r = gw_read(self.root, "overview", "DEC-0001")
        self.assertEqual(r.returncode, 0, r.stderr)

    def test_writer_blocks_reader_then_reader_sees_result(self):
        results = {}
        with gw_lock.write_lock(self.root):
            t = threading.Thread(target=lambda: results.update(
                r=gw_read(self.root, "overview", "DEC-0001")))
            t.start()
            time.sleep(0.5)
            self.assertIsNone(results.get("r"),
                              "reader finished during held write lock")
        t.join(timeout=15)
        self.assertEqual(results["r"].returncode, 0)

    def test_second_writer_times_out_with_holder_message(self):
        with gw_lock.write_lock(self.root):
            r = gw(self.root, "create", "--type", "idea",
                   "--title", "Blocked", "--overview", "Blocked idea.",
                   env={"GW_LOCK_TIMEOUT": "1"})
        self.assertEqual(r.returncode, 1)
        self.assertIn("could not acquire the exclusive corpus lock",
                      r.stderr)
        self.assertIn("pid", r.stderr)

    def test_writer_vs_writer_serializes(self):
        rs = []

        def w(i):
            rs.append(gw(self.root, "create", "--type", "idea",
                         "--title", f"Serial {i}",
                         "--overview", "Serialization test idea."))

        ts = [threading.Thread(target=w, args=(i,)) for i in range(2)]
        for t in ts:
            t.start()
        for t in ts:
            t.join()
        self.assertTrue(all(r.returncode == 0 for r in rs))
        ids = re.findall(r"OK create (IDEA-\d{4})",
                         "\n".join(r.stdout for r in rs))
        self.assertEqual(sorted(ids), ["IDEA-0001", "IDEA-0002"])


class RollbackTests(unittest.TestCase):
    """Test-plan items 3 and 4: all-or-nothing applies, crash recovery."""

    def setUp(self):
        self._tmp = tempfile.TemporaryDirectory()
        self.root = Scratch(self._tmp.name).baseline().root
        self.addCleanup(self._tmp.cleanup)

    def test_failed_batch_leaves_corpus_untouched(self):
        before = corpus_state(self.root)
        ops = [
            {"op": "create", "type": "idea", "title": "Batch idea",
             "overview": "First op lands, second fails."},
            {"op": "edit-section", "id": "IDEA-9999",
             "heading": "The Idea", "content": "Nope."},
        ]
        f = Path(self._tmp.name) / "ops.json"
        f.write_text(json.dumps(ops), encoding="utf-8")
        r = gw(self.root, "apply", str(f))
        self.assertEqual(r.returncode, 1)
        self.assertIn("rolling back", r.stdout + r.stderr)
        self.assertEqual(corpus_state(self.root), before,
                         "corpus changed despite failed batch")
        self.assertFalse(
            (self.root / ".groundwork-journal").exists(),
            "journal left behind after rollback")

    def test_reciprocal_second_file_rolls_back_too(self):
        self.root.joinpath("docs/ideas").mkdir(parents=True, exist_ok=True)
        before = corpus_state(self.root)
        ops = [
            {"op": "create", "type": "spike", "title": "Impactful",
             "overview": "Creates an impact edge onto BG-0001? No — "
                         "spikes impact spikes; this op fails on the "
                         "same-type rule after the file is written.",
             "links": {"derives-from": ["BG-0001"],
                       "impacts": ["BG-0001"]}},
        ]
        f = Path(self._tmp.name) / "ops.json"
        f.write_text(json.dumps(ops), encoding="utf-8")
        r = gw(self.root, "apply", str(f))
        self.assertEqual(r.returncode, 1)
        self.assertEqual(corpus_state(self.root), before)

    def test_crash_mid_apply_recovers_on_next_write(self):
        before = corpus_state(self.root)
        r = gw(self.root, "create", "--type", "idea",
               "--title", "Doomed", "--overview", "Crashes mid-apply.",
               env={"GW_TEST_CRASH": "after-first-write"})
        self.assertEqual(r.returncode, 9, "crash hook did not fire")
        self.assertTrue(
            (self.root / ".groundwork-journal/manifest.json").exists(),
            "no journal left by the crash")
        rd = gw_read(self.root, "overview", "DEC-0001")
        self.assertIn("interrupted write apply", rd.stderr)
        r2 = gw(self.root, "create", "--type", "idea",
                "--title", "Survivor", "--overview", "Lands cleanly.")
        self.assertEqual(r2.returncode, 0, r2.stderr)
        self.assertIn("rolled back an interrupted apply", r2.stdout)
        after = corpus_state(self.root)
        gone = set(before) - set(after)
        self.assertFalse(gone, "baseline files lost in recovery")
        self.assertIn("OK create IDEA-0001", r2.stdout,
                      "recovered corpus should re-allocate IDEA-0001")
        c = check(self.root)
        self.assertEqual(c.returncode, 0, c.stdout + c.stderr)

    def test_recover_op_standalone(self):
        gw(self.root, "create", "--type", "idea", "--title", "Doomed",
           "--overview", "Crashes mid-apply.",
           env={"GW_TEST_CRASH": "after-first-write"})
        r = gw(self.root, "recover")
        self.assertEqual(r.returncode, 0, r.stderr)
        self.assertIn("rolled back", r.stdout)
        r2 = gw(self.root, "recover")
        self.assertIn("no interrupted apply pending", r2.stdout)


class VersionTokenTests(unittest.TestCase):
    """Test-plan item 5: stale tokens refused, fresh tokens apply."""

    def setUp(self):
        self._tmp = tempfile.TemporaryDirectory()
        self.root = Scratch(self._tmp.name).baseline().root
        self.addCleanup(self._tmp.cleanup)

    def test_edit_section_requires_token(self):
        r = gw(self.root, "edit-section", "DEC-0001", "Context",
               stdin="New context.")
        self.assertEqual(r.returncode, 1)
        self.assertIn("--if-match", r.stderr)

    def test_fresh_token_applies_and_is_stable(self):
        t1 = token_from_section_read(self.root, "DEC-0001", "Context")
        t2 = token_from_section_read(self.root, "DEC-0001", "Context")
        self.assertEqual(t1, t2, "token unstable across unchanged reads")
        r = gw(self.root, "edit-section", "DEC-0001", "Context",
               "--if-match", t1, stdin="Fresh context, token held.")
        self.assertEqual(r.returncode, 0, r.stderr)

    def test_stale_token_refused_with_reread_instruction(self):
        t1 = token_from_section_read(self.root, "DEC-0001", "Context")
        r = gw(self.root, "edit-section", "DEC-0001", "Context",
               "--if-match", t1, stdin="First edit wins.")
        self.assertEqual(r.returncode, 0, r.stderr)
        r2 = gw(self.root, "edit-section", "DEC-0001", "Context",
                "--if-match", t1, stdin="Second edit with stale token.")
        self.assertEqual(r2.returncode, 1)
        self.assertIn("changed since your read", r2.stderr)
        self.assertIn("re-read", r2.stderr)

    def test_update_overview_token_round_trip(self):
        r = gw_read(self.root, "overview", "DEC-0001")
        m = re.search(r"^  token: (v:[0-9a-f]{12})$", r.stdout, re.M)
        self.assertTrue(m, r.stdout)
        bad = gw(self.root, "update-overview", "DEC-0001",
                 "--text", "New overview text for the test decision.",
                 "--if-match", "v:000000000000")
        self.assertEqual(bad.returncode, 1)
        good = gw(self.root, "update-overview", "DEC-0001",
                  "--text", "New overview text for the test decision.",
                  "--if-match", m.group(1))
        self.assertEqual(good.returncode, 0, good.stderr)

    def test_created_in_batch_exempt_from_token(self):
        ops = [
            {"op": "create", "type": "idea", "title": "Batch built",
             "overview": "Created and edited in one batch."},
            {"op": "edit-section", "id": "IDEA-0001",
             "heading": "The Idea", "content": "Edited without token."},
        ]
        f = Path(self._tmp.name) / "ops.json"
        f.write_text(json.dumps(ops), encoding="utf-8")
        r = gw(self.root, "apply", str(f))
        self.assertEqual(r.returncode, 0, r.stdout + r.stderr)


class TurnAppendTests(unittest.TestCase):
    """Test-plan item 6: auto-numbering and the expect precondition."""

    def setUp(self):
        self._tmp = tempfile.TemporaryDirectory()
        self.root = Scratch(self._tmp.name).baseline().root
        self.addCleanup(self._tmp.cleanup)

    def test_auto_number_continues_from_live_max(self):
        r = gw(self.root, "append-turn", "SES-0001",
               stdin="### T1 (tester)\n\nMisnumbered on purpose.")
        self.assertEqual(r.returncode, 0, r.stderr)
        self.assertIn("assigned T2", r.stdout)
        body = gw_read(self.root, "turns", "SES-0001", "T2")
        self.assertIn("Misnumbered on purpose", body.stdout)

    def test_multi_turn_payload_numbers_sequentially(self):
        r = gw(self.root, "append-turn", "SES-0001",
               stdin="### T90 (a)\n\nOne.\n\n### T91 (b)\n\nTwo.")
        self.assertEqual(r.returncode, 0, r.stderr)
        self.assertIn("assigned T2-T3", r.stdout)

    def test_expect_first_turn_mismatch_refused(self):
        r = gw(self.root, "append-turn", "SES-0001",
               "--expect-first-turn", "5",
               stdin="### T5 (tester)\n\nExpecting T5.")
        self.assertEqual(r.returncode, 1)
        self.assertIn("next turn is T2", r.stderr)

    def test_parallel_appends_serialize_without_duplicates(self):
        rs = []

        def w(i):
            rs.append(gw(self.root, "append-turn", "SES-0001",
                         stdin=f"### T1 (racer {i})\n\nRacing."))

        ts = [threading.Thread(target=w, args=(i,)) for i in range(2)]
        for t in ts:
            t.start()
        for t in ts:
            t.join()
        self.assertTrue(all(r.returncode == 0 for r in rs))
        text = self.root.joinpath(
            "docs/sessions/SES-0001-test.md").read_text()
        turns = re.findall(r"^### T(\d+)", text, re.M)
        self.assertEqual(sorted(turns), ["1", "2", "3"],
                         f"turn numbers corrupted: {turns}")


if __name__ == "__main__":
    unittest.main(verbosity=2)
