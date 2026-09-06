# Downstream Concept-Card Handoff Template

This optional preparation record passes upstream provenance to `concept-cards`
when requested and available. It is not a concept-card schema and does not
implement card extraction, claim verification, reconciliation or memory
admission. Standalone indexing, reading, source review and analysis use the
[manifest](./manifest.md) and [readiness report](./validation-readiness.md)
without this record. See the [filled handoff](../examples/concept-card-handoff.md).

## Delivery Context

| Field | Value |
| --- | --- |
| Handoff ID / date / preparer / operating mode | <values; direct versus operator-reported evidence> |
| Source / raw or supplied snapshot / conversion / prepared snapshot / run | <IDs; unavailable values explicit> |
| Requested consumer / availability | <concept-cards; confirmed available, unavailable, or unchecked> |
| Original extraction request and scope | <content, desired provenance properties; no invented card decisions> |
| Evidence home / path convention / manifest | <paths and reference> |
| Prepared inventory / reading order / structure map | <references> |
| Media / locator / validation / caveat records | <references for same run and snapshot> |
| Saved and received status | <storage/reference checks; actual recipient acknowledgement or delivery unverified> |

## Span-Level Provenance

| Section / prepared file and locator | Original locator IDs / snapshot | Mapping evidence / status | Caveats retained | Preparation disposition for requested use |
| --- | --- | --- | --- | --- |
| <section ID; snapshot-bound output span> | <typed endpoints; unknown bases explicit> | <check IDs; verified within scope, inferred, unresolved, unchecked> | <IDs and effects, not only a global caveat link> | <readiness status and limits from report> |

## Consumer Instructions And Open Work

- Preparation status for the full request: <Ready, Caveated, Blocked, Not assessed;
  supporting checks and actual coverage>.
- Limited usable scope if any: <explicit limit; full request still assessed honestly>.
- Preserve with excerpts: <source/snapshot/run IDs, original and output locators,
  map/evidence references, uncertainty and caveat IDs>.
- Required preparation follow-up: <specific affected span and repair/check>.
- Downstream-owned decisions: card and claim semantics, whether source spans
  support a claim, evidence grading, relationships, reconciliation, validation,
  and memory admission. Preparation statuses do not pre-decide these.
- Consumer unavailable: <durable handoff location and pending action; no claim
  that cards were produced or material was admitted to memory>.
