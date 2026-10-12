# Arc01 — Baseline and Evidence

## Capability and authority

Deliver a reproducible preservation baseline, migration and claim/source
inventories, inherited-gap dispositions, and an accepted scope/evaluation
contract for CHCD design. This is the first capability in the
[project roadmap](../project-plan.md); [the arc ledger](ledger.md) governs its
composition. Arc01 establishes evidence and design inputs; Arc02 makes the
detailed generalized-protocol and compatibility design decisions.

Opened by the Operator on 2026-10-09. Status: **active**. Current slice:
[Slice01 — Baseline and Migration Inventory](slice01-baseline-and-migration-inventory/slice-plan.md),
open with its initial CC prompt ready for Operator relay. No execution or
acceptance has occurred. Two-Contributor Workflow: Sofie is CDC; CC is the
separate context receiving that prompt, not yet identified. No CRC or
Expedited Mode is enabled.

## Scope and boundaries

Inspect the pinned source tree, publication/build routes, existing corpus and
declared readiness gaps. Verify the sources behind existing and proposed
claims, including the limits of architecture-specific evidence. Preserve the
project's generalization notes and settled naming/compatibility decisions:
CHCD Protocol, `chcdp` paths, legacy CCDP names supported with deprecation in
0.3 and removed from protocol support in 0.4; archive and redirects retained.

Source checkout: `/Users/oubiwann/lab/billosys/ai-engineering` on `main`.
Initial baseline: `dffa504e851b03b8e4746f1941068e4cc850b612`.
Planning: the existing `.worktrees/planning/project12-chcd-protocol/` tree.
All durable evidence belongs to its producing slice's `artifacts/` directory.
Consume prior slice artifacts directly with exact identities; do not duplicate
them into a competing arc-level registry.

No source copy, rename, schema implementation, assembler changes, guide
rewrites, redirect deployment or publication belongs to this arc. Findings
produce evidence and scoped decisions, not opportunistic repairs. New factual
research requires primary-source verification; legacy link-check statements
and historical acceptance are not current verification.

## Slice roadmap and dependencies

| Slice | Capability | Dependencies and downstream use |
|---|---|---|
| slice01-baseline-and-migration-inventory | Pin tracked bytes and modes; classify legacy-name surfaces and build/publication routes; explain guide divergence; enumerate inherited gaps | Opens now; bounds all later evidence work and Arc03 copy preservation |
| slice02-existing-claims-and-source-review | Map existing specification/guide claims to references; check normative sources and supported claims; explicitly record unsupported, stale and inaccessible evidence | Accepted Slice01 scope; establishes claim/source coverage for Slice03 and Arc02 |
| slice03-model-and-comparison-evidence | Investigate non-LLM and multi-model requirements, exact JEPA/Jev/Laya referents, and protocol comparisons; test whether cited limitations generalize | Slice02 claim map; supplies evidence for Arc02 design and Arc04 guide |
| slice04-readiness-and-design-inputs | Reconcile inventories, inherited gaps, source results and compatibility questions into accepted scope, preservation/publishing policy and concrete evaluation cases | Accepted Slices01–03; gates detailed Arc02 work |

Only Slice01 is opened. Size later slices against actual inventory and reading
volume before issuing prompts; split source-review work explicitly if needed,
retaining the full denominator and ownership of every claim. Slice04 establishes
design inputs and decisions within authority; it does not preempt Arc02's wire
contract design or reopen the agreed 0.3/0.4 schedule.

## Composition and exit

Arc01 is complete when the slice evidence composes into one navigable, pinned
input set: every baseline surface and inherited gap has a disposition/owner,
every relevant claim has source coverage or an explicit restriction, and the
remaining design questions have named decision owners and blocking scopes.
Blocked research must stay visible; acceptance cannot retain an unsupported
normative claim as established fact. Map results back to P12-01 through P12-10
without claiming future implementation rows complete.

CDC independently verifies CC evidence in each slice's `cdc-verification.md`.
At arc close, CDC assembles `closing-report.md`; a fresh independent context or
the Operator records the composition gate there with attribution. Child closure
alone does not establish arc composition. No close-set records are opened now.

## Version History

- 1.0 (2026-10-09): Opened Arc01 with four staged evidence capabilities and a
  bounded initial baseline/migration assignment, preserving later design authority.
