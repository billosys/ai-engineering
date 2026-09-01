# Project02 Conceptual Boundary Aid

```yaml
project: project03-concept-card-method
arc: arc01-method-positioning
slice: slice01-project02-boundary-aid
status: proposed-done
consumer: project02-collab-breakout:arc02-conceptual-analysis
architecture-decisions: none
```

## Purpose

This aid gives Project02 Arc02 a concept-card-method lens for deciding
collaboration-framework component boundaries. It is non-final and does not
decide Project02 architecture.

Use it as a sharper question set when Arc02 evaluates whether a Project02 label
is a component, support asset, adapter, dependency edge, constraint, template,
or package/release gate.

## Source Basis

Project02 already identified the right component-selection axes:

- reason to load;
- problem ownership;
- dependency direction;
- package behavior;
- maintenance ownership.

The v3.2 baseline concept-card method contributes a complementary ontology
lens:

- one concept per card;
- source-faithful extraction;
- explicit relationships;
- confidence as information;
- sacred provenance;
- competency questions as both requirements and coverage checks;
- re-extraction with preservation of unique prior value.

Project03 now targets v4.0 rather than v3.3. That major-version framing matters
because the expected changes are architectural: evidence grading,
verification/reconciliation, memory admission, graph relationships, and CCDP
compatibility should become first-class method concepts rather than appended
cleanup notes.

## Boundary Heuristics for Project02 Arc02

### 1. Concept is not automatically component

A concept names something that should be understood atomically. A component is
something with a distinct reason to load and a useful standalone contract.

Arc02 question: If this label had a perfect concept card, would a user still
need to load it as a standalone skill? If not, it is likely a support concept
inside another component.

### 2. Component requires a competency question set

A component should answer a cluster of user or LLM competency questions on its
own. One isolated question usually points to a guide section or support asset,
not a full component.

Arc02 question: What questions does this component let a fresh session answer
that the top-level composer should not have to answer directly?

### 3. Support assets travel with the owner of the rule

Examples, templates, version histories, and provenance files are valuable, but
they are usually memory supports rather than independent load targets.

Arc02 question: Which component owns the rule that this asset clarifies,
instantiates, or preserves?

### 4. Adapter is a surface, not a discipline

An adapter translates between users, tools, source checkout, packaged zip,
Codex, Claude, or future surfaces. It may deserve a guide, but it is not a
domain discipline unless it owns a problem beyond translation.

Arc02 question: Does this material teach a reusable practice, or does it route
the reader to the practice?

### 5. Constraint is not user-facing unless users act on it directly

Project01 path/package rules are hard gates, but they should not become
components merely because every component must obey them.

Arc02 question: Is this label something a user loads to do work, or a rule
implementation slices must satisfy?

### 6. Claim and evidence must stay separate

Project02 candidate labels are claims about possible components. Evidence is
the source-backed reason to believe the claim is valid. Do not let a tidy label
become accepted architecture before its evidence is checked.

Arc02 question: What source, problem, load moment, and package fact supports
this boundary?

### 7. Relationship type matters

Use different edges for different truths:

- prerequisite: must be loaded or understood first;
- extends: specializes a more general discipline;
- uses: calls on another component in a workflow;
- supports: supplies a template, example, or provenance note;
- constrains: imposes a release, path, evidence, or package gate;
- contrasts-with: helps avoid a likely confusion.

Arc02 question: Are two labels merged because they share an edge, or because
they truly share ownership?

### 8. Memory admission is stricter than extraction

A generated component proposal is not yet durable substrate. To enter the
framework as memory, it needs source evidence, explicit relationships,
coverage against competency questions, and verification.

Arc02 question: What evidence grade does this candidate have now: asserted,
attested, reproduced, reconciled, or operator-accepted?

## Recommended Arc02 Artifact

Project02 Arc02 should create a `component-boundary-ledger.md` or equivalent
artifact with one row per candidate component. Each row should include:

- candidate label;
- proposed classification;
- competency questions answered;
- source evidence;
- problem ownership;
- reason to load;
- dependency edges;
- support assets;
- package/release constraints;
- evidence grade;
- decision owner;
- disposition.

This artifact should remain analytical until operator acceptance. It should
not replace Project02's normal arc ledger; it is a conceptual-analysis aid.

## Likely Project02 Implications

- `ledger-verification-protocol` looks like a strong component because it owns
  clear competency questions and a distinct evidence problem.
- `project-management-*` looks like a component family or one wayfinder with
  focused guides, because the sublabels have distinct load moments but share a
  lifecycle contract.
- `contribution-ticket-template` looks like a support asset unless Arc02 finds
  standalone competency questions that justify loading it without contribution
  style.
- `path-contract-constraints` should stay a constraint and package/release
  gate, not a component.
- `agent-adapter-and-routing` should be tested as an adapter before it is
  promoted to component.
- `engineering-methodology-and-process` may need to split substrate/method,
  verification, and process only where the competency questions and load
  moments separate cleanly.

## Relation to Project03

Project03 should later turn this aid into a v4.0 concept-card method skill.
That future skill may supply templates and validation scripts for this kind of
analysis, but Project02 does not need to wait for the full skill before Arc02
can proceed. It only needs this small boundary aid and operator acceptance of
the soft dependency.
