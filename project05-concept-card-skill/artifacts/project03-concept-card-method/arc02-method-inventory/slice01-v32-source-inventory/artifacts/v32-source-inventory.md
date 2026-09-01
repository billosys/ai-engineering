# v3.2 Source Inventory

```yaml
project: project03-concept-card-method
arc: arc02-method-inventory
slice: slice01-v32-source-inventory
status: proposed-done
source-docs:
  - artifacts/source-docs/0009-howto-concept-card-extraction-with-llms-v3.2.md
  - artifacts/source-docs/0010-a-guide-for-parallel-concept-card-re-extraction-v3.2.md
inventory-mode: descriptive
v4-design-decisions: none
```

## Scope Note

This inventory records what the v3.2 baseline method actually says. It uses
the preserved source snapshots under `artifacts/source-docs/` as the line
anchored baseline; those snapshots were verified to match the workbench inputs.
The prior assessment memo is useful context for later gap analysis, but it is
not the source of truth for this inventory.

## Source Documents

### 0009-howto

Path:
`artifacts/source-docs/0009-howto-concept-card-extraction-with-llms-v3.2.md`

Purpose: a practical howto for creating high-quality concept cards from
primary source material, including re-extraction over older card inventories
(lines 1-3). It defines the card format, the extraction rules, the file layout,
fresh extraction workflow, re-extraction workflow, quality checklist, common
mistakes, and edge cases.

Structure:

- Version framing: v3.2 is a path/layout update over v3.1, with no schema,
  body-section, confidence, relationship, or competency-question changes
  (lines 5-18).
- Concept-card definition: cards are atomic knowledge units with YAML
  frontmatter for machine use and Markdown body sections for human and LLM use
  (lines 22-33).
- Golden rules: atomicity, source-faithful synthesis, explicit typed
  relationships, confidence signalling, and source provenance (lines 36-89).
- Frontmatter schema: core identification, classification, provenance,
  confidence, aliases, typed relationships, and `answers_questions` (lines
  92-219).
- Body schema: `Quick Definition`, `Core Definition`, `Prerequisites`,
  `Key Properties`, `Construction / Recognition`, `Context & Application`,
  `Examples`, `Relationships`, `Common Errors`, `Common Confusions`, `Source
  Reference`, and `Verification Notes` (lines 222-470).
- File organization: unified `ai-engineering` layout under
  `knowledge/<kb>/`, with converted Markdown as canonical extraction input,
  concept cards under `knowledge/<kb>/concept-cards/<source-slug>/`, and
  metadata under `knowledge/<kb>/extraction-metadata/<source-slug>/` (lines
  474-518).
- Re-extraction workflow: source-primary, old-card-secondary, v3-template
  target, unique-value preservation, per-chapter and per-concept procedure,
  and post-re-extraction checks (lines 571-629).
- Quality and error controls: frontmatter, body, cross-reference,
  re-extraction, common-mistake, edge-case, and final-checklist controls
  (lines 632-854).

### 0010-a-guide

Path:
`artifacts/source-docs/0010-a-guide-for-parallel-concept-card-re-extraction-v3.2.md`

Purpose: a coordinator guide for re-extracting an existing card inventory to
the v3 template with multiple LLM agents working in parallel (lines 1-4). It
operationalizes the 0009 howto for larger re-extraction runs.

Structure:

- Version framing: v3.2 updates repo paths, source-format paths, and the 0009
  reference, but leaves the extraction machinery unchanged (lines 7-19).
- Overview: four phases - requirements and scope, analysis and planning,
  parallel re-extraction, and validation/preservation check (lines 24-31).
- Prerequisites: LLM/model setup, converted Markdown source files, existing
  cards, the 0009 howto, and the unified `knowledge/<kb>/` directory structure
  (lines 35-91).
- Phase 0: audit existing cards, elicit 30-50 competency questions, define
  domain taxonomy, and document notation conventions (lines 95-236).
- Phase 1: analyze source material, map competency questions to chapters and
  concepts, create exactly five balanced agent assignments, and compile agent
  instructions (lines 240-339).
