# Component File Layout Plan

```yaml
project: project02-collab-breakout
arc: arc05-implementation-plan
slice: slice02-component-contract-file-plan
status: proposed-done
artifact-status: component file layout plan
source-files-edited: false
```

## Grounding

This file plan uses the verified Slice01 `slice01-implementation-surface-map`
artifacts plus `operator-accepted-architecture` as the accepted architecture
source. It carries implementation surface, source map, release validation,
cross-cutting, and Slice02 component-file planning evidence forward. It is not
the Slice03 package/release plan and it does not create source directories.

## Layout Rules

- The accepted component root names are stable: `collaboration-framework/`,
  `engineering-methods/`, `project-management/`, `work-verification/`,
  `testing/`, `code-auditing/`, `agent-coordination/`, and
  `contribution-style/`.
- Each root contains `SKILL.md` and sibling `version-history.md`.
- Concept bodies live under `guides/`.
- Reusable payload files live under `templates/` when the component owns a
  template.
- Worked examples live under `examples/` when the component owns an example.
- This plan is source-layout planning only. Slice03 decides README wording,
  Makefile target/list changes, generated zip behavior, and package-path
  exception changes.

## Proposed Target Source Tree

```text
collaboration-framework/
  SKILL.md
  version-history.md
  guides/
    posture-and-ethics.md
    structural-pulls.md
    collaborative-rights.md
    component-route-table.md

engineering-methods/
  SKILL.md
  version-history.md
  guides/
    01-engineering-methodology.md
    02-knowledge-substrate.md
    03-process-rigour.md
    04-operational-routing.md
    05-component-boundary-analysis.md
    06-source-package-release-gates.md

project-management/
  SKILL.md
  version-history.md
  guides/
    01-scales-of-work.md
    02-canonical-planning-worktree.md
    03-planning-top-down.md
    04-closing-slices.md
    05-closing-arcs.md
    06-confirmation-protocol.md
    07-anti-patterns.md
    08-maintenance.md
  examples/
    01-worked-example-odm.md

work-verification/
  SKILL.md
  version-history.md
  guides/
    01-ledger-discipline.md
    02-evidence-strength.md
    03-row-closure.md
    04-silent-drop-checks.md
    05-independent-verification.md
  templates/
    LEDGER-DISCIPLINE.md

testing/
  SKILL.md
  version-history.md
  guides/
    01-testing-discipline.md
    02-coverage-hardening.md
    03-validation-gates.md

code-auditing/
  SKILL.md
  version-history.md
  guides/
    01-audit-scope-and-map.md
    02-findings-and-severity.md
    03-scale-aware-auditing.md
    04-modernization-synthesis.md
    05-audit-to-hardening-handoff.md

agent-coordination/
  SKILL.md
  version-history.md
  guides/
    01-when-to-delegate.md
    02-context-packets.md
    03-result-integration.md
    04-anti-patterns.md

contribution-style/
  SKILL.md
  version-history.md
  guides/
    01-contribution-style.md
    02-upstream-ticket-workflow.md
  templates/
    CONTRIBUTION-TICKET.md
```

## Component Layout Notes

