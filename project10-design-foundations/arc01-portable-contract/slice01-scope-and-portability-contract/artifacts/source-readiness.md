# Design-corpus source availability

Source snapshot: `dffa504e851b03b8e4746f1941068e4cc850b612` on `main`.
Population witness: `baseline-files.tsv` and
`card-source-index.jsonl`. This is an availability and locator assessment,
not semantic verification of the cards or originals.

## Source-identity groups

The existing availability table stays human-readable. Its added raw identity key
is a JSON pair `[source_raw, authors_raw]`, unambiguously linking each display
row to the literal index identity. The records below were generated from all
233 index objects; JSON parsing preserves the raw strings, including YAML quote
characters and literal backslashes. This is slice evidence, not a new card or
global source schema. For a parsed group `g`, select rows with the exact
predicate:

`r["source_fields_raw"]["source"][0] == g["source_raw"] and r["source_fields_raw"]["authors"][0] == g["authors_raw"]`.

| Asserted source title and author | Card count | Raw identity key (JSON `[source_raw, authors_raw]`) | Local prepared/original holdings and identifying checks | Locator and readiness limits; next action |
|---|---:|---|---|---|
| `Art and Visual Perception: A Psychology of the Creative Eye` — Rudolf Arnheim | 112 | `["\"Art and Visual Perception: A Psychology of the Creative Eye\"","\"Rudolf Arnheim\""]` | No matching original or prepared text under the complete designated `knowledge/design/sources/` tree (161 files). Cards are in `concept-cards/art-and-visual-perception/`; their section/chapter/page assertions are preserved in the index. | Edition, printing and page-label convention are absent from the asserted bibliographic fields; original not located in this tree. Slice02/CDC must identify and obtain an authorized source snapshot with edition identity and locator map before source-fidelity review. Semantic support is unassessed; affected 112 cards cannot be promoted on metadata alone. |
| `A Practical Description of The Munsell Color System` — T. M. Cleland | 19 | `["\"A Practical Description of The Munsell Color System\"","\"T. M. Cleland\""]` | No matching original/prepared text in the designated source tree. All 19 asserted identities are in `concept-cards/munsell-colour-system/`. The atomic `munsell-hue-circle.md` witness was read completely; it asserts Chapter 4, section I, `pdf_page: 4`, and a prose construction. | The card's locator basis and source edition remain unresolved. Its source-reference prose is the card's assertion, not a Cleland source witness. Slice02/CDC must locate the edition, document physical versus printed page convention, and prepare a stable snapshot/map. Semantic support is unassessed for all 19. |
| `The New Typography` — Jan Tschichold | 19 | `["\"The New Typography\"","\"Jan Tschichold\""]` | No matching original/prepared text in the designated source tree. Cards are in `concept-cards/the-new-typography/`; source-reference bodies preserve chapter and page claims. | Edition/translation, publication data and page-label basis are not pinned. Slice02/CDC must identify the actual edition represented by the claims and map those locators before fidelity review. Semantic support is unassessed for all 19. |
| `Butterick's Practical Typography` — Matthew Butterick | 37 | `["\"Butterick's Practical Typography\"","\"Matthew Butterick\""]` | Prepared Markdown is present at `knowledge/design/sources/md/practical-typography/`: 156 `.md` files plus `_conversion-report.txt`. The report says 156 HTML inputs/156 Markdown outputs, records a March 1, 2026 conversion, three residue checks, and five broken internal links. Its index and mapped section/title text were inspected; all 37 cards' section assertions were searched in the prepared tree. | The raw HTML inputs are not present in the designated tree, so the original capture and its exact date/revision are not independently compared here. Several section-title/frontmatter forms do not match literally; resolve each card's exact source-file/heading locator in Slice02. Prepared reading text exists, but extraction completeness/fidelity and every card claim remain unassessed. Preserve the report's broken-link caveat; repair or disposition only in authorized preparation work. |
| `Working With Colors Guide` — Sarah Drasner | 12 | `["\"Working With Colors Guide\"","\"Sarah Drasner\""]` | Prepared capture at `knowledge/design/sources/md/posts/working-with-colours.md` (hash in baseline). Its title/author passage and `Color mixing` and `Accessibility and Other Things to Note about Color` identifying headings were inspected. | Card `Source Reference` sections name article sections, but many frontmatter `section` values are explicit null. Capture date/revision and fidelity to the original web article are not established. Slice02 should pin a stable source identity and section/anchor mapping, then review claims against contextual spans. Semantic support is unassessed. |
| `More Meaningful Typography` — Tim Brown | 10 | `["\"More Meaningful Typography\"","\"Tim Brown\""]` | Prepared capture at `knowledge/design/sources/md/posts/more-meaningful-typography.md` (hash in baseline). The article title/author/date and the `Modular scales...`, `Creating...`, `Applying...`, `Where does this fit...`, and `Conclusion` passages were inspected. In the complete capture at line 314 the author expressly says a scale is a tool, not magic, and permits rounding, combining values or departing from it; this is an identifying witness, not a blanket card verdict. | The capture has HTML presentation residue; capture revision and fidelity remain unverified. Some card `section` values are null while their raw source-reference body gives section-level locators. Slice02 should pin identity and resolve those mappings. Semantic support is unassessed. |
| `A Perceptual Color Space for Image Processing` — Björn Ottosson (literal metadata preserves `Bj\\u00f6rn`) | 13 | `["\"A Perceptual Color Space for Image Processing\"","\"Bj\\u00f6rn Ottosson\""]` | Prepared capture at `knowledge/design/sources/md/posts/a-perceptual-colour-space.md` (hash in baseline). The title/introduction states the Oklab article was originally introduced in 2020; the XYZ-to-Oklab section is present and was inspected. Cards' raw references name conversion, derivation, comparison, blending and dataset sections. | Converted HTML wrappers and embedded assets remain. Web article has no page numbers; several frontmatter `section` values are null, though source-reference text supplies headings. Pin capture identity/anchors in Slice02. Semantic support is unassessed. |
| `Okhsv and Okhsl` — Björn Ottosson (literal metadata preserves `Bj\\u00f6rn`) | 11 | `["\"Okhsv and Okhsl\"","\"Bj\\u00f6rn Ottosson\""]` | Prepared capture at `knowledge/design/sources/md/posts/okhsv-and-okhsl.md` (hash in baseline). The title/subtitle, author attribution in the article capture, `Color picking before computers`, `What makes a good color picker?`, and Okhsv/Okhsl sections were inspected. | Converted page wrappers, inline image/data residue and ambiguous/null card section fields remain. No immutable original web snapshot/date is established. Slice02 should pin identity and resolve heading anchors. Semantic support is unassessed. |

