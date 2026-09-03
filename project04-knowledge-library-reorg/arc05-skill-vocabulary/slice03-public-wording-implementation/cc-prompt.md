# CC Prompt: Arc05 Slice03 Public Wording Implementation

You are CC working in Project04 Expedited Mode.

## Context

Project: `project04-knowledge-library-reorg`

Arc: `arc05-skill-vocabulary`

Slice: `slice03-public-wording-implementation`

Source checkout:
`/Users/oubiwann/lab/billosys/ai-engineering`

Planning checkout:
`/Users/oubiwann/lab/billosys/ai-engineering/.worktrees/planning`

Project directory:
`/Users/oubiwann/lab/billosys/ai-engineering/.worktrees/planning/project04-knowledge-library-reorg`

## Required Reading

Read these files before working:

- `project-plan.md`
- `ledger.md`
- `artifacts/external-ontology-rubric-research.md`
- `arc01-material-inventory/slice03-skill-topology-classification/cdc-verification.md`
- `arc01-material-inventory/slice03-skill-topology-classification/artifacts/public-language-implications.md`
- `arc04-user-docs/closing-report.md`
- `arc05-skill-vocabulary/arc-plan.md`
- `arc05-skill-vocabulary/ledger.md`
- `arc05-skill-vocabulary/slice01-public-language-surface-inventory/cdc-verification.md`
- `arc05-skill-vocabulary/slice01-public-language-surface-inventory/artifacts/current-public-language-surface-map.md`
- `arc05-skill-vocabulary/slice02-accepted-vocabulary-positioning/cdc-verification.md`
- `arc05-skill-vocabulary/slice02-accepted-vocabulary-positioning/artifacts/accepted-public-vocabulary.md`
- `arc05-skill-vocabulary/slice02-accepted-vocabulary-positioning/artifacts/example-and-edge-case-positioning.md`
- `arc05-skill-vocabulary/slice02-accepted-vocabulary-positioning/artifacts/public-language-avoid-list.md`
- `arc05-skill-vocabulary/slice02-accepted-vocabulary-positioning/artifacts/source-edit-authorization-plan.md`
- `arc05-skill-vocabulary/slice02-accepted-vocabulary-positioning/artifacts/re-entry-condition-register.md`
- `arc05-skill-vocabulary/slice03-public-wording-implementation/slice-plan.md`
- `arc05-skill-vocabulary/slice03-public-wording-implementation/ledger.md`

## Task

Implement the accepted Arc05 public vocabulary in the authorized public source
surfaces only.

Authorized source surfaces:

- `README.md`
- `docs/repository-overview.md`
- `docs/skill-library.md`
- `docs/collaboration-framework.md`
- `docs/knowledge-library-anatomy.md`
- `docs/protocols.md`
- `docs/contributing.md`
- `docs/building-and-installing.md`
- top-level `SKILL.md`

Create these planning artifacts:

- `arc05-skill-vocabulary/slice03-public-wording-implementation/artifacts/public-wording-implementation-map.md`
- `arc05-skill-vocabulary/slice03-public-wording-implementation/artifacts/vocabulary-scan-evidence.md`
- `arc05-skill-vocabulary/slice03-public-wording-implementation/artifacts/source-change-and-validation-evidence.md`
- `arc05-skill-vocabulary/slice03-public-wording-implementation/artifacts/deferred-reentry-notes.md`

Update:

- `arc05-skill-vocabulary/slice03-public-wording-implementation/ledger.md`

Add:

- `arc05-skill-vocabulary/slice03-public-wording-implementation/closing-report.md`

Do not create `cdc-verification.md`; CDC owns that after your proposed close.

## Wording Requirements

Preserve the two-axis model:

- skill kind: what the skill is about;
- topology: how the skill composes.

Use the accepted public terms from Slice02 where useful:

- domain/tooling skill;
- framework/operational skill;
- method skill, with availability qualifiers;
- protocol distribution;
- protocol package;
- support material;
- support template;
- knowledge substrate;
- atomic skill;
- composite skill.

Use accepted examples carefully:

- Rust is the public example of an atomic domain/tooling skill.
- `collaboration-framework` is the accepted public example of a composite
  framework/operational skill and daily-driver composer.
- CCDP is a protocol distribution / protocol package, not an installable skill
  package.
- Biome is a multi-entrypoint knowledge root.
- `templates/GUIDE.md` is support material / support template.
- `concept-card-method` is only a planned method skill until source and
  package support exist.

Avoid unqualified prohibited claims:

- atomic means domain;
- composite means framework;
- method skills are composite;
- CCDP is a skill;
- concept-card-method is available;
- source-root/package-root equivalence;
- `collaboration-framework` is deprecated;
- all knowledge lives in docs;
- all framework material is documentation;
- CCDP package is installed by `make install`.

## Source Edit Policy

Commit source edits first, before planning edits, using explicit file paths in
both staging and commit commands. Do not commit generated zips.

Do not edit:

