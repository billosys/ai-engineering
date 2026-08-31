# Implementation Surface Inventory

```yaml
project: project02-collab-breakout
arc: arc05-implementation-plan
slice: slice01-implementation-surface-map
status: proposed-done
artifact-status: implementation surface map
accepted-architecture-source: ../../arc04-breakout-architecture/slice04-operator-acceptance-architecture-synthesis/artifacts/operator-accepted-architecture.md
project01-source-package-source: ../../../project01-harmonise-paths/closing-report.md
source-files-edited: false
```

## Input Contract

This implementation surface map consumes the accepted architecture in
`operator-accepted-architecture.md`, Arc04 close, Arc05 plan inputs, and the
Project01 / project01-harmonise-paths close report. Project01 supplies the
source/package, package-local, zip root, README, `SKILL.md`, Makefile,
generated zip, validation, and CCDP separation constraints.

The current source checkout was inspected read-only at
`/Users/oubiwann/lab/billosys/ai-engineering`. This inventory is not a final
source-edit plan and does not finalize package paths beyond accepted component
root names and planning assumptions.

## Accepted Component Roots

Arc04 accepted exactly eight component roots:

- `collaboration-framework`
- `engineering-methods`
- `project-management`
- `work-verification`
- `testing`
- `code-auditing`
- `agent-coordination`
- `contribution-style`

## Current Source Documents

| Current surface | Current role | Accepted component pressure |
|-----------------|--------------|-----------------------------|
| `README.md` | Repository overview, collaboration framework explanation, skill library table, build/install commands, repository layout, CCDP package guidance. | Must route composed `collaboration-framework` use, individual component use, generated zip use, installed skill use, and CCDP separation. |
| `SKILL.md` | Current monolithic collaboration-framework skill, frontmatter `name: collaboration-framework`, `version: 1.4.1`, posture summary, methodology summary, routing to operational docs. | Becomes daily-driver composer with compact collaboration/posture floor and route table. It should not continue to own full specialist bodies after breakout. |
| `docs/AI-CONSTITUTION-SUPPLEMENT.md` | Current posture and collaborative rights source. | Moves into `collaboration-framework` guide surface as posture floor material. |
| `docs/AI-ENGINEERING-METHODOLOGY.md` | Current methodology, 9-point SDLC, knowledge substrate, process rigour, ledger and audit relations, subagent notes, version history. | Maps primarily to `engineering-methods`, with routes out to PM, work verification, testing, code auditing, agent coordination, contribution, and domain skills. |
| `docs/PROJECT-MANAGEMENT.md` | PM wayfinder for planning layout, required load set, and close machinery. | Maps to `project-management/SKILL.md` and PM guide surface. |
| `docs/pm/01-scales-of-work.md` | Project, arc, slice, step, and iteration scale definitions. | `project-management` guide input. |
| `docs/pm/02-canonical-planning-worktree.md` | Planning worktree, canonical filenames, ledger locations, and slice artifact home. | `project-management` guide input plus source/package planning surface. |
| `docs/pm/03-planning-top-down.md` | Project, arc, and slice planning mechanics. | `project-management` guide input. |
| `docs/pm/04-closing-slices.md` | Slice close report and bubble-up mechanics. | `project-management` guide input with dependency on `work-verification`. |
| `docs/pm/05-closing-arcs.md` | Arc close, project bubble-up, and plan-change discipline. | `project-management` guide input with dependency on `work-verification`. |
| `docs/pm/06-confirmation-protocol.md` | Layout confirmation protocol. | `project-management` guide input. |
| `docs/pm/07-anti-patterns.md` | Planning anti-patterns to refuse. | `project-management` guide input. |
| `docs/pm/08-maintenance.md` | PM spec maintenance rules. | `project-management` guide input and component maintenance input. |
| `docs/pm/09-worked-example-odm.md` | PM worked example. | `project-management/examples/01-worked-example-odm.md` candidate input. |
| `docs/pm/version-history.md` | Current PM-specific version history. | Needs reconciliation with accepted sibling `project-management/version-history.md`. |
| `templates/LEDGER-DISCIPLINE.md` | Current ledger protocol and template. | Maps to `work-verification`; may travel as a template/support asset. |
| `docs/CODE-AUDIT.md` | Current diagnosis-only audit prompt with audit map, severity, scale coverage, modernization synthesis, and output guidance. | Maps to `code-auditing`; guide surface likely splits by scope/map, findings/severity, scale-aware auditing, modernization, and audit-to-hardening handoff. |
| `docs/CLAUDE-CODE-COVERAGE.md` | Current hard coverage prompt, Codex adapter, testing strategy, coverage gates, and anti-patterns. | Maps to `testing`; current name is historical and narrower than accepted component identity. |
| `docs/SUBAGENT-DELEGATION-POLICY.md` | Current delegation policy, thinking/lookup boundary, install notes, and Codex notes. | Maps to `agent-coordination`; current source is narrower than accepted context-packets/result-integration component. |
| `docs/CONTRIBUTION-STYLE.md` | Current upstream contribution style guide. | Maps to `contribution-style`. |
| `templates/CONTRIBUTION-TICKET.md` | Current upstream contribution ticket template. | Maps to `contribution-style/templates/CONTRIBUTION-TICKET.md` as support asset. |
| `templates/GUIDE.md` | Generic new-guide skeleton. | Not an accepted component by itself; possible support for future component-file planning. |