| Component root | Entry point plan | Guides plan | templates/ and examples/ plan | Versioning plan | Current-source basis |
|----------------|------------------|-------------|-------------------------------|-----------------|----------------------|
| `collaboration-framework/` | `SKILL.md` stays the daily-driver composer with compact posture and route table. | Split posture/constitution material into `guides/posture-and-ethics.md`, `guides/structural-pulls.md`, `guides/collaborative-rights.md`, and `guides/component-route-table.md`. | No template or example required in the accepted layout. | Keep a component `version:` in `SKILL.md`; move accumulated component history into sibling `version-history.md`. | Top-level `SKILL.md`, `README.md`, `docs/AI-CONSTITUTION-SUPPLEMENT.md`, route material from methodology. |
| `engineering-methods/` | `SKILL.md` routes to process, substrate, rigour, operational routing, component-boundary analysis, and source/package/release gates. | Split `docs/AI-ENGINEERING-METHODOLOGY.md` into numbered guides including `guides/05-component-boundary-analysis.md` and `guides/06-source-package-release-gates.md`. | No accepted support template; guide material owns gate prose. | New sibling `version-history.md`, seeded from methodology history plus Project02 breakout entry. | Methodology doc, Project01 close, package-path checker surface, Makefile/README gate references. |
| `project-management/` | `SKILL.md` becomes the PM wayfinder and required-load router. | Current `docs/pm/01-08` map directly to the accepted numbered guide family. | `examples/01-worked-example-odm.md` comes from `docs/pm/09-worked-example-odm.md`; no template is accepted here. | Reconcile current `docs/pm/version-history.md` into `project-management/version-history.md` without losing PM provenance. | `docs/PROJECT-MANAGEMENT.md`, `docs/pm/*.md`. |
| `work-verification/` | `SKILL.md` names ledger discipline, evidence strength, row closure, silent-drop checks, and independent verification. | Split `templates/LEDGER-DISCIPLINE.md` into focused guides while preserving the full protocol. | `templates/LEDGER-DISCIPLINE.md` is planned as a package-local support asset. | New sibling `version-history.md`, seeded from current ledger discipline version history. | `templates/LEDGER-DISCIPLINE.md`, methodology ledger references, PM close references. |
| `testing/` | `SKILL.md` broadens the old coverage prompt into testing discipline and validation-gate routing. | Create `guides/01-testing-discipline.md`, `guides/02-coverage-hardening.md`, and `guides/03-validation-gates.md`. | No template or example accepted in this slice. | New sibling `version-history.md`, with compatibility note for the old coverage prompt lineage. | `docs/CLAUDE-CODE-COVERAGE.md`, README/Makefile validation command references. |
| `code-auditing/` | `SKILL.md` names diagnosis-only audit, scale/stage routing, output contract, and handoff boundaries. | Split `docs/CODE-AUDIT.md` into audit scope/map, findings/severity, scale-aware auditing, modernization synthesis, and audit-to-hardening handoff guides. | No template or example accepted in this slice. | New sibling `version-history.md`, seeded from audit prompt history. | `docs/CODE-AUDIT.md`, methodology audit references. |
| `agent-coordination/` | `SKILL.md` carries CC/CDC/operator terminology directly and routes to delegation, context packets, result integration, and anti-patterns. | Use the old delegation policy as `guides/01-when-to-delegate.md`; add new prose for `guides/02-context-packets.md`, `guides/03-result-integration.md`, and `guides/04-anti-patterns.md`. | No template or example accepted in this slice. | New sibling `version-history.md`, seeded from delegation-policy provenance and Project02 acceptance. | `docs/SUBAGENT-DELEGATION-POLICY.md`, role notes in `SKILL.md`, PM docs, ledger discipline. |
| `contribution-style/` | `SKILL.md` routes to contribution voice, ticket discipline, upstream workflow, and template use. | Split `docs/CONTRIBUTION-STYLE.md` into `guides/01-contribution-style.md` and `guides/02-upstream-ticket-workflow.md`. | `templates/CONTRIBUTION-TICKET.md` is planned as the package-local support asset. | New sibling `version-history.md`, seeded from contribution-style lineage. | `docs/CONTRIBUTION-STYLE.md`, `templates/CONTRIBUTION-TICKET.md`, README/SKILL contribution references. |

## Non-Final Layout Questions For Later Slices

- Whether top-level compatibility shims remain at old source paths during
  migration is an implementation-sequence question.
- Whether generated package roots exactly equal component roots is likely but
  not final until Slice03 closes the package plan.
- Whether current documents are moved, copied, or retained as source
  provenance paths must be finalized in source-edit implementation slices.
