# Work Verification Version History

## Version 1.1.0 - 2026-09-04

Split the work-verification guide surface into five selective-load guides:
ledger discipline, evidence strength, row closure, silent-drop checks, and
independent verification. Retained `templates/LEDGER-DISCIPLINE.md` as the full
protocol and copyable table support asset, with cross-routes from the template
to the focused guide set.

## Version 1.0.1 - 2026-09-04

Normalized the component history into this sibling file for Arc08 Slice05.
The ledger-discipline protocol remains the live guide/template payload; its
former embedded history is preserved below as component lineage. Future changes
to `SKILL.md`, `guides/`, `templates/`, or `examples/` for this component
should be recorded here.

## Ledger Discipline Lineage

### Version 2.4 - September 2026

Routed CC, CDC, and Operator terminology to the methodology source of truth
instead of carrying local role definitions in the ledger protocol. The ledger
separation rule is unchanged: the closer of a row remains structurally
separate from its verifier.

### Version 2.3 - August 2026

Synchronized with `PROJECT-MANAGEMENT.md` v2.5. Durable artifacts produced by a
slice now default to `sliceNN-<slug>/artifacts/`, with an operator-recorded
override allowed. CC evidence should point to that artifact home when durable
outputs are part of a ledger row, and CDC now verifies artifact placement during
slice close.

### Version 2.2 - August 2026

Updated the ledger layout to match `PROJECT-MANAGEMENT.md` v2.4: every scale
now gets a dedicated sibling `ledger.md` file. Project ledgers live beside
`project-plan.md`, arc ledgers live beside `arc-plan.md`, and slice ledgers
continue to live beside `slice-plan.md`. This replaces the v2.0/v2.1
transitional layout where arc and project rows lived as sections inside their
plan files. The ledger mechanics are unchanged.

### Version 2.1 - August 2026

Updated the slice-ledger path example to match
[`../project-management/guides/PROJECT-MANAGEMENT.md`](../project-management/guides/PROJECT-MANAGEMENT.md)
v2.2: planning artifacts now default to the orphan `planning` branch/worktree
under `projectNN-<slug>`, not an implementation-branch `docs/design-vX.Y.Z`
tree. Also renamed the referenced slice plan-of-record from `slice-doc.md` to
`slice-plan.md`. The ledger protocol itself is unchanged.

### Version 2.0 - June 2026

Extended the discipline from slice-only to all three scales: slice, arc, and
project. Restructured into a scale-free invariant spine followed by three
self-contained sections. Section A is the prior slice protocol, reframed as
the leaf scale and otherwise unchanged. Sections B and C are new: the arc and
project tiers, with composition rows reproduced at scale, a doer/gatekeeper
role shift, and remediation-not-iteration in place of the fix-loop cap.

Per the layout decision at the time, the arc and project ledgers lived as
sections in `arc-plan.md` and `project-plan.md` and closed in companion
`closing-report.md` files. That embedded-section layout was superseded by
v2.2, which gives every scale its own sibling `ledger.md`. Added lineage
grounding the multi-scale extension in assurance cases / GSN, the V-model,
and stage-gate reviews, alongside the slice tier's corrective-action heritage.

### Version 1 - June 2026

The original slice-scoped protocol: grep-verifiable rows, evidence-backed
closure, the CC/CDC separation, the five-iteration cap, and the
silent-drop/spec-softening/partial-adoption failure modes. Terminology aligned
to the methodology: the level-1 ledger-bearing unit is slice, not milestone,
and the ledger path is `arcNN-<slug>/sliceNN-<slug>/ledger.md`.
