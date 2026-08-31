# Cross-Cutting Concern Map

```yaml
project: project02-collab-breakout
arc: arc05-implementation-plan
slice: slice01-implementation-surface-map
status: proposed-done
source-files-edited: false
```

## Scope

This map carries support asset, adapter, versioning, component-boundary,
memory, source/package/release gates, and CCDP separation concerns into
Slice02 without turning them into unplanned source edits.

## Cross-Cutting Rows

| Concern | Accepted owner | Current source surface | Slice02 input |
|---------|----------------|------------------------|---------------|
| source/package/release gates | `engineering-methods`, plus mandatory per-component contract fields. | Project01 close, `README.md`, `Makefile`, `package-path-exceptions.tsv`, `scripts/check-package-paths`, `scripts/check-skill-description.sh`. | Plan `engineering-methods/guides/06-source-package-release-gates.md` and require fields in every component contract. |
| Package/source contract per component | Every accepted component. | Current monolithic `CF_FILES`, README package wording, and package checker exceptions. | Each component file plan must state source path, package path, package-local links, zip root, README route, `SKILL.md` route, Makefile impact, generated zip behavior, validation, owner, and version-history.md. |
| Agent terminology adapter | `agent-coordination`. | `SKILL.md` Notes for Codex, `docs/PROJECT-MANAGEMENT.md`, `templates/LEDGER-DISCIPLINE.md`, and `docs/SUBAGENT-DELEGATION-POLICY.md`. | Plan direct terminology in `agent-coordination/SKILL.md` plus local notes only where standalone use requires them. |
| Delegation and context packets | `agent-coordination`. | Current source has delegation policy but not full context-packet/result-integration guides. | Plan `01-when-to-delegate.md`, `02-context-packets.md`, `03-result-integration.md`, and `04-anti-patterns.md`; mark new prose need. |
| Support asset: ledger template | `work-verification`. | `templates/LEDGER-DISCIPLINE.md`. | Decide whether it remains both guide and template or is split into guide plus copied template. |
| Support asset: contribution ticket template | `contribution-style`. | `templates/CONTRIBUTION-TICKET.md`. | Package under `contribution-style/templates/CONTRIBUTION-TICKET.md` with package-local link from guides. |
| Support asset: PM worked example | `project-management`. | `docs/pm/09-worked-example-odm.md`. | Plan under `project-management/examples/01-worked-example-odm.md` per accepted layout. |
| Support asset: PM anti-patterns | `project-management`. | `docs/pm/07-anti-patterns.md`. | Plan as PM guide, not standalone package. |
| Component versioning | Every accepted component. | Top-level `SKILL.md` has version; source docs have embedded Version History; current standalone sibling `version-history.md` exists only as `docs/pm/version-history.md`. | Plan component `SKILL.md` version plus sibling `version-history.md` for all eight components. |
| component-boundary-analysis | `engineering-methods`. | No exact current source file; accepted target is `engineering-methods/guides/05-component-boundary-analysis.md`. | Treat ontology critique as reusable guide input, not standalone component. |
| memory admission | Deferred future research. | No Project02 source file; visible only as deferred accepted non-component decision. | Keep deferred; do not create Project02 component or package plan. |
| CCDP separation | CCDP package owner outside Project02 component set; `engineering-methods` records gate. | `README.md`, `Makefile`, `protocols/ccdp/`, `ccdp.zip`, `scripts/check-ccdp-package`. | Preserve protocol distribution boundary; no accepted component should bundle CCDP source. |

## Adapter Boundaries

`agent-coordination` replaces the earlier narrow delegation surface and owns
role language, delegation decisions, context-packet discipline, and result
integration. Source/package reader-mode language is a release gate owned by
`engineering-methods`, but each component still needs a local package/source
contract.

## Deferred And Non-Component Boundaries

- Memory admission is deferred future research.
- CCDP remains a separate protocol distribution.
- Component maintenance is not a standalone component; component versioning is
  `SKILL.md` version plus sibling `version-history.md`.
- Ontology critique is implemented, if accepted in later planning, as
  `engineering-methods/guides/05-component-boundary-analysis.md`.

No source edits are authorized by this cross-cutting concern map.
