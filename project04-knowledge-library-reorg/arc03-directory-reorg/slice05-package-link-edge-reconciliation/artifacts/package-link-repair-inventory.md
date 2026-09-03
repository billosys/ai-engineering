# Package Link Repair Inventory

Date: 2026-09-02
Slice: Arc03 Slice05 package/link edge reconciliation
Source checkout: `/Users/oubiwann/lab/billosys/ai-engineering`
Baseline source commit: `873a5502acef9c087cefd78d468cf6d123a27341`
Final source commit: `9b6d5d83d9c8debd977609aa1118004e89e2c895`

## Scope

This inventory reviews package-local link behavior after the Arc03 Slice04
component/method/template moves. The Slice05 rule was repair before exception:
fix package-local links and package lists when possible; keep only narrow,
auditable exceptions when the reference intentionally points outside the package
or represents deferred historical/source prose.

## Reviewed Surfaces

- `Makefile` package lists and roots, including `CF_FILES`, `INSTALL_ZIPS`,
  `CCDP_NAME`, `CCDP_ZIP`, `ccdp-package`, and `check-ccdp-package`.
- `SKILL.md` top-level wayfinder and collaboration-framework package entry.
- `package-path-exceptions.tsv` existing exception register.
- Generated `collaboration-framework.zip` package-local contents.
- Generated Biome packages:
  - `biome-js-linter.zip`
  - `biome-linter.zip`
- Generated CCDP package:
  - `ccdp.zip`

## Collaboration Framework Package

`make collab-framework` generated a package root that includes the moved
component roots:

- `collaboration-framework/SKILL.md`
- `collaboration-framework/knowledge/collaboration-framework/`
- `collaboration-framework/knowledge/project-management/`
- `collaboration-framework/knowledge/code-auditing/`
- `collaboration-framework/knowledge/testing/`
- `collaboration-framework/knowledge/engineering-methods/`
- `collaboration-framework/knowledge/work-verification/`
- `collaboration-framework/knowledge/contribution-style/`
- `collaboration-framework/knowledge/agent-coordination/`

Result: package-local moved-path coverage is present. No missing owner-root
package entry was found for the accepted Slice04 moves.

## Link Repair Outcome

`make check-package-paths` completed successfully with exit 0 after the CCDP
freshness repair. Warning-only path dispositions remain governed by
`package-path-exceptions.tsv`; no broad exception was added or widened.

hard failures: 0.

## Reconciliation Notes

- The first source defect encountered was not a broken package-local link in the
  collaboration framework package; it was a stale assembled CCDP protocol file
  detected by `make ccdp-package`.
- The repair was to run `make ccdp`, refreshing
  `protocols/ccdp/composite-cognition-dispatch-protocol.md`.
- The resulting source commit was limited to that generated protocol refresh.
- Generated zip artifacts were rebuilt for validation and left uncommitted.
