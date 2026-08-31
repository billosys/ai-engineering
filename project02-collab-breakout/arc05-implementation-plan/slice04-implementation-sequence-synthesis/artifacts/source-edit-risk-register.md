# Source-Edit Risk Register

```yaml
project: project02-collab-breakout
arc: arc05-implementation-plan
slice: slice04-implementation-sequence-synthesis
status: proposed-done
artifact-status: source-edit risk register
source-files-edited: false
```

## Grounding

This risk register consumes verified Slice01 implementation surface evidence,
verified Slice02 component contract and migration evidence, verified Slice03
package target / package-path / migration compatibility evidence, and the
operator-accepted architecture. The register is planning-only; source files
remain untouched by this slice.

## Risk Rows

| ID | Risk | Affected surface | Why it matters | Mitigation | Validation or gate |
|----|------|------------------|----------------|------------|--------------------|
| R-1 | top-level SKILL.md compatibility break | Top-level `SKILL.md`, `collaboration-framework/SKILL.md`, README source-checkout route. | Removing or moving the old source path before replacement routes exist can strand source readers and old prompts. | Keep top-level `SKILL.md` as a temporary source-checkout shim during implementation unless the operator explicitly chooses direct removal. Do not package the shim as the composer zip payload. | README migration note, root shim grep, `make collab-framework`, and `make check-skills`. |
| R-2 | old source path references become broken links | `docs/AI-CONSTITUTION-SUPPLEMENT.md`, `docs/AI-ENGINEERING-METHODOLOGY.md`, `docs/PROJECT-MANAGEMENT.md`, `docs/pm/*`, `templates/*`, and old root paths. | Source history and package links can diverge if old paths are deleted without provenance or route replacement. | Convert old source path references to historical/provenance text or source-checkout migration notes; use package-local links for shipped files. | `make check-package-paths`, README link review, version-history provenance checks. |
| R-3 | old prompt name references are silently erased | `docs/CLAUDE-CODE-COVERAGE.md`, `docs/SUBAGENT-DELEGATION-POLICY.md`, `docs/CODE-AUDIT.md`, `docs/CONTRIBUTION-STYLE.md`. | Users may still recognize the old prompt names; erasing them loses migration context. | Preserve old prompt name references as compatibility notes in component `version-history.md`, migration notes, and relevant guides while making accepted component names primary. | Grep for old names in migration/version-history text; CDC checks expansion versus overwrite. |
| R-4 | package root and source root mismatch | Component source roots, generated zip roots, installed skill routes. | Package consumers expect each generated zip to unzip under one root matching the component name. | Make package root equal source root and frontmatter `name:` for all eight components. | Component package targets, `make check-package-paths`, zip root inspection. |
| R-5 | package-local links fail inside generated zips | Component `SKILL.md`, guides, templates, examples. | Relative links that work in the source checkout can escape or break inside a package root. | Use package-local links inside packages and installed-skill route wording across components. Repair links before exceptions. | `make check-package-paths`, generated zip inspection, package-local link scan. |
| R-6 | installed-skill routes are ambiguous | README, route tables, component `SKILL.md` files. | Users need to know when to load `/collaboration-framework` versus a specialist component. | README and route tables name installed-skill routes explicitly: `/engineering-methods`, `/project-management`, `/work-verification`, `/testing`, `/code-auditing`, `/agent-coordination`, and `/contribution-style`. | README route grep, entrypoint route-table review, `make check-package-paths`. |
| R-7 | package-path-exceptions.tsv hides real failures | `package-path-exceptions.tsv`, package-path checker warnings. | Broad exceptions can turn broken package links into accepted warnings. | Add exceptions only after link repair, with package, document, target, classification, disposition, reason, source, and expiration. | `scripts/check-package-paths --check-exceptions-only` when available, `make check-package-paths`, accepted-warning inventory. |
| R-8 | generated zip behavior surprises composer users | `collaboration-framework.zip`, new component zips, Makefile install behavior. | The composer zip keeps its name but changes from monolith to composer-local payload. | State composer-only payload in README and `collaboration-framework/version-history.md`; add seven standalone generated zips installed by default. | `make collab-framework`, `make all`, zip payload inspection, README migration note. |
| R-9 | provenance loss during mechanical moves | Component `version-history.md`, guide histories, template histories. | Mechanical moves can preserve content while losing why the source existed and how it changed. | Seed sibling `version-history.md` files from current source histories and record Project02 breakout as expansion or migration, not silent overwrite. | Version-history review, source-prose preservation review, CDC silent-drop check. |
| R-10 | CCDP separation weakens during package work | `protocols/ccdp/`, `ccdp.zip`, Makefile CCDP targets, README CCDP section. | CCDP is a separate protocol distribution, not one of the eight collaboration-framework components. | Keep CCDP outside `INSTALL_ZIPS` and component payloads; run CCDP gates only when CCDP surfaces are touched. | `rg -n "CCDP separation"`, Makefile review, conditional `make ccdp-package` and `make check-ccdp-package`. |
| R-11 | source files change before Arc05 closes | Main source checkout. | Arc05 is planning-only; implementation starts only after Slice04 CDC verification, Arc05 close, and operator authorization. | Require source checkout cleanliness before and after this planning slice and again at source implementation entry. | `git -C /Users/oubiwann/lab/billosys/ai-engineering diff --quiet`. |
| R-12 | Makefile list drift | `COMPONENT_ZIPS`, `INSTALL_ZIPS`, `ALL_SKILL_FILES`, `CF_FILES`, help text, aggregate targets. | A component can exist in source but be missing from validation, package build, install, or help output. | Implement package list changes in one Makefile-focused source slice after payloads exist. Prefer one component list or closely scoped variables. | `make help`, `make check-skills`, component package targets, `make all`, `make check-package-paths`. |

## Carry-Forward Gates

- No source implementation starts until Arc05 is CDC-verified and the operator
  authorizes source edits.
- No generated zip behavior is accepted without `make all`, `make
  collab-framework`, component package targets, and `make check-package-paths`.
- No package-path exception is accepted without a classification, reason, and
  expiration.
- No CCDP validation gate is required unless CCDP source or package surfaces
  are touched; if touched, CCDP gates become mandatory.
