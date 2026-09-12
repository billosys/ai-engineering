# Rich Concept-Card Profile Design

## Decision

Real-corpus extraction defaults to a rich readable card body plus the existing v4 record/lifecycle control layer. The body serves learning and reference use; v4 fields and linked records state what supports it and what review has occurred. Neither replaces the other.

## Required Body Sections

| Section | V4 coexistence rule |
| --- | --- |
| Concept boundary | State one-concept scope and exclusions; do not hide a multi-concept record in a rich body. |
| Quick definition and core definition | Keep qualified, source-faithful explanation; substantive assertions retain claim/source-support links. |
| Prerequisites and key properties | Explain dependencies and defining conditions; prose does not create typed edges. |
| Construction / recognition | Give only source-supported procedures or cues; state not applicable/unresolved with reason instead of inventing one. |
| Context and application | Preserve source/report/inference distinction, conditions, and limits. |
| Examples | Use named source-specific examples and worked examples only where supported by locators and source support. |
| Relationships and CQs | Explain useful connections; typed edge/CQ records remain authoritative and absence stays explicit. |
| Common errors and common confusions | Keep procedural misuse separate from conceptual misunderstanding; use source-, domain-, or marked review-informed material only. |
| Source reference and support map | Point to snapshots, locators, claims, and support; prepared source is provenance, not support. |
| Extraction notes and review boundaries | Explain extraction rationale/caveats and name linked checks; it cannot claim a check without a v4 result record. |

Every section is present in the rich template. A section lacking source-supported material says `not applicable`, `not established in the selected source`, or `unresolved`, with a reason. Generic filler is not compliance.

## Required Control Layer

Keep stable identity/revision; source and prepared-source provenance; claim/source-support and extraction-run references; evidence grade; extraction confidence; validation and verification results/states; reconciliation; preservation; and memory-admission decision separate. `Extraction notes and review boundaries` replaces the overloaded v3.2 `Verification Notes`; it may link results but never collapse their meanings. Operator acceptance is not a default body result.

## Routing And Non-Goals

Raw PDF/EPUB/HTML conversion, cleanup, mapping, media repair, and locator preparation remain `document-extraction` work. This design creates no graph/RAG/MCP runtime, import automation, retrieval evaluation, memory write, operator acceptance, semantic verification, admission, or full-book claim.
