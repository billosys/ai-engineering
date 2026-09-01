# Concept Card Framework: Immediate Improvements Report

## Executive Summary

This report synthesizes actionable recommendations from the critical assessment and response papers to improve concept card extraction quality. The focus is on changes that can be implemented immediately within the existing framework—deeper architectural changes (like full Knowledge Space Theory verification or OntoClean integration) are deferred to future iterations.

---

## Part 1: Frontmatter / Metadata Improvements

### Current State

The existing YAML frontmatter captures:

```yaml
concept: [Concept Name]
category: [theory/technique/analysis/form/application]
source: [Source Title]
chapter: [Chapter Title]
chapter_number: [number]
pdf_page: [number or null]
unit: [number or null]
authors: [Author List]
```

### Identified Gaps (from Critical Assessment)

1. **No confidence scoring** — All extracted concepts carry equal implicit confidence regardless of extraction clarity or source attestation
2. **No variant tracking** — No mechanism to capture alternative names, abbreviations, or notational forms (authority control gap)
3. **Sparse relation inventory** — The "Related Concepts" section conflates multiple relationship types into an undifferentiated list
4. **No competency question linkage** — No connection between cards and the queries they should answer
5. **Missing provenance granularity** — `pdf_page` is chapter-level; no section or paragraph-level tracking

### Recommended Frontmatter Extensions

```yaml
---
# === CORE IDENTIFICATION ===
concept: [Concept Name - properly capitalized]
slug: [lowercase-hyphenated-filename-without-extension]

# === CLASSIFICATION ===
category: [primary category from domain taxonomy]
subcategory: [optional: more specific classification]
tier: [foundational/intermediate/advanced - based on prerequisite depth]

# === PROVENANCE (enhanced) ===
source: [Source Title]
source_slug: [source-directory-slug]
authors: [Author List]
chapter: [Chapter Title]
chapter_number: [number]
pdf_page: [PDF page number from chapter metadata, or null]
section: [Section heading if identifiable, or null]

# === CONFIDENCE (new) ===
extraction_confidence: [high/medium/low]
# high: Concept clearly defined in source with explicit terminology
# medium: Concept present but requires interpretation/synthesis
# low: Concept inferred or reconstructed from partial information

# === VARIANTS (new - authority control) ===
aliases:
  - [alternative name 1]
  - [abbreviated form]
  - [notational form if applicable]
  - [common misspelling if known]

# === RELATIONSHIPS (typed - new) ===
prerequisites:
  - [concepts that must be understood before this one]
extends:
  - [concepts this one builds upon or elaborates]
related:
  - [concepts with non-hierarchical relationships]
contrasts_with:
  - [commonly confused concepts to distinguish]

# === COMPETENCY QUESTIONS (new) ===
answers_questions:
  - [What questions does this card help answer?]
  - [e.g., "What is the structure of a major scale?"]
---
```

### Implementation Notes

**Extraction Confidence Criteria:**

- **High**: The source explicitly defines the concept with clear terminology; extraction is straightforward
- **Medium**: The concept is discussed but not explicitly defined; extraction requires synthesis across paragraphs
- **Low**: The concept is implied or must be reconstructed from context; extraction involves interpretation

**Variant Collection Strategy:**
During extraction, prompt the LLM to identify:

1. Formal name (for `concept` field)
2. Abbreviated forms (e.g., "V7" for "dominant seventh chord")
3. Alternative terminology (e.g., "major-minor seventh" for "dominant seventh")
4. Notational representations (e.g., "^7" in music theory)
5. Common misspellings (populated post-hoc from search analytics)

**Relationship Typing:**
Replace the single "Related Concepts" list with typed fields:

- `prerequisites`: Strict dependency (must know X before Y)
- `extends`: Elaboration relationship (Y builds on X)
- `related`: Non-hierarchical association
- `contrasts_with`: Disambiguation relationship (X is often confused with Y)

---

## Part 2: Body Content Quality Improvements

### Current Template Sections

```markdown
# Quick Definition
# Formal Definition
# Construction/Recognition
# Context/Application
# Examples
# Related Concepts
# Common Confusions
# Source Reference
```

### Identified Gaps (from Critical Assessment)

1. **No distinction between declarative and procedural knowledge** — The card mixes "what is X" with "how to use X" without clear separation
2. **Related Concepts is unstructured** — A flat list that doesn't capture relationship types
3. **No verification markers** — No indication of which assertions are directly quoted vs. synthesized
4. **Missing prerequisite chain visibility** — No clear "what to learn before this" guidance
5. **No common errors/pitfalls section** — "Common Confusions" focuses on conceptual misunderstanding, not practical mistakes

