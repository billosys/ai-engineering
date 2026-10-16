---
concept: "Additive Colour Mixing"
slug: "additive-colour-mixing"
category: "visual-perception"
subcategory: "colour-physics"
tier: "foundational"
layer: "0-perception"
source: "Working With Colors Guide"
source_slug: "posts"
authors: "Sarah Drasner"
chapter: "Color mixing"
chapter_number: null
pdf_page: null
section: null
extraction_confidence: "high"
aliases:
  -
    - "additive mixing"
    - "light mixing"
    - "RGB mixing"
prerequisites: []
extends: []
related:
  - "subtractive-colour-mixing"
  - "rgb-colour-model"
  - "colour-bit-depth"
contrasts_with:
  - "subtractive-colour-mixing"
answers_questions:
  - "What distinguishes additive from subtractive colour mixing, and which does a monitor use?"
rosetta_stone:
  -
    domain: "mathematics"
    concept: "Vector addition"
    rating: "structural"
    note: "In a specified linear-light RGB space, adding channel contributions is component-wise vector addition. This mapping is limited to fixed primaries and does not describe encoded-sRGB arithmetic, interpolation or alpha compositing."
---

# Quick Definition

Additive colour mixing combines light from specified primaries. In a linear-light RGB space, the channel contributions add; real displays have bounded primaries and gamut, so RGB cannot reproduce every visible colour.

# Core Definition

Drasner explains additive colour mixing in terms of its historical and physical basis: "On a computer (or any monitor), we're working with light. Which means that when all of the colors mix together, they make white." She credits Newton's prism experiment as establishing that white light is composed of multiple colours. "In additive color mixing, the type of color mixing you get in a monitor, red green and blue can be used to produce all colors, or rgb. In this type of mixing, red and green create yellow." Drasner also notes the historical precedent in art: "Seurat and the Pointillists used red and green to create yellow in paintings like 'La Grande Jatte'... This type of painting was created under the belief that optical mixing created more pure resonance in your eye than traditional subtractive pigment color mixing."

# Prerequisites

- None — this is a foundational physical concept

# Key Properties

1. Adding emitted-light contributions increases the result in a specified linear-light space; perceived brightness and encoded-sRGB arithmetic are not this operation
2. Under fixed RGB primaries, full red + full green + full blue contributions produce the additive white point
3. In the absence of all light = black (the default background)
4. The primary colours are Red, Green, Blue (not the red/yellow/blue of paint mixing)

# Construction / Recognition

## To Identify/Recognise:
1. Monitors, projectors, and phone screens use additive mixing
2. Identify additive mixing from emitted-light contributions and the specified primaries; a lighter result alone does not identify the operation
3. With full contributions from the specified red and green primaries (for example `rgb(255 0 0)` and `rgb(0 255 0)` in an additive RGB display model), the result is the RGB yellow primary; this does not describe arbitrary CSS interpolation or pigment recipes

# Context & Application

- **Typical contexts**: Display technology, photography, digital colour authoring, stage lighting, CSS colour specification
- **Common applications**: CSS colour values describe colours for rendering; many map to RGB spaces, but this does not make encoded-channel arithmetic, interpolation or compositing equivalent to physical light summation

## Cross-Domain Connections

**Mathematics → STRUCTURAL**: Additive colour mixing corresponds structurally to vector addition. Each colour channel (R, G, B) is a component; combining colours is summing the vectors. The analogy applies to linear-light channel coordinates under fixed primaries. Encoded sRGB values are nonlinear; averaging, CSS interpolation and alpha compositing are separate operations.

# Examples

**Example 1** (source claim, bounded): Drasner says red and green create yellow. For emitted RGB light this means full red plus full green primary contributions; it is not a general rule for every digital colour operation or pigment mixture.

**Example 2** (from source): Monitors as "many combinations of small bits of light combined that resonate to create a myriad of colors" — each pixel is a small additive mixture of R, G, B sub-pixels.

# Relationships

## Builds Upon
- **Physics of light** — Additive mixing models the summation of emitted light under specified primaries

## Enables
- **RGB colour model** — RGB is a coordinate system for specifying display colours; linear-light RGB channel contributions add for fixed primaries
- **Colour bit depth** — Bit allocation can quantize encoded RGB values; it does not itself define physical light intensity or gamut
- **CSS colour specification** — CSS values are rendered as colours; some RGB spaces model additive light, while notation and interpolation remain distinct

## Related
- **HSL colour space** — CSS HSL is a cylindrical transformation of sRGB coordinates; this is a representational relationship, not a claim that HSL channel arithmetic adds light

## Contrasts With
- **Subtractive colour mixing** — Contrasts emitted-light mixing with pigment absorption; actual pigment mixtures depend on materials and conditions

# Common Errors

- **Error**: Treating every operation on digital colour values as additive light mixing.
  **Correction**: Additive mixing describes emitted-light contributions under specified primaries. It does not determine encoded-sRGB interpolation, blend modes, alpha compositing or pigment outcomes. For full red and green RGB primary contributions, the additive result is yellow.

# Common Confusions

- **Confusion**: Monitors use subtractive mixing because they produce colours by "filtering" the backlight.
  **Clarification**: LCD screens do filter light, but the resulting pixel colour is perceived additively by the eye — the colour model of the output is still additive RGB.

# Source Reference

"Color mixing" section, Working With Colors Guide (Sarah Drasner).

# Verification Notes

- Current technical support: [CSS Color 4 §2](https://www.w3.org/TR/2026/CRD-css-color-4-20261009/#color-space) distinguishes additive linear-light colour spaces from gamma-encoded RGB; the gamut of real displays is bounded. This 2026-10-09 Candidate Recommendation Draft is work in progress.

- Definition source: Direct quotes from Drasner
- Confidence rationale: High — Drasner provides a clear, dedicated section on this concept
- Uncertainties: None significant
- Cross-reference status: Not discussed in Ottosson source
- Rosetta Stone check: Mathematics/vector-addition mapping added as structural
- OCR issues: HTML figure markup stripped; prose content clean
