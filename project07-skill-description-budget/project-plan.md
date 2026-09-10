---
project: project07-skill-description-budget
status: ready-for-review
depends-on: []
blocks: []
related: [Codex CLI skill metadata rendering]
---

# Skill Description Budget

Deliver a current description inventory, reliable length checks, and a workflow
that prepares LLM shortening proposals and applies only user-approved changes.
This is one slice, `slice01-inventory-and-tooling`, without an arc wrapper.
Inspect packaged source skills and the actual installed Codex catalog. Distinguish
per-description limits from the aggregate model-dependent catalog budget.

Completion requires reproducible measurements, real parser and workflow tests,
Make-backed checks, documented usage, and a concrete review packet. Applying the
proposed rewrites or changing installed plugins is a subsequent user decision.
No model-quality claim is made merely because a description is shorter.

Current baseline: main `c8909905`, planning `361cdc6f`. Inventory includes all
22 source skills and separately the 20-entry package list. The two source-only
skills stay under Project05's packaging scope. Fifteen refreshed proposals are
ready for review, not applied. Current live Codex evidence shows no shortening
after the separately approved Anthropic plugin removal. Existing version/history
gates remain part of verification; historical evidence is archived in the slice.

## Version History

- 1.2 (2026-09-10): Renumbered to project07 after synchronizing main and
  planning. Integrate tooling with upstream version gates and refresh inventory
  and unapplied proposals against the expanded source tree.
- 1.1 (2026-09-10): slice01 delivered inventory, YAML-aware tooling, live
  diagnostic, and 13 unapplied proposals. Added CI dependency installation after
  packaging integration review. Operator review/application remains separate.
- 1.0 (2026-09-10): Initial scope from the user's three requested outcomes.
