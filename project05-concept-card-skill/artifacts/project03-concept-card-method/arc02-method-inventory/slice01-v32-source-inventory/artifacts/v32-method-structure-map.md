# v3.2 Method Structure Map

```yaml
project: project03-concept-card-method
arc: arc02-method-inventory
slice: slice01-v32-source-inventory
status: proposed-done
map-mode: baseline-observation-with-v4-questions
v4-design-decisions: none
```

## Scope Fence

This map organizes the v3.2 baseline so later Arc02 slices can compare it to
the v4.0 target. It does not design the v4.0 conceptual model, final skill
layout, validation scripts, memory admission workflow, or CCDP integration.
The `v4.0 question` entries are prompts for later gap analysis and Arc03,
without answering them prematurely.

## Cross-Document Shape

| Construct | v3.2 baseline | Primary source | v4.0 question |
|-----------|---------------|----------------|---------------|
| Concept card | Atomic unit with YAML frontmatter and Markdown body for humans and LLMs. | 0009 lines 22-33 | Should v4.0 distinguish card, claim, source span, extraction run, and memory admission as separate constructs? |
| Schema | v3 frontmatter and body template; v3.2 changes only paths and references. | 0009 lines 5-18; 0010 lines 7-19 | Which schema elements need typed validation rather than prose/checklist enforcement? |
| Workflow | Fresh extraction and re-extraction procedures over canonical Markdown sources. | 0009 lines 571-761 | What workflow states need to become explicit before cards enter durable substrate? |
| Parallel workflow | Four phases: requirements, analysis/planning, five-agent re-extraction, validation/preservation. | 0010 lines 24-31 | Does v4.0 need a separate reconciliation authority after parallel extraction? |
| Validation | Frontmatter/body checks, cross-reference checks, preservation checks, LLM artifact search, CQ coverage, and quality sampling. | 0009 lines 632-672; 0010 lines 625-733 | What should be machine schema, semantic QA, sampled audit, or operator judgment? |
| Provenance | Source title, slug, authors, chapter, page, section, source reference, and verification notes. | 0009 lines 81-89, 126-144, 438-470 | Should v4.0 model source spans and evidence grades separately from source citations? |
| Relationship | Four typed relationship fields plus explanatory body sections. | 0009 lines 183-207, 370-399; 0010 lines 868-874 | Which graph edges are needed for ontology critique, reconciliation, and retrieval? |
| Competency question | `answers_questions` per card; 30-50 CQs elicited and mapped for parallel runs. | 0009 lines 209-219; 0010 lines 143-190, 289-309 | Should CQs become both requirements and coverage tests with explicit status? |
| Confidence | `high`, `medium`, `low` based on source definition clarity. | 0009 lines 71-79; 0010 lines 860-866 | How should extraction confidence differ from evidence grade, verification status, and usability? |
| Re-extraction | Source-primary, old-card-secondary, v3-template target, preserve unique value. | 0009 lines 585-619; 0010 lines 534-551 | What trace should record old-card value, merge decisions, and rejected preservation candidates? |
| Preservation | Card-count comparison, content spot-checks, preservation notes, lost-content troubleshooting. | 0009 lines 621-629; 0010 lines 684-713, 778-796 | What level of preservation evidence is required before replacing durable cards? |
| Memory admission | Not explicitly modeled; validated cards become the effective durable substrate. | 0009 lines 632-672; 0010 lines 715-733 | What separates extracted content from admitted memory that future cognition may rely on? |
| CCDP | Not present in v3.2 baseline. | 0009 and 0010 no CCDP construct | How should cards represent claims, evidence, audit, and dispatchable cognitive services in CCDP terms? |

## Structure By Layer

### Layer 1: Source And Repository Placement

v3.2 baseline:

- Canonical input is converted Markdown under
  `knowledge/<kb>/sources/md/<source-slug>/`.
- Raw PDF, EPUB, and HTML sources may live under sibling format directories,
  but extractors read Markdown.
- Cards write to `knowledge/<kb>/concept-cards/<source-slug>/`.
- Extraction metadata writes to
  `knowledge/<kb>/extraction-metadata/<source-slug>/`.

Source anchors: 0009 lines 474-518; 0010 lines 35-91.

v4.0 question: Which of these are method concepts, which are package/path
constraints, and which belong to the eventual skill architecture?

