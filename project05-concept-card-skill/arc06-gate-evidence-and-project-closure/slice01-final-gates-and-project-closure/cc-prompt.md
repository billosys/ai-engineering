# CC Prompt: Arc06 Slice01 Final Gates And Project Closure

You are CC implementing Project05 Arc06 Slice01 in Expedited Mode.

## Required Reading

Read these first:

- `project05-concept-card-skill/project-plan.md`
- `project05-concept-card-skill/ledger.md`
- `project05-concept-card-skill/arc01-readiness-and-scope-lock/closing-report.md`
- `project05-concept-card-skill/arc02-document-extraction-skill/closing-report.md`
- `project05-concept-card-skill/arc03-concept-cards-skill-core/closing-report.md`
- `project05-concept-card-skill/arc04-concept-card-records-and-examples/closing-report.md`
- `project05-concept-card-skill/arc05-packaging-docs-and-installability/closing-report.md`
- `project05-concept-card-skill/arc05-packaging-docs-and-installability/slice03-package-validation-and-install-smoke/cdc-verification.md`
- `project05-concept-card-skill/arc06-gate-evidence-and-project-closure/arc-plan.md`
- `project05-concept-card-skill/arc06-gate-evidence-and-project-closure/ledger.md`
- `project05-concept-card-skill/arc06-gate-evidence-and-project-closure/slice01-final-gates-and-project-closure/slice-plan.md`
- `project05-concept-card-skill/arc06-gate-evidence-and-project-closure/slice01-final-gates-and-project-closure/ledger.md`

## Task

Run the final Project05 closure pass. Reproduce the current repository-local
gate evidence, inspect the current generated packages, reconcile the project
ledger, and write proposed Project05 closure artifacts.

At minimum:

- run `make check-skills`;
- run `make check-skill-versions`;
- run `make check-package-paths`;
- run `make all`;
- run `make -s print-skill-zips` and confirm both
  `target/skills/document-extraction.zip` and
  `target/skills/concept-cards.zip`;
- inspect both generated zips for the documented support shape, including
  `concept-cards/references/`;
- perform targeted stale-name and runtime-overclaim scans;
- reconcile project ledger rows P-2 through P-8 with reproduced evidence,
  explicit deferrals, or explicit no-op decisions;
- write a final Project05 closing report or proposed closure report at the
  project root that records delivered capabilities, final gates, accepted
  warnings, operational incidents, explicit deferrals/no-ops, and future work.

Do not defer the nondeferrable objectives: live installable
`document-extraction` and `concept-cards`. If a final check finds a defect,
fix it narrowly and rerun the affected checks before proposing closure.

## Out Of Scope

Do not redesign the delivered skills or add new skills unless the operator
explicitly expands Project05. Do not add executable validators, JSON Schema,
runtime services, graph/ontology databases, GraphRAG integration, CCDP
services, live-corpus extraction, memory runtime work, CI expansion, release
publishing, `knowledge/concept-card-method/`, or
`knowledge/source-preparation/`.

## Required Validation

Run and record:

- `make check-skills`;
- `make check-skill-versions`;
- `make check-package-paths`;
- `make all`;
- `make -s print-skill-zips`;
- direct archive inspection for the two Project05 generated packages;
- targeted stale-name and runtime-overclaim scans;
- `git diff --check`;
- source and planning `git status --short --untracked-files=all`.

## Commit Discipline

Before committing, inspect `git status --short --untracked-files=all`. Commit
only intended source files with explicit pathspecs. Do not commit generated
`target/`, `build/`, or temporary install artifacts.

Use the required trailers:

```text
Co-authored-by: Codex <noreply@openai.com>
Co-authored-by: Billo AI <ai-engineering@billo.systems>
```

After any source commit, update the project ledger, Arc06 ledger, Slice01
ledger, and closure artifacts, then commit only those planning files with
explicit pathspecs. Mark the slice and project closure as CC proposed-done
pending CDC verification. Do not write `cdc-verification.md`.
