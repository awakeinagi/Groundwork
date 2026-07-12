#!/usr/bin/env python3
"""Tests for the SES-0072 structural guards in gw_write.py and the
rule 21-24 additions to check_links.py (IDEA-0041/IDEA-0028).

Self-contained: builds a scratch corpus in a temp dir per test class.
Run: python3 test_gw_guards.py
"""

import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

HERE = Path(__file__).resolve().parent
GW_WRITE = HERE / "gw_write.py"
CHECK = HERE / "check_links.py"

FM_TEMPLATE = """---
id: {aid}
type: {atype}
title: "Test {aid}"
status: {status}
owner: t@example.com
created: 2026-07-12
{extra}overview: >-
  Test artifact {aid} for the structural guard tests.
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


def spike_body(aid, findings="Investigated."):
    return (f"# {aid}: Test spike\n\n## Question\n\nWhat.\n\n"
            f"## Why It Blocks\n\nBecause.\n\n## Method\n\nLook.\n\n"
            f"## Findings\n\n{findings}\n\n"
            f"## Resulting Decisions\n\nNone yet.\n")


def decision_body(aid):
    return (f"# {aid}: Test decision\n\n## Context\n\nCtx.\n\n"
            f"## Decision\n\nDo it.\n\n## Rationale\n\nWhy not.\n\n"
            f"## Alternatives Considered\n\nNone.\n\n"
            f"## Implications\n\nFew.\n")


def idea_body(aid, first_line=None):
    return ((first_line or f"# {aid}: Test idea") +
            "\n\n## The Idea\n\nThing.\n\n## Spark Context\n\nChat.\n\n"
            "## Disposition\n\nPending.\n")


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
        """A minimal corpus that passes the full checker."""
        self.write("BG-0001", "business-goal", "approved",
                   "# BG-0001: Test goal\n\n## Problem\n\nPain.\n\n"
                   "## Derived Work\n\nSP-0001 derives from this goal.\n")
        self.write("SES-0001", "session", "open", session_body("SES-0001"),
                   links="links:\n  relates-to: [DEC-0001]\n",
                   extra=SESSION_EXTRA)
        self.write("DEC-0001", "decision", "proposed",
                   decision_body("DEC-0001"),
                   links="links:\n  derives-from: [SES-0001]\n")
        self.write("SP-0001", "spike", "draft", spike_body("SP-0001"),
                   links="links:\n  derives-from: [BG-0001]\n")
        return self


def gw(root, *argv, stdin=None):
    return subprocess.run(
        [sys.executable, str(GW_WRITE), "--root", str(root), *argv],
        input=stdin, capture_output=True, text=True)


def check(root):
    return subprocess.run([sys.executable, str(CHECK), str(root)],
                          capture_output=True, text=True)


class GuardTests(unittest.TestCase):
    def setUp(self):
        self._tmp = tempfile.TemporaryDirectory()
        self.s = Scratch(self._tmp.name).baseline()
        self.root = self.s.root
        self.addCleanup(self._tmp.cleanup)

    def path_of(self, aid, atype):
        return self.root / "docs" / DIR_FOR[atype] / f"{aid}-test.md"

    # A1: heading guard on edit-section
    def test_heading_payload_refused_file_unchanged(self):
        p = self.path_of("SES-0001", "session")
        before = p.read_text()
        r = gw(self.root, "edit-section", "SES-0001", "Purpose",
               stdin="## Purpose\n\nNew purpose.")
        self.assertNotEqual(r.returncode, 0, r.stdout + r.stderr)
        self.assertIn("heading-level line", r.stderr)
        self.assertEqual(p.read_text(), before)

    def test_lower_level_heading_allowed(self):
        r = gw(self.root, "edit-section", "SES-0001", "Purpose",
               stdin="Intro.\n\n### Sub-point\n\nDetail.")
        self.assertEqual(r.returncode, 0, r.stdout + r.stderr)

    def test_clean_edit_idempotent(self):
        p = self.path_of("SES-0001", "session")
        r1 = gw(self.root, "edit-section", "SES-0001", "Purpose",
                stdin="New purpose.")
        self.assertEqual(r1.returncode, 0, r1.stderr)
        after1 = p.read_text()
        r2 = gw(self.root, "edit-section", "SES-0001", "Purpose",
                stdin="New purpose.")
        self.assertEqual(r2.returncode, 0, r2.stderr)
        self.assertEqual(p.read_text(), after1)

    # A2: --occurrence and delete-section
    def corrupt_spike(self):
        return self.s.write(
            "SP-0002", "spike", "draft",
            spike_body("SP-0002").replace(
                "## Findings\n", "## Findings\n\n## Findings\n", 1),
            links="links:\n  derives-from: [BG-0001]\n")

    def test_occurrence_targets_nth(self):
        p = self.corrupt_spike()
        r = gw(self.root, "edit-section", "SP-0002", "Findings",
               "--occurrence", "2", stdin="Repaired content.")
        self.assertEqual(r.returncode, 0, r.stderr)
        text = p.read_text()
        self.assertIn("Repaired content.", text)
        self.assertEqual(text.count("## Findings"), 2)  # not yet deleted

    def test_delete_section_removes_duplicate_keeps_required(self):
        p = self.corrupt_spike()
        r = gw(self.root, "delete-section", "SP-0002", "Findings",
               "--occurrence", "1")
        self.assertEqual(r.returncode, 0, r.stderr)
        text = p.read_text()
        self.assertEqual(text.count("## Findings"), 1)
        self.assertIn("Investigated.", text)
        r2 = gw(self.root, "delete-section", "SP-0002", "Findings")
        self.assertNotEqual(r2.returncode, 0)
        self.assertIn("required section", r2.stderr)

    def test_delete_section_refuses_closed_session(self):
        self.s.write("SES-0002", "session", "closed",
                     session_body("SES-0002"),
                     links="links:\n  relates-to: [DEC-0001]\n",
                     extra=SESSION_EXTRA)
        r = gw(self.root, "delete-section", "SES-0002", "Conflicts Raised")
        self.assertNotEqual(r.returncode, 0)
        self.assertIn("immutable", r.stderr)

    # A3: append-turn guard
    def test_append_turn_guard(self):
        r = gw(self.root, "append-turn", "SES-0001",
               stdin="## Rogue heading\n\nText.")
        self.assertNotEqual(r.returncode, 0)
        self.assertIn("heading-level line", r.stderr)
        r2 = gw(self.root, "append-turn", "SES-0001",
                stdin="### T2 — facilitator\n\nMore.")
        self.assertEqual(r2.returncode, 0, r2.stderr)

    # A4: ratification structural gate
    def test_approve_with_duplicate_headings_refused(self):
        self.s.write("SP-0003", "spike", "gated",
                     spike_body("SP-0003").replace(
                         "## Findings\n", "## Findings\n\n## Findings\n",
                         1),
                     links="links:\n  derives-from: [BG-0001]\n")
        r = gw(self.root, "set-status", "SP-0003", "approved",
               "--approved-by", "tester")
        self.assertNotEqual(r.returncode, 0)
        self.assertIn("duplicate sibling heading", r.stderr)

    def test_close_with_placeholder_refused(self):
        self.s.write("SES-0003", "session", "open",
                     session_body("SES-0003", decisions_produced="TBD."),
                     extra=SESSION_EXTRA)
        r = gw(self.root, "set-status", "SES-0003", "closed")
        self.assertNotEqual(r.returncode, 0)
        self.assertIn("placeholder", r.stderr)

    # A5: session close frontmatter completeness
    def test_close_missing_frontmatter_refused(self):
        self.s.write("SES-0004", "session", "open",
                     session_body("SES-0004"),
                     extra="participant: tester\n")
        r = gw(self.root, "set-status", "SES-0004", "closed")
        self.assertNotEqual(r.returncode, 0)
        self.assertIn("facilitator", r.stderr)

    # A6: zero-decision close acknowledgment
    def test_zero_decision_close(self):
        self.s.write("SES-0005", "session", "open",
                     session_body("SES-0005", decisions_produced="None."),
                     extra=SESSION_EXTRA)
        r = gw(self.root, "set-status", "SES-0005", "closed")
        self.assertNotEqual(r.returncode, 0)
        self.assertIn("no decision derives", r.stderr)
        r2 = gw(self.root, "set-status", "SES-0005", "closed",
                "--no-decisions-ok", "idea-capture session")
        self.assertEqual(r2.returncode, 0, r2.stderr)
        self.assertIn("zero decisions acknowledged", r2.stdout)

    def test_close_with_decisions_needs_no_flag(self):
        r = gw(self.root, "set-status", "SES-0001", "closed")
        self.assertEqual(r.returncode, 0, r.stderr)

    # A7: create stamps the allocated ID into a placeholder H1
    def test_create_stamps_h1(self):
        body = idea_body("IDEA-0001", first_line="# IDEA-XXXX: Test idea")
        bf = self.root / "body.md"
        bf.write_text(body)
        r = gw(self.root, "create", "--type", "idea", "--title",
               "Test idea", "--overview", "A test idea.",
               "--from-file", str(bf))
        self.assertEqual(r.returncode, 0, r.stderr)
        created = next((self.root / "docs" / "ideas").glob("IDEA-0001-*"))
        self.assertTrue(created.read_text().split("---\n")[-1]
                        .lstrip().startswith("# IDEA-0001:"))

    # B1 (SES-0077, DEC-0399): body ID scans are code-span-aware
    def test_code_span_id_in_body_passes(self):
        r = gw(self.root, "edit-section", "SES-0001", "Purpose",
               stdin="A verbatim quote mentioning `DEC-9999` in backticks.")
        self.assertEqual(r.returncode, 0, r.stdout + r.stderr)

    def test_fenced_block_id_passes(self):
        r = gw(self.root, "edit-section", "SES-0001", "Purpose",
               stdin="Example:\n\n```\nsee DEC-9999\n```\n\nDone.")
        self.assertEqual(r.returncode, 0, r.stdout + r.stderr)

    def test_bare_unresolvable_id_still_refused(self):
        r = gw(self.root, "edit-section", "SES-0001", "Purpose",
               stdin="Prose naming DEC-9999 bare.")
        self.assertNotEqual(r.returncode, 0)
        self.assertIn("unresolved", r.stderr)

    def test_turn_code_span_id_passes(self):
        r = gw(self.root, "append-turn", "SES-0001",
               stdin="### T2 — facilitator\n\nQuoted `DEC-9999` verbatim.")
        self.assertEqual(r.returncode, 0, r.stdout + r.stderr)

    # B2 (SES-0077, DEC-0398): overview IDs must resolve, backticks
    # grant no exemption on that surface
    def test_overview_backticked_unresolvable_id_refused(self):
        r = gw(self.root, "update-overview", "SES-0001",
               "--text", "Mentions `DEC-9999` which does not exist.")
        self.assertNotEqual(r.returncode, 0)
        self.assertIn("unresolved", r.stderr)

    # B3 (SES-0077, DEC-0402): typed frontmatter validation at create
    def test_create_bad_enum_refused(self):
        r = gw(self.root, "create", "--type", "session", "--title",
               "Bad fidelity", "--overview", "A test session.",
               "--field", "transcript-fidelity: live")
        self.assertNotEqual(r.returncode, 0)
        self.assertIn("transcript-fidelity", r.stderr)
        self.assertIn("verbatim", r.stderr)

    def test_create_list_valued_scalar_refused(self):
        r = gw(self.root, "create", "--type", "session", "--title",
               "List participant", "--overview", "A test session.",
               "--field", "participant: [a, b]")
        self.assertNotEqual(r.returncode, 0)
        self.assertIn("single scalar", r.stderr)

    def test_create_bad_date_refused(self):
        r = gw(self.root, "create", "--type", "decision", "--title",
               "Bad date", "--overview", "A test decision.",
               "--link", "derives-from=SES-0001",
               "--field", "decided-on: last week")
        self.assertNotEqual(r.returncode, 0)
        self.assertIn("YYYY-MM-DD", r.stderr)

    def test_create_wrong_type_field_refused(self):
        r = gw(self.root, "create", "--type", "idea", "--title",
               "Wrong field", "--overview", "A test idea.",
               "--field", "transcript-fidelity: verbatim")
        self.assertNotEqual(r.returncode, 0)
        self.assertIn("applies to", r.stderr)

    def test_create_unknown_field_passes(self):
        r = gw(self.root, "create", "--type", "idea", "--title",
               "Custom field ok", "--overview", "A test idea.",
               "--field", "custom-key: anything goes")
        self.assertEqual(r.returncode, 0, r.stdout + r.stderr)

    # B4 (SES-0077 item 9): required-section skeleton at create
    def test_create_sectionless_body_refused(self):
        bf = self.root / "flat.md"
        bf.write_text("# IDEA-XXXX: Flat\n\nJust prose, no sections.\n")
        r = gw(self.root, "create", "--type", "idea", "--title", "Flat",
               "--overview", "A flat test idea.", "--from-file", str(bf))
        self.assertNotEqual(r.returncode, 0)
        self.assertIn("missing required section", r.stderr)
        self.assertEqual(
            list((self.root / "docs" / "ideas").glob("IDEA-*")), [])

    def test_create_at_ratified_status_runs_structural_gate(self):
        # A decision created directly at accepted with placeholder text
        # must refuse — closing the DEC-0378 bypass.
        bf = self.root / "dec.md"
        bf.write_text(decision_body("DEC-XXXX").replace("Few.", "TBD."))
        r = gw(self.root, "create", "--type", "decision", "--title",
               "Direct accepted", "--overview", "A test decision.",
               "--status", "accepted",
               "--link", "derives-from=SES-0001", "--from-file", str(bf))
        self.assertNotEqual(r.returncode, 0)
        self.assertIn("placeholder", r.stderr)
        # the same body at proposed status is fine (drafts may stub)
        r2 = gw(self.root, "create", "--type", "decision", "--title",
                "Proposed ok", "--overview", "A test decision.",
                "--link", "derives-from=SES-0001", "--from-file", str(bf))
        self.assertEqual(r2.returncode, 0, r2.stdout + r2.stderr)

    def test_create_with_full_skeleton_at_accepted_passes(self):
        bf = self.root / "dec2.md"
        bf.write_text(decision_body("DEC-XXXX"))
        r = gw(self.root, "create", "--type", "decision", "--title",
               "Clean accepted", "--overview", "A test decision.",
               "--status", "accepted",
               "--link", "derives-from=SES-0001", "--from-file", str(bf))
        self.assertEqual(r.returncode, 0, r.stdout + r.stderr)

    # SES-0072 fold-in: PyYAML frontmatter validation at recheck
    def test_invalid_yaml_frontmatter_refused(self):
        r = gw(self.root, "create", "--type", "idea", "--title",
               "Bad yaml probe", "--overview", "A test idea.",
               "--field", "bad: [unclosed")
        self.assertNotEqual(r.returncode, 0)
        self.assertIn("parseable YAML", r.stderr)

    # A8: accepted-in stamp
    def test_accept_requires_session_and_stamps(self):
        r = gw(self.root, "set-status", "DEC-0001", "accepted")
        self.assertNotEqual(r.returncode, 0)
        self.assertIn("--session", r.stderr)
        r2 = gw(self.root, "set-status", "DEC-0001", "accepted",
                "--session", "SES-0001")
        self.assertEqual(r2.returncode, 0, r2.stderr)
        self.assertIn("accepted-in: SES-0001",
                      self.path_of("DEC-0001", "decision").read_text())


class RemoveCiteTests(unittest.TestCase):
    """SES-0077 (DEC-0403): the remove-cite operation."""

    def setUp(self):
        self._tmp = tempfile.TemporaryDirectory()
        self.s = Scratch(self._tmp.name).baseline()
        self.root = self.s.root
        self.addCleanup(self._tmp.cleanup)

    def test_clean_removal_drops_cites_line(self):
        # SP-0001's body never mentions DEC-0001 — removal is legal.
        gw(self.root, "add-cite", "SP-0001", "DEC-0001")
        r = gw(self.root, "remove-cite", "SP-0001", "DEC-0001")
        self.assertEqual(r.returncode, 0, r.stdout + r.stderr)
        text = (self.root / "docs" / "spikes" /
                "SP-0001-test.md").read_text()
        self.assertNotIn("cites:", text)

    def test_body_reference_refuses(self):
        # SES-0001's body says "DEC-0001 recorded." — a live reference.
        gw(self.root, "add-cite", "SES-0001", "DEC-0001")
        r = gw(self.root, "remove-cite", "SES-0001", "DEC-0001")
        self.assertNotEqual(r.returncode, 0)
        self.assertIn("still references", r.stderr)

    def test_code_span_body_mention_does_not_block(self):
        gw(self.root, "add-cite", "SP-0001", "DEC-0001")
        gw(self.root, "edit-section", "SP-0001", "Findings",
           stdin="Quoting `DEC-0001` in a code span only.")
        r = gw(self.root, "remove-cite", "SP-0001", "DEC-0001")
        self.assertEqual(r.returncode, 0, r.stdout + r.stderr)

    def test_not_cited_refuses(self):
        r = gw(self.root, "remove-cite", "SP-0001", "DEC-0001")
        self.assertNotEqual(r.returncode, 0)
        self.assertIn("does not cite", r.stderr)

    def test_closed_session_refuses(self):
        self.s.write("SES-0002", "session", "closed",
                     session_body("SES-0002"),
                     links=("links:\n  relates-to: [DEC-0001]\n"
                            "cites: [DEC-0001]\n"),
                     extra=SESSION_EXTRA)
        r = gw(self.root, "remove-cite", "SES-0002", "DEC-0001")
        self.assertNotEqual(r.returncode, 0)
        self.assertIn("immutable", r.stderr)

    def test_approved_requires_amend(self):
        self.s.write("SP-0004", "spike", "approved", spike_body("SP-0004"),
                     links=("links:\n  derives-from: [BG-0001]\n"
                            "cites: [DEC-0001]\n"))
        r = gw(self.root, "remove-cite", "SP-0004", "DEC-0001")
        self.assertNotEqual(r.returncode, 0)
        self.assertIn("--amend", r.stderr)
        r2 = gw(self.root, "remove-cite", "SP-0004", "DEC-0001", "--amend")
        self.assertEqual(r2.returncode, 0, r2.stdout + r2.stderr)


class BatchTests(unittest.TestCase):
    """SES-0077: batch pre-validation (DEC-0400) and failure
    accounting (DEC-0401)."""

    def setUp(self):
        self._tmp = tempfile.TemporaryDirectory()
        self.s = Scratch(self._tmp.name).baseline()
        self.root = self.s.root
        self.addCleanup(self._tmp.cleanup)

    def apply(self, ops):
        import json
        bf = self.root / "batch.json"
        bf.write_text(json.dumps(ops))
        return gw(self.root, "apply", str(bf))

    def test_string_link_key_refuses_whole_batch(self):
        # The SES-0067 failure shape: CLI-style link string in batch —
        # previously silently dropped; now the WHOLE batch refuses.
        r = self.apply([
            {"op": "create", "type": "idea", "title": "Valid one",
             "overview": "A valid idea."},
            {"op": "create", "type": "idea", "title": "Bad link",
             "overview": "Link as string.",
             "link": "derives-from=SES-0001"},
        ])
        self.assertNotEqual(r.returncode, 0)
        self.assertIn("nothing applied", r.stderr)
        self.assertIn("'link'", r.stderr)
        # the VALID sibling op must not have applied either
        self.assertEqual(
            list((self.root / "docs" / "ideas").glob("IDEA-*")), [])

    def test_unknown_rel_key_refused_not_written(self):
        # Previously an unknown rel key was written verbatim into
        # frontmatter; now it refuses at pre-validation.
        r = self.apply([
            {"op": "create", "type": "idea", "title": "Bad rel",
             "overview": "Bad rel key.",
             "links": {"derived-from": ["SES-0001"]}},
        ])
        self.assertNotEqual(r.returncode, 0)
        self.assertIn("'derived-from'", r.stderr)
        self.assertEqual(
            list((self.root / "docs" / "ideas").glob("IDEA-*")), [])

    def test_links_value_must_be_list(self):
        r = self.apply([
            {"op": "create", "type": "idea", "title": "Scalar target",
             "overview": "Links target not a list.",
             "links": {"derives-from": "SES-0001"}},
        ])
        self.assertNotEqual(r.returncode, 0)
        self.assertIn("must be a list", r.stderr)

    def test_unknown_op_refuses_whole_batch(self):
        r = self.apply([{"op": "remove-everything", "id": "BG-0001"}])
        self.assertNotEqual(r.returncode, 0)
        self.assertIn("unknown op", r.stderr)

    def test_happy_batch_prints_applied_summary(self):
        r = self.apply([
            {"op": "create", "type": "idea", "title": "First",
             "overview": "First idea.",
             "links": {"derives-from": ["SES-0001"]}},
            {"op": "edit-section", "id": "SES-0001", "heading": "Purpose",
             "content": "Updated purpose."},
        ])
        self.assertEqual(r.returncode, 0, r.stdout + r.stderr)
        self.assertIn("applied 2/2", r.stdout)

    def test_apply_time_failure_prints_manifest(self):
        # Op 0 applies; op 1 fails at apply time (nonexistent cite
        # target passes pre-validation, fails on load); op 2 is never
        # attempted. The manifest must say all three things.
        r = self.apply([
            {"op": "edit-section", "id": "SES-0001", "heading": "Purpose",
             "content": "First edit lands."},
            {"op": "add-cite", "id": "SES-0001", "target": "DEC-9999"},
            {"op": "edit-section", "id": "SES-0001",
             "heading": "Conflicts Raised", "content": "Never reached."},
        ])
        self.assertNotEqual(r.returncode, 0)
        self.assertIn("applied 1 of 3", r.stdout)
        self.assertIn("not attempted: 2 (edit-section)", r.stdout)
        text = (self.root / "docs" / "sessions" /
                "SES-0001-test.md").read_text()
        self.assertIn("First edit lands.", text)
        self.assertNotIn("Never reached.", text)


class PipeSafetyTests(unittest.TestCase):
    """SES-0077 (DEC-0404): closed output pipes exit clean, no
    traceback."""

    def setUp(self):
        self._tmp = tempfile.TemporaryDirectory()
        self.s = Scratch(self._tmp.name).baseline()
        self.root = self.s.root
        # Enough output to overflow the 64KB pipe buffer so the write
        # is guaranteed to hit the closed pipe.
        for i in range(2, 52):
            aid = f"IDEA-{i:04d}"
            p = self.s.write(aid, "idea", "captured", idea_body(aid))
            p.write_text(p.read_text().replace(
                f"Test artifact {aid} for the structural guard tests.",
                "pad " * 400))
        self.addCleanup(self._tmp.cleanup)

    def test_read_survives_early_pipe_close(self):
        reader = HERE / "groundwork_read.py"
        cmd = (f"set -o pipefail; {sys.executable} {reader} --root "
               f"{self.root} overview --type idea | head -c 100 "
               ">/dev/null")
        r = subprocess.run(["bash", "-c", cmd],
                           capture_output=True, text=True)
        self.assertEqual(r.returncode, 0, r.stderr)
        self.assertNotIn("Traceback", r.stderr)
        self.assertNotIn("BrokenPipeError", r.stderr)


class HelpContractTests(unittest.TestCase):
    """SES-0077 (DEC-0406): every subcommand of the stdlib argparse
    scripts answers --help with substantive text, so agents can learn
    usage without reading source. (The search family carries the same
    standard but needs uv-run dependencies, so it is smoke-tested
    manually rather than here.)"""

    SURFACES = {
        "gw_write.py": ["create", "set-status", "add-link", "add-cite",
                        "remove-cite", "update-overview", "edit-section",
                        "delete-section", "append-turn", "supersede",
                        "apply"],
        "groundwork_read.py": ["overview", "outline", "section",
                               "element", "item", "turns", "term",
                               "citers"],
        "groundwork_consistency.py": ["sweep", "terms"],
        "groundwork_epic_coupling.py": ["check"],
    }

    def test_every_subcommand_help_is_substantive(self):
        for script, subs in self.SURFACES.items():
            for cmd in [[]] + [[s] for s in subs]:
                r = subprocess.run(
                    [sys.executable, str(HERE / script), *cmd, "--help"],
                    capture_output=True, text=True)
                where = f"{script} {' '.join(cmd)} --help"
                self.assertEqual(r.returncode, 0, where + r.stderr)
                self.assertGreater(
                    len(r.stdout), 200, f"{where}: thin help text")

    def test_dispatcher_help_maps_all_families(self):
        r = subprocess.run([sys.executable, str(HERE / "gw.py"),
                            "--help"], capture_output=True, text=True)
        self.assertEqual(r.returncode, 0, r.stderr)
        for family in ("read", "write", "check", "status", "consistency",
                       "coupling", "search", "graph"):
            self.assertIn(family, r.stdout)
        self.assertIn("remove-cite", r.stdout)  # op map stays current


class CheckerTests(unittest.TestCase):
    def setUp(self):
        self._tmp = tempfile.TemporaryDirectory()
        self.s = Scratch(self._tmp.name).baseline()
        self.root = self.s.root
        self.addCleanup(self._tmp.cleanup)

    def test_baseline_green(self):
        r = check(self.root)
        self.assertEqual(r.returncode, 0, r.stdout)

    def test_rules_21_to_24(self):
        # 21: duplicate sibling headings (draft artifact — rule is global)
        self.s.write("IDEA-0002", "idea", "captured",
                     idea_body("IDEA-0002").replace(
                         "## The Idea\n", "## The Idea\n\n## The Idea\n",
                         1))
        # 21 negative: same heading text under different parents is legal
        self.s.write("IDEA-0003", "idea", "captured",
                     "# IDEA-0003: Test idea\n\n## The Idea\n\n"
                     "### Detail\n\nA.\n\n## Spark Context\n\n"
                     "### Detail\n\nB.\n\n## Disposition\n\nPending.\n")
        # 22: placeholder in ratified vs draft
        self.s.write("SES-0002", "session", "closed",
                     session_body("SES-0002", decisions_produced="TBD."),
                     links="links:\n  relates-to: [DEC-0001]\n",
                     extra=SESSION_EXTRA)
        self.s.write("SP-0002", "spike", "draft",
                     spike_body("SP-0002", findings="TBD."),
                     links="links:\n  derives-from: [BG-0001]\n")
        # 23: session lacks back-link for a produced decision
        self.s.write("DEC-0002", "decision", "proposed",
                     decision_body("DEC-0002"),
                     links="links:\n  derives-from: [SES-0001]\n")
        # 24: H1 names another artifact's ID
        self.s.write("IDEA-0004", "idea", "captured",
                     idea_body("IDEA-0004",
                               first_line="# DEC-0001: Test idea"))
        r = check(self.root)
        self.assertEqual(r.returncode, 1, r.stdout)
        out = r.stdout
        self.assertIn("duplicate sibling heading ## 'The Idea'", out)
        self.assertNotIn("IDEA-0003-test.md", out)
        self.assertIn("placeholder text 'TBD.' (rule 22)", out)
        self.assertNotIn("SP-0002-test.md", out)
        self.assertIn("relates-to omits it (rule 23)", out)
        self.assertIn("body H1 names DEC-0001, not IDEA-0004", out)

    # SES-0077 (DEC-0402): rule 25 fails on off-schema fields
    # (promoted from WARN — the rollout sweep found zero legacy hits)
    def test_rule_25_field_schema_fails(self):
        self.s.write("SES-0006", "session", "open",
                     session_body("SES-0006"),
                     links="links:\n  relates-to: [DEC-0001]\n",
                     extra=("participant: tester\n"
                            "participant-role: sponsor\n"
                            "facilitator: facilitator-agent\n"
                            "transcript-fidelity: live\n"))
        r = check(self.root)
        self.assertEqual(r.returncode, 1, r.stdout)
        self.assertIn("rule 25", r.stdout)
        self.assertIn("transcript-fidelity", r.stdout)

    # SES-0077 item 9: rule 26 warns on missing required sections
    def test_rule_26_missing_sections_warn(self):
        p = self.s.write("IDEA-0002", "idea", "captured",
                         idea_body("IDEA-0002"))
        p.write_text(p.read_text().replace("## Disposition\n\nPending.\n",
                                           ""))
        r = check(self.root)
        self.assertEqual(r.returncode, 0, r.stdout)  # WARN severity
        self.assertIn("rule 26", r.stdout)
        self.assertIn("'Disposition'", r.stdout)

    # SES-0077 (DEC-0398/DEC-0399): checker agreement with the recheck
    def test_body_code_span_id_legal_overview_id_flagged(self):
        # A code-span ID in body prose is quotation — corpus stays green.
        self.s.write("IDEA-0002", "idea", "captured",
                     idea_body("IDEA-0002").replace(
                         "Thing.", "Quoting `DEC-9999` is legitimate."))
        r = check(self.root)
        self.assertEqual(r.returncode, 0, r.stdout)
        # The same unresolvable token in an overview is a violation —
        # backticks grant no exemption there (DEC-0398).
        p = self.s.write("IDEA-0003", "idea", "captured",
                         idea_body("IDEA-0003"))
        p.write_text(p.read_text().replace(
            "Test artifact IDEA-0003 for the structural guard tests.",
            "Overview quoting `DEC-9999` which does not resolve."))
        r2 = check(self.root)
        self.assertEqual(r2.returncode, 1, r2.stdout)
        self.assertIn("references unknown artifact DEC-9999", r2.stdout)


if __name__ == "__main__":
    unittest.main(verbosity=2)
