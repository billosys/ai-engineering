# Representative PDF/Marker Handoff

**Synthetic example.** The source, paths, observations, dates and results below
are invented to demonstrate filled records. No PDF was converted or inspected
for this example; there are no accompanying source files or execution logs.
In a real handoff replace these values and supply the referenced evidence.
This combined report follows the [manifest](../templates/manifest.md),
[locator](../templates/locator-map.md), [media](../templates/media-report.md)
and [readiness](../templates/validation-readiness.md) templates and the
[PDF guide](../guides/04-pdf-source-preparation.md).

## Manifest

| Field | Scenario value |
| --- | --- |
| Manifest / source / title | pdf-manifest-01 / pdf-brief / Wetland Monitoring Brief; author and edition unknown |
| Input / conversion / prepared snapshot / run | pdf-raw-a / pdf-marker-a / pdf-prepared-a / pdf-run-01 |
| Date / mode | 2026-09-06 UTC; human-assisted, operator supplies files and page observations |
| Requested work | Standalone reading of the full three-page brief; full numeric-table analysis; concept-card preparation with verified original locators |
| Path root / evidence home | All scenario file paths resolve from `/case/pdf/`; evidence home `records/run-01/` |
| Inputs preserved | `raw/brief.pdf` (three pages), `conversion/book.md` (90 lines), `conversion/metadata.json`, `conversion/images/figure-1.png` |
| Lineage | Operator identifies Marker; version, command and settings unavailable; no reconversion performed |
| Checksums | Not supplied or measured in this scenario; no byte-identity attestation, C-P3 |
| Derived inventory | `prepared/book.md`, same 90-line order; `prepared/assets/figure-1.png`; no splits or generated headers |
| Transformation | Copy text and image; at line 46 change image target from `images/figure-1.png` to `assets/figure-1.png`; preserve alt text and title; table left unchanged |
| Regeneration | Plan uses preserved conversion into a fresh destination with the same map; not exercised, C-P3 |

