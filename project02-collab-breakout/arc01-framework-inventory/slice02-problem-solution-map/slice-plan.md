# Slice 02: Problem-Solution Map

```yaml
project: project02-collab-breakout
arc: arc01-framework-inventory
slice: slice02-problem-solution-map
status: proposed-done
proposed-done-on: 2026-08-29
artifact-home: artifacts/
depends-on:
  - slice01-source-inventory:verified-closed
blocks:
  - slice03-arc01-synthesis
related:
  - ../slice01-source-inventory/cdc-verification.md
  - ../slice01-source-inventory/artifacts/framework-source-inventory.md
  - ../slice01-source-inventory/artifacts/source-to-concept-map.md
  - ../slice01-source-inventory/artifacts/project01-path-contract-notes.md
  - /Users/oubiwann/lab/billosys/ai-engineering/SKILL.md
  - /Users/oubiwann/lab/billosys/ai-engineering/docs
  - /Users/oubiwann/lab/billosys/ai-engineering/templates
```

## Goal

Convert the verified Slice 01 source inventory into a historical and functional
problem-to-solution map for the current collaboration framework.

For each major failure mode the framework appears designed to address, identify
the current mechanism or mechanisms that address it, the source evidence for
those mechanisms, the candidate breakout labels involved, and the quality of
the fit. The output should make later conceptual analysis more honest by
separating "this mechanism exists" from "this mechanism is the right component
boundary."

## Scope

In scope:

- Consume the verified Slice 01 close evidence and artifacts as the starting
  evidence base.
- Inspect current source framework files read-only where needed to clarify a
  mechanism or failure mode.
- Produce durable analysis artifacts under `artifacts/`.
- Map historical/user-stated problems, LLM failure modes, collaboration
  problems, SDLC/process problems, verification problems, planning-path
  problems, package/release-surface problems, and maintainability problems to
  the mechanisms that address them.
- Identify suspected underfit, overfit, overlap, duplication, mislabeling,
  improper merges, improper splits, and missing solution areas.
- Record open questions for Slice 03, Arc 02, and operator discussion.

Out of scope:

- Deciding final component boundaries.
- Editing source `SKILL.md`, `README.md`, framework docs, templates, Makefiles,
  package scripts, generated zips, or package exceptions.
- Opening or closing Arc 02.
- Treating current file boundaries or Slice 01 candidate labels as accepted
  component boundaries.

## Required Artifacts

Produce these durable artifacts under `artifacts/`:

- `problem-solution-map.md` - source-backed map from failure modes/problems to
  current framework mechanisms and fit assessments.
- `mechanism-coverage-matrix.md` - matrix showing which current mechanisms and
  candidate labels cover which problem classes, including primary and
  secondary coverage.
- `problem-solution-findings.md` - critical findings: overlaps, duplicated
  solutions, weak fits, missing solution areas, mislabel candidates, and open
  questions.

## Verification Approach

The slice verifies by checking that the durable artifacts exist in the standard
artifact home, that the required problem classes and current mechanism labels
are represented, that source evidence is cited from actual files or Slice 01
artifacts, and that critical findings do not collapse into final architecture
decisions.

## Exit Criteria

- Slice 01 verified-close evidence is consumed and cited.
- `artifacts/problem-solution-map.md` covers all required problem classes with
  mechanism mappings, source evidence, fit assessment, and open questions where
  needed.
- `artifacts/mechanism-coverage-matrix.md` covers every non-final candidate
  label from Slice 01 and shows primary/secondary problem coverage.
- `artifacts/problem-solution-findings.md` names suspected overlap,
  duplication, underfit, overfit, mislabeling, improper merge/split candidates,
  missing solution areas, and operator questions.
- Project01 source/package path constraints are included as functional release
  surface constraints.
- No source files are edited.
