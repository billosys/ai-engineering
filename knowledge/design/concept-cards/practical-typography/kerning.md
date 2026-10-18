---
concept: "Kerning"
slug: "kerning"
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
section: "Kerning"
extraction_confidence: "high"
aliases:
  - "kern pairs"
  - "pair kerning"
prerequisites:
  - "font"
extends: []
related:
  - "letterspacing"
  - "optical-vs-metric-spacing"
  - "opentype-features"
contrasts_with:
  - "letterspacing"
answers_questions:
  - "CQ 5: What are the basic anatomical parts of a letterform (baseline, x-height, cap height, ascender, descender, counter)?"
  - "CQ 12: How do font weight, colour, and spacing work together with font size to create typographic hierarchy — why is size alone insufficient?"
rosetta_stone: []
css_implementation:
  -
    property: "font-kerning"
    example: ".text { font-kerning: normal; } /* metric kerning request; inspect actual font and text */"
    support: "baseline"
---

# Quick Definition

Kerning adjusts spacing between glyphs using font-provided data or a typesetting system's adjustment. It differs from tracking, which adds spacing across text; a visible gap by itself does not show whether kerning is active.

# Core Definition

Butterick defines kerning as adjustment of specific letter pairs and contrasts it with letterspacing, which affects all pairs. He recommends “Always use kerning” and says built-in kerning is sufficient for most users; retain this as his advice, not a claim about every application's default or every font's data.

CSS Fonts defines `font-kerning` values `auto`, `normal` and `none`. `normal` requests metric kerning for proportionally spaced glyphs. `auto` leaves application to the user agent; fonts without kerning data show no effect. This request does not promise equal gaps: glyph shapes, pair data, script, font selection and shaping affect the result. Tracking is applied in addition to kerning.

# Prerequisites

- **Font** — The selected font may provide kerning data; the actual shaped result also depends on text and rendering stack.

# Key Properties

1. **Pair/context sensitive**: spacing adjustments relate to glyphs in context, not a uniform addition after every character.
2. **Data and output differ**: a font can contain kerning data without a visible change for a particular string; a CSS declaration does not prove the result.
3. **Tracking is separate**: `letter-spacing` adds spacing after shaping and kerning rather than replacing pair adjustments.
4. **Fixed-width glyphs**: CSS Fonts says kerning is not intended for fixed-width glyphs.
5. **Source recommendation**: Butterick's “Always use kerning” is useful advice, not evidence that all tools have the same default.

# Construction / Recognition

## To Construct/Create:
1. Use a high-level control such as `font-kerning: normal` when metric kerning is intended and the target supports it.
2. Inspect the actual font and representative text, including the script, size and style in use.
3. Treat Butterick's Word and Pages instructions as source-era procedures; check current application guidance rather than assuming the settings remain universal.
4. Add tracking only for a separate contextual spacing goal; judge the combined result.

## To Identify/Recognise:
1. Compare actual shaped output for pairs such as AV, To or Wa, which the card uses as visual examples.
2. A large visible gap does not prove kerning is off: the font may lack data, the pair may have no adjustment, or other shaping and spacing may affect it.

# Context & Application

- **Typical contexts**: Review pair spacing in the actual text and styles, especially where large display text makes a particular pair conspicuous.
- **Common applications**: Use the target application's current controls and inspect output; this card does not establish a current default for Word, Pages or browsers.

# Examples

**Example 1** (kerning): Butterick's prepared page describes kerning reducing conspicuous gaps between selected pairs so they sit more consistently with the font. This is his explanation of the example, not a newly rendered specimen.

# Relationships

## Builds Upon
- **Font** — A resource may include spacing and kerning data; its presence alone does not establish the final shaped spacing.

## Contrasts With
- **Letterspacing** — Kerning uses pair/context adjustments; tracking adds spacing across typographic character units. CSS Text places letter spacing in addition to kerning.

## Related
- **Optical vs. Metric Spacing** — Butterick's comparison concerns InDesign's named modes; Adobe describes metrics as using font data and optical as shape-based adjustment. Do not generalize it to a CSS control.
- **OpenType Features** — OpenType `kern` is one feature route; CSS recommends the higher-level `font-kerning` control for ordinary kerning requests.

# Common Errors

- **Error**: Treating a visible gap as proof that kerning is disabled or prescribing `text-rendering: optimizeLegibility` as a universal kerning switch.
  **Correction**: Check the font, text, shaping environment and current application controls. `font-kerning: normal` requests metric kerning, but no data can mean no visible effect.

# Common Confusions

- **Confusion**: Kerning and letterspacing are interchangeable.
  **Clarification**: Kerning adjusts spacing in glyph context; tracking adds spacing across text. Neither guarantees a particular visual result without reviewing the actual string.

# Source Reference

"Kerning" page. "Text Formatting" chapter.

# Verification Notes

- Pair-specific explanation and “Always use kerning” are attributed to Butterick; his application steps are source-era reports.
- CSS Fonts defines metric kerning controls, proportionally spaced glyph scope, missing-data behavior and interaction with tracking.
- No browser, font, app, assistive technology or actual pair output was tested.
- The prerequisite, contrast and related entries state local premises; CQ5/CQ12 contributions and gaps are separately recorded in the batch.