- Phase 2: give agents the v3 concept-card template plus merge-aware
  re-extraction instructions, quality requirements, file naming rules, and
  per-agent scope (lines 343-621).
- Phase 3: validate structure, slug/filename consistency, cross-references,
  preservation, CQ coverage, and sampled quality (lines 625-733).
- Troubleshooting, workflow summary, version history, and quick reference
  tables for confidence, relationships, required frontmatter, and per-card
  re-extraction checks (lines 736-907).

## Method Inventory By Category

### Purpose

The v3.2 method aims to create source-faithful, structured, queryable concept
cards for humans and LLMs. 0009 defines the card and extraction standard;
0010 defines the coordinator process for re-extracting larger existing
inventories in parallel.

### Schema

The v3.2 schema is the v3 card template with path updates only. It includes:

- Core identification: `concept` and `slug` (0009 lines 92-109; 0010 lines
  877-889).
- Classification: `category`, `subcategory`, and `tier` (0009 lines 111-124).
- Provenance: `source`, `source_slug`, `authors`, `chapter`,
  `chapter_number`, `pdf_page`, and `section` (0009 lines 126-144).
- Confidence: `extraction_confidence` with `high`, `medium`, or `low` (0009
  lines 146-152; 0010 lines 860-866).
- Authority control: `aliases`, with explicit YAML quoting guidance for values
  containing colons (0009 lines 154-181).
- Relationship fields: `prerequisites`, `extends`, `related`, and
  `contrasts_with` using exact concept slugs (0009 lines 183-207; 0010 lines
  868-874).
- Competency question linkage: `answers_questions` lists questions the card
  helps answer (0009 lines 209-219; 0010 lines 553-557).

The body schema is standardized and section-driven. Each card has quick and
core definitions, prerequisites, key properties, construction/recognition,
context/application, examples, relationships, common errors, common confusions,
source reference, and verification notes (0009 lines 222-470; 0010 lines
396-509).

### Workflow

Fresh extraction in 0009 is chapter-first and concept-first:

- Read the chapter.
- List concepts by importance and complexity.
- Determine tiers from prerequisites.
- Extract in dependency order.
- Cross-reference during extraction.
- Validate structure and references (0009 lines 737-761).

Re-extraction in 0009 is merge-aware:

- Use the source material as primary.
- Treat old cards as secondary preservation inputs.
- Target the v3 template.
- Preserve unique old-card value.
- Run card-count, preservation, structural, and LLM-artifact checks after
  re-extraction (0009 lines 571-629).

Parallel re-extraction in 0010 adds a coordinator layer:

- Phase 0 audits existing cards and prepares requirements (0010 lines 95-236).
- Phase 1 analyzes source material, maps competency questions, and balances
  exactly five agent assignments (0010 lines 240-339).
- Phase 2 runs merge-aware re-extraction agents with a shared template and
  prompt contract (0010 lines 343-621).
- Phase 3 validates structure, references, preservation, CQ coverage, and
  sampled semantic quality (0010 lines 625-733).

### Validation

Validation in v3.2 is mostly checklist and shell-command based. It checks:

- Required frontmatter fields and body sections (0009 lines 632-659; 0010
  lines 627-649).
- Cross-reference existence and relationship typing (0009 lines 661-665; 0010
  lines 666-681).
- Re-extraction preservation of old-card value (0009 lines 667-672; 0010
  lines 684-713).
- CQ coverage: each competency question should be listed by at least one card
  and substantively answerable from those cards (0010 lines 715-720).
- Quality sampling: definitions, confidence rationales, prerequisite chains,
  source examples, variants, relationships, and section names (0010 lines
  722-733).
- LLM artifact detection using simple text searches (0009 lines 621-629; 0010
  lines 708-713).

### Provenance

