# Visual Design Concept Card Extraction Prompt

**Copy this prompt and fill in the bracketed fields for each new source.**

---

## Prompt

You are extracting concept cards from a visual design source text. This extraction is part of a larger knowledge engineering project that builds a queryable, graph-backed knowledge base for visual design — with the same rigour applied to our mathematics and music theory knowledge bases.

### Source to Process

- **Source title**: [TITLE]
- **Authors**: [AUTHORS]
- **Source slug**: [source-slug]
- **Source location**: `sources-md/[source-slug]/`
- **Output location**: `concept-cards/visual-design/`
- **Extraction wave**: [1/2/3/4] (see `crates/design/dev/0009-phase-0-section-6-source-prioritisation-and-extraction-order.md` for wave context)

### What This Source Covers

[2-4 sentences describing what this source contributes and what categories/tiers to expect. Copy the relevant entry from 0009's source-specific extraction notes, or write your own if the source isn't listed.]

### Process Overview

This extraction combines a general methodology with domain-specific requirements. You have two process documents and a domain specification. **Do not load all of them at once.** Follow the phased reading order below — each phase tells you exactly which files to read and what to do with them.

---

## Phase 1: Understand the Domain Requirements

**Read these files first** (in this order):

1. `crates/design/dev/0004-phase-0-section-1-background.md` — Understand the target user and why this project exists. This shapes every extraction decision.
2. `crates/design/dev/0005-phase-0-section-2-domain-taxonomy.md` — The 13 categories across 4 layers. Every concept card gets exactly one `category` from this taxonomy. Pay close attention to the orthogonality notes and cross-cutting concept specifications.
3. `crates/design/dev/0006-phase-0-section-3-tier-definitions.md` — Foundational / intermediate / advanced criteria, plus the per-category tier assignment table.
4. `crates/design/dev/0007-phase-0-section-4-competency-questions.md` — The 55 competency questions. Every card must list at least one in `answers_questions`. Note the high-priority CQs in Section 4.4.

**After reading these four files**, you should be able to answer:

- What categories exist and what each one covers
- What tier a given concept likely belongs to
- What questions the knowledge base must answer
- Who the target user is and what makes their needs unique

**You do not need to hold these files in context for the rest of the process** — they establish your mental model. You can re-read specific sections as needed during extraction.

## Phase 2: Understand the Extraction Methodology

**Read these files next:**

1. `crates/design/dev/concept-cards/0002-a-guide-for-parallel-concept-card-extraction-v3.md` — The general extraction methodology. This defines the three-phase process (Phase 0/1/2), the concept card template, the parallel agent architecture, and post-processing validation. **You are executing Phase 1 (analysis & planning) and Phase 2 (extraction) of this document.** Phase 0 is already complete — that's what files 0004-0014 represent.
2. `crates/design/dev/concept-cards/0003-howto-concept-card-extraction-with-claude-code.md` — Practical guidance on card quality: the golden rules (one concept per card, source-faithful not source-copied, explicit relationships, confidence scoring, provenance), field-by-field frontmatter guidance, body section best practices, and the quality checklist.

**Key integration point**: The general methodology (0002) defines the base concept card template. The domain specification adds visual-design-specific extensions. Use the **combined template** specified in Phase 4 below.

## Phase 3: Read Domain-Specific Extraction Instructions

**Read these files for extraction-time reference:**

1. `crates/design/dev/0008-phase-0-section-5-notation-conventions.md` — How to notate colour (OKLCH + hex), typography (modular scales, fluid type), spacing (4pt/8pt, t-shirt sizing), responsive design, and mathematical formulations. Follow these conventions in every card.
2. `crates/design/dev/0012-phase-0-section-9-extraction-specific-instructions.md` — The concept card template extensions (`layer`, `rosetta_stone`, `css_implementation` fields) and the six domain-specific agent instructions (always note mathematical formulations, always note CSS implementations, check Rosetta Stone mappings, etc.).
3. `crates/design/dev/0010-phase-0-section-7-the-rosetta-stone-framework.md` — The cross-domain mapping tables. During extraction, check each concept against these tables. If a mapping exists, include it in the card's `rosetta_stone` frontmatter field and Context & Application section.

**Keep file 0010 (Rosetta Stone) accessible for lookup during extraction** — you'll reference it repeatedly.

## Phase 4: Analyse the Source and Plan Extraction

Now apply the Phase 1 process from the general methodology (0002, Section "Phase 1: Analysis & Planning") to the source material.

### Step 4.1: Analyse the Source

Read through `sources-md/[source-slug]/` to produce:

1. **Source metadata** — title, authors, publication type, subject area, scope
2. **Chapter/section inventory** — all divisions with titles, descriptions, and complexity assessment
3. **Concept inventory** — complete concept list per chapter with estimated card counts
4. **Category assignment** — map each chapter's concepts to taxonomy categories (from 0005)
5. **Tier assignment** — assign foundational/intermediate/advanced (from 0006)
6. **Cross-reference mapping** — concepts appearing in multiple chapters, prerequisite chains

### Step 4.2: Map Competency Questions

