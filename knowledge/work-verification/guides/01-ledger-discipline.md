# Ledger Discipline

Load this guide at the start of any ledgered project, arc, or slice. It gives
the scale-free verification spine: every acceptance claim is a row, every row
has a reproducible verification route, the doer reports disposition, and an
independent reviewer checks the evidence before the unit advances.

For the full protocol and copyable table templates, use
[`../templates/LEDGER-DISCIPLINE.md`](../templates/LEDGER-DISCIPLINE.md). For a
narrower lookup, use the companion guides for
[evidence strength](./02-evidence-strength.md),
[row closure](./03-row-closure.md),
[silent-drop checks](./04-silent-drop-checks.md), and
[independent verification](./05-independent-verification.md).

## What The Ledger Is

Ledger discipline is a verification practice adapted from defect-register and
corrective-action traditions: nuclear power, aviation, surgery, clinical
trials, food safety, financial audit, and human spaceflight. Its useful part is
not the register alone. It is the closure culture around the register:
observable rows, explicit closure criteria, evidence, separation of doing from
verifying, and a final row walk.

The short version:

1. Enumerate every acceptance criterion for the unit of work as a ledger row.
2. Give each row a verification command, grep, test, demonstration, or
   witnessable check.
3. Work against the ledger while preserving scope; amend openly if the ledger
   is wrong.
4. Close every row as `done`, `deferred`, or `no-op`.
5. Attach evidence with an explicit strength level.
6. Have an independent reviewer reproduce the evidence before treating the
   unit as closed.

## Scale-Free Spine

The same discipline applies at three scales:

| Scale | What rows assert | Closure question |
|---|---|---|
| Slice | Acceptance criteria for one mergeable execution unit. | Did this slice deliver every promised row, or explicitly defer/no-op it? |
| Arc | Closed child slices, slice composition into the arc capability, and dispositioned bubble-up findings. | Do the slices compose into the capability the arc promised? |
| Project | Closed child arcs, arc composition into the project definition of done, and dispositioned arc findings. | Do the arcs compose into the project definition of done? |

The higher scales are the recomposition side of the planning loop. Planning
decomposes a project into arcs and slices; ledgers discharge those claims from
the leaves upward. At arc and project scale, composition rows must be
demonstrated at that scale. A pointer to closed children is useful attestation,
but it is not proof that the children compose.

## Ledger Format

A ledger is a table with one row per observable acceptance criterion.

| Column | Meaning |
|---|---|
| ID | Unique row identifier. |
| Criterion | One observable claim. |
| Verify | Command, grep, test, or demonstration that checks the claim. |
| Significance | `serious`, `correctness-grade`, or `polish`. |
| Origin | Plan, review, bubble-up, or other source of the row. |
| Status | `open`, `done`, `deferred`, or `no-op`. |
| Evidence | Evidence pointer plus strength. Empty while open. |
| Notes | Deferred reasons, no-op rationales, caveats, or reviewer notes. |

## Rules

1. Every row reaches a final status before the unit advances.
2. `done` requires evidence.
3. `deferred` requires a reason and a re-entry condition.
4. `no-op` requires a rationale.
5. Missing rows are ledger bugs, not harmless omissions.
6. Evidence must be independently reproducible.
7. The closer is structurally separate from the verifier.

## Scale Adaptation

| Axis | Slice | Arc | Project |
|---|---|---|---|
| Rows assert | Acceptance criteria. | Slices closed, slices compose, findings dispositioned. | Arcs closed, arcs compose, findings dispositioned. |
| Evidence kind | Grep, unit test, local demonstration. | Integration demonstration, plus child-ledger pointers. | System/acceptance demonstration, plus arc-ledger pointers. |
| Doer/verifier | CC implements, CDC verifies. | CDC assembles, fresh context or operator gates. | Planner assembles, operator plus fresh context gates. |
| Remediation | Five-iteration fix loop within the slice. | Failed composition spawns a remediation slice. | Failed definition of done spawns a remediation arc or roadmap re-scope. |
| Cadence | `ledger.md` beside `slice-plan.md`. | `ledger.md` beside `arc-plan.md`. | `ledger.md` beside `project-plan.md`. |

## When To Load Companions

Load [Evidence Strength](./02-evidence-strength.md) when deciding whether a
claim is only proposed-done or independently verified. Load
[Row Closure](./03-row-closure.md) before writing a closing report or CDC
verification. Load [Silent-Drop Checks](./04-silent-drop-checks.md) when
checking scope-as-specified against scope-as-delivered. Load
[Independent Verification](./05-independent-verification.md) when assigning or
performing the verifier role.