## Current Release And Package Surfaces

| Surface | Current state | Arc05 planning implication |
|---------|---------------|----------------------------|
| `Makefile` | Builds current monolithic `collaboration-framework.zip` and domain skill zips. | Slice02 and Slice03 must plan new component package targets and list changes before source edits. |
| `INSTALL_ZIPS` | Includes `collaboration-framework.zip` and ten domain/tooling skill zips. | Accepted component zips are not listed yet. |
| `ALL_SKILL_FILES` | Includes top-level `SKILL.md` and domain/tooling skill entrypoints. | Accepted component `SKILL.md` entrypoints are not listed yet. |
| `CF_FILES` | Explicit current collaboration-framework bundle list: top-level `SKILL.md`, framework docs, PM docs, audit, coverage, delegation, contribution, and two templates. | This is the main source of monolithic bundle membership to split. |
| `collaboration-framework.zip` | Present ignored generated zip, root `collaboration-framework/`, currently includes the monolithic `CF_FILES` set. | Root name remains accepted, but contents must shrink/re-route after implementation planning. |
| `package-path-exceptions.tsv` | Contains visible warnings plus explicit exceptions for current collaboration-framework package references to source-only domain skill placeholders. | New component package plans must prefer package-local links and add exceptions only when explicit and justified. |
| `scripts/check-package-paths` | Validates package-context Markdown paths in generated skill zips with warnings and explicit exceptions. | `engineering-methods` owns the source/package/release gate semantics; each component contract must name validation coverage. |
| `scripts/check-skill-description.sh` | Validates skill description length before packaging. | Every accepted component `SKILL.md` needs inclusion in validation coverage. |
| `scripts/stage-skill-entrypoint` | Stages domain skill entrypoints for packaged bundles. | Slice03 should decide whether component packages reuse this transform or keep a collaboration-framework-specific path. |
| `ccdp.zip` | Present ignored generated zip, root `ccdp/`, separate from skill bundles. | Preserve CCDP separation; do not bundle CCDP into accepted components. |
| `protocols/ccdp/` | Source protocol tree with README, assembled spec, chapters, JSON corpus, visual guide, templates, and tool source. | Adjacent protocol distribution only, not Project02 component source. |

## Current Gaps To Carry Forward

- No source directories currently exist for the accepted component roots except
  the generated-package root name `collaboration-framework/` inside the zip.
- No component-root sibling `version-history.md` files exist in source today.
  Current versioning is embedded in top-level `SKILL.md`, source documents,
  and `docs/pm/version-history.md`.
- No current source file corresponds exactly to
  `engineering-methods/guides/05-component-boundary-analysis.md`; Arc04
  acceptance creates that planning target from ontology/component-boundary
  analysis evidence.
- No current source file corresponds exactly to the broadened
  `agent-coordination` context-packet and result-integration scope. Current
  source starts from `docs/SUBAGENT-DELEGATION-POLICY.md`.
- Memory admission is deferred future research and has no Project02 source
  implementation surface.
- The Arc04 `arc05-implementation-inputs.md` still contains pre-acceptance
  names for several components; `operator-accepted-architecture.md` is the
  authoritative naming source for Arc05.
