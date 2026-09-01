# HOWTO: Concept Card Extraction with Claude Code

A practical guide to the mechanics and best practices for creating high-quality concept cards from primary source material.

> **Note:** The extraction prompt template (`cc-extraction-prompt-template-v2.md`) is the operational entry point for each source extraction. It orchestrates reading order across all section documents.

---

## What Are Concept Cards?

Concept cards are atomic knowledge units that capture a single concept in a structured, queryable format. Each card has:

1. **YAML Frontmatter** — Machine-readable metadata for search, filtering, and graph construction
2. **Markdown Body** — Human-readable exposition organized into standardized sections

The dual format serves two consumers:

- **Humans** reading for understanding
- **LLMs** accessing structured knowledge during interactions

---

## The Golden Rules

### 1. One Concept, One Card

Never combine multiple concepts into a single card, even if they're related. If you find yourself writing "X and Y" as the concept name, you need two cards.

**Bad**: "Major and Minor Scales" → One card trying to cover two concepts
**Good**: "Major Scale" + "Minor Scale" → Two cards, cross-referenced

### 2. Source-Faithful, Not Source-Copied

Extract the concept as the source presents it, but in your own structured format. Don't plagiarize paragraphs—synthesize and structure.

**Bad**: Copy-pasting source paragraphs into sections
**Good**: Extracting the essence into structured sections with source citations

### 3. Explicit Relationships

Every concept exists in a web of relationships. Make these explicit in typed fields, not buried in prose.

**Bad**: "This concept is related to several others including..."
**Good**:

```yaml
prerequisites:
  - interval
  - scale-degree
extends:
  - triad
related:
  - chord-inversion
contrasts_with:
  - minor-triad
```

### 4. Confidence Is Information

Not all extractions are equally reliable. Signal this in the `extraction_confidence` field.

| Confidence | When to Use |
|------------|-------------|
| **high** | Source explicitly defines the concept with clear terminology |
| **medium** | Concept is present but definition must be synthesized from context |
| **low** | Concept is inferred, implied, or reconstructed |

### 5. Provenance Is Sacred

Every assertion should be traceable to the source. Include:

- Chapter and chapter number
- PDF page number (from metadata header)
- Section heading if identifiable
- Specific examples with page references

---

## Frontmatter: Field by Field

### Core Identification

```yaml
concept: Major Scale
slug: major-scale
```

- **concept**: The human-readable name, properly capitalized
- **slug**: The filename (without `.md`), lowercase with hyphens

**Slug rules:**

- All lowercase
- Hyphens for spaces
- No special characters
- Match the filename exactly

### Classification

```yaml
category: scales-modes
subcategory: diatonic-scales
tier: foundational
```

- **category**: Primary classification from the domain taxonomy
- **subcategory**: Optional finer classification
- **tier**: Prerequisite depth
  - `foundational`: No prerequisites within this source
  - `intermediate`: Requires foundational concepts
  - `advanced`: Requires intermediate concepts

### Provenance

```yaml
source: "Music Theory for the 21st-Century Classroom"
source_slug: 21st-century-classroom
authors: "Robert Hutchinson"
chapter: "Scales and Scale Degrees"
chapter_number: 3
pdf_page: 42
section: "The Major Scale"
```

- **source**: Full title, in quotes if it contains special characters
- **source_slug**: The directory name for this source
- **authors**: As credited in the source
- **chapter**: Exact chapter title from source
- **chapter_number**: Integer
- **pdf_page**: From the chapter's metadata header, or `null`
- **section**: Section heading if identifiable, or `null`

### Confidence

```yaml
extraction_confidence: high
```

Document your rationale in the Verification Notes section of the body.

### Variants (Authority Control)

```yaml
aliases:
  - "Ionian mode"
  - "major mode"
  - "diatonic major scale"
```

Capture all alternative names, including:

- Synonyms
- Abbreviations
- Notational forms
- Historical names
- Common misspellings (for search)

