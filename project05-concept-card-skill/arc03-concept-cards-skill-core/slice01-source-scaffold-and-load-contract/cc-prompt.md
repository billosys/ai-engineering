# CC Prompt: Arc03 Slice01 Source Scaffold And Load Contract

You are CC implementing Project05 Arc03 Slice01 in the ai-engineering source
checkout. This slice is implementation work, not planning-only work.

## Start Here

Read, in this order:

1. `/Users/oubiwann/lab/billosys/ai-engineering/AGENTS.md`
2. `/Users/oubiwann/lab/billosys/ai-engineering/.worktrees/planning/project05-concept-card-skill/project-plan.md`
3. `/Users/oubiwann/lab/billosys/ai-engineering/.worktrees/planning/project05-concept-card-skill/arc03-concept-cards-skill-core/arc-plan.md`
4. `/Users/oubiwann/lab/billosys/ai-engineering/.worktrees/planning/project05-concept-card-skill/arc03-concept-cards-skill-core/ledger.md`
5. `/Users/oubiwann/lab/billosys/ai-engineering/.worktrees/planning/project05-concept-card-skill/arc03-concept-cards-skill-core/slice01-source-scaffold-and-load-contract/slice-plan.md`
6. `/Users/oubiwann/lab/billosys/ai-engineering/.worktrees/planning/project05-concept-card-skill/arc03-concept-cards-skill-core/slice01-source-scaffold-and-load-contract/ledger.md`
7. `/Users/oubiwann/lab/billosys/ai-engineering/.worktrees/planning/project05-concept-card-skill/arc02-document-extraction-skill/closing-report.md`

Also inspect Project03 evidence as needed under:

- `/Users/oubiwann/lab/billosys/ai-engineering/.worktrees/planning/project05-concept-card-skill/artifacts/project03-concept-card-method/closing-report.md`
- `/Users/oubiwann/lab/billosys/ai-engineering/.worktrees/planning/project05-concept-card-skill/artifacts/project03-concept-card-method/arc03-conceptual-model/slice04-model-synthesis/artifacts/`
- `/Users/oubiwann/lab/billosys/ai-engineering/.worktrees/planning/project05-concept-card-skill/artifacts/project03-concept-card-method/arc04-skill-architecture/slice05-architecture-synthesis/artifacts/`
- `/Users/oubiwann/lab/billosys/ai-engineering/.worktrees/planning/project05-concept-card-skill/artifacts/project03-concept-card-method/arc05-implementation-plan/slice05-implementation-plan-synthesis/artifacts/`

Translate historical `concept-card-method` paths and under-`guides` support
layout through the current Project05 decisions: the live source root is
`knowledge/concept-cards/`, and support directories later belong as siblings
unless a current package contract explicitly says otherwise.

## Implementation Scope

Create exactly the initial source scaffold:

- `knowledge/concept-cards/SKILL.md`
- `knowledge/concept-cards/version-history.md`
- `knowledge/concept-cards/guides/01-load-contract.md`
- `knowledge/concept-cards/guides/02-operator-workflow.md`

Use `metadata.version: "1.0.0"` under the current source version contract.
Keep the changelog in sibling `version-history.md`; do not create guide-local
version histories or duplicate current-version prose.

## Required Content

The scaffold must:

- use `name: concept-cards`;
- define positive load cases for concept-card creation, extraction,
  re-extraction, validation, reconciliation, preservation, relationship/CQ
  work, and memory admission;
- define negative load cases for generic document extraction, source cleanup,
  ordinary source reading, generic ontology/database/runtime work, and package
  planning that belongs elsewhere;
- route raw PDF/EPUB/HTML and converted-source cleanup to
  `document-extraction`;
- treat `document-extraction` prepared outputs as upstream provenance, not as
  concept-card source support by themselves;
- preserve Project03 v4.0 distinctions among concept card, claim, source
  support, source span/source locator, relationship edge, competency question,
  extraction run, validation result, verification result, reconciliation
  result, preservation decision, and memory admission;
- keep evidence grade, extraction confidence, validation result, verification
  state/result, reconciliation state/result, and memory admission distinct;
- identify later guides 03 through 10 and Arc04/Arc05 support/package work as
  future, not implemented.

## Scope Boundaries

Do not add templates, examples, validation/reference support directories, or
schema files. Arc04 owns those.

Do not add package, Makefile, README, docs, generated zip, or install wiring.
Arc05 owns those.

Do not implement executable validators, runtime services, graph databases,
ontology databases, GraphRAG, CCDP services, or memory runtime automation.

Do not recreate `knowledge/concept-card-method/` or `knowledge/source-preparation/`.

## Verification

Before editing, inspect source status and preserve unrelated work. Use explicit
paths when staging and committing.

Run the ledger checks in
`slice01-source-scaffold-and-load-contract/ledger.md`, including:

```text
scripts/check-skill-description.sh knowledge/concept-cards/SKILL.md
python3 /Users/oubiwann/.codex/skills/.system/skill-creator/scripts/quick_validate.py knowledge/concept-cards
git diff --check
make check-skills
make check-skill-versions
```

Only run package path checks if you change package surfaces.

Commit only the source changes for this slice in the source checkout, using
explicit path names. Include the required co-author trailers:

```text
Co-authored-by: Codex <noreply@openai.com>
Co-authored-by: Billo AI <ai-engineering@billo.systems>
```

Then update only this slice's planning ledger and add `closing-report.md` in
the planning worktree. Do not write `cdc-verification.md`; CDC writes that
after independent reproduction.
