# CC Prompt: Arc03 Slice03 Evidence, Validation, And Verification

You are CC implementing Project05 Arc03 Slice03 in the ai-engineering source
checkout. This slice is implementation work, not planning-only work.

## Start Here

Read, in this order:

1. `/Users/oubiwann/lab/billosys/ai-engineering/AGENTS.md`
2. `/Users/oubiwann/lab/billosys/ai-engineering/.worktrees/planning/project05-concept-card-skill/project-plan.md`
3. `/Users/oubiwann/lab/billosys/ai-engineering/.worktrees/planning/project05-concept-card-skill/arc03-concept-cards-skill-core/arc-plan.md`
4. `/Users/oubiwann/lab/billosys/ai-engineering/.worktrees/planning/project05-concept-card-skill/arc03-concept-cards-skill-core/ledger.md`
5. `/Users/oubiwann/lab/billosys/ai-engineering/.worktrees/planning/project05-concept-card-skill/arc03-concept-cards-skill-core/slice03-evidence-validation-verification/slice-plan.md`
6. `/Users/oubiwann/lab/billosys/ai-engineering/.worktrees/planning/project05-concept-card-skill/arc03-concept-cards-skill-core/slice03-evidence-validation-verification/ledger.md`
7. `/Users/oubiwann/lab/billosys/ai-engineering/.worktrees/planning/project05-concept-card-skill/arc03-concept-cards-skill-core/slice02-extraction-reextraction-provenance/cdc-verification.md`
8. `/Users/oubiwann/lab/billosys/ai-engineering/knowledge/concept-cards/SKILL.md`
9. `/Users/oubiwann/lab/billosys/ai-engineering/knowledge/concept-cards/guides/01-load-contract.md`
10. `/Users/oubiwann/lab/billosys/ai-engineering/knowledge/concept-cards/guides/02-operator-workflow.md`
11. `/Users/oubiwann/lab/billosys/ai-engineering/knowledge/concept-cards/guides/03-extraction.md`
12. `/Users/oubiwann/lab/billosys/ai-engineering/knowledge/concept-cards/guides/04-re-extraction-preservation.md`

Also inspect Project03 evidence as needed under:

- `/Users/oubiwann/lab/billosys/ai-engineering/.worktrees/planning/project05-concept-card-skill/artifacts/project03-concept-card-method/arc03-conceptual-model/slice04-model-synthesis/artifacts/v40-conceptual-model.md`
- `/Users/oubiwann/lab/billosys/ai-engineering/.worktrees/planning/project05-concept-card-skill/artifacts/project03-concept-card-method/arc04-skill-architecture/slice05-architecture-synthesis/artifacts/v40-skill-architecture.md`
- `/Users/oubiwann/lab/billosys/ai-engineering/.worktrees/planning/project05-concept-card-skill/artifacts/project03-concept-card-method/arc05-implementation-plan/slice05-implementation-plan-synthesis/artifacts/v40-source-edit-sequence.md`

Translate historical `concept-card-method` paths through the current live
source root `knowledge/concept-cards/`.

## Implementation Scope

Implement exactly this source-skill slice:

- add `knowledge/concept-cards/guides/05-evidence-lifecycle.md`;
- add `knowledge/concept-cards/guides/08-validation-verification.md`;
- update `knowledge/concept-cards/SKILL.md`;
- update `knowledge/concept-cards/version-history.md`;
- update `knowledge/concept-cards/guides/01-load-contract.md`,
  `knowledge/concept-cards/guides/02-operator-workflow.md`,
  `knowledge/concept-cards/guides/03-extraction.md`, and
  `knowledge/concept-cards/guides/04-re-extraction-preservation.md` only as
  needed to make live-route wording accurate.

Advance `metadata.version` to `"1.2.0"` and add a sibling
`version-history.md` entry. Do not create guide-local version histories.

## Required Content

Guide 05 must provide detailed evidence lifecycle instructions:

- define source support and source span as support attachments/selected source
  material, not bibliography or prepared-source provenance;
- define evidence grade as warrant on a claim or claim-source support
  relationship, with explicit rationale and scope;
- define extraction confidence as a signal about the extraction act, distinct
  from source support, evidence grade, validation, verification,
  reconciliation, preservation, and memory admission;
- explain where these signals attach: card, claim, support relationship, edge,
  CQ coverage assertion, or extraction run;
- describe how to record insufficient, partial, conflicting, and unassessed
  evidence without upgrading it;
- preserve validation result, verification state/result, reconciliation
  state/result, preservation decision, and memory admission as separate
  lifecycle concerns;
- include human-assisted and agent-direct operation notes;
- report handoff output and remaining work.

Guide 08 must provide detailed validation and verification instructions:

- define structural validation and validation-result scope;
- define semantic verification and verification-result/state scope;
- separate validation from verification, reconciliation, and memory admission;
- identify review actors and evidence provenance: same-context assistant
  checks, independent CDC/fresh-context checks, operator-reported observations,
  human review, tool/process checks, and unavailable evidence;
- record actor, method, target, evidence, scope, outcome, caveats, and revision
  identity for each result;
- prevent false upgrades from one claim to a whole card, from successful
  extraction to verification, from validation to admission, and from worker
  agreement to independent verification;
- include human-assisted and agent-direct operation notes;
- report handoff output and remaining work.

Also clean the Slice02 caller wording:

- guide 01 must no longer say routes 03 through 10 are all future;
- guide 02 must no longer say detailed extraction or re-extraction/
  preservation procedures are future/unavailable;
- guides 03/04 should point to guides 05 and 08 as live where relevant after
  this slice lands;
- `SKILL.md` should identify guides 01-05 and 08 as live, and guides 06, 07,
  09, and 10 as future.

## Scope Boundaries

Do not implement guides 06, 07, 09, or 10 in this slice, except for future
route wording in `SKILL.md`.

Do not add templates, examples, validation/reference support directories,
schema files, executable validators, runtime services, graph databases,
ontology databases, GraphRAG, CCDP services, memory runtime automation,
package targets, Makefile changes, README/docs changes, generated zips, or
install wiring.

Do not perform live validation or verification against a real corpus.

Do not recreate `knowledge/concept-card-method/` or
`knowledge/source-preparation/`.

## Verification

Before editing, inspect source status and preserve unrelated work. Use explicit
paths when staging and committing.

Run the ledger checks in
`slice03-evidence-validation-verification/ledger.md`, including:

```text
scripts/check-skill-description.sh knowledge/concept-cards/SKILL.md
python3 /Users/oubiwann/.codex/skills/.system/skill-creator/scripts/quick_validate.py knowledge/concept-cards
git diff --check
make check-skills
make check-skill-versions
```

Also run a local Markdown link/anchor check over `knowledge/concept-cards/`.
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
