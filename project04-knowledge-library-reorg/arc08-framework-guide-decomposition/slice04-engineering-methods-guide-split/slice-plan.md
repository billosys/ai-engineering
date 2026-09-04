# Slice 04: Engineering-Methods Guide Split

```yaml
project: project04-knowledge-library-reorg
arc: arc08-framework-guide-decomposition
slice: slice04-engineering-methods-guide-split
status: open
opened-by: CDC
opened-on: 2026-09-04
source_checkout: /Users/oubiwann/lab/billosys/ai-engineering
planning_checkout: /Users/oubiwann/lab/billosys/ai-engineering/.worktrees/planning
source-files-edited: authorized
operating-mode: expedited
artifact_home: artifacts/
depends-on: slice03-collaboration-framework-posture-split/cdc-verification.md
```

## Goal

Split the engineering-methods methodology monolith into the six accepted
numbered guides while preserving source meaning, improving selective loading,
and keeping collaboration-framework package/install behavior coherent.

## Scope

In scope:

- Split `knowledge/engineering-methods/guides/AI-ENGINEERING-METHODOLOGY.md`
  into the accepted guide sequence:
  - `knowledge/engineering-methods/guides/01-engineering-methodology.md`
  - `knowledge/engineering-methods/guides/02-knowledge-substrate.md`
  - `knowledge/engineering-methods/guides/03-process-rigour.md`
  - `knowledge/engineering-methods/guides/04-operational-routing.md`
  - `knowledge/engineering-methods/guides/05-component-boundary-analysis.md`
  - `knowledge/engineering-methods/guides/06-source-package-release-gates.md`
- Preserve the semantic substance of the monolith while making each target
  guide loadable on its own.
- Remove the old monolith as a live load target, or retain only an explicitly
  justified compatibility/provenance stub if source evidence requires it.
- Create or update `knowledge/engineering-methods/version-history.md` as the
  sibling history file for engineering-methods component changes.
- Reconcile embedded `## Version History` material from the old monolith into
  the sibling history file.
- Update `knowledge/engineering-methods/SKILL.md` route text to use the new
  numbered guides.
- Update collaboration-framework route surfaces, including
  `knowledge/collaboration-framework/SKILL.md` and
  `knowledge/collaboration-framework/guides/04-component-route-table.md`.
- Preserve Slice02 Expedited Mode guardrails and Slice03 posture guide routes.
- Update package/build surfaces affected by the split, including `Makefile`,
  package path exceptions, and staging scripts if required.
- Repair live references in README/docs/AGENTS/SKILL/release notes that point
  at `AI-ENGINEERING-METHODOLOGY.md`.
- Create Slice04 planning evidence artifacts under `artifacts/` and close the
  slice with explicit source and planning commits.

Out of scope:

- Renaming or changing the Slice03 collaboration-framework posture guides.
- Normalizing remaining non-engineering-methods component histories except for
  direct route repairs required by this split.
- Changing the approved guide names or order.
- Changing public skill kind/topology vocabulary.
- Committing generated zips, `build/`, or `target/skills`.

## Support Inputs

- `../slice01-split-map-version-history-confirmation/artifacts/operator-confirmation-packet.md`
- `../slice01-split-map-version-history-confirmation/artifacts/current-monolith-and-history-inventory.md`
- `../slice01-split-map-version-history-confirmation/artifacts/source-impact-and-validation-plan.md`
- `../slice02-project-management-process-history/cdc-verification.md`
- `../slice03-collaboration-framework-posture-split/cdc-verification.md`
- `../../artifacts/operator-accepted-architecture.md`
- `../../artifacts/component-file-layout-plan.md`
- Arc08 `arc-plan.md` and `ledger.md`

## Expected Artifacts

- `artifacts/methodology-split-map.md`
- `artifacts/source-route-repair-map.md`
- `artifacts/version-history-reconciliation.md`
- `artifacts/source-validation-results.md`

## Verification Approach

CC should do the semantic work required to preserve the methodology guide's
substance. Do not perform a heading-only split unless the resulting guides are
independently useful, correctly cross-routed, and easier to load selectively.

Validation must cover local links, package paths, generated
collaboration-framework package shape, and absence or explicit disposition of
the old methodology monolith path. Treat Expedited Mode as only the explicit
process behavior recorded in Arc08; do not infer source scope, reduce scope,
skip checks, weaken evidence, change review quality, or bypass approval gates.

## Exit Criteria

- The six accepted numbered engineering-methods guides exist.
- The old `AI-ENGINEERING-METHODOLOGY.md` path is absent as a live load target
  or explicitly compatibility/provenance-dispositioned.
- `knowledge/engineering-methods/SKILL.md` routes to the new numbered guides.
- Collaboration-framework routes refer to the new engineering-methods guide
  set without regressing Slice03 posture routes.
- Engineering-methods version history lives in sibling
  `knowledge/engineering-methods/version-history.md`.
- README/docs/AGENTS/SKILL/release-note references to the old monolith are
  repaired or explicitly dispositioned.
- `make check-skills`, `make collab-framework`, and `make check-package-paths`
  pass with zero hard failures.
- Generated `collaboration-framework.zip` contains the new numbered
  engineering-methods guides and does not expose the old monolith path as the
  live route.
- Source and planning commits are created with explicit file lists and both
  required co-author trailers.
