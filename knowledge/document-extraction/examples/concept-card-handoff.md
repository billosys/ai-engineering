# Representative Downstream Concept-Card Handoff

**Synthetic example.** This fills the
[handoff template](../templates/concept-card-handoff.md) using the invented
[PDF/Marker case](./pdf-marker-handoff.md). No concept-card extraction,
consumer delivery or source verification was performed. This is preparation
provenance, not a concept-card record or evidence grade.

## Delivery Context

| Field | Scenario value |
| --- | --- |
| Handoff / date / preparer | pdf-to-cards-01 / 2026-09-06 UTC / assistant assembling operator-supplied observations |
| Mode | Human-assisted; operator observations remain labelled in upstream checks |
| Source / raw / conversion / prepared snapshot / run | pdf-brief / pdf-raw-a / pdf-marker-a / pdf-prepared-a / pdf-run-01 |
| Original request | Prepare the full Wetland Monitoring Brief for concept-card extraction with verified original-source locators, including table-based statements |
| Consumer / availability | `concept-cards`; availability unchecked in this scenario; no dependency for standalone document use |
| Path root / evidence home | `/case/pdf/` / `records/run-01/` |
| Prepared file and order | `prepared/book.md`; p-front, p-method, p-notes |
| Manifest / structure / media / locators | pdf-manifest-01 / pdf-structure-01 / pdf-media-01 / pdf-locators-01 in the linked PDF case |
| Validation and caveats | P-C1–P-C5 and C-P1–C-P3 in that case; IDs resolve to the same source, snapshots and run |
| Storage / received status | Example text only; no actual evidence-home files or recipient acknowledgement; delivery unverified |

## Span-Level Provenance

| Prepared content | Original or conversion locations | Mapping evidence / status | Caveats passed with the span |
| --- | --- | --- | --- |
| p-method opening, P-L4: output lines 13–20 in pdf-prepared-a `prepared/book.md` | P-L2 physical page 2 (one-based full PDF), P-L3 printed label `1`; P-L1 converter `page_id: 1` has unknown basis | P-M1, operator paired-excerpt observation only; P-L1 relation unresolved; no inferred global offset | C-P1 page basis, C-P3 limited checks/unknown lineage; excerpt does not approve full request |
| p-method table, output lines 50–61 in the same snapshot, one-based inclusive | Original table span not mapped; do not substitute the opening paragraph's page locator | P-C3 reports merged numeric columns; original table mapping unchecked | C-P2 damaged cells, C-P1/C-P3 provenance and coverage limits; table-dependent extraction blocked |
| p-front and p-notes, output lines 1–12 and 79–90, one-based inclusive | Conversion has same spans in pdf-marker-a; full original spans not recorded | P-C1 supports conversion-to-output coverage only | C-P3 original fidelity and lineage limits; do not invent original locators |

The recipient must retain source/snapshot/run IDs, typed original and output
locations, map/check references, and the specific caveats with any excerpt.
A readable paragraph cannot erase uncertainty attached to its mapping, and a
printed page label cannot silently replace a physical ordinal.

## Disposition And Next Actions

Preparation status for the full concept-card request: **Blocked**, as in the
upstream report. P-C3 and P-C4 leave table fidelity and original locator
coverage insufficient; C-P1–C-P3 remain attached. A limited opening excerpt
has an operator-reported local mapping, but the original full-source request
has not been narrowed or satisfied by that sample.

Next preparation work: compare separated PDF/converted locations to establish
page mapping, inspect and repair every affected table cell from the original,
record table-span locators, then rerun affected checks under a new prepared
snapshot/run. Preserve pdf-prepared-a and its existing locator meanings.
Do not replace unknown lineage with guessed tool settings.

Once available, `concept-cards` owns source-support judgments, card/claim
semantics, evidence grading, relationships, reconciliation, validation and
memory admission. This handoff pre-decides none of them. No cards or admitted
memories are claimed here. Independently, the same upstream bundle remains
Caveated for standalone reading/source review, Blocked for numeric-table
analysis, and Not assessed for indexing, exactly as its readiness report says.
