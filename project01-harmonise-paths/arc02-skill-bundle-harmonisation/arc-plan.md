# Arc 02: Skill Bundle Harmonisation

```yaml
arc: arc02-skill-bundle-harmonisation
status: active
project: project01-harmonise-paths
depends-on:
  - arc01-distribution-path-contract
blocks:
  - arc03-ccdp-distribution-package
  - arc04-release-and-adoption-hardening
related:
  - Makefile
  - scripts/check-package-paths
  - package-path-exceptions.tsv
  - knowledge/*/SKILL*.md
```

## Capability Statement

This arc burns down package-path warnings in the generated skill bundles while
preserving source-clone usefulness. It applies the Arc 01 contract: use source
edits where one path spelling works in both contexts, use staging-time
transforms where source-root prose should remain source-rooted, keep package
layout expansion rare and justified, and leave CCDP package work to Arc 03.

The arc must not bulk-edit mature guide prose just to satisfy the gate. Mature
language packs may receive packaging transforms or entrypoint-only changes, but
substantive guide restructuring needs a separate operator-approved project.

## Slice Breakdown

### Slice 01: Tooling Entrypoint Links

Status: verified/closed.

Scope: reduce high-confidence bundled-reference warnings in smaller/simple
skill entrypoints where `guides/...` works from both the source skill file and
the packaged skill root. Initial candidates are:

- `knowledge/deno/SKILL-js-linter.md`
- `knowledge/biome/SKILL-js-linter.md`
- `knowledge/biome/SKILL-web-linter.md`
- `knowledge/tailwindcss/SKILL.md`
- `knowledge/cobalt/SKILL.md`

Load-bearing for: proving the cleanest Arc 02 path before touching mature
language packs or generalized staging transforms.

### Slice 02: Collaboration Framework Links

Status: active/opened.

Expected scope: address collaboration-framework/package-management links that
still warn in generated packages, using source edits where one spelling is
true in both contexts and narrow staging transforms where source semantics
must remain source-rooted.

### Slice 03: Mature Entrypoint Staging Transforms

Status: stub.

Expected scope: add or refine package-stage transforms for mature language
skill entrypoints, especially where source-root `knowledge/<domain>/guides/**`
references should package as `guides/**` without bulk source prose churn.

### Slice 04: Warning Policy Tightening

Status: stub.

Expected scope: remove or expire transitional exception rows resolved by Arc
02, decide whether remaining warnings are permanent explicit exceptions or
later-arc work, and prepare Arc 02 for close.

## Dependencies

Arc 02 consumes the executable `make check-package-paths` gate from Arc 01. The
source implementation for the gate and Slice 01 tooling link harmonisation is
committed on `main` at `09d1550`.

## Version History

### v1.0 - 2026-08-29

Initial Arc 02 plan opened after Arc 01 closed. Slice 01 opens on
tooling/simple skill entrypoint links to burn down a small, high-confidence
class before broader framework or mature-language work.

### v1.1 - 2026-08-29

Slice 01 marked verified/closed by CDC. The slice burned targeted
tooling/simple entrypoint bundled-reference warnings from 20 to 0, with total
package-path warnings moving from 426 to 406 and no new hard failures. No Arc
02 plan change is required before Slice 02.

### v1.2 - 2026-08-29

Slice 02 opened on collaboration-framework links after Slice 01 CDC
verification. The scope starts with a generated-package warning baseline and
requires classification before edits so framework methodology examples are not
mechanically rewritten into misleading package paths.
