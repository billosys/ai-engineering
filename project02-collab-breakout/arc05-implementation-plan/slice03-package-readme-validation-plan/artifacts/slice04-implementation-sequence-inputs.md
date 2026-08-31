# Slice04 Implementation Sequence Inputs

```yaml
project: project02-collab-breakout
arc: arc05-implementation-plan
slice: slice03-package-readme-validation-plan
handoff: slice04-implementation-sequence-synthesis
status: proposed-done
source-files-edited: false
```

## Boundary

These are inputs for Slice04 implementation sequence synthesis. They are not
source-edit authorization, no source edits were made in Slice03, and source
files remain untouched.

## Ordered Concerns For Slice04

1. Establish the final source-edit order for component roots, starting with
   source extraction/migration before package target changes.
2. Decide compatibility for top-level `SKILL.md` and old source paths before
   README route text changes.
3. Plan component `SKILL.md` entrypoint creation and `version-history.md`
   migration before `ALL_SKILL_FILES` validation changes.
4. Plan Makefile package targets, `INSTALL_ZIPS`, `CF_FILES`, and aggregate
   behavior after component payloads are known.
5. Plan README updates after package names, installed routes, and source paths
   are stable.
6. Plan package-path and link repairs before adding any
   `package-path-exceptions.tsv` row.
7. Plan generated zip validation after Makefile targets and package-local
   links exist.
8. Preserve CCDP separation throughout; CCDP validation gates are only needed
   if CCDP source or `ccdp.zip` packaging is touched.

## Source-Edit Risks

| risk | Why it matters | Mitigation input |
|------|----------------|------------------|
| source-edit ordering breaks readers | Moving top-level `SKILL.md` before README and Makefile routes are ready can strand source checkout users. | Sequence compatibility shim or README route update with the move. |
| package paths fail after split | Cross-component relative links may escape generated package roots. | Use package-local links inside packages and installed skill route wording across components. |
| Makefile list drift | `INSTALL_ZIPS`, `ALL_SKILL_FILES`, `CF_FILES`, component targets, `make all`, and `make collab-framework` must agree. | Use one component list or closely-scoped package variables rather than duplicating names by hand. |
| generated zip payload surprises users | `collaboration-framework.zip` keeps its name but changes from monolith to composer. | Record migration note in README and `collaboration-framework/version-history.md`. |
| provenance loss | Old prompt names and histories can vanish during moves. | Carry `version-history.md` entries and migration notes into each component. |
| exception sprawl | Broad package-path exceptions can hide real hard failures. | Prefer link repair; require explicit rationale and expiration for exceptions. |

## Validation Gates For Slice04 To Preserve

- `make check-skills` must cover every component `SKILL.md`.
- `make check-package-paths` must cover every generated skill zip listed in
  `INSTALL_ZIPS`.
- `make all` must build all skill zips after component targets are added.
- `make collab-framework` must still build the composer package.
- Component package targets should validate package roots and content lists.
- `scripts/check-package-paths --check-exceptions-only` should pass after any
  package-path exception edits.
- `make ccdp-package` and `make check-ccdp-package` should run only if CCDP
  surfaces are touched.
- `git diff --check` should pass for the implementation plan and later source
  edits.

## Open Questions For Slice04

- Should top-level `SKILL.md` remain as a temporary source compatibility shim,
  or should README/source routes move directly to `collaboration-framework/SKILL.md`?
- Should Makefile use a generic component-packaging helper that supports
  optional `guides/`, `templates/`, `examples/`, and `version-history.md`?
- Should `collaboration-framework.zip` ever vendor specialist component docs
  for offline generated zip use, or should it remain composer-only?
- Which package-path warnings are acceptable after link repair, and which must
  become hard failures in the implementation sequence?
- How should the implementation slices divide mechanical moves from new prose
  for `engineering-methods`, `testing`, and `agent-coordination`?
