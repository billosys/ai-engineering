# Slice03 Plan: Evidence, Validation, And Verification

```yaml
project: project05-concept-card-skill
arc: arc03-concept-cards-skill-core
slice: slice03-evidence-validation-verification
status: open
opened: 2026-09-06
depends-on:
  - slice01-source-scaffold-and-load-contract
  - slice02-extraction-reextraction-provenance
```

## Goal

Implement the evidence lifecycle and validation/verification core of
`concept-cards`. This slice turns the scaffold's future evidence and review
routes into detailed guides for evidence grade, extraction confidence,
validation results, verification state/results, semantic review boundaries,
and human/operator review boundaries without collapsing them into a single
confidence or approval field.

## Scope

In scope:

- add `knowledge/concept-cards/guides/05-evidence-lifecycle.md`;
- add `knowledge/concept-cards/guides/08-validation-verification.md`;
- update `knowledge/concept-cards/SKILL.md` so guides 05 and 08 are live;
- update `knowledge/concept-cards/version-history.md`;
- update existing guides 01 through 04 only as needed to route guides 03, 04,
  05, and 08 accurately as live and remove stale foundation wording disclosed
  by Slice02 CDC;
- advance the source skill version from `1.1.0` to `1.2.0`;
- define evidence grade as warrant on a claim or claim-source support
  relationship, separate from extraction confidence;
- define extraction confidence as a signal about the extraction act, not a
  warrant, validation result, verification result/state, reconciliation result,
  preservation decision, or memory admission;
- define validation result as structural/reference consistency review, separate
  from semantic verification;
- define verification state/result as scoped checking against evidence, with
  actor, method, target, evidence, scope, outcome, and revision identity;
- define review boundaries for same-context self-checks, human-assisted
  operator reports, agent-direct checks, tool/process checks, and independent
  verification.

Out of scope:

- implementing relationship/CQ guide 06, reconciliation guide 07, memory
  admission guide 09, or maintenance/packaging guide 10;
- adding templates, examples, validation/reference support directories,
  schema files, executable validators, runtime services, graph databases,
  ontology databases, GraphRAG, CCDP services, memory runtime automation,
  package targets, Makefile changes, README/docs changes, generated zips, or
  install wiring;
- performing live validation or verification against a real corpus;
- recreating `knowledge/concept-card-method/` or `knowledge/source-preparation/`.

## Required Design Pressure

The guides must support both human-assisted and agent-direct operation. They
should be procedural enough for an assistant to run bounded structural and
semantic checks when files are accessible, while preserving uncertainty when
source material, independent review, or operator evidence is unavailable.

The evidence lifecycle guide must keep these concerns separate:

- source support and source span;
- evidence grade and its rationale;
- extraction confidence and its rationale;
- validation result;
- verification state and verification result;
- reconciliation state/result;
- preservation decision;
- memory admission.

The validation/verification guide must prevent common false upgrades:

- valid structure is not semantic verification;
- semantic support for one claim does not verify every claim in a card;
- a same-context self-check is not independent verification;
- operator-reported observations are evidence with provenance, not direct
  assistant inspection;
- tool/process output is scoped evidence, not automatically a final method
  verdict;
- memory admission remains future guide 09 work.

## Exit Criteria

Slice03 is complete when:

- guides 05 and 08 exist and are routed as live from `SKILL.md`;
- `SKILL.md` and `version-history.md` agree on version `1.2.0`;
- stale caller wording in guides 01/02 no longer says guides 03/04 are future
  or unavailable, and references to guides 05/08 match their new live status;
- guide 05 covers evidence grade, extraction confidence, source support/span,
  validation result, verification state/result, reconciliation state/result,
  preservation decision, memory admission boundary, and handoff output;
- guide 08 covers structural validation, semantic verification, review actors,
  same-context limits, human-assisted/operator reports, agent-direct checks,
  tool/process checks, independent verification boundaries, outcomes, caveats,
  and handoff output;
- later guide/support/package/runtime work remains explicit future scope;
- no old roots, templates/examples, package/docs/install changes, executable
  validators, live corpus checks, or runtime behavior are added;
- focused validators and local Markdown link checks pass.

## Expected Artifacts

No separate durable planning artifacts are expected. Implementation output is
the source files listed above. Durable close evidence belongs in this slice's
`closing-report.md`, `ledger.md`, and later `cdc-verification.md`.
