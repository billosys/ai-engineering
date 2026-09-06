# Slice04 Plan: Relationships, CQs, Reconciliation, And Memory

```yaml
project: project05-concept-card-skill
arc: arc03-concept-cards-skill-core
slice: slice04-relationships-cqs-reconciliation-memory
status: open
opened: 2026-09-06
depends-on:
  - slice01-source-scaffold-and-load-contract
  - slice02-extraction-reextraction-provenance
  - slice03-evidence-validation-verification
```

## Goal

Complete the Arc03 `concept-cards` source-guidance core by adding the remaining
relationship/CQ, reconciliation, memory-admission and maintenance/promise
boundary guides. This slice turns guides 06, 07, 09 and 10 from future routes
into live, detailed procedures while preserving the source/package boundaries
assigned to Arc04 and Arc05.

## Scope

In scope:

- add `knowledge/concept-cards/guides/06-graph-cq.md`;
- add `knowledge/concept-cards/guides/07-reconciliation.md`;
- add `knowledge/concept-cards/guides/09-memory-admission.md`;
- add `knowledge/concept-cards/guides/10-maintenance-packaging.md`;
- update `knowledge/concept-cards/SKILL.md` so guides 01 through 10 are live;
- update `knowledge/concept-cards/version-history.md`;
- update existing guides 01 through 05 and 08 only as needed to remove stale
  future-route wording and route the now-live detailed guides accurately;
- advance the source skill version from `1.2.0` to `1.3.0`;
- define relationship edge identity, endpoint discipline, directionality,
  support/provenance, lifecycle attachments and non-runtime graph boundaries;
- define competency question identity, coverage assertions, answerability
  review, retrieval-probe limits, obsolete/deferred CQs and handoff output;
- define reconciliation workflow for duplicate concepts, competing definitions,
  slug/taxonomy drift, conflicting support, relationship asymmetry, CQ coverage
  disagreements, preservation implications and reconciliation results;
- define memory admission as an evidence-dependent reliance decision distinct
  from artifact retention, validation, verification, reconciliation,
  preservation and memory-runtime writes;
- define maintenance and package promise boundaries for this source-only skill
  core, including what Arc04 and Arc05 still own.

Out of scope:

- adding templates, examples, validation/reference support directories,
  schema files or executable validators;
- adding package targets, Makefile changes, README/docs changes, generated
  zips, install wiring or package path exceptions;
- performing live graph construction, ontology engineering, GraphRAG, CCDP
  service integration, memory runtime automation, database work or live corpus
  processing;
- recreating `knowledge/concept-card-method/` or
  `knowledge/source-preparation/`.

## Required Design Pressure

The new guides must support both human-assisted and agent-direct operation.
They should be procedural enough for an assistant to inspect accessible card
sets, identify edges/CQs/conflicts/admission gates, and produce scoped handoff
records, while preserving uncertainty when source material, reviewer evidence
or operator acceptance is unavailable.

Relationship and CQ guidance must keep these concerns separate:

- edge identity versus card-local navigation;
- endpoint validity versus relationship warrant;
- CQ coverage versus answerability;
- retrieval success versus admission or verification;
- graph representation guidance versus runtime graph/database construction.

Reconciliation guidance must prevent silent loss of prior value. It must retain
conflicts, competing interpretations and unresolved dependencies at their
actual scope instead of letting a rewritten card or clean validation result
erase them.

Memory-admission guidance must make admission a deliberate, evidence-dependent
decision. A file existing, a card validating, a claim verifying, a conflict
reconciling, or a prior annotation being preserved does not by itself authorize
durable semantic reliance or a memory-runtime write.

## Exit Criteria

Slice04 is complete when:

- guides 06, 07, 09 and 10 exist and are routed as live from `SKILL.md`;
- `SKILL.md` and `version-history.md` agree on version `1.3.0`;
- guide 06 covers relationship edges, endpoints, directionality, source
  support, lifecycle attachments, competency questions, CQ coverage,
  answerability, retrieval-probe limits, both operating modes and handoff;
- guide 07 covers reconciliation targets, conflicts, duplicate concepts,
  competing definitions, slug/taxonomy drift, relationship/CQ disagreements,
  preservation implications, reconciliation results, both operating modes and
  handoff;
- guide 09 covers evidence-dependent memory admission, required inputs,
  acceptance boundaries, rejection/deferment, revision invalidation, both
  operating modes and handoff;
- guide 10 covers maintenance ownership and promise boundaries without
  claiming Arc04 templates/examples/schema/support or Arc05 package/docs/install
  work as done;
- existing guides no longer say guides 06, 07, 09 or 10 are unavailable after
  this slice lands;
- no old roots, templates/examples/support dirs, package/docs/install changes,
  executable validators, live corpus checks, runtime behavior, graph databases,
  ontology databases, GraphRAG, CCDP services or memory automation are added;
- focused validators and local Markdown link checks pass.

## Expected Artifacts

No separate durable planning artifacts are expected. Implementation output is
the source files listed above. Durable close evidence belongs in this slice's
`closing-report.md`, `ledger.md`, and later `cdc-verification.md`.