**YAML quoting rule:** Any alias containing a colon (`:`) MUST be quoted. YAML interprets `key: value` as a mapping, not a string.

```yaml
# BAD — YAML parses this as a map, not a string:
  - Kotlin variant: panache-kotlin

# GOOD — quotes prevent misparse:
  - "Kotlin variant: panache-kotlin"
```

This applies to all string-valued list entries, not just aliases.

### Typed Relationships

```yaml
prerequisites:
  - half-step
  - whole-step
  - scale-degree
extends:
  - diatonic-scale
related:
  - key-signature
  - major-key
contrasts_with:
  - minor-scale
  - chromatic-scale
```

**Use exact slugs** that match existing or planned card filenames.

**Relationship semantics:**

- **prerequisites**: Concepts that MUST be understood before this one
- **extends**: Concepts this one builds upon or elaborates
- **related**: Non-hierarchical associations
- **contrasts_with**: Commonly confused concepts

### Competency Questions

```yaml
answers_questions:
  - "What is a major scale?"
  - "How do I construct a major scale?"
  - "What is the interval pattern of a major scale?"
```

Link to the competency questions this card helps answer.

---

## Body Sections: Best Practices

### Quick Definition

**Purpose**: Fast lookup for someone who knows the concept but needs a reminder.

**Guidelines:**

- Maximum 2 sentences
- No jargon that isn't in the concept name itself
- Write for quick scanning

**Example:**
> A major scale is a seven-note diatonic scale with a specific pattern of whole and half steps (W-W-H-W-W-W-H). It's the most fundamental scale in Western tonal music.

### Core Definition

**Purpose**: Authoritative technical reference definition.

**Guidelines:**

- Quote the source directly if it provides a clear definition
- Include all defining characteristics
- Use proper technical terminology
- Cite the source location

**Example:**
> The major scale is a diatonic scale consisting of seven distinct pitch classes arranged in the intervallic pattern: whole step, whole step, half step, whole step, whole step, whole step, half step (W-W-H-W-W-W-H). When constructed from C, this produces the "white key" scale C-D-E-F-G-A-B-C with no sharps or flats. The major scale defines the intervallic foundation for major keys and serves as the reference point for describing other scales and modes (Hutchinson, p. 42).

### Prerequisites

**Purpose**: Explicit dependency chain for learning paths.

**Guidelines:**

- List every concept needed to understand this one
- State WHY each is required
- Use bold for concept names
- For foundational concepts: explicitly state "No prerequisites"

**Example:**
>
> - **Half step** — The major scale's structure is defined by half-step placements
> - **Whole step** — Most intervals in the major scale are whole steps
> - **Scale degree** — Understanding major scale requires knowing how to identify positions within a scale

**For foundational concepts:**
> This is a foundational concept with no prerequisites within this source.

### Key Properties

**Purpose**: Enumerated characteristics that define the concept.

**Guidelines:**

- Use numbered list
- Each property should be verifiable
- Include edge cases and boundary conditions

**Example:**
>
> 1. Contains exactly seven distinct pitch classes
> 2. Interval pattern: W-W-H-W-W-W-H (2-2-1-2-2-2-1 in semitones)
> 3. Half steps occur between scale degrees 3-4 and 7-8
> 4. The seventh degree is a half step below the tonic (leading tone)
> 5. All other adjacent scale degrees are whole steps apart

### Construction / Recognition

**Purpose**: Procedural knowledge—how to do it.

**Guidelines:**

- Use numbered steps
- Separate construction from recognition if both apply
- Be explicit enough that someone could follow the steps

**Example:**