### Recommended Body Structure

```markdown
# Quick Definition
[1-2 sentence accessible definition for quick reference]

# Core Definition
[Precise technical/academic definition with proper terminology. This is the authoritative definition from the source.]

# Prerequisites
[Explicit list of concepts that should be understood before this one, with brief rationale for each dependency]

# Key Properties
[Enumerated properties, characteristics, or rules that define the concept—what makes it what it is]

# Construction / Recognition
[Procedural knowledge: How to build, construct, identify, or apply this concept. Use numbered steps where appropriate.]

# Context & Application
[When, where, and why this concept is used. Domain-specific contexts and typical use cases.]

# Examples
[Specific examples from the source text. Include page/section references. Avoid generic examples—use what the source provides.]

## Worked Example (if applicable)
[Step-by-step walkthrough of applying the concept, drawn from source material]

# Relationships
## Builds Upon
[Concepts this one extends or elaborates—the "parent" concepts]

## Enables
[Concepts that build upon this one—what learning this unlocks]

## Related
[Non-hierarchical associations—concepts often discussed together]

## Contrasts With
[Commonly confused concepts and how to distinguish them]

# Common Errors
[Practical mistakes when applying the concept, not just conceptual misunderstandings]

# Common Confusions
[Conceptual misunderstandings—what people often get wrong about what this IS]

# Source Reference
[Full citation: Chapter X: Title, Section Y, pages Z. Include any specific paragraph or figure references.]

# Verification Notes (internal)
[For extraction tracking: What was directly stated vs. synthesized? Any uncertainties?]
```

### Section-by-Section Guidance

**Quick Definition vs. Core Definition:**

- Quick Definition: For rapid lookup, written for someone who needs a reminder
- Core Definition: The authoritative technical definition, suitable for formal reference

**Prerequisites Section:**
This directly addresses the Knowledge Space Theory alignment. Each prerequisite should:

- Name the required concept (using exact card names for linking)
- Briefly state WHY it's a prerequisite (what knowledge it provides)

Example:

```markdown
# Prerequisites
- **Interval** — Understanding interval quality (major, minor, perfect) is necessary to construct triads
- **Scale degrees** — Triad construction references scale degree positions
```

**Key Properties:**
Enumerate the defining characteristics. This supports the declarative knowledge function.

Example for "Major Triad":

```markdown
# Key Properties
1. Contains exactly three distinct pitch classes
2. Built from root, major third (4 semitones), and perfect fifth (7 semitones)
3. The interval between root and third is a major third
4. The interval between third and fifth is a minor third
5. Classified as a consonant sonority in common-practice harmony
```

**Construction / Recognition:**
This is the procedural knowledge section. Use explicit steps.

Example:

```markdown
# Construction / Recognition

## To Construct a Major Triad:
1. Start with the root note
2. Add the note a major third (4 semitones) above the root
3. Add the note a perfect fifth (7 semitones) above the root

## To Recognize a Major Triad:
1. Identify the three pitch classes
2. Arrange in close position (within one octave)
3. Check: Is the bottom interval a major third?
4. Check: Is the top interval a minor third?
5. If both yes → major triad
```

**Relationships Section:**
Structured to support graph construction with typed edges:

- "Builds Upon" → `extends` edge in graph
- "Enables" → inverse of `prerequisite_of`
- "Related" → `related` edge
- "Contrasts With" → `contrasts_with` edge

**Common Errors vs. Common Confusions:**

- Common Errors: Practical mistakes in application (e.g., "Forgetting to raise the leading tone in melodic minor ascending")
- Common Confusions: Conceptual misunderstandings (e.g., "Confusing harmonic minor with melodic minor")

**Verification Notes:**
Internal section for quality tracking:

```markdown
# Verification Notes
- Core definition: Direct quote from p. 47
- Key Properties 1-3: Explicit in source
- Key Property 4: Synthesized from context on p. 48-49
- Construction steps: Adapted from source's worked example
- Extraction confidence: HIGH
```

---

## Part 3: Process Improvements for Extraction Quality

### Pre-Extraction: Competency Questions

Before extracting from any source, develop 30-50 competency questions organized by type:

