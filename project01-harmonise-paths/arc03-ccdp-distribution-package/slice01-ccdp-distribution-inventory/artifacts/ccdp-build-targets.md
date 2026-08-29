# CCDP Build Target Inventory

Sources:

- Root `Makefile`
- `protocols/ccdp/Makefile`
- Assembly transcript: `ccdp-assembly-check.txt`

## Root Targets

| Target | Definition | CCDP role |
|--------|------------|-----------|
| `ccdp` | Root `Makefile` delegates with `cd protocols/ccdp && make`. | Public repository entrypoint for CCDP assembly. |

The root `Makefile` does not currently define a CCDP archive/package target.
Existing package targets are skill-bundle targets only.

## CCDP-Local Targets

| Target | Definition | Output |
|--------|------------|--------|
| `ccdp-rfc` | `tools/ccdp-assembler/target/release/ccdp-assembler --validate --src-dir src --output composite-cognition-dispatch-protocol.md --version 0.2` | GitHub-Flavored Markdown assembled spec. |
| `ccdp-rfc-strict` | Same as `ccdp-rfc`, plus `--strict`. | Strict validation gate for the assembled spec. |
| `ccdp-rfc-kramdown` | Assembles using `--format kramdown-rfc` and `templates/draft-rfcxml-general-template-standard-00.xml-edited.md`. | kramdown-rfc-flavored Markdown for RFC XML/HTML tooling. |
| `ccdp-rfc-kramdown-strict` | Same as `ccdp-rfc-kramdown`, plus `--strict`. | Strict kramdown-rfc validation gate. |
| `clean` | Removes `composite-cognition-dispatch-protocol.md` and runs Cargo clean in the assembler. | Cleanup only. |

## Tooling Inputs

- Assembler crate: `protocols/ccdp/tools/ccdp-assembler/`
- Source chapters: `protocols/ccdp/src/`
- RFC template: `protocols/ccdp/templates/draft-rfcxml-general-template-standard-00.xml-edited.md`
- Assembled output: `protocols/ccdp/composite-cognition-dispatch-protocol.md`

## Observed Gate Result

`make ccdp` exited 0. It also rewrote generated output, captured in
`ccdp-assembly-generated-drift.patch`: the assembled spec date changed from
2026-08-04 to 2026-08-29 and the previous-versions section gained a v0.2 link.
The generated file was restored afterward to keep this diagnosis-only slice
free of implementation edits.
