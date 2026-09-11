# Arc01: Contracts and Design

Status: active; Slice03 open and ready for CC; Slice01 handoff held pending the
reviewed and accepted metadata contract.

Planning remains in this worktree. Source reads and future implementation or
validation use `.worktrees/project-status-feature` on `feature/project-status`,
as specified in the project plan; CC's initial planning directory is not the
implementation working directory.

## Capability

Turn the operator's decisions, original ODM research/design, Rootstock trial,
and Lykn consumer cases into an implementable contract. Read [project-plan.md](../project-plan.md) first.
This arc leaves stable semantics, field responsibilities, portability and
upgrade boundaries, and acceptance cases for implementation and UAT.

## Slice breakdown

| Slice | Scope | Dependencies | State |
| --- | --- | --- | --- |
| slice03-planning-metadata-contract | Define prospective metadata for all planning-document roles, document/schema version identity, field ownership, relationships, compatibility and status projection from ODM research | Accepted operator requirements and preserved ODM inputs; unresolved D-01–D-06 details are proposal outputs | Open; [Slice03 open set](slice03-planning-metadata-contract/slice-plan.md) ready for CC |
| slice01-status-contract | Revise the status model, hierarchy, evidence and roll-up semantics against the metadata contract; reconcile ODM, Rootstock and Lykn cases | Slice03 accepted; existing project decisions and R-01 | Existing open set held for reevaluation |
| slice02-toolkit-and-acceptance-design | Specify local-copy distribution/upgrade mechanics, renderer/validator command contracts, test matrix, UAT intake and source/package impact map | Slice03 and Slice01 verified and design accepted | Planned; open set written when next |

The design brief is an input, not an approved schema. Resolve shared schema
dialect, identity and metadata representation in Slice03, before Slice01 depends
on them. Slice02 resolves runtime and command mechanics using both contracts
and current dependency evidence. This supersedes the earlier placement of schema
dialect in Slice02, which would have left upstream contracts underspecified.
Keep design judgment with the coordinating context and operator.

## Composition and exit

Operator Q-03 correction (2026-09-10): Slice01 must revise the flattened
project slice ratio to equally weighted planned arcs with fractional arc
contributions, following the
[progress decision](slice01-status-contract/artifacts/progress-decision.md).
The revision also includes R-01. Slice02 must carry the coverage table and
worked hierarchical examples into its source/package impact map as mandatory
guide content. The earlier two-slice sufficiency assessment is superseded by the 2026-09-11
metadata expansion. Preserve existing slice identities; dependency order is now
Slice03 metadata design → resumed Slice01 status contract → Slice02 toolkit design.

[ledger.md](ledger.md) checks that the three slices agree: each field needed by a
view has a defined source and validation rule, each promised validator behavior
has an executable acceptance case, and each Lykn requirement has an adoption
or UAT check. Record port-lane/lessons disposition and unresolved questions.
Arc01 close must make Arc02 implementable without re-inventing the contracts.

## Manual maintenance design requirement — 2026-09-11

Slice03 must specify field ownership and manual-edit invariants; Slice01 must
specify status-JSON reconciliation; Slice02 must map the chapters and executable
maintenance scenarios in [the notes](../artifacts/metadata-maintenance-notes.md)
to source/package deliverables and Lykn UAT. D-02 separation is accepted;
versioning remains open. This extends v1.3's ODM design scope without changing
the new dependency order.

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

### v1.3 — 2026-09-11

Operator's pre-handoff ODM reevaluation expands Arc01 from status-only contracts
to planning metadata plus traceable projections. Added planned Slice03 before
resumed Slice01, preserving existing identities; Slice02 consumes both contracts
and inventories original ODM visual assets. Read the project-level source index
and reevaluation first. No new CC assignment is opened during operator discussion.


### v1.4 — 2026-09-11

Recorded the accepted work-origin/source separation and mandatory manual-maintenance
guide design across the three slices, with packaged-guide and Lykn scenarios.

### v1.5 — 2026-09-11

Operator clarified skill/document/schema version axes and broadened metadata scope
to all planning-document roles. Slice03 inventories common and role-specific
metadata, own document histories and named-schema identity; Slice02 carries their
manual maintenance and compatibility procedures into the guide/package design.

### v1.6 — 2026-09-11

Packet review moved shared schema dialect/identity decisions into Slice03 before
the status-contract revision. Runtime/command design stays in Slice02. Refreshed
brief and historical artifact notices distinguish scope updates from a completed
contract rewrite. No CC open set or schema implementation is claimed.

### v1.7 — 2026-09-11

Opened the planned Slice03 metadata-contract open set at operator request. Replaced
its discussion prerequisite with proposal work against accepted requirements and
preserved sources; retained the Slice03 → Slice01 → Slice02 dependency sequence.
