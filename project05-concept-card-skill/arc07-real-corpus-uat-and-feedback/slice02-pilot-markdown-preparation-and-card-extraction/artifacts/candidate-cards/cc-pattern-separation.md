---
record_type: concept-card
id: cc-pattern-separation
revision: 1
title: Pattern separation limits interference
concept_slug: pattern_separation
aliases: [sparse representations, low-overlap encoding]
card_status: candidate-requires-operator-review
method_ref: {id: concept-cards, revision: "1.7.4", path: "../../../../../../../knowledge/concept-cards/SKILL.md"}
actor: {id: codex-cc, role: extractor, mode: agent-direct}
created_at: 2026-09-11
source_refs: [{id: ccn-book, revision: e0c697b4, path: "../source-acquisition.md"}]
prepared_source_refs: [{id: ps-ccn-book-pilot-20260911, revision: 1, path: "../prepared-source-manifest.md"}]
claim_refs: [{id: claim-pattern-separation, revision: 1, path: "#claim-pattern-separation"}]
relationship_refs: []
cq_refs: []
run_refs: [{id: run-arc07-s02-pilot, revision: 1, path: "../extraction-run.md"}]
extraction_confidence: {assessment: high-for-selected-span, rationale: "Direct inspection of selected text and named figure asset, with cited literature held caveated.", scope: "claim-pattern-separation"}
validation_refs: []
verification_state: unassessed
verification_refs: []
reconciliation_state: unassessed
reconciliation_refs: []
preservation_refs: []
memory_admission_ref: null
---

# Concept Card: Pattern Separation Limits Interference

## Concept Boundary And Summary

This candidate concerns the source's claim that low-overlap neural patterns
support rapid encoding of novel episodes with less interference from prior
learning. It excludes a claim that the mechanism is conclusively established,
that a particular cited study proves it, or that it applies unchanged outside
the source's hippocampal framing.

## Claims And Evidence

### Claim `claim-pattern-separation`

The source reports that pattern separation enables the hippocampus to rapidly
encode novel episodes with minimal interference on prior learning because the
involved neuron patterns overlap relatively little.

Support: [support-pattern-separation.md](./support-pattern-separation.md).

## Relationships And Competency Questions

The source discusses a tradeoff with pattern completion, but this candidate
does not assert an edge because the tradeoff's cited basis and downstream
Executive Function cross-reference have not been reviewed.

## Provenance And Preparation Limits

The claim uses `chapter-07.md` lines 67-75 and direct inspection of
`figures/fig_patsep_clr.png`. The figure visibly contrasts sparse hippocampal
with overlapping cortical activation patterns. The `@Marr71` citation at line
67 was identified but its cited work was not inspected.

## Lifecycle And Prior Value

This candidate is not operator-accepted, independently verified, reconciled,
or admitted to memory. Evidence grade remains scoped to what this source
reports, not a judgment about the underlying neuroscience.

## Handoff And Remaining Work

An operator should evaluate whether to retain the mechanism as one card or
split sparseness, overlap, and interference into distinct reviewed candidates.
