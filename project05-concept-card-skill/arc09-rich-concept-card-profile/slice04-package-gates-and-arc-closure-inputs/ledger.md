# Slice04 Ledger

| ID | Criterion | Verify | Significance | Origin | Status | Evidence | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| S4-1 | Final repository-local gates pass after Arc09 source and regression work. | Run `make check-skills`, `make check-skill-versions`, `make check-package-paths`, and `git diff --check`; record warnings and exceptions. | serious | Arc09 exit criteria | open |  | Use Make-backed gates; do not weaken evidence. |
| S4-2 | Generated `concept-cards` package contains the Arc09 rich-profile surfaces. | Inspect `target/skills/concept-cards.zip` for entrypoint, version history, rich template, rich-profile example, affected guides, and review references. | serious | package gate | open |  | Package inspection must use freshly generated or verified-current archives. |
| S4-3 | `document-extraction` package shape is not silently changed by Arc09. | Inspect package contents or source/package diff for no unintended Arc09 coupling. | correctness-grade | scope boundary | open |  | Arc09 should remain `concept-cards`-owned. |
| S4-4 | Arc09 caveats are retained for closure. | Inspect final artifacts for the synthetic example's non-resolving traceability paths, historical Erlang wrapper finding, no semantic verification, and no runtime/admission claims. | serious | Slice03 caveats | open |  | Caveats should not be laundered into acceptance claims. |
| S4-5 | Arc09 ledger rows A9-5 and A9-6 have closure-ready evidence. | Inspect Arc09 ledger, Slice04 artifacts, and closing report inputs. | serious | arc closure | open |  | A9-4 is already CDC-verified; A9-5/A9-6 remain to close. |
| S4-6 | Slice04 produces Arc09 closure inputs and Arc10 handoff notes. | Inspect `arc-closure-inputs.md` and closing report for next action. | serious | Expedited Mode handoff | open |  | After CDC verifies Slice04, close Arc09 and open Arc10. |

Rows: 6. Open: 6. Done: 0. Deferred: 0. No-op: 0. Independent CDC verification: pending.
