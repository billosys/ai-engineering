---
# === CORE IDENTIFICATION ===
concept: Hue
slug: hue

# === CLASSIFICATION ===
category: colour-theory
subcategory: colour-properties
tier: foundational
layer: 2-domain

# === PROVENANCE ===
source: "Art and Visual Perception: A Psychology of the Creative Eye"
source_slug: art-and-visual-perception
authors: "Rudolf Arnheim"
chapter: "VII. Color"
chapter_number: 7
pdf_page: 371
section: "The Generative Primaries"

# === CONFIDENCE ===
extraction_confidence: medium

# === VARIANTS ===
aliases:
  - chromatic quality
  - colour quality

# === TYPED RELATIONSHIPS ===
prerequisites: []
extends: []
related:
  - saturation
  - tonal-value
  - colour-constancy
  - simultaneous-contrast
  - complementary-colours
  - colour-temperature
contrasts_with:
  - tonal-value
  - saturation

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is the difference between hue, saturation/chroma, and lightness/value?"
  - "What are the three components of HSL, and why is HSL more useful than hex notation for palette construction?"

# === VISUAL DESIGN EXTENSIONS ===
rosetta_stone:
  - domain: mathematics
    concept: "Angular coordinate on a circular/cylindrical colour space"
    rating: rigorous
    note: "In OKLCH and HSL, hue is represented as an angle (0–360°) on the hue circle, a mathematical encoding of the perceptual hue dimension."
  - domain: music
    concept: "Pitch class (note quality, e.g. C, D, E)"
    rating: loose
    note: "Both hue and pitch class are circular, categorical qualities that cycle back to their starting point, but the perceptual mechanisms and interval structures differ entirely."

css_implementation:
  - property: "hue (in oklch/hsl)"
    example: "color: oklch(0.6 0.15 270); /* hue = 270° (blue-violet) */"
    support: baseline
  - property: "filter: hue-rotate()"
    example: "filter: hue-rotate(90deg);"
    support: baseline
---

# Quick Definition

Hue is the chromatic quality of a colour — the dimension that distinguishes red from green from blue from yellow — independent of how light or dark or how pure or greyish the colour is.

# Core Definition

Hue is the perceptual dimension of colour experience that corresponds to what we ordinarily mean when we say a colour is "red," "orange," "yellow," "green," "blue," or "violet." Arnheim treats hue as the fundamental chromatic identity of a colour, clearly distinguishing it from brightness (the light-dark dimension) and saturation (the purity dimension). In discussing the spectrum and colour organisation, he notes that "the sequence leads seamlessly from one hue to the next" and that pure hues are defined by their perceptual irreducibility: "a blue or yellow or red is pure because it is an irreducible element, i.e., it does not look like a mixture" (Chapter VII, p. 379).

Hue is the quality that makes red and blue perceivably different chromatic qualities while two greys of different lightness remain in the same chromatic category. Arnheim identifies three fundamental primaries — red, yellow, and blue — as the pure hues that serve as irreducible elements from which all others are perceived as mixtures.

Note: Arnheim's account is phenomenological and predates mathematical colour science. In OKLCH and CIELAB, hue is formalised as an angular dimension (H = 0–360°) in a cylindrical colour space designed for perceptual uniformity.

# Prerequisites

- None — hue is a foundational atomic concept in colour perception.

# Key Properties

1. **Categorical but continuous** — Hue is experienced in recognisable categories (red, orange, etc.) but varies continuously through the spectrum.
2. **Circular** — The hue dimension wraps around: violet connects back to red.
3. **Independent of lightness and saturation** — A dark blue and a light blue share a hue; a vivid red and a grey-red share a hue.
4. **Three fundamental primaries** — Red, yellow, and blue are the perceptually irreducible (fundamental) hues from which all other hues are perceived as mixtures.
5. **Chromatic identity** — Hue is what changes when a colour "becomes" another colour (red becomes orange becomes yellow); lightness and saturation changes modify a colour without changing its hue identity.

# Construction / Recognition

## To Construct/Create:
1. Start with a pure fundamental (red, yellow, or blue) as an anchor hue.
2. Mix adjacent primaries to produce secondaries (orange, green, violet).
3. Specify hue precisely using H in HSL or OKLCH — the angular value (e.g. 270° for blue-violet).
4. Distinguish hue shifts from lightness or saturation shifts: only changing the angular coordinate changes hue.

## To Identify/Recognise:
1. Name the chromatic quality of the colour — what colour "family" does it belong to?
2. Ignore lightness (how bright?) and saturation (how vivid?); focus only on chromatic identity.
3. In colour tools, isolate the H channel in HSL or OKLCH.

# Context & Application

