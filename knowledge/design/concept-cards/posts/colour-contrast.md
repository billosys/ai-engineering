---
concept: "CSS Colour Contrast (Accessibility)"
slug: "colour-contrast"
category: "accessibility"
subcategory: "wcag-contrast"
tier: "intermediate"
layer: "2-domain"
source: "Working With Colors Guide"
source_slug: "posts"
authors: "Sarah Drasner"
chapter: "Accessibility and Other Things to Note about Color"
chapter_number: null
pdf_page: null
section: null
extraction_confidence: "medium"
aliases:
  -
    - "color contrast"
    - "WCAG contrast"
    - "contrast ratio"
    - "a11y color"
prerequisites:
  - "rgb-colour-model"
  - "additive-colour-mixing"
extends: []
related:
  - "colour-bit-depth"
  - "css-colour-custom-properties"
contrasts_with: []
answers_questions:
  - "What WCAG contrast ratio requirements apply to normal vs large text?"
rosetta_stone: []
css_implementation:
  -
    property: "color"
    example: "color: #000; background-color: #fff; /* ratio: 21:1 */"
    support: "baseline"
---

# Quick Definition

Colour contrast is evaluated between a foreground and its background. WCAG 2.2 defines distinct text contrast criteria and non-text contrast requirements; passing a pair calculation alone does not establish page conformance.

# Core Definition

Drasner introduces colour contrast as a relational, context-dependent property: "A color is only a color in reference to another color. This is part of what makes color so difficult. You're probably a little familiar with this in terms of accessibility. A light green on a black may be accessible, but when you change it to a white background it no longer is." She provides several accessibility checking tools but does not state WCAG ratios explicitly. She recommends establishing accessible palettes from the start: "It's also really nice to set up your palette for accessibility from the start. Color Safe is a great tool that helps with that."

WCAG 2.2 SC 1.4.3 (AA) requires 4.5:1 for text and images of text, except large-scale text (at least 18 pt or 14 pt bold, with CJK equivalent sizing), which requires 3:1. Inactive UI components, pure decoration, invisible text and text in images containing significant other visual content are excepted; logos have no minimum. SC 1.4.6 (AAA) uses 7:1 and 4.5:1 for large-scale text with the same exceptions. SC 1.4.11 separately requires 3:1 for essential UI component/state information and graphical objects against adjacent colours, subject to its stated exceptions. SC 1.4.1 says colour is not the only visual means of conveying information.

# Prerequisites

- **RGB colour model** — Contrast ratio calculations require computing relative luminance from RGB values
- **Additive colour mixing** — WCAG relative luminance is calculated from linearized sRGB components using its specified weights

# Key Properties

1. Contrast is always measured between two colours — foreground and background — not in isolation
2. WCAG 2.2 SC 1.4.3 (AA): 4.5:1 for text; 3:1 for large-scale text (at least 18 pt or 14 pt bold; see the criterion’s exceptions)
3. WCAG 2.2 SC 1.4.6 (AAA): 7:1 for text; 4.5:1 for large-scale text, with criterion exceptions
4. Contrast is calculated from relative luminance (a weighted sum of linearised RGB channels), not from HSL Lightness

# Construction / Recognition

## To Identify/Recognise:
1. Use automated tools: browser DevTools, Colorable, WAVE, or Accessible Colors
2. Decode sRGB components to linear values, calculate relative luminance `L = 0.2126R + 0.7152G + 0.0722B`, then use `(Llighter + 0.05)/(Ldarker + 0.05)`; compare the unrounded result
3. A ratio of 1:1 means equal relative luminance (the colours may differ chromatically); 21:1 is the maximum for opaque sRGB black and white

# Context & Application

- **Typical contexts**: Web accessibility compliance, design system colour palette design, legal requirements for digital products
- **Common applications**: Choosing accessible foreground colours for text over a given background; validating design tokens for WCAG compliance; automated accessibility testing

# Examples

**Example 1** (from source): "A light green on a black may be accessible, but when you change it to a white background it no longer is" — Drasner's illustration of contrast as context-dependent.

**Example 2** (from source — tools): Drasner lists Colorable, Contrast-A, Accessible Colors, and Color Safe as tools for measuring and designing for colour contrast.

# Relationships

## Builds Upon
- **RGB colour model** — Relative luminance is computed from linearised RGB values

## Enables
- **Accessible colour palettes** — Knowing contrast requirements allows proactive palette design
- **CSS custom properties** — A project may store chosen palette values in custom properties; the token mechanism does not establish contrast

## Related
- **Colour atmosphere** — Drasner notes "Things that are closer to you are in higher saturation, and in more contrast" — contrast is also a perceptual depth cue

# Common Errors

- **Error**: Using HSL Lightness to estimate whether two colours will pass contrast requirements.
  **Correction**: HSL Lightness is not WCAG relative luminance. For example, `#ffff00` and `#0000ff` have equal HSL lightness but a contrast ratio of about 8.0016:1; equal HSL lightness neither predicts equal luminance nor establishes a passing text pair.

- **Error**: Applying one text threshold to every visual element.
  **Correction**: Evaluate text under SC 1.4.3 or 1.4.6, and essential UI component/state information and graphical objects under SC 1.4.11. Their scopes and exceptions differ; a focus indicator may also need review under the applicable focus criteria.

# Common Confusions

- **Confusion**: "Colour-blind friendly" means high contrast.
  **Clarification**: These are related but distinct. High contrast (luminance ratio) helps users with low vision. Colour-blind friendliness means not relying solely on hue to convey information (e.g. using both colour and shape for error indicators). A design can have sufficient contrast but still be unusable for colour-blind users if information is conveyed by hue alone.

# Source Reference

"Accessibility and Other Things to Note about Color" section, Working With Colors Guide (Sarah Drasner).

# Verification Notes

- Formula scope: For opaque rendered sRGB pairs, decode each channel, calculate relative luminance and compare the unrounded ratio. Resolve transparency, overlays and backgrounds to the actual rendered pair first; pair arithmetic does not establish page conformance.
- Primary criteria and formula: [WCAG 2.2 SC 1.4.1, 1.4.3, 1.4.6, 1.4.11 and glossary](https://www.w3.org/TR/WCAG22/). The sRGB relative-luminance definition uses the piecewise sRGB decoding and 0.2126/0.7152/0.0722 weights.

- Definition source: Drasner for general principle and tools; WCAG ratio numbers synthesised from standard knowledge (not directly quoted from source)
- Confidence rationale: Medium — Drasner covers the contextual principle and tools; current WCAG 2.2 criteria and formula are separately linked as technical support
- Uncertainties: Drasner’s prepared passage does not state WCAG thresholds. The added criteria are based on the linked WCAG 2.2 recommendation; actual conformance still requires checking page content and rendered contexts.
- Cross-reference status: Not in Ottosson source
- Rosetta Stone check: No mappings added
- OCR issues: None significant
