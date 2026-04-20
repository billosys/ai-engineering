---
concept: CSS Colour Contrast (Accessibility)
slug: colour-contrast
category: accessibility
subcategory: wcag-contrast
tier: intermediate
layer: 2-domain
source: "Working With Colors Guide"
source_slug: posts
authors: "Sarah Drasner"
chapter: "Accessibility and Other Things to Note about Color"
chapter_number: null
pdf_page: null
section: null
extraction_confidence: medium
aliases:
  - ["color contrast", "WCAG contrast", "contrast ratio", "a11y color"]
prerequisites:
  - rgb-colour-model
  - additive-colour-mixing
extends:
  - []
related:
  - colour-bit-depth
  - css-colour-custom-properties
contrasts_with:
  - []
answers_questions:
  - "What WCAG contrast ratio requirements apply to normal vs large text?"
rosetta_stone: []
css_implementation:
  - property: "color"
    example: "color: #000; background-color: #fff; /* ratio: 21:1 */"
    support: baseline
---

# Quick Definition

Colour contrast in accessibility refers to the luminance ratio between foreground and background colours; WCAG defines minimum ratios (4.5:1 for normal text, 3:1 for large text) below which text is considered inaccessible to users with low vision or colour-blindness.

# Core Definition

Drasner introduces colour contrast as a relational, context-dependent property: "A color is only a color in reference to another color. This is part of what makes color so difficult. You're probably a little familiar with this in terms of accessibility. A light green on a black may be accessible, but when you change it to a white background it no longer is." She provides several accessibility checking tools but does not state WCAG ratios explicitly. She recommends establishing accessible palettes from the start: "It's also really nice to set up your palette for accessibility from the start. Color Safe is a great tool that helps with that."

Note: The WCAG 4.5:1 (normal text) and 3:1 (large text) contrast ratio requirements are standard accessibility specifications not explicitly cited in the Drasner source text. The card content for those ratios is synthesised from standard WCAG knowledge, not from the source.

# Prerequisites

- **RGB colour model** \u2014 Contrast ratio calculations require computing relative luminance from RGB values
- **Additive colour mixing** \u2014 Luminance is derived from the additive combination of the RGB channels

# Key Properties

1. Contrast is always measured between two colours \u2014 foreground and background \u2014 not in isolation
2. WCAG 2.1 AA requires: 4.5:1 for normal text (under 18pt/14pt bold), 3:1 for large text (18pt+ or 14pt+ bold)
3. WCAG 2.1 AAA requires: 7:1 for normal text, 4.5:1 for large text
4. Contrast is calculated from relative luminance (a weighted sum of linearised RGB channels), not from HSL Lightness

# Construction / Recognition

## To Identify/Recognise:
1. Use automated tools: browser DevTools, Colorable, WAVE, or Accessible Colors
2. Contrast ratio = (L1 + 0.05) / (L2 + 0.05), where L1 is the lighter colour's relative luminance and L2 is the darker
3. A ratio of 1:1 means identical colours (no contrast); 21:1 is the maximum (black on white)

# Context & Application

- **Typical contexts**: Web accessibility compliance, design system colour palette design, legal requirements for digital products
- **Common applications**: Choosing accessible foreground colours for text over a given background; validating design tokens for WCAG compliance; automated accessibility testing

# Examples

**Example 1** (from source): "A light green on a black may be accessible, but when you change it to a white background it no longer is" \u2014 Drasner's illustration of contrast as context-dependent.

**Example 2** (from source \u2014 tools): Drasner lists Colorable, Contrast-A, Accessible Colors, and Color Safe as tools for measuring and designing for colour contrast.

# Relationships

## Builds Upon
- **RGB colour model** \u2014 Relative luminance is computed from linearised RGB values

## Enables
- **Accessible colour palettes** \u2014 Knowing contrast requirements allows proactive palette design
- **CSS custom properties** \u2014 Contrast-aware palettes are often stored and managed via CSS custom properties

## Related
- **Colour atmosphere** \u2014 Drasner notes "Things that are closer to you are in higher saturation, and in more contrast" \u2014 contrast is also a perceptual depth cue

# Common Errors

- **Error**: Using HSL Lightness to estimate whether two colours will pass contrast requirements.
  **Correction**: HSL Lightness does not correlate with perceptual luminance. Two colours with very different HSL Lightness values may still fail contrast requirements (e.g. saturated yellow vs. saturated blue), and two colours with similar Lightness may have very different luminance.

- **Error**: Testing contrast only for the primary text colour and forgetting placeholder text, disabled states, or icon colours.
  **Correction**: WCAG contrast requirements apply to all informational content, including placeholder text (which frequently fails due to low opacity), UI components, and focus indicators.

# Common Confusions

- **Confusion**: "Colour-blind friendly" means high contrast.
  **Clarification**: These are related but distinct. High contrast (luminance ratio) helps users with low vision. Colour-blind friendliness means not relying solely on hue to convey information (e.g. using both colour and shape for error indicators). A design can have sufficient contrast but still be unusable for colour-blind users if information is conveyed by hue alone.

# Source Reference

"Accessibility and Other Things to Note about Color" section, Working With Colors Guide (Sarah Drasner).

# Verification Notes

- Definition source: Drasner for general principle and tools; WCAG ratio numbers synthesised from standard knowledge (not directly quoted from source)
- Confidence rationale: Medium \u2014 Drasner covers the concept correctly but with limited technical depth; ratio numbers are external knowledge applied to fill the card
- Uncertainties: WCAG ratio values (4.5:1, 3:1, 7:1) are NOT directly stated in the Drasner source and are synthesised from WCAG specifications. This should be verified against a primary WCAG source before treating as source-verified.
- Cross-reference status: Not in Ottosson source
- Rosetta Stone check: No mappings added
- OCR issues: None significant