- **Typical contexts**: Palette construction, brand colour selection, colour coding, information visualisation, colour harmony.
- **Common applications**: Distinguishing categories in data visualisation (each category gets a distinct hue); brand identity (a brand's signature hue); colour harmony (selecting hues at specific angular relationships).

## Cross-Domain Connections

**Mathematics → RIGOROUS**: In OKLCH and HSL, hue is encoded as an angle H ∈ [0°, 360°), making it a coordinate on a circle. Rotating H by 180° gives the complementary hue. Equal angular steps in OKLCH approximate equal perceptual hue differences — a property not available in earlier models like HSL.

**Music → LOOSE**: Pitch class (C, D, E...) and hue both cycle and return to origin. However, the 12-semitone octave has no rigorous analogue in the hue circle, which has no natural discrete step size; the comparison is structural at best and breaks down under analysis.

# Examples

**Example 1** (p. 371): Arnheim opens Chapter VII by observing that a red ball on green grass is discriminated by its hue alone — "the intense red color that sets it apart from the green grass" — illustrating hue as the primary chromatic discrimination dimension.

**Example 2** (p. 379): The spectrum as a seamless continuum — yet certain hues stand out as perceptually pure (red, yellow, blue), demonstrating the categorical structure of hue perception despite its physical continuity.

**Example 3** (p. 382): Cézanne's use of pure hue: "Cézanne often indicates the highest point of a convexity — a cheek or an apple — by a pure red spot." The hue identity (redness) is isolated from lightness and saturation effects.

# Relationships

## Builds Upon
- None — hue is a foundational colour element.

## Enables
- **Saturation** — Saturation is the degree to which a colour's hue is expressed (vs. diluted toward grey).
- **Complementary colours** — Complementary relationships are defined by hue relationships (opposite hues on the colour wheel).
- **Colour harmony** — Harmonic colour relationships (complementary, analogous, triadic) are described in terms of hue angles.
- **Colour temperature** — Warm/cool distinction correlates partially with hue (reds/yellows warm, blues/greens cool).

## Related
- **Tonal value** — The light-dark dimension; independent of hue.
- **Saturation** — The purity dimension; orthogonal to hue.
- **Colour constancy** — The perceptual stability of hue under changing illumination.

## Contrasts With
- **Tonal value** — Value is the light-dark dimension; hue is the chromatic dimension.
- **Saturation** — Saturation describes how vivid or grey a colour is; hue describes which chromatic quality it has.

# Common Errors

- **Error**: Treating hue as equivalent to colour (using "hue" to mean the full colour).
  **Correction**: Hue is one dimension of colour. A full colour specification requires hue, saturation, and lightness/value.

- **Error**: Assuming HSL hue angles are perceptually uniform (equal steps = equal perceived difference).
  **Correction**: HSL is device-dependent and perceptually non-uniform. Use OKLCH for perceptually uniform hue manipulation.

# Common Confusions

- **Confusion**: "Changing the hue of a colour changes its lightness too."
  **Clarification**: In perceptually non-uniform models (HSL, HSV), this appears true because different hues have different intrinsic luminance (yellow is lighter than blue at equal HSL saturation). In OKLCH, hue and lightness are decoupled.

- **Confusion**: "Red, yellow, and blue are the primaries because of physics."
  **Clarification**: Arnheim's "fundamental primaries" (red, yellow, blue) are perceptual — based on phenomenal irreducibility in experience. The physical/generative primaries for light (red, green, blue) and pigment (cyan, magenta, yellow) differ and serve different practical purposes.

# Source Reference

Chapter VII: Color, "Art and Visual Perception," pp. 371–382 (sections "From Light to Color," "Shape and Color," "How Colors Come About," "The Generative Primaries").

# Verification Notes

- Definition source: Synthesised from discussion throughout Chapter VII. Arnheim does not give a single explicit definition of hue; the account is built from his discussion of the spectrum, primaries, and colour properties.
- Confidence rationale: Medium — Arnheim's treatment is phenomenological and distributed across the chapter. He uses "hue" as a technical term but does not define it in isolation from the broader colour discussion.
- Uncertainties: Arnheim's "fundamental primaries" (R, Y, B) differ from modern tristimulus primaries and from painter's process primaries (C, M, Y). The card preserves Arnheim's perceptual framing while noting the discrepancy.
- Cross-reference status: Verified — maps to H in OKLCH/HSL. Arnheim predates CIELAB (1976) and OKLAB (2020); his hue account is perceptual/phenomenological without mathematical specification.
- Rosetta Stone check: Mappings added (mathematics: angular coordinate, rigorous; music: pitch class, loose).
- OCR issues: None detected.
