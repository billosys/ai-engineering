# Fresh Codex Prompt: Resume Project05

You are working in the `ai-engineering` repository. Resume Project05 from the
current plan-of-record; do not treat the older copied artifacts as current
instructions.

## Worktrees

- Source checkout: `/Users/oubiwann/lab/billosys/ai-engineering`
- Planning checkout: `/Users/oubiwann/lab/billosys/ai-engineering/.worktrees/planning`
- Project05 directory:
  `/Users/oubiwann/lab/billosys/ai-engineering/.worktrees/planning/project05-concept-card-skill`

Use the planning checkout for Project05 planning files. Use the source
checkout only for source implementation when the active slice authorizes it.

## Required Route

1. Load the `collaboration-framework` skill.
2. Load the `project-management` skill and read
   `/Users/oubiwann/.codex/skills/project-management/guides/README.md`.
3. Load the project-management focused guides required by the work you are
   doing.
4. Load `work-verification` ledger guidance before opening or closing any
   ledgered unit.
5. Read Project05 `project-plan.md`, project `ledger.md`, and the active arc
   and slice open sets before acting.

## Current Project05 Direction

Project05 began before Project04 completed the repository's skill/layout
reorganization. Project04 is now closed, and its current source/package layout
supersedes stale Project03 and early Project05 assumptions.

Project05 must implement at least two live installable skills:

- `document-extraction`
- `concept-cards`

`document-extraction` replaces the earlier planning name
`source-preparation`. It must stand alone for extracting usable Markdown,
structure, media references, locators, manifests, reports, and caveats from
PDF, EPUB, HTML, converted Markdown, indexing, reading, source review, and
downstream method workflows.

`concept-cards` replaces the earlier planning name `concept-card-method`. It
owns the concept-card v4.0 method: cards, claims, source support, source
spans, relationships, competency questions, extraction runs, validation,
verification, reconciliation, preservation decisions, evidence lifecycle, and
memory admission.

`ontology-engineering` is a likely future composite skill. Reserve that name
for later work unless the operator explicitly expands Project05.

## Layout Guardrails

Use the post-Project04 skill layout. Guides are single-purpose. Templates,
examples, and similar support material should live in sibling directories when
the skill needs them; do not place them under `guides/` merely because older
Project03 planning did.

If package behavior does not yet ship a support directory required by these
skills, update the package plan and implementation surface instead of hiding
the support material inside `guides/`.

## Nondeferrable Objectives

Do not defer:

- creation of `document-extraction`;
- creation of `concept-cards`;
- detailed human-assisted and agent-direct guidance for both skills;
- packaging, docs, generated-zip, install, and validation integration for both
  skills.

Allowed deferrals are limited to adjacent systems not required for these two
skills to exist and be usable: executable validators, runtime services, graph
databases, ontology databases, GraphRAG integrations, CCDP services, memory
runtime automation, CI expansion, and release publishing outside local
repository validation gates. Any deferral needs a durable reason and re-entry
condition.

## Current Starting Point

Closed:

- Arc01: `arc01-readiness-and-scope-lock/`

Arc02 is open:

`arc02-document-extraction-skill/`

Slice01 is open:

`arc02-document-extraction-skill/slice01-source-scaffold-and-load-contract/`

Use that slice's `cc-prompt.md` if you are CC for the next execution pass.
If that slice is already closed, read its closing report and CDC verification
before advancing.

## Commit Discipline

Preserve unrelated work. When committing, use explicit Project05 pathspecs.
Every assistant-authored commit must include:

```text
Co-authored-by: Codex <noreply@openai.com>
Co-authored-by: Billo AI <ai-engineering@billo.systems>
```
