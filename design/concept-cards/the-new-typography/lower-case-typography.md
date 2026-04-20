---
# === CORE IDENTIFICATION ===
concept: Lower-Case Typography
slug: lower-case-typography

# === CLASSIFICATION ===
category: typography
subcategory: typography-foundations
tier: intermediate
layer: 2-domain

# === PROVENANCE ===
source: "The New Typography"
source_slug: the-new-typography
authors: "Jan Tschichold"
chapter: "The Principles of the New Typography"
chapter_number: 12
pdf_page: 102
section: "Orthography as at present or all in lower case?"

# === CONFIDENCE ===
extraction_confidence: medium

# === VARIANTS ===
aliases:
  - "Kleinschreibung"
  - "minuscule-only typography"
  - "single-alphabet typography"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - sans-serif-advocacy  # the argument for lower-case depends on sans-serif as the base form
extends: []
related:
  - the-new-typography  # lower-case advocacy is part of the movement's reform programme
  - functional-typography  # the argument is grounded in economy and function
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "CQ 56: What typographic details (ligatures, true small caps, old-style figures, proper dashes, correct quotation marks) distinguish professionally set text from amateur typography?"

# === VISUAL DESIGN EXTENSIONS ===
rosetta_stone:
  - domain: linguistics
    concept: "orthographic reform"
    rating: structural
    note: "Tschichold's argument for abolishing capitals parallels broader linguistic reform movements — the methodology (rational simplification based on functional analysis) matches, though the application domain (visual form vs. language rules) differs."

css_implementation:
  - property: "text-transform"
    example: "text-transform: lowercase; /* All text in lower case */"
    support: baseline
---

# Quick Definition

The New Typography advocates abolishing capital letters for German text, using only lower-case (minuscule) letterforms — arguing that Roman capitals and Carolingian minuscules are "two different styles" awkwardly combined, and that a single-alphabet system would yield economic, pedagogical, and aesthetic advantages.

# Core Definition

Tschichold historicises the problem: capitals and lower-case are "not one but two alphabets" — Roman majuscules from "the beginning of our era" and Carolingian minuscules from "about A.D. 800" — combined only during the Renaissance, producing "the dichotomy, especially noticeable in German, between the capitals and the smaller letters."

The functional argument: "Lower-case letters are far easier to read, because of the ascenders and descenders which make complete words easier to recognize." The economic argument: "A completely one-type system, using lower case only, would be of great advantage to the national economy; it would entail savings and simplifications in many areas."

He is pragmatic about adoption: "While the New Typography regards the removal of capitals as desirable, it is not an absolute demand. But it lies, like a more logical design for our orthography, in our path."

# Prerequisites

- **Sans-Serif Advocacy** — The lower-case argument assumes sans-serif as the base form, since "roman type and its simpler form, sanserif" are the letterforms under discussion.

# Key Properties

1. **Two alphabets**: Roman capitals and Carolingian minuscules are historically separate systems combined during the Renaissance.
2. **Readability advantage**: Lower-case letters with ascenders and descenders create more distinctive word shapes than all-caps.
3. **Economic efficiency**: Simplifications in teaching, typewriting, type design, type-cutting, and composition.
4. **Aesthetic unity**: "A stylistically faultless letter" — avoiding the visual mismatch of two design systems.
5. **International precedent**: French fashion design already uses lower-case only; German capitalisation of nouns is an anomaly compared to other European languages.
6. **Not absolute**: Tschichold acknowledges this is aspirational, not an immediate demand.

# Construction / Recognition

## To Construct/Create:
1. Set text in lower-case only, retaining capitals only for proper names and sentence beginnings (following Jakob Grimm's model).
2. Choose sans-serif for maximum consistency of the single-alphabet approach.
3. Consider the readability impact — lower-case for body text, capitals available as a separate "alphabet" for display use.

## To Identify/Recognise:
1. Lower-case typography: text set without capitalised nouns or mixed-case conventions.
2. Historical examples: French fashion advertising, Bauhaus publications, De Stijl typography.

# Context & Application

- **Typical contexts**: Experimental typography, brand identity, display typography.
- **Common applications**: Lowercase-only logotypes (e.g., adidas, intel), experimental editorial design, web typography where text-transform controls case.
- **Historical note**: Tschichold later retreated from this position in his 1946 essay "Glaube und Wirklichkeit," acknowledging that the lower-case-only approach was too radical for practical adoption. The Bauhaus used lower-case-only typography in its publications. Today, lowercase-only setting is common in brand identities and display contexts but not in body text.

# Examples

**Example 1** (p. 77): French fashion advertisement from Vogue — "All words are set in lower case" — cited as existing international precedent.

**Example 2** (p. 76): The argument from readability — "Lower-case letters are far easier to read, because of the ascenders and descenders which make complete words easier to recognize."

# Relationships

## Builds Upon
- **Sans-Serif Advocacy** — Lower-case typography presupposes sans-serif as the appropriate typeface.

## Related
- **The New Typography** — Lower-case advocacy is part of the movement's broader reform programme.
- **Functional Typography** — The argument is grounded in functional economy.

# Common Errors

- **Error**: Setting continuous text in all capitals for emphasis.
  **Correction**: All-caps text is harder to read than lower-case because it lacks the distinctive word shapes created by ascenders and descenders.

# Common Confusions

- **Confusion**: Lower-case typography means abolishing capital letters entirely.
  **Clarification**: Tschichold distinguishes between eliminating capitals and using them as a separate display alphabet — "the two alphabets of roman are really two different styles, and should be used in parallel, but not mixed."

# Source Reference

"The Principles of the New Typography" — section "Orthography as at present or all in lower case?" (pp. 75-82).

# Verification Notes

- Definition source: Direct quotes from Ch. 12, orthography section.
- Confidence rationale: Medium — a subsection within a larger chapter; Tschichold himself qualifies the position as aspirational rather than absolute. The concept is historically significant but largely abandoned in practice.
- Uncertainties: The degree to which Tschichold considered this a firm requirement vs. a theoretical ideal is ambiguous.
- Cross-reference status: All referenced slugs correspond to planned cards.
- Rosetta Stone check: Checked against 0010 tables. Linguistics parallel (orthographic reform) noted as STRUCTURAL.
- OCR issues: Minor — broken spacing in section heading. Reconstructed from context.
