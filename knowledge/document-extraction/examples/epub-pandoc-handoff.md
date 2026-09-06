# Representative EPUB/Pandoc Handoff

**Synthetic example.** All source names, files, checks and results below are
invented illustrations, not a conversion run or tested fixture. No referenced
book or log ships with this example. Use the
[EPUB guide](../guides/05-epub-source-preparation.md),
[structure template](../templates/structure-map.md) and
[media template](../templates/media-report.md) with real observed evidence.

## Manifest

Manifest epub-manifest-01, source epub-field-notes, title Field Notes on Ponds,
author/edition unknown. Run epub-run-01 dated 2026-09-06 UTC uses agent-direct
operation within this imagined case. IDs: epub-raw-a (preserved EPUB),
epub-pandoc-a (supplied conversion), epub-prepared-a (derived output).
All scenario paths resolve from `/case/epub/`; evidence home `records/run-01/`.

Requested uses: section-keyed indexing and reading/source review of the whole
short book. Inputs: `raw/field-notes.epub`, `conversion/book.md` (50 lines),
`conversion/media/media/pond.svg`. Supplied lineage names pandoc, but version,
exact invocation and output dialect are unknown; no conversion is rerun.
Checksums and asset size were not recorded in this illustration, C-E2.

Derived inventory in reading order: `prepared/00-front.md` (8 lines),
`prepared/chapters/01-observations.md` (30 lines),
`prepared/02-notes.md` (12 lines), and copied asset
`prepared/media/media/pond.svg`. No generated headers; manifest/structure
records serve as sidecar metadata. Transformations: split at inspected complete
units; in the chapter change only image target `media/media/pond.svg` to
`../media/media/pond.svg`; retain all original titles, IDs, wrappers and alt text.

