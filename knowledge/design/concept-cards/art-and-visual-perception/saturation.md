---
# === CORE IDENTIFICATION ===
concept: Saturation
slug: saturation

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
section: "Interaction of Color"

# === CONFIDENCE ===
extraction_confidence: medium

# === VARIANTS ===
aliases:
  - chroma
  - purity
  - colour intensity
  - vividness

# === TYPED RELATIONSHIPS ===
prerequisites:
  - hue
extends: []
related:
  - hue
  - tonal-value
  - simultaneous-contrast
  - colour-constancy
contrasts_with:
  - tonal-value
  - achromatic-colour

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is the difference between hue, saturation/chroma, and lightness/value?"
  - "What are the three components of HSL, and why is HSL more useful than hex notation for palette construction?"
  - "How do you ensure a coloured status badge communicates its meaning without relying solely on colour? What redundant encoding strategies exist?"

# === VISUAL DESIGN EXTENSIONS ===
rosetta_stone:
  - domain: mathematics
    concept: "Chroma (C) in cylindrical colour spaces (OKLCH)"
    rating: rigorous
    note: "In OKLCH, chroma C is the radial distance from the achromatic axis, directly representing saturation in a perceptually uniform space."

css_implementation:
  - property: "chroma (in oklch)"
    example: "color: oklch(0.6 0.25 150); /* chroma = 0.25, high saturation */"
    support: baseline
  - property: "saturation (in hsl)"
    example: "color: hsl(150 80% 45%); /* saturation = 80% */"
    support: baseline
  - property: "filter: saturate()"
    example: "filter: saturate(1.5);"
    support: baseline
---

# Quick Definition

Saturation is the dimension of colour experience that describes how vivid or chromatic a colour is — how much pure hue it contains versus how much grey or neutrality dilutes it.

# Core Definition

Saturation (also termed chroma or purity) is the degree to which a colour's hue quality is expressed in its full intensity, as opposed to being diluted by grey or white. A fully saturated red is the most intensely red possible at a given lightness; a desaturated red is a dull, greyish pink or grey. Arnheim addresses saturation as a key dimension of colour that interacts with hue and brightness to determine colour character and distinctiveness.

He notes that "the distinctness of color depends more upon brightness than upon hue" (p. 389) and explicitly treats saturation as a distinct dimension: colours can be related not only by hue but "also be related only through their brightness or saturation, not as hues" (Chapter VII, p. 382). In discussing colour contrast, he states: "Relations between hues cannot be described adequately without reference to saturation and brightness" (p. 389).

Arnheim also discusses the concept under the related term "purity": "If we examine the raw material of color gradations... we observe that certain colors are distinguished by their purity... an orange or a green looks pure when it is only itself, e.g., without an admixture that would make us speak of a reddish orange or a yellowish green" (p. 379). He carefully distinguishes perceptual purity from physical/spectral purity.

Note: Arnheim's treatment is phenomenological (1954/1974) and predates the mathematical formalisation of chroma in CIELAB (1976) and OKLCH (2020).

# Prerequisites

- **Hue** — Saturation is the degree of expression of a colour's hue; without hue identity, there is nothing to saturate or desaturate.

# Key Properties

1. **Chromatic intensity** — High saturation = vivid, fully chromatic; low saturation = dull, grey-like.
2. **Zero saturation = achromatic** — At zero saturation, all hues converge to grey (at their respective lightness level).
3. **Independent of hue** — Any hue can have any level of saturation.
4. **Interacts with value** — Very dark or very light colours are perceptually limited in achievable saturation; mid-lightness colours can achieve the highest chromaticity.
5. **Perceptually distinct from lightness** — Desaturation is not the same as darkening; a desaturated colour is greyer, not darker.

# Construction / Recognition

## To Construct/Create:
1. Start with a fully saturated hue (a pure pigment or the maximum chroma at a given H/L in OKLCH).
2. Reduce saturation by mixing in grey (or in digital: reduce the C/chroma value in OKLCH, or the S value in HSL).
3. Monitor that only saturation changes, not lightness — desaturating should not darken the colour.

## To Identify/Recognise:
1. Ask: is this colour vivid (high saturation) or dull/greyish (low saturation)?
2. Convert to HSL or OKLCH and inspect the S/chroma value.
3. Squinting does not suppress saturation the way it does tonal differences; instead, compare chromatic intensity directly.

# Context & Application

