#!/usr/bin/env python3
"""Recall-audit judge-packet assembly (SES-0077, IDEA-0027).

Pure stdlib and model-free by design: groundwork_search.py computes the
similarity ranking and hands the raw results here, so the packet's
contract — field set, candidate shape, deterministic ordering — is
testable without the embedding stack (test_audit_packet.py).

The packet is machine-parsed by judge subagents; every change to its
shape is a contract change for the judge protocol documented in the
groundwork-design-session skill's semantic-search reference.
"""

JUDGE_INSTRUCTIONS = (
    "First confirm this packet's artifact.id matches the artifact you "
    "were assigned to audit; on a mismatch, stop and report the mismatch "
    "instead of judging. Then, for each candidate, judge whether it is "
    "BOTH (a) genuinely relevant to the artifact's content and (b) "
    "missing from consideration — the artifact should cite, reference, "
    "or consciously address it. Be strict: most retrieval candidates are "
    "noise; do not manufacture relevance; follow citation chains before "
    "flagging (a decision already carried by a cited decision's "
    "provenance is NOT missing). Candidate scores are cosine "
    "similarities — treat low-scoring tail candidates with extra "
    "suspicion. Report at most 4 findings ranked by importance (ID + "
    "why relevant + where to consider it), or exactly 'Nothing to add.' "
    "plus the closest near-miss and why it fails. Also report, "
    "separately and clearly labeled, any contract gap you notice while "
    "judging.")


def rank_candidates(best, k):
    """Top-k of {dec_id: (score, artifact_section, decision_section)}.

    Deterministic: score descending, then ID ascending — score ties no
    longer inherit database row order (IDEA-0027).
    """
    return sorted(best.items(), key=lambda x: (-x[1][0], x[0]))[:k]


def build_packet(artifact, considered, ranked, meta):
    """Assemble the judge context packet.

    artifact: dict with id/title/overview/body — the audited artifact
    travels IN the packet so judges never evaluate blind (IDEA-0027).
    ranked: rank_candidates() output. meta: {id: (atype, status, title)}.
    """
    candidates = []
    for i, (dec_id, (score, asect, dsect)) in enumerate(ranked):
        candidates.append({
            "rank": i + 1,
            "id": dec_id,
            "title": meta.get(dec_id, ("", "", ""))[2],
            "score": round(float(score), 3),
            "matched_artifact_section": asect,
            "matched_decision_section": dsect,
        })
    return {
        "artifact": artifact,
        "considered": sorted(considered),
        "candidates": candidates,
        "judge_instructions": JUDGE_INSTRUCTIONS,
    }