Record register: [structure](#structure), [media](#media), [locators](#locators),
[checks](#checks-and-readiness), [caveats](#caveats). All use the manifest's
source/run; input and output snapshots are explicit above. This is a combined
illustrative report; no actual evidence-home storage is claimed.

## Structure

Map epub-structure-01. Source spans in epub-pandoc-a `conversion/book.md`
and output spans are one-based inclusive, counting wrapper lines. Parent is
root for each row; original section labels are unnumbered.

| Order / ID | Original title / resource and anchor | Input to output | Boundary evidence |
| --- | --- | --- | --- |
| 1 / e-front | Field Notes on Ponds / `OEBPS/front.xhtml#title` | 1–8 to `prepared/00-front.md` 1–8 | Title and inline contents retained; nav entries distinguished from body headings |
| 2 / e-observe | Observations / `OEBPS/ch01.xhtml#observations` | 9–38 to `prepared/chapters/01-observations.md` 1–30 | Opening div and its final close included; heading follows the opening wrapper |
| 3 / e-notes | Notes / `OEBPS/notes.xhtml#notes` | 39–50 to `prepared/02-notes.md` 1–12 | Notes heading and closing text retained; no unexplained remainder |

Scenario direct inspection covers all cut edges and input/output bodies; the
map is verified for these three units. Ranges cover 1–50 without gaps or
overlap, names remain unique after case folding, original labels stay intact.
No cross-unit footnotes or shared definitions were found in this inspected
50-line conversion. It uses explicit IDs, with no cross-file internal links
requiring a rewrite beyond the media target. These are case facts, not a rule
that other EPUBs lack shared definitions or navigation links.

## Media

Report epub-media-01: one SVG asset E-A1, one Markdown reference E-R1, no
unreferenced assets in the inventoried bundle. Full original identity:
`OEBPS/media/pond.svg` inside epub-raw-a. Supplied extracted file:
`conversion/media/media/pond.svg`; copied file:
`prepared/media/media/pond.svg`. The nested directory is observed, not a
universal pandoc convention. Size/hash unknown, C-E2.

E-R1 is conversion line 20, output chapter line 12, with alt text “Pond depth
profile”, no title or other attributes. Original local base is
`/case/epub/conversion/`; emitted `../media/media/pond.svg` resolves from
`/case/epub/prepared/chapters/01-observations.md` to
`/case/epub/prepared/media/media/pond.svg`. Disposition changed; one of one
references resolves. SVG markup was inspected and no external dependencies
found; the archive-to-conversion pairing was established by resource path and
matching markup, not basename alone. Rendering is unavailable, so visual
equivalence remains not checked, C-E1.

## Locators

Map epub-locators-01, source epub-field-notes:

| ID | Snapshot / resource | Kind / value / basis | Status and evidence |
| --- | --- | --- | --- |
| E-L1 | epub-raw-a / `raw/field-notes.epub`, member `OEBPS/ch01.xhtml` | Anchor/ID `observations`, unique within this member | Verified in scenario by nav target and source element inspection |
| E-L2 | epub-pandoc-a / `conversion/book.md` | Source lines 9–38, one-based inclusive | Verified whole-unit boundary inspection; preserved div and heading ID |
| E-L3 | epub-prepared-a / `prepared/chapters/01-observations.md` | Output lines 1–30, one-based inclusive, wrappers included | Verified body comparison allowing only declared image target rewrite |

Relation E-M1: E-L1's containing section maps to E-L2 and E-L3; the anchor is a
point and does not itself assert a line range. Conversion-to-output relation
E-M2 maps the full E-L2 range to E-L3. Original fragment spelling
`ch01.xhtml#observations` is retained from navigation resolved relative to
`OEBPS/nav.xhtml`. No fixed page numbers or generated heading-slug equivalence
are asserted.

## Caveats

Caveats belong to epub-run-01, dated 2026-09-06, unresolved with no resolution
history. Actor: preparer; observations are scenario direct inspections.

| ID / category | Affected locations / evidence | Handling, impact and re-entry |
| --- | --- | --- |
| C-E1 / fidelity coverage | E-A1/E-R1, chapter line 12; no SVG renderer available | Preserve SVG and reference; reading caveated for diagram interpretation; render and compare original and prepared appearance |
| C-E2 / lineage and regeneration | All input/output files; exact pandoc invocation/version, digests and second-run comparison absent | Preserve supplied files and transformation map; do not claim reproducible conversion or historical byte identity; identify inputs, capture future commands, regenerate derived files into a new directory and compare |

## Checks And Readiness

| Check | Scenario scope / method | Outcome / record |
| --- | --- | --- |
| E-C1 structure and split integrity | All 50 input lines and three outputs compared; navigation/body correspondence and complete containers inspected | Pass within captured book; structure map |
| E-C2 media | All 1/1 paths resolved from final containing file; SVG markup compared | Pass for path and markup identity; visual appearance not checked, C-E1 |
| E-C3 locators and text fidelity | All three source resource headings matched; all short-book prose compared with XHTML; E-M1/E-M2 recorded in detail | Pass for prose/structure within inspected scope; excludes rendered diagram |
| E-C4 preservation/regeneration | Originals retained separately but no digests or repeat run | Not checked for byte identity/repeatability, C-E2 |

| Requested use | Status | Justification and next action |
| --- | --- | --- |
| Whole-book section-keyed indexing | Caveated | E-C1/E-C3 support text and section keys; C-E1 means diagram-only content is not represented by verified text. Original whole-book request remains limited until diagram handling is decided and checked |
| Whole-book reading/source review | Caveated | Prose checks pass; C-E1 leaves diagram appearance unchecked; compare rendered SVG before relying on its depiction |
| Analysis | Not assessed | Not requested |
| Concept-cards | Not assessed | Not requested; records are available as upstream provenance |

Handoff: three text files in manifest order plus the SVG and this record set.
Regeneration must reuse the recorded section-to-name and target maps from the
preserved conversion, without adding a second `../` or duplicating media.
The [helper plan](../templates/helper-script-plan.md) can specify such work;
this example provides no executable helper or successful repeat-run evidence.
