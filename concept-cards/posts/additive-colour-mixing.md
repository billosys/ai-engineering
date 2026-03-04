---
concept: Additive Colour Mixing
slug: additive-colour-mixing
category: visual-perception
subcategory: colour-physics
tier: foundational
layer: 0-perception
source: "Working With Colors Guide"
source_slug: posts
authors: "Sarah Drasner"
chapter: "Color mixing"
chapter_number: null
pdf_page: null
section: null
extraction_confidence: high
aliases:
  - ["additive mixing", "light mixing", "RGB mixing"]
prerequisites:
  - []
extends:
  - []
related:
  - subtractive-colour-mixing
  - rgb-colour-model
  - colour-bit-depth
contrasts_with:
  - subtractive-colour-mixing
answers_questions:
  - "What distinguishes additive from subtractive colour mixing, and which does a monitor use?"
rosetta_stone:
  - domain: mathematics
    concept: "Vector addition"
    rating: structural
    note: "Additive colour mixing is literally vector addition of light intensities in each channel. Combining red and green light is R + G = yellow in the same way as adding component vectors."
---

# Quick Definition

Additive colour mixing is the process of combining light of different wavelengths, where each added colour increases the total luminance; combining red, green, and blue light at full intensity produces white.

# Core Definition

Drasner explains additive colour mixing in terms of its historical and physical basis: "On a computer (or any monitor), we're working with light. Which means that when all of the colors mix together, they make white." She credits Newton's prism experiment as establishing that white light is composed of multiple colours. "In additive color mixing, the type of color mixing you get in a monitor, red green and blue can be used to produce all colors, or rgb. In this type of mixing, red and green create yellow." Drasner also notes the historical precedent in art: "Seurat and the Pointillists used red and green to create yellow in paintings like 'La Grande Jatte'... This type of painting was created under the belief that optical mixing created more pure resonance in your eye than traditional subtractive pigment color mixing."

# Prerequisites

- None \u2014 this is a foundational physical concept

# Key Properties

1. Adding colours increases brightness \u2014 more light = brighter result
2. Red + Green + Blue at full intensity = white
3. In the absence of all light = black (the default background)
4. The primary colours are Red, Green, Blue (not the red/yellow/blue of paint mixing)

# Construction / Recognition

## To Identify/Recognise:
1. Monitors, projectors, and phone screens use additive mixing
2. If mixing two colours produces something lighter than either original, it is additive
3. Red + Green = Yellow is the canonical non-obvious result of additive mixing that distinguishes it from paint

# Context & Application

- **Typical contexts**: Display technology, photography, digital colour authoring, stage lighting, CSS colour specification
- **Common applications**: All CSS and web colour is additive; RGB, hex, HSL, and other web colour formats all ultimately describe additive light values

## Cross-Domain Connections

**Mathematics \u2192 STRUCTURAL**: Additive colour mixing corresponds structurally to vector addition. Each colour channel (R, G, B) is a component; combining colours is summing the vectors. This is why RGB is a linear colour space at its base \u2014 before gamma encoding.

# Examples

**Example 1** (from source): "red and green create yellow" \u2014 Drasner's primary example of additive mixing, contrasted with paint mixing where red and green produce brown.

**Example 2** (from source): Monitors as "many combinations of small bits of light combined that resonate to create a myriad of colors" \u2014 each pixel is a small additive mixture of R, G, B sub-pixels.

# Relationships

## Builds Upon
- **Physics of light** \u2014 Additive mixing reflects the physical behaviour of photons

## Enables
- **RGB colour model** \u2014 RGB is the direct expression of additive mixing with red, green, blue primaries
- **Colour bit depth** \u2014 The quantisation of additive light intensities per channel
- **CSS colour specification** \u2014 All CSS colour formats ultimately resolve to additive RGB values

## Related
- **HSL colour space** \u2014 HSL re-parameterises RGB; it still describes additive light values

## Contrasts With
- **Subtractive colour mixing** \u2014 Used by paint, ink, and print; primaries are cyan/magenta/yellow; combining produces darker colours; more colours \u2192 approaches black

# Common Errors

- **Error**: Expecting red and green to produce brown or muddy colour on a monitor.
  **Correction**: In additive mixing, red + green = yellow. The brain-learned expectation from paint mixing does not apply.

# Common Confusions

- **Confusion**: Monitors use subtractive mixing because they produce colours by "filtering" the backlight.
  **Clarification**: LCD screens do filter light, but the resulting pixel colour is perceived additively by the eye \u2014 the colour model of the output is still additive RGB.

# Source Reference

"Color mixing" section, Working With Colors Guide (Sarah Drasner).

# Verification Notes

- Definition source: Direct quotes from Drasner
- Confidence rationale: High \u2014 Drasner provides a clear, dedicated section on this concept
- Uncertainties: None significant
- Cross-reference status: Not discussed in Ottosson source
- Rosetta Stone check: Mathematics/vector-addition mapping added as structural
- OCR issues: HTML figure markup stripped; prose content clean
