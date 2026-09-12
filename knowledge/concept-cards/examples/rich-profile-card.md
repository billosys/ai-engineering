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

# Concept Card: Evidence Map

**Synthetic example.** The source, support records, and linked control records
are fictional. This example illustrates record shape; it does not claim that a
validation, verification, reconciliation, operator decision, or admission has
occurred.

## Concept Boundary

An evidence map links a card's substantive statements to the claims, locators
and support records a reviewer needs to inspect them. It is a lookup aid for
source support, not a decision about whether the source is reliable or the card
is admitted.

## Quick Definition And Core Definition

Quick definition: an evidence map shows where to inspect the support for each
important card statement.

Core definition: in the fictional field guide, an evidence map records a
statement's claim identity, source locator and support attachment. Its purpose
is traceability: a reader can move from card prose to the specific support
relation without treating a bibliography, prepared-source manifest or fluent
summary as evidence by itself.

## Prerequisites And Key Properties

- Stable claim identities.
- Recoverable source locators.
- Support attachments that explain what the cited span warrants.
- A compact rendering that helps review rather than interrupting the card.

The fictional source does not establish a complete ontology of evidence-map
types.

## Construction Or Recognition

Recognize an evidence map when the card lets a reviewer answer: "Which claim
does this sentence belong to, and where is the supporting span?" It does not
require a particular table format; the useful feature is recoverable support.

## Context And Application

The fictional guide uses evidence maps in compact concept cards where the main
body teaches the concept and the later support section keeps the assertions
inspectable. The map is especially useful when a card has been prepared from a
converted source, because preparation provenance and claim support must remain
separate.

## Examples

The guide's named example maps the statement "a locator addresses material" to
`claim-evidence-map-links-assertions`, locator `section: definition`, and
`support-evidence-map-definition-001`. The example shows how a reader can jump
from prose to support; it does not prove the statement true in every possible
documentation system.

## Common Errors And Common Confusions

- Confusing bibliography with support: a bibliography identifies a work; an
  evidence map identifies the support relation for a particular assertion.
- Treating a map as verification: the map makes checking possible, but it does
  not say the check has happened.
- Turning the map into the card: the teaching body should remain readable, with
  the map available for inspection.

## Source Reference And Support Map

| Body statement | Claim/support | Locator |
| --- | --- | --- |
| An evidence map links statements to claim/support records. | `claim-evidence-map-links-assertions`; `support-evidence-map-definition-001` | `source-synthetic-field-guide-001`, section `Definition` |
| A prepared-source manifest is provenance, not claim support. | `claim-evidence-map-links-assertions`; `support-evidence-map-definition-001` | `source-synthetic-field-guide-001`, section `Definition` |

## Claims And Evidence

`claim-evidence-map-links-assertions` carries the definition and support
boundary. Evidence grade belongs on that claim/support relationship; this
card's direct extraction confidence does not supply it.

## Relationships And Competency Questions

- Related: claim records and source-support records.
- Contrasts with: bibliography, manifest and validation result.
- CQ: How can a reader inspect the support for a card statement?

The typed relationship candidate is `edge-evidence-map-related-to-claim`; the
CQ candidate is `cq-inspect-support-for-card-statement`. Their presence here
does not establish separate edge warrant or CQ answerability.

## Provenance And Preparation Limits

`run-synthetic-field-guide-001` records the fictional extraction scope. The
prepared source is limited to the named guide section; no broader corpus,
alternate source edition or external evidence was inspected.

## Extraction Notes And Review Boundaries

The definition and example were drafted from one fictional source section. The
main body is intentionally concise; audit detail is kept in the support map and
review sections.

## Lifecycle And Prior Value

This draft card has no validation, verification, reconciliation, preservation,
operator-acceptance, or memory-admission result. It is a sample card shape, not
an accepted semantic-memory record.

## Handoff And Remaining Work

An actual card using this profile would need its real source snapshot, claims,
locators, support records and scoped review results. The next bounded check is
to inspect whether each named body statement is warranted by its linked span.
