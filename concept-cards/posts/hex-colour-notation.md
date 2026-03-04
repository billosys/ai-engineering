---
concept: Hex Colour Notation
slug: hex-colour-notation
category: colour-theory
subcategory: colour-notation
tier: foundational
layer: 3-implementation
source: "Working With Colors Guide"
source_slug: posts
authors: "Sarah Drasner"
chapter: "Color values / Hex Values"
chapter_number: null
pdf_page: null
section: null
extraction_confidence: high
aliases:
  - ["hex color", "hexadecimal color", "#rrggbb"]
prerequisites:
  - rgb-colour-model
  - colour-bit-depth
extends:
  - rgb-colour-model
related:
  - rgb-colour-model
  - css-rgba
contrasts_with:
  - hsl
answers_questions:
  - "What is the relationship between bit depth and available colour range?"
rosetta_stone:
  - domain: mathematics
    concept: "Base-16 (hexadecimal) positional numeral system"
    rating: rigorous
    note: "Hex colour notation is literally base-16 positional notation. Each two-character group represents one byte (8 bits, 0\u2013255 in decimal, 00\u2013FF in hex). The mapping is exact and mechanical."
---

# Quick Definition

Hex colour notation is a compact hexadecimal encoding of RGB colour values as a six-character string (preceded by `#`), where each pair of characters encodes one colour channel (0\u2013255 as 00\u2013FF).

# Core Definition

Drasner explains: "Hex colors are a slightly different format to represent the values in the same way. Hex values are probably the most common way developers designate color on the web." The structure: "If you recall that a byte is 8 bits, each Hex color or number represents a byte. A color is specified according to the intensity of its red, green and blue components, so we call it a triplet, with each expressed in two places. One byte represents a number in the range 00 to FF (in hexadecimal notation), or 0 to 255 in decimal notation. Byte 1 is Red, byte 2 is green, and byte 3 is blue." The base: "Hexadecimal is named this because it uses a base 16 system. The values use ranges from 0-9 and A-F, 0 being the lowest value and F being the highest, or `#000000` being black and `#FFFFFF` being white." Shorthand: "For triplets with repeated values, you can eliminate the repetition by writing in shorthand, for instance, `#00FFFF` becomes `#0FF`."

# Prerequisites

- **RGB colour model** \u2014 Hex is an alternative encoding of the same R, G, B integer values
- **Colour bit depth** \u2014 Each hex pair represents one 8-bit byte (0\u2013255)

# Key Properties

1. Six hex digits (plus `#`): two per channel, in R-G-B order
2. Values 00\u2013FF per channel correspond to decimal 0\u2013255
3. Shorthand `#RGB` works when each hex pair has repeated digits (e.g. `#AABBCC` \u2192 `#ABC`)
4. Case-insensitive: `#FF0000` and `#ff0000` are equivalent

# Construction / Recognition

## To Construct/Create:
1. Take the decimal R, G, B values (0\u2013255)
2. Convert each to a two-digit hexadecimal string (0 \u2192 "00", 255 \u2192 "FF", 128 \u2192 "80")
3. Concatenate as `#RRGGBB`

## To Identify/Recognise:
1. Starts with `#` followed by exactly 6 (or 3 shorthand) alphanumeric characters using [0-9A-Fa-f]
2. `#000000` = black; `#FFFFFF` = white; `#FF0000` = red; `#00FF00` = green; `#0000FF` = blue

# Context & Application

- **Typical contexts**: CSS stylesheets, design tool colour exports, HTML attributes, JSON colour tokens
- **Common applications**: Copy-pasting colours from design tools into code; storing colours in configuration files; version control (hex changes are diff-visible)

## Cross-Domain Connections

**Mathematics \u2192 RIGOROUS**: Hex colour notation is direct base-16 positional notation. Converting `#FF0000` to decimal: FF = 15\u00d716+15 = 255 (red channel at max); 00 = 0 (green off); 00 = 0 (blue off). The encoding is a mechanical mathematical identity.

# Examples

**Example 1** (from source): "`#00FFFF` becomes `#0FF`" \u2014 Drasner's example of the shorthand rule; each channel pair (00, FF, FF) has a repeated digit so each reduces to one character.

**Example 2** (from source): "`#000000` being black and `#FFFFFF` being white" \u2014 the boundary values.

# Relationships

## Builds Upon
- **RGB colour model** \u2014 Hex encodes the same R, G, B values as rgb()
- **Colour bit depth** \u2014 Two hex digits per channel = one byte = 8 bits = 256 values

## Enables
- **Design token storage** \u2014 Hex is the most common format for storing colours in design tokens and configuration files

## Related
- **CSS rgba()** \u2014 For alpha channel support, rgba() is needed; CSS Color 4 adds `#RRGGBBAA` 8-digit hex

## Contrasts With
- **HSL** \u2014 Drasner notes: "if you're going to work with colors in a more involved way, though, HSL is a little bit more human-readable"

# Common Errors

- **Error**: Expecting `#RGB` shorthand to work for all hex colours.
  **Correction**: Shorthand only works when each channel's two hex digits are identical: `#AABBCC` \u2192 `#ABC`. `#A1B2C3` cannot be shortened.

- **Error**: Using hex for programmatic colour manipulation.
  **Correction**: Hex is string-based and difficult to manipulate mathematically. For programmatic adjustment, use HSL or RGB numeric forms and convert to hex for output.

# Common Confusions

- **Confusion**: Longer hex strings mean more colours.
  **Clarification**: Standard 6-digit hex has the same colour gamut as rgb(). 8-digit hex (`#RRGGBBAA`) adds an alpha channel but does not expand the colour gamut.

# Source Reference

"Hex Values" section under "Color values," Working With Colors Guide (Sarah Drasner).

# Verification Notes

- Definition source: Direct quotes from Drasner
- Confidence rationale: High \u2014 complete and explicit definition with examples
- Uncertainties: Drasner's article predates 8-digit hex support becoming widely available; omits alpha-in-hex
- Cross-reference status: Not in Ottosson source
- Rosetta Stone check: Mathematics/base-16 mapping added as rigorous
- OCR issues: None significant
