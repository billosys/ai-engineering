# Source To Component Migration Plan

```yaml
project: project02-collab-breakout
arc: arc05-implementation-plan
slice: slice02-component-contract-file-plan
status: proposed-done
artifact-status: source-to-component migration plan
source-files-edited: false
```

## Grounding

This migration plan consumes verified Slice01 evidence from
`slice01-implementation-surface-map`, including the implementation surface
inventory, accepted component source map, release validation surface map, and
cross-cutting concern map, plus the Arc04 `operator-accepted-architecture`
accepted architecture. This is a Slice02 planning artifact only.

## Action Vocabulary

- `move`: target component should become the primary source home for the
  material.
- `copy`: a support asset or compatibility payload may be duplicated into a
  package-local target while source provenance is preserved.
- `split`: one current file feeds multiple component files or guides.
- `new prose`: accepted component scope requires new writing beyond a direct
  move/copy.
- `defer`: the decision belongs to Slice03 or a later implementation slice.

## Migration Mapping

| Current source path | Decision | Target component file(s) | Notes |
|---------------------|----------|--------------------------|-------|
| `README.md` | defer, then split route prose | Slice03 inputs for repository README component table, composed use route, source clone route, generated zip route, installed skill route, and CCDP separation. | Do not edit in Slice02. README release wording belongs to Slice03. |
| `SKILL.md` | split | `collaboration-framework/SKILL.md`, `collaboration-framework/guides/component-route-table.md`, selected route notes in specialist `SKILL.md` files. | Preserve `/collaboration-framework` as composer; remove full specialist bodies only during implementation. |
| `docs/AI-CONSTITUTION-SUPPLEMENT.md` | split / move | `collaboration-framework/guides/posture-and-ethics.md`, `collaboration-framework/guides/structural-pulls.md`, `collaboration-framework/guides/collaborative-rights.md`. | Source keeps the posture floor with the composer. Exact extraction boundaries need implementation review. |
| `docs/AI-ENGINEERING-METHODOLOGY.md` | split / move / new prose | `engineering-methods/guides/01-engineering-methodology.md`, `02-knowledge-substrate.md`, `03-process-rigour.md`, `04-operational-routing.md`, `05-component-boundary-analysis.md`, `06-source-package-release-gates.md`. | Component-boundary and source/package/release gate guides require new prose from Project02 and Project01 evidence. |
| `docs/PROJECT-MANAGEMENT.md` | move / split | `project-management/SKILL.md` plus PM wayfinder material inside `project-management/guides/` as needed. | The entrypoint should stay a wayfinder, not reload the whole PM body inline. |
| `docs/pm/01-scales-of-work.md` | move | `project-management/guides/01-scales-of-work.md`. | Direct PM guide mapping. |
| `docs/pm/02-canonical-planning-worktree.md` | move | `project-management/guides/02-canonical-planning-worktree.md`. | Retain default `artifacts/` home rule. |
| `docs/pm/03-planning-top-down.md` | move | `project-management/guides/03-planning-top-down.md`. | Direct PM guide mapping. |
| `docs/pm/04-closing-slices.md` | move with dependency note | `project-management/guides/04-closing-slices.md`. | Keep dependency on `work-verification` for ledger mechanics. |
| `docs/pm/05-closing-arcs.md` | move with dependency note | `project-management/guides/05-closing-arcs.md`. | Preserve plan-change discipline and bubble-up mechanics. |
| `docs/pm/06-confirmation-protocol.md` | move | `project-management/guides/06-confirmation-protocol.md`. | Direct PM guide mapping. |
| `docs/pm/07-anti-patterns.md` | move | `project-management/guides/07-anti-patterns.md`. | Direct PM guide mapping. |
| `docs/pm/08-maintenance.md` | move / split | `project-management/guides/08-maintenance.md`, relevant per-component maintenance notes in `engineering-methods/guides/06-source-package-release-gates.md`. | Component maintenance is not a component; versioning remains per component. |
| `docs/pm/09-worked-example-odm.md` | move | `project-management/examples/01-worked-example-odm.md`. | Accepted example placement. |
| `docs/pm/version-history.md` | split / move | `project-management/version-history.md`. | Preserve PM provenance while aligning with sibling component `version-history.md`. |
| `templates/LEDGER-DISCIPLINE.md` | split / copy | `work-verification/guides/01-ledger-discipline.md`, `02-evidence-strength.md`, `03-row-closure.md`, `04-silent-drop-checks.md`, `05-independent-verification.md`, and `work-verification/templates/LEDGER-DISCIPLINE.md`. | Keep the support asset package-local if links or user workflows need the full template payload. |
| `docs/CODE-AUDIT.md` | split / move | `code-auditing/guides/01-audit-scope-and-map.md`, `02-findings-and-severity.md`, `03-scale-aware-auditing.md`, `04-modernization-synthesis.md`, `05-audit-to-hardening-handoff.md`. | Repair output-home wording to point durable slice artifacts to `artifacts/`. |
| `docs/CLAUDE-CODE-COVERAGE.md` | split / move / new prose | `testing/guides/01-testing-discipline.md`, `02-coverage-hardening.md`, `03-validation-gates.md`. | Preserve old prompt lineage as compatibility text while broadening the component identity to testing. |
| `docs/SUBAGENT-DELEGATION-POLICY.md` | split / move / new prose | `agent-coordination/guides/01-when-to-delegate.md`, `02-context-packets.md`, `03-result-integration.md`, `04-anti-patterns.md`, plus `agent-coordination/SKILL.md` terminology. | Current source is narrower than accepted agent-coordination scope. Add context-packet and result-integration prose. |
| `docs/CONTRIBUTION-STYLE.md` | split / move | `contribution-style/guides/01-contribution-style.md`, `contribution-style/guides/02-upstream-ticket-workflow.md`. | Keep voice and workflow together in the accepted component. |
| `templates/CONTRIBUTION-TICKET.md` | copy / move | `contribution-style/templates/CONTRIBUTION-TICKET.md`. | Treat as package-local support asset with README/SKILL/template links resolved in Slice03. |
| `templates/GUIDE.md` | defer | Possible future component-authoring support, no accepted component target in Slice02. | Do not pull into any package unless a later slice records why. |
| `Makefile` | defer | Slice03 package and validation plan. | Must eventually update package lists/targets, but not in Slice02. |
| `package-path-exceptions.tsv` | defer | Slice03 package-path exception plan. | Prefer package-local link repairs; add exceptions only with explicit rationale. |
| `protocols/ccdp/`, `ccdp.zip`, and CCDP Make targets | defer / non-component | Outside Project02 component set. | Preserve CCDP separation; do not migrate protocol source into collaboration-framework components. |

## Migration Constraints

- Source files remain untouched in this slice.
- Accepted component names from `operator-accepted-architecture.md` override
  older pre-acceptance names in prior Arc04 inputs.
- The migration should preserve source provenance. Mechanical extraction should
  not copyedit source prose unless a later implementation slice explicitly
  scopes that change.
- Slice03 must decide README, Makefile, generated zip, and package-path
  exception behavior before source-edit implementation begins.
