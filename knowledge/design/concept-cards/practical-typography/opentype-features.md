---
concept: "OpenType Features"
slug: "opentype-features"
category: "typography"
subcategory: "type-elements"
tier: "intermediate"
layer: "2-domain"
source: "Butterick's Practical Typography"
source_slug: "practical-typography"
authors: "Matthew Butterick"
chapter: "Text Formatting"
chapter_number: null
pdf_page: null
section: "OpenType Features"
extraction_confidence: "high"
aliases:
  - "OT features"
  - "OpenType layout features"
prerequisites:
  - "font"
extends: []
related:
  - "small-caps"
  - "ligatures"
  - "alternate-figures"
  - "kerning"
contrasts_with: []
answers_questions:
  - "CQ 1: What is visual hierarchy, and what visual properties (size, colour, contrast, weight, spacing) establish it?"
rosetta_stone: []
css_implementation:
  -
    property: "font-variant-ligatures, font-variant-numeric"
    example: ".text { font-variant-ligatures: common-ligatures; } .numbers { font-variant-numeric: tabular-nums; } /* requests depend on supplied font and shaping; no feature guarantee */"
    support: "baseline"
---

# Quick Definition

OpenType layout features let a font provide alternate glyphs and shaping rules. A usable result depends on the supplied font and the shaping application; language-required shaping and optional refinements such as Latin discretionary forms are different cases.

# Core Definition

Butterick describes OpenType features as font-provided alternate letterforms and rules for inserting them into text. His prepared page says OpenType layout features are necessary for languages such as Arabic and Urdu, while examples such as small caps, alternate figures, ordinals and fractions are optional typographic refinements. Feature availability varies by font, and the application must support the requested feature.

The prepared page reports browser and desktop/mobile support and names Word versions and application controls from its source era. Treat those as attributed, time-bounded reports, not a current compatibility list. Check the actual font, application, script and text. A declaration requests a feature; it cannot supply missing glyphs or feature data.

# Prerequisites

- **Font** — The selected resource must provide the relevant feature or glyphs; the shaping environment must support their use.

# Key Properties

1. **Two-sided availability**: inspect both the supplied font and the shaping application.
2. **Font-specific selection**: designers may include different features, or none.
3. **Different purposes**: required script shaping is not equivalent to optional Latin refinements such as stylistic forms or discretionary ligatures.
4. **High-level controls**: use purpose-specific CSS properties when available; low-level feature tags are for specific controls and may override higher-level requests.
5. **No behavior claim from syntax**: verify representative strings and fallback in the target environment.

# Construction / Recognition

## To Construct/Create:
1. Identify the actual language, script, text and reading role.
2. Inspect supplied font documentation or feature metadata, then choose controls supported by the target application.
3. Compare real strings in the selected face and fallback, including the styles that will be used.
4. Treat source-era Word, Pages and browser steps as historical guidance; consult current application documentation for a current procedure.

## To Identify/Recognise:
1. A specimen or font inspection can show which features are supplied; it does not establish how the target stack will shape the text.
2. Compare actual output for the relevant script and string. A Latin sample cannot establish coverage for another writing system.

# Examples

**Example 1** (opentype-features): Butterick presents small caps, ligatures and alternate figures as optional refinements made possible by OpenType. His prepared page separately notes that layout features are required for scripts such as Arabic and Urdu. The example is a distinction of purpose, not a test of a named font.

# Relationships

## Builds Upon
- **Font** — Font resources may contain layout features; actual availability and shaping also depend on application and text.

## Related
- **Small Caps** — `smcp` is one possible feature; inspect the font and target shaping behavior.
- **Ligatures** — Ligature classes differ; optional common forms do not replace required script shaping.
- **Alternate Figures** — Figure forms and widths are optional font features with separate typographic choices.
- **Kerning** — Kerning is a specific spacing feature, distinct from other substitutions and positioning behavior.

# Common Errors

- **Error**: Assuming every OpenType font exposes the same features or that every feature must be explicitly enabled.
  **Correction**: Inspect the actual resource and application. CSS Fonts specifies required script features and common ligatures among defaults; optional features and supported forms still vary.

# Common Confusions

- **Confusion**: OpenType support means a particular feature will appear in every font and script.
  **Clarification**: The format permits features; each resource, shaping system, language and text determines what is available and applied.

# Source Reference

"OpenType Features" page. "Text Formatting" chapter.

# Verification Notes

- Definition and application-support advice are attributed to Butterick's prepared page; its compatibility statements are source-era reports.
- CSS Fonts Module Level 4 is a Working Draft; its defaults distinguish required script features from optional feature requests.
- No named font, application, browser, assistive technology or rendered feature was tested.
- The local prerequisite and related entries are retained with qualified, card-specific premises; CQ1 membership is reviewed separately in the batch record.
