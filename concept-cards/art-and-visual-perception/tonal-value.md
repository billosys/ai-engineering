---
# === CORE IDENTIFICATION ===
concept: Tonal Value
slug: tonal-value

# === CLASSIFICATION ===
category: visual-elements
subcategory: brightness
tier: foundational
layer: 0-perception

# === PROVENANCE ===
source: "Art and Visual Perception: A Psychology of the Creative Eye"
source_slug: art-and-visual-perception
authors: "Rudolf Arnheim"
chapter: "VI. Light"
chapter_number: 6
pdf_page: 356
section: "Relative Brightness"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - brightness value
  - lightness value
  - value
  - light-dark range

# === TYPED RELATIONSHIPS ===
prerequisites: []
extends: []
related:
  - brightness-constancy
  - chiaroscuro
  - tonal-contrast
  - luminosity
  - hue
  - saturation
contrasts_with:
  - hue
  - saturation

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is the difference between hue, saturation/chroma, and lightness/value?"
  - "How does the visual-elements concept of 'value' (light-dark range) connect to colour theory's 'lightness' and to contrast as a design principle?"

# === VISUAL DESIGN EXTENSIONS ===
rosetta_stone:
  - domain: mathematics
    concept: "Ordinal scale / linear range"
    rating: structural
    note: "Value is an ordered one-dimensional scale from black to white, analogous to a bounded ordinal dimension in measurement theory."

css_implementation:
  - property: "lightness (in hsl/oklch)"
    example: "color: oklch(0.75 0.1 270);"
    support: baseline
  - property: "filter: brightness()"
    example: "filter: brightness(1.5);"
    support: baseline
---

# Quick Definition

Tonal value is the dimension of visual experience that ranges from absolute black through all greys to absolute white — the light-dark scale independent of hue or colour.

# Core Definition

Tonal value (also called brightness value or simply value) is the perceptual dimension describing the relative lightness or darkness of a surface or area within a visual field. Arnheim establishes that value is relational, not absolute: the perceived brightness of any area is determined by its position in the scale of brightness values present across the total visual field, not by the absolute quantity of light it emits or reflects. "Whether or not a handkerchief looks white is determined not by the absolute amount of light it sends to the eye, but by its place in the scale of brightness values provided by the total setting" (Chapter VI, p. 357).

Value is one of the atomic visual elements — a building block of visual perception that exists independently of hue and saturation. It is the only visual dimension preserved in achromatic (black-and-white) media.

# Prerequisites

- **Figure-ground perception** — Value differences at boundaries create the edges that define figures against grounds.

# Key Properties

1. **Relational, not absolute** — The same physical luminance can appear bright or dark depending on the surrounding values.
2. **Continuous scale** — From 0 (black) to maximum (white), with an infinite continuum of greys between.
3. **Independent of hue** — Two surfaces of identical hue can differ in value; two surfaces of identical value can differ in hue.
4. **Prerequisite for form** — Without value differences, no shape, edge, or spatial relief is visible.
5. **Expressive dimension** — High-key (bright) vs. low-key (dark) compositions carry different emotional registers.

# Construction / Recognition

## To Construct/Create:
1. Establish the darkest and lightest anchors in the composition — these define the value range.
2. Assign each area a relative position on the scale between those anchors.
3. Test by desaturating (converting to greyscale) — all form should still read clearly.
4. Use value contrast at important edges to establish hierarchy and separation.

## To Identify/Recognise:
1. Squint at the image to suppress colour and hue detail — remaining distinctions are value-based.
2. Identify the darkest, lightest, and middle-grey regions.
3. Note which transitions are gradual (gradients, suggesting depth/roundness) vs. abrupt (flat contrast).

# Context & Application

- **Typical contexts**: All visual design, illustration, photography, painting, typography (text-to-background contrast), UI design.
- **Common applications**: Establishing hierarchy (brighter/darker elements draw attention), creating depth (value gradients model form), ensuring legibility (sufficient value contrast between text and background).

