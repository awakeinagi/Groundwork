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


if __name__ == "__main__":
    unittest.main(verbosity=2)
