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
  version: "1.3.0"
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

Arc04 owns future sibling templates, examples,
validation/reference support and schema material. Arc05 owns future package
targets, generated zips, docs/discoverability and install integration. No
executable validators, runtime services, graph or ontology database, GraphRAG,
CCDP services or memory runtime automation are supplied by this skill.

Source lineage is recorded in the [version history](./version-history.md).