Raw-pair records (exact index strings):

```json
[
  {
    "source_raw": "\"Art and Visual Perception: A Psychology of the Creative Eye\"",
    "authors_raw": "\"Rudolf Arnheim\"",
    "card_count": 112
  },
  {
    "source_raw": "\"A Practical Description of The Munsell Color System\"",
    "authors_raw": "\"T. M. Cleland\"",
    "card_count": 19
  },
  {
    "source_raw": "\"Working With Colors Guide\"",
    "authors_raw": "\"Sarah Drasner\"",
    "card_count": 12
  },
  {
    "source_raw": "\"A Perceptual Color Space for Image Processing\"",
    "authors_raw": "\"Bj\\u00f6rn Ottosson\"",
    "card_count": 13
  },
  {
    "source_raw": "\"Okhsv and Okhsl\"",
    "authors_raw": "\"Bj\\u00f6rn Ottosson\"",
    "card_count": 11
  },
  {
    "source_raw": "\"More Meaningful Typography\"",
    "authors_raw": "\"Tim Brown\"",
    "card_count": 10
  },
  {
    "source_raw": "\"Butterick's Practical Typography\"",
    "authors_raw": "\"Matthew Butterick\"",
    "card_count": 37
  },
  {
    "source_raw": "\"The New Typography\"",
    "authors_raw": "\"Jan Tschichold\"",
    "card_count": 19
  }
]
```

## Complete local-tree observations

The source manifest contains 161 files under `knowledge/design/sources/`:
160 Markdown files and one conversion report. The only holdings are the
`md/posts/` and `md/practical-typography/` groups. No `Arnheim`, `Munsell`, or
`Tschichold` original is represented in this designated tree. This says nothing
about files the Operator may hold elsewhere; no private location was searched.

Each post capture is associated by exact asserted source/author identity and
inspected for its identifying title and relevant headings. Cards retain
different locator completeness: the JSONL projection shows 75 explicit null
`section` fields and 83 explicit null `pdf_page` fields across all sources.
These are literal card values, not inferred absence from the source. The post
article `Source Reference` bodies often contain richer heading descriptions;
those do not establish capture-to-original fidelity.

For Butterick, the 37-card membership is selected by the record whose parsed
`source_raw` is `"\"Butterick's Practical Typography\""` and parsed
`authors_raw` is `"\"Matthew Butterick\""`, using the exact predicate above.
This is not a claim that all 156 files are represented by cards. The
conversion report provides useful conversion lineage and reports five broken
internal links, but not proof of source completeness or fidelity. All mapped
section strings were checked against the prepared tree; title differences,
frontmatter aliases and ambiguous substring matches need a stronger per-card
locator map before review. Do not call these 37 source claims verified.

## Readiness by use

| Source group | Standalone reading of local prepared text | Full semantic/source-fidelity review | Limitation |
|---|---|---|---|
| Arnheim, Cleland, Tschichold | Original/prepared local text not available in this tree; not assessed outside it | Blocked pending an identified source snapshot and locator mapping | No conclusion about external availability or claim truth |
| Butterick | Caveated: converted Markdown can be read; conversion report notes five broken links | Blocked pending original/capture identity, per-card locator reconciliation and content-fidelity checks | Readability does not prove completeness or fidelity |
| Four web posts | Caveated: local prepared text and identifying passages are present | Not assessed pending stable capture identity and claim-by-claim comparison | Headings/metadata presence is not semantic support |

This slice did not assess full-text indexing, conversion fidelity across all
source files, or ordinary source-supported analysis. No source is globally
labelled “ready” by this inventory. Missing evidence remains an explicit
blocker for affected semantic claims; it is not evidence that those claims are
false. Slice02 owns the acquisition/preparation plan, edition and locator
resolution, and review-readiness method. The Operator must provide or authorize
missing source inputs through that later work; this slice did not search
private storage, download, buy, convert, or write source material.
