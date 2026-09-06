# CC Prompt: Arc02 Slice01 Source Scaffold And Load Contract

You are working in the `ai-engineering` repository.

## Role

You are CC for Project05 Arc02 Slice01. Implement the first source slice for
the live `document-extraction` skill.

## Worktrees

- Source checkout:
  `/Users/oubiwann/lab/billosys/ai-engineering`
- Planning checkout:
  `/Users/oubiwann/lab/billosys/ai-engineering/.worktrees/planning`
- Project05 directory:
  `/Users/oubiwann/lab/billosys/ai-engineering/.worktrees/planning/project05-concept-card-skill`
- Slice directory:
  `/Users/oubiwann/lab/billosys/ai-engineering/.worktrees/planning/project05-concept-card-skill/arc02-document-extraction-skill/slice01-source-scaffold-and-load-contract`

## Required Context

Read, in this order:

1. `/Users/oubiwann/.codex/skills/collaboration-framework/SKILL.md`
2. `/Users/oubiwann/.codex/skills/project-management/SKILL.md`
3. `/Users/oubiwann/.codex/skills/project-management/guides/README.md`
4. `/Users/oubiwann/.codex/skills/work-verification/SKILL.md`
5. Project05 open context:
   - `project-plan.md`
   - `ledger.md`
   - `arc01-readiness-and-scope-lock/closing-report.md`
   - `arc02-document-extraction-skill/arc-plan.md`
   - `arc02-document-extraction-skill/ledger.md`
   - `arc02-document-extraction-skill/slice01-source-scaffold-and-load-contract/slice-plan.md`
   - `arc02-document-extraction-skill/slice01-source-scaffold-and-load-contract/ledger.md`
6. Arc01 readiness artifacts:
   - `arc01-readiness-and-scope-lock/slice01-current-layout-reconciliation/artifacts/project05-current-source-surface-inventory.md`
   - `arc01-readiness-and-scope-lock/slice01-current-layout-reconciliation/artifacts/project05-artifact-relevance-register.md`
   - `arc01-readiness-and-scope-lock/slice01-current-layout-reconciliation/artifacts/project05-naming-and-scope-register.md`
   - `arc01-readiness-and-scope-lock/slice01-current-layout-reconciliation/artifacts/project05-package-surface-requirements.md`
   - `arc01-readiness-and-scope-lock/slice01-current-layout-reconciliation/artifacts/project05-implementation-roadmap-update.md`
7. Project05 accepted architecture inputs:
   - `artifacts/operator-accepted-project05-reorientation.md`
   - `artifacts/operator-accepted-src-prep-arch.md`
8. Current source examples:
   - `knowledge/scientific-methods/SKILL.md`
   - `knowledge/scientific-methods/version-history.md`
   - `knowledge/scientific-methods/guides/`
   - `knowledge/project-management/SKILL.md`
   - `knowledge/work-verification/SKILL.md`

## Implementation Scope

Create this source scaffold:

```text
/Users/oubiwann/lab/billosys/ai-engineering/knowledge/document-extraction/
  SKILL.md
  version-history.md
  guides/
    01-load-contract.md
    02-workflow.md
    03-output-contract.md
```

The entrypoint must use frontmatter:

```yaml
name: document-extraction
```

The skill should describe a standalone capability for extracting usable
Markdown, structure, media references, locators, manifests, readiness reports,
and caveats from PDF, EPUB, HTML, converted Markdown, and converter-produced
source bundles.

The skill must support:

- standalone indexing, reading, source review, and analysis workflows;
- downstream `concept-cards` use as upstream provenance;
- human-assisted operation;
- agent-direct operation when files/tools are available;
- read-before-write inspection;
- raw input preservation;
- explicit caveats for unverifiable structure, media, locator, or conversion
  ambiguity.

The first three guides should cover:

- positive and negative load triggers;
- ownership and routing boundaries;
- human-assisted and agent-direct workflow;
- output contract for prepared Markdown, structure maps, media references,
  locator records, manifests, readiness reports, and caveats;
- future guide routes for detailed PDF/Marker, EPUB/pandoc, HTML/converted
  Markdown, media normalization, structure splitting, locator, validation,
  template, and example work.

## Out Of Scope

Do not:

- create `knowledge/source-preparation/`;
- create or edit `knowledge/concept-cards/`;
- add detailed PDF/Marker or EPUB/pandoc procedural guides in this slice;
- add templates or examples in this slice;
- change `Makefile`, `README.md`, `docs/`, release notes, generated zips, or
  install behavior in this slice;
- claim `document-extraction.zip` exists yet.

## Validation

Before closing, run:

```sh
cd /Users/oubiwann/lab/billosys/ai-engineering
scripts/check-skill-description.sh knowledge/document-extraction/SKILL.md
git diff --check
git status --short --untracked-files=all
```

Do not run package gates unless you changed package machinery, which this
slice should not do.

## Close And Commit

Update the Slice01 ledger row by row. Write
`slice01-source-scaffold-and-load-contract/closing-report.md` with:

- source files changed;
- source commit hash or `pending until committed`;
- planning files changed;
- validation results;
- row walk;
- artifact inventory;
- bubble-up to Arc02, including whether Arc02's plan needs changes.

Commit the source files and planning close files. Use explicit file names in
the commit command; preserve unrelated changes.

Use the required trailers:

```text
Co-authored-by: Codex <noreply@openai.com>
Co-authored-by: Billo AI <ai-engineering@billo.systems>
```
