---
concept: "Hyphenation"
slug: "hyphenation"
category: "typography"
subcategory: "type-composition"
tier: "intermediate"
layer: "2-domain"
source: "Butterick's Practical Typography"
source_slug: "practical-typography"
authors: "Matthew Butterick"
chapter: "Page Layout"
chapter_number: null
pdf_page: null
section: "Hyphenation"
extraction_confidence: "high"
aliases:
  - "automatic hyphenation"
  - "word breaking"
prerequisites:
  - "justified-text"
  - "line-length"
extends: []
related:
  - "hyphens-and-dashes"
  - "headings"
contrasts_with: []
answers_questions:
  - "CQ 1: What is visual hierarchy, and what visual properties (size, colour, contrast, weight, spacing) establish it?"
rosetta_stone: []
css_implementation:
  -
    property: "hyphens"
    example: "p { hyphens: auto; } /* needs known content language and a suitable resource; HTML lang may be on this element or an ancestor */"
    support: "baseline"
---

# Quick Definition

Hyphenation can break words between lines. Butterick recommends it for justified text, treats it as optional with left alignment and advises suppressing it in headings; actual behavior depends on language resources and the engine.

# Core Definition

Butterick defines: "Hyphenation is the automated process of breaking words between lines to create more consistency across a text block."

Butterick recommends hyphenation with justified text to reduce large word gaps and treats it as optional with left alignment. This is advice rather than a CSS validity condition; language resources and engines affect the result.

Butterick says hyphenation becomes more useful as lines shorten; this is a recommendation that depends on language, content and engine.

# Prerequisites

- **Justified Text** — Butterick recommends hyphenation with justification; language and engine affect results.
- **Line Length** — Shorter measures may make word breaking useful.

# Key Properties

1. **Source recommendation**: Butterick recommends hyphenation with justification to reduce large word spaces.
2. **Optional by source advice**: Butterick says it can even a left-aligned rag; review the actual result.
3. **May help short measures**: Fewer spaces can make word breaking useful, subject to language, content and engine support.
4. **Heading advice**: Butterick advises suppressing breaks in short headings because they can disrupt them.
5. **Conditional behavior**: `hyphens: auto` requires known language and a suitable hyphenation resource; a declaration alone does not prove breaks will occur. No current cross-browser support survey was performed.

# Construction / Recognition

## To Construct/Create:
1. In Word: Page Layout > Hyphenation > Automatic.
2. In Pages: Document > Hyphenation checkbox.
3. In CSS, `hyphens: auto` needs the content language to be known (for example, on an ancestor or the element) and an available resource; inspect actual breaks.
4. Consider `hyphens: none` for headings when it suits the language and layout; review actual wrapping.

## To Identify/Recognise:
1. In justified text, uneven word spacing can sometimes form visible rivers; hyphenation may help in some languages, measures and engines, but does not guarantee their removal.
2. Over-hyphenation: too many consecutive lines ending with hyphens.

# Examples

**Example 1** (hyphenation): A heading hyphenated across three lines ("contradic-tions" and "use-less") vs. the same heading unhyphenated — the unhyphenated version is clearer.

# Relationships

## Builds Upon
- **Justified Text** — Butterick recommends it with justified alignment; this is advice rather than a property requirement.
- **Line Length** — Shorter measures may make word breaking useful; assess content and engine behavior.

## Related
- **Hyphens and Dashes** — Distinguish automatic line-break hyphens, discretionary soft hyphens, editorial hyphens and emergency overflow wrapping.
- **Headings** — Butterick advises suppressing hyphenation in short headings where breaks disrupt the text; check the actual language, layout and wrapping.

# Common Errors

- **Error**: Treating hyphenation as an automatic requirement for justified text.
  **Correction**: Butterick recommends it to reduce conspicuous word gaps. Whether it helps depends on the script, language data, measure and engine; inspect the actual output.

# Common Confusions

- **Confusion**: Does declaring `hyphens: auto` always produce automatic word breaks?
  **Clarification**: No. The content language must be known and a suitable hyphenation resource must be available; a declaration alone does not establish that breaks occur. The language may come from the element or an ancestor. Inspect the actual output. Butterick treats hyphenation as optional for left-aligned text and advises suppressing it in short headings when breaks disrupt them; these are contextual recommendations.

# Source Reference

"Hyphenation" page. "Page Layout" chapter.

# Verification Notes

- Claim review: source advice is attributed and scoped; the technical corrections in this assigned card are summarized in the changed teaching above.
- Source basis: the prepared Practical Typography page named in Source Reference was read. Extraction confidence is provenance, not a current technical proof.
- Technical review: relevant CSS behavior was checked against the cited primary specifications. No browser, assistive-technology, font-failure or readability study was run.
- Primary definitions: CSS Text [hyphenation §5.3](https://www.w3.org/TR/css-text-3/#hyphenation).
- Source-fidelity limit: P10-11 original capture and conversion-fidelity evidence remains open.
- Relationship and competency-question contribution is reconciled in Slice19 batch record; this does not establish whole-card endpoint review or full-corpus closure.
