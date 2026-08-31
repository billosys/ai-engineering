# Slice03 Package README Validation Inputs

```yaml
project: project02-collab-breakout
arc: arc05-implementation-plan
slice: slice02-component-contract-file-plan
handoff: slice03-package-readme-validation-plan
status: proposed-done
source-files-edited: false
```

## Boundary

These are non-final inputs for Slice03 package, README, SKILL.md, Makefile,
generated zip, package-path exception, validation, and migration planning.
There are no source edits in Slice02; source files remain untouched.

## Concrete Inputs For Slice03

| Surface | Slice03 input | Not-final boundary |
|---------|---------------|--------------------|
| package names and roots | Plan whether every accepted component ships as a generated zip with a root matching `collaboration-framework`, `engineering-methods`, `project-management`, `work-verification`, `testing`, `code-auditing`, `agent-coordination`, and `contribution-style`. | Component names are accepted, but package target mechanics remain open. |
| README | Add a route model for composed use through `collaboration-framework`, standalone use through individual components, source checkout use, generated zip use, installed skill use, and CCDP separation. | README prose is not written in Slice02. |
| SKILL.md | Plan top-level composer `SKILL.md` changes and new component `SKILL.md` entrypoints, including description lengths and route tables. | Exact entrypoint text and version bumps are implementation-slice work. |
| Makefile | Plan updates to `INSTALL_ZIPS`, `ALL_SKILL_FILES`, package targets, `CF_FILES`, aggregate targets, and help text. | Do not edit Makefile until package plan closes. |
| generated zip | Decide which zips are built, installed, ignored, and validated; preserve `collaboration-framework.zip` as composer and CCDP as `ccdp.zip`. | Generated archives remain release artifacts and should not be committed unless policy changes. |
| package-path exception | Plan any new `package-path-exceptions.tsv` rows only after preferring package-local link repairs. | No exceptions are justified merely because the old monolith had them. |
| validation | Plan `make check-skills`, `make check-package-paths`, and any component-specific package build commands. Preserve `make check-ccdp-package` only for CCDP changes. | Command sequencing is Slice03 scope. |
| migration | Plan compatibility for old source paths such as `docs/CLAUDE-CODE-COVERAGE.md` and top-level `SKILL.md`, including whether shims, moves, or copies are needed. | The migration strategy must not erase provenance or silently move history. |

## Open Questions

- What exact Makefile shape should package eight component skills without
  duplicating the old monolithic `CF_FILES` pattern?
- Should `collaboration-framework.zip` contain only the composer and local
  posture/route guides, or should it vendor any specialist support files for
  offline packaged use?
- How should README present individual component loading without making the
  daily-driver composer look deprecated?
- Which source-clone links should remain relative paths, and which package
  links should become installed-skill route guidance?
- Does `templates/LEDGER-DISCIPLINE.md` ship only under
  `work-verification/templates/`, or also as source provenance during
  migration?
- What compatibility note preserves the old `CLAUDE-CODE-COVERAGE.md` name
  while making `testing` the accepted component?
- Which package-path exception rows are still legitimate after package-local
  links are repaired?

## Required Slice03 Checks To Plan

- `make check-skills` covers every component `SKILL.md`.
- `make check-package-paths` validates generated component zips and package
  links.
- README routes distinguish source checkout, generated zip, unzipped/install,
  and installed skill use.
- CCDP separation remains explicit and `ccdp.zip` is not treated as a skill
  component package.
- The final package/README/validation plan records no source edits from
  Slice02 and confirms source files remain untouched before implementation
  planning continues.
