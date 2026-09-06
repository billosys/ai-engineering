# Arc01 Plan: Readiness And Scope Lock

```yaml
project: project05-concept-card-skill
arc: arc01-readiness-and-scope-lock
status: open
opened: 2026-09-06
depends-on:
  - project03-concept-card-method
  - project04-knowledge-library-reorg
```

## Capability

Arc01 reconciles Project05's historical seed packet with the current
post-Project04 repository. It locks the implementation names, confirms the
source/package surfaces for two live skills, and produces the evidence needed
for implementation arcs to edit source files without inheriting stale layout
assumptions.

This arc is a readiness and scope-lock step, not a deferral gate. Its job is
to make the required implementation safer and more exact.

## Slice Breakdown

| Slice | Scope | Dependencies |
| --- | --- | --- |
| Slice01: Current Layout Reconciliation | Inventory current source/package layout, classify Project03 and Project05 artifacts as current/superseded/deferred evidence, lock names and support-directory policy, and produce the updated implementation roadmap. | Project plan, Project04 close evidence, current source tree. |

## Outputs

Slice01 should produce durable artifacts under its `artifacts/` directory:

- `project05-current-source-surface-inventory.md`
- `project05-artifact-relevance-register.md`
- `project05-naming-and-scope-register.md`
- `project05-package-surface-requirements.md`
- `project05-implementation-roadmap-update.md`

## Arc Exit Criteria

Arc01 closes when Slice01 is closed and its artifacts make the implementation
surface for `document-extraction` and `concept-cards` checkable against the
current repository.

## Version History

### v1.0 - 2026-09-06

Opened Arc01 as the post-Project04 readiness and scope-lock arc for Project05.
