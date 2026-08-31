# Package Target Plan

```yaml
project: project02-collab-breakout
arc: arc05-implementation-plan
slice: slice03-package-readme-validation-plan
status: proposed-done
artifact-status: package target plan
source-files-edited: false
```

## Grounding

This Slice03 plan consumes verified Slice01 release validation evidence,
verified Slice02 component contract and file layout evidence, the Slice02
package/source contract register, and the Arc04
`operator-accepted-architecture`. It plans the package release surface without
editing source files, Makefile targets, package exceptions, README, `SKILL.md`,
or generated zip artifacts.

## Package Targets

| Component | Package root | generated zip | install behavior | Makefile impact | Validation |
|-----------|--------------|---------------|------------------|-----------------|------------|
| `collaboration-framework` | `collaboration-framework/` | Keep `collaboration-framework.zip` as the daily-driver composer package. | Keep installed skill route `/collaboration-framework`. It remains installed by default. | Keep `make collab-framework`, but change `CF_FILES` to composer-local files after implementation. Include composer `SKILL.md` in `ALL_SKILL_FILES` and keep the zip in `INSTALL_ZIPS`. | `make collab-framework`, `make check-skills`, `make check-package-paths`, and `make all`. |
| `engineering-methods` | `engineering-methods/` | Add `engineering-methods.zip`. | Install by default as `/engineering-methods`. | Add component package target, add zip to `INSTALL_ZIPS`, add `engineering-methods/SKILL.md` to `ALL_SKILL_FILES`, and include in aggregate `make all`. | `make check-skills`, component package target, `make check-package-paths`, and `make all`. |
| `project-management` | `project-management/` | Add `project-management.zip`. | Install by default as `/project-management`. | Add package target with `guides/` and `examples/`, add zip to `INSTALL_ZIPS`, add `project-management/SKILL.md` to `ALL_SKILL_FILES`, and include in aggregate `make all`. | `make check-skills`, component package target, `make check-package-paths`, and `make all`. |
| `work-verification` | `work-verification/` | Add `work-verification.zip`. | Install by default as `/work-verification`. | Add package target with `guides/` and `templates/`, add zip to `INSTALL_ZIPS`, add `work-verification/SKILL.md` to `ALL_SKILL_FILES`, and include in aggregate `make all`. | `make check-skills`, component package target, `make check-package-paths`, and `make all`. |
| `testing` | `testing/` | Add `testing.zip`. | Install by default as `/testing`. | Add package target with `guides/`, add zip to `INSTALL_ZIPS`, add `testing/SKILL.md` to `ALL_SKILL_FILES`, and include in aggregate `make all`. | `make check-skills`, component package target, `make check-package-paths`, and `make all`. |
| `code-auditing` | `code-auditing/` | Add `code-auditing.zip`. | Install by default as `/code-auditing`. | Add package target with `guides/`, add zip to `INSTALL_ZIPS`, add `code-auditing/SKILL.md` to `ALL_SKILL_FILES`, and include in aggregate `make all`. | `make check-skills`, component package target, `make check-package-paths`, and `make all`. |
| `agent-coordination` | `agent-coordination/` | Add `agent-coordination.zip`. | Install by default as `/agent-coordination`. | Add package target with `guides/`, add zip to `INSTALL_ZIPS`, add `agent-coordination/SKILL.md` to `ALL_SKILL_FILES`, and include in aggregate `make all`. | `make check-skills`, component package target, `make check-package-paths`, and `make all`. |
| `contribution-style` | `contribution-style/` | Add `contribution-style.zip`. | Install by default as `/contribution-style`. | Add package target with `guides/` and `templates/`, add zip to `INSTALL_ZIPS`, add `contribution-style/SKILL.md` to `ALL_SKILL_FILES`, and include in aggregate `make all`. | `make check-skills`, component package target, `make check-package-paths`, and `make all`. |

## Makefile Shape

Recommended Makefile planning shape:

- Add a `COMPONENT_ZIPS` list containing `collaboration-framework.zip`,
  `engineering-methods.zip`, `project-management.zip`,
  `work-verification.zip`, `testing.zip`, `code-auditing.zip`,
  `agent-coordination.zip`, and `contribution-style.zip`.
- Keep the existing domain/tooling skill list separate so language packages do
  not become accidental dependencies of framework-component packages.
- Make `INSTALL_ZIPS` include `COMPONENT_ZIPS` plus the existing domain/tooling
  zips. CCDP remains outside `INSTALL_ZIPS`.
- Make `ALL_SKILL_FILES` include the eight component `SKILL.md` files plus the
  existing domain/tooling skill files.
- Keep `make collab-framework` as the named composer target.
- Add named component targets for the seven new packages and a framework
  aggregate target if that improves operator ergonomics.
- Keep `make all` as the full skill-bundle aggregate.
- Keep `make install` installing skill zips only. It should not install
  `ccdp.zip`.

## Generated Artifact Policy

- Generated zip files remain ignored release artifacts and should not be
  committed during implementation unless release policy explicitly changes.
- Component generated zip roots should match package roots.
- `collaboration-framework.zip` should contain the composer entrypoint,
  composer-local posture guides, and route table. It should not silently vendor
  every specialist body unless Slice04 records an offline-use reason.
- Specialist generated zip packages should contain their local `SKILL.md`,
  sibling `version-history.md`, `guides/`, and any accepted `templates/` or
  `examples/`.

## CCDP Separation

CCDP separation remains unchanged:

- `ccdp.zip` is a separate protocol package, not a skill component.
- `protocols/ccdp/` remains outside the collaboration-framework component
  package payloads.
- `make ccdp-package` and `make check-ccdp-package` run only when CCDP
  surfaces are touched.
- `make all`, component package targets, and `make install` should not build or
  install `ccdp.zip`.
