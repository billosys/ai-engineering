# Slice01: Status Contract

Status: open; CC handoff held for operator-requested ODM reevaluation (2026-09-11).
The earlier initial-reconnaissance-only input boundary is superseded. Consume
[the project-level reevaluation](../../artifacts/odm-reevaluation.md) and the
planned Slice03 metadata contract before resuming the status revision.

Worktree routing: write this slice's planning artifacts here on `planning`.
Read source skills and packaging from
`/Users/oubiwann/lab/billosys/ai-engineering/.worktrees/project-status-feature`
on `feature/project-status`. Later implementation and package gates run there,
not in main. This routing update does not add implementation to this slice.

## Goal and inputs

Define an implementable, general data contract for Saga, project, and arc
status. Read the [project plan](../../project-plan.md), [arc plan](../arc-plan.md),
[design brief](artifacts/design-brief.md), and
[reconnaissance](artifacts/source-reconnaissance.md) in that order.

## In scope

2026-09-10 scope clarification: the
[operator's progress decision](artifacts/progress-decision.md) replaces the
draft-1 flattened project ratio. Revise project/arc aggregation, cases and
required guide content accordingly, together with CDC R-01. The original scope
below still applies; explicit mixed-hierarchy policies remain part of design.

- Explicit common and scale-specific fields, required/optional/null rules,
  entity identity, relationships, schema identity and compatibility policy.
- Status/evidence/closure/progress distinctions, unknown denominators and
  parent/child summary responsibility; no automatically inherited acceptance.
- Saga as repository collection with generic status filenames; optional lower
  pages and direct project slices without manufactured arc wrappers.
- Source-to-contract mapping from ODM planning metadata and its accepted research
  dispositions into status records, then for Rootstock, including deliberate removal or
  optionalisation of private/domain-specific material and port-lane/lessons.
- Lykn case walkthroughs including historical archives, decimal IDs, research,
  source-branch evidence, and acceptance pending after mechanical verification.
- A draft positive/negative fixture specification and explicit unresolved
  decisions for Slice02. Field contracts describe presentation needs without
  putting CSS classes or arbitrary pre-escaped HTML into the core data model.

## Out of scope

Executable implementation, changes to the source skill or Makefile, copying
private JSON into the public repo, edits to either consumer, executing hardware
instructions, adjudicating Lykn's current software completion, or opening later
slice work prematurely.

## Deliverables and verification

Artifacts live in this slice's `artifacts/`. Produce `status-contract.md` and
`contract-cases.md`; amend the design brief only with disclosed decisions.
Verify each [ledger](ledger.md) row by field-level mapping and worked record
examples against inspected inputs. Check local links and diff whitespace.
Record assumptions and questions explicitly; review accepted semantics with
the operator before implementation. Closing evidence is written only after
the work and remains proposed-done until independent verification.

## Version history

### v1.0 — 2026-09-06

Opened from the accepted project charter and live Rootstock/Lykn reconnaissance.

### v1.1 — 2026-09-06

Updated source-reference and future implementation routes for the operator's
feature worktree. Planning outputs and acceptance criteria are unchanged.

### v1.2 — 2026-09-10

Incorporated the operator's Q-03 correction and coverage-guide requirement into
the existing contract/case revision. S-03's check now includes the four-arc
examples and denominator behavior; no existing acceptance criterion removed.

### v1.3 — 2026-09-11

Operator held the CC handoff to recover ODM research and metadata decisions.
Added original ODM evidence and the planned Slice03 metadata contract as inputs;
retain all existing rows, Q-03 and R-01. Detailed planning-metadata design has its
own slice rather than silently inflating this status-contract assignment.
