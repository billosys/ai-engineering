# protocol package separation report

## Scope

This report records `ccdp.zip` root/content inspection and confirms CCDP
remains a separate protocol package, not an installable skill package.

## Root and Content Inspection

Command:

```sh
unzip -Z1 ccdp.zip | awk -F/ 'NR==1 {root=$1} END {print root, NR " entries"}'
```

Result:

```text
ccdp 122 entries
```

Expected protocol package contents observed:

```text
ccdp/visual-guide/index.html
ccdp/visual-guide/ccdp-reference.md
ccdp/tools/ccdp-assembler/Cargo.toml
ccdp/tools/ccdp-assembler/Cargo.lock
ccdp/Makefile
ccdp/README.md
ccdp/json/MANIFEST.md
ccdp/json/FINDINGS.md
ccdp/templates/draft-rfcxml-general-template-standard-00.xml-edited.md
ccdp/composite-cognition-dispatch-protocol.md
ccdp/src/README.md
```

The package also contains CCDP source chapters under `ccdp/src/`, JSON
canonical/example/inventory content under `ccdp/json/`, and the assembler
source under `ccdp/tools/ccdp-assembler/src/`.

## Installable Skill Separation

`ccdp.zip` is separate from the installable skill set:

- it is built by `make ccdp-package`, not `make all`;
- it is validated by `make check-ccdp-package`, not
  `make check-package-paths`;
- it is not installed by `make install`;
- it has no `SKILL.md`, `SKILL-js-linter.md`, or `SKILL-web-linter.md`
  entrypoint claim.

Command:

```sh
unzip -Z1 ccdp.zip | rg '^ccdp/SKILL' || true
```

Result: no output.

Conclusion: CCDP remains a protocol package with protocol package contents and
no installable skill entrypoint.
