# v4.0 Validator Scope and Test Plan

```yaml
project: project03-concept-card-method
arc: arc05-implementation-plan
slice: slice03-schema-validation-plan
artifact: v40-validator-scope-test-plan
status: proposed-done
validator-code-scope: source documentation only for first implementation plan
```

## Purpose

This artifact decides validator-code scope, test scope, invalid example and
failure-output expectations, and what remains manual or deferred for the
first implementation plan.

This is planning only. It does not edit source, does not implement executable
validators, does not implement tests, does not create generated zips, does not
perform package release, does not claim release readiness, and does not create
runtime services, GraphRAG, graph database, ontology database, memory runtime,
CCDP service, or live extraction behavior.

## Validator-Code Scope Decision

Accepted Slice03 decision: validator-code scope for the first implementation
plan is source documentation only. Executable validator implementation is
explicitly deferred.

Rationale:

- The planned v4.0 method skill can ship schema, enum, validation, and review
  guidance as package-compatible documentation under `guides/`.
- The schema and enum vocabulary need human review stability before executable
  checks become a maintenance burden.
- Slice04 has not yet accepted Makefile targets, package list edits,
  package-path checks, generated zip policy, release gates, or source version
  history obligations.
- Executable validator-code would require implementation language,
  repository integration, failure message, and test harness decisions that
  belong to a later implementation owner after Slice04 and Slice05.

## First Implementation Test Scope

The first implementation plan should include documentary test scope, not
executable test files:

- examples should cover every release-critical example class from Arc04;
- invalid example expectations should be documented as named cases;
- failure-output expectations should describe what a future validator would
  report without implementing the validator;
- manual review checklists should cover semantic audit and human/operator
  review boundaries;
- package and release tests should be routed to Slice04.

## Invalid Example Expectations

Document these invalid example cases for later executable validation:

- missing required concept card frontmatter;
- missing required concept-card section;
- unsupported enum value;
- claim without source support;
- source support without source span;
- source span without source locator;
- relationship edge with missing endpoint;
- directional relationship missing direction metadata;
- CQ coverage reference to a missing card, claim, or edge;
- extraction run without source snapshot or agent scope;
- validation result without target reference;
- verification result without evidence reference;
- reconciliation result without conflict class or decision;
- preservation decision without old-card reference or rationale;
- memory admission record without validation, verification, reconciliation, or
  operator acceptance fields where required.

## Failure-Output Expectations

Future validator failure-output should be deterministic and reviewable:

- include file path;
- include record id when available;
- include field or section name;
- include expected value or allowed enum values;
- include observed value when available;
- distinguish error from warning;
- include a short failure message suitable for ledger evidence;
- avoid claiming semantic correctness from structural checks.

Failure message text is not finalized by Slice03. Exact failure-message format
belongs to the future implementation owner after Slice04 and Slice05 accept
package and release constraints.

## Manual and Deferred Work

Manual work remains:

- source-aware semantic audit;
- evidence grade adequacy review;
- extraction confidence calibration review;
- relationship meaning review;
- CQ answerability review;
- reconciliation rationale review;
- preservation rationale review;
- memory admission approval;
- material uncertainty and operator override decisions.

Deferred implementation remains:

- executable validator-code;
- executable tests;
- generated zips;
- package target implementation;
- package list edits;
- package-path exception rows;
- package release;
- release gate implementation;
- source version-history text;
- runtime services, GraphRAG, graph database, ontology database, memory
  runtime, CCDP service, and live extraction behavior.

## Later-Slice Routing

- Slice04 owns README, library discoverability, Makefile package target
  names, package list edits, package-path exception rows, package-path checks,
  generated zip policy, release gate details, package release boundaries, and
  source version history.
- Slice05 owns implementation-plan synthesis, implementation slice
  recommendations, deferral register, and Project03 close input.

Slice03 found no validator-scope or test-scope fact that requires Arc05
re-sequencing, a new slice, or a scope correction.
