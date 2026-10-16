---
concept: "Hex Colour Notation"
slug: "hex-colour-notation"
category: "colour-theory"
subcategory: "colour-notation"
tier: "foundational"
layer: "3-implementation"
source: "Working With Colors Guide"
source_slug: "posts"
authors: "Sarah Drasner"
chapter: "Color values / Hex Values"
chapter_number: null
pdf_page: null
section: null
extraction_confidence: "high"
aliases:
  -
    - "hex color"
    - "hexadecimal color"
    - "#rrggbb"
prerequisites:
  - "rgb-colour-model"
  - "colour-bit-depth"
extends:
  - "rgb-colour-model"
related:
  - "rgb-colour-model"
  - "css-rgba"
contrasts_with:
  - "hsl"
answers_questions:
  - "What is the relationship between bit depth and available colour range?"
rosetta_stone:
  -
    domain: "mathematics"
    concept: "Base-16 (hexadecimal) positional numeral system"
    rating: "rigorous"
    note: "Hex colour notation is literally base-16 positional notation. Each two-character group represents one byte (8 bits, 0–255 in decimal, 00–FF in hex). The mapping is exact and mechanical."
---

# Quick Definition

CSS hexadecimal notation encodes sRGB channels as `#RGB`, `#RGBA`, `#RRGGBB` or `#RRGGBBAA`. In the four/eight-digit forms the final component is alpha. Each full pair is one 8-bit value; shorthand duplicates each digit (`#0f08` → `#00ff0088`). Numeric `rgb()` can express fractional values that an 8-bit hex channel cannot.

# Core Definition

Drasner presents hexadecimal as another way to represent the same RGB values and describes it as a common web notation; that popularity statement is attributed to her prepared article, not a universal current ranking. She explains that each full two-digit channel is a byte (00–FF, or 0–255), ordered red, green and blue, and demonstrates shorthand with `#00FFFF` becoming `#0FF`. CSS also defines four/eight-digit forms with alpha last. Shorthand expands only when each channel's two digits repeat. The prepared passage contains a `#00000` typo for black; the valid six-digit value is `#000000`.

# Prerequisites

- **RGB colour model** — Hex is an alternative encoding of the same R, G, B integer values
- **Colour bit depth** — Each hex pair represents one 8-bit byte (0–255)

# Key Properties

1. CSS supports 3/4/6/8 hexadecimal digits: RGB, RGBA, RRGGBB, RRGGBBAA
2. Values 00–FF per channel correspond to decimal 0–255
3. Shorthand `#RGB` works when each hex pair has repeated digits (e.g. `#AABBCC` → `#ABC`)
4. Case-insensitive: `#FF0000` and `#ff0000` are equivalent

# Construction / Recognition

## To Construct/Create:
1. Take the decimal R, G, B values (0–255)
2. Convert each to a two-digit hexadecimal string (0 → "00", 255 → "FF", 128 → "80")
3. Concatenate as `#RRGGBB`

## To Identify/Recognise:
1. Starts with `#` followed by exactly 3, 4, 6 or 8 hexadecimal digits using [0-9A-Fa-f]; 4/8-digit forms include alpha last
2. `#000000` = black; `#FFFFFF` = white; `#FF0000` = red; `#00FF00` = green; `#0000FF` = blue

# Context & Application

- **Typical contexts**: CSS stylesheets, design tool colour exports, HTML attributes, JSON colour tokens
- **Common applications**: Copy-pasting colours from design tools into code; storing colours in configuration files; version control (hex changes are diff-visible)

## Cross-Domain Connections

**Mathematics → RIGOROUS**: Hex colour notation is direct base-16 positional notation. Converting `#FF0000` to decimal: FF = 15×16+15 = 255 (red channel at max); 00 = 0 (green off); 00 = 0 (blue off). The encoding is a mechanical mathematical identity.

# Examples

**Example 1** (from source): "`#00FFFF` becomes `#0FF`" — Drasner's example of the shorthand rule; each channel pair (00, FF, FF) has a repeated digit so each reduces to one character.

**Example 2** (corrected source-example paraphrase): the prepared passage’s `#00000` appears to be a typo; valid six-digit black is `#000000`, while `#FFFFFF` is white.

# Relationships

## Builds Upon
- **RGB colour model** — Hex encodes the same R, G, B values as rgb()
- **Colour bit depth** — Two hex digits per channel = one byte = 8 bits = 256 values

## Enables
- **Design token storage** — Hex is one possible notation for sRGB token values; a project may choose another representation

## Related
- **CSS rgba()** — `#RGBA` and `#RRGGBBAA` also encode alpha; `rgba()` is an alternative notation

## Contrasts With
- **HSL** — Drasner notes: "if you're going to work with colors in a more involved way, though, HSL is a little bit more human-readable"

# Common Errors

- **Error**: Expecting `#RGB` shorthand to work for all hex colours.
  **Correction**: Shorthand only works when each channel's two hex digits are identical: `#AABBCC` → `#ABC`. `#A1B2C3` cannot be shortened.

- **Error**: Using hex for programmatic colour manipulation.
  **Correction**: Hex is a notation, not a prohibition on string processing. Numeric RGB or another suitable colour space may be more convenient for calculations; convert when the required output format is hex.

# Common Confusions

- **Confusion**: Longer hex strings mean more colours.
  **Clarification**: Standard 6-digit hex has the same colour gamut as rgb(). 8-digit hex (`#RRGGBBAA`) adds an alpha channel but does not expand the colour gamut.

# Source Reference

"Hex Values" section under "Color values," Working With Colors Guide (Sarah Drasner).

# Verification Notes

- Current syntax and alpha ordering: [CSS Color 4 §5.2](https://www.w3.org/TR/2026/CRD-css-color-4-20261009/#hex-notation) defines all four forms and shorthand expansion.

- Definition source: Direct quotes from Drasner
- Confidence rationale: High — complete and explicit definition with examples
- Uncertainties: Drasner's article predates 8-digit hex support becoming widely available; omits alpha-in-hex
- Cross-reference status: Not in Ottosson source
- Rosetta Stone check: Mathematics/base-16 mapping added as rigorous
- OCR issues: None significant
