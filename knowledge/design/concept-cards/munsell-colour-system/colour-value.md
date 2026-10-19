---
concept: "Colour Value"
slug: "colour-value"
category: "colour-theory"
subcategory: "colour-properties"
tier: "foundational"
layer: "2-domain"
source: "A Practical Description of The Munsell Color System"
source_slug: "munsell-colour-system"
authors: "T. M. Cleland"
chapter: "II. Value"
chapter_number: 5
pdf_page: 6
section: "II. Value"
extraction_confidence: "high"
aliases:
  - "value"
  - "lightness"
  - "Munsell value"
  - "tone"
prerequisites: []
extends: []
related:
  - "munsell-colour-system"
  - "hue"
  - "chroma"
  - "neutral-axis"
  - "munsell-value-scale"
contrasts_with:
  - "hue"
  - "chroma"
answers_questions:
  - "CQ 3: What is the difference between hue, saturation/chroma, and lightness/value?"
  - "CQ 14: How does the visual-elements concept of 'value' (light-dark range) connect to colour theory's 'lightness' and to contrast as a design principle?"
rosetta_stone:
  -
    domain: "mathematics"
    concept: "Scalar on a bounded interval [0, 10]"
    rating: "rigorous"
    note: "Munsell value uses a nominal 0-to-10 lightness scale. Perceptual calibration is approximate and reference-dependent; photometric luminance, perceived lightness and CSS colour coordinates are distinct. Equal value increments alone do not imply geometric luminance ratios."
css_implementation:
  -
    property: "oklch() lightness channel"
    example: "color: oklch(0.5 0.1 240); /* CSS candidate; L is not Munsell V/10 */"
    support: "baseline"
  -
    property: "hsl() lightness channel"
    example: "color: hsl(240, 50%, 50%); /* L = 50% */"
    support: "baseline"
---

# Quick Definition

Munsell value is a nominal 0–10 lightness coordinate, with a calibrated, reference-dependent relation to photometric quantities. It is not luminance, brightness, CIELAB L* or OKLCH L.

# Core Definition

The earlier extraction attributes the following wording to Cleland; the book and prepared text are unavailable, so quotations, locators, context and historical attribution remain unverified.

Retained reported wording: "The quality by which we distinguish a light color from a dark one" "We noted that the first dimension did not tell us whether a color was light or dark. It told us, for example, that it was red and not green, but we know that there may be light red and dark red, and it is the function of this dimension of Value to tell us how light or how dark a given color may be" "scientifically measured and registered by means of an instrument known as a Photometer" "B6/ for example, by which we mean that this particular blue, regardless of its other qualities, is as light or as dark as the 6th step upon the scale of Value"

Munsell V represents light/dark character with approximate reference-dependent calibration. Photometric luminance, perceived brightness/lightness, CIELAB L* and OKLCH L differ. No fixed power exponent or V/10 CSS conversion is supplied.

Further recorded extraction wording (unverified attribution/context; these are not adopted universal claims):

- "a vertical pole, or axis to our circle of Hues, black at the lower end... and white at the top" (p. 6)
- "Since pure black is unattainable, we will call that 0... Pure white, which is also unattainable, we will call 10" (p. 6)
- "These steps of Value have been scientifically measured and registered by means of an instrument known as a Photometer" (p. 6)
- "The first dimension did not tell us whether a color was light or dark" (p. 6)

# Prerequisites

No card-local prerequisite is recorded in the preserved metadata. This is an editorial starting point, not proof that the concept has no dependencies in the wider domain.

# Key Properties

1. Value describes light/dark character; hue and chroma describe different properties.
2. V5 is the nominal midpoint, not automatically 50% reflectance/luminance or CSS L=.5.
3. The recorded nine grays 1–9 are a historical example; decimals and other samples are possible.
4. Photometry measures light, not exact perceptual equality. Calibration is approximate and conditional.
5. A specified value/luminance relation and reference conditions are required; no universal exponent .33 or cube-root Munsell conversion is supplied.
6. A value difference can contribute to hierarchy, but it cannot certify WCAG contrast or overall legibility.

# Construction / Recognition

## To Construct/Create:

1. Choose a reference scale and viewing/measurement conditions.
2. Compare or assign samples using that calibration, retaining needed decimals.
3. Treat 1–9 as the recorded sample set, not “the darkest/lightest achievable” physical law.
4. For digital output apply an identified conversion and check rendered pairs; do not divide V by ten to obtain OKLCH L.

## To Identify/Recognise:

