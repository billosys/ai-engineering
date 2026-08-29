# Slice 02: Collaboration Framework Links

```yaml
project: project01-harmonise-paths
arc: arc02-skill-bundle-harmonisation
slice: slice02-collaboration-framework-links
status: open
opened-on: 2026-08-29
opened-by: CDC
implementation-checkout: /Users/oubiwann/lab/billosys/ai-engineering
planning-worktree: /Users/oubiwann/lab/billosys/ai-engineering/.worktrees/planning
artifact-home: /Users/oubiwann/lab/billosys/ai-engineering/.worktrees/planning/project01-harmonise-paths/arc02-skill-bundle-harmonisation/slice02-collaboration-framework-links/artifacts
depends-on:
  - arc02-skill-bundle-harmonisation/slice01-tooling-entrypoint-links
```

## Capability Statement

This slice harmonises package-path warnings in the collaboration-framework
bundle while preserving the framework's source-clone usefulness and planning
methodology meaning.

The goal is to remove high-confidence package-invalid framework references:
package-internal links that can be expressed with relative paths valid from
both source and bundle context, plus any narrow exception-file retirements or
staging transforms required by the evidence. The goal is not to rewrite the
methodology, rename canonical planning examples, or clear every remaining
framework warning regardless of semantics.

## Inputs

- `/Users/oubiwann/lab/billosys/ai-engineering/.worktrees/planning/project01-harmonise-paths/project-plan.md`
- `/Users/oubiwann/lab/billosys/ai-engineering/.worktrees/planning/project01-harmonise-paths/arc02-skill-bundle-harmonisation/arc-plan.md`
- `/Users/oubiwann/lab/billosys/ai-engineering/.worktrees/planning/project01-harmonise-paths/arc02-skill-bundle-harmonisation/ledger.md`
- `/Users/oubiwann/lab/billosys/ai-engineering/.worktrees/planning/project01-harmonise-paths/arc02-skill-bundle-harmonisation/slice01-tooling-entrypoint-links/cdc-verification.md`
- `/Users/oubiwann/lab/billosys/ai-engineering/Makefile`
- `/Users/oubiwann/lab/billosys/ai-engineering/scripts/check-package-paths`
- `/Users/oubiwann/lab/billosys/ai-engineering/package-path-exceptions.tsv`
- `/Users/oubiwann/lab/billosys/ai-engineering/SKILL.md`
- `/Users/oubiwann/lab/billosys/ai-engineering/docs/PROJECT-MANAGEMENT.md`
- `/Users/oubiwann/lab/billosys/ai-engineering/docs/AI-ENGINEERING-METHODOLOGY.md`
- `/Users/oubiwann/lab/billosys/ai-engineering/docs/CODE-AUDIT.md`
- `/Users/oubiwann/lab/billosys/ai-engineering/docs/pm/`
- `/Users/oubiwann/lab/billosys/ai-engineering/templates/LEDGER-DISCIPLINE.md`

## Artifact Home

Durable slice-produced evidence belongs here:

`/Users/oubiwann/lab/billosys/ai-engineering/.worktrees/planning/project01-harmonise-paths/arc02-skill-bundle-harmonisation/slice02-collaboration-framework-links/artifacts/`

Expected artifacts include the collaboration-framework warning baseline,
targeted warning inventories before and after changes, package gate
transcripts, compatibility check transcripts, and implementation scope
evidence.

## Scope

In scope:

- establish a baseline warning inventory for the generated
  `collaboration-framework.zip` package;
- classify framework warnings by policy class: package-internal bundled
  reference, source-clone reference, repo-only/provenance, example-project
  path, explicit exception, or checker false positive;
- edit framework entrypoint/docs/templates where a relative path spelling is
  valid in both source and generated package context;
- use a narrow Make/script staging transform only if the baseline proves a
  source-root spelling must remain in source but package differently;
- update `package-path-exceptions.tsv` to retire resolved transitional
  framework rows or add explicit exceptions only for intentional non-bundled
  references;
- keep durable evidence in this slice's `artifacts/` directory;
- update the slice ledger and close report.

High-confidence initial targets from the Slice 01 post-change gate include:

- `docs/pm/06-confirmation-protocol.md` references to
  `docs/PROJECT-MANAGEMENT.md` from a packaged `docs/pm/` file;
- `docs/pm/version-history.md` references to `docs/PROJECT-MANAGEMENT.md`
  from a packaged `docs/pm/` file;
- `docs/AI-ENGINEERING-METHODOLOGY.md` references to package root
  `SKILL.md` from a packaged `docs/` file;
- source-clone-only framework references such as `README.md`,
  `knowledge/rust/guides/11-anti-patterns.md`, `./knowledge/`, and
  `./dev/concept-cards/...`, which must be either made package-valid,
  explicitly marked as source-clone/provenance, or left as warnings with a
  documented rationale.

Out of scope:

- substantive edits to the collaboration-framework methodology or posture;
- changing the project-management spec except for path-reference wording
  needed to preserve source/package correctness;
- mature language guide prose changes;
- non-framework skill bundle harmonisation;
- CCDP package work;
- package layout expansion unless the close report proves it is the smallest
  correct fix and the operator accepts it;
- URL liveness checks.

## Verification Approach

The close set must show:

- baseline collaboration-framework warning inventory before edits;
- post-change collaboration-framework warning inventory;
- targeted framework warning reduction or explicit policy disposition;
- `make check-package-paths` exits 0 with no new hard failures;
- `scripts/check-package-paths --check-exceptions-only` passes;
- `make check-skills` passes;
- `make all` passes;
- implementation diff scope stays within framework docs/templates/entrypoint,
  `package-path-exceptions.tsv`, and any justified Make/script staging
  transform;
- durable artifacts are under this slice's `artifacts/` directory.

## Close Conditions

This slice closes when collaboration-framework package-path warnings have a
measurable burn-down or explicit policy disposition, all package and
compatibility checks pass, every ledger row has attested evidence, durable
evidence artifacts live under `artifacts/`, and the close report walks every
row with Bubble-up to Arc 02.
