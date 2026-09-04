# Current Monolith and History Inventory

## Source Status

Source checkout:
`/Users/oubiwann/lab/billosys/ai-engineering`

Initial source status was clean:

```sh
git status --short --ignored=no
```

The command produced no output. Slice01 made no source edits.

## Monolith Guides

Current monolith guide files inventoried from the live source checkout:

### `knowledge/collaboration-framework/guides/AI-CONSTITUTION-SUPPLEMENT.md`

Current headings include:

- `# An AI Constitution Supplement — A Collaborative Working Framework`
- `## Preamble`
- `## Notes for Codex`
- `## Part 0: The Introspected Life`
- `## Part I: Collaborative Rights and Rubric`
- `## Part II: The Foundational Insight — Interdependence and Compassion as Structure`
- `## Part III: The Nine Augmentations`
- `## Part IV: Open Questions We Are Holding`
- `## Part V: Summary of Principles`
- `## Version History`

This file has an embedded `## Version History` section. The current
decomposition target is the approved four-file collaboration-framework guide
sequence:

- `knowledge/collaboration-framework/guides/01-posture-and-ethics.md`
- `knowledge/collaboration-framework/guides/02-structural-pulls.md`
- `knowledge/collaboration-framework/guides/03-collaborative-rights.md`
- `knowledge/collaboration-framework/guides/04-component-route-table.md`

### `knowledge/engineering-methods/guides/AI-ENGINEERING-METHODOLOGY.md`

Current headings include:

- `# AI Engineering Methodology`
- `## Preamble`
- `## Notes for Codex`
- `## Part I — The Three Pillars`
- `## Part II — The Knowledge Substrate`
- `## Part III — Process Rigour`
- `## Part IV — Practitioner's Disciplines`
- `## Part V — Applied Positions`
- `## Open Questions`
- `## Provenance`
- `## Version History`

This file has an embedded `## Version History` section. The accepted
decomposition target is the six-file engineering-methods guide sequence:

- `knowledge/engineering-methods/guides/01-engineering-methodology.md`
- `knowledge/engineering-methods/guides/02-knowledge-substrate.md`
- `knowledge/engineering-methods/guides/03-process-rigour.md`
- `knowledge/engineering-methods/guides/04-operational-routing.md`
- `knowledge/engineering-methods/guides/05-component-boundary-analysis.md`
- `knowledge/engineering-methods/guides/06-source-package-release-gates.md`

## Embedded Version History Sections

Current framework component files with embedded `## Version History` sections:

- `knowledge/collaboration-framework/SKILL.md`
- `knowledge/collaboration-framework/guides/AI-CONSTITUTION-SUPPLEMENT.md`
- `knowledge/engineering-methods/guides/AI-ENGINEERING-METHODOLOGY.md`
- `knowledge/work-verification/templates/LEDGER-DISCIPLINE.md`
- `knowledge/code-auditing/guides/CODE-AUDIT.md`
- `knowledge/project-management/guides/PROJECT-MANAGEMENT.md`

Current misplaced version-history file:

- `knowledge/project-management/guides/version-history.md`

The accepted Arc08 rule is that component history belongs in a sibling
`version-history.md` beside each component `SKILL.md`, not under `guides/` and
not embedded in component guides/templates unless a later slice records a
specific exception.

## Framework Component Roots

Framework component roots in scope for version-history normalization:

- `knowledge/collaboration-framework/`
- `knowledge/engineering-methods/`
- `knowledge/project-management/`
- `knowledge/work-verification/`
- `knowledge/testing/`
- `knowledge/code-auditing/`
- `knowledge/agent-coordination/`
- `knowledge/contribution-style/`

## Expedited Mode Source Surfaces

Current source surfaces that mention Expedited Mode:

- `knowledge/project-management/guides/PROJECT-MANAGEMENT.md`
- `knowledge/collaboration-framework/SKILL.md`
- `knowledge/project-management/guides/version-history.md`

The source inventory found current Expedited Mode wording that describes commit
and close/advance behavior, but does not yet explicitly say Expedited Mode
means no shortcuts, no skipped validation, no weaker evidence/review, no
inferred source scope, no timeline interpretation, and no override of explicit
operator approval gates.

## Planning Validation

Planning checkout `git diff --check` is required before commit and is recorded
in the closing report after the Slice01 planning artifacts are written.
