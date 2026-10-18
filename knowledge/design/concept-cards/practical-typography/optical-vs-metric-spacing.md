---
concept: "Optical vs. Metric Spacing"
slug: "optical-vs-metric-spacing"
category: "typography"
subcategory: "type-formatting"
tier: "advanced"
layer: "2-domain"
source: "Butterick's Practical Typography"
source_slug: "practical-typography"
authors: "Matthew Butterick"
chapter: "Text Formatting"
chapter_number: null
pdf_page: null
section: "Metrics vs. Optical Spacing"
extraction_confidence: "high"
aliases:
  - "metrics vs optical"
  - "InDesign spacing modes"
prerequisites:
  - "kerning"
  - "font"
extends: []
related:
  - "letterspacing"
  - "typographic-color"
  - "body-text"
contrasts_with: []
answers_questions:
  - "CQ 5: What are the basic anatomical parts of a letterform (baseline, x-height, cap height, ascender, descender, counter)?"
  - "CQ 12: How do font weight, colour, and spacing work together with font size to create typographic hierarchy — why is size alone insufficient?"
rosetta_stone: []
css_implementation: []
---

# Quick Definition

In Butterick's InDesign-specific comparison, metrics uses spacing and kerning data in the font; optical applies a shape-based adjustment. Adobe describes optical as a possible aid in particular contexts, so neither mode is a universal rule for every font and task.

# Core Definition

Butterick explicitly limits his discussion to Adobe InDesign. He says metrics relies on character-spacing information and kerning pairs in the font, while optical uses an algorithmic estimate. His strong preference for metrics, his claim that optical discards font information, and his statement that a patented algorithm is involved are source claims and opinions; this card makes no present legal or implementation claim about that algorithm.

Adobe defines metrics kerning as using built-in font kern pairs and optical kerning as adjusting spacing based on glyph shapes. Adobe identifies cases where optical adjustment can help, including fonts with few or no kern pairs, mixed typefaces in a word, or different sizes on one line. It also notes manual kerning and tracking can be cumulative. This conditional guidance does not predict the result for an arbitrary font or text.

Butterick's prepared comparison reports differences in `nu`/`un`, `un`/`no` and `nt`/`it`, then argues that small differences accumulate in body text. These are his descriptions of the prepared illustration, not a new rendering or general measurement. CSS `font-kerning` controls metric kerning; this InDesign “optical” menu is not a CSS property and is distinct from optical sizing/`opsz`.

# Prerequisites

- **Kerning** — The comparison concerns use of font spacing data and alternative spacing adjustment; the actual shaped result depends on the font and application.
- **Font** — Font metrics and glyph shapes are inputs to these approaches; their quality is not inferred from price.

# Key Properties

1. **Metrics definition**: Adobe describes metrics kerning as using font-provided kerning pairs.
2. **Optical definition**: Adobe describes shape-based adjustment; Butterick objects to its use in the InDesign contexts he discusses.
3. **Conditional choice**: Adobe identifies situations where optical adjustment may help; inspect the actual font, text and output.
4. **InDesign scope**: Butterick's menu comparison cannot be mapped to a CSS optical-kerning switch.
5. **Attributed example**: the `nu`/`un`, `un`/`no` and `nt`/`it` descriptions are his reading of the prepared comparison.

# Construction / Recognition

## To Construct/Create:
1. In InDesign, identify whether the task is using metrics or optical kerning and compare the actual text at its intended size.
2. Consider optical adjustment only in a relevant context, such as absent/sparse pair data, mixed typefaces or different type sizes on one line; inspect whether it helps.
3. Review manual kerning and tracking alongside automatic adjustments because Adobe notes they can accumulate.
4. Do not translate the InDesign setting into CSS. For CSS metric kerning, consult `font-kerning` and inspect the actual result.

## To Identify/Recognise:
1. Compare actual target output for the intended string and style; Butterick's `nu`/`un` example is a source illustration, not a universal diagnostic.
2. An uneven-looking passage alone does not identify which spacing method caused it.

# Context & Application

- **Typical contexts**: Adobe's optical guidance is conditional and describes particular InDesign uses; Butterick argues for metrics in his source context.
- **Common applications**: This card makes no claim about current InDesign defaults, other applications, or a legal status of the algorithm.

# Examples

**Example 1** (metrics-vs-optical-spacing): Butterick describes `nu` and `un` as visually balanced under metrics in his illustration and says optical shifts the `u`; he also discusses `un`/`no` and `nt`/`it`. Preserve this as his reported comparison, not an independently rendered result.

**Example 2** (metrics-vs-optical-spacing): Butterick argues that small spacing differences accumulate over many pairs in body text. Adobe's separate guidance describes optical kerning as potentially useful in selected cases; compare actual output rather than treating either account as universal.

# Relationships

## Builds Upon
- **Kerning** — The comparison concerns font pair data and alternative adjustment; CSS metric kerning is a distinct control.
- **Font** — Font data and glyph shapes inform the methods; neither price nor file format establishes suitability.

## Related
- **Letterspacing** — Tracking adds spacing while kerning adjusts glyph spacing; the amount and order depend on the application and script.
- **Typographic Color** — Spacing can affect the texture of a text block, but no universal “even color” outcome is established here.
- **Body Text** — Butterick discusses accumulated differences at body size; this is an attributed argument, not a tested universal effect.

# Common Errors

- **Error**: Treating Butterick's metrics preference as a universal rule, or calling InDesign Optical a CSS equivalent.
  **Correction**: Attribute the source's judgment, include Adobe's conditional contexts, and compare the actual output. Do not infer current algorithm details or legal status.

# Common Confusions

- **Confusion**: “Optical” means CSS optical sizing, or necessarily means better spacing.
  **Clarification**: Butterick's page concerns an InDesign spacing choice. Optical sizing/`opsz` concerns a font axis; the names do not establish equivalence.

# Source Reference

"Metrics vs. Optical Spacing" page. "Text Formatting" chapter.

# Verification Notes

- Butterick's evaluation and pair examples remain attributed to his InDesign-specific prepared page; the reported patent reference is not a current legal finding.
- Adobe's metrics/optical definitions and conditional contexts inform the qualified description.
- No InDesign, browser, font, assistive-technology or rendering comparison was run.
- The local kerning/font/letterspacing/color/body-text premises and CQ5/CQ12 gaps are recorded separately in the batch.
