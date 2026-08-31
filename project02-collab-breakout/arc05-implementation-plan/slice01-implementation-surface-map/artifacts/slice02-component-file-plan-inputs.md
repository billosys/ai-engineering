# Slice02 Component File Plan Inputs

```yaml
project: project02-collab-breakout
arc: arc05-implementation-plan
slice: slice01-implementation-surface-map
handoff: slice02-component-contract-file-plan
status: proposed-done
source-files-remain-untouched: true
```

## Boundary

These Slice02 inputs support the component file plan. They are not final
source edits, not final package paths, and not implementation authorization.
No source edits were made; source files remain untouched.

## Required Inputs For Slice02

| Accepted component | Component file plan input | Open question |
|--------------------|---------------------------|---------------|
| `collaboration-framework` | Plan composer `SKILL.md`, sibling `version-history.md`, compact posture guides, structural-pulls/collaborative-rights guides if kept, and route table. | Which posture material remains inline in `SKILL.md` versus guide-only while keeping daily-driver load useful? |
| `engineering-methods` | Plan `SKILL.md`, sibling `version-history.md`, methodology guide split, operational routing guide, `05-component-boundary-analysis.md`, and source/package/release gates guide. | How much of current `docs/AI-ENGINEERING-METHODOLOGY.md` stays in one guide versus split into knowledge substrate, process rigour, and operational routing? |
| `project-management` | Plan `SKILL.md`, sibling `version-history.md`, numbered PM guides, example path, and dependency on `work-verification`. | How should existing `docs/pm/version-history.md` map into component-level `version-history.md` without losing PM provenance? |
| `work-verification` | Plan `SKILL.md`, sibling `version-history.md`, ledger discipline guide split, evidence-strength guide, row-closure guide, silent-drop guide, independent-verification guide, and template travel. | Should `templates/LEDGER-DISCIPLINE.md` remain a package-local template, a guide source, or both? |
| `testing` | Plan `SKILL.md`, sibling `version-history.md`, testing discipline guide, coverage-hardening guide, validation-gates guide, and compatibility note from `docs/CLAUDE-CODE-COVERAGE.md`. | What migration text preserves the old coverage prompt name while accepting the broader `testing` component? |
| `code-auditing` | Plan `SKILL.md`, sibling `version-history.md`, audit scope/map guide, findings/severity guide, scale-aware auditing guide, modernization synthesis guide, and audit-to-hardening handoff. | Which current output-home wording needs direct repair so durable planning outputs default to slice `artifacts/`? |
| `agent-coordination` | Plan `SKILL.md`, sibling `version-history.md`, when-to-delegate guide, context-packets guide, result-integration guide, anti-patterns guide, and CC/CDC/operator terminology. | What new source prose is needed for context-packet discipline and result integration beyond current delegation policy? |
| `contribution-style` | Plan `SKILL.md`, sibling `version-history.md`, contribution style guide, upstream-ticket workflow guide, and `templates/CONTRIBUTION-TICKET.md` support asset. | How should template links resolve from source clone, generated zip, and installed skill modes? |

## Cross-Cutting File Plan Questions

- Slice02 must use `operator-accepted-architecture.md` as the authoritative
  naming input, because the older Arc04 `arc05-implementation-inputs.md`
  carries pre-acceptance names for several components.
- Slice02 must keep source/package/release gates under `engineering-methods`
  while adding package/source contract fields to every component.
- Slice02 must plan component versioning as `SKILL.md` version plus sibling
  `version-history.md`.
- Slice02 must place ontology critique at
  `engineering-methods/guides/05-component-boundary-analysis.md`.
- Slice02 must keep memory admission deferred future research.
- Slice02 must preserve CCDP separation and avoid treating `ccdp.zip` or
  `protocols/ccdp/` as collaboration-framework component package content.
- Slice02 must not design final README, Makefile, generated zip, or validation
  edits beyond the component file plan inputs; Slice03 owns that release
  surface plan.

## Non-Final State

The accepted component root names are stable, but file movements, copied
content, guide splits, package-local links, generated zip contents, Makefile
targets, package-path exceptions, and validation command sequencing are not
final until later Arc05 slices close.
