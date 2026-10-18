---
concept: "Letterspacing"
slug: "letterspacing"
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
section: "Letterspacing"
extraction_confidence: "high"
aliases:
  - "tracking"
  - "character spacing"
prerequisites:
  - "font"
extends: []
related:
  - "kerning"
  - "all-caps"
  - "small-caps"
contrasts_with:
  - "kerning"
answers_questions:
  - "CQ 11: What distinguishes a spacing system from arbitrary padding values — what problem does constraint solve?"
  - "CQ 12: How do font weight, colour, and spacing work together with font size to create typographic hierarchy — why is size alone insufficient?"
rosetta_stone: []
css_implementation:
  -
    property: "letter-spacing"
    example: ".caps { letter-spacing: 0.05em; } /* illustrative 5% of font size; choose for the actual script, font, and text */"
    support: "baseline"
---

# Quick Definition

Letterspacing, or tracking, adds spacing across text; kerning adjusts glyph spacing in context. Its amount and use depend on the actual string, font, script, size and setting.

# Core Definition

Butterick describes letterspacing as adjustment of horizontal space between letters, unlike pair-specific kerning. He recommends an additional 5–12% for all caps or small caps, particularly at small sizes, while explicitly saying the range is not absolute and judgment matters. Preserve that as his advice, not a mandatory value or comfort guarantee.

He says lowercase usually needs no added spacing, but the prepared page names exceptions: lowercase below 9 pt may benefit from added tracking to keep spaces distinct, and tracking may be removed from lowercase at larger headline sizes. His Goudy anecdote says some sources attribute the “steal sheep” wording to blackletter rather than lowercase and report a more colorful verb; the attribution is disputed.

CSS Text defines `letter-spacing` as additional spacing between typographic character units, in addition to kerning and word spacing. It applies after bidi reordering, and script shaping rules matter: cursive text cannot be handled by blindly inserting a gap between every codepoint. Nonzero tracking can suppress optional ligatures under specified conditions; low-level feature settings can override that behavior.

# Prerequisites

- **Font** — Added tracking is evaluated against the selected font's own spacing and the shaped text.

# Key Properties

1. **Tracking versus kerning**: tracking adds spacing across text; kerning adjusts glyph spacing in context.
2. **Attributed range**: Butterick's 5–12% suggestion is a starting point for caps/small caps, not a rule.
3. **Context exceptions**: small lowercase text may benefit; large lowercase display text may call for removing tracking.
4. **Script aware**: use typographic and shaping behavior for the actual script, not a codepoint-spacing assumption.
5. **Review output**: excessive or insufficient spacing is judged in the real text and hierarchy.

# Construction / Recognition

## To Construct/Create:
1. Start with the actual language, script, face, size and text. Use `letter-spacing` only for an identified tracking need.
2. `0.05em` illustrates 5% of the font size; it is not a prescribed default. Butterick's 5–12% range is his contextual advice for caps/small caps.
3. Compare the result at the intended size and in fallback runs. Avoid applying Latin caps guidance to scripts whose shaping uses different spacing behavior.
4. Keep paragraph or character styles consistent where the project chooses tracking for a role; do not turn that into a universal rule.

## To Identify/Recognise:
1. Compare the added spacing across a representative string and check the visual rhythm and word shapes.
2. A numeric CSS value alone does not establish comfortable, readable or script-appropriate spacing.

# Context & Application

- **Typical contexts**: Caps, small caps, small lowercase text and large display lowercase are distinct contexts with different possible adjustments.
- **Common applications**: Use judgment with the specific face and output; the prepared Word/Pages instructions are source-era examples.

# Examples

**Example 1** (letterspacing): Butterick contrasts tight all-caps spacing with an illustrative 5–12% increase. The result remains a judgment call; his warning sign is spacing so wide that another letter could fit.

**Example 2** (letterspacing): Butterick repeats the Goudy “steal sheep” quip, while noting disputed blackletter attribution and wording. The anecdote does not support a ban on lowercase tracking.

**Example 3** (letterspacing): Butterick says lowercase under 9 pt may benefit from tracking, while larger headline lowercase may have tracking removed. These are source examples, not universal thresholds.

# Relationships

## Builds Upon
- **Font** — Tracking is additional to the selected font's spacing and shaping result.

## Contrasts With
- **Kerning** — Kerning adjusts spacing in glyph context; tracking adds spacing across typographic character units.

## Related
- **All Caps** — Tracking can be considered for a particular caps string; Butterick's range is not mandatory.
- **Small Caps** — Tracking may be useful with a specific small-cap design and output; no fixed amount is required.

# Common Errors

- **Error**: Treating 5–12% as required for all caps and small caps, or forbidding tracking on every lowercase string.
  **Correction**: Attribute the range to Butterick, retain his size exceptions and judgment caveat, and inspect the actual script, font and text.

# Common Confusions

- **Confusion**: Letterspacing adjusts every Unicode codepoint uniformly or replaces kerning.
  **Clarification**: CSS operates on typographic character units after shaping/reordering; tracking is additive to kerning and script behavior can constrain spacing.

# Source Reference

"Letterspacing" page. "Text Formatting" chapter.

# Verification Notes

- The 5–12% advice, lowercase exceptions and Goudy anecdote are attributed to Butterick; attribution remains disputed as described in his page.
- CSS Text defines typographic-unit tracking and script-sensitive behavior; no script-specific rendering was tested.
- The example `0.05em` is illustrative arithmetic, not a comfort or accessibility finding.
- The local kerning/caps/small-caps relations and CQ11/CQ12 answer gaps are evaluated separately in the batch record.
