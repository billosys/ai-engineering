---
version: "1.0.0"
status: open
created: 2026-09-11
---

# Slice03: Planning-metadata contract

## Goal and authority

Produce a reviewable contract for prospective planning-document metadata and its
mapping into status data. This is the first work after the ODM research catch-up.
The operator requested this open set on 2026-09-11; the earlier blanket handoff
hold is superseded for this slice. Remaining design questions are assignment
outputs, not prerequisites to starting. Proposals still require review and
operator acceptance before dependent implementation.

Read the [project plan](../../project-plan.md) and [ledger](../../ledger.md), then
[arc plan](../arc-plan.md) and [ledger](../ledger.md), then this plan and
[slice ledger](ledger.md). The existing sequence is Slice03 → resumed Slice01 →
Slice02; numbering is preserved. Slice01 remains open and held pending the
accepted metadata contract. Its draft is evidence, not a prerequisite to close.

These bootstrap documents have content versions and end-of-document histories.
They do not claim conformance to the schemas this project has yet to define.

## Inputs

- [ODM reevaluation](../../artifacts/odm-reevaluation.md), including D-01–D-06,
  and [source index](../../artifacts/odm-source-index.md), including all nine
  immutable source snapshots and their provenance.
- [Accepted version model and remaining decisions](../../artifacts/versioning-decision.md).
- [Manual-maintenance notes](../../artifacts/metadata-maintenance-notes.md).
- Slice01's [design brief](../slice01-status-contract/artifacts/design-brief.md),
  [source reconnaissance](../slice01-status-contract/artifacts/source-reconnaissance.md),
  [progress decision](../slice01-status-contract/artifacts/progress-decision.md),
  [historical contract](../slice01-status-contract/artifacts/status-contract.md),
  [cases](../slice01-status-contract/artifacts/contract-cases.md), and
  [CDC review](../slice01-status-contract/cdc-verification.md).

Source skills/guides are read from
`/Users/oubiwann/lab/billosys/ai-engineering/.worktrees/project-status-feature`
on `feature/project-status`. Planning outputs stay in
`/Users/oubiwann/lab/billosys/ai-engineering/.worktrees/planning/project06-project-status`
on `planning`. Record actual revisions inspected; preserve unrelated work.

## In scope

1. Inventory maintained planning-document roles: project/arc/slice plans, ledgers,
   prompts, author closing reports, independent verification, decisions, research,
   notes and other authored artifacts. Define shared metadata and role-specific
   constraints without turning supporting documents into work units. Separate
   immutable imported evidence and unadopted legacy records from maintained records.
2. Propose schema dialect, named identity, exact instance markers, local resolution,
   pinned shared definitions and compatibility policy. Preserve the accepted skill,
   document and schema version axes. Resolve independent versus synchronized schema
   cadence as a recommendation with alternatives; explicitly reconcile draft Q-04's
   uniform status-format counter. Define document bump/history rules with examples.
   Do not invent independent guide/template/toolkit release sequences.
3. Define a field dictionary: meaning, type, applicability, required/optional/null/
   unknown semantics, owning record/actor, mutability, references, evidence, validation
   rule and status projection destination or explicit non-projection reason. Include
   stable identity versus locator, containment versus dependencies, work-origin versus
   authoring/source provenance, purpose/DoD, typed blocks/deferrals/lineage, named gates,
   scoped evidence and its current applicability, and coverage assertions.
4. Define the authority boundary between planning records and status projections,
   including reported-source adoption before frontmatter exists. Avoid dual manual
   authority. Specify the metadata support needed for R-01's structured child
   exclusions; Slice01 owns the final status-rule revision and case integration.
5. Disposition all nine ODM inputs and D-01–D-06 against current operator decisions.
   Preserve useful semantics and provenance; identify adapted, historical, deferred
   and rejected proposals with reasons. Separate accepted decisions from CC proposals.
6. Make the design usable manually: worked edits, dependent updates, version/history
   changes, validation expectations and evidence boundaries. Map the existing six
   chapter outlines and maintenance scenarios to concrete contract elements.

## Boundaries

This slice produces design documents and fictional worked examples. Production
schemas, validators, scripts, templates, shipped guides, package changes and metadata
adoption belong to later slices/arcs. Do not rewrite Slice01's packet, preserved ODM
copies, closed planning history, or Rootstock/Lykn. No ODM CLI/probes are required.
No new full literature review, runtime selection or renderer/visual inventory is
assigned here. Cite source locators and qualify research claims; independently check
primary sources only where a new load-bearing claim is used. Do not infer industry
validation from an ODM recommendation or treat its Rust implementation as authority.

Preserve accepted equal-arc progress and the 25%/12.5% examples, explicit unknowns,
separate delivery/verification/acceptance, local toolkit copies and lessons/port-lane
adjacent-link scope. Record unresolved mixed-hierarchy progress policy for Slice01;
do not silently choose a new denominator here.

## Deliverables

Durable output home is this slice's `artifacts/` directory:

- `planning-metadata-contract.md`: role inventory, field dictionary, schema and
  revision policy, ownership/projection map, invariants and numbered decision register.
- `odm-dispositions.md`: source/section-to-decision trace for all nine imports and
  D-01–D-06; downstream obligations and bounded deferrals with rationale/owner/re-entry.
- `metadata-contract-cases.md`: fictional records and positive/negative cases with
  stable IDs, expected outcomes, rule/ledger references and a coverage matrix.
- `manual-maintenance-outline.md`: chapter handoff and representative before/after
  procedures with exact proposed fields; distinguish contract expectations from
  commands that have not been implemented or chosen.
- `verification-record.md`: author checks, exact revisions, reproduction steps,
  case/field/decision/link coverage and limitations.

Create `closing-report.md` only when reporting the work. CDC owns subsequent
`cdc-verification.md`. Each newly authored document has its own content version and
history at the end, without falsely declaring adoption of a nonexistent schema.

## Acceptance and verification

The [ledger](ledger.md) is the row-level contract. At minimum, cases cover every
inventoried document role and each of the six observed Lykn project shapes, using
fictional examples. Include rename/reparent without identity loss; planned/discovered/
amendment independently of authored/imported; reference and cycle/exception policy;
child-set changes invalidating coverage; four known arcs with later JIT decomposition;
wrong-child/dangling/prose-only exclusions; a gate result becoming stale after revision
or environment change; imported provenance retained after local authorship; strict
unknown-field diagnostics without destructive rewriting; unsupported versions and
pinned shared-schema changes; document-only revisions versus deliberate schema upgrades.

Show old-instance/new-validator and new-instance/old-validator compatibility separately.
Examples must explain omitted, null, unknown and known-zero values. Demonstrate how
preservation and closed-history exclusions can be verified during later adoption.

Parse complete YAML/JSON examples with an available parser and identify snippets
that are intentionally partial. Check field references, identity links, arithmetic,
local Markdown links, all case IDs and the ledger/decision coverage matrix. Record
only checks actually run. These checks are not schema validation, runtime verification
or Lykn UAT. Do not create a throwaway validator as purported production evidence.

CC may report proposed-done with a complete recommendation packet while decisions
await operator review. Keep ledger rows open with author evidence pointers. CDC
independently reviews/reproduces document checks; operator acceptance resolves design
forks before closure and the resumed Slice01 assignment. Record a genuine scope gap
as a bubble-up with impact and recommendation, not silent omission or a new work unit.

## Version history

### 1.0.0 — 2026-09-11

Opened at operator request as the first post-research work. Converted pending design
forks into concrete proposal outputs, preserving review gates and the Slice01 hold.
