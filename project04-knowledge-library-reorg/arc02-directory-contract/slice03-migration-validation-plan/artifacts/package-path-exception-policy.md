# Package Path Exception Policy

```yaml
project: project04-knowledge-library-reorg
arc: arc02-directory-contract
slice: slice03-migration-validation-plan
artifact: package-path-exception-policy
artifact-status: implementation planning input
created-on: 2026-09-02
source_checkout: /Users/oubiwann/lab/billosys/ai-engineering
source-files-edited: false
```

## Purpose

This package-path exception policy defines when a package-path exception or
accepted warning is allowed after Project04 source/package root changes. An
exception is visible debt, not a way to hide broken package-local links.

## Core Rule

Repair before exception. Every package-local link failure must first be tested
for a package-local link repair, wrapper route, migration note, package payload
adjustment, or generated package layout correction. A package-path exception
is allowed only when the remaining divergence is intentional, narrow, and
recorded with evidence.

## Allowed Exception Classes

| Class | Allowed when | Required validation command |
|-------|--------------|-----------------------------|
| Source-only provenance | A source path is intentionally not included in generated packages. | `make check-package-paths` plus generated package inspection. |
| External URL or upstream citation | The link target is intentionally outside the repository or package. | `make check-package-paths` or link checker evidence when available. |
| Transitional wrapper | An old route must remain during migration but points to a new accepted root. | README/docs route review plus `make check-package-paths` if packaged. |
| Selected-file composer packaging | `collaboration-framework` still assembles package contents from selected files during transition. | `make collab-framework`; `make check-package-paths`; generated package inspection. |
| Multi-entrypoint package behavior | A single source root such as Biome intentionally produces multiple package roots. | `make check-skills`; `make check-package-paths`; generated package inspection. |
| Protocol separation | `protocols/ccdp` remains separate from installable skill packages while being referenced by docs or skills. | `make ccdp-package`; `make check-ccdp-package`; `INSTALL_ZIPS` review. |
| Checker false positive | The checker cannot model an intentional path shape, and the source/package behavior is otherwise verified. | Checker output plus manual/generated package inspection. |

## Required Exception Row Fields

Every exception row must include:

- owner;
- source path;
- package or generated package root;
- reason;
- validation command;
- evidence pointer;
- expiration date or no-expiration rationale;
- operator approval status;
- accepted warning text, if the exception remains visible in validation
  output;
- re-entry condition.

## Operator Approval

Operator approval is required for:

- any persistent exception with a no-expiration rationale;
- any accepted warning that remains after an implementation slice closes;
- any exception that leaves source-like material in `docs/`;
- any exception that leaves owner-local templates in top-level `templates/`;
- any exception that keeps top-level SKILL.md as a composer source after the
  composer source root moves;
- any CCDP package-policy change;
- any broad pattern exception that covers more than one named owner or package
  root.

## Prohibited Uses

- Do not use an exception before trying package-local link repair.
- Do not use broad wildcard exceptions to make `make check-package-paths` pass.
- Do not use an exception to claim Project03 `concept-card-method` is live
  source before implementation.
- Do not use an exception to add CCDP to installable skill packages.
- Do not use an exception to avoid updating `CF_FILES`, `ALL_SKILL_FILES`,
  `INSTALL_ZIPS`, README routes, wrappers, or migration notes when those are
  the real source of the mismatch.

## Review Workflow

1. Run the relevant source-edit validation gates.
2. Attempt package-local link repair or package payload correction.
3. Re-run `make check-package-paths` and inspect the generated package.
4. If the failure is intentional, draft a narrow exception row with owner,
   reason, validation command, expiration or no-expiration rationale, operator
   approval status, accepted warning text, and re-entry condition.
5. Obtain operator approval for persistent exceptions or accepted warnings.
6. Re-run the validation command and record the evidence pointer in the
   implementation slice closing report.

## Re-Entry Conditions

- Re-enter this policy if package-local link repair cannot keep exceptions
  narrow.
- Re-enter Slice02 source/package root decisions if generated packages require
  broad divergence from accepted source roots.
- Re-enter CCDP policy if protocol separation cannot be validated without
  changing package behavior.
- Re-enter Arc05 if public vocabulary choices become necessary to explain
  accepted warnings to end users.
