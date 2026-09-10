# Arc01: Contracts and Design

Status: active; Slice01 open for contract design.

Planning remains in this worktree. Source reads and future implementation or
validation use `.worktrees/project-status-feature` on `feature/project-status`,
as specified in the project plan; CC's initial planning directory is not the
implementation working directory.

## Capability

Turn the operator's decisions, Rootstock trial, and Lykn consumer cases into
an implementable contract. Read [project-plan.md](../project-plan.md) first.
This arc leaves stable semantics, field responsibilities, portability and
upgrade boundaries, and acceptance cases for implementation and UAT.

## Slice breakdown

| Slice | Scope | Dependencies | State |
| --- | --- | --- | --- |
| slice01-status-contract | Define the status data model, hierarchy, evidence and roll-up semantics; reconcile Rootstock and Lykn cases | Project decisions; initial reconnaissance | Open set present |
| slice02-toolkit-and-acceptance-design | Specify local-copy distribution/upgrade mechanics, renderer/validator command contracts, test matrix, UAT intake and source/package impact map | Slice01 verified and design accepted | Planned; open set written when next |

The initial design brief is a seed for Slice01, not an approved schema. Resolve
runtime and schema dialect decisions using current source/dependency evidence
in Slice02. Keep design judgment with the coordinating context and operator.

## Composition and exit

Operator Q-03 correction (2026-09-10): Slice01 must revise the flattened
project slice ratio to equally weighted planned arcs with fractional arc
contributions, following the
[progress decision](slice01-status-contract/artifacts/progress-decision.md).
The revision also includes R-01. Slice02 must carry the coverage table and
worked hierarchical examples into its source/package impact map as mandatory
guide content. The current slice sequence remains sufficient.

[ledger.md](ledger.md) checks that the two slices agree: each field needed by a
view has a defined source and validation rule, each promised validator behavior
has an executable acceptance case, and each Lykn requirement has an adoption
or UAT check. Record port-lane/lessons disposition and unresolved questions.
Arc01 close must make Arc02 implementable without re-inventing the contracts.

## Version history

### v1.0 — 2026-09-06

Opened for Project06. Two bounded design slices precede implementation; the
first consumes this session's inspected-source and consumer-shape notes.

### v1.1 — 2026-09-06

Applied the operator's dedicated feature-worktree route to the arc and active
slice. Contract-design scope and slice sequence are unchanged.

### v1.2 — 2026-09-10

Applied the operator's Slice01 progress correction and required coverage-guide
content. Slice01 stays open for the bounded contract/case revision; Slice02
inherits the guide/package requirement. No additional arc or premature closure.