1. Ask which lightness/value model and reference are in use.
2. Distinguish the value number from luminance Y, perceived brightness and CSS coordinates.
3. Use tonal comparison as a diagnostic; calculate actual contrast separately.

# Context & Application

Use value differences to discuss hierarchy and light/dark composition. For text, icons and controls, inspect complete rendered/composited pairs and relevant states under the chosen accessibility criterion. Munsell V alone and a squint/grayscale test cannot establish a contrast ratio.

## Cross-Domain Connections

**Mathematics → Scoped calibration**: A bounded value coordinate can sample a nonlinear relation, but the actual relation must be identified. Even if one stipulates ψ=I^(1/3), equal outputs ψ=1,2,3 imply inputs I=1,8,27; successive ratios 8 and 27/8 differ. Equal output increments therefore do not imply geometric inputs. CIELAB L* has a piecewise definition and a reference white; it is not Munsell V or a universal brightness law.

# Examples

Recorded extraction examples below retain their reported locators; they were not checked against the missing book. Any balance or harmony result is historical advice or conditional arithmetic, not an independently observed mixing or aesthetic result.

**Example 1** (p. 6): "B6/" — a blue at value 6, "regardless of its other qualities, is as light or as dark as the 6th step upon the scale of Value."

**Example 2** (p. 6): "A color such as is commonly called 'maroon' is an example of a red which is low in Value, because it is dark, and what is called 'pink' is a red which is high in Value because it is light."

# Relationships

## Builds Upon

No additional card-local bullet is recorded here. This is navigation scope, not a verified absence or a historical-source completeness result.

## Enables

- **Munsell Value Scale** — The scale samples the value coordinate; decimals and conditions remain possible.
- **Munsell Colour Notation** — Value is V before the slash, distinct from hue prefixes and C.
- **Colour Balance** — The recorded positive-input approximation uses V in C×V; no measured visual weight follows.
- **Munsell Balance Formula** — The inverse-product formula excludes V=0 and C=0 and does not predict arbitrary mixtures.

## Related

- **Munsell Colour System** — Value is a named H/V/C coordinate, not luminance or CSS L.
- **Neutral Axis** — Neutral samples illustrate the value axis; calibration requires a reference.
- **Hue** — Hue character differs from lightness/value; separate labels do not prove perceptual independence.
- **Chroma** — Chroma differs from light/dark value, with reference/gamut-dependent limits.

## Contrasts With

- **Hue** — Hue is perceptual colour character, not unique wavelength; value describes light/dark character.
- **Chroma** — Chroma and value name different attributes; neither alone certifies rendered contrast.

# Common Errors

- **Error**: Treating value as linear luminance or as an exact universal power law.
  **Correction**: Use an identified calibrated relation and conditions. No generic exponent supplies a Munsell-to-CSS conversion.
- **Error**: Using V difference or OKLCH L difference as a contrast test.
  **Correction**: Evaluate the actual rendered pair using the applicable contrast method.

# Common Confusions

- **Confusion**: Value equals physical brightness.
  **Clarification**: Brightness is perceptual, luminance is photometric, and value is a reference-dependent lightness coordinate.
- **Confusion**: HSL L, CIELAB L*, OKLCH L and Munsell V share numbers or exact equal appearance.
  **Clarification**: Their definitions differ. Similar labels and numeric steps do not establish conversion or appearance equivalence.

# Source Reference

Chapter 3: By T. M. Cleland, p. 4 (introduction). Chapter 5: II. Value, pp. 6-7.

# Verification Notes

- This revision reviewed the complete available card body and local relationships/CQ components; it did not inspect the missing original book, prepared Cleland text or diagrams. All historical quotations, dates, page claims, named attributions and source-specific efficacy claims remain unassessed for fidelity.
- Extraction-confidence metadata is preserved from the predecessor. Earlier “exact quote,” “verified planned cards” and “0010 checked” notes described historical extraction/navigation observations, not current independent semantic proof.
- Current technical qualifications use the [RIT renotation overview](https://www.rit.edu/science/munsell-color-science-lab-educational-resources#munsell-renotation-data), [CIE appearance terminology](https://cie.co.at/eilvterm/17-22-067) and [CSS Color4](https://www.w3.org/TR/2026/CRD-css-color-4-20261009/), with elementary conditional algebra where stated. These do not establish historical-source fidelity, exact perceptual equality, physical neutralisation or aesthetic guarantees.
- CSS metadata/body examples are model-specific illustrations, not Munsell conversions, checked contrast pairs or mandatory project palettes. No browser, assistive-technology, disc/material experiment or hosted rendering result was produced.
