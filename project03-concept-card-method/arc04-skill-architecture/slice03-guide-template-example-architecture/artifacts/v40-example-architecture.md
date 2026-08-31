# v4.0 Example Architecture

```yaml
project: project03-concept-card-method
arc: arc04-skill-architecture
slice: slice03-guide-template-example-architecture
status: proposed-done
mode: example architecture
```

## Purpose

This artifact defines the example architecture for the first v4.0
concept-card method skill. It decides which examples are release-critical,
which are optional or later, and how examples should preserve the Slice02 load
contract and Arc03 conceptual distinctions.

Examples should demonstrate positive load triggers for concept-card method
work and negative load boundaries for ordinary research, project management,
source reading, implementation planning, and memory lookup.

## Release-Critical Examples

| Example | Status | Coverage required |
|---------|--------|-------------------|
| minimal card | Release-critical | One concept card with source-faithful synthesis, provenance, and no claim split unless needed. |
| claim-backed card | Release-critical | A concept card with claims, source support, source span references, evidence grade, extraction confidence, verification state, validation result, reconciliation state, and memory admission shown as distinct concerns. |
| CQ coverage | Release-critical | A competency question/CQ example showing requirement role, coverage target, answerability, covered card/claim/edge, and verification target without implying memory admission. |
| relationship/edge | Release-critical | Relationship vocabulary and an edge example where direction or symmetry, source support, evidence grade, extraction run, verification, reconciliation, and memory-admission implication attach to the relationship. |
| extraction-run trace | Release-critical | Extraction-run trace with source snapshot, prompt or method version, agent scope, generated/updated cards, old-card inputs, validation result, reconciliation result, and downstream memory-admission implication. |
| reconciliation | Release-critical | Reconciliation result for duplicate concept, competing definition, slug drift, taxonomy drift, relationship asymmetry, CQ coverage conflict, parallel-worker conflict, or preservation conflict. |
| memory-admission | Release-critical | Memory-admission decision showing source support, evidence grade, verification state, validation result, reconciliation state, preservation disposition, and operator acceptance when required. |
| parallel-worker default recipe | Release-critical | A five-agent default recipe example that states five-agent is not an invariant and records actual parallel-worker provenance in the extraction run. |

## Optional or Later Examples

| Example | Status | Later owner |
|---------|--------|-------------|
| Multi-source source span comparison | Optional or later | Slice05 can preserve as an unresolved example expansion; Arc05 can decide implementation planning and exact schema syntax. |
| Complex CQ retrieval probe | Optional or later | Slice04 and Slice05 should keep runtime services out of scope; later runtime work can decide graph database or memory runtime behavior. |
| Package README walkthrough | Optional or later | Slice04 owns README integration, package behavior, package inclusion, and discoverability. |
| Validator failure corpus | Optional or later | Slice04 owns validation determinism and validation candidate selection; Arc05 owns validator-code and tests. |
| Release artifact smoke example | Optional or later | Arc05 owns generated zips, release mechanics, Makefile changes, source edit work, and package updates. |

## Example Design Rules

- Every release-critical example should show whether it is a user-authored
  surface, trace record, or result record.
- Examples must not collapse concept card, claim, source support, source span,
  evidence grade, extraction confidence, verification state, validation
  result, reconciliation state, extraction run, competency question, CQ, and
  memory admission into one confidence field.
- Examples should show problem ownership and dependency direction: this skill
  owns concept-card method representation, while adjacent guidance owns
  collaboration-framework project management, source reading, domain knowledge,
  implementation planning, and source edits.
- Five-agent examples should present the five-agent workflow as a default
  recipe, not an invariant. The example must require extraction-run and
  parallel-worker provenance for the actual workflow used.
- Examples should route unresolved validation, package, README, Makefile,
  source edit, schema syntax, enum spelling, generated zips, release mechanics,
  and implementation planning choices to later owners.

## Later Owner Routing

| Later owner | Routed question |
|-------------|-----------------|
| Slice04 | validation determinism, validation candidate selection, package behavior, package inclusion, README integration, discoverability, and maintenance ownership for examples. |
| Slice05 | Architecture synthesis, first-release example set confirmation, optional-example disposition, and Arc05 handoff. |
| Arc05 | implementation planning for source edit work, exact example files, schema syntax, enum spelling, Makefile changes, README changes, validator-code, generated zips, release mechanics, tests, and package updates. |

## Out of Scope

Out of scope for this slice: validation candidate selection, package
inclusion, README integration, Makefile changes, validator-code, deterministic
validation scripts, generated zips, released skill bundles, released skill
mechanics, source checkout edits, schema syntax, enum spelling, graph database
design, memory runtime design, CCDP service design, live extraction behavior,
runtime services, exact example files in the source checkout, and source
implementation.
