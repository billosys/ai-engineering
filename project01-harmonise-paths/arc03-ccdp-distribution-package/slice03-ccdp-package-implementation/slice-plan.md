# Slice 03: CCDP Package Implementation

```yaml
project: project01-harmonise-paths
arc: arc03-ccdp-distribution-package
slice: slice03-ccdp-package-implementation
status: open
opened-on: 2026-08-29
artifact-home: artifacts/
depends-on:
  - slice01-ccdp-distribution-inventory
  - slice02-ccdp-package-contract-design
implementation-checkout: /Users/oubiwann/lab/billosys/ai-engineering
planning-worktree: /Users/oubiwann/lab/billosys/ai-engineering/.worktrees/planning
```

## Capability

Implement the CCDP distribution contract selected by Slice 02: a
rebuild-capable `ccdp.zip` with one `ccdp/` archive root, a generated
package-local entrypoint, package-local links, and a CCDP-specific package
validator that checks both zipped and unzipped usage.

## Inputs

- `../slice01-ccdp-distribution-inventory/cdc-verification.md`
- `../slice01-ccdp-distribution-inventory/artifacts/ccdp-file-inventory.md`
- `../slice01-ccdp-distribution-inventory/artifacts/package-risk-map.md`
- `../slice02-ccdp-package-contract-design/cdc-verification.md`
- `../slice02-ccdp-package-contract-design/artifacts/ccdp-package-contract-design.md`
- `../slice02-ccdp-package-contract-design/artifacts/package-contents-manifest-draft.md`
- `../slice02-ccdp-package-contract-design/artifacts/package-path-semantics.md`
- `../slice02-ccdp-package-contract-design/artifacts/generated-output-freshness-decision.md`
- `../slice02-ccdp-package-contract-design/artifacts/validation-checker-strategy.md`
- `../slice02-ccdp-package-contract-design/artifacts/slice03-implementation-inputs.md`
- implementation checkout `Makefile`
- implementation checkout `scripts/check-package-paths`
- implementation checkout `protocols/ccdp/Makefile`
- implementation checkout `protocols/ccdp/`

## Scope

Implement, in the source checkout:

- root Makefile targets `ccdp-package` and `check-ccdp-package`;
- package staging for `build/ccdp/`;
- `ccdp.zip` with exactly one `ccdp/` archive root;
- generated package-local `ccdp/README.md`;
- selected required contents from the Slice 02 manifest;
- required exclusions for workbench, prompts, Cargo target output, root
  README, and root Makefile;
- a CCDP-specific `scripts/check-ccdp-package` validator;
- zip and unzipped path checks with protocol-syntax filters;
- extracted-package non-mutating assembly validation;
- generated assembled-spec freshness reconciliation before packaging.

If temporary assembly output differs from
`protocols/ccdp/composite-cognition-dispatch-protocol.md`, the implementation
may update the committed assembled spec as a named pre-package repair inside
this slice, then rerun the freshness check before packaging.

## Out of Scope

- CCDP runtime behavior.
- URL liveness checking.
- Including `protocols/ccdp/workbench/` or `protocols/ccdp/prompts/` in the
  package.
- Rewriting protocol prose except generated assembled-spec refresh required by
  the freshness gate.
- Broad skill-bundle packaging changes beyond proving existing package checks
  still pass.
- Source-clone or release-facing reader guidance beyond the generated package
  README; broader documentation belongs to Slice 04 unless required for this
  target to work.

## Verification Approach

Run from `/Users/oubiwann/lab/billosys/ai-engineering`:

```sh
make ccdp-package
make check-ccdp-package
unzip -l ccdp.zip
make check-package-paths
make all
git diff --check
```

Run or record equivalent validator evidence that proves:

- `ccdp.zip` exists;
- every zip entry is under one `ccdp/` root;
- required files are present;
- excluded trees/files are absent;
- package-local Markdown links resolve after unzip;
- JSON Pointers, slash-prefixed protocol paths, elision comments, and field
  paths are not treated as filesystem paths;
- `make -C <unzipped>/ccdp ccdp-rfc OUTPUT=/private/tmp/...` succeeds without
  mutating the package artifact;
- root `make ccdp` or an equivalent CCDP-local assembly gate still works.

Run from the planning worktree:

```sh
git diff --check
find project01-harmonise-paths/arc03-ccdp-distribution-package/slice03-ccdp-package-implementation/artifacts -maxdepth 2 -type f -print
test -f project01-harmonise-paths/arc03-ccdp-distribution-package/slice03-ccdp-package-implementation/closing-report.md
rg -n "F-1|F-2|F-3|F-4|F-5|F-6|F-7|F-8|F-9|F-10|F-11|F-12|Artifacts|Bubble-up to Arc 03" project01-harmonise-paths/arc03-ccdp-distribution-package/slice03-ccdp-package-implementation/closing-report.md
```

## Exit Criteria

- `ccdp.zip` builds from the implementation checkout.
- The CCDP package validator passes against the zipped and extracted package.
- Existing skill-bundle package checks still pass.
- Existing CCDP assembly remains usable.
- Any generated assembled-spec drift is either reconciled in this slice or
  explicitly fails the package target/check.
- Slice-produced durable evidence lives under this slice's `artifacts/`
  directory.
- The close report walks every ledger row and bubbles findings up to Arc 03.