Map the competency questions (from 0007) to the concepts you've identified:

- Which CQs does this source help answer?
- Which concepts are needed for each CQ?
- Are any high-priority CQs (Section 4.4) addressed by this source?
- Are there coverage gaps — CQs this source *should* address but doesn't seem to?

### Step 4.3: Create Agent Assignments

Divide the work among **5 parallel agents** following the methodology in 0002:

- Group chapters sequentially, no gaps
- Balance workload (±20% card count variance)
- Respect natural thematic divisions
- Distribute CQ coverage across agents
- Verify: every chapter assigned, no gaps, balanced counts

### Step 4.4: Compile Agent-Specific Instructions

For each agent, prepare:

1. Chapter assignments with titles
2. Category guidance (which taxonomy categories to use)
3. Tier assignments
4. CQs to address
5. Cross-reference alerts (concepts shared with other agents' chapters)
6. Source-specific notes (see 0009 for this source's notes, if available)

**Include the combined concept card template** (below) in each agent's instructions.

## Phase 5: Extract

Launch the 5 agents with their compiled instructions. Each agent extracts concept cards following the combined template below.

### Combined Concept Card Template

This merges the v3 base template (from 0002) with the visual design extensions (from 0012):

```markdown
---
# === CORE IDENTIFICATION ===
concept: [Concept Name - properly capitalised]
slug: [lowercase-hyphenated]

# === CLASSIFICATION ===
category: [from 0005 taxonomy - one of: visual-elements, visual-perception, design-principles, colour-theory, typography, layout-composition, interaction-design, motion-design, information-architecture, data-visualisation, imagery, design-systems, accessibility, visual-identity]
subcategory: [optional finer classification]
tier: [foundational/intermediate/advanced - per 0006 criteria]
layer: [0-perception/1-principles/2-domain/3-implementation]

# === PROVENANCE ===
source: "[Source Title]"
source_slug: [source-slug]
authors: "[Authors]"
chapter: "[Chapter Title]"
chapter_number: [number]
pdf_page: [page number or null]
section: [section heading or null]

# === CONFIDENCE ===
extraction_confidence: [high/medium/low]

# === VARIANTS ===
aliases:
  - [alternative names, abbreviations, notational forms]

# === TYPED RELATIONSHIPS ===
prerequisites:
  - [concept-slug]
extends:
  - [concept-slug]
related:
  - [concept-slug]
contrasts_with:
  - [concept-slug]

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "[CQ from 0007 that this card helps answer]"

# === VISUAL DESIGN EXTENSIONS (optional) ===
rosetta_stone:
  - domain: [engineering/music/mathematics/art]
    concept: "[concept name in source domain]"
    rating: [rigorous/structural/loose]
    note: "[brief description]"

css_implementation:
  - property: "[CSS property or technique]"
    example: "property: value;"
    support: [baseline/partial/experimental]
---

# Quick Definition

[1-2 sentences. Maximum. For quick reference.]

# Core Definition

[Precise technical definition with source attribution. Quote directly where the source provides a clear definition.]

# Prerequisites

- **[Prerequisite]** — [Why it's needed]

[Or: "This is a foundational concept with no prerequisites within this source."]

# Key Properties

1. [Property 1]
2. [Property 2]
3. [Property 3]

# Construction / Recognition

## To Construct/Create:
1. [Step]

## To Identify/Recognise:
1. [Step]

# Context & Application

- **Typical contexts**: [Where this appears]
- **Common applications**: [How it's used]

## Cross-Domain Connections

[If rosetta_stone entries exist, expand them here:]

**[Source Domain] → [Rating]**: [Description of the mapping and why it holds or where it breaks down.]

# Examples

**Example 1** (p. XX): [From the source text, with citation]

## Worked Example

[If the source provides step-by-step, include it here]

# Relationships

## Builds Upon
- **[Concept]** — [How]

## Enables
- **[Concept]** — [Why]

## Related
- **[Concept]** — [Nature of relationship]

## Contrasts With
- **[Concept]** — [Key difference]

# Common Errors

- **Error**: [Procedural mistake]
  **Correction**: [Fix]

# Common Confusions

- **Confusion**: [Conceptual misunderstanding]
  **Clarification**: [Correct understanding]

# Source Reference

Chapter X: [Title], Section X.X, pages XX-XX.

# Verification Notes

- Definition source: [Direct quote from p. X / Synthesised from pp. X-Y / Inferred]
- Confidence rationale: [Why high/medium/low]
- Uncertainties: [Aspects needing review]
- Cross-reference status: [Verified / Unverified]
- Rosetta Stone check: [Checked against 0010 tables / No mappings found]
```

### Agent-Level Quality Requirements

Each agent MUST ensure every card has:

- [ ] All required frontmatter fields populated (use null/empty array where N/A)
- [ ] `category` is from the 0005 taxonomy (exact slug match)
- [ ] `layer` matches the category's layer assignment in 0005
- [ ] `tier` is consistent with the 0006 tier table for this category
- [ ] Quick Definition ≤ 2 sentences
- [ ] Core Definition with source attribution
- [ ] At least one example from the source text with page citation
- [ ] Prerequisites section (even if "foundational, no prerequisites")
- [ ] At least one CQ from 0007 in `answers_questions`
- [ ] `rosetta_stone` field populated if concept appears in 0010 mapping tables
- [ ] `css_implementation` field populated if concept has a CSS realisation
- [ ] Mathematical formulation included if one exists (per 0008 notation conventions)
- [ ] Verification Notes with confidence rationale and Rosetta Stone check confirmation

### File Naming

- Filename: `[slug].md` (lowercase, hyphenated, no numerical prefix)
- Output to: `concept-cards/visual-design/`
- ✅ `visual-hierarchy.md`, `modular-type-scale.md`, `gestalt-proximity.md`
- ❌ `001-visual-hierarchy.md`, `Visual_Hierarchy.md`

## Phase 6: Validate

After all agents complete, run the validation process from 0002 (Post-Processing & Validation) **plus** the domain-specific validation from `crates/design/dev/0013-phase-0-section-10-validation-criteria.md`.

### Structural Validation

```bash
# Required frontmatter check
for file in concept-cards/visual-design/*.md; do
  grep -q "^concept:" "$file" || echo "MISSING concept: $file"
  grep -q "^category:" "$file" || echo "MISSING category: $file"
  grep -q "^tier:" "$file" || echo "MISSING tier: $file"
  grep -q "^layer:" "$file" || echo "MISSING layer: $file"
  grep -q "^extraction_confidence:" "$file" || echo "MISSING confidence: $file"
done
```

### Consistency Validation

```bash
# Valid category check
VALID_CATS="visual-elements visual-perception design-principles colour-theory typography layout-composition interaction-design motion-design information-architecture data-visualisation imagery design-systems accessibility visual-identity"
for file in concept-cards/visual-design/*.md; do
  cat=$(grep "^category:" "$file" | sed 's/^category: *//')
  echo "$VALID_CATS" | grep -qw "$cat" || echo "INVALID category '$cat' in $file"
done

# Slug-to-filename match
for file in concept-cards/visual-design/*.md; do
  slug=$(grep "^slug:" "$file" | sed 's/^slug: *//')
  expected="$(basename "$file" .md)"
  [ "$slug" != "$expected" ] && echo "MISMATCH: slug '$slug' vs filename '$expected' in $file"
done

# Dangling relationship references
ls concept-cards/visual-design/*.md | xargs -n1 basename | sed 's/.md$//' | sort > /tmp/existing-slugs.txt
grep -h "^  - " concept-cards/visual-design/*.md | sed 's/^  - //' | sort -u > /tmp/all-refs.txt
comm -23 /tmp/all-refs.txt /tmp/existing-slugs.txt | head -20
```

### Domain-Specific Validation (from 0013)

- [ ] Every taxonomy category has at least 3 concept cards from this source (where the source covers that category)
- [ ] Cross-cutting concepts in `design-principles` link to domain-specific cards via `related`
- [ ] High-priority CQs addressed by this source have at least one card in `answers_questions`
- [ ] Every RIGOROUS Rosetta Stone mapping relevant to this source appears in at least one card
- [ ] Layer integrity: no Layer 0 card has prerequisites from Layer 2 or 3
- [ ] No circular prerequisites

### Quality Sampling

Sample 3-5 cards from each agent and verify:

- [ ] Definitions accurate to source
- [ ] Confidence scoring justified
- [ ] Prerequisites form valid chains
- [ ] Examples cite specific source locations
- [ ] Rosetta Stone mappings correctly rated (RIGOROUS/STRUCTURAL/LOOSE)

---

## Context Management Notes

**To stay within context limits:**

- Load Phase 1 files (0004-0007) for planning, then release them before extraction
- During extraction, agents need only: the source chapters they're assigned, the combined template (above), their agent-specific instructions, and file 0010 (Rosetta Stone) for lookup
- Do NOT load the full Phase 0 spec into every agent — the agent instructions compiled in Phase 4 should contain everything each agent needs
- If an agent needs to verify a taxonomy category or tier assignment, re-read just the relevant section of 0005 or 0006, not the entire file
- Post-validation (Phase 6) needs only the output cards and the validation scripts — not the source material

**To maintain quality:**

- Extract in dependency order within each agent's chapters (foundational concepts first)
- When uncertain about category assignment, check the scope descriptions in 0005
- When uncertain about tier, check the per-category table in 0006
- When uncertain about a Rosetta Stone mapping's rigour rating, check the criteria in 0010 Section 7.2
- When a concept is discussed across multiple chapters, create ONE card citing all locations (see "When to Create Multiple Cards" in 0003)
- Never invent examples — if the source doesn't provide one, state that explicitly

---

## Checklist Before Starting

- [ ] Source files are in `sources-md/[source-slug]/` as chapter-level `.md` files
- [ ] Output directory `concept-cards/visual-design/` exists
- [ ] You've filled in all bracketed fields at the top of this prompt
- [ ] You've read the source-specific notes in 0009 (if this source is listed)
- [ ] You understand the target user (senior engineer, art background, mathematical, needs vocabulary + systems)

Begin with Phase 1.
