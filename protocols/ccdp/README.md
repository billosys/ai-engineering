# Composite Cognition Dispatch Protocol

This directory is the CCDP protocol root. In the source checkout it lives at
`protocols/ccdp/`; in `ccdp.zip` it is staged as the unzipped `ccdp/` package
root. The links below are relative to this directory so they work in both
contexts.

## Start Here

- [Assembled specification](composite-cognition-dispatch-protocol.md)
- [Source chapter guide](src/README.md)
- [JSON corpus manifest](json/MANIFEST.md)
- [Visual guide](visual-guide/index.html)
- [Visual guide reference](visual-guide/ccdp-reference.md)

## Source Checkout

From the repository root:

```sh
make ccdp
make ccdp-package
make check-ccdp-package
```

`make ccdp` assembles the source protocol document. `make ccdp-package` builds
`ccdp.zip`, and `make check-ccdp-package` validates the zip shape, package-local
Markdown paths, and extracted-package rebuild.

## Package Use

After unzipping `ccdp.zip`, start at `ccdp/README.md`. From inside the unzipped
`ccdp/` directory, the package can be read directly or rebuilt locally:

```sh
make ccdp-rfc OUTPUT=ccdp-rebuilt.md
```

The included `Makefile` builds `tools/ccdp-assembler/` and assembles from
`src/`. The package is also usable read-only if the local Rust toolchain is not
available.

## Package Contents

- `composite-cognition-dispatch-protocol.md`: assembled protocol specification.
- `src/`: source chapters used by the assembler.
- `json/`: extracted examples, canonical instances, and inventory notes.
- `visual-guide/`: reader-facing visual explanation and source reference.
- `templates/`: kramdown-rfc template used by the CCDP Makefile.
- `tools/ccdp-assembler/`: Rust assembler source and Cargo metadata.

## Source-only Material

The source checkout also contains `workbench/` and `prompts/`. Those directories
are provenance, review, and prompt material. They are intentionally excluded
from `ccdp.zip` and are not package entrypoints.
