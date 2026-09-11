# Prepared Source Manifest

## Preparation Record

| Field | Value |
| --- | --- |
| Prepared-source ID | `ps-ccn-book-pilot-20260911` |
| Revision | `1` |
| Input snapshot | `e0c697b4d4d134f29cb5c2bbde41b1b6b409b63d` / tree `894b3e10baa38e9d9c29a2e52b64f4d0ffb1378a` |
| Representation | Upstream-authored Markdown, directly inspected in temporary checkout |
| Preparation mode | Structure and locator mapping only; no conversion, normalization, splitting, or source rewrite |
| Downstream use | Candidate-card extraction for this Slice02 pilot only |

## Included Units

| Resource | Included headings/line spans | Excluded material |
| --- | --- | --- |
| `chapter-01.md` | `# Introduction` (5-60); `## The Computational Approach` (31-49); `## Emergent Phenomena` (51-60) | All remaining Chapter 1 sections and every other corpus file |
| `chapter-07.md` | `# Memory` (5-15); `## Episodic Memory` (17-45); hippocampus/pattern separation/completion material (47-83); consolidation (113-117) | Other Chapter 7 sections, all other chapters, the full bibliography, and unselected figures |

The inclusion ranges overlap their enclosing chapter headings intentionally.
They describe reviewed context and candidate-support spans, not separately
extracted copies.

## Preparation Outputs

The preparation outputs are [structure map](./structure-map.md),
[locator map](./locator-map.md), and
[validation readiness](./validation-readiness.md). They retain source identity
and navigation evidence only. They are upstream provenance for candidate cards,
not semantic support or verification.

## Caveats

The corpus has its own Markdown and heading anchors, but no immutable remote
line-address service was used. This pilot therefore records the pinned file
hash, heading anchor, and one-based inclusive line range together. The source
references a local `ccnlab.bib` while the repository inventory records
`references.bib`; citation-key resolution is not claimed here and every
candidate dependency is assessed separately.
