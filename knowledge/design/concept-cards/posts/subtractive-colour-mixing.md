---
concept: "Subtractive Colour Mixing"
slug: "subtractive-colour-mixing"
category: "visual-perception"
subcategory: "colour-physics"
tier: "foundational"
layer: "0-perception"
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
    - "subtractive mixing"
    - "pigment mixing"
    - "paint mixing"
prerequisites: []
extends: []
related:
  - "additive-colour-mixing"
contrasts_with:
  - "additive-colour-mixing"
answers_questions:
  - "What distinguishes additive from subtractive colour mixing, and which does a monitor use?"
rosetta_stone: []
css_implementation: []
---

# Quick Definition

Subtractive colour mixing is a simplified model of combining pigments or dyes: each selectively absorbs portions of the illuminating spectrum and reflects the remainder. Outcomes depend on materials, concentrations, illumination and mixing process.

# Core Definition

Drasner introduces subtractive mixing through the contrast with digital work: "As a child, you're working with paint. Paint and inks from a printer have tiny particles called pigments that mix together and reflect to present color to your eye. This is subtractive color mixing. The more colors you add to it, the darker it becomes, until we get brown. Primaries are close to what you're used to: red, yellow, blue. But when you mix these colors with subtractive color mixing, you arrive at brown." The absorption model explains why many pigment mixtures become darker or less saturated, but does not guarantee that every added pigment darkens every mixture or that the result approaches brown or black. Traditional red-yellow-blue painting practice differs from cyan-magenta-yellow process printing.

# Prerequisites

- None — this is a foundational physical concept

# Key Properties

1. Absorptive mixtures often reduce reflected light; the actual result depends on pigment and conditions
2. Traditional primaries are red, yellow, blue (artists); professional print uses cyan, magenta, yellow (CMY)
3. Combining pigments does not guarantee a particular neutral or dark result
4. Pigments work by absorbing (subtracting) light; the reflected remainder is what we see as colour

# Construction / Recognition

## To Identify/Recognise:
1. Physical media — paint, ink, markers, dyes — use subtractive mixing
2. Compare mixtures in context; additional pigments can shift hue, chroma and lightness in different ways
3. Pigment mixtures depend on their spectra, concentration, medium and illumination; traditional red/blue/purple and red/yellow/orange outcomes are examples, not guaranteed recipes

# Context & Application

- **Typical contexts**: Traditional art media, print production (CMYK), textile dyeing, photographic colour processes
- **Common applications**: Understanding why CMYK is used in print (not RGB); understanding why design tools convert RGB to CMYK for print output

# Examples

**Example 1** (from source): "The more colors you add to it, the darker it becomes, until we get brown" — Drasner's description of what happens when mixing many paint colours together, contrasted with white light as the additive complement.

# Relationships

## Builds Upon
- **Physics of pigments and light absorption** — Subtractive mixing reflects how pigment particles selectively absorb wavelengths

## Related
- **CMYK colour model** — The print industry colour model based on subtractive mixing with cyan, magenta, yellow (and black) inks

## Contrasts With
- **Additive colour mixing** — A useful contrast between emitted light and reflected pigment, but not a universal prediction for every pigment recipe

# Common Errors

- **Error**: Treating “digital colour mixing” as one operation with a guaranteed red-plus-green result.
  **Correction**: Specified emitted RGB primary contributions combine additively, so full red plus full green gives the RGB yellow primary. CSS interpolation, blend functions and compositing follow their own rules; pigment mixtures depend on materials and conditions.

# Source Reference

"Color mixing" section, Working With Colors Guide (Sarah Drasner).

# Verification Notes

- Iteration02 scope: The current technical support below uses the prepared text and linked rules; this correction does not assess fidelity to the unavailable original capture or browser behavior. Extraction-confidence metadata is unchanged. Retained extraction/provenance remarks below are predecessor assertions present at source 19c7a08a; their authorship is not inferred here, and they are not new current results. Where this iteration clarifies a note, that clarification scopes a prior assertion rather than recording a new extraction or verification result.

- Current technical context: [CSS Color 4 §2](https://www.w3.org/TR/2026/CRD-css-color-4-20261009/#color-space) defines additive linear-light spaces; it does not make encoded sRGB arithmetic or pigment outcomes interchangeable.

- Definition source: Direct quote from Drasner
- Confidence rationale: High — clearly stated in dedicated section
- Uncertainties: The prepared account does not establish a universal result for every pigment recipe; outcomes depend on materials and conditions. Original-capture fidelity is unassessed because the immutable capture is unavailable.
- Cross-reference status: Not in Ottosson source
- Rosetta Stone check: No mappings added
- OCR issues: None significant
