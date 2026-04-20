# A Guide for Parallel Concept Card Extraction (v3)

This guide documents how to extract concept cards from primary sources (books, handbooks, papers, repositories) that have been converted from PDF, LaTeX, or EPUB formats to Markdown, using Claude Code with Opus agents working in parallel.

Note that previous versions of this extraction process were initially defined and then later refined in the PoC project "AI Music Theory" (<https://github.com/music-comp/ai-music-theory>) and are documented in the design and developer docs in that repository.

Further: improvements introduced with v3 derive from analysis of previous versions against accepted best practices in the fields of ontology engineering, library science, and cognitive architecture. For more infornation, see selections in `./assets/papers` of this repository.

**Version 3 Changes:**

- Enhanced YAML frontmatter with confidence scoring, variant tracking, and typed relationships
- Improved body structure with explicit prerequisite chains and procedural/declarative separation
- Added competency question framework for scope definition and validation
- Added structural validation checks for post-processing

---

## Overview

This is a **three-phase process**:

1. **Phase 0: Requirements & Scope** - Define competency questions and domain customizations
2. **Phase 1: Analysis & Planning** - Analyze source material and create extraction plans
3. **Phase 2: Parallel Extraction** - Five Opus agents extract concept cards simultaneously

---

## Prerequisites

### 1. Environment Setup

- **Claude Code** installed and configured
- **Model access**: Coordinator should use **Opus model**, with access to spawn Opus agents
- **Source files** in place at `sources-md/<source-slug>/` with chapter/section files as `.md`
- **Output directory** ready at `concept-cards/<source-slug>/` (will be created if needed)

### 2. Directory Structure

Your project should follow this structure:

```
project-root/
├── sources-md/
│   └── <source-slug>/
│       ├── 00-frontmatter.md
│       ├── 01-introduction.md
│       ├── 02-chapter-two.md
│       └── ... (additional chapters/sections)
├── concept-cards/
│   └── <source-slug>/
│       └── (concept cards will be created here)
└── extraction-metadata/
    └── <source-slug>/
        ├── competency-questions.md
        └── extraction-log.md
```

### 3. Source Material Requirements

- Source must be split into logical divisions (chapters, sections, papers)
- Each division should be a separate `.md` file
- Files should be in a single directory: `sources-md/<source-slug>/`

---

## Phase 0: Requirements & Scope (NEW)

**Purpose**: Define what the knowledge base must accomplish before extracting anything.

### Step 0.1: Competency Question Elicitation

Before analyzing the source, identify **30-50 competency questions** the knowledge base should answer. Organize by type:

| Type | Count Target | Example |
|------|--------------|---------|
| Definitional | 10-15 | "What is a dominant seventh chord?" |
| Relational | 8-12 | "How does the dominant relate to the tonic?" |
| Procedural | 8-12 | "How do I construct a major scale?" |
| Prerequisite | 5-8 | "What must I know before learning sonata form?" |
| Diagnostic | 5-8 | "What distinguishes major from minor mode?" |

**Methods for generating CQs:**

1. Review source table of contents and chapter summaries
2. Identify learning objectives stated in the source
3. Consider typical user queries for this domain
4. Ask: "What questions would a learner at each level ask?"

Save to `extraction-metadata/<source-slug>/competency-questions.md`:

```markdown
# Competency Questions for <Source Title>

## Definitional (What is X?)
1. What is a major scale?
2. What is a chord inversion?
...

## Relational (How does X relate to Y?)
1. How does the subdominant function relate to the dominant?
...

## Procedural (How do I do X?)
1. How do I identify the key of a piece?
...

## Prerequisite (What before X?)
1. What concepts must I know before understanding secondary dominants?
...

## Diagnostic (What distinguishes X from Y?)
1. What is the difference between a half cadence and a deceptive cadence?
...
```

### Step 0.2: Domain Taxonomy

Define the category values for this domain. Categories should be:

- Mutually exclusive (each concept fits one primary category)
- Collectively exhaustive (every concept has a category)
- Hierarchical if needed (category + subcategory)

**Example for Music Theory:**

```
Categories:
- fundamentals (pitch, rhythm, notation basics)
- scales-modes (scale structures, mode relationships)
- intervals (interval types, qualities, recognition)
- chords (chord construction, types, inversions)
- harmony (harmonic function, progressions, voice leading)
- form (structural patterns, sections, large-scale organization)
- rhythm-meter (time signatures, rhythmic patterns)
- counterpoint (voice relationships, species)

Tiers:
- foundational (no prerequisites from this source)
- intermediate (requires foundational concepts)
- advanced (requires intermediate concepts)
```

### Step 0.3: Notation Conventions

Document domain-specific notation requirements:

```markdown
# Notation Conventions for <Source>

## Scale Degrees
- Use caret notation: ^1, ^2, ^3, ^4, ^5, ^6, ^7
- For chromatic alterations: ^♯4, ^♭7

## Chord Symbols
- Roman numerals: I, ii, iii, IV, V, vi, vii°
- Lead-sheet: Cmaj7, Dm7, G7

## Intervals
- Format: quality + number (e.g., M3, m7, P5, A4, d5)
```

---

## Phase 1: Analysis & Planning

**Model**: Use Opus for this phase

### Step 1.1: Initial Source Analysis

Use the **Explore agent** with "very thorough" mode:

```
Please analyze the source material in sources-md/<source-slug>/ to create a comprehensive concept extraction plan. Use very thorough exploration mode.
```

The analysis should produce:

1. **Source metadata:**
   - Full title, authors, publication type
   - Subject area and scope
   - PDF page numbers from chapter metadata headers

2. **Chapter inventory:**
   - Total chapters with titles and brief descriptions
   - Length/complexity assessment per chapter
   - PDF page numbers (from metadata headers)

3. **Concept inventory:**
   - Complete concept list per chapter
   - Estimated card counts (ranges)
   - Total estimated cards

4. **Categorization:**
   - Major thematic divisions
   - Category assignment per chapter
   - Tier assignment (foundational/intermediate/advanced)

5. **Cross-reference mapping:**
   - Concepts that appear in multiple chapters
   - Prerequisite chains visible in chapter sequencing

### Step 1.2: Competency Question Mapping

Map each competency question to the chapters/concepts that should answer it:

```markdown
# CQ-to-Chapter Mapping

## "What is a major scale?" (Definitional)
- Primary: Chapter 3 (Scales)
- Concepts needed: major-scale, scale-degree, whole-step, half-step

## "How do I construct a dominant seventh chord?" (Procedural)
- Primary: Chapter 7 (Seventh Chords)
- Concepts needed: dominant-seventh-chord, root, third, fifth, seventh, chord-construction
```

This mapping reveals:

- Extraction priorities (concepts that answer multiple CQs)
- Coverage gaps (CQs with no clear chapter mapping)
- Completeness requirements (all concepts needed per CQ)

### Step 1.3: Create Balanced Agent Assignments

Divide work among **exactly 5 agents**:

1. **Group chapters sequentially** — maintain order, no gaps
2. **Balance workload** — aim for ±20% card count variance
3. **Respect natural divisions** — don't split major themes across agents
4. **Match competency coverage** — each agent should address some CQs fully

**Assignment verification checklist:**

- [ ] Every chapter assigned to exactly one agent
- [ ] No gaps in chapter ranges
- [ ] Card count estimates balanced (±20%)
- [ ] Each agent has clear thematic coherence
- [ ] CQ coverage distributed across agents

### Step 1.4: Compile Agent Instructions

For each agent, compile:

1. **Chapter assignments** with titles and page numbers
2. **Category guidance** for their chapters
3. **Tier assignments** for expected concept levels
4. **Domain-specific notes** (notation, terminology)
5. **CQs to address** (the questions their concepts should answer)
6. **Cross-reference alerts** (concepts shared with other agents' chapters)

---

## Phase 2: Parallel Extraction

### Concept Card Template (v3)

```markdown
---
# === CORE IDENTIFICATION ===
concept: [Concept Name - properly capitalized]
slug: [lowercase-hyphenated-filename-without-extension]

# === CLASSIFICATION ===
category: [primary category from domain taxonomy]
subcategory: [optional: more specific classification]
tier: [foundational/intermediate/advanced]

# === PROVENANCE ===
source: <SourceTitle>
source_slug: <SourceSlug>
authors: <AuthorList>
chapter: "<ChapterTitle>"
chapter_number: [number]
pdf_page: [PDF page number, or null]
section: [section heading if identifiable, or null]

# === CONFIDENCE ===
extraction_confidence: [high/medium/low]
# high: Concept explicitly defined in source
# medium: Concept present but requires synthesis
# low: Concept inferred from context

# === VARIANTS (authority control) ===
# Quote any alias containing a colon — YAML treats `key: value` as a mapping.
aliases:
  - [alternative name]
  - [abbreviated form]
  - [notational form]

# === TYPED RELATIONSHIPS ===
prerequisites:
  - [concept-slug-that-must-be-known-first]
extends:
  - [concept-slug-this-builds-upon]
related:
  - [associated-concept-slug]
contrasts_with:
  - [commonly-confused-concept-slug]

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is [concept]?"
  - [other CQs this card helps answer]
---

# Quick Definition

[1-2 sentence accessible definition for quick reference. Write for someone who needs a reminder, not a full explanation.]

# Core Definition

[Precise technical definition with proper terminology. This is the authoritative reference definition from the source. Quote directly where possible.]

# Prerequisites

[List concepts that must be understood before this one. For each, briefly state WHY it's needed:]

- **[Prerequisite Concept]** — [What knowledge it provides that this concept requires]
- **[Another Prerequisite]** — [Rationale]

[For foundational concepts with no prerequisites, state: "This is a foundational concept with no prerequisites within this source."]

# Key Properties

[Enumerate the defining characteristics—what makes this concept what it is:]

1. [Property 1]
2. [Property 2]
3. [Property 3]

# Construction / Recognition

[Procedural knowledge: How to build, identify, or apply this concept.]

## To Construct/Create:
1. [Step 1]
2. [Step 2]
3. [Step 3]

## To Identify/Recognize:
1. [Recognition step 1]
2. [Recognition step 2]

[If construction/recognition doesn't apply, explain the typical procedure or workflow involving this concept.]

# Context & Application

[When, where, and why this concept is used. Be specific to the domain:]

- **Typical contexts**: [Where this appears]
- **Common applications**: [How it's used]
- **Historical/stylistic notes**: [If relevant]

# Examples

[Specific examples FROM THE SOURCE TEXT. Always cite page/section. Avoid generic examples.]

**Example 1** (p. XX): [Description of example from source]

**Example 2** (p. XX): [Another example from source]

## Worked Example

[If the source provides a step-by-step walkthrough, include it here:]

1. [Step from source's worked example]
2. [Next step]
3. [Result]

# Relationships

## Builds Upon
[Concepts this one extends or elaborates:]
- **[Concept]** — [How this concept elaborates it]

## Enables
[Concepts that require this one as foundation:]
- **[Concept]** — [Why this is a prerequisite for it]

## Related
[Associated concepts, non-hierarchical:]
- **[Concept]** — [Nature of the relationship]

## Contrasts With
[Commonly confused concepts and distinguishing features:]
- **[Concept]** — [Key difference to remember]

# Common Errors

[Practical mistakes when APPLYING this concept:]

- **Error**: [What people do wrong]
  **Correction**: [How to do it correctly]

- **Error**: [Another mistake]
  **Correction**: [Fix]

# Common Confusions

[Conceptual misunderstandings about what this concept IS:]

- **Confusion**: [What people wrongly believe]
  **Clarification**: [The correct understanding]

# Source Reference

Chapter <ChapterNum>: <ChapterTitle>, [Section X.X if applicable], pages XX-XX.

[Include specific figure, table, or example references if the source provides them.]

# Verification Notes

[INTERNAL - for extraction quality tracking:]

- Definition source: [Direct quote from p. X / Synthesized from pp. X-Y / Inferred]
- Confidence rationale: [Why high/medium/low]
- Uncertainties: [Any aspects that need expert review]
- Cross-reference status: [Verified concept names exist / Unverified]
```

### Agent Prompt Template

```
Extract concept cards from "<SourceTitle>" Chapters <ChStart>-<ChEnd> (<ChGroupName>).

## Your Scope

Chapters <ChStart>-<ChEnd>:
- Ch <ChStart>: <ChapterTitle> (pdf p. XX)
- Ch <ChStart+1>: <ChapterTitle> (pdf p. XX)
... [list all chapters]
- Ch <ChEnd>: <ChapterTitle> (pdf p. XX)

**Target**: ~<EstimatedCardRangeTotal> concept cards

## Paths

- **Source files**: `sources-md/<SourceSlug>/`
- **Output directory**: `concept-cards/<SourceSlug>/`

## Competency Questions to Address

Your extracted concepts should help answer these questions:
<CQsForThisAgent>

## Taxonomy for Your Chapters

Categories to use:
- <category1>: [description]
- <category2>: [description]

Tiers:
- foundational: Chapters X-Y
- intermediate: Chapters Z
- advanced: Chapter W

## Concept Card Template

[Insert the v2 template from above]

## Key Concepts to Extract

- Ch <ChStart>: <ListOfConcepts> (~<EstimatedCardRangeCh> cards)
- Ch <ChStart+1>: <ListOfConcepts> (~<EstimatedCardRangeCh> cards)
... [all chapters]

## Important Notes

<ImportantNotes>

## Extraction Guidelines

1. **One concept per card** — Don't combine related concepts
2. **Confidence scoring** — Assign high/medium/low based on:
   - High: Explicit definition in source
   - Medium: Concept present but requires synthesis
   - Low: Inferred from context
3. **Collect variants** — Note abbreviations, alternative names, notational forms. **Quote any value containing a colon** (e.g., `"Kotlin variant: panache-kotlin"`) to prevent YAML from parsing it as a mapping.
4. **Type relationships** — Distinguish prerequisites/extends/related/contrasts
5. **Source-specific examples** — Use examples from the text, not generic ones
6. **Prerequisites explicit** — Every non-foundational concept needs prerequisites
7. **CQ linkage** — Note which questions each card helps answer
8. **Cross-reference by slug** — Use exact concept slugs for relationship fields

## Quality Requirements

Each card MUST have:
- [ ] All frontmatter fields populated (use null/empty array where N/A)
- [ ] Quick Definition ≤ 2 sentences
- [ ] Core Definition with source attribution
- [ ] At least one example from source text
- [ ] Prerequisites section (even if "foundational, no prerequisites")
- [ ] At least one competency question in `answers_questions`
- [ ] Confidence rationale in Verification Notes

## File Naming

- Filename: `[slug].md` (lowercase, hyphenated, no numerical prefix)
- ✅ `major-scale.md`, `dominant-seventh-chord.md`
- ❌ `001-major-scale.md`, `Major_Scale.md`, `chord.yaml`

Work systematically through each chapter. Prioritize quality over speed.
```

**Model:** opus

---

## Post-Processing & Validation

### Structural Validation Checklist

After extraction, verify:

**Completeness Checks:**

```bash
# Check all cards have required frontmatter
for file in concept-cards/<source-slug>/*.md; do
  grep -q "^concept:" "$file" || echo "Missing concept: $file"
  grep -q "^extraction_confidence:" "$file" || echo "Missing confidence: $file"
  grep -q "^prerequisites:" "$file" || echo "Missing prerequisites: $file"
done
```

**Consistency Checks:**

```bash
# Extract all slugs
ls concept-cards/<source-slug>/*.md | xargs -n1 basename | sed 's/.md$//' > /tmp/slugs.txt

# Extract all referenced concepts from prerequisites/extends/related fields
grep -h "^  - " concept-cards/<source-slug>/*.md | sed 's/^  - //' > /tmp/refs.txt

# Find references to non-existent concepts
comm -23 <(sort /tmp/refs.txt | uniq) <(sort /tmp/slugs.txt)
```

**Orphan Detection:**

```bash
# Concepts with no incoming relationships (never referenced as prerequisite/related)
# and no outgoing relationships (empty relationship fields)
# These may be legitimate foundational concepts OR extraction gaps
```

**CQ Coverage Check:**
For each competency question, verify that:

1. At least one concept card lists it in `answers_questions`
2. The card(s) actually contain enough information to answer it

### Quality Verification Sampling

Sample 3-5 cards from each agent and verify:

- [ ] Definitions accurate to source
- [ ] Confidence scoring justified in Verification Notes
- [ ] Prerequisites form valid chains (no circular dependencies)
- [ ] Examples cite specific source locations
- [ ] Variants capture alternative terminology
- [ ] Relationships use valid slugs

---

## Troubleshooting

### Issue: Low confidence scores across many cards

**Cause**: Source doesn't provide explicit definitions (common in advanced texts)

**Solution**:

- Accept medium confidence as normal for synthesis-heavy sources
- Flag low confidence cards for expert review
- Consider adding competency questions that match source's implicit assumptions

### Issue: Circular prerequisites detected

**Cause**: Mutually dependent concepts extracted without proper ordering

**Solution**:

- Identify the foundational concept in the cycle
- Mark it as foundational (no prerequisites)
- Re-run affected agent with guidance on which concept is base

### Issue: Many orphaned concepts

**Cause**: Insufficient relationship extraction

**Solution**:

- Review orphans—are they truly isolated or missing relationships?
- Re-extract with explicit instruction to connect each concept
- Some foundational concepts legitimately have only outgoing edges

### Issue: Competency questions unanswered

**Cause**: Coverage gap—needed concepts not extracted

**Solution**:

- Map unanswered CQs to source sections
- Re-extract from those sections with specific CQ guidance
- If source doesn't cover the CQ, document as out-of-scope

---

## Workflow Summary

### Phase 0: Requirements (30-60 minutes)

1. ✅ Generate 30-50 competency questions
2. ✅ Define domain taxonomy (categories, tiers)
3. ✅ Document notation conventions
4. ✅ Save to `extraction-metadata/<source-slug>/`

### Phase 1: Analysis (20-30 minutes)

1. ✅ Run Explore agent on source
2. ✅ Map CQs to chapters/concepts
3. ✅ Create 5 balanced agent assignments
4. ✅ Compile agent-specific instructions
5. ✅ Verify assignments (no gaps, balanced, CQ coverage)

### Phase 2: Extraction (20-40 minutes)

1. ✅ Launch all 5 agents in parallel
2. ✅ Monitor for completion
3. ✅ Run post-processing cleanup

### Phase 3: Validation (15-30 minutes)

1. ✅ Run structural validation checks
2. ✅ Check consistency (valid slugs, no orphans)
3. ✅ Verify CQ coverage
4. ✅ Sample quality check (3-5 cards per agent)
5. ✅ Re-extract if needed

**Total: ~90-160 minutes** for complete, validated extraction

---

## Version History

- **v1**: Original template (basic frontmatter, no relationships)
- **v2**: Updated for use in graph databases and for improving full text search (flat relationships)
- **v3**: Enhanced with confidence scoring, authority control, typed relationships, CQ framework, structural validation

---

## Appendix: Quick Reference

### Confidence Scoring

| Level | Criteria |
|-------|----------|
| High | Source explicitly defines concept; extraction is straightforward |
| Medium | Concept discussed but not formally defined; requires synthesis |
| Low | Concept inferred or reconstructed from context |

### Relationship Types

| Type | Direction | Semantics |
|------|-----------|-----------|
| prerequisites | Incoming | Must know this first |
| extends | Outgoing | This builds upon |
| related | Symmetric | Associated, non-hierarchical |
| contrasts_with | Symmetric | Often confused with |

### Required Frontmatter Fields

```yaml
concept:              # REQUIRED
slug:                 # REQUIRED
category:             # REQUIRED
tier:                 # REQUIRED
source:               # REQUIRED
chapter:              # REQUIRED
chapter_number:       # REQUIRED
extraction_confidence: # REQUIRED
aliases:              # REQUIRED (empty array if none)
prerequisites:        # REQUIRED (empty array if foundational)
answers_questions:    # REQUIRED (at least one CQ)
```
