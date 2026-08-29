# Slice 04: Warning Policy Tightening

```yaml
project: project01-harmonise-paths
arc: arc02-skill-bundle-harmonisation
slice: slice04-warning-policy-tightening
status: open
opened-on: 2026-08-29
opened-by: CDC
implementation-checkout: /Users/oubiwann/lab/billosys/ai-engineering
planning-worktree: /Users/oubiwann/lab/billosys/ai-engineering/.worktrees/planning
artifact-home: /Users/oubiwann/lab/billosys/ai-engineering/.worktrees/planning/project01-harmonise-paths/arc02-skill-bundle-harmonisation/slice04-warning-policy-tightening/artifacts
depends-on:
  - arc02-skill-bundle-harmonisation/slice03-mature-entrypoint-staging-transforms
```

## Capability Statement

This slice tightens Arc 02's remaining package-path warning policy after the
entrypoint warning classes have been burned down. It does not need to make the
package-path warning count zero; it needs to make the remaining warning surface
honest, intentional, and actionable.

The expected result is a clean policy boundary:

- resolved transitional exception rows are retired;
- truly intentional source/provenance, source-clone, example-project, and
  parser-false-positive rows are explicitly documented;
- unresolved real package usability issues remain visible as later-arc work,
  with concrete backlog notes instead of broad allowlists.

## Inputs

- `/Users/oubiwann/lab/billosys/ai-engineering/.worktrees/planning/project01-harmonise-paths/project-plan.md`
- `/Users/oubiwann/lab/billosys/ai-engineering/.worktrees/planning/project01-harmonise-paths/arc02-skill-bundle-harmonisation/arc-plan.md`
- `/Users/oubiwann/lab/billosys/ai-engineering/.worktrees/planning/project01-harmonise-paths/arc02-skill-bundle-harmonisation/ledger.md`
- `/Users/oubiwann/lab/billosys/ai-engineering/.worktrees/planning/project01-harmonise-paths/arc02-skill-bundle-harmonisation/slice03-mature-entrypoint-staging-transforms/cdc-verification.md`
- `/Users/oubiwann/lab/billosys/ai-engineering/scripts/check-package-paths`
- `/Users/oubiwann/lab/billosys/ai-engineering/package-path-exceptions.tsv`
- generated package-path output from `make check-package-paths`

## Artifact Home

Durable slice-produced evidence belongs here:

`/Users/oubiwann/lab/billosys/ai-engineering/.worktrees/planning/project01-harmonise-paths/arc02-skill-bundle-harmonisation/slice04-warning-policy-tightening/artifacts/`

Expected artifacts include the post-Slice-03 warning baseline, policy
classification, exception diff notes, package-path transcripts, compatibility
check transcripts, implementation scope evidence, and later-arc backlog notes.

## Scope

In scope:

- establish a current generated-package warning baseline from
  `make check-package-paths`;
- classify all remaining warning classes after Slice 03, starting from the CDC
  reproduced totals:
  - 89 `bundled-reference` rows;
  - 146 `repo-only/provenance` rows;
  - 26 `source-clone-reference` rows;
  - 25 `example-project path` rows;
  - 9 parser false positives;
- inspect the five transitional rows currently expiring `after-arc02` in
  `package-path-exceptions.tsv`;
- retire any transitional rows that are obsolete;
- promote intentionally permanent policy rows to explicit exceptions with
  specific package/document/target patterns and reasons;
- produce a later-arc backlog for real package usability issues that should
  stay visible rather than become permanent exceptions;
- run package and compatibility gates;
- update this slice's ledger and close report.

Likely policy decisions to make:

- Rust guide-internal `09-common-pitfalls.md` references: decide whether they
  should be fixed now, deferred to later language-pack maintenance, or marked
  as intentionally unbundled.
- C++ `param-passing-*.png` references: decide whether missing images imply a
  later package-layout/assets slice or an explicit non-bundled/provenance
  exception.
- JavaScript/Deno guide-internal cross-guide rows: decide whether these are
  package-path spelling issues suitable for a later source/staging slice, or
  intentional current-document-relative examples.
- Non-bundled source/provenance, source-clone, example-project, and parser
  false-positive rows: decide which deserve durable explicit exceptions and
  which should remain warnings until a later arc.

Out of scope:

- broad mature guide prose rewriting;
- moving mature language-pack guide directory trees;
- adding CCDP package targets;
- changing package checker architecture beyond small policy/reporting fixes
  required by this slice;
- URL liveness checks;
- collaboration-framework methodology changes unrelated to package warning
  policy;
- closing Arc 02 before CDC verifies this slice.

## Verification Approach

The close set must show:

- current warning baseline derived from generated zips;
- complete classification of remaining warning classes;
- explicit disposition for every transitional exception row;
- no broad package/document wildcard exception that hides unresolved work;
- `package-path-exceptions.tsv` schema validation passes;
- `make check-package-paths` exits 0 with no new hard failures;
- warning count either decreases or the remaining count is explained by
  explicit policy/backlog disposition;
- `make check-skills` passes;
- `make all` passes;
- implementation diff scope stays within exception policy, small checker
  policy/reporting changes if justified, and any tiny source/package fix
  explicitly approved by this slice;
- durable artifacts live under this slice's `artifacts/` directory.

## Close Conditions

This slice closes when the post-Slice-03 warning surface has an explicit,
auditable policy disposition; transitional rows are retired or converted; real
later work remains visible; all package and compatibility gates pass; every
ledger row has attested evidence; durable evidence artifacts live under
`artifacts/`; and the close report walks every row with Bubble-up to Arc 02.
