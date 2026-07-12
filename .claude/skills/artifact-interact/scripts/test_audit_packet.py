#!/usr/bin/env python3
"""Tests for the recall-audit judge-packet contract (SES-0077,
IDEA-0027). Pure stdlib — exercises groundwork_audit_packet.py without
the embedding stack. Run: python3 test_audit_packet.py
"""

import unittest

from groundwork_audit_packet import (JUDGE_INSTRUCTIONS, build_packet,
                                     rank_candidates)

ARTIFACT = {"id": "SES-0001", "title": "A session",
            "overview": "One overview.", "body": "## Purpose\nBody text."}
META = {"DEC-0001": ("decision", "accepted", "First decision"),
        "DEC-0002": ("decision", "accepted", "Second decision"),
        "DEC-0003": ("decision", "accepted", "Third decision")}


class RankingTests(unittest.TestCase):
    def test_orders_by_score_descending(self):
        best = {"DEC-0001": (0.2, "Purpose", "Context"),
                "DEC-0002": (0.9, "Purpose", "Decision"),
                "DEC-0003": (0.5, "Purpose", "Rationale")}
        ranked = rank_candidates(best, 3)
        self.assertEqual([d for d, _ in ranked],
                         ["DEC-0002", "DEC-0003", "DEC-0001"])

    def test_score_ties_break_by_id_deterministically(self):
        # Pre-fix, ties inherited database row order (IDEA-0027); the
        # contract is now score desc, ID asc — insertion order must not
        # matter.
        best_a = {"DEC-0003": (0.5, "P", "C"), "DEC-0001": (0.5, "P", "C"),
                  "DEC-0002": (0.5, "P", "C")}
        best_b = dict(reversed(list(best_a.items())))
        want = ["DEC-0001", "DEC-0002", "DEC-0003"]
        self.assertEqual([d for d, _ in rank_candidates(best_a, 3)], want)
        self.assertEqual([d for d, _ in rank_candidates(best_b, 3)], want)

    def test_k_truncates(self):
        best = {f"DEC-{i:04d}": (float(i), "P", "C") for i in range(1, 30)}
        self.assertEqual(len(rank_candidates(best, 15)), 15)


class PacketTests(unittest.TestCase):
    def packet(self):
        best = {"DEC-0002": (0.91234, "Purpose", "Decision"),
                "DEC-0001": (0.5, "Transcript", "Context")}
        return build_packet(ARTIFACT, {"DEC-0003"},
                            rank_candidates(best, 15), META)

    def test_artifact_travels_in_packet(self):
        art = self.packet()["artifact"]
        self.assertEqual(art["id"], "SES-0001")
        self.assertEqual(art["title"], "A session")
        self.assertEqual(art["overview"], "One overview.")
        self.assertIn("Body text.", art["body"])

    def test_candidates_carry_rank_title_and_rounded_score(self):
        cands = self.packet()["candidates"]
        self.assertEqual([c["rank"] for c in cands], [1, 2])
        self.assertEqual(cands[0]["id"], "DEC-0002")
        self.assertEqual(cands[0]["title"], "Second decision")
        self.assertEqual(cands[0]["score"], 0.912)
        self.assertEqual(cands[0]["matched_artifact_section"], "Purpose")
        self.assertEqual(cands[0]["matched_decision_section"], "Decision")

    def test_considered_is_sorted_list(self):
        p = build_packet(ARTIFACT, {"DEC-0009", "DEC-0001"}, [], META)
        self.assertEqual(p["considered"], ["DEC-0001", "DEC-0009"])

    def test_unknown_candidate_title_defaults_empty(self):
        p = build_packet(ARTIFACT, set(),
                         [("DEC-9999", (0.4, "P", "C"))], META)
        self.assertEqual(p["candidates"][0]["title"], "")

    def test_judge_instructions_demand_identity_self_check(self):
        self.assertIn("artifact.id matches", JUDGE_INSTRUCTIONS)
        self.assertIn("report the mismatch", JUDGE_INSTRUCTIONS)
        self.assertEqual(self.packet()["judge_instructions"],
                         JUDGE_INSTRUCTIONS)


if __name__ == "__main__":
    unittest.main(verbosity=2)
