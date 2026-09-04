# CC Prompt: Arc08 Slice04 Engineering-Methods Guide Split

You are CC working in Project04 Arc08 Slice04.

## Required Context

Read these files before editing:

- `/Users/oubiwann/lab/billosys/ai-engineering/AGENTS.md`
- `/Users/oubiwann/lab/billosys/ai-engineering/knowledge/collaboration-framework/SKILL.md`
- `/Users/oubiwann/lab/billosys/ai-engineering/knowledge/project-management/SKILL.md`
- `/Users/oubiwann/lab/billosys/ai-engineering/knowledge/project-management/guides/PROJECT-MANAGEMENT.md`
- `/Users/oubiwann/lab/billosys/ai-engineering/knowledge/work-verification/templates/LEDGER-DISCIPLINE.md`
- `project04-knowledge-library-reorg/project-plan.md`
- `project04-knowledge-library-reorg/arc08-framework-guide-decomposition/arc-plan.md`
- `project04-knowledge-library-reorg/arc08-framework-guide-decomposition/ledger.md`
- `project04-knowledge-library-reorg/arc08-framework-guide-decomposition/slice04-engineering-methods-guide-split/slice-plan.md`
- `project04-knowledge-library-reorg/arc08-framework-guide-decomposition/slice04-engineering-methods-guide-split/ledger.md`
- `project04-knowledge-library-reorg/arc08-framework-guide-decomposition/slice01-split-map-version-history-confirmation/artifacts/operator-confirmation-packet.md`
- `project04-knowledge-library-reorg/arc08-framework-guide-decomposition/slice01-split-map-version-history-confirmation/artifacts/current-monolith-and-history-inventory.md`
- `project04-knowledge-library-reorg/arc08-framework-guide-decomposition/slice01-split-map-version-history-confirmation/artifacts/source-impact-and-validation-plan.md`
- `project04-knowledge-library-reorg/arc08-framework-guide-decomposition/slice02-project-management-process-history/cdc-verification.md`
- `project04-knowledge-library-reorg/arc08-framework-guide-decomposition/slice03-collaboration-framework-posture-split/cdc-verification.md`
- `project04-knowledge-library-reorg/artifacts/operator-accepted-architecture.md`
- `project04-knowledge-library-reorg/artifacts/component-file-layout-plan.md`

## Task

Implement Slice04 exactly as planned: split
`knowledge/engineering-methods/guides/AI-ENGINEERING-METHODOLOGY.md` into the
six accepted numbered engineering-methods guides:

1. `knowledge/engineering-methods/guides/01-engineering-methodology.md`
2. `knowledge/engineering-methods/guides/02-knowledge-substrate.md`
3. `knowledge/engineering-methods/guides/03-process-rigour.md`
4. `knowledge/engineering-methods/guides/04-operational-routing.md`
5. `knowledge/engineering-methods/guides/05-component-boundary-analysis.md`
6. `knowledge/engineering-methods/guides/06-source-package-release-gates.md`

Do the semantic work required to keep the framework just as usable as before
and easier to load selectively. Preserve the substance of the old monolith;
do not reduce the material to a mechanical heading split if the resulting
guides need introductions, route notes, cross-links, or small connective
adjustments.

Normalize engineering-methods history into
`knowledge/engineering-methods/version-history.md`. Do not leave component
history under `guides/` merely because guide files changed.

Update every affected live route, including:

- `knowledge/engineering-methods/SKILL.md`
- `knowledge/collaboration-framework/SKILL.md`
- `knowledge/collaboration-framework/guides/04-component-route-table.md`
- `Makefile`
- `scripts/stage-skill-entrypoint`, if package-only transforms are needed
- `assets/packaging/path-exceptions.tsv`, if and only if package validation
  requires an explicit exception
- README/docs/AGENTS/SKILL/release-note references that point to the old
  methodology monolith

Preserve the Slice02 Expedited Mode wording and Slice03 posture guide routes.
Expedited Mode means only the explicit commit, close, and advance behaviors
recorded in the written instructions. It does not authorize shortcuts, skipped
validation, reduced evidence, weaker CDC review, inferred source scope, any
reduction or other change in scope, timeline interpretation, or approval-gate
override.

## Required Artifacts

Create these Slice04 artifacts:

- `artifacts/methodology-split-map.md`
- `artifacts/source-route-repair-map.md`
- `artifacts/version-history-reconciliation.md`
- `artifacts/source-validation-results.md`

The artifacts must cite the support inputs above and explicitly map:

- old monolith sections to new guide files;
- semantic preservation and selective loading checks;
- old-path references that were repaired or intentionally dispositioned;
- version-history material moved/reconciled into the sibling history file;
- validation commands and results.

## Required Validation

Run and record results for:

- `git diff --check`
- a focused local Markdown link check over every touched README/docs/AGENTS/SKILL/guide/history/release-note file
- `make check-skills`
- `make collab-framework`
- `make check-package-paths`
- generated `collaboration-framework.zip` inspection proving the six new
  engineering-methods guides are present and
  `AI-ENGINEERING-METHODOLOGY.md` is absent as the live package route

Do not run package-building targets concurrently; they share `build/`.

## Commit Requirements

Use explicit file lists for every commit.

Create a source commit for the implementation if source files changed. Do not
commit generated zips, `build/`, or `target/skills`.

Create a planning commit for:

- `arc08-framework-guide-decomposition/slice04-engineering-methods-guide-split/artifacts/methodology-split-map.md`
- `arc08-framework-guide-decomposition/slice04-engineering-methods-guide-split/artifacts/source-route-repair-map.md`
- `arc08-framework-guide-decomposition/slice04-engineering-methods-guide-split/artifacts/version-history-reconciliation.md`
- `arc08-framework-guide-decomposition/slice04-engineering-methods-guide-split/artifacts/source-validation-results.md`
- `arc08-framework-guide-decomposition/slice04-engineering-methods-guide-split/ledger.md`
- `arc08-framework-guide-decomposition/slice04-engineering-methods-guide-split/closing-report.md`

Every assistant-authored commit must include:

```text
Co-authored-by: Codex <noreply@openai.com>
Co-authored-by: Billo AI <ai-engineering@billo.systems>
```

## Completion Report

Report:

- source commit hash, or `none` if no source edit was needed;
- planning commit hash;
- exact source files changed;
- exact planning files changed;
- validation results;
- final source and planning checkout status;
- any bubble-up for Slice05.

Do not create `cdc-verification.md`; CDC will verify independently.