| Type | Purpose | Example |
|------|---------|---------|
| Definitional | "What is X?" | "What is a tritone?" |
| Relational | "How does X relate to Y?" | "How does the dominant chord relate to the tonic?" |
| Procedural | "How do I accomplish Z?" | "How do I construct a major scale?" |
| Prerequisite | "What must I know before X?" | "What concepts are needed to understand sonata form?" |
| Diagnostic | "What distinguishes X from Y?" | "What is the difference between simple and compound meter?" |

These questions serve as:

1. **Scope definition**: What the knowledge base must answer
2. **Extraction guidance**: What concepts must be captured
3. **Acceptance criteria**: Post-extraction validation

### During Extraction: Multi-Pass Consistency

For higher confidence scoring, implement a lightweight consistency check:

**Single-Pass Extraction (current):**

- Extract once, accept result
- Fast but no verification

**Two-Pass Verification (recommended for important concepts):**

1. Extract concept card
2. Re-extract with slightly different prompt framing
3. Compare: If definitions align → high confidence; if they diverge → flag for review

This doesn't require running every card twice—apply selectively to:

- Concepts the source doesn't explicitly define
- Concepts that synthesize across multiple sections
- Concepts flagged as "medium" or "low" confidence in first pass

### Post-Extraction: Structural Validation

After extraction, run automated checks:

**Completeness Checks:**

- All required frontmatter fields present
- All required sections have content (not just headers)
- Prerequisites field populated for non-foundational concepts

**Consistency Checks:**

- All concepts mentioned in "Prerequisites" or "Relationships" exist as cards
- No orphaned concepts (cards with no incoming or outgoing relationships)
- No circular prerequisites (A requires B requires A)

**Quality Checks:**

- Quick Definition ≤ 2 sentences
- Examples section references source material (not generic)
- At least one competency question linkage per card

---

## Part 4: Implementation Checklist

### Immediate Changes (This Sprint)

- [ ] Update YAML frontmatter schema with new fields
- [ ] Add `extraction_confidence` field with clear criteria
- [ ] Add `aliases` field for variant tracking
- [ ] Split "Related Concepts" into typed relationship fields
- [ ] Add "Prerequisites" section to body content
- [ ] Add "Key Properties" section to body content
- [ ] Split "Common Confusions" into Errors + Confusions
- [ ] Add "Verification Notes" section (internal)

### Process Changes (This Sprint)

- [ ] Create competency question template
- [ ] Document confidence scoring criteria
- [ ] Add structural validation checklist to post-processing

### Deferred to Future Iteration

- [ ] Full Knowledge Space Theory verification
- [ ] OntoClean metaproperty analysis
- [ ] Automated OOPS! pitfall scanning
- [ ] Cross-source entity resolution (`same_as` relationships)
- [ ] Feedback loops from validation → re-extraction

---

## Appendix A: Relationship Type Definitions

| Relationship | Direction | Semantics | Graph Edge Type |
|--------------|-----------|-----------|-----------------|
| Prerequisites | Incoming | "Must know X before this" | `prerequisite_of` (X → this) |
| Builds Upon | Outgoing | "This extends X" | `extends` (this → X) |
| Enables | Inverse | "This is prerequisite for X" | `prerequisite_of` (this → X) |
| Related | Symmetric | "Associated, non-hierarchical" | `related` (bidirectional) |
| Contrasts With | Symmetric | "Often confused with" | `contrasts_with` (bidirectional) |

---

## Appendix B: Confidence Scoring Rubric

| Signal | High | Medium | Low |
|--------|------|--------|-----|
| Definition in source | Explicit, quoted | Implicit, synthesized | Inferred |
| Terminology | Exact term used | Variant used | No specific term |
| Context | Dedicated section | Mentioned in passing | Background assumption |
| Examples | Source provides | Must generate | None available |
| Boundary conditions | Clearly specified | Partially stated | Unstated |

---

## Appendix C: Competency Question Categories

**Definitional (What/Who):**

- What is [concept]?
- What are the defining characteristics of [concept]?
- How is [concept] formally defined?

**Relational (How Related):**

- How does [concept A] relate to [concept B]?
- What is the difference between [concept A] and [concept B]?
- What category does [concept] belong to?

**Procedural (How To):**

- How do I construct/build [concept]?
- How do I identify/recognize [concept]?
- What are the steps to apply [concept]?

**Prerequisite (What Before):**

- What must I understand before learning [concept]?
- What concepts build upon [concept]?
- What is the learning path to [concept]?

**Diagnostic (Why/When):**

- Why is [concept] used instead of [alternative]?
- When should I apply [concept]?
- What are common mistakes when using [concept]?
