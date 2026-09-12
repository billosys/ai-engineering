---
synthetic: true
surface_class: user-authored
record_type: concept-card
id: cc-synthetic-evidence-map
revision: 1
title: Evidence map
concept_slug: evidence-map
card_status: draft
source_refs:
  - id: source-synthetic-field-guide-001
    revision: 1
    path: sources/synthetic-field-guide-001.md
prepared_source_refs:
  - id: prepared-synthetic-field-guide-001
    revision: 1
    path: document-extraction/prepared/synthetic-field-guide-001.md
claim_refs:
  - id: claim-evidence-map-links-assertions
    revision: 1
    path: records/claim-evidence-map-links-assertions.md
source_support_refs:
  - id: support-evidence-map-definition-001
    revision: 1
    path: records/support-evidence-map-definition-001.md
relationship_refs:
  - id: edge-evidence-map-related-to-claim
    revision: 1
    path: records/edge-evidence-map-related-to-claim.md
cq_refs:
  - id: cq-inspect-support-for-card-statement
    revision: 1
    path: records/cq-inspect-support-for-card-statement.md
run_refs:
  - id: run-synthetic-field-guide-001
    revision: 1
    path: records/run-synthetic-field-guide-001.md
extraction_confidence:
  assessment: direct
  rationale: The fictional source definition is direct in the named section.
  scope: Definition and named example only.
validation_refs: []
verification_state: unassessed
verification_refs: []
reconciliation_state: unassessed
reconciliation_refs: []
preservation_refs: []
memory_admission_ref: null
---

# Rich Profile Card: Evidence Map

**Synthetic example.** The source, support records, and linked control records
are fictional. This example illustrates record shape; it does not claim that a
validation, verification, reconciliation, operator decision, or admission has
occurred.

## Concept Boundary

An evidence map is the source-specific navigation layer connecting a card's
substantive statements to their claims, locators, and support records. It does
not assess the underlying evidence grade or decide whether a claim is true.

## Quick Definition And Core Definition

The fictional field guide defines an evidence map as a list of a statement's
claim identity, source locator, and support attachment. This card preserves that
limited definition; it does not claim every map entry has been semantically
verified.

## Prerequisites And Key Properties

The map depends on stable claim identities and recoverable source locators. Its
key property is inspectability: a reader can find the support attachment for a
named assertion. The fictional source does not establish a complete ontology of
evidence-map types.

## Construction Or Recognition

The fictional guide recognizes an evidence map when each substantive card
statement names a claim and the claim points to a locator-bound support record.
It does not establish a required rendering or file format.

## Context And Application

In the selected fictional guide, the map is used to review a compact card
without treating a bibliography or prepared-source manifest as claim support.
This is a source-reported method context, not a demonstrated operational result.

## Examples

The guide's named example maps the statement "a locator addresses material" to
`claim-evidence-map-links-assertions`, locator `section: definition`, and
`support-evidence-map-definition-001`. The example is source-specific to
`source-synthetic-field-guide-001`, revision 1; it does not establish a general
rule for all documentation systems.

## Common Errors And Common Confusions

The fictional guide distinguishes a source bibliography from an evidence map:
the former identifies a work, while the latter identifies the support relation
for a particular assertion. No procedural misuse is established in the selected
source, so that part is not established in the selected source.

## Source Reference And Support Map

`source-synthetic-field-guide-001`, revision 1, section `Definition` is the
fictional source snapshot. `support-evidence-map-definition-001` connects its
named locator to `claim-evidence-map-links-assertions`. The prepared-source
record is provenance for the fictional text, not support by itself.

## Claims And Evidence

`claim-evidence-map-links-assertions` carries the substantive definition and
its support attachment. Evidence grade is assessed on that claim/support
relationship; this card's direct extraction confidence does not supply it.

## Relationships And Competency Questions

`edge-evidence-map-related-to-claim` is the typed relationship candidate for
the map's connection to claims. `cq-inspect-support-for-card-statement` asks
how a reader can inspect a card assertion's support. This prose does not claim
the edge is warranted or the CQ is answerable.

## Provenance And Preparation Limits

`run-synthetic-field-guide-001` records the fictional extraction scope. The
prepared source is limited to the named guide section; no broader corpus was
inspected.

## Extraction Notes And Review Boundaries

The definition and example were drafted from one fictional source section.
Validation, semantic verification, reconciliation, preservation, operator
acceptance, and memory admission remain unassessed; no result record is linked.

## Lifecycle And Prior Value

This draft card has no validation, verification, reconciliation, preservation,
or memory-admission result. It must not be relied upon as an accepted or
admitted semantic-memory record.

## Handoff And Remaining Work

An actual card using this profile would need its real source snapshot, claims,
locators, support records, and scoped review results. The next bounded check is
to inspect whether each named body statement is warranted by its linked span.
