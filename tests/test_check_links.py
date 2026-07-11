"""Tests for check_links.py rule 20 (typed Uses: lines — DEC-0299,
DEC-0306, DEC-0309; SPEC-design-elements).

Each test builds a minimal synthetic Groundwork corpus in tmp_path —
valid under rules 1-19 — and varies only the rule-20-relevant shape,
isolating checker behavior from the real corpus state.
"""

import subprocess
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parents[1]
CHECKER = REPO / "tools" / "check_links.py"
CANONICAL = (REPO / ".claude" / "skills" / "artifact-interact" /
             "scripts" / "check_links.py")


def _write(root, rel, text):
    p = root / rel
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(text, encoding="utf-8")


def build_corpus(root, alpha_uses="Uses: BetaSvc.B-1 (interface)",
                 alpha_depends="[CMP-0002]", alpha_implements=True,
                 beta_range=False, with_stub=False):
    """Two-component corpus; AlphaSvc's Uses:/depends-on vary per test.

    alpha_uses: full Uses: line for AlphaSvc; '' omits the line.
    """
    _write(root, "docs/goals/BG-0001-test-goal.md", """---
id: BG-0001
type: business-goal
title: "Test Goal"
status: approved
overview: >-
  Synthetic fixture goal for checker tests.
---

## Purpose

A goal.

## Derived Work

- ST-0001
""")
    _write(root, "docs/stories/ST-0001-test-story.md", """---
id: ST-0001
type: story
title: "Test Story"
status: approved
overview: >-
  Synthetic fixture story for checker tests.
links:
  derives-from: [BG-0001]
---

## Purpose

A story.

## Component Impact

Handled by CMP-0001 and CMP-0002.
""")
    impl = "Implements: ST-0001\n" if alpha_implements else ""
    uses = f"{alpha_uses}\n" if alpha_uses else ""
    _write(root, "docs/components/CMP-0001-alpha.md", f"""---
id: CMP-0001
type: component
title: "Alpha"
status: approved
overview: >-
  Synthetic fixture component Alpha for checker tests.
links:
  derives-from: [ST-0001]
  depends-on: {alpha_depends}
---

## Purpose

Alpha component.

## Design Elements

### AlphaSvc (service)

{impl}{uses}
- `AlphaSvc.A-1` — does a thing.
- `AlphaSvc.A-2` — does another thing.

### AlphaVal (value)

Implements: ST-0001
Uses: none

- `AlphaVal.D-1` — a value schema.
""")
    beta_items = ("- `BetaSvc.B-1..B-3` — three operations.\n" if beta_range
                  else "- `BetaSvc.B-1` — an operation.\n")
    _write(root, "docs/components/CMP-0002-beta.md", f"""---
id: CMP-0002
type: component
title: "Beta"
status: approved
overview: >-
  Synthetic fixture component Beta for checker tests.
links:
  derives-from: [ST-0001]
  depends-on: []
---

## Purpose

Beta component.

## Design Elements

### BetaSvc (service)

Implements: ST-0001
Uses: none

{beta_items}""")
    if with_stub:
        _write(root, "docs/components/CMP-0003-stub.md", """---
id: CMP-0003
type: component
title: "Stub"
status: draft
overview: >-
  Synthetic non-conforming draft stub with no element structure.
links:
  derives-from: [ST-0001]
  depends-on: [CMP-0002]
---

## Purpose

A draft stub.

## Pending — Design Elements

Blocked on upstream work.
""")


def run(root, *flags):
    return subprocess.run(
        [sys.executable, str(CHECKER), *flags, str(root)],
        capture_output=True, text=True)


def test_valid_explicit_qualifier(tmp_path):
    build_corpus(tmp_path)
    r = run(tmp_path)
    assert r.returncode == 0, r.stdout
    assert "OK:" in r.stdout


def test_uses_none_with_empty_depends(tmp_path):
    build_corpus(tmp_path, alpha_uses="Uses: none", alpha_depends="[]")
    r = run(tmp_path)
    assert r.returncode == 0, r.stdout