Record register: structure = [structure](#structure), media = [media](#media),
locators = [locators](#locators), validation/readiness = [checks-and-readiness](#checks-and-readiness),
caveats = [caveats](#caveats). Every section uses the manifest's source and run;
endpoint snapshots are named where they differ. Storage in a real workspace
is not established by this example; these sections are the illustrative record set.

## Structure

Map pdf-structure-01. All text spans below are one-based inclusive in
`conversion/book.md` (pdf-marker-a), mapped to the same lines in
`prepared/book.md` (pdf-prepared-a). All sections have parent root, no source
anchor, and no generated title or header.

| Order / ID | Original title / kind | Input to output span | Boundary evidence and disposition |
| --- | --- | --- | --- |
| 1 / p-front | Wetland Monitoring Brief / title matter | 1–12 to 1–12 | Operator opening-page comparison; verified within supplied observation |
| 2 / p-method | Monitoring observations / body | 13–78 to 13–78 | Heading/context and complete table inspected; retained in monolith |
| 3 / p-notes | Notes / back matter | 79–90 to 79–90 | Closing content compared; retained, no trailing span discarded |

The three ranges cover lines 1–90 without gaps or overlaps. No split is needed;
table and image context remain together. Counts and range arithmetic support
coverage of the conversion, not completeness or fidelity against the PDF.

## Media

Report pdf-media-01 has one reference and one asset, no unreferenced assets in
the supplied listing. Asset P-A1 is `conversion/images/figure-1.png`, copied to
`prepared/assets/figure-1.png`; format PNG, size/checksum unknown. Reference
P-R1 at conversion line 46 has alt text “Sampling sites” and title “Figure 1”.
Its local resolution base is `/case/pdf/conversion/`; the emitted target
`assets/figure-1.png` resolves from `/case/pdf/prepared/book.md` to
`/case/pdf/prepared/assets/figure-1.png`. Disposition: changed.

Operator-reported existence check covers this one output reference. Identity
and appearance comparison against the PDF were not supplied, C-P3; a resolving
path does not establish that the figure was captured faithfully.

## Locators

Map pdf-locators-01 retains four typed records, all for source pdf-brief:

| ID | Snapshot / resource | Kind / value / basis | Verification |
| --- | --- | --- | --- |
| P-L1 | pdf-marker-a / `conversion/metadata.json` | Converter page index, verbatim `page_id: 1`; numbering basis and sequence scope unknown | Unresolved, C-P1; no physical-page interpretation assigned |
| P-L2 | pdf-raw-a / `raw/brief.pdf` | Physical PDF page 2, one-based within full three-page file; single page | Operator reports viewer position and matching “Monitoring observations” opening; checked at this location only |
| P-L3 | pdf-raw-a / `raw/brief.pdf` | Printed page label `1`, single label on physical page P-L2 | Operator-reported printed label; distinct from ordinal and converter index |
| P-L4 | pdf-prepared-a / `prepared/book.md` | Output lines 13–20, one-based inclusive including all file lines, no added headers | Excerpt received and line position inspected within supplied output |

Mapping P-M1 connects P-L2's opening paragraph to P-L4, verified only within
the operator's paired excerpt; it does not map the entire physical page to
eight lines. P-L3 labels P-L2. P-L1's intended correspondence remains inferred
from heading text and is withheld as a verified relation. No global PDF page
offset follows from this single match. Table lines 50–61 have only output
locations at present; original table-span mapping is unchecked.

## Caveats

All caveats are unresolved, recorded for pdf-run-01 on 2026-09-06, with no
resolution history yet; next actor is the operator. They affect pdf-prepared-a.

| ID / category | Affected input and output / observation | Handling, per-use impact and re-entry |
| --- | --- | --- |
| C-P1 / locator | P-L1 and all mappings based on converter page index; basis not supplied | Preserve raw values; withhold inferred offset. Full concept-card preparation blocked until several separated page/label/content comparisons establish usable original mappings |
| C-P2 / fidelity | `conversion/book.md` and `prepared/book.md` lines 50–61; operator reports two numeric columns merged relative to PDF table | Retain damaged text, do not infer numbers; table analysis blocked. Repair from source and compare every affected cell before changing status |
| C-P3 / lineage and coverage | All preserved inputs lack hashes and exact converter invocation; only selected PDF excerpts and one media path checked; regeneration untested | Keep supplied bundle and reports; full reading caveated for uninspected text/figures. Obtain missing lineage where possible, record identities and complete task-relevant comparisons; later checks cannot retroactively prove the initial bytes |

## Checks And Readiness

| Check | Scenario method / actual coverage | Outcome / evidence in this report |
| --- | --- | --- |
| P-C1 preservation and structure | Operator file listing; inspect all 90 supplied conversion/output lines for retained order and the declared target-only rewrite | Pass for text-span accounting; byte preservation unverified, C-P3; structure table above |
| P-C2 media | Operator reports filesystem resolution of 1/1 output reference | Pass for existence only; media record above; appearance not checked |
| P-C3 original fidelity | Operator page opening/closing excerpts and table observation; remaining body and figure not compared | Fail for table fidelity, C-P2; sampled prose observation does not certify rest |
| P-C4 page mapping | One physical page/label/excerpt pair; no separated page-basis checks | Not checked for global converter basis, C-P1; locator map above |
| P-C5 regeneration | No second run | Not checked, C-P3 |

| Use / full requested scope | Status | Supporting checks / limits / next action |
| --- | --- | --- |
| Reading/source review of full brief | Caveated | P-C1–3; damaged table and uninspected figure/body remain flagged C-P2/C-P3; consult PDF for affected content |
| Numeric-table analysis | Blocked | P-C3, C-P2; source cell comparison and repair required |
| Concept-card preparation of full brief with original locators | Blocked | P-C3/P-C4, C-P1/C-P2/C-P3; verified local excerpt is insufficient for full request |
| Indexing | Not assessed | Not requested |

Prepared location and order: `prepared/book.md`, front then body then notes.
Hand off this whole report with the text. A
[downstream handoff example](./concept-card-handoff.md) shows how the blocking
caveats survive copying a readable excerpt. No claim is made about source
truth or memory admission.
