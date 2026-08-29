# CCDP Package Path Semantics

The package root is `ccdp/`. All reader-facing links inside the package must
resolve either from the current document location or from the package root.

| Area | Package path | Path contract | Slice 03 transform/check |
|------|--------------|---------------|--------------------------|
| Package entrypoint | `ccdp/README.md` | Links are package-root relative: `composite-cognition-dispatch-protocol.md`, `src/README.md`, `json/MANIFEST.md`, `visual-guide/index.html`. | Generate during staging; validate all links after unzip. |
| Assembled spec | `ccdp/composite-cognition-dispatch-protocol.md` | Existing anchors and external URLs are preserved. JSON Pointers and protocol slash paths are not filesystem links. | Validate Markdown links; filter JSON Pointer/protocol slash paths from filesystem checks. |
| Source chapters | `ccdp/src/*.md` | Source chapter cross-references remain document-relative or anchor-only. `src/README.md` may reference `../tools/` because tools ship. | Include tools or transform `../tools/`; selected contract includes tools, so no source README transform is required initially. |
| JSON corpus | `ccdp/json/**` | `json/MANIFEST.md` references `src/...` as CCDP-root-relative conceptual source paths. | Package validator should recognize `src/...` from JSON docs as package-root relative, not relative to `json/`. |
| Visual guide | `ccdp/visual-guide/**` | Guide files must not depend on repo-root `protocols/ccdp/...` paths. | Inspect `index.html` for local asset references and validate any present package paths. |
| Template | `ccdp/templates/**` | Used by kramdown-rfc targets, not a reader navigation surface. | Presence check only unless Markdown links appear later. |
| Assembler tooling | `ccdp/tools/ccdp-assembler/**` | Tool source is package-local; Cargo `target/` is excluded. | Presence check `Cargo.toml`, `Cargo.lock`, `src/*.rs`; optionally build in package validation. |
| Package-local Makefile | `ccdp/Makefile` | Running from `ccdp/` should assemble from `src/` and write `composite-cognition-dispatch-protocol.md`. | Run `make -C <unzipped>/ccdp ccdp-rfc OUTPUT=/private/tmp/...` in validation to avoid mutating package artifact. |
| Root README material | not included as-is | Repository-wide links are not package-local CCDP links. | Distill only CCDP package usage into generated entrypoint. |

## Scanner Rules

- External URLs are recorded but not liveness-checked.
- Anchor-only links are validated only within their containing Markdown file
  if anchor validation is implemented; they are not filesystem paths.
- JSON Pointers such as `/body/translation` are protocol syntax, not absolute
  filesystem paths.
- Elision comments such as `// ...` and `/* ... */` are not package paths.
- Code spans are warnings unless they clearly name a packaged file path.
- Workbench and prompt references are ignored because those trees are excluded.