> ## To Construct a Major Scale
>
> 1. Start with the tonic note
> 2. Move up a whole step to scale degree 2
> 3. Move up a whole step to scale degree 3
> 4. Move up a half step to scale degree 4
> 5. Move up a whole step to scale degree 5
> 6. Move up a whole step to scale degree 6
> 7. Move up a whole step to scale degree 7
> 8. Move up a half step to return to the tonic (scale degree 8)
>
> ## To Recognize a Major Scale
>
> 1. Identify the starting and ending note (should be the same pitch class)
> 2. Check that there are exactly seven distinct notes plus the octave
> 3. Verify half steps occur only between degrees 3-4 and 7-8
> 4. Verify all other adjacent degrees are whole steps

### Context & Application

**Purpose**: When, where, and why this concept matters.

**Guidelines:**

- Be specific to the domain
- Include historical/stylistic context if relevant
- Mention typical usage patterns

**Example:**
> The major scale is foundational to Western tonal music from the Baroque period onward. It defines the pitch content for pieces in major keys and serves as the reference for describing other scales (e.g., "minor scale has a lowered third compared to major").
>
> **Typical contexts:**
>
> - Establishing tonal center in major-key pieces
> - Melodic construction in tonal music
> - Foundation for understanding key signatures
>
> **Historical note:** The major scale corresponds to the Ionian mode of the medieval church modes, though its dominance in Western music is a post-Renaissance development.

### Examples

**Purpose**: Concrete instances from the source text.

**Guidelines:**

- Always cite page/section
- Use source's own examples, not generic ones
- Include any worked examples the source provides

**Example:**
> **Example 1** (p. 43): The C major scale (C-D-E-F-G-A-B-C) demonstrates the pattern using all natural notes.
>
> **Example 2** (p. 44): The G major scale (G-A-B-C-D-E-F♯-G) shows how the pattern requires F♯ to maintain the W-W-H-W-W-W-H interval structure.
>
> ## Worked Example
>
> Constructing the D major scale (from source, p. 45):
>
> 1. Start on D
> 2. Whole step → E
> 3. Whole step → F♯ (not F natural, which would be a half step)
> 4. Half step → G
> 5. Whole step → A
> 6. Whole step → B
> 7. Whole step → C♯
> 8. Half step → D
>
> Result: D-E-F♯-G-A-B-C♯-D (two sharps)

### Relationships

**Purpose**: Structured connections to other concepts.

**Guidelines:**

- Repeat frontmatter relationships with additional context
- Explain the nature of each relationship
- Use concept names that match card slugs

**Example:**

> ## Builds Upon
>
> - **Diatonic scale** — The major scale is a specific type of diatonic scale
>
> ## Enables
>
> - **Key signature** — Key signatures derive from major scale structures
> - **Major key** — Major keys are defined by major scale pitch content
> - **Relative minor** — Found by relationship to the major scale
>
> ## Related
>
> - **Circle of fifths** — Organizes major scales by key signature
> - **Scale degree names** — Named positions apply to major scale
>
> ## Contrasts With
>
> - **Minor scale** — Has lowered 3rd, 6th, and/or 7th compared to major
> - **Chromatic scale** — Contains all 12 semitones, not just 7

### Common Errors

**Purpose**: Practical mistakes when applying the concept.

**Guidelines:**

- Focus on procedural errors (doing it wrong)
- Provide corrections
- These are "how you mess up" not "what you misunderstand"

**Example:**
>
> - **Error**: Placing half steps between degrees 2-3 and 5-6 (confusing with natural minor)
>   **Correction**: Half steps in major scale are ONLY between 3-4 and 7-8
>
> - **Error**: Forgetting to raise F to F♯ when constructing G major scale
>   **Correction**: Always apply the W-W-H-W-W-W-H pattern from the tonic; adjust accidentals as needed

### Common Confusions

**Purpose**: Conceptual misunderstandings about what this IS.

**Guidelines:**

- Focus on what people wrongly believe about the concept
- Provide clarifications
- These are "what you misunderstand" not "how you mess up"

