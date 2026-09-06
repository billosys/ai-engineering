# CC Prompt: Arc03 Slice04 Relationships, CQs, Reconciliation, And Memory

You are CC implementing Project05 Arc03 Slice04 in the ai-engineering source
checkout. This slice is implementation work, not planning-only work.

## Start Here

Read, in this order:

1. `/Users/oubiwann/lab/billosys/ai-engineering/AGENTS.md`
2. `/Users/oubiwann/lab/billosys/ai-engineering/.worktrees/planning/project05-concept-card-skill/project-plan.md`
3. `/Users/oubiwann/lab/billosys/ai-engineering/.worktrees/planning/project05-concept-card-skill/arc03-concept-cards-skill-core/arc-plan.md`
4. `/Users/oubiwann/lab/billosys/ai-engineering/.worktrees/planning/project05-concept-card-skill/arc03-concept-cards-skill-core/ledger.md`
5. `/Users/oubiwann/lab/billosys/ai-engineering/.worktrees/planning/project05-concept-card-skill/arc03-concept-cards-skill-core/slice04-relationships-cqs-reconciliation-memory/slice-plan.md`
6. `/Users/oubiwann/lab/billosys/ai-engineering/.worktrees/planning/project05-concept-card-skill/arc03-concept-cards-skill-core/slice04-relationships-cqs-reconciliation-memory/ledger.md`
7. `/Users/oubiwann/lab/billosys/ai-engineering/.worktrees/planning/project05-concept-card-skill/arc03-concept-cards-skill-core/slice03-evidence-validation-verification/cdc-verification.md`
8. `/Users/oubiwann/lab/billosys/ai-engineering/knowledge/concept-cards/SKILL.md`
9. `/Users/oubiwann/lab/billosys/ai-engineering/knowledge/concept-cards/version-history.md`
10. `/Users/oubiwann/lab/billosys/ai-engineering/knowledge/concept-cards/guides/01-load-contract.md`
11. `/Users/oubiwann/lab/billosys/ai-engineering/knowledge/concept-cards/guides/02-operator-workflow.md`
12. `/Users/oubiwann/lab/billosys/ai-engineering/knowledge/concept-cards/guides/03-extraction.md`
13. `/Users/oubiwann/lab/billosys/ai-engineering/knowledge/concept-cards/guides/04-re-extraction-preservation.md`
14. `/Users/oubiwann/lab/billosys/ai-engineering/knowledge/concept-cards/guides/05-evidence-lifecycle.md`
15. `/Users/oubiwann/lab/billosys/ai-engineering/knowledge/concept-cards/guides/08-validation-verification.md`

Also inspect Project03 evidence as needed under:

- `/Users/oubiwann/lab/billosys/ai-engineering/.worktrees/planning/project05-concept-card-skill/artifacts/project03-concept-card-method/arc03-conceptual-model/slice04-model-synthesis/artifacts/v40-conceptual-model.md`
- `/Users/oubiwann/lab/billosys/ai-engineering/.worktrees/planning/project05-concept-card-skill/artifacts/project03-concept-card-method/arc04-skill-architecture/slice05-architecture-synthesis/artifacts/v40-skill-architecture.md`
- `/Users/oubiwann/lab/billosys/ai-engineering/.worktrees/planning/project05-concept-card-skill/artifacts/project03-concept-card-method/arc05-implementation-plan/slice05-implementation-plan-synthesis/artifacts/v40-source-edit-sequence.md`

Translate historical `concept-card-method` paths through the current live
source root `knowledge/concept-cards/`.

## Implementation Scope

Implement exactly this source-skill slice:

- add `knowledge/concept-cards/guides/06-graph-cq.md`;
- add `knowledge/concept-cards/guides/07-reconciliation.md`;
- add `knowledge/concept-cards/guides/09-memory-admission.md`;
- add `knowledge/concept-cards/guides/10-maintenance-packaging.md`;
- update `knowledge/concept-cards/SKILL.md`;
- update `knowledge/concept-cards/version-history.md`;
- update existing guides 01 through 05 and 08 only as needed to make live-route
  wording accurate now that guides 06, 07, 09 and 10 are implemented.