### Layer 2: Concept Identification And Atomicity

v3.2 baseline:

- One concept per card is the first golden rule.
- Split when definitions, prerequisites, applications, or common confusions
  differ.
- Merge when the same concept appears in multiple contexts or is progressively
  elaborated.

Source anchors: 0009 lines 36-44, 764-781.

v4.0 question: What evidence should justify a split or merge decision, and how
should that decision be audited?

### Layer 3: Card Schema

v3.2 baseline:

- Frontmatter carries identity, classification, provenance, confidence,
  aliases, typed relationships, and competency-question links.
- Body sections carry definitions, prerequisites, properties, procedural
  knowledge, context, examples, relationship explanations, errors,
  confusions, source reference, and verification notes.

Source anchors: 0009 lines 92-219 and 222-470; 0010 lines 345-509.

v4.0 question: Which fields remain card-local, and which become separate
entities such as claim, source span, extraction run, evidence grade, or
verification result?

### Layer 4: Extraction Workflow

v3.2 baseline:

- Fresh extraction reads chapters, identifies concepts, determines tiers,
  extracts in dependency order, cross-references as it goes, and validates
  frontmatter/body completeness.
- Re-extraction adds old-card lookup, unique-value preservation, overwrite,
  and verification-note recording.

Source anchors: 0009 lines 571-629 and 737-761; 0010 lines 534-551.

v4.0 question: What workflow state machine, if any, should distinguish
candidate, extracted, validated, reconciled, operator-accepted, and admitted
cards?

### Layer 5: Parallel Coordination

v3.2 baseline:

- The coordinator audits the existing inventory, generates CQs, defines
  taxonomy and notation, analyzes source material, maps CQs, and creates
  exactly five balanced agent assignments.
- Agents receive scoped chapters, CQs, taxonomy, key concepts, paths, template,
  and quality requirements.

Source anchors: 0010 lines 95-236, 240-339, and 512-621.

v4.0 question: Is five-agent parallelism a reusable method rule, an example
operating recipe, or a parameterized coordination pattern?

### Layer 6: Validation And Quality Control

v3.2 baseline:

- Structural validation is primarily grep/checklist based.
- Slug/filename consistency, missing references, orphaned concepts, card count,
  lost unique content, CQ coverage, and semantic quality samples are checked
  after extraction.
- The method names common failure modes: low confidence, circular
  prerequisites, orphaned concepts, unanswered CQs, decreased card count, lost
  unique content, and wrong paths.

Source anchors: 0009 lines 632-854; 0010 lines 625-846.

v4.0 question: Which validation checks should become deterministic scripts,
which require semantic review, and which require operator acceptance?

## Baseline Constructs For Later Gap Analysis

| Category | v3.2 construct | Baseline status | Gap-analysis prompt |
|----------|----------------|-----------------|---------------------|
| schema | v3 frontmatter and body sections | Explicit and stable | Identify fields that mix multiple meanings. |
| workflow | fresh extraction | Explicit in 0009 | Decide whether fresh extraction needs run metadata. |
| workflow | re-extraction | Explicit in both docs | Decide how preservation evidence is recorded. |
| validation | quality checklist | Explicit but manual | Separate schema checks from semantic QA. |
| provenance | source metadata and source reference | Explicit | Decide whether source spans need first-class identity. |
| relationship | four typed relationships | Explicit | Test whether graph-native work needs more edge types or edge status. |
| competency question | card-level answers plus run-level CQ generation | Explicit | Decide whether CQ coverage should be machine-reportable. |
| confidence | `high` / `medium` / `low` | Explicit but flat | Separate confidence from evidence grade and verification status. |
| re-extraction | old-card preservation | Explicit | Decide how to audit merge decisions and discarded content. |
| preservation | card count and spot checks | Explicit | Decide whether preservation requires full diff evidence. |
| memory admission | not explicit | Implicit only | Define whether memory admission is a separate lifecycle state. |
| CCDP | not explicit | Absent | Decide how claim/provenance/audit semantics map to the method. |

## What This Slice Does Not Decide

- It does not design the v4.0 conceptual model.
- It does not choose the final v4.0 skill layout.
- It does not define memory admission rules.
- It does not define CCDP evidence semantics.
- It does not decide which validation checks become scripts.
- It does not edit or rewrite the v3.2 source documents.
