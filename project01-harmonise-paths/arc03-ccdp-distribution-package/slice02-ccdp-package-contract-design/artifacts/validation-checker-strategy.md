# Validation and Checker Strategy

Selected strategy: implement CCDP-specific package validation in Slice 03 and
wire it to the root Makefile package flow.

## Make Targets

Proposed root targets:

- `make ccdp-package`: build `ccdp.zip`.
- `make check-ccdp-package`: build or inspect `ccdp.zip`, inspect zipped
  contents, inspect unzipped contents, run package path validation, and run a
  non-mutating assembly check from the unzipped package.

Proposed CCDP-local target:

- Keep existing `protocols/ccdp` assembly targets intact.
- Reuse the CCDP-local `Makefile` inside the package as `ccdp/Makefile`.

## Validator Shape

Preferred implementation: `scripts/check-ccdp-package`.

Required checks:

1. Open `ccdp.zip` and assert all entries are under one `ccdp/` root.
2. Assert required files/directories from `package-contents-manifest-draft.md`
   exist.
3. Assert excluded trees are absent: `workbench/`, `prompts/`,
   `tools/ccdp-assembler/target/`, root repository `README.md` copy as-is, and
   root repository `Makefile`.
4. Extract to a temporary directory and validate package-local Markdown links
   from included reader-facing Markdown.
5. Treat external URLs as out of scope for liveness.
6. Treat JSON Pointers, protocol slash paths, elision comments, and field paths
   as non-filesystem syntax.
7. Run a non-mutating assembly check from the extracted package:
   `make -C <tmp>/ccdp ccdp-rfc OUTPUT=/private/tmp/ccdp-package-assembled.md`.
8. Compare the extracted package's assembled spec with the temporary assembly
   output or record a clear freshness failure.

## Why Not Reuse `check-package-paths` Unchanged

The existing package-path checker is tuned for installable skill bundles:
archive root plus `SKILL.md`/`guides/` semantics, domain source prefixes, and
skill-specific exception policy. CCDP needs protocol/package semantics:
`src/`, `json/`, `visual-guide/`, `templates/`, `tools/`, JSON Pointer syntax,
and rebuild validation. Reusing the checker unchanged would either miss CCDP
risks or over-report protocol syntax as filesystem failures.

Slice 03 may share extraction helpers with `scripts/check-package-paths`, but
the validation mode should be CCDP-specific.
