---
project: project08-concept-card-metadata
arc: arc01-metadata-research-and-requirements
status: active
version: "1.3"
---

# Metadata Research And Requirements

Establish what the historical cards and prompts enabled, what the current skill
represents or loses, and what a general, queryable profile must preserve. Ground
the architecture handoff in actual artifacts and primary-source research.

Consumes the Project08 operator brief, current source skills, historical prompts
and card corpora, and Project05 UAT evidence. Delivers requirements and alternatives
to Arc02; no field layout or particular standard is accepted by this arc merely
because it appears in the initial hypothesis.

## Slice Breakdown

| Slice | Scope | Dependency | State |
| --- | --- | --- | --- |
| `slice01-metadata-inventory-and-research-questions` | Reproduce field/capability inventory, register baseline evidence and formulate research questions | Project brief | CDC changes required; Iteration 03 ready for CC |
| `slice02-standards-and-source-model-research` | Primary-source research on classification, source identity/locators, typed relations, provenance and metadata profiles | Slice01 inventory/questions | Plan after Slice01 review |
| `slice03-requirements-and-acceptance-design` | No-loss requirements, migration/query fixtures and repeated-run quality criteria for architecture/UAT | Slice01/02 | Plan when near |

Add or split slices if inventory or research reveals a larger problem. A complete
inventory does not require every card body to be read in one session: parse all
available frontmatter to discover fields and value shapes, then inspect named
representative and anomalous records. Capture unavailable evidence explicitly.

Research should compare candidate standards such as SKOS, Dublin Core application
profiles, BIBFRAME and PROV-O with the practical needs of plain Markdown/YAML
cards. Examine locator approaches and domain-specific relationship predicates
separately. Keep classification broader/narrower distinct from pedagogical
prerequisites. Consult NeON or other ontology-method sources when relevant to
competency questions or requirements engineering. Seek benefits and costs, not
standards adoption for its own sake.

## Acceptance And Handoff

Current: Iteration 02 now reproduces the typed fixture and all 308 normalized
paths. Iteration 03 repairs JSON/control-character and framing classification
failures, finishes the semantic crosswalk and supplies working verification
commands. Current assignment: Slice01 `artifacts/iteration-03-cc-prompt.md`.
The earlier Iteration 01/02 assessment below is historical.

Slice01 Iteration 01 removed Ruby and corrected headline populations, but CDC
reproduction found boolean/type loss and omitted null/empty field paths. All
307 semantic dispositions still contain the same deferred-decision placeholder.
Iteration 02 repairs these failures and finishes the original crosswalk and
reproduction requirements. Current review and assignment live in Slice01
`cdc-verification.md` and `artifacts/iteration-02-cc-prompt.md`. Was:
Iteration 01 pending. Slice02 remains unopened until this evidence is corrected
and independently verified.

The [arc ledger](./ledger.md) requires both child verification and a composition
check: trace every operator concern through observed examples, research questions,
evidence and a testable requirement. Include unresolved alternatives and an Arc02
decision agenda. The later trial rubric must measure usable output, not only
template conformance. Architecture, implementation and actual extraction remain
later work, with evidence ownership recorded rather than presumed complete.

## Version History

- 1.3 (2026-09-12): Slice01 Iteration 02 independently reproduces the census
  and path coverage, resolving R6/R7's original data failures. Remaining
  R2/R4 and new R8/R9 require Iteration 03. Slice02 remains unopened.

- 1.2 (2026-09-12): Slice01 post-Iteration-01 CDC checks require Iteration 02:
  type preservation, complete path coverage, semantic dispositions and reconciled
  evidence. Ruby removal and deterministic runs are retained as demonstrated
  improvements. No scope reduction or advancement to Slice02.

- 1.1 (2026-09-12): Slice01 CDC findings R1-R5 require a follow-up iteration
  within the existing slice. Was: initial open set ready for CC. No slice-order
  change; research must consume corrected, complete evidence.

- 1.0 (2026-09-12): Initial three-slice hypothesis. Opens inventory first so
  research and acceptance design respond to actual field/capability gaps.
