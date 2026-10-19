---
concept: "Tonal Value"
slug: "tonal-value"
category: "visual-elements"
subcategory: "brightness"
tier: "foundational"
layer: "0-perception"
source: "Art and Visual Perception: A Psychology of the Creative Eye"
source_slug: "art-and-visual-perception"
authors: "Rudolf Arnheim"
chapter: "VI. Light"
chapter_number: 6
pdf_page: 356
section: "Relative Brightness"
extraction_confidence: "high"
aliases:
  - "brightness value"
  - "lightness value"
  - "value"
  - "light-dark range"
prerequisites: []
extends: []
related:
  - "brightness-constancy"
  - "chiaroscuro"
  - "tonal-contrast"
  - "luminosity"
  - "hue"
  - "saturation"
contrasts_with:
  - "hue"
  - "saturation"
answers_questions:
  - "What is the difference between hue, saturation/chroma, and lightness/value?"
  - "How does the visual-elements concept of 'value' (light-dark range) connect to colour theory's 'lightness' and to contrast as a design principle?"
rosetta_stone:
  -
    domain: "mathematics"
    concept: "Ordered light-dark comparisons versus a declared numerical coordinate"
    rating: "structural"
    note: "Darker/lighter ordering differs from a declared numerical lightness coordinate. Model formulas and approximate appearance correlates do not supply one universal linear perceptual scale."
css_implementation:
  -
    property: "lightness (model-specific hsl/oklch)"
    example: "color: oklch(0.75 0.1 270);"
    support: "baseline"
  -
    property: "filter: brightness()"
    example: "filter: brightness(1.5); /* encoded-channel effect, not perceptual value scaling */"
    support: "baseline"
---

# Quick Definition

Tonal value describes light-dark appearance and pictorial ordering. It differs from measured luminance, CIE brightness/lightness and model coordinates such as HSL L, HSV V or OKLCH L; context matters.

# Core Definition

This presents the represented Arnheim account. Exact edition, pages, quotations, named examples, figures, experiments, historical claims and physiological explanations remain unassessed against the unavailable original. Current analytic qualifications do not certify source fidelity.

Tonal value (also called brightness value or simply value) is the perceptual dimension describing the relative lightness or darkness of a surface or area within a visual field. The represented Arnheim account emphasises value relations within a field; it does not establish that absolute stimulus intensity is irrelevant to appearance. "Whether or not a handkerchief looks white is determined not by the absolute amount of light it sends to the eye, but by its place in the scale of brightness values provided by the total setting" (Chapter VI, p. 357).

Value is a useful visual-element description, distinct from hue and saturation without universal perceptual independence. Achromatic media retain shape, texture and other relations as well as light-dark differences.

# Prerequisites

- **Figure-ground perception** — Value differences can help distinguish a figure boundary; chromatic cues can also contribute. The accepted figure-ground card supplies this comparison, without adding a typed prerequisite.

# Key Properties

1. **Contextual appearance** — A luminance can look different against another surround.
2. **Ordering versus coordinate** — Darker/lighter comparisons differ from a declared numerical scale; endpoints depend on model and medium.
3. **Distinct attributes** — Hue and vividness can differ at similar light-dark appearance; model independence is not universal perceptual independence.
4. **Boundary cue** — Value differences can help visibility, while chromatic differences can also reveal edges.
5. **Expression** — High/low-key arrangements can serve different content without a fixed emotional law.

# Construction / Recognition

## To Construct/Create:
1. Begin with supplied content, identity and actual surfaces; extreme black/white anchors are optional.
2. Compare light-dark relations for hierarchy, boundaries and depicted depth.
3. Use greyscale conversion as a declared-model diagnostic; it discards chromatic cues and is not a conformance test.
4. For text, resolve actual foreground/background pairs, alpha, filters, font/size and states; use the applicable contrast method rather than a raw L difference.

## To Identify/Recognise:
1. Squinting can reduce detail, but does not selectively measure value or prove legibility.
2. Identify relative dark/light regions and compare gradient versus abrupt transitions in their actual context.

# Context & Application

Painting, photography and interface work use light-dark relations for composition and legibility. WCAG opaque-sRGB ratios use decoded linear relative luminance; HSL L, HSV V and OKLCH L are different quantities. Inspect actual pair/state and typography conditions independently of a pictorial value judgment.

