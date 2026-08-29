# CCDP Package Risk Map

Inputs:

- `ccdp-file-inventory.txt`
- `ccdp-file-inventory-tracked.txt`
- `ccdp-file-counts.tsv`
- `ccdp-path-reference-scan.tsv`
- `ccdp-path-reference-counts.tsv`
- `ccdp-tracking-status-summary.txt`

## Reference Classes

`ccdp-path-reference-scan.tsv` contains 1,277 extracted references from the
current on-disk CCDP Markdown/JSON surface plus the root README/Makefile,
excluding Cargo `target/` output. `ccdp-reader-facing-path-counts.tsv` excludes
`workbench` and `prompts` rows so package design can see the reader-facing
signal separately from provenance material.

| Class | Count | Package risk | Disposition for Slice 02 |
|-------|------:|--------------|--------------------------|
| `anchor-only` | 141 full / 140 reader-facing | Low. These are intra-document anchors or section links. | Preserve; validate entrypoint anchors after package generation. |
| `path-like` | 603 full / 86 reader-facing | Mixed. Many are schema field paths, JSON Pointer examples, command snippets, review citations, or prose identifiers rather than file links. | Do not blindly hard-fail; checker policy needs CCDP-aware filtering. |
| `repo-root-relative` | 343 full / 2 reader-facing | High in workbench; medium elsewhere. Workbench review packets cite repo-root source paths heavily. | Exclude workbench by default; transform or document any repo-root paths that ship. |
| `parent-relative` | 52 full / 1 reader-facing | High in workbench; medium in reader-facing source README. | Decide whether source README ships unchanged, is transformed, or includes tools. |
| `absolute-or-rooted` | 39 full / 21 reader-facing | Mostly JSON Pointer paths such as `/body/translation` or elision comments, not filesystem paths. | Treat as scanner caveats unless a package checker can distinguish URI/JSON-pointer syntax. |
| `document-relative` | 30 full / 29 reader-facing | Mostly root `README.md` links to repo-level docs/skills, not CCDP-local package contents. | Do not put root README in a CCDP package unless transformed or paired with repo context. |
| `workbench-only` | 25 full / 0 reader-facing | Workbench provenance only. | Exclude from package. |
| `ccdp-root-relative` | 20 full / 3 reader-facing | Low if the archive root is `ccdp/` and includes matching `src/`/`json/` material; otherwise medium. | Define package root semantics and validate these paths from the package entrypoint. |
| `external-url` | 18 full / 15 reader-facing | Not a package-local path risk. | Preserve without URL liveness checks. |
| `local-absolute` | 5 full / 0 reader-facing | Local machine paths in ignored prompts/workbench. | Exclude from package. |
| `other` | 1 full / 0 reader-facing | Scanner residue. | Ignore unless a checker later classifies it as a concrete path. |

## Concrete Risks

- `protocols/ccdp/src/README.md` references `../tools/`; a package that ships
  source chapters without assembler tooling will break that reference.
- `protocols/ccdp/json/MANIFEST.md` references `src/README.md`,
  `src/01-abstract.md`, and `src/21-version-history.md`; these are safe only if
  `src/` ships at the CCDP package root.
- The repository root `README.md` links broadly into `docs/`, `templates/`,
  and `knowledge/`; it is not a CCDP package entrypoint without transformation.
- `protocols/ccdp/prompts/` and `protocols/ccdp/workbench/` are on disk but
  ignored/untracked. They should not be silently captured by a package target.
- Running `make ccdp` rewrites the assembled spec from tracked source inputs.
  Slice 02 should decide whether generated-output freshness is a precondition
  for packaging or a separate repair before package implementation.

## Non-Risks / Scanner Caveats

- JSON Pointers and slash-prefixed protocol paths are not filesystem paths.
- External URLs are package references but not package-local path obligations.
- Workbench review packets are provenance/review material and should not be
  treated as reader-facing distribution content by default.
