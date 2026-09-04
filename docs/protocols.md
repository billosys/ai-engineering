# Protocols

Protocol material lives under [`protocols/`](../protocols/). The current
protocol distribution is the Composite Cognition Dispatch Protocol, or CCDP,
under [`protocols/ccdp/`](../protocols/ccdp/).

CCDP is related to the repository's assistant-engineering work, but it is not
packaged as an installable assistant skill.

## CCDP Entry Points

Start with [`protocols/ccdp/README.md`](../protocols/ccdp/README.md). It links
to the protocol's source and package entrypoints:

- [`composite-cognition-dispatch-protocol.md`](../protocols/ccdp/composite-cognition-dispatch-protocol.md):
  assembled specification.
- [`src/README.md`](../protocols/ccdp/src/README.md): source chapter guide.
- [`json/MANIFEST.md`](../protocols/ccdp/json/MANIFEST.md): JSON corpus
  manifest.
- [`visual-guide/index.html`](../protocols/ccdp/visual-guide/index.html):
  visual guide.
- [`visual-guide/ccdp-reference.md`](../protocols/ccdp/visual-guide/ccdp-reference.md):
  visual guide source reference.

## Source Use And Package Use

In the source checkout, CCDP lives at `protocols/ccdp/`. Build and validation
commands are run from the repository root:

```sh
make ccdp
make ccdp-package
make check-ccdp-package
```

In package form, CCDP is written to `target/skills/ccdp.zip`. After unzipping
it, start at `ccdp/README.md`. The package includes the assembled
specification, source chapters, JSON material, visual guide, templates, and
assembler source needed for package-local rebuilds.

## Source-Only Material

The source checkout can also contain CCDP workbench and prompt material used
for provenance, review, or future development. Those paths are useful to
maintainers, but they are not package entrypoints.

## Boundary

Use skill package language for generated assistant skills. Use protocol
distribution language for CCDP. Arc05 owns final public vocabulary, but this
boundary is already operational: CCDP has its own package, validation targets,
and reader entrypoints.
