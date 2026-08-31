# v4.0 Content Sequence Plan

```yaml
project: project03-concept-card-method
arc: arc05-implementation-plan
slice: slice02-source-layout-content-plan
artifact: v40-content-sequence-plan
status: proposed-done
planned-source-home: knowledge/concept-card-method/
```

## Purpose

This artifact decides the content sequence for the planned thin SKILL.md and
supporting guides. It preserves accepted Arc04 problem ownership, dependency
direction, load triggers, guide routing, package behavior, and maintenance
ownership while leaving schema, validation, package, release, and source
version-history mechanics to later Arc05 slices.

This plan is out of scope for source implementation. It does not edit source,
create generated zips, perform package release, claim release readiness,
create runtime services, GraphRAG, graph database, ontology database, memory
runtime, CCDP service, or live extraction behavior.

## Thin SKILL.md Content Sequence

The planned thin SKILL.md at `knowledge/concept-card-method/SKILL.md` should
use this sequence:

1. Frontmatter with skill name, description, version, license, and metadata.
2. One-paragraph purpose: the skill owns concept-card method representation.
3. Reason to load: concept-card extraction, re-extraction, auditing,
   reconciliation, validation, verification, planning, or memory-admission work
   where output must become provenance-bearing concept-card substrate.
4. Positive load triggers: concept-card extraction, re-extraction, claim-level
   source support, source span capture, evidence grade analysis, extraction
   confidence capture, verification state/result capture, validation result
   capture, reconciliation result/state handling, competency question/CQ
   coverage, relationship/edge modeling, preservation decisions, extraction
   run provenance, parallel-worker provenance, and memory admission.
5. Negative load triggers: ordinary research summaries, generic project
   management, ordinary source reading, unrelated domain-knowledge work,
   source implementation planning without concept-card method output, runtime
   service design, GraphRAG design, graph database design, ontology database
   design, memory runtime work, CCDP service work, and memory lookup that does
   not ask for concept-card method output.
6. Problem ownership: this skill owns concept-card method surfaces and routes
   adjacent work to the appropriate skill or planning artifact.
7. Dependency direction: collaboration-framework owns posture and ledgered
   process; domain skills own domain correctness; source-reading practice owns
   faithful evidence capture; Arc05 or later implementation plans own source
   edit and release work.
8. Operator workflow: identify task, choose source snapshot, choose extraction
   or re-extraction path, capture source support, create or revise cards,
   capture lifecycle/result records, run validation candidates, perform
   semantic or human review, reconcile conflicts, decide memory admission, and
   record provenance.
9. Guide routing: link to focused guides by operator task instead of embedding
   the full method in SKILL.md.
10. Templates, examples, and validation documentation routing: point into
    `guides/templates/`, `guides/examples/`, and `guides/validation/`.
11. Package and promise boundary: state that packaged surfaces are planned
    guidance assets and that executable validator-code, generated zip output,
    release gates, source implementation, and runtime systems are not promised
    by the skill text alone.
12. Version history: include a source version history section or route to an
    enclosing source version history location as decided by Slice04.

## Guide Routing Sequence

Guide routing should keep the SKILL.md short and move method detail into
focused guide files:

- `guides/01-load-contract.md`: load boundary, reason to load, positive load,
  negative load, problem ownership, and dependency direction.
- `guides/02-operator-workflow.md`: end-to-end operator workflow and decision
  points.
- `guides/03-extraction.md`: new card extraction, claim capture, source
  support, source span handling, evidence grade, and extraction confidence.
- `guides/04-re-extraction-preservation.md`: re-extraction from old card
  inventory, preservation decision handling, and parallel-worker provenance.
- `guides/05-evidence-lifecycle.md`: lifecycle attachment points and result
  record boundaries.
- `guides/06-graph-cq.md`: relationship, edge identity, CQ coverage,
  answerability, retrieval, obsolete, and deferred roles.
- `guides/07-reconciliation.md`: conflict classes and reconciliation result
  records.
