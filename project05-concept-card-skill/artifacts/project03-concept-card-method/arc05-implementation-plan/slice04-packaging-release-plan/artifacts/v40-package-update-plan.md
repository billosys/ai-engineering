# v4.0 Package Update Plan

```yaml
project: project03-concept-card-method
arc: arc05-implementation-plan
slice: slice04-packaging-release-plan
artifact: v40-package-update-plan
status: proposed-done
planned-package-name: concept-card-method.zip
planned-source-home: knowledge/concept-card-method/
```

## Purpose

This artifact plans future Makefile and package-list requirements for the
v4.0 concept-card method skill. It preserves the verified Slice02
package-compatible `guides/` layout and the verified Slice03
documentation-only validator-code scope.

This plan is not source implementation. It is out of scope to edit source,
implement package targets, edit package lists, create package-path exception
rows, build generated zips, perform package release, implement executable
validator-code, implement release gates, claim release readiness, create
runtime services, GraphRAG, graph database, ontology database, memory runtime,
CCDP service, or live extraction behavior.

## Package Target Decision

Accepted Slice04 package target names for the future implementation plan:

- Add a `concept-card-method` Makefile target that packages
  `knowledge/concept-card-method/SKILL.md` plus
  `knowledge/concept-card-method/guides/`.
- The generated zip should be `concept-card-method.zip`, named from the
  future SKILL.md frontmatter `name: concept-card-method`.
- Add a `concept-card-method-clean` target only if the generic packaging
  pattern needs a target-specific staging clean step.

The planned target should reuse the existing `pack_skill` pattern if the
implementation can keep all packaged surfaces under `guides/`. No package
behavior change is required by the verified Slice02 layout.

## Package List Edits

Future implementation should update the source Makefile package list surfaces:

- add `concept-card-method.zip` to `INSTALL_ZIPS`;
- add `knowledge/concept-card-method/SKILL.md` to `ALL_SKILL_FILES`;
- add `concept-card-method` to `.PHONY`;
- add `concept-card-method` to the `skills` aggregate;
- ensure `all` includes it through `skills`;
- ensure `install` and `uninstall` include it through `INSTALL_ZIPS` and
  `INSTALL_SKILLS`;
- update `help` text to list the new package target and generated zip.

These are future package list edits. Slice04 does not edit the Makefile.

## Install and Clean Behavior

Install behavior should follow the existing skill pattern:

- `make concept-card-method` creates `concept-card-method.zip`;
- `make install` builds all installable skill zips and unpacks
  `concept-card-method.zip` into `$(INSTALL_DIR)`;
- the installed package root should be `concept-card-method/`;
- `make uninstall` removes `$(INSTALL_DIR)/concept-card-method`;
- `make clean` removes `/build` and generated zip files, including
  `concept-card-method.zip`.

Clean behavior should not remove source files under
`knowledge/concept-card-method/`.

## Generated Archive Behavior

The generated archive behavior should match existing skills:

- generated archive: `concept-card-method.zip`;
- generated zip location: repository root;
- package root inside zip: `concept-card-method/`;
- package contents: `concept-card-method/SKILL.md` plus
  `concept-card-method/guides/**`;
- generated zip output remains ignored by existing `/*.zip` ignore behavior;
- intermediate staging remains under `build/`, which is ignored and cleaned.

The generated zip policy is to produce a local build artifact only during
future implementation verification. The generated archive is not committed
unless a later release owner explicitly changes repository policy.

## Package-Path Checks and Exceptions

Future implementation should add the package to package-path checks through
the same generated archive path used by `make check-package-paths`.

Package-path exception policy:

- avoid new `package-path-exceptions.tsv` rows by making package-local links
  resolve inside `concept-card-method/`;
- add a package-path exception only for intentional source-only provenance or
  intentionally excluded material that cannot be represented as a package-local
  link;
- every exception row must include package, document, target, classification,
  disposition, reason, source, and expires;
- exception rows should be treated as tracked debt or explicit policy, not as
  a way to hide broken package links.

Slice04 plans package-path checks and package-path exception rules, but does
not edit `package-path-exceptions.tsv`.

## Package Update Boundary

The package update boundary is:

- in scope for future implementation: Makefile target, `INSTALL_ZIPS`,
  `ALL_SKILL_FILES`, `.PHONY`, `skills`, help text, package-path checks,
  install behavior, clean behavior, generated archive verification, and README
  package expectation text;
- out of scope for Slice04: source edits, source implementation, generated
  zips, package release, release readiness, executable validator-code,
  runtime services, GraphRAG, graph database, ontology database, memory
  runtime, CCDP service, and live extraction.

## Later-Slice Routing

Slice05 owns implementation-plan synthesis, implementation slice
recommendations, deferral register, source edit sequence, and Project03 close
input. Slice05 should compose this package update plan with the verified
layout, schema, validation, discoverability, release gate, and source
version-history plans.

Slice04 found no packaging fact that requires Arc05 re-sequencing, a new
slice, or a scope correction.

Continuity note: this plan preserves the Slice02 SKILL.md plus sibling guides
package contract and the Slice03 documentation-only validator scope; executable
validator-code deferred remains the accepted first-implementation boundary.
