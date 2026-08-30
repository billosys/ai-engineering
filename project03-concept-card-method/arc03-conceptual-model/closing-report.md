---
status: closed
closed-on: 2026-08-30
closed-by: Codex Desktop CDC arc-close pass
composition-verdict: delivered
source_checkout: /Users/oubiwann/lab/billosys/ai-engineering
planning_checkout: /Users/oubiwann/lab/billosys/ai-engineering/.worktrees/planning
---

# Arc 03 Close Report: Conceptual Model

## Capability

Arc03 defines the v4.0 conceptual model for the concept-card method. It turns
the Arc02 inventory and gap analysis into a bounded ontology of cards, claims,
source spans, evidence grades, relationships, competency questions, extraction
runs, verifier roles, reconciliation, and memory admission.

Composition verdict: delivered.

## Slice Walk

- Slice01, `slice01-construct-boundaries`: delivered. CDC verified the
  construct boundary model and decision register for the v4.0 method
  constructs.
- Slice02, `slice02-evidence-lifecycle`: delivered. CDC verified the evidence
  lifecycle model and decision register that separate extraction confidence,
  source support, evidence grade, verification state/result, reconciliation
  state/result, validation result, and memory admission.
- Slice03, `slice03-graph-cq-run-semantics`: delivered. CDC verified the
  graph/CQ/run semantics model and reconciliation/traceability decision
  register.
- Slice04, `slice04-model-synthesis`: delivered. CDC verified the accepted
  v4.0 conceptual model, synthesized model decision register, and skill
  architecture handoff input.

Slice count: 4. This matches the Arc03 slice breakdown.

## Composition Check

Arc-capability-as-specified:

- Define the v4.0 ontology of the method across concept cards, claims, source
  spans, evidence grades, relationships, competency questions, extraction
  runs, verifier roles, reconciliation, and memory admission.
- Preserve the boundary between conceptual model, skill architecture, package
  behavior, deterministic validator implementation, README integration, and
  source edits.
- Leave an accepted model and explicit inputs for later skill-architecture
  planning.

Arc-capability-as-delivered:

- Slice01 established construct boundaries and accepted/provisional
  classifications for the candidate v4.0 constructs.
- Slice02 separated lifecycle and evidence concerns that v3.2 had partly
  overloaded into confidence, validation, or prose.
- Slice03 defined graph-native relationship/edge semantics, CQ roles and
  coverage semantics, extraction-run traceability, and reconciliation result
  semantics.
- Slice04 synthesized those layers into the accepted v4.0 conceptual model,
  consolidated model decisions, and prepared the architecture handoff input.

Silent drops: none identified.

## Arc Ledger Walk

- A-1: done. Slice01 has `cdc-verification.md`; the verification file records
  reproduced rows and closure.
- A-2: done. Slice02 has `cdc-verification.md`; the verification file records
  reproduced rows and closure.
- A-3: done. Slice03 has `cdc-verification.md`; the verification file records
  reproduced rows and closure.
- A-4: done. Slice04 has `cdc-verification.md`; the verification file records
  reproduced rows and closure.
- A-5: done. CDC reproduced the arc-scale grep showing concept card, claim,
  source span, evidence grade, relationship, competency question, extraction
  run, verifier, reconciliation, memory admission, construct boundary, and
  v4.0 conceptual model coverage across `slice*/artifacts` and `arc-plan.md`.
- A-6: done. CDC reproduced the arc-scale grep showing extraction confidence,
  source support, evidence grade, verification state, reconciliation state,
  memory admission, `not one confidence field`, and lifecycle separation
  across `slice*/artifacts`.
- A-7: done. CDC reproduced the arc-scale grep showing relationship/edge,
  competency-question/CQ, extraction-run, traceability, carry-forward, and
  v3.2 preservation terms across `slice*/artifacts`.
- A-8: done. CDC reproduced the arc-scale grep showing the boundary that this
  arc does not choose skill layout, package behavior, deterministic
  validators, README integration, source edits, or later-arc work.

## Accumulated Arc-plan Changes

- v1.1: Slice01 verified-closed; Slice02 could proceed with lifecycle focus.
- v1.2: Slice02 opened for evidence and lifecycle semantics.
- v1.3: Slice02 verified-closed; Slice03 could proceed against reserved
  lifecycle attachment points.
- v1.4: Slice03 opened for relationship, CQ, extraction-run, and reconciliation
  semantics.
- v1.5: Slice03 verified-closed; Slice04 could synthesize construct
  boundaries, evidence/lifecycle semantics, graph/CQ/run semantics, and
  provisional decisions.
- v1.6: Slice04 opened for model synthesis and acceptance.
- v1.7: Slice04 verified-closed; Arc03 ready for formal arc close.

## Bubble-up to Project03

Arc03 delivered the conceptual-model capability named in the Project03 roadmap.
The project now has an accepted v4.0 conceptual model and a bounded input
packet for skill-architecture planning.

What this arc revealed:

- The visible card can remain the authoring unit while claims become the finer
  support, evidence, verification, reconciliation, and memory-admission unit.
- Evidence, lifecycle, graph/CQ/run, reconciliation, and memory-admission
  constructs are interdependent enough that Arc04 should preserve the accepted
  conceptual model before deciding file layout or package behavior.
- Exact schema syntax, enum spelling, validator implementation, package
  behavior, README integration, and source edits remain correctly deferred.

Project-plan change required: status-only plus marking Project03 P-3 done.
No roadmap re-sequencing or new arc is required. Arc04 can be planned next.

## What Worked / What Recurred

- Layering construct boundaries before lifecycle and graph/CQ/run semantics
  made the final synthesis smaller and less ambiguous.
- Scope fences recurred as useful protection: each slice added its assigned
  model layer without consuming later architecture or implementation work.
- The final synthesis artifact gives the next arc one accepted model to
  preserve rather than asking it to infer the model from several slice-local
  documents.

## Closure

Composition verdict: delivered.
Gate reviewed by: Codex Desktop CDC arc-close pass.
Slices: 4.
Findings dispositioned: 0 new remediation findings; status-only bubble-up
routed to Project03 and Arc04 readiness.

Rows: 8. Done: 8. Deferred: 0. No-op: 0.
