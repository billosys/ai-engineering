# Arc05 Implementation Inputs

```yaml
project: project02-collab-breakout
arc: arc04-breakout-architecture
slice: slice04-operator-acceptance-architecture-synthesis
status: accepted-architecture-inputs
implementation-started: false
source-files-remain-untouched: true
```

## Boundary

These are Arc05 implementation-plan inputs. They do not start Arc05
implementation, do not edit source files, and do not finalise package paths.
Operator acceptance evidence is recorded in
`operator-accepted-architecture.md`. Arc05 can now plan from the accepted
architecture, while implementation-plan decisions still remain subject to
Arc05 closure before source edits begin.

Source files remain untouched. No source edits, README updates, `SKILL.md`
entrypoints, packaging changes, Makefile changes, package list edits,
generated zip updates, or CCDP package edits were made by Slice04.

## Implementation-Plan Inputs

| Arc05 area | Required planning content | Current input |
|------------|---------------------------|---------------|
| Source edits | Exact source files to edit, move, split, copy, or stage. | Prepare from accepted component contracts only. Candidate sources include top-level `SKILL.md`, README, `docs/AI-CONSTITUTION-SUPPLEMENT.md`, `docs/AI-ENGINEERING-METHODOLOGY.md`, `docs/PROJECT-MANAGEMENT.md`, `docs/pm/*.md`, `templates/LEDGER-DISCIPLINE.md`, `docs/CODE-AUDIT.md`, `docs/CLAUDE-CODE-COVERAGE.md`, `docs/SUBAGENT-DELEGATION-POLICY.md`, `docs/CONTRIBUTION-STYLE.md`, and `templates/CONTRIBUTION-TICKET.md`. |
| README updates | Source-clone routes, component routes, composed collaboration-framework route, package routes, installed skill routes, and CCDP separation. | Add only after operator accepts final architecture or explicit changes. |
| SKILL.md entrypoints | Top-level composer rewrite plus direct-load component `SKILL.md` entrypoints. | Each accepted component entrypoint must include trigger/scope, dependency edges, local adapter notes, support assets, package paths, maintenance owner, and version-history responsibility. |
| Packaging changes | Package roots, support asset travel, package-local links, generated zip behavior, and migration from current `collaboration-framework.zip`. | Use pending paths only until operator acceptance; preserve Project01 package-local link contract. |
| Makefile | `INSTALL_ZIPS`, `ALL_SKILL_FILES`, package targets, `CF_FILES`, package-path exceptions, and CCDP package boundary. | Update in one coherent release-surface change after architecture acceptance. |
| Validation gates | `make check-skills`, `make check-package-paths`, `make collab-framework`, `make all`, and CCDP validation only if CCDP source is touched. | Every implementation slice must name the validation gates it can run and record accepted warnings separately from hard failures. |
| Migration notes | Compatibility aliases, renamed coverage surface, old workbench audit output-home language, current package users, and package root migration. | Preserve history and package reader clarity while moving durable planning output defaults to slice `artifacts/`. |
| Review concerns | Over-thin direct loads, monolith recreation, PM/ledger drift, role-language drift, package-local link drift, unsupported component promotion, and operator acceptance evidence. | Treat as Arc05 review checklist before any source edit is complete. |

## Component-Specific Inputs

| Proposed component or row | Arc05 input |
|---------------------------|-------------|
| `collaboration-framework` | Rewrite as composer, not full monolith; include compact posture/process floor, route table, agent adapter note, repository orientation note, and package/release gate reminders. |
| `collaborative-posture-and-ethics` | Create or stage posture entrypoint and guide from accepted source; include methodology dependency and compact composer summary. |
| `engineering-methodology-and-process` | Create process/router entrypoint; prevent re-owning PM, ledger, audit, coverage, delegation, contribution, or domain skill bodies. |
| `ledger-verification-protocol` | Make ledger direct-load; preserve row states, evidence strength, silent-drop checks, CDC verification boundary, deferral, and no-op rules. |
| `project-management` | Build PM wayfinder and family package; keep examples, anti-patterns, PM provenance/version notes, and ledger dependency inside family. |
| `code-audit-discipline` | Keep audit diagnosis-only; repair output-home examples to use slice `artifacts/` for durable planning outputs unless operator override exists. |
| `coverage-hardening-discipline` | Generalize coverage guide and preserve compatibility from historical `CLAUDE-CODE-COVERAGE.md` route. |
| `delegation-policy` | Keep focused on subagent and lookup boundaries with role-language adapter note. |
| `contribution-style-and-voice` | Package `CONTRIBUTION-TICKET.md` as support asset and verify package-local template link. |
| Adapters and gates | Keep `agent-adapter-and-routing` and `repository-orientation-and-distribution` as central plus local notes; keep Project01 gates mandatory. |
| Deferred/non-component rows | Do not implement verification-methodology, ontology critique, component-maintenance, or evidence strength/memory admission as standalone packages without a new acceptance event. |

## Source Boundary For Arc05

Implementation not started. Source files remain untouched by Slice04. Arc05
must explicitly carry operator acceptance evidence into its implementation
plan before performing source edits.
