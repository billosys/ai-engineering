---
concept: "Typographic Color"
slug: "typographic-color"
category: "typography"
subcategory: "type-formatting"
tier: "intermediate"
layer: "2-domain"
source: "Butterick's Practical Typography"
source_slug: "practical-typography"
authors: "Matthew Butterick"
chapter: "Text Formatting"
chapter_number: null
pdf_page: null
section: "Color"
extraction_confidence: "high"
aliases:
  - "color in typography"
  - "typographic colour"
prerequisites:
  - "body-text"
  - "typographic-emphasis"
extends: []
related:
  - "font"
  - "point-size"
  - "small-caps"
contrasts_with: []
answers_questions:
  - "CQ 1: What is visual hierarchy, and what visual properties (size, colour, contrast, weight, spacing) establish it?"
  - "CQ 12: How do font weight, colour, and spacing work together with font size to create typographic hierarchy — why is size alone insufficient?"
rosetta_stone: []
css_implementation:
  -
    property: "color"
    example: ".text { color: inherit; } /* use the project's supplied text colour; check the rendered foreground/background pair */"
    support: "baseline"
---

# Quick Definition

Typographic colour can mean the apparent density or texture of a text block, while literal text colour means its foreground hue/value; these are different observations and checks.

# Core Definition

Butterick describes typographic colour as a qualitative impression involving darkness, contrast, rhythm, and texture, even when the text is black. He also discusses literal colour and how size or weight may affect its appearance. These observations are useful design considerations, not guarantees that bold always attracts more attention, that a particular gray is comfortable, or that print body text must always be black. Evaluate the actual foreground/background pair, states, content, and medium.

# Prerequisites

- **Body Text** — Text density may be considered in relation to a block of body text; no universal colour is prescribed.
- **Typographic Emphasis** — Weight and style may change apparent density; markup meaning remains separate.

# Key Properties

1. **Two senses**: Density/texture is not the same as literal foreground colour.
2. **Multiple influences**: Font, size, weight, spacing, content, and rendering can affect perceived density.
3. **Contextual attention**: Literal colour, weight, and size can contribute to hierarchy; no single property is universally strongest.
4. **Pairs matter**: A gray value alone does not establish contrast, comfort, or accessibility without its background and state.
5. **Do not rely on colour alone**: Convey information and links with additional cues as appropriate.

# Construction / Recognition

## To Construct/Create:
1. Use the project's supplied text colour unless the brief identifies a need to change it.
2. Check actual foreground/background pairs across relevant states and output; use the existing `colour.md` method for full contrast checking.
3. Consider density and literal colour separately when tuning hierarchy.
4. Provide non-colour cues where colour conveys information.

## To Identify/Recognise:
1. Ask whether “colour” refers to text-block density or literal hue/value.
2. Identify both foreground and background before drawing a contrast conclusion.
3. Check links and other meaningful states for cues beyond colour.

# Context & Application

Typography may appear to have consistent density even when set in one hue, and literal colour may affect hierarchy. Butterick's black-print and dark-gray-screen advice remains an attributed preference, not a fixed palette or optical-comfort guarantee.

# Examples

**Example 1** (color): The source says bold can create more emphasis than italic through darker apparent colour. Compare the actual face and text; the outcome is not universal.

**Example 2** (color): The source suggests dark gray on screen. A gray foreground without the actual background does not establish contrast or comfort.

# Relationships

## Builds Upon
- **Body Text** — Density can be assessed in a text block; this does not prescribe its literal foreground colour.
- **Typographic Emphasis** — Weight or style may change apparent density; neither alone determines semantic meaning or attention.

## Related
- **Font** — Different resources may render with different density at the same settings; inspect actual output.
- **Point Size** — Size can affect apparent density; it does not establish pair contrast.
- **Small Caps** — Compare forms for appearance and weight; density difference is not a contrast ratio.

# Common Errors

- **Error**: Treating “dark gray” as automatically comfortable or accessible, or using colour alone to signal meaning.
  **Correction**: Check the complete rendered pair and state, and add another cue where information depends on colour.

# Common Confusions

- **Confusion**: Typographic colour and literal text hue are the same measure.
  **Clarification**: Density/texture describes an impression of a text block; foreground/background contrast is a separate pair-based evaluation.

# Source Reference

"Color" page. "Text Formatting" chapter.

# Verification Notes

- Five outcomes: distinguish density from hue; identify properties affecting density; judge visual hierarchy in context; check the complete colour pair/state; avoid color-only meaning and unqualified comfort claims.
- Support: Butterick's assigned page directly distinguishes typographic colour and literal colour. WCAG 2.2 SC1.4.1 states that colour is not the only visual means for conveying information.
- Limitation: this slice did not test a palette, contrast pair, comfort, browser rendering, or accessibility conformance. The sibling `colour.md` method owns complete contrast work.
- Existing `css_implementation[0].example` is corrected to the exact prompt-authorized value; its other metadata is frozen.
- Confidence records extraction confidence, not a universal attention or comfort result.
- Cross-reference identities and literal source reference are retained. Original capture fidelity remains a Project10-11 dependency.
