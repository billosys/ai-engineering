# Arc07 Candidate-Set Handoff Manifest

## Purpose And Status

This manifest hands a bounded, inspectable candidate set to future
memory-protocol, RAG, graph, or MCP planning. It is a planning input, not an
import package, a runtime ingestion record, or evidence of retrieval quality.

| Field | Value |
| --- | --- |
| Corpus | *Computational Cognitive Neuroscience*, Fifth Edition |
| Upstream | `https://github.com/compcogneuro/book` |
| Pinned commit | `e0c697b4d4d134f29cb5c2bbde41b1b6b409b63d` |
| Tree | `894b3e10baa38e9d9c29a2e52b64f4d0ffb1378a` |
| License basis | CC-BY-4.0; preserve attribution and modification handling recorded in Slice01 |
| Candidate count | 10, at their original Slice02 and Slice04 paths |
| Coverage | Chapter 1 framing inputs and a bounded Chapter 7 memory subset |
| Candidate lifecycle | All require operator review; none is operator-accepted, independently semantically verified, reconciled, preserved, admitted to memory, or runtime-ingested |

## Handoff Contents

| Item | Location | Consumer use |
| --- | --- | --- |
| Candidate identities and locations | [candidate-set inventory](./candidate-set-inventory.md) | Resolve the ten source records without copying or silently normalizing them. |
| Projection requirements | [projection assumptions](./projection-assumptions.md) | Design a later import representation that keeps provenance and lifecycle state. |
| Query and access inputs | [query and access needs](./query-and-access-needs.md) | Define operator tasks before retrieval or MCP implementation. |
| UAT result synthesis | [UAT synthesis](./uat-synthesis.md) | Understand the protocol, real-use outcomes, refinement, no-ops, and limitations. |
| Coverage and re-entry | [coverage caveats and re-entry](./coverage-caveats-and-reentry.md) | Keep partial coverage visible and prevent a false full-book claim. |
| Non-runtime boundary | [runtime boundary](./runtime-boundary.md) | Keep this planning handoff distinct from a deployed system. |
| Arc close composition input | [Arc07 close inputs](./arc07-close-inputs.md) | Support Arc07 composition and the Arc08 closure refresh. |

## Required Consumer Checks

Before a downstream project projects any record, it must resolve every listed
candidate path, retain the pinned-source identity and locator, carry forward
the evidence and dependency caveats, and make a new decision about review,
verification, reconciliation, preservation, and admission. A projection may
add operational identifiers later; it may not replace these records as the
source of truth.
