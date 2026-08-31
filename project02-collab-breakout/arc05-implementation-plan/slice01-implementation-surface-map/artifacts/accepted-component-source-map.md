# Accepted Component Source Map

```yaml
project: project02-collab-breakout
arc: arc05-implementation-plan
slice: slice01-implementation-surface-map
status: proposed-done
accepted-architecture-source: ../../arc04-breakout-architecture/slice04-operator-acceptance-architecture-synthesis/artifacts/operator-accepted-architecture.md
source-files-edited: false
```

## Naming Rule

This map preserves the accepted eight-component map exactly:
`collaboration-framework`, `engineering-methods`, `project-management`,
`work-verification`, `testing`, `code-auditing`, `agent-coordination`, and
`contribution-style`.

Older proposed names in prior Arc04 implementation inputs are not
authoritative for Arc05 naming. They remain migration/history evidence only.

## Component Map

| Accepted component | Current source files | Current package/release surface | Source status | Slice02 file-plan input |
|--------------------|----------------------|---------------------------------|---------------|-------------------------|
| `collaboration-framework` | `SKILL.md`, `README.md`, `docs/AI-CONSTITUTION-SUPPLEMENT.md`, selected route summaries from `docs/AI-ENGINEERING-METHODOLOGY.md`. | Existing `collaboration-framework.zip`; current `CF_FILES` monolithic package list; README `/collaboration-framework` use path. | Existing component root name but current source body is monolithic. | Plan composer `SKILL.md`, sibling `version-history.md`, compact posture guides, and route table without retaining full specialist docs. |
| `engineering-methods` | `docs/AI-ENGINEERING-METHODOLOGY.md`; source/package/release gate material from `README.md`, `Makefile`, `package-path-exceptions.tsv`, `scripts/check-package-paths`, and Project01 close; new target `engineering-methods/guides/05-component-boundary-analysis.md`. | No current package root; no current `SKILL.md` entrypoint; package/release gates currently live across source docs and Makefile. | New accepted component root. | Plan process/router entrypoint, guide split, source/package/release gates guide, and component-boundary-analysis guide. |
| `project-management` | `docs/PROJECT-MANAGEMENT.md`, `docs/pm/01-scales-of-work.md`, `docs/pm/02-canonical-planning-worktree.md`, `docs/pm/03-planning-top-down.md`, `docs/pm/04-closing-slices.md`, `docs/pm/05-closing-arcs.md`, `docs/pm/06-confirmation-protocol.md`, `docs/pm/07-anti-patterns.md`, `docs/pm/08-maintenance.md`, `docs/pm/09-worked-example-odm.md`, `docs/pm/version-history.md`. | Currently bundled inside `collaboration-framework.zip` through `CF_FILES`; no standalone PM zip. | Existing source family, new component root. | Plan PM family `SKILL.md`, sibling `version-history.md`, numbered guides, example path, and dependency on `work-verification`. |
| `work-verification` | `templates/LEDGER-DISCIPLINE.md`; ledger/process references in `docs/AI-ENGINEERING-METHODOLOGY.md`; close mechanics references in `docs/PROJECT-MANAGEMENT.md` and `docs/pm/04-closing-slices.md` / `docs/pm/05-closing-arcs.md`. | Currently bundled as template inside `collaboration-framework.zip`; no standalone zip. | New accepted component root replacing narrower ledger name. | Plan `SKILL.md`, sibling `version-history.md`, ledger discipline guide split, and template travel rules. |
| `testing` | `docs/CLAUDE-CODE-COVERAGE.md`; validation command references in `README.md` and `Makefile`. | Currently bundled as coverage prompt inside `collaboration-framework.zip`; no general testing zip. | New accepted component root; current guide is narrower and historically named. | Plan broader testing entrypoint, coverage-hardening guide, validation-gates guide, compatibility/migration note from coverage prompt. |
| `code-auditing` | `docs/CODE-AUDIT.md`; source-only domain skill placeholder exception in `package-path-exceptions.tsv`. | Currently bundled as audit prompt inside `collaboration-framework.zip`; no standalone audit zip. | New accepted component root with existing guide source. | Plan audit `SKILL.md`, sibling `version-history.md`, stage/scale-aware guide split, output-home repair, and handoff to `testing`. |
| `agent-coordination` | `docs/SUBAGENT-DELEGATION-POLICY.md`; CC/CDC/operator notes in `SKILL.md`, `docs/PROJECT-MANAGEMENT.md`, and `templates/LEDGER-DISCIPLINE.md`; accepted architecture adds context-packet and result-integration requirements. | Currently bundled as delegation policy inside `collaboration-framework.zip`; no standalone coordination zip. | New accepted component root broader than current source. | Plan terminology, when-to-delegate, context-packets, result-integration, and anti-pattern guides. |
| `contribution-style` | `docs/CONTRIBUTION-STYLE.md`, `templates/CONTRIBUTION-TICKET.md`, contribution references in `README.md` and `SKILL.md`. | Currently bundled as contribution style plus ticket template inside `collaboration-framework.zip`; no standalone contribution zip. | New accepted component root with existing source guide and template. | Plan contribution `SKILL.md`, sibling `version-history.md`, guide split, and package-local template link. |

## Cross-Component Dependencies

| From | To | Planning note |
|------|----|---------------|
| `collaboration-framework` | all accepted components | Composer route table should point to component entrypoints and keep daily-driver posture floor. |
| `engineering-methods` | all accepted components | Owns source/package/release gates and operational routing; every component keeps its own package/source contract. |
| `project-management` | `work-verification` | PM owns lifecycle; work verification owns evidence closure. |
| `code-auditing` | `testing` | Audit remains diagnosis-only and can hand off to testing for hardening. |
| `testing` | domain skills and project tooling | Testing work must load relevant domain skills and target project test commands. |
| `agent-coordination` | all role-bearing components | Owns CC/CDC/operator terminology, delegation decisions, context-packet discipline, and result integration. |
| `contribution-style` | `collaboration-framework` and `code-auditing` | Uses collaboration posture and can consume audit findings as upstream-ticket inputs. |

## Package Path Caution

The accepted component root names are stable planning inputs, but source edits
and package paths are not final. Slice02 must convert this source map into a
component file plan before implementation begins, and Slice03 must separately
plan README, `SKILL.md`, Makefile, generated zip, and validation behavior.
