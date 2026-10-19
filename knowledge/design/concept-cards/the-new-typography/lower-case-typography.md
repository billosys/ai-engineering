---
concept: "Lower-Case Typography"
slug: "lower-case-typography"
category: "typography"
subcategory: "typography-foundations"
tier: "intermediate"
layer: "2-domain"
source: "The New Typography"
source_slug: "the-new-typography"
authors: "Jan Tschichold"
chapter: "The Principles of the New Typography"
chapter_number: 12
pdf_page: 102
section: "Orthography as at present or all in lower case?"
extraction_confidence: "medium"
aliases:
  - "Kleinschreibung"
  - "minuscule-only typography"
  - "single-alphabet typography"
prerequisites:
  - "sans-serif-advocacy"
extends: []
related:
  - "the-new-typography"
  - "functional-typography"
contrasts_with: []
answers_questions: []
rosetta_stone:
  -
    domain: "linguistics"
    concept: "orthographic reform"
    rating: "structural"
    note: "Tschichold's argument for abolishing capitals parallels broader linguistic reform movements — the methodology (rational simplification based on functional analysis) matches, though the application domain (visual form vs. language rules) differs."
css_implementation:
  -
    property: "text-transform"
    example: ".lowercase-display { text-transform: lowercase; } /* Display only; preserve meaningful source casing. */"
    support: "baseline"
---

# Quick Definition

The New Typography advocates abolishing capital letters for German text, using only lower-case (minuscule) letterforms — arguing that Roman capitals and Carolingian minuscules are "two different styles" awkwardly combined, and that a single-alphabet system would yield economic, pedagogical, and aesthetic advantages.

# Core Definition

This section preserves the card’s recorded account of Tschichold’s historical programme; quotations, attributions and page claims have not been checked against the unavailable represented edition. Its polemics are not universal contemporary rules.

Tschichold historicises the problem: capitals and lower-case are "not one but two alphabets" — Roman majuscules from "the beginning of our era" and Carolingian minuscules from "about A.D. 800" — combined only during the Renaissance, producing "the dichotomy, especially noticeable in German, between the capitals and the smaller letters."

The functional argument: "Lower-case letters are far easier to read, because of the ascenders and descenders which make complete words easier to recognize." The economic argument: "A completely one-type system, using lower case only, would be of great advantage to the national economy; it would entail savings and simplifications in many areas."

He is pragmatic about adoption: "While the New Typography regards the removal of capitals as desirable, it is not an absolute demand. But it lies, like a more logical design for our orthography, in our path."

# Prerequisites

- **Sans-Serif Advocacy** — Sans-serif advocacy supplies context for the programme’s reform argument and "roman type and its simpler form, sanserif" wording; learning support does not imply that lower-case requires sans-serif. Serif status and case are independent.

# Key Properties

The historical preferences below describe the programme; current use depends on content, audience, language/script, output, constraints and supplied identity.

1. **Recorded historical argument**: The card reports an origin account for Roman capitals and Carolingian minuscules; that chronology is unverified here, not a newly established orthographic history.
2. **Attributed readability argument**: The ascender/descender and word-shape claim is the source’s reported rationale, not universal empirical proof that one casing treatment is easiest for every text and reader.
3. **Economic efficiency**: Simplifications in teaching, typewriting, type design, type-cutting, and composition.
4. **Aesthetic unity**: "A stylistically faultless letter" — avoiding the visual mismatch of two design systems.
5. **International precedent**: French fashion design already uses lower-case only; German capitalisation of nouns is an anomaly compared to other European languages.
6. **Not absolute**: Tschichold acknowledges this is aspirational, not an immediate demand.

# Construction / Recognition

## To Construct/Create:
1. Distinguish the recorded all-lowercase proposal from the separate reform option retaining proper-name and sentence-initial capitals (reported as Jakob Grimm’s model). These are not one casing algorithm.
2. In contemporary work, preserve author- and language-appropriate case in source text. Choose display casing separately, regardless of serif/sans classification.
3. CSS `text-transform: lowercase` styles display without rewriting underlying content or semantics; declare the actual language and inspect meaningful names, abbreviations and text. Capitals as a separate "alphabet" are a reported historical proposal, not a source rewrite instruction.

## To Identify/Recognise:
1. Lower-case typography: text set without capitalised nouns or mixed-case conventions.
2. Historical examples: French fashion advertising, Bauhaus publications, De Stijl typography.

# Context & Application

- **Typical contexts**: Experimental typography, brand identity, display typography.
- **Common applications**: Lowercase-only logotypes (e.g., adidas, intel), experimental editorial design, web typography where text-transform controls case.
- **Historical note (reported, unverified here)**: Tschichold later retreated from this position in his 1946 essay "Glaube und Wirklichkeit," acknowledging that the lower-case-only approach was too radical for practical adoption. The Bauhaus used lower-case-only typography in its publications. Today, lowercase-only setting is common in brand identities and display contexts but not in body text.

# Examples

These are retained reported examples and quoted wording, not newly verified figure, authorship, priority or page evidence.

**Example 1** (p. 77): French fashion advertisement from Vogue — "All words are set in lower case" — cited as existing international precedent.

**Example 2** (p. 76): The argument from readability — "Lower-case letters are far easier to read, because of the ascenders and descenders which make complete words easier to recognize."

# Relationships

## Builds Upon
- **Sans-Serif Advocacy** — Sans-serif advocacy helps explain the historical context; lower-case can be used with serif or sans-serif faces and does not presuppose either.

## Related
- **The New Typography** — Lower-case advocacy is part of the movement's broader reform programme.
- **Functional Typography** — The argument is grounded in functional economy.

# Common Errors

- **Error**: Setting continuous text in all capitals for emphasis.
  **Correction**: Consider purpose, length, script and actual rendered reading conditions. The recorded word-shape argument does not establish a universal all-caps readability law.

# Common Confusions

- **Confusion**: Lower-case typography means abolishing capital letters entirely.
  **Clarification**: Tschichold distinguishes between eliminating capitals and using them as a separate display alphabet — "the two alphabets of roman are really two different styles, and should be used in parallel, but not mixed."

# Source Reference

"The Principles of the New Typography" — section "Orthography as at present or all in lower case?" (pp. 75-82).

# Verification Notes

Current scoped review: contemporary correctness/scope, local consistency and the exact relationship/CQ occurrences are assessed in Slice26’s batch record. The unavailable edition, translation and page basis leave source fidelity, quotations, figures and historical dates/priority unassessed/input-blocked. No new original read, empirical readability result, browser/AT check or full-standard inspection is claimed.

The following notes are preserved historical extraction assertions, including their old confidence, OCR and uncertainty wording. They are not newly verified results:

- Definition source: Direct quotes from Ch. 12, orthography section.
- Confidence rationale: Medium — a subsection within a larger chapter; Tschichold himself qualifies the position as aspirational rather than absolute. The concept is historically significant but largely abandoned in practice.
- Uncertainties: The degree to which Tschichold considered this a firm requirement vs. a theoretical ideal is ambiguous.
- Cross-reference status: All referenced slugs correspond to planned cards.
- Rosetta Stone check: Checked against 0010 tables. Linguistics parallel (orthographic reform) noted as STRUCTURAL.
- OCR issues: Minor — broken spacing in section heading. Reconstructed from context.
