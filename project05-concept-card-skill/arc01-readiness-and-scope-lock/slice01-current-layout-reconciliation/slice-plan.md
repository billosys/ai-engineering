# Slice01 Plan: Current Layout Reconciliation

```yaml
project: project05-concept-card-skill
arc: arc01-readiness-and-scope-lock
slice: slice01-current-layout-reconciliation
status: open
opened: 2026-09-06
artifact-home: artifacts/
```

## Goal

Produce the current evidence map that lets Project05 implementation begin
without duplicating stale Project03 assumptions or pre-Project04 layout
decisions.

## In Scope

- Read Project05's seed artifacts and classify which claims are still current,
  which are superseded, and which remain useful provenance.
- Read Project04 close/layout/package evidence and the current source tree
  enough to identify present skill layout, package behavior, docs/library
  discoverability, version-history practice, and generated-zip gates.
- Confirm the accepted Project05 naming and scope decisions:
  `document-extraction`, `concept-cards`, and future `ontology-engineering`.
- Define exact expected source/package surfaces for the two required skills.
- Produce a refreshed implementation roadmap that preserves the
  nondeferrable objectives.

## Out Of Scope

- Source edits under `knowledge/`, `docs/`, `Makefile`, scripts, or release
  notes.
- Implementing either skill.
- Closing Project05, Arc01, or later arcs.
- Deciding to defer `document-extraction` or `concept-cards`.

## Durable Artifacts

Write these files under `artifacts/`:

- `project05-current-source-surface-inventory.md`
- `project05-artifact-relevance-register.md`
- `project05-naming-and-scope-register.md`
- `project05-package-surface-requirements.md`
- `project05-implementation-roadmap-update.md`

## Verification Approach

Use direct file inspection and repository commands against the source checkout
and planning checkout. Every artifact should cite the files or commands it
uses as evidence. The slice ledger must be updated row by row before close.

## Exit Criteria

- All five durable artifacts exist.
- The artifacts distinguish current source facts from historical planning
  evidence.
- The artifacts state that `document-extraction` and `concept-cards` are
  required Project05 implementation outputs.
- The artifacts identify the current package-layout implication for sibling
  `templates/`, `examples/`, and any `reference/` or validation support.
