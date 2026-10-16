---
concept: "Colour Bit Depth"
slug: "colour-bit-depth"
category: "colour-theory"
subcategory: "digital-colour"
tier: "foundational"
layer: "2-domain"
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
    - "bit depth"
    - "color depth"
    - "True Color"
prerequisites:
  - "additive-colour-mixing"
extends: []
related:
  - "rgb-colour-model"
  - "hex-colour-notation"
contrasts_with: []
answers_questions:
  - "What is the relationship between bit depth and available colour range?"
rosetta_stone:
  -
    domain: "mathematics"
    concept: "Binary exponentiation (2^n)"
    rating: "rigorous"
    note: "For a specified n-bit field there are 2^n bit patterns; for three independent 8-bit RGB channels there are 2^24 combinations. Keep the field/channel allocation explicit: this count is not a gamut or human-discrimination claim."
---

# Quick Definition

Bit depth describes the number of bits used for a particular encoded value. State whether the count is per channel or per pixel: three independent 8-bit RGB channels yield 256³ = 16,777,216 code combinations; RGBA8 uses 32 bits per pixel including alpha. These counts do not specify gamut or reproduction accuracy.

# Core Definition

Drasner describes the growth in representable values with bit depth and gives a 24-bit RGB example. Her prepared passage also associates 32-bit with alpha and asserts a fixed human discrimination count; those are source claims, not general guarantees. An n-bit field has 2^n patterns. Three 8-bit RGB channels have 2^24 = 16,777,216 combinations. RGBA8 is a common 32-bit allocation, but formats allocate bits differently; a larger code count does not by itself increase gamut, accuracy or match a universal vision threshold.

# Prerequisites

- **Additive colour mixing** — A storage format may quantise encoded channel values used to represent colour; bit depth does not itself quantise a physical light spectrum

# Key Properties

1. An n-bit field has 2^n patterns; 8-bit channels have 256 patterns each
2. 24-bit RGB8 has 8 bits × 3 channels = 16,777,216 code combinations
3. RGBA8 is one common 32-bit-per-pixel allocation; other formats allocate channels differently
4. Code combinations do not establish a fixed number of distinguishable colours

# Construction / Recognition

## To Identify/Recognise:
1. Legacy numeric CSS RGB components use a 0–255 scale, but CSS syntax permits fractional and percentage values and does not assert 8-bit storage
2. Hex colour values use two hexadecimal digits per channel (00–FF), representing 256 values = 8 bits
3. A one-bit field has two code patterns; whether a display uses them for black/white is a format/device choice

# Context & Application

- **Typical contexts**: Display technology specifications, image file formats, CSS colour value ranges
- **Common applications**: Understanding why RGB values go from 0 to 255; understanding why hex colours have 6 digits (2 per channel × 3 channels)

## Cross-Domain Connections

**Mathematics → RIGOROUS**: An n-bit field has exactly 2^n bit patterns. Three independent 8-bit RGB fields have 256^3 = 2^24 = 16,777,216 code combinations. The channel allocation must be stated; the count does not specify gamut or how many colours a person can distinguish.

# Examples

**Example 1** (from source): "In terms of web color values in an RGB channel, we specify color on a range from 0-255" — Drasner’s historical description of the legacy 0–255 component scale; CSS syntax does not prescribe channel storage depth.

# Relationships

## Builds Upon
- **Additive colour mixing** — Bit depth quantises encoded channel values; it does not define the continuous light spectrum

## Enables
- **RGB colour model** — CSS `rgb()` accepts numeric 0–255 values and percentages; this syntax is not a promise of 8-bit storage
- **Hex colour notation** — Six-digit CSS hex uses two digits per sRGB channel; this encoding has 8 bits per channel

## Related
- **Alpha channel** — Some formats allocate a separate alpha field; RGBA8 is one common 32-bit layout

# Common Errors

- **Error**: Assuming 32-bit colour means more colour than 24-bit.
  **Correction**: RGBA8 is one common 32-bit allocation with 8 bits each for RGB and alpha; the label “32-bit colour” alone does not guarantee that layout.

# Common Confusions

- **Confusion**: "True Color" means the display can show colours that look exactly like reality.
  **Clarification**: “True Color” is a format label associated with 24-bit RGB code combinations; it does not guarantee accurate reproduction or a universal human discrimination threshold.

# Source Reference

"Color mixing" section, Working With Colors Guide (Sarah Drasner).

# Verification Notes

- Current technical context: [CSS Color 4 §5.1](https://www.w3.org/TR/2026/CRD-css-color-4-20261009/#rgb-functions) defines CSS RGB values; bit allocation is a storage-format property, distinct from CSS gamut.

- Definition source: Direct quotes from Drasner
- Confidence rationale: High — explicitly defined with specific numbers
- Uncertainties: None significant
- Cross-reference status: Not in Ottosson source
- Rosetta Stone check: Mathematics/binary-exponentiation added as rigorous
- OCR issues: None significant