Advance `metadata.version` to `"1.3.0"` and add a sibling
`version-history.md` entry. Do not create guide-local version histories. Do
not repeat the skill version anywhere except `SKILL.md` metadata and sibling
`version-history.md`.

## Required Content

Guide 06 must provide detailed relationship edge and competency question
instructions:

- define when a relationship needs first-class edge identity rather than
  ordinary card-local navigation;
- identify endpoints, directionality, inverse/symmetric relation concerns,
  relation meaning, support/provenance and lifecycle attachments;
- keep valid endpoints separate from warranted relationship meaning;
- define competency questions, CQ coverage assertions and answerability;
- keep CQ coverage separate from retrieval success, validation, verification,
  reconciliation and memory admission;
- cover obsolete, deferred or changed CQs without silent deletion;
- include human-assisted and agent-direct operation notes;
- report handoff output and remaining work;
- state explicitly that this is not runtime graph/database construction.

Guide 07 must provide detailed reconciliation instructions:

- identify reconciliation targets and conflict scope;
- cover duplicate concepts, competing definitions, slug/taxonomy drift,
  conflicting source support, relationship asymmetry and CQ coverage disputes;
- compare source evidence and prior values without letting structural validity
  or worker agreement select a winner automatically;
- record affected constructs, disposition, rationale, actor/run, evidence,
  preservation implications, verification implications, admission implications
  and unresolved work;
- keep reconciliation result/state distinct from validation result,
  verification result/state, preservation decision and memory admission;
- include human-assisted and agent-direct operation notes;
- report handoff output and remaining work.

Guide 09 must provide detailed memory-admission instructions:

- define memory admission as permission to rely on a construct as durable
  semantic memory under the applicable evidence and acceptance requirements;
- distinguish admission from keeping an artifact, source support, evidence
  grade, extraction confidence, validation, verification, reconciliation,
  preservation and memory-runtime storage;
- identify required inputs: target revision, source support, evidence grade,
  validation result, verification result/state, reconciliation result/state,
  preservation decisions, intended use and operator acceptance where required;
- cover admit/reject/defer outcomes, caveats, revision invalidation and
  re-entry checks;
- include human-assisted and agent-direct operation notes;
- report handoff output and remaining work;
- state explicitly that the guide does not perform a memory-runtime write.

Guide 10 must provide maintenance and promise-boundary instructions:

- identify what the source-core skill owns after Arc03;
- state what Arc04 still owns: sibling templates, examples,
  validation/reference support and schemas;
- state what Arc05 still owns: package targets, generated zips, docs,
  README/discoverability, install behavior and package validation;
- prevent source guidance from promising executable validators, runtime
  services, graph/ontology databases, GraphRAG, CCDP services, memory runtime
  automation or live corpus processing;
- describe how future edits should preserve construct distinctions, route
  document extraction to `document-extraction`, maintain version history, and
  avoid duplicate skill-version prose;
- include handoff guidance for future Arc04/Arc05 work.

Also clean now-stale future-route wording:

- `SKILL.md` should identify guides 01 through 10 as live;
- guide 01 should no longer say guides 06, 07, 09 or 10 are future;
- guide 02 should route relationship/CQ, reconciliation, memory-admission and
  maintenance tasks to the newly live guides;
- guides 03, 04, 05 and 08 should point to the newly live guides where their
  handoffs mention those concerns.

## Scope Boundaries

Do not add templates, examples, validation/reference support directories,
schema files, executable validators, runtime services, graph databases,
ontology databases, GraphRAG, CCDP services, memory runtime automation,
package targets, Makefile changes, README/docs changes, generated zips, install
wiring, or package path exceptions.

Do not perform live extraction, graph construction, reconciliation, memory
admission or validation/verification against a real corpus.

Do not recreate `knowledge/concept-card-method/` or
`knowledge/source-preparation/`.

## Verification

Before editing, inspect source status and preserve unrelated work. Use explicit
paths when staging and committing.

Run the ledger checks in
`slice04-relationships-cqs-reconciliation-memory/ledger.md`, including:

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
