# CCDP Package Contents Manifest Draft

Archive: `ccdp.zip`

Root directory: `ccdp/`

## Required Contents

| Package path | Source path | Required | Notes |
|--------------|-------------|----------|-------|
| `ccdp/README.md` | generated during package staging | yes | Package-local entrypoint. Do not copy root `README.md` unchanged. |
| `ccdp/composite-cognition-dispatch-protocol.md` | `protocols/ccdp/composite-cognition-dispatch-protocol.md` after freshness reconciliation | yes | Primary assembled specification. |
| `ccdp/src/README.md` | `protocols/ccdp/src/README.md` | yes | Source-chapter overview; `../tools/` remains valid because tools ship. |
| `ccdp/src/*.md` | `protocols/ccdp/src/*.md` | yes | Source chapters, including version history and previous versions. |
| `ccdp/json/MANIFEST.md` | `protocols/ccdp/json/MANIFEST.md` | yes | JSON corpus entrypoint; `src/...` references remain valid from package root if linked from README as `json/MANIFEST.md`. |
| `ccdp/json/FINDINGS.md` | `protocols/ccdp/json/FINDINGS.md` | yes | Descriptive discrepancy register. |
| `ccdp/json/canonical/**` | `protocols/ccdp/json/canonical/**` | yes | Canonical JSON instances and notes. |
| `ccdp/json/examples/**` | `protocols/ccdp/json/examples/**` | yes | Extracted examples, including intentionally non-parsing elision examples. |
| `ccdp/json/inventory/**` | `protocols/ccdp/json/inventory/**` | yes | Field and enum inventories. |
| `ccdp/visual-guide/index.html` | `protocols/ccdp/visual-guide/index.html` | yes | Reader-facing guide. Slice 03 should inspect local asset assumptions. |
| `ccdp/visual-guide/ccdp-reference.md` | `protocols/ccdp/visual-guide/ccdp-reference.md` | yes | Visual-guide source/reference material. |
| `ccdp/templates/draft-rfcxml-general-template-standard-00.xml-edited.md` | `protocols/ccdp/templates/draft-rfcxml-general-template-standard-00.xml-edited.md` | yes | Required for kramdown-rfc Make targets. |
| `ccdp/tools/ccdp-assembler/Cargo.toml` | `protocols/ccdp/tools/ccdp-assembler/Cargo.toml` | yes | Rebuild-capable package tooling. |
| `ccdp/tools/ccdp-assembler/Cargo.lock` | `protocols/ccdp/tools/ccdp-assembler/Cargo.lock` | yes | Reproducible Cargo resolution for package consumers. |
| `ccdp/tools/ccdp-assembler/src/**` | `protocols/ccdp/tools/ccdp-assembler/src/**` | yes | Assembler source. |
| `ccdp/Makefile` | `protocols/ccdp/Makefile`, staged unchanged unless Slice 03 finds package-local breakage | yes | Build entrypoint inside extracted package. |

## Required Exclusions

| Excluded source path | Reason |
|----------------------|--------|
| `protocols/ccdp/workbench/**` | Ignored/untracked review/provenance material, not reader-facing package content. |
| `protocols/ccdp/prompts/**` | Ignored/untracked local prompt/provenance material; includes local absolute paths. |
| `protocols/ccdp/tools/ccdp-assembler/target/**` | Cargo build output. |
| Root `README.md` | Repository-wide documentation, not package-local CCDP entrypoint. |
| Root `Makefile` | Repository-wide skill packaging and install entrypoint; CCDP package should expose a package-local `Makefile`. |

## Optional Later Additions

- `ccdp/MANIFEST.tsv` generated during staging with source path, package path,
  required/optional flag, and SHA-256 checksums.
- `ccdp/VERSION` generated from the CCDP document version once the release flow
  decides how document version and archive version relate.
