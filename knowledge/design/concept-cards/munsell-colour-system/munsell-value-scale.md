---
concept: "Munsell Value Scale"
slug: "munsell-value-scale"
category: "colour-theory"
subcategory: "colour-systems"
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
  - "Munsell gray scale"
  - "value scale"
  - "lightness scale"
prerequisites:
  - "colour-value"
extends:
  - "colour-value"
related:
  - "munsell-colour-system"
  - "neutral-axis"
  - "munsell-colour-notation"
contrasts_with: []
answers_questions:
  - "CQ 3: What is the difference between hue, saturation/chroma, and lightness/value?"
  - "CQ 14: How does the visual-elements concept of 'value' (light-dark range) connect to colour theory's 'lightness' and to contrast as a design principle?"
rosetta_stone:
  -
    domain: "mathematics"
    concept: "Discrete psychophysical scale on [0, 10]"
    rating: "rigorous"
    note: "A value scale can sample a reference-dependent nonlinear lightness relation. Munsell V, CIELAB L*, OKLCH L and luminance Y are distinct; neither a generic cube-root model nor equal value increments establishes geometric luminance spacing or exact equal appearance."
css_implementation:
  -
    property: "oklch() lightness channel"
    example: "/* Munsell V is not OKLCH L: use an identified value/luminance relation and reference conditions for conversion. */"
    support: "baseline"
---

# Quick Definition

Munsell value is a nominal 0–10 lightness coordinate, with a calibrated, reference-dependent relation to photometric quantities. It is not luminance, brightness, CIELAB L* or OKLCH L.

# Core Definition

The earlier extraction attributes the following wording to Cleland; the book and prepared text are unavailable, so quotations, locators, context and historical attribution remain unverified.

Retained reported wording: "a vertical pole, or axis to our circle of Hues, black at the lower end, representing total absence of light, and white at the top, representing pure light, and between these a number of divisions of gray, regularly graded between black and white" "Since pure black is unattainable, we will call that 0 and begin our scale with the darkest gray as 1, numbering the steps up to 9, which is the lightest gray. Pure white, which is also unattainable, we will call 10" "the middle one of these will be 5 — what is referred to as Middle Value" "These steps of Value, have been scientifically measured and registered by means of an instrument known as a Photometer"

The recorded 1–9 grayscale is one historical sampling of a nominal 0–10 value coordinate. Decimal values and reference conditions matter. Neither exact equal appearance nor a universal power/cube-root calibration follows from the photometer account.

# Prerequisites

- **Colour Value** — Supplies the relevant H/V/C or diagram vocabulary for this card; this is an understanding route, not a claim of physical or historical derivation.

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

**Example 1** (p. 6): "B6/" — a blue at value 6, "is as light or as dark as the 6th step upon the scale of Value."

**Example 2** (p. 6): "A color such as is commonly called 'maroon' is an example of a red which is low in Value, because it is dark, and what is called 'pink' is a red which is high in Value because it is light."

# Relationships

## Builds Upon

- **Colour Value** — The scale supplies a reference-dependent implementation of the value coordinate.

## Enables

- **Munsell Colour Notation** — Value is V in H V/C; no V/10 CSS conversion follows.
- **Colour Balance** — The historical approximation multiplies positive C,V; no appearance or mixture proof follows.
- **Munsell Colour Solid** — Value is drawn vertically in the diagram, separate from its irregular chroma limits.

## Related

- **Neutral Axis** — Neutral samples illustrate value; a photometer alone does not establish equal appearance.
- **Munsell Colour System** — The value scale is a system component, not an exact universal psychophysical law.

## Contrasts With

No additional card-local bullet is recorded here. This is navigation scope, not a verified absence or a historical-source completeness result.

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

Chapter 5: II. Value, pp. 6-7.

# Verification Notes

- This revision reviewed the complete available card body and local relationships/CQ components; it did not inspect the missing original book, prepared Cleland text or diagrams. All historical quotations, dates, page claims, named attributions and source-specific efficacy claims remain unassessed for fidelity.
- Extraction-confidence metadata is preserved from the predecessor. Earlier “exact quote,” “verified planned cards” and “0010 checked” notes described historical extraction/navigation observations, not current independent semantic proof.
- Current technical qualifications use the [RIT renotation overview](https://www.rit.edu/science/munsell-color-science-lab-educational-resources#munsell-renotation-data), [CIE appearance terminology](https://cie.co.at/eilvterm/17-22-067) and [CSS Color4](https://www.w3.org/TR/2026/CRD-css-color-4-20261009/), with elementary conditional algebra where stated. These do not establish historical-source fidelity, exact perceptual equality, physical neutralisation or aesthetic guarantees.
- CSS metadata/body examples are model-specific illustrations, not Munsell conversions, checked contrast pairs or mandatory project palettes. No browser, assistive-technology, disc/material experiment or hosted rendering result was produced.