**Example:**
>
> - **Confusion**: Believing that "major" means "louder" or "more important"
>   **Clarification**: "Major" refers to the quality of the third scale degree (major third above tonic) and the characteristic interval pattern
>
> - **Confusion**: Thinking all major scales use the same notes as C major
>   **Clarification**: Each major scale uses different pitch classes; only C major uses all naturals

### Source Reference

**Purpose**: Full citation for traceability.

**Guidelines:**

- Chapter number and title
- Section if applicable
- Page range
- Any figures, tables, or example numbers

**Example:**
> Chapter 3: Scales and Scale Degrees, Section 3.2 "The Major Scale," pages 42-47. See especially Figure 3.1 (major scale interval pattern) and Example 3.2 (constructing major scales on various tonics).

### Verification Notes

**Purpose**: Internal tracking for quality assurance.

**Guidelines:**

- Document what was directly quoted vs. synthesized
- Justify confidence level
- Note any uncertainties
- Flag cross-references for verification

**Example:**
>
> - Definition: Direct adaptation from p. 42, paragraph 1
> - Key Properties: Items 1-4 explicit in source; item 5 synthesized from discussion
> - Construction steps: Adapted from source's worked examples (pp. 44-45)
> - Confidence: HIGH — explicit definition and extensive examples in source
> - Cross-references: All slug references verified against planned extractions
> - Uncertainties: None

---

## File Organization

### Naming Conventions

| Element | Format | Example |
|---------|--------|---------|
| Concept card | `slug.md` | `major-scale.md` |
| Source directory | `sources-md/source-slug/` | `sources-md/21st-century-classroom/` |
| Output directory | `concept-cards/source-slug/` | `concept-cards/21st-century-classroom/` |

### Slug Rules

- All lowercase
- Hyphens for word separation
- No underscores, spaces, or special characters
- No numerical prefixes
- Match exactly between `slug:` field and filename

**Good slugs:**

- `major-scale`
- `dominant-seventh-chord`
- `circle-of-fifths`
- `voice-leading`

**Bad slugs:**

- `Major-Scale` (uppercase)
- `major_scale` (underscore)
- `001-major-scale` (prefix)
- `majorscale` (no separation)

---

## Quality Checklist

Before considering a card complete, verify:

### Frontmatter

- [ ] `concept` is properly capitalized
- [ ] `slug` matches filename (without `.md`)
- [ ] `category` is from defined taxonomy
- [ ] `tier` is assigned (foundational/intermediate/advanced)
- [ ] `extraction_confidence` is set with rationale
- [ ] `aliases` includes all known variants (empty array if none)
- [ ] `prerequisites` lists all dependencies (empty array if foundational)
- [ ] `answers_questions` has at least one CQ

### Body

- [ ] Quick Definition is ≤2 sentences
- [ ] Core Definition cites source location
- [ ] Prerequisites explains WHY each is needed
- [ ] Key Properties are enumerated, not prose
- [ ] Construction/Recognition uses numbered steps
- [ ] Examples cite specific source pages
- [ ] Relationships use valid concept slugs
- [ ] Common Errors vs. Confusions are distinguished
- [ ] Source Reference is complete
- [ ] Verification Notes justify confidence

### Cross-References

- [ ] All concepts in prerequisites/extends/related/contrasts_with exist as cards
- [ ] Relationship types are correctly applied
- [ ] No circular prerequisites

---

## Common Mistakes to Avoid

### 1. Combining Concepts

**Wrong**: Creating "Triads and Seventh Chords" as one card
**Right**: Separate cards for "Triad" and "Seventh Chord"

### 2. Generic Examples

**Wrong**: "For example, C major is a common key"
**Right**: "Example (p. 47): Beethoven's Sonata Op. 2 No. 3 demonstrates the major scale in C"

### 3. Buried Relationships

**Wrong**: "This concept relates to several others, including intervals and scale degrees..."
**Right**: Use the structured `prerequisites`/`related` fields

### 4. Missing Provenance

**Wrong**: "The major scale has seven notes"
**Right**: "The major scale has seven notes (Hutchinson, p. 42)"