- `Makefile`
- `package-path-exceptions.tsv`
- package target names
- `INSTALL_ZIPS`
- `ALL_SKILL_FILES`
- `CF_FILES`
- generated zips
- package root names
- `knowledge/*/SKILL*.md` frontmatter names/descriptions/categories
- `protocols/ccdp/**`
- `templates/GUIDE.md`
- source moves or file renames
- `concept-card-method` implementation
- CCDP repackaging as an installable skill

If accepted vocabulary appears to require one of those excluded surfaces,
record it in `artifacts/deferred-reentry-notes.md` rather than editing that
surface.

Every assistant-authored commit must include both trailers:

```text
Co-authored-by: Codex <noreply@openai.com>
Co-authored-by: Billo AI <ai-engineering@billo.systems>
```

## Validation

Run and record:

- source `git status --short --untracked-files=all` before edits
- source `git diff --check`
- accepted/avoided vocabulary scans over `README.md`, `docs/`, and `SKILL.md`
- README/docs route scans for `docs/`, `knowledge/`, `protocols/`,
  `templates/`, `Makefile`, and package links
- local Markdown link validation if any links change
- `make check-skills`
- `make check-package-paths` if top-level `SKILL.md` changes
- `make all` if top-level `SKILL.md` changes
- `make ccdp-package` and `make check-ccdp-package` if `docs/protocols.md`
  changes CCDP route or package wording
- planning `git diff --check`
- all seven Slice03 ledger verifier commands
- final source and planning `git status --short --untracked-files=all`

If a scan still reports a risky phrase, record whether the match is a quoted
avoid-list item, a caveated "not this" explanation, a valid historical
reference, a deferral, or a remaining defect.

## Source Commit

Commit source edits with an explicit path list. Adjust this list to exactly
match every source file you edit:

```bash
git -C /Users/oubiwann/lab/billosys/ai-engineering add \
  README.md \
  docs/repository-overview.md \
  docs/skill-library.md \
  docs/collaboration-framework.md \
  docs/knowledge-library-anatomy.md \
  docs/protocols.md \
  docs/contributing.md \
  docs/building-and-installing.md \
  SKILL.md
```

```bash
git -C /Users/oubiwann/lab/billosys/ai-engineering commit \
  -m "Implement Arc05 public skill vocabulary" \
  -- \
  README.md \
  docs/repository-overview.md \
  docs/skill-library.md \
  docs/collaboration-framework.md \
  docs/knowledge-library-anatomy.md \
  docs/protocols.md \
  docs/contributing.md \
  docs/building-and-installing.md \
  SKILL.md
```

Include the required co-author trailers in the source commit message.

## Planning Commit

After source commit and validation, commit only the Slice03 planning close
packet with an explicit file list:

```bash
git -C /Users/oubiwann/lab/billosys/ai-engineering/.worktrees/planning add \
  project04-knowledge-library-reorg/arc05-skill-vocabulary/slice03-public-wording-implementation/artifacts/public-wording-implementation-map.md \
  project04-knowledge-library-reorg/arc05-skill-vocabulary/slice03-public-wording-implementation/artifacts/vocabulary-scan-evidence.md \
  project04-knowledge-library-reorg/arc05-skill-vocabulary/slice03-public-wording-implementation/artifacts/source-change-and-validation-evidence.md \
  project04-knowledge-library-reorg/arc05-skill-vocabulary/slice03-public-wording-implementation/artifacts/deferred-reentry-notes.md \
  project04-knowledge-library-reorg/arc05-skill-vocabulary/slice03-public-wording-implementation/ledger.md \
  project04-knowledge-library-reorg/arc05-skill-vocabulary/slice03-public-wording-implementation/closing-report.md
```

```bash
git -C /Users/oubiwann/lab/billosys/ai-engineering/.worktrees/planning commit \
  -m "Complete Project04 Arc05 Slice03" \
  -- \
  project04-knowledge-library-reorg/arc05-skill-vocabulary/slice03-public-wording-implementation/artifacts/public-wording-implementation-map.md \
  project04-knowledge-library-reorg/arc05-skill-vocabulary/slice03-public-wording-implementation/artifacts/vocabulary-scan-evidence.md \
  project04-knowledge-library-reorg/arc05-skill-vocabulary/slice03-public-wording-implementation/artifacts/source-change-and-validation-evidence.md \
  project04-knowledge-library-reorg/arc05-skill-vocabulary/slice03-public-wording-implementation/artifacts/deferred-reentry-notes.md \
  project04-knowledge-library-reorg/arc05-skill-vocabulary/slice03-public-wording-implementation/ledger.md \
  project04-knowledge-library-reorg/arc05-skill-vocabulary/slice03-public-wording-implementation/closing-report.md
```

Include both required trailers in the planning commit message.

## Report

Report:

- source commit hash;
- planning commit hash;
- source files edited;
- artifacts created;
- accepted vocabulary implementation summary;
- deferrals or re-entry conditions;
- ledger result;
- validation commands and outcomes;
- final source and planning checkout status;
- whether Slice03 is proposed-done pending CDC verification.
