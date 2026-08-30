# Functional Analysis Method

```yaml
project: project02-collab-breakout
arc: arc03-functional-analysis
slice: slice01-usage-surface-instrument
status: proposed-done
architecture-decisions: none
method-status: analytical, non-final, not accepted architecture
```

## Evidence Basis

This method consumes the Arc02 closed/composed conceptual analysis:

- `../../arc02-conceptual-analysis/closing-report.md`
- `../../arc02-conceptual-analysis/slice03-ontology-decision-synthesis/artifacts/arc02-conceptual-model.md`
- `../../arc02-conceptual-analysis/slice03-ontology-decision-synthesis/artifacts/boundary-and-naming-findings.md`
- `../../arc02-conceptual-analysis/slice03-ontology-decision-synthesis/artifacts/arc04-operator-decision-register.md`
- `../../arc02-conceptual-analysis/slice03-ontology-decision-synthesis/artifacts/arc02-close-readiness.md`

The conceptual model, boundary and naming findings, operator decision register,
and close-readiness assessment are inputs for functional analysis. They do not
decide architecture. Arc03 tests how those candidate concepts behave in real
usage surfaces before Arc04 and operator acceptance select any final breakout.

Project01 and `project01-harmonise-paths` remain source/package functional
test surfaces: package-local links, zip roots, release surface distinctions,
CCDP package separation, component contract fields, and `make
check-package-paths` are package/release gate inputs.

## Purpose

Arc03 asks how the current framework works for expected human and LLM users. It
turns Arc02 conceptual risks and Arc04 operator decisions into functional
questions that later slices can apply to the current monolith and to candidate
standalone or composed component scenarios.

This method does not decide final architecture. It defines the row vocabulary,
evidence grades, and scenario fields used by the later Arc03 slices.

## Vocabulary

- usage surface: a recognizable place where a human, LLM, maintainer, or
  package reader tries to use the framework.
- load path: the path from trigger to loaded material, including README,
  `SKILL.md`, package root, source document, prompt, template, or planning
  artifact.
- entrypoint: the first file, command, skill invocation, or package root the
  actor reaches.
- trigger: the event that causes the actor to load the framework, such as
  starting a substantial session, opening a slice, running an audit, or filing
  an upstream ticket.
- actor: the user of the surface, such as operator, CC, CDC, fresh LLM context,
  maintainer, source-clone reader, package reader, or release checker.
- minimum useful load set: the smallest set of documents or components that
  lets the actor complete the scenario without hidden dependencies.
- dependency order: the order in which the actor must load or understand
  prerequisites before the surface is safe to use.
- context cost: the attention or model-context budget consumed by the load set,
  including repeated summaries, duplicated rules, and support assets.
- routing friction: extra lookup, ambiguity, role translation, broken links, or
  unclear entrypoint choice that slows or misroutes the actor.
- functional deficiency: a missing, weak, over-broad, or misleading behavior
  that prevents the actor from completing the scenario as intended.
- source/package mode: whether the actor is using a source clone, generated
  skill zip, unzipped installed skill, planning worktree, or CCDP package.
- role-language clarity: whether CDC, CC, Claude, Codex, operator, and fresh
  context language is clear in the current surface.
- evidence grade: asserted, attested, reproduced, reconciled, or
  operator-accepted input, preserving the Arc02 evidence vocabulary.
- non-final architecture posture: every scenario result remains analytical and
  non-final; final architecture is deferred to Arc04 after Arc03 functional
  analysis and operator acceptance.

## Scenario Evaluation Fields

Later slices should evaluate each scenario with these fields:

| Field | Meaning |
|-------|---------|
| Scenario ID | Stable row identifier for cross-reference. |
| Actor | Who is using the surface. |
| Entrypoint | First file, command, skill, package root, or planning artifact reached. |
| Trigger | Why the actor starts this workflow. |
| Inputs | Required prior evidence, source files, package files, or planning artifacts. |
| Expected outcome | What the actor should be able to do after the minimum load. |
| Load set | Documents or candidate components actually needed. |
| Dependencies | Required load order or prerequisite concepts. |
| Friction signals | Context cost, routing friction, unclear handoff, broken source/package mode, or role-language clarity gaps. |
| Evidence to collect | Grep, source read, package inspection, walkthrough, or comparison needed. |
| Downstream owner | Slice02, Slice03, Slice04, Arc04, or Arc05 owner for the resulting finding. |

## Evaluation Rules

- Preserve Arc02 distinctions between candidate component, component family
  member, support asset, adapter, dependency edge, constraint, template,
  package/release gate, and non-component concept.
- Evaluate current-monolith behavior first, then compare standalone component
  and composed component scenarios.
- Treat source/package behavior as a functional surface, not only as release
  tooling.
- Record whether a surface is usable in direct source-clone reading, packaged
  skill reading, LLM skill loading, and planning-worktree modes.
- Keep role-language clarity explicit whenever a surface mentions CDC, CC,
  Claude, Codex, operator, verifier, reviewer, or fresh context.
- Record context cost qualitatively as low, medium, high, or unknown until a
  later slice collects measured or walkthrough evidence.
- Mark missing functional goals instead of turning gaps into architecture
  choices.
- Keep all outputs analytical and non-final; this method does not decide final
  breakout architecture.

## Evidence Grades

- asserted: scenario claim exists without a checked artifact or walkthrough.
- attested: CC supplies a source pointer, command output, or scenario row.
- reproduced: CDC or another independent pass repeats the check.
- reconciled: scenario evidence is also checked against broader source/package,
  release, or arc-level state.
- operator-accepted input: an operator decision or input accepted for analysis,
  not final architecture.

## Success And Failure Signals

Successful functional behavior means the actor can enter through the expected
entrypoint, load the minimum useful set in a coherent dependency order, preserve
source/package mode, understand role language, and complete the task without
unexpected context load or routing ambiguity.

Failure signals include excessive context cost, unclear handoff between
components, duplicated rules without ownership, hidden support asset
dependencies, source/package link ambiguity, role-language drift, missing
functional goal, and premature architecture claims.
