# CC Prompt: Arc03 Slice02 Extraction, Re-Extraction, And Provenance

You are CC implementing Project05 Arc03 Slice02 in the ai-engineering source
checkout. This slice is implementation work, not planning-only work.

## Start Here

Read, in this order:

1. `/Users/oubiwann/lab/billosys/ai-engineering/AGENTS.md`
2. `/Users/oubiwann/lab/billosys/ai-engineering/.worktrees/planning/project05-concept-card-skill/project-plan.md`
3. `/Users/oubiwann/lab/billosys/ai-engineering/.worktrees/planning/project05-concept-card-skill/arc03-concept-cards-skill-core/arc-plan.md`
4. `/Users/oubiwann/lab/billosys/ai-engineering/.worktrees/planning/project05-concept-card-skill/arc03-concept-cards-skill-core/ledger.md`
5. `/Users/oubiwann/lab/billosys/ai-engineering/.worktrees/planning/project05-concept-card-skill/arc03-concept-cards-skill-core/slice02-extraction-reextraction-provenance/slice-plan.md`
6. `/Users/oubiwann/lab/billosys/ai-engineering/.worktrees/planning/project05-concept-card-skill/arc03-concept-cards-skill-core/slice02-extraction-reextraction-provenance/ledger.md`
7. `/Users/oubiwann/lab/billosys/ai-engineering/.worktrees/planning/project05-concept-card-skill/arc03-concept-cards-skill-core/slice01-source-scaffold-and-load-contract/cdc-verification.md`
8. `/Users/oubiwann/lab/billosys/ai-engineering/knowledge/concept-cards/SKILL.md`
9. `/Users/oubiwann/lab/billosys/ai-engineering/knowledge/concept-cards/guides/01-load-contract.md`
10. `/Users/oubiwann/lab/billosys/ai-engineering/knowledge/concept-cards/guides/02-operator-workflow.md`

Also inspect Project03 evidence as needed under:

- `/Users/oubiwann/lab/billosys/ai-engineering/.worktrees/planning/project05-concept-card-skill/artifacts/project03-concept-card-method/arc03-conceptual-model/slice04-model-synthesis/artifacts/v40-conceptual-model.md`
- `/Users/oubiwann/lab/billosys/ai-engineering/.worktrees/planning/project05-concept-card-skill/artifacts/project03-concept-card-method/arc04-skill-architecture/slice05-architecture-synthesis/artifacts/v40-skill-architecture.md`
- `/Users/oubiwann/lab/billosys/ai-engineering/.worktrees/planning/project05-concept-card-skill/artifacts/project03-concept-card-method/arc05-implementation-plan/slice05-implementation-plan-synthesis/artifacts/v40-source-edit-sequence.md`

Translate historical `concept-card-method` paths through the current live
source root `knowledge/concept-cards/`. Historical under-`guides` support
layouts remain evidence only; support directories later belong as siblings
unless a current package contract explicitly says otherwise.

## Implementation Scope

Implement exactly this source-skill slice:

- add `knowledge/concept-cards/guides/03-extraction.md`;
- add `knowledge/concept-cards/guides/04-re-extraction-preservation.md`;
- update `knowledge/concept-cards/SKILL.md`;
- update `knowledge/concept-cards/version-history.md`.

Advance `metadata.version` to `"1.1.0"` and add a sibling
`version-history.md` entry. Do not create guide-local version histories.

## Required Content

Guide 03 must provide detailed instructions for source-faithful extraction:

- establish source snapshot/prepared-source identity, including optional
  `document-extraction` manifests, locator maps, readiness reports, and
  caveats;
- define extraction-run identity, method/prompt identity, actor scope, input
  revisions, expected output set, and worker provenance when parallel work
  actually occurs;
- select concept boundaries and keep one concept per card;
- identify claims as source-grounded assertions;
- capture source locators and source spans with enough basis to recover the
  source material;
- assert source support only after comparing the selected span to the claim;
- separate source statements from assistant inference;
- record extraction confidence as the extraction-act signal, not evidence
  grade or verification state;
- include human-assisted and agent-direct operation notes;
- report caveats, unresolved support, and handoff output.

Guide 04 must provide detailed instructions for source-primary re-extraction
and preservation:

- inventory prior cards, claims, support attachments, locators, spans, edges,
  CQs, run records, and prior results before rewriting;
- compare against source first, then use prior cards as comparison inputs;
- handle source drift, unavailable source, damaged conversion, unsupported
  prior material, changed claims, unchanged claims, and new source coverage;
- record preservation decisions as preserved, superseded, rejected, or
  unresolved with rationale and affected constructs;
- keep unique prior value traceable even when it is unsupported or not admitted;
- record re-extraction run provenance, including old-card inputs and worker
  scopes when present;
- include human-assisted and agent-direct operation notes;
- report handoff output and remaining work.

Both guides must keep source support, source span, source locator, extraction
run provenance, extraction confidence, evidence grade, validation result,
verification result, reconciliation result, preservation decision, and memory
admission distinct.

## Scope Boundaries

Do not implement guide 05 or later guides in this slice, except for future
route wording in `SKILL.md`.

Do not add templates, examples, validation/reference support directories,
schema files, executable validators, runtime services, graph databases,
ontology databases, GraphRAG, CCDP services, memory runtime automation,
package targets, Makefile changes, README/docs changes, generated zips, or
install wiring.

Do not perform live extraction against a real corpus.

Do not recreate `knowledge/concept-card-method/` or
`knowledge/source-preparation/`.

## Verification

Before editing, inspect source status and preserve unrelated work. Use explicit
paths when staging and committing.

Run the ledger checks in
`slice02-extraction-reextraction-provenance/ledger.md`, including:

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
