# Architecture Decision Method

```yaml
project: project02-collab-breakout
arc: arc04-breakout-architecture
slice: slice01-architecture-decision-instrument
status: proposed-done
method-status: decision-instrument
architecture-decisions: none
```

## Input Contract

This architecture decision method consumes the closed Arc02 conceptual model,
boundary and naming findings, operator decision register, Arc03 functional
model, scenario coverage, functional fit synthesis, architecture inputs, and
closing report. It defines how Arc04 will evaluate candidates without
accepting final architecture in this slice.

## Classification Vocabulary

Arc04 uses the following classification vocabulary:

- `candidate component`: a candidate with an owned problem, coherent purpose,
  credible reason-to-load, direct-load or composed-load value, named
  dependencies, and maintainable package/source behavior.
- `component family`: a coherent component with internal guides or subparts
  that should usually load through a wayfinder rather than as unrelated
  top-level components.
- `support asset`: a template, example, provenance note, checklist, or sample
  that travels with an owning component and is not useful enough alone to be a
  component.
- `adapter`: a routing or translation surface that lets humans or LLMs enter
  the right component, interpret role language, or cross source/package modes.
- `constraint`: a cross-cutting rule every affected component must obey.
- `package/release gate`: a checkable packaging, path, zip, README, SKILL.md,
  Makefile, CCDP, or validation requirement that governs release readiness.
- `dependency edge`: a directed relationship where one component must be
  loaded, cited, or understood before another component can be used safely.
- `non-component`: a real concept that belongs in the ontology but should not
  become a standalone component on current evidence.
- `deferred question`: an unresolved architecture or operator question that
  must be dispositioned before close or explicitly carried forward.

## Reason-To-Load Test

A candidate has a reason-to-load when Arc04 can answer yes to the following:

- Does a human or LLM have a natural trigger for loading this surface?
- Does it own a problem that would be harder to solve through another
  component?
- Does it reduce context cost compared with loading the full
  collaboration-framework composer?
- Does it avoid becoming over-thin by naming prerequisites and dependency
  edges?
- Does it have a minimum useful load that is smaller than the monolith and
  sufficient for the task?
- Can it be read in source-clone mode and packaged skill mode without broken
  package-local links or missing support assets?
- Does role-language remain clear for CC, CDC, Codex, Claude, and the human
  operator when loaded alone?

Failure on one question does not automatically reject the candidate. It marks
the candidate as adjust or defer until the failure is resolved or accepted by
the operator.

## Direct-Load Test

A candidate passes the direct-load test when it can be loaded without the
top-level composer and still gives the user enough to act correctly:

1. The entrypoint states the purpose and owned problem.
2. The in/out boundary is visible.
3. The dependency order is explicit.
4. Support assets and templates are linked package-locally.
5. Adapter notes cover source/package and role-language differences.
6. Release gates and validation commands are discoverable.
7. The component can name what it does not decide.

Strong direct-load candidates can proceed to contract evaluation with a go
posture. Plausible direct-load candidates proceed with adjust posture. Weak
direct-load candidates become dependency edges, support assets, adapters,
constraints, package/release gates, non-component concepts, or deferred
questions unless later evidence changes the classification.

## Distinction Rules

Component versus component family:

- A component has one primary load surface and one owned problem.
- A component family has one owned problem area but multiple internal guides
  that should be routed by a wayfinder.
- Project management currently fits component family better than a set of
  unrelated standalone components.

Component versus support asset:

- A support asset is incomplete without an owning discipline.
- `CONTRIBUTION-TICKET.md` supports contribution guidance; it should not be
  evaluated as a standalone component unless Arc04 records a new reason.

Component versus adapter:

- An adapter translates, routes, or orients. It does not own the full
  discipline.
- The top-level composer, repository orientation, PM wayfinder, and agent
  adapter are adapter surfaces unless later evidence proves component status.

Component versus constraint or package/release gate:

- A constraint applies across components and should become contract language.
- A package/release gate is checkable by a command or release checklist.
- Project01 source/package rules are gates and constraints, not standalone
  user-facing components.

Component versus non-component:

- Non-component does not mean irrelevant. It means the concept should be
  owned by another component, expressed as a dependency edge, or deferred as
  ontology rather than packaged as a standalone entrypoint.

## Evidence Grade Expectations

Arc04 uses the ledger evidence-grade vocabulary:

- `asserted`: a claim without evidence. Not valid for acceptance.
- `attested`: the doer reports evidence. Valid for proposed-done only.
- `reproduced`: CDC, a fresh context, or operator reruns or witnesses the
  evidence. Required before a slice or arc can claim closure.
- `reconciled`: reproduced evidence checked against broader repository,
  package, CI, or release state.

Contract evaluation should cite closed Arc02 and Arc03 evidence. New
architecture choices should record whether their support is conceptual,
functional, source-grounded, operator-accepted, or still only a low-weight
hypothesis.

## Go / Adjust / Defer Rubric

Use go / adjust / defer as follows:

- `go`: evidence supports contract evaluation with no known architecture
  blocker. Later slices still fill the component contract.
- `adjust`: evidence supports the candidate, but naming, boundary,
  dependency, adapter, source/package, support-asset, or release-gate issues
  must be fixed before acceptance.
- `defer`: evidence is insufficient for a component decision, the candidate
  is better modeled as a non-component category, or operator acceptance is
  needed before work can proceed.

No row may be accepted by enthusiasm. Every go or adjust disposition needs a
specific evidence basis and a named risk disposition.

## Operator Acceptance Rules

Operator acceptance is required for final Arc04 architecture. Before a choice
is accepted, Arc04 must show:

- the component name and owned problem;
- what is in boundary and out of boundary;
- dependencies, adapters, and support assets;
- source paths, package paths, package-local links, and zip root assumptions;
- Project01 package/release gate implications;
- risks, rejected alternatives, and deferred questions;
- Arc05 implementation-plan implications.

The operator-provided soft layout sketch is low-weight hypothesis evidence.
It can help seed options, but it cannot override closed Arc02/Arc03 evidence
or decide architecture by itself. Source edits remain out of scope until the
accepted architecture is translated into Arc05 implementation planning.