- **Typical contexts**: Palette construction (brand, UI, data viz), colour hierarchy, emotional tone, accessibility.
- **Common applications**: High saturation for emphasis, alerts, and calls to action; low saturation for backgrounds and supporting text; systematic saturation reduction for disabled/inactive states.

## Cross-Domain Connections

**Mathematics → RIGOROUS**: In OKLCH, saturation corresponds to the chroma axis C (the radial distance from the neutral grey axis in the Oklab colour space). This is a mathematically precise, perceptually uniform encoding: equal changes in C correspond to equal perceived changes in chromatic intensity. Arnheim's phenomenological account predates this formalisation; his observation that colours can be related "through their saturation" anticipates the chroma dimension without specifying it mathematically.

# Examples

**Example 1** (p. 379): Arnheim's discussion of colour purity — "an orange or a green looks pure when it is only itself, e.g., without an admixture that would make us speak of a reddish orange." Purity here is saturation: the degree to which the hue is unmixed and fully expressed.

**Example 2** (p. 389): Liebmann's experiment — placing a red figure on a green background of equal brightness makes boundaries "fluid, soft, colloidal." The colour boundary is visible because the hues differ, but the perceptual separation weakens. Adding saturation contrast (not just hue) strengthens figure-ground.

**Example 3** (p. 382): In describing mixtures of primaries, Arnheim notes that pure primaries "can be related only through their brightness or saturation, not as hues" — establishing saturation as an independent relational axis between colours.

# Relationships

## Builds Upon
- **Hue** — Saturation is the degree to which a hue is expressed; it presupposes a hue to saturate.

## Enables
- **Colour harmony** — Saturation parity or controlled saturation contrast is a key tool in palette construction.
- **Simultaneous contrast** — Contrast effects alter perceived saturation as well as hue.
- **Colour weight** — Highly saturated colours tend to carry more visual weight and attract more attention.

## Related
- **Tonal value** — The light-dark dimension; orthogonal to saturation (a dark colour can be highly saturated).
- **Achromatic colour** — The limit state of zero saturation; white, grey, and black are achromatic.
- **Simultaneous contrast** — Contrast effects can shift perceived saturation as well as hue.

## Contrasts With
- **Tonal value** — Value describes lightness/darkness; saturation describes chromatic purity/intensity.
- **Achromatic colour** — Achromatic colours have zero saturation by definition.

# Common Errors

- **Error**: Equating desaturation with darkening (reducing saturation to make a colour "less prominent").
  **Correction**: Desaturation shifts a colour toward grey at the same lightness; darkening reduces lightness. Both reduce prominence but in different ways with different perceptual effects.

- **Error**: Assuming maximum HSL saturation (S=100%) means maximum perceptual saturation.
  **Correction**: HSL saturation is not perceptually uniform and not gamut-aware. At the same HSL saturation, different hues appear perceptually different in intensity. OKLCH chroma is more reliable for perceptually consistent saturation.

# Common Confusions

- **Confusion**: "Saturation and brightness are the same — a bright colour is saturated."
  **Clarification**: Saturation and brightness are independent. A bright yellow can be desaturated (a pale, washed-out yellow); a dark navy is low-brightness but can be high-saturation. They are orthogonal dimensions.

- **Confusion**: "Chroma and saturation are the same thing."
  **Clarification**: In common usage, often treated as synonyms. Technically, chroma is the absolute chromatic intensity (used in CIELAB/OKLCH), while saturation in some models (HSL) is chroma relative to the maximum achievable at that lightness. The distinction matters in implementation but not in Arnheim's phenomenological account.

# Source Reference

Chapter VII: Color, "Art and Visual Perception," pp. 379–389 (sections "The Generative Primaries," "Fundamental Primaries," "Syntax of Combinations," "Interaction of Color").

# Verification Notes

- Definition source: Synthesised from distributed discussion. Arnheim treats saturation/purity as a key dimension throughout Chapter VII but does not isolate it in a single definitional passage.
- Confidence rationale: Medium — the concept is clearly present and used technically, but Arnheim's treatment is embedded in broader discussion rather than systematically defined.
- Uncertainties: Arnheim uses "purity" and "saturation" with some terminological overlap; the card normalises to "saturation" (standard design term) with "chroma" as the modern mathematical alias.
- Cross-reference status: Verified — maps to C (chroma) in OKLCH. Arnheim predates CIELAB (1976) and OKLAB (2020).
- Rosetta Stone check: Mapping added (mathematics: chroma in OKLCH, rigorous).
- OCR issues: None detected.
