---
name: concept-cards
description: |
  Create, extract, re-extract, validate, verify, reconcile, and preserve
  provenance-bearing concept cards. Use for claim-level source support,
  evidence distinctions, relationships, competency questions, and memory
  admission decisions. Route raw document extraction and source cleanup to
  document-extraction; ordinary source reading does not require this skill.
license: MIT
metadata:
  version: "1.7.0"
  hermes:
    tags: [concept-cards, provenance, knowledge, evidence]
    category: method-skills
---

# Concept Cards

Use this method when the requested output is a durable concept-card knowledge
substrate. Keep one concept per card, synthesize faithfully from sources, and
retain enough provenance to inspect each substantive assertion's basis.

## When To Use

- Create or extract concept cards, including claims and their source support.
- Re-extract from sources, compare prior cards, and record preservation decisions.
- Validate structure, verify source support, or reconcile competing card material.
- Work on relationship edges, competency questions (CQs), and CQ coverage.
- Assess evidence grade, extraction confidence, lifecycle results or memory admission.

## When Not To Use

Ordinary source reading, research summaries and domain analysis do not require
concept cards. Generic document extraction or source cleanup belongs to
`document-extraction`. Generic ontology/database design, GraphRAG, runtime or
CCDP service work, memory lookup, project/package planning and installation
belong to their relevant workflows unless a separate concept-card output is
actually requested.

## Ownership And Dependencies

This skill owns concept-card method representation and its evidence lifecycle.
A concept card organizes a concept; a claim states an assertion; source support
connects that assertion to a source span identified by a source locator.
Bibliographic identity or a prepared document alone is not claim support.

Route raw PDF/EPUB/HTML and converted-source cleanup to `document-extraction`
when preparation is needed. Consume its snapshot, manifest, mappings, readiness
and caveats as upstream provenance. Inspect the relevant content before
claiming it supports a card, claim, relationship edge or CQ coverage assertion.
Preparation readiness does not establish semantic verification or admission.

Keep evidence grade, extraction confidence, validation result, verification
state/result, reconciliation state/result, preservation decision and memory
admission distinct. Do not compress them into one confidence or approval field.
See the [load contract](./guides/01-load-contract.md) for construct boundaries
and the [operator workflow](./guides/02-operator-workflow.md) for working in
human-assisted or agent-direct mode.

Domain guidance remains responsible for domain correctness. Use
`collaboration-framework` for posture, ledger discipline and project/close
mechanics when that work requires them; loading this method does not create a
project or imply permission to build a runtime or write to a memory system.

## Guide Map

| Need | Route | Availability |
| --- | --- | --- |
| Select method scope and preserve construct distinctions | [Load Contract](./guides/01-load-contract.md) | Live |
| Establish inputs, operating mode, outputs and review handoff | [Operator Workflow](./guides/02-operator-workflow.md) | Live |
| Source-faithful extraction, claims and run provenance | [Extraction](./guides/03-extraction.md) | Live |
| Source-primary re-extraction and prior-value preservation | [Re-Extraction And Preservation](./guides/04-re-extraction-preservation.md) | Live |
| Evidence lifecycle, source support, evidence grade and extraction confidence | [Evidence Lifecycle](./guides/05-evidence-lifecycle.md) | Live |
| Relationships, edge identity and CQ coverage/answerability | [Relationships And CQs](./guides/06-graph-cq.md) | Live |
| Conflicts and reconciliation results | [Reconciliation](./guides/07-reconciliation.md) | Live |
| Structural validation and semantic verification | [Validation And Verification](./guides/08-validation-verification.md) | Live |
| Evidence-dependent memory admission | [Memory Admission](./guides/09-memory-admission.md) | Live |
| Maintenance ownership and package promise boundaries | [Maintenance And Package Boundaries](./guides/10-maintenance-packaging.md) | Live |

All guides 01 through 10 are live. Choose the guide for the requested
operation; completing one procedure does not imply completion of the others.
Guide 10 records maintenance ownership and the remaining delivery boundaries.

## Record Templates

The twelve sibling templates, eight representative examples, and sibling
reference/review material below are live source support. These documents describe
record conventions and review candidates; they are not executable schemas or
validators.

| Surface class | Copy when needed |
| --- | --- |
| User-authored | [Concept card](./templates/concept-card.md), [claim](./templates/claim.md), [source support](./templates/source-support.md), [relationship edge](./templates/relationship-edge.md), [competency question](./templates/competency-question.md) |
| Trace record | [Source locator](./templates/source-locator.md), [extraction run](./templates/extraction-run.md) |
| Result record | [Validation result](./templates/validation-result.md), [verification result](./templates/verification-result.md), [reconciliation result](./templates/reconciliation-result.md), [preservation decision](./templates/preservation-decision.md), [memory admission](./templates/memory-admission.md) |

## Representative Examples

These synthetic examples illustrate bounded record combinations. They are not
real corpus work, successful independent verification, or memory-system writes.

| Need | Example |
| --- | --- |
| One concept with explicit unknowns | [Minimal card](./examples/minimal-card.md) |
| Claim-specific source support | [Claim-backed card](./examples/claim-backed-card.md) |
| CQ component coverage and answerability | [CQ coverage](./examples/cq-coverage.md) |
| Directed relationship with scoped support | [Relationship edge](./examples/relationship-edge.md) |
| Prepared-source extraction provenance | [Extraction-run trace](./examples/extraction-run-trace.md) |
| Conflict comparison and prior-value retention | [Reconciliation](./examples/reconciliation.md) |
| Scoped reliance decision without a runtime write | [Memory admission](./examples/memory-admission.md) |
| Default parallel roles and recorded actual scope | [Parallel-worker default recipe](./examples/parallel-worker-default-recipe.md) |

## References And Review Surfaces

The sibling [reference index](./references/README.md) documents field groups,
vocabulary, structural candidates, semantic audit boundaries, and operator review
gates. It is live source support and is copied by the Makefile package target.
Docs/discoverability and isolated install-smoke evidence remain later Arc05
work.

Copy only records the task needs into its accepted artifact home. Replace
placeholder text and null identities; keep unknown or unassessed values explicit
with reasons. Empty lists mean no entries recorded, not that review found none.
These Markdown records with YAML frontmatter and named sections are templates,
not finalized schemas, enum definitions, validators or completed results.

Use stable `id` and `revision` values for each record. Unless a field describes
a different shape, a singular `*_ref` takes a mapping with `id`, `revision` and
`path`; `*_refs` takes a list of those mappings. Add `record_type` or a section
anchor when the target needs disambiguation. Paths locate records; IDs and
revisions preserve identity. Source snapshots and method/prompt references must
identify the actual input or procedure revision, not merely a mutable title.
Record unknown identity or inaccessible references with the affected limitation.

Bodies explain rationale, scope and how to fill structured lists. Keep result
references separate from summarized lifecycle states and tie every assessment
to its actual subject, actor, evidence and revision. Draft/unassessed values do
not claim a check, resolved conflict or admission. Rebase skill-document links
when copying outside this directory and preserve resolvable evidence links;
do not leave template-relative paths pretending to locate the copied records.

Arc05 owns remaining docs/discoverability and install integration work. No
executable validators, runtime services, graph or ontology database, GraphRAG,
CCDP services or memory runtime automation are supplied by this skill.

Source lineage is recorded in the [version history](./version-history.md).
