---
concept: Colour Bit Depth
slug: colour-bit-depth
category: colour-theory
subcategory: digital-colour
tier: foundational
layer: 2-domain
source: "Working With Colors Guide"
source_slug: posts
authors: "Sarah Drasner"
chapter: "Color mixing"
chapter_number: null
pdf_page: null
section: null
extraction_confidence: high
aliases:
  - ["bit depth", "color depth", "True Color"]
prerequisites:
  - additive-colour-mixing
extends:
  - []
related:
  - rgb-colour-model
  - hex-colour-notation
contrasts_with:
  - []
answers_questions:
  - "What is the relationship between bit depth and available colour range?"
rosetta_stone:
  - domain: mathematics
    concept: "Binary exponentiation (2^n)"
    rating: rigorous
    note: "The number of representable colours at a given bit depth is exactly 2^n. At 24-bit (3\u00d78-bit channels) this is 2^24 = 16,777,216. This is a direct mathematical identity, not an analogy."
---

# Quick Definition

Colour bit depth specifies how many bits are used to encode colour information per pixel; higher bit depth allows more distinct colour values to be represented, with 24-bit being the standard for web displays ("True Color").

# Core Definition

Drasner explains: "Monitors are made in a few different display modes that change the way we perceive color through them. We express this the term 'color bit depth'. The number of colors that can be displayed at one time is determined by this color bit depth. If we have a bit depth of 1, we can produce two colors, or monochrome. Bit depth of two levels creates 4, and so on until we reach a bit-depth of 32, though commonly monitors that project the web have 24 bit-depth density and 16,777,216 colors which is True Color and Alpha Channel." She further explains: "We call this True Color because our human eyes can discern 10,000,000 unique colors, so 24-bit depth will certainly allow for this. In this 24-bit depth, 8 bits are dedicated to red, green, and blue. The rest are used for transparency or alpha channels."

# Prerequisites

- **Additive colour mixing** \u2014 Bit depth quantises the continuous additive light values into discrete steps

# Key Properties

1. Bit depth n \u2192 2^n representable values per channel; for 8-bit: 256 values (0\u2013255) per R, G, B channel
2. 24-bit "True Color" = 8 bits \u00d7 3 channels = 16,777,216 distinct colours
3. 32-bit adds an 8-bit alpha channel for transparency, leaving 24 bits for colour
4. Human vision can distinguish approximately 10,000,000 colours \u2014 24-bit exceeds this threshold

# Construction / Recognition

## To Identify/Recognise:
1. CSS rgb() and rgba() values range from 0\u2013255 per channel \u2014 this is the 8-bit range
2. Hex colour values use two hexadecimal digits per channel (00\u2013FF), representing 256 values = 8 bits
3. A "1-bit" display is monochrome (two colours: black/white)

# Context & Application

- **Typical contexts**: Display technology specifications, image file formats, CSS colour value ranges
- **Common applications**: Understanding why RGB values go from 0 to 255; understanding why hex colours have 6 digits (2 per channel \u00d7 3 channels)

## Cross-Domain Connections

**Mathematics \u2192 RIGOROUS**: The number of colours at n-bit depth is exactly 2^n. At 24 bits: 2^24 = 16,777,216. Per-channel at 8 bits: 2^8 = 256. This is a direct mathematical identity.

# Examples

**Example 1** (from source): "In terms of web color values in an RGB channel, we specify color on a range from 0-255" \u2014 Drasner's description of the 8-bit-per-channel range that underlies CSS rgb() values.

# Relationships

## Builds Upon
- **Additive colour mixing** \u2014 Bit depth quantises the continuous spectrum of additive light values

## Enables
- **RGB colour model** \u2014 The 0\u2013255 range in CSS rgb() is the direct expression of 8-bit channels
- **Hex colour notation** \u2014 Hex uses two hexadecimal digits (00\u2013FF) to represent each 8-bit channel

## Related
- **Alpha channel** \u2014 The extra 8 bits in 32-bit colour are used for transparency

# Common Errors

- **Error**: Assuming 32-bit colour means more colour than 24-bit.
  **Correction**: 32-bit colour typically uses the same 24 bits for RGB colour as 24-bit, with the extra 8 bits dedicated to an alpha (transparency) channel.

# Common Confusions

- **Confusion**: "True Color" means the display can show colours that look exactly like reality.
  **Clarification**: "True Color" is a technical term meaning the display has sufficient bit depth (24-bit) to exceed human colour discrimination ability (~10 million colours). It does not guarantee accurate reproduction of absolute colour values.

# Source Reference

"Color mixing" section, Working With Colors Guide (Sarah Drasner).

# Verification Notes

- Definition source: Direct quotes from Drasner
- Confidence rationale: High \u2014 explicitly defined with specific numbers
- Uncertainties: None significant
- Cross-reference status: Not in Ottosson source
- Rosetta Stone check: Mathematics/binary-exponentiation added as rigorous
- OCR issues: None significant