## Cross-Domain Connections

**Mathematics → STRUCTURAL**: Value is a bounded one-dimensional ordinal scale. Modern colour science formalises it as the L* (lightness) axis in CIELAB and the L (lightness) parameter in OKLCH, where perceptual uniformity is engineered so that equal numerical steps correspond to equal perceived differences. Arnheim's phenomenological account (1954) precedes this formalisation; Stevens's power law (n ≈ 0.33 for brightness) provides the psychophysical basis.

# Examples

**Example 1** (p. 357): Arnheim's handkerchief example — a white handkerchief at midnight may send less light to the eyes than charcoal in midday sun, yet still appears white because its relational position in the total value scale is preserved.

**Example 2** (p. 358): Alberti's observation: "Ivory and silver are white, which, when placed near swan's down, seem pale." Value appearance shifts depending on comparison context.

**Example 3** (p. 358): Rembrandt's glow — dark objects placed in even darker environments appear luminous because they exceed the expected average brightness of the total field.

# Relationships

## Builds Upon
- **Visual perception of contrast** — Value is the dimension along which contrast operates most fundamentally.

## Enables
- **Chiaroscuro** — The full system of light-and-shadow modelling depends on controlled value gradients.
- **Tonal contrast** — Compositional use of value differences as a design tool.
- **Brightness constancy** — The perceptual phenomenon by which value remains stable across changing illumination.
- **Form perception** — Three-dimensional surfaces are perceived as solid by means of value gradients.

## Related
- **Hue** — The chromatic dimension; independent of value but interacts with it in colour perception.
- **Saturation** — The purity/intensity dimension of colour; value is distinct from saturation.
- **Luminosity** — A related but distinct concept: luminosity describes surfaces that appear to emit light rather than merely reflect it.

## Contrasts With
- **Hue** — Hue describes the chromatic quality (redness, blueness, etc.); value describes the light-dark dimension only.
- **Saturation** — Saturation is the purity/greyness dimension; a highly saturated colour can have any value.

# Common Errors

- **Error**: Treating value as equivalent to the physical luminance of a surface.
  **Correction**: Value is perceptual and relational. Physical luminance determines raw light input; perceived value is determined by the distribution of luminances across the entire visual field.

- **Error**: Confusing value with brightness in the HSB/HSV colour model.
  **Correction**: "Brightness" in HSB is a device-dependent, perceptually non-uniform quantity. True perceptual value corresponds more closely to the L axis in CIELAB or OKLCH.

# Common Confusions

- **Confusion**: "Value and saturation are the same thing — a dull colour has low value."
  **Clarification**: A colour can be low-saturation (greyish) but high-value (light), or highly saturated but low-value (dark). Value (light/dark) and saturation (pure/grey) are orthogonal dimensions.

- **Confusion**: "Value only matters in black-and-white work."
  **Clarification**: Value is the most fundamental visual dimension and governs legibility, contrast, depth, and hierarchy in all chromatic work as well.

# Source Reference

Chapter VI: Light, "Art and Visual Perception," pp. 356–360 (section "Relative Brightness").

# Verification Notes

- Definition source: Synthesised from discussion across Chapter VI, especially pp. 357–358. The relational definition ("place in the scale") is close to a direct quote.
- Confidence rationale: High — Arnheim's relational account of brightness is explicit and central to the chapter. The concept is universal; Arnheim's contribution is the clear statement of its relational character.
- Uncertainties: Arnheim uses "brightness" and "value" somewhat interchangeably; the card normalises to "tonal value" as the standard design term.
- Cross-reference status: Verified — maps directly to L* in CIELAB and L in OKLCH; note that Arnheim (1954/1974) predates CIELAB (1976) and OKLAB (2020).
- Rosetta Stone check: Mapping added (mathematics / ordinal scale). No music or engineering mappings primary here.
- OCR issues: None detected.
