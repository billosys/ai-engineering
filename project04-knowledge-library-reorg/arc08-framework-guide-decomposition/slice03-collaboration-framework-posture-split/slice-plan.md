# Slice 03: Collaboration-Framework Posture Guide Split

```yaml
project: project04-knowledge-library-reorg
arc: arc08-framework-guide-decomposition
slice: slice03-collaboration-framework-posture-split
status: verified-closed
opened-by: CDC
opened-on: 2026-09-04
source_checkout: /Users/oubiwann/lab/billosys/ai-engineering
planning_checkout: /Users/oubiwann/lab/billosys/ai-engineering/.worktrees/planning
source-files-edited: authorized
operating-mode: expedited
artifact_home: artifacts/
depends-on: slice02-project-management-process-history/cdc-verification.md
```

## Goal

Split the collaboration-framework posture monolith into the four approved
numbered guides while preserving source meaning, improving selective loading,
and keeping package/install behavior coherent.

## Scope

In scope:

- Split `knowledge/collaboration-framework/guides/AI-CONSTITUTION-SUPPLEMENT.md`
  into the approved guide sequence:
  - `knowledge/collaboration-framework/guides/01-posture-and-ethics.md`
  - `knowledge/collaboration-framework/guides/02-structural-pulls.md`
  - `knowledge/collaboration-framework/guides/03-collaborative-rights.md`
  - `knowledge/collaboration-framework/guides/04-component-route-table.md`
- Preserve the semantic substance of the monolith while making each target
  guide loadable on its own.
- Remove the old monolith as a live load target, or retain only an explicitly
  justified compatibility/provenance stub if source evidence requires it.
- Create or update `knowledge/collaboration-framework/version-history.md` as
  the sibling history file for collaboration-framework component changes.
- Reconcile embedded `## Version History` material from the old monolith into
  the sibling history file.
- Update `knowledge/collaboration-framework/SKILL.md` route text and component
  route table to use the new numbered guides.
- Preserve Slice02 Expedited Mode guardrail wording.
- Update package/build surfaces affected by the split, including `Makefile`,
  package path exceptions, and staging scripts if required.
- Repair live references in README/docs/AGENTS/SKILL/release notes that point
  at `AI-CONSTITUTION-SUPPLEMENT.md`.
- Create Slice03 planning evidence artifacts under `artifacts/` and close the
  slice with explicit source and planning commits.

Out of scope:

- Splitting `AI-ENGINEERING-METHODOLOGY.md`.
- Normalizing non-collaboration-framework component histories except for direct
  route repairs required by this split.
- Changing the approved guide names or order.
- Changing public skill kind/topology vocabulary.
- Committing generated zips, `build/`, or `target/skills`.

## Support Inputs

- `../slice01-split-map-version-history-confirmation/artifacts/operator-confirmation-packet.md`
- `../slice01-split-map-version-history-confirmation/artifacts/current-monolith-and-history-inventory.md`
- `../slice01-split-map-version-history-confirmation/artifacts/source-impact-and-validation-plan.md`
- `../slice02-project-management-process-history/cdc-verification.md`
- `../../artifacts/operator-accepted-architecture.md`
- `../../artifacts/component-file-layout-plan.md`
- Arc08 `arc-plan.md` and `ledger.md`

## Expected Artifacts

- `artifacts/posture-split-map.md`
- `artifacts/source-route-repair-map.md`
- `artifacts/version-history-reconciliation.md`
- `artifacts/source-validation-results.md`

## Verification Approach

CC should preserve content deliberately, not mechanically chop the file at
headings without checking readability. The new guides should have clear
standalone openings and cross-routes where useful. Source validation must cover
local links, package paths, generated collaboration-framework package shape,
and absence or explicit disposition of the old monolith path.

## Exit Criteria

- The four approved numbered collaboration-framework guides exist.
- The old `AI-CONSTITUTION-SUPPLEMENT.md` path is absent as a live load target
  or explicitly compatibility/provenance-dispositioned.
- `knowledge/collaboration-framework/SKILL.md` routes to the new guides and
  preserves Slice02 Expedited Mode guardrails.
- Collaboration-framework version history lives in sibling
  `knowledge/collaboration-framework/version-history.md`.
- README/docs/AGENTS/SKILL/release-note references to the old monolith are
  repaired or explicitly dispositioned.
- `make check-skills`, `make collab-framework`, and `make check-package-paths`
  pass with zero hard failures.
- Generated `collaboration-framework.zip` contains the new numbered guides and
  does not expose the old monolith path as the live route.
- Source and planning commits are created with explicit file lists and both
  required co-author trailers.

## CDC Closure

Closed by CDC verification on 2026-09-04.

- Source commit verified:
  `e7ba785bf8c48ef061f69f9d90d176030b62dfc4`
- Planning close packet verified:
  `5de33d7fcd49d6de80737f730d3e92f69ea4089b`
- Planning close-hash follow-up verified:
  `00855d161d264534c25a673bd9c2b5eeb0cf70a4`
- Verification artifact:
  `cdc-verification.md`