The method treats provenance as required card content. Each assertion should be
traceable to source chapter, chapter number, PDF page, section heading, and
source examples where available (0009 lines 81-89, 126-144, 438-449). The body
also carries a `Source Reference` section and `Verification Notes` that
distinguish direct quotation, synthesis, uncertainty, confidence rationale, and
cross-reference status (0009 lines 438-470; 0010 lines 495-509).

### Relationship Model

The relationship model is typed but compact:

- `prerequisites`: concepts that must be understood first.
- `extends`: concepts this one builds upon or elaborates.
- `related`: non-hierarchical associations.
- `contrasts_with`: commonly confused concepts (0009 lines 183-207; 0010
  lines 868-874).

Relationships appear both in frontmatter and in the body. The body repeats the
relationships with explanatory context and uses subsections such as Builds
Upon, Enables, Related, and Contrasts With (0009 lines 370-399; 0010 lines
  462-477).

### Competency Question Handling

Competency questions are first-class coverage hooks in v3.2. Individual cards
list `answers_questions` (0009 lines 209-219). The parallel guide requires the
coordinator to elicit 30-50 CQs across definitional, relational, procedural,
prerequisite, and diagnostic types before source analysis (0010 lines 143-190).
It then maps CQs to chapters and concepts to reveal priorities, coverage gaps,
and completeness requirements (0010 lines 289-309). Phase 3 checks that every
CQ is covered by at least one card that contains enough information to answer
it (0010 lines 715-720).

### Confidence Semantics

The v3.2 confidence model is a single `extraction_confidence` enum:

- `high`: source explicitly defines the concept and extraction is
  straightforward.
- `medium`: concept is present but requires synthesis.
- `low`: concept is inferred or reconstructed from context (0009 lines 71-79;
  0010 lines 860-866).

Confidence is assigned from source definition clarity, not from old-card
content, and must be justified in `Verification Notes` (0009 lines 146-152,
608-619, 648-659).

### Re-Extraction Mechanics

Re-extraction is triggered when older cards lack v3 frontmatter fields, body
sections, or standard section names (0009 lines 575-583). The mechanics are:

- Inventory existing cards.
- Read source chapters from `knowledge/<kb>/sources/md/<source-slug>/`.
- Identify concepts against existing filenames.
- Extract fresh from source.
- Before writing, read the old card if it exists.
- Preserve hand-curated corrections, additional examples, domain-expert notes,
  or unique old-card content.
- Overwrite into the v3 template and record preservation notes (0009 lines
  585-619; 0010 lines 534-551).

### Preservation Checks

Preservation is explicit in both docs:

- New card count should be greater than or equal to old card count unless
  investigated and justified (0009 lines 621-626; 0010 lines 684-699).
- Unique old-card content must be spot-checked and preserved where valid (0009
  lines 621-626; 0010 lines 701-706).
- Verification Notes should record what was preserved from the old card (0009
  lines 608-619; 0010 lines 895-902).
- Troubleshooting treats decreased card count and lost unique content as
  defects requiring investigation or re-run (0010 lines 778-796).

### Notable Limitations In The Baseline

These limitations are source-grounded observations, not v4.0 design answers:

- Confidence is flat: one enum carries source clarity, extractor certainty,
  and likely verification concerns without separating them (0009 lines 71-79;
  0010 lines 860-866).
- Validation is shell/checklist shaped. It checks required fields and obvious
  consistency, but it does not define a formal schema, semantic validator, or
  reconciliation authority (0009 lines 632-672; 0010 lines 625-733).
- Relationship semantics are typed but limited to four fields; there is no
  graph-level reconciliation model beyond slug existence and circular
  prerequisite checks (0009 lines 183-207, 661-665; 0010 lines 666-681).
- Parallel extraction assigns exactly five agents, but the merge authority is
  mostly procedural and validation-oriented rather than a separately specified
  reconciliation role (0010 lines 311-339, 625-733).
- Memory admission is implicit: cards are validated and preserved, but there is
  no distinct admission state for whether a card may enter durable LLM memory.
- CCDP compatibility is not part of v3.2. Claims, evidence grades, audit
  history, and dispatcher capabilities are not represented in the baseline
  schema.