def test_multi_target_mixed_qualifiers(tmp_path):
    build_corpus(tmp_path, alpha_uses=(
        "Uses: BetaSvc.B-1 (interface), AlphaVal.D-1 (implementation)"))
    r = run(tmp_path)
    assert r.returncode == 0, r.stdout


def test_omitted_qualifier_defaults_to_interface(tmp_path):
    build_corpus(tmp_path, alpha_uses="Uses: BetaSvc.B-1")
    r = run(tmp_path)
    assert r.returncode == 0, r.stdout


def test_missing_uses_line_blocks(tmp_path):
    build_corpus(tmp_path, alpha_uses="", alpha_depends="[]")
    r = run(tmp_path)
    assert r.returncode == 1
    assert "lacks a Uses: line" in r.stdout
    assert "FAIL" in r.stdout


def test_unresolvable_element_target(tmp_path):
    build_corpus(tmp_path, alpha_uses="Uses: GammaSvc.C-1 (interface)",
                 alpha_depends="[]")
    r = run(tmp_path)
    assert r.returncode == 1
    assert "resolves to no element" in r.stdout


def test_unresolvable_item_target(tmp_path):
    build_corpus(tmp_path, alpha_uses="Uses: BetaSvc.B-9 (interface)")
    r = run(tmp_path)
    assert r.returncode == 1
    assert "defines no item B-9" in r.stdout


def test_unknown_qualifier(tmp_path):
    build_corpus(tmp_path, alpha_uses="Uses: BetaSvc.B-1 (runtime)")
    r = run(tmp_path)
    assert r.returncode == 1
    assert "unknown qualifier" in r.stdout


def test_elementless_stub_skipped(tmp_path):
    build_corpus(tmp_path, with_stub=True)
    r = run(tmp_path)
    assert r.returncode == 0, r.stdout


def test_projection_missing_depends_entry(tmp_path):
    build_corpus(tmp_path, alpha_depends="[]")
    r = run(tmp_path)
    assert r.returncode == 1
    assert "depends-on omits it" in r.stdout


def test_projection_unsupported_depends_entry(tmp_path):
    build_corpus(tmp_path, alpha_uses="Uses: none",
                 alpha_depends="[CMP-0002]")
    r = run(tmp_path)
    assert r.returncode == 1
    assert "supported by no element Uses: edge" in r.stdout


def test_intra_component_edge_needs_no_depends(tmp_path):
    build_corpus(tmp_path, alpha_uses="Uses: AlphaVal.D-1 (implementation)",
                 alpha_depends="[]")
    r = run(tmp_path)
    assert r.returncode == 0, r.stdout


def test_range_items_expand_for_resolution(tmp_path):
    build_corpus(tmp_path, alpha_uses="Uses: BetaSvc.B-2 (interface)",
                 beta_range=True)
    r = run(tmp_path)
    assert r.returncode == 0, r.stdout


def test_bare_element_target_resolves(tmp_path):
    build_corpus(tmp_path, alpha_uses="Uses: BetaSvc (test)")
    r = run(tmp_path)
    assert r.returncode == 0, r.stdout


def test_advisory_mode_demotes_to_warning_exit_zero(tmp_path):
    build_corpus(tmp_path, alpha_uses="", alpha_depends="[]")
    r = run(tmp_path, "--uses-advisory")
    assert r.returncode == 0, r.stdout
    assert "WARN" in r.stdout
    assert "lacks a Uses: line" in r.stdout
    assert "OK:" in r.stdout


def test_advisory_mode_does_not_mask_other_rules(tmp_path):
    build_corpus(tmp_path, alpha_implements=False)
    r = run(tmp_path, "--uses-advisory")
    assert r.returncode == 1
    assert "lacks an Implements: line" in r.stdout


def test_existing_rules_not_regressed(tmp_path):
    build_corpus(tmp_path, alpha_implements=False)
    r = run(tmp_path)
    assert r.returncode == 1
    assert "lacks an Implements: line" in r.stdout


def test_canonical_and_installed_copies_identical():
    assert CHECKER.read_bytes() == CANONICAL.read_bytes()
