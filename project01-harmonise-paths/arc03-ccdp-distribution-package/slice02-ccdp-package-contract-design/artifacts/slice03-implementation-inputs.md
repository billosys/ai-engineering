# Slice 03 Implementation Inputs

## Implementation Scope

Implement a rebuild-capable CCDP distribution package:

- Root archive: `ccdp.zip`
- Archive root: `ccdp/`
- Entry target: `make ccdp-package`
- Validation target: `make check-ccdp-package`
- Validator: `scripts/check-ccdp-package`

## Proposed Implementation Steps

1. Add a generated-output freshness check that compares temporary assembly
   output with `protocols/ccdp/composite-cognition-dispatch-protocol.md`.
2. If the freshness check fails, update the committed assembled spec as a named
   pre-package step and rerun the check.
3. Add CCDP package staging logic to copy selected tracked contents into
   `build/ccdp/`.
4. Generate package-local `build/ccdp/README.md`.
5. Copy `protocols/ccdp/Makefile` to `build/ccdp/Makefile`.
6. Copy required contents: assembled spec, `src/`, `json/`, `visual-guide/`,
   `templates/`, and assembler source/Cargo metadata.
7. Exclude `workbench/`, `prompts/`, Cargo `target/`, and root README/Makefile.
8. Zip `build/ccdp` as `ccdp.zip`.
9. Add `scripts/check-ccdp-package` and wire `make check-ccdp-package`.
10. Run zipped/unzipped validation and non-mutating assembly check from the
    extracted package.

## Proposed Ledger Anchors

- Freshness check either passes cleanly or records/commits generated assembled
  spec refresh before packaging.
- `ccdp.zip` exists and contains one `ccdp/` root.
- Required package contents exist and excluded trees are absent.
- `ccdp/README.md` is package-local and links only to packaged CCDP content or
  external URLs.
- Package-local Markdown path validation passes without treating JSON Pointers
  or protocol slash paths as filesystem paths.
- Extracted package can run `make -C <tmp>/ccdp ccdp-rfc OUTPUT=/private/tmp/...`.
- Existing root `make ccdp` behavior is preserved.
- Implementation scope does not modify workbench/prompts or implement CCDP
  runtime behavior.
