# Composite Cognition Dispatch Protocol

This package is a standalone CCDP protocol distribution. It can be read directly after unzip or rebuilt locally from the included source chapters and assembler source.

## Start Here

- [Assembled specification](composite-cognition-dispatch-protocol.md)
- [Source chapter guide](src/README.md)
- [JSON corpus manifest](json/MANIFEST.md)
- [Visual guide](visual-guide/index.html)
- [Visual guide reference](visual-guide/ccdp-reference.md)

## Rebuild

From this `ccdp/` directory:

```sh
make ccdp-rfc OUTPUT=/private/tmp/ccdp-rebuilt.md
```

The included `Makefile` builds `tools/ccdp-assembler/` and assembles from `src/`.

## Package Contents

- `composite-cognition-dispatch-protocol.md`: assembled protocol specification.
- `src/`: source chapters used by the assembler.
- `json/`: extracted examples, canonical instances, and inventory notes.
- `visual-guide/`: reader-facing visual explanation and source reference.
- `templates/`: kramdown-rfc template used by the CCDP Makefile.
- `tools/ccdp-assembler/`: Rust assembler source and Cargo metadata.
