---
concept: "Em Unit"
slug: "em-unit"
category: "typography"
subcategory: "type-formatting"
tier: "foundational"
layer: "2-domain"
source: "Butterick's Practical Typography"
source_slug: "practical-typography"
authors: "Matthew Butterick"
chapter: "Appendix"
chapter_number: null
pdf_page: null
section: "Em Sizing"
extraction_confidence: "high"
aliases:
  - "em"
  - "em square"
  - "em sizing"
prerequisites:
  - "point-size"
extends: []
related:
  - "font"
  - "hyphens-and-dashes"
contrasts_with: []
answers_questions:
  - "CQ 5: What are the basic anatomical parts of a letterform (baseline, x-height, cap height, ascender, descender, counter)?"
rosetta_stone: []
css_implementation:
  -
    property: "text-indent"
    example: "p + p { text-indent: 1em; } /* illustrative; 1em uses this element's computed font-size */"
    support: "baseline"
---

# Quick Definition

The em is a typographic unit used in metal type and digital font metrics; it does not guarantee that every digital glyph fits within a one-em vertical box. It also names a CSS font-relative length whose reference depends on the property.

# Core Definition

Butterick explains: "The em size of a font is the same as its point size. This was true for hundreds of years of metal type." For digital fonts, the em square is a coordinate space for font metrics, not a guaranteed maximum outline bound: glyph outlines may extend beyond it. The source’s historical explanation is useful context but its maximum-box statement is not a technical invariant.

This is why point size is not absolute: "Two fonts set at the same point size will appear to be different sizes if one occupies less space on its em."

The em is *not* the letter M: "the word em denotes a typographer's measurement, not the letter M." The en is half the em. In traditional print shops, they were called "mutton" and "nut" to disambiguate.

# Prerequisites

- **Point Size** — The em is the unit that underlies point size measurement.

# Key Properties

1. **Equal to point size**: A 12pt font has a 12pt em.
2. **Metric coordinate space**: The em square does not guarantee that digital glyph outlines stay within its bounds.
3. **Not the letter M**: Despite the homophony, em is a unit of measurement.
4. **En = half em**: The en is half the width of the em.
5. **Explains apparent size differences**: Fonts that use their em space differently appear different sizes at the same point setting.
6. **Consistent for centuries**: The concept has survived the transition from metal to digital type.

# Construction / Recognition

## To Construct/Create:
1. In CSS, `em` is property-specific: most properties use the element’s computed font size; `font-size` resolves against the inherited size. `rem` uses the root element’s font size.
2. The nominal em size historically corresponds to type size; it does not equal visible glyph height or line-box height.
3. Em dashes and en dashes are named for these units (though modern digital versions often run narrower).

## To Identify/Recognise:
1. Printed appearance does not expose the em square directly; visible outlines and line boxes are distinct metrics.
2. Two fonts at the same point size looking different sizes demonstrates the em at work.

# Context & Application

- **Typical contexts**: Understanding font metrics; CSS relative sizing; typographic measurement.
- **Common applications**: Em-based CSS units for scalable layouts; understanding why fonts look different at the same nominal size; dash sizing conventions.
- **Historical note**: Butterick recounts a 2012 Michigan Supreme Court case that turned on the legal definition of point size and em sizing.

# Examples

**Example 1** (em-sizing): "Why not just make the point size equal to something specific, like the height of the capital H?" — Because "since fonts vary widely in their design, there's no character you could pick that would always be consistent."

**Example 2** (em-sizing): Butterick recounts a Michigan ballot case to illustrate a traditional point-size definition. This is the author’s historical account, not an independently checked legal finding.

# Relationships

## Builds Upon
- **Point Size** — The em is the unit of measurement underlying point size.

## Related
- **Font** — Each font uses its em space differently, causing apparent size variation.
- **Hyphens and Dashes** — Em dash and en dash are named for these units.

# Common Errors

- **Error**: Assuming the em is the width of the letter "M".
  **Correction**: "The word em denotes a typographer's measurement, not the letter M." The typographic em is a size unit, not the letter M; CSS `em` also has property-specific resolution.

# Common Confusions

- **Confusion**: Point size directly measures cap height or contains every outline.
  **Clarification**: Nominal em size is distinct from cap/x-height and line boxes; digital glyph outlines can extend outside the em square.

# Source Reference

"Em Sizing" page. "Appendix" chapter.

# Verification Notes

- Claim review: the concept and useful source recommendations are retained with explicit scope; technical corrections above are limited to the assigned paragraph-composition claims.
- Source basis: the prepared Practical Typography pages named in Source Reference were read. Historical extraction confidence is retained as provenance, not treated as proof of current technical correctness.
- Technical review: CSS units, line-height, measurement, paragraph spacing, hyphenation and fragmentation claims were checked against the cited specifications where applicable. No browser, assistive-technology, font-failure or readability study was run.
- Primary definitions: CSS Values and Units [font-relative lengths §6.1.1](https://www.w3.org/TR/css-values-4/#font-relative-lengths); OpenType [FUnits and the em square](https://learn.microsoft.com/en-us/typography/opentype/spec/ttch01#funits-and-the-em-square).
- Source-fidelity limit: P10-11 original capture and conversion-fidelity evidence remains open; this correction does not verify fidelity to an immutable original.
- Relationships and competency-question contribution are reconciled in Slice19 batch record; they do not establish whole-card endpoint review or full-corpus closure.