### 5. Flat Confidence

**Wrong**: Assigning `high` to everything
**Right**: Vary based on source clarity; document rationale

### 6. Undefined Slugs

**Wrong**: `prerequisites: [some-concept-maybe]`
**Right**: Only use slugs that match actual or planned cards

### 7. Prose in Properties

**Wrong**: "The major scale has several key properties. First, it contains..."
**Right**: Numbered list of discrete properties

### 8. Confusing Errors and Confusions

**Wrong**: Mixing procedural mistakes with conceptual misunderstandings
**Right**:

- Common Errors = "You did it wrong" (procedural)
- Common Confusions = "You understood it wrong" (conceptual)

---

## Extraction Workflow

### For Each Chapter

1. **Read the chapter** to identify concepts
2. **List concepts** with estimated importance/complexity
3. **Determine tiers** based on prerequisite analysis
4. **Extract in dependency order** (foundational first)
5. **Cross-reference** as you extract (note slugs for later cards)
6. **Validate** frontmatter and body completeness
7. **Verify** cross-references resolve to actual cards

### For Each Concept

1. **Identify** the concept boundaries (what's in, what's out)
2. **Find** the source's definition (if explicit)
3. **Assign** confidence based on definition clarity
4. **List** prerequisites by tracing the "what must you know first" chain
5. **Extract** key properties as discrete, enumerable items
6. **Document** construction/recognition procedures
7. **Pull** examples directly from source with citations
8. **Map** relationships to other concepts
9. **Note** errors vs. confusions from your domain knowledge
10. **Complete** verification notes

---

## When to Create Multiple Cards

Sometimes a single source section covers what should be multiple cards. Split when:

1. **Different definitions**: The source defines X and Y separately
2. **Different prerequisites**: X requires A, Y requires B
3. **Different applications**: X is used for purpose P, Y for purpose Q
4. **Common confusion**: People often mix up X and Y (they need separate cards to disambiguate)

Sometimes multiple source sections cover what should be one card. Merge when:

1. **Same concept, different contexts**: Chapter 3 introduces X, Chapter 7 applies X
2. **Progressive elaboration**: Basic definition in Ch. 2, formal definition in Ch. 5
3. **Cross-references**: Source explicitly says "X (see also Chapter N)"

When merging, cite all source locations and use the most comprehensive definition.

---

## Handling Edge Cases

### Concept Not Explicitly Defined

- Set `extraction_confidence: medium` or `low`
- In Core Definition, note: "The source does not explicitly define this concept. Synthesized from discussion on pp. X-Y."
- In Verification Notes, document your synthesis process

### Circular Dependencies

If A requires B and B requires A:

1. Identify which is more fundamental
2. Make the fundamental one `foundational` (no prerequisites)
3. Add a note explaining the mutual dependency

### Multiple Source Treatments

If different chapters present conflicting information:

1. Note the conflict in Verification Notes
2. Use the most authoritative treatment for the definition
3. Document alternatives in Context & Application

### No Suitable Examples in Source

- First, look harder—sources usually have examples
- If truly none, note: "The source provides no explicit examples for this concept"
- Do NOT invent generic examples

### Concept Appears in Multiple Chapters

Decide based on treatment:

- **Same treatment**: One card, cite both chapters
- **Different treatments**: Separate cards with cross-references, or one card with "Context & Application" covering both

---

## Final Checklist Before Committing

- [ ] All cards pass frontmatter validation
- [ ] All cards have complete body sections
- [ ] All cross-referenced slugs exist
- [ ] No orphaned cards (unless legitimately foundational)
- [ ] No circular prerequisites
- [ ] Confidence distribution is realistic (not all high)
- [ ] At least one CQ per card
- [ ] Competency questions have coverage
- [ ] Filenames match slugs
- [ ] No numerical prefixes on files
- [ ] All files have `.md` extension