## Cross-Domain Connections

**Mathematics → STRUCTURAL**: An ordinal darker/lighter comparison provides an order, while a declared model supplies numerical coordinates with its own reference and formula. Equal OKLCH/CIELAB L steps are approximate appearance correlates, not an exact sensory scale. For encoded sRGB .5, decoding gives about .21404114 linear channel value; it is not linear .5. HSL red/lime at L=.5 have relative luminances .2126/.7152, so their white ratios differ (about3.99848/1.37219). A fixed brightness power exponent is not a universal derivation of value.

# Examples

These are retained reported examples from the existing extraction, not independently verified quotations, figures, experiments or historical conclusions.

**Example 1** (p. 357): Arnheim's handkerchief example — a white handkerchief at midnight may send less light to the eyes than charcoal in midday sun, yet still appears white because its relational position in the total value scale is preserved.

**Example 2** (p. 358): Alberti's observation: "Ivory and silver are white, which, when placed near swan's down, seem pale." Value appearance shifts depending on comparison context.

**Example 3** (p. 358): Rembrandt's glow — dark objects placed in even darker environments appear luminous because they exceed the expected average brightness of the total field.

# Relationships

## Builds Upon
- **Visual perception of contrast** — Local comparison construct; value differences can support edges without being the sole perceptual dimension.

## Enables
- **Chiaroscuro** — One light/shadow modelling practice.
- **Tonal contrast** — Relations between light-dark appearances or actual rendered pairs.
- **Brightness constancy** — Conditional surface-identity stability across lighting.
- **Form perception** — Gradients are one form cue, not necessary for all visible shape.

## Related
- **Hue** — A distinct chromatic description with possible appearance interaction.
- **Saturation** — Relative colourfulness/model parameters need separate definitions.
- **Luminosity** — A light-emitting appearance mode rather than high value alone.

## Contrasts With
- **Hue** — Chromatic character versus light-dark appearance.
- **Saturation** — A vividness comparison under stated definition; available model chroma depends on hue/lightness/gamut.

# Common Errors

- **Error**: Treating value as equivalent to the physical luminance of a surface.
  **Correction**: Luminance is a measured photometric quantity; brightness/lightness appearance also depends on context. A model coordinate is not either quantity without its definition and conditions.

- **Error**: Confusing value with brightness in the HSB/HSV colour model.
  **Correction**: HSV V is the maximum encoded-RGB channel in the normalized model. HSL L and OKLCH L use other formulas; none is a universal "true value" or automatic contrast result.

# Common Confusions

- **Confusion**: "Value and saturation are the same thing — a dull colour has low value."
  **Clarification**: Light-dark and vividness comparisons differ. CIE saturation is relative to own brightness, while coordinate independence and perceptual independence remain separate.

- **Confusion**: "Value only matters in black-and-white work."
  **Clarification**: Light-dark relationships also matter in chromatic work, alongside hue, texture, content and viewing conditions. They contribute to hierarchy and legibility without determining them alone.

# Source Reference

Chapter VI: Light, "Art and Visual Perception," pp. 356–360 (section "Relative Brightness").

# Verification Notes

Current bounded review separates appearance, model coordinates and rendering operations as explained above. Technical corrections and local relationship/CQ decisions are same-context proposals; original fidelity and actual rendered/observer outcomes remain unassessed. Extraction-confidence metadata is unchanged.

Legacy extraction notes below are preserved as historical assertions from the predecessor card, **not current verification results**. In particular, their equivalence, chronology, physiology and “Verified” claims are not adopted by this review.

- Definition source: Synthesised from discussion across Chapter VI, especially pp. 357–358. The relational definition ("place in the scale") is close to a direct quote.
- Confidence rationale: High — Arnheim's relational account of brightness is explicit and central to the chapter. The concept is universal; Arnheim's contribution is the clear statement of its relational character.
- Uncertainties: Arnheim uses "brightness" and "value" somewhat interchangeably; the card normalises to "tonal value" as the standard design term.
- Cross-reference status: Verified — maps directly to L* in CIELAB and L in OKLCH; note that Arnheim (1954/1974) predates CIELAB (1976) and OKLAB (2020).
- Rosetta Stone check: Mapping added (mathematics / ordinal scale). No music or engineering mappings primary here.
- OCR issues: None detected.