- `guides/08-validation-verification.md`: deterministic validation candidates,
  semantic verification boundaries, and human/operator review routing.
- `guides/09-memory-admission.md`: memory admission as a lifecycle gate.
- `guides/10-maintenance-packaging.md`: maintenance ownership, package
  promise boundary, package-compatible source surfaces, and version history
  routing.

## Template Files

Template file routing should be referenced from the relevant guides:

- `guides/templates/concept-card.md`
- `guides/templates/claim-source-support.md`
- `guides/templates/competency-question.md`
- `guides/templates/relationship-edge.md`
- `guides/templates/extraction-run.md`
- `guides/templates/validation-result.md`
- `guides/templates/verification-result.md`
- `guides/templates/reconciliation-result.md`
- `guides/templates/preservation-decision.md`
- `guides/templates/memory-admission.md`

The template files should carry placeholders and explanatory comments only
where needed. Slice03 owns exact schema syntax, enum spelling, deterministic
validation semantics, validator-code scope, tests, and failure-message format.

## Example Files

Example file routing should be referenced from guides and templates:

- `guides/examples/minimal-card.md`
- `guides/examples/claim-backed-card.md`
- `guides/examples/cq-coverage.md`
- `guides/examples/relationship-edge.md`
- `guides/examples/extraction-run-trace.md`
- `guides/examples/reconciliation.md`
- `guides/examples/memory-admission.md`
- `guides/examples/five-agent-default-recipe.md`

The five-agent default recipe must remain a default recipe, not an invariant.
Actual extraction run records must capture actual agent scope and
parallel-worker provenance.

## Cross-Link Decisions

Accepted cross-link decisions:

- SKILL.md cross-links to `guides/01-load-contract.md` and
  `guides/02-operator-workflow.md` first.
- `guides/02-operator-workflow.md` cross-links to every workflow guide in the
  order an operator normally uses them.
- Extraction and re-extraction guides cross-link to source support templates,
  concept-card templates, extraction-run templates, and example files.
- Evidence lifecycle, graph/CQ, reconciliation, validation/verification, and
  memory-admission guides cross-link to their result-record templates and
  examples.
- `guides/08-validation-verification.md` cross-links to
  `guides/validation/structural-candidates.md`,
  `guides/validation/semantic-review-boundary.md`,
  `guides/validation/human-review-boundary.md`, and
  `guides/validation/deferred-runtime-checks.md`.
- `guides/10-maintenance-packaging.md` cross-links to the package and
  discoverability work planned by Slice04, without choosing package targets or
  release gates.

## First Implementation Edit Order

The first implementation edit order should be:

1. Add the package-compatible source home and directory skeleton:
   `knowledge/concept-card-method/`, `SKILL.md`, and `guides/`.
2. Add thin SKILL.md content through guide routing only.
3. Add `guides/01-load-contract.md` and
   `guides/02-operator-workflow.md`.
4. Add the remaining guide files in numbered order.
5. Add template file stubs under `guides/templates/`.
6. Add example file stubs under `guides/examples/`.
7. Add validation documentation under `guides/validation/`.
8. Add support documents under `guides/reference/`.
9. Run Slice03-planned schema and validation checks when available.
10. Run Slice04-planned package, README, Makefile, package-path, generated zip,
    release gate, and version history checks only after those plans are
    accepted.

## Later-Slice Routing

- Slice03: schema syntax, enum spelling, validator-code scope, deterministic
  validation, tests, failure-message format, source support identity, and
  source span identity.
- Slice04: README/library discoverability, Makefile targets, package target
  names, package list edits, package-path exceptions, package-path checks,
  generated zip policy, generated archives, release gates, package release
  boundaries, and source version-history text.
- Slice05: implementation-plan synthesis, implementation slice
  recommendations, deferral register, source edit sequence composition, and
  Project03 close input.

No layout or content-sequencing fact found in Slice02 requires Arc05
re-sequencing, a new slice, or a scope correction.
