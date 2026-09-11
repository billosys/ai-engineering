# Corpus Intake: Computational Cognitive Neuroscience

## Snapshot Identity

| Field | Recorded value |
| --- | --- |
| Corpus | *Computational Cognitive Neuroscience*, Fifth Edition |
| Upstream repository | `https://github.com/compcogneuro/book` |
| Requested ref | `main` |
| Pinned commit | `e0c697b4d4d134f29cb5c2bbde41b1b6b409b63d` |
| Commit timestamp | 2026-02-22T20:20:49Z |
| Commit message | `Update chapter-04.md` |
| Tree | `894b3e10baa38e9d9c29a2e52b64f4d0ffb1378a` |
| Metadata edition/version | Fifth Edition; `v1.1.1` in `metadata.yaml` |
| Intake inspection | Public GitHub API tree and raw-file inspection on 2026-09-11; no checkout or corpus copy was placed in the planning worktree. |

The pinned commit, not the moving `main` ref, is the source identity for this
pilot. A later execution must obtain this exact commit, or record and review a
new snapshot identity before treating its results as comparable to this plan.

## License And Attribution

The repository declares `CC-BY-4.0`; its `LICENSE` contains the Creative
Commons Attribution 4.0 International text. The README and `metadata.yaml`
identify the copyright owners as Randall C. O'Reilly, Yuko Munakata, Michael J.
Frank, Thomas E. Hazy, and Contributors (2024).

Pilot records and review material must preserve the upstream repository URL,
pinned commit, title, stated creators/copyright notice, and CC-BY-4.0 license
reference. Any redistributed derivative material must identify modifications
and retain the attribution and license information required by that license.
This is a provenance and handling requirement, not legal advice. Slice02 must
also flag any third-party material whose rights or attribution are not clear
from the inspected source.

## Inventory

The recursive tree for the pinned commit contained 153 blobs.

| Surface | Location or form | Count | Intake relevance |
| --- | --- | ---: | --- |
| Chapter Markdown | `chapter-01.md` through `chapter-10.md` | 10 | Primary prose candidates |
| Other Markdown | `README.md`, `frontmatter.md`, `endmatter.md`, `glossary.md` | 4 | Context, publication framing, and terminology |
| Metadata and build support | `metadata.yaml`, `Makefile`, `apa-6th-edition.csl` | 3 | Edition and rendering context |
| Bibliography | `references.bib` | 1 | Citation resolution support |
| License | `LICENSE` | 1 | Reuse and attribution handling |
| Figures | `figures/` PNG, JPG, and SVG assets | 131 | Direct inspection is required when a claim depends on a figure |
| Cover assets | `cover.png`, `cover.svg` | 2 | Publication asset, outside pilot scope |
| Repository support | `.gitignore` | 1 | No extraction role |

The selected pilot draws from `chapter-01.md` and `chapter-07.md`; those files
are already authored Markdown with headings, anchors, citations, cross-links,
and figure references. The inventory is not a content-completeness claim and
does not assert that every reference or figure has been resolved.

## Preparation Approach

Slice02 should use a temporary checkout outside this planning tree, verify that
`HEAD` equals the pinned commit, and retain a preparation record rather than
vendoring the corpus here. For the existing Markdown, preparation is limited to
an input manifest, structure map, stable locators, and readiness/caveat record:

1. Record the checkout path, commit, tree, and file hashes or equivalent input
   identity evidence.
2. Map headings, explicit anchors, citation references, figure references, and
   relevant front/end matter for the sampled files.
3. Record the exact locator convention used by candidate records, including a
   stable fallback if a renderer-specific location is unavailable.
4. Mark figure- or bibliography-dependent support as unresolved until directly
   inspected; do not silently convert a reference into source support.

The output of that preparation is upstream provenance and navigation support.
It is not itself claim-level evidence, record verification, or admission to any
memory system.

## Intake Decision And Caveats

The corpus is caveated-ready for the bounded Chapter 1 and Chapter 7 pilot.
It is not approved for a whole-corpus run, a claim about textbook correctness,
or runtime ingestion. The principal caveats are that the current inspection is
remote rather than a retained checkout, bibliography resolution has not been
performed, and the 131 figures have not been reviewed. Slice02 must preserve
those boundaries in its execution evidence.
