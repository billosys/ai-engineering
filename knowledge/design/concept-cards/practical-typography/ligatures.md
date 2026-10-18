---
concept: "Ligatures"
slug: "ligatures"
category: "typography"
subcategory: "type-composition"
tier: "intermediate"
layer: "2-domain"
source: "Butterick's Practical Typography"
source_slug: "practical-typography"
authors: "Matthew Butterick"
chapter: "Type Composition"
chapter_number: null
pdf_page: null
section: "Ligatures"
extraction_confidence: "high"
aliases:
  - "character ligatures"
  - "fi ligature"
prerequisites:
  - "font"
extends: []
related:
  - "opentype-features"
  - "kerning"
contrasts_with: []
answers_questions:
  - "CQ 5: What are the basic anatomical parts of a letterform (baseline, x-height, cap height, ascender, descender, counter)?"
rosetta_stone: []
css_implementation:
  -
    property: "font-variant-ligatures"
    example: ".text { font-variant-ligatures: common-ligatures; } /* requests common ligatures; required script shaping is separate */"
    support: "baseline"
---

# Quick Definition

A ligature substitutes one glyph for a sequence of characters during shaping. Optional Latin common ligatures and features required for a script are different cases; a CSS request does not add a missing font feature.

# Core Definition

Butterick explains ligatures as a historical solution to collisions in metal type. His prepared page focuses on whether lowercase `f` and `i` visibly collide in the font and styles being used. It gives a row comparison for `fi`, `fj`, `fl`, `ffi`, `gg` and `gy`; the captured example does not preserve both font names, so none are supplied here. The page also notes that a `gy` ligature may separate glyphs rather than connect them.

Butterick says ligatures beyond a visible `fi` collision are largely a stylistic choice and expresses a personal preference against them in body text. His “only fi is mandatory” claim describes that Latin example; it is not a rule for required script shaping. CSS Fonts says common ligatures are normally enabled by default and that required script features remain enabled. `font-variant-ligatures` controls optional classes but cannot guarantee a supplied font has them.

The source warns that manually inserting ligature characters can confuse spellcheck, hyphenation and search. Automated shaping preserves the underlying character sequence; this card does not claim a specific search or assistive-technology outcome.

# Prerequisites

- **Font** — The selected resource must provide a requested optional ligature; the shaping system and text determine what is applied.

# Key Properties

1. **Historical purpose**: ligatures addressed collisions in metal type; digital forms may still be useful where a particular sequence visually collides.
2. **Optional and required cases differ**: common Latin ligatures are an optional typographic choice; script-required shaping is not governed by a Latin `fi` preference.
3. **Default behavior matters**: common ligatures normally default on under CSS Fonts; explicit activation is not universally required.
4. **Manual text differs from shaping**: inserting a ligature character changes the text sequence; a shaping feature substitutes glyphs for display.
5. **Availability varies**: inspect the actual face, application, script and style.

# Construction / Recognition

## To Construct/Create:
1. Inspect the relevant string, script, font and styles for a real visual or typographic need.
2. Use `font-variant-ligatures` for an intentional optional ligature request or suppression, where supported; do not use `text-rendering: optimizeLegibility` as a universal feature control.
3. Keep the source text as ordinary characters when automatic shaping is intended. Review the actual output and fallback.

## To Identify/Recognise:
1. Compare the supplied text with optional common ligatures enabled and suppressed in the target environment, focusing on the actual sequence and style.
2. A requested feature or Latin specimen does not prove required shaping or output in another script.

# Examples

**Example 1** (ligatures): Butterick's prepared comparison shows `fi`, `fj`, `fl`, `ffi`, `gg` and `gy` across rows with and without ligatures. The accompanying text discusses a visible `fi` collision but loses the two font names; the missing names remain unknown.

**Example 2** (ligatures): The prepared page notes that italic `gy` can use a ligature that separates glyphs. “Ligature” therefore does not always mean two forms visually connect.

# Relationships

## Builds Upon
- **Font** — Optional ligature availability depends on the font and shaping environment.

## Related
- **OpenType Features** — Ligatures are one feature class; required script shaping and optional Latin forms must remain distinct.
- **Kerning** — Both can affect the appearance of adjacent glyphs, but ligatures substitute glyphs while kerning adjusts spacing.

# Common Errors

- **Error**: Manually replacing character sequences with ligature codepoints or applying one blanket on/off policy.
  **Correction**: Prefer shaping features when appropriate, check text/search requirements, and preserve features required by the script. Do not promise search, spellcheck or assistive-technology outcomes without testing.

# Common Confusions

- **Confusion**: Every ligature joins letters, or every ligature must be explicitly enabled.
  **Clarification**: Butterick's `gy` example separates glyphs, while CSS Fonts normally enables common ligatures by default. Required script features remain a separate shaping requirement.

# Source Reference

"Ligatures" page. "Type Composition" chapter.

# Verification Notes

- The collision example and personal stylistic preference are attributed to Butterick; omitted font names remain unknown.
- CSS Fonts Working Draft defines defaults and feature classes; no target font/script output was observed.
- Manual-text risks are reported by the prepared page; no search, hyphenation or assistive-technology test was run.
- The local feature/kerning relations and CQ5 gap are reviewed separately in the batch.
