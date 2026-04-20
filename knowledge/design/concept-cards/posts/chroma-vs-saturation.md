---
concept: Chroma vs Saturation (Colour Picker Context)
slug: chroma-vs-saturation
category: colour-theory
subcategory: colour-properties
tier: intermediate
layer: 2-domain
source: "Okhsv and Okhsl"
source_slug: posts
authors: "Bj\u00f6rn Ottosson"
chapter: "HSL"
chapter_number: null
pdf_page: null
section: "Color spaces for color picking"
extraction_confidence: high
aliases:
  - ["saturation vs chroma", "colorfulness"]
prerequisites:
  - hsl
  - hsv
extends:
  - []
related:
  - orthogonal-colour-properties
  - okhsl
  - okhsv
contrasts_with:
  - []
answers_questions:
  - "What distinguishes chroma from saturation in a colour space?"
  - "What makes a colour picker perceptually well-designed?"
rosetta_stone: []
css_implementation: []
---

# Quick Definition

Chroma is an absolute measure of a colour's colourfulness; saturation is a relative measure, expressing colourfulness as a proportion of the maximum possible at the same lightness. They are distinct perceptual quantities that are frequently confused in colour space nomenclature.

# Core Definition

Ottosson distinguishes the two clearly in his critique of HSL's terminology: HSL's "Saturation" parameter is "roughly the chroma of the color relative to the most colorful color with the same 'lightness' and 'hue.'" He notes it is "confusingly referred to as saturation, which it is not comparable to. In the original paper it was referred to as 'relative chroma', which is more accurate." In the Munsell system, as Ottosson discusses, colours are described by "Hue, Chroma and Value" \u2014 chroma there is an independent perceptual dimension. Saturation in the perceptual sense is the colourfulness of a stimulus relative to its own brightness, meaning a pale pastel can have high saturation at low chroma if it is also low in brightness. The practical consequence for picker design is that Orthogonal Chroma and Orthogonal Saturation are distinct design goals: "Orthogonal Chroma \u2014 Lightness/Hue can be altered, while keeping perceived Chroma constant" and "Orthogonal Saturation \u2014 Lightness/Hue can be altered, while keeping perceived Saturation constant."

# Prerequisites

- **HSL colour space** \u2014 The confusion arises specifically in HSL's naming convention
- **HSV colour space** \u2014 HSV Saturation is also a relative quantity but differently defined from HSL Saturation

# Key Properties

1. Chroma: absolute colourfulness, independent of lightness \u2014 used in Munsell, CIELab, Oklab
2. Saturation: colourfulness relative to maximum possible at same lightness/hue \u2014 used in HSL, HSV (differently in each)
3. HSL "Saturation" is more accurately called "relative chroma" \u2014 it does not correspond to perceptual saturation
4. HSV "Saturation" and HSL "Saturation" are not the same quantity, even though both use the same name

# Construction / Recognition

## To Identify/Recognise:
1. If two colours look equally colourful despite having different brightnesses, they have similar chroma but different saturation
2. A pale lemon yellow and a deep olive may have equal saturation but very different chroma
3. In a picker: if reducing lightness while keeping the "Saturation" slider constant visually changes the purity of the colour disproportionately, the slider is controlling relative chroma, not true saturation

# Context & Application

- **Typical contexts**: Colour model design, perceptual colour science, colour picker implementation, data visualisation colour scale design
- **Common applications**: Understanding what a "saturation" slider actually does in different tools; designing colour palettes where colourfulness should remain constant across lightness variations

# Examples

**Example 1** (from source): "Not the same as 'saturation' in HSV" \u2014 Ottosson makes explicit that HSL Saturation and HSV Saturation are different quantities sharing the same label.

**Example 2** (from source): HSLuv's "Saturation" is described as "based on chroma as defined in CIELChuv, but rescaled to be relative to the most saturated sRGB color of the same 'lightness' and 'hue'" \u2014 this rescaling is what makes HSLuv Saturation non-smooth: the uneven gamut shape causes abrupt chroma jumps when hue is changed at constant HSLuv Saturation.

# Relationships

## Builds Upon
- **Perceptual colour science** \u2014 The distinction is defined by how the visual system processes colour signals

## Enables
- **Orthogonal colour properties** \u2014 Recognising the distinction enables understanding why Orthogonal Chroma and Orthogonal Saturation are separate goals
- **Okhsl design** \u2014 Okhsl's saturation parameter is designed to be smoothly varying in a way that HSL's is not

## Related
- **Munsell colour system** \u2014 Uses Chroma (not Saturation) as an independent dimension
- **Okhsl / Okhsv** \u2014 Both provide saturation parameters that are defined carefully to avoid confusion

# Common Errors

- **Error**: Assuming HSL Saturation = HSV Saturation.
  **Correction**: Ottosson explicitly states these are not the same. They are both relative quantities but relative to different reference colours.

- **Error**: Using "saturation" and "chroma" interchangeably in discussion of perceptual colour spaces.
  **Correction**: Chroma is absolute; saturation is relative. In Munsell and Oklab, chroma is the appropriate term.

# Common Confusions

- **Confusion**: Maximum HSL Saturation (100%) always gives the most colourful colour.
  **Clarification**: At HSL Lightness of 0% or 100%, the colour is black or white regardless of Saturation. Maximum perceived chroma occurs around L=50% for most hues.

# Source Reference

"HSL" section under "Color spaces for color picking" and "What makes a good color picker?" section, Okhsv and Okhsl (Bj\u00f6rn Ottosson).

# Verification Notes

- Definition source: Direct quotes from Ottosson
- Confidence rationale: High \u2014 Ottosson makes this distinction explicit and central to his argument
- Uncertainties: None significant
- Cross-reference status: Not explicitly discussed in Drasner source
- Rosetta Stone check: No mappings added
- OCR issues: None significant
