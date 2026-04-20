---
concept: Perceptual Uniformity (Colour)
slug: perceptual-uniformity
category: visual-perception
subcategory: colour psychophysics
tier: foundational
layer: 0-perception
source: "A Perceptual Color Space for Image Processing"
source_slug: posts
authors: "Bj\u00f6rn Ottosson"
chapter: "Motivation and derivation of Oklab"
chapter_number: null
pdf_page: null
section: null
extraction_confidence: high
aliases:
  - []
prerequisites:
  - []
extends:
  - []
related:
  - colour-space
  - oklab
  - cielab
contrasts_with:
  - []
answers_questions:
  - "What makes a colour space perceptually uniform, and why does it matter for design?"
  - "What is the mathematical relationship between perceptual uniformity in colour and equal temperament in music?"
rosetta_stone:
  - domain: music
    concept: "Equal temperament (12-TET)"
    rating: rigorous
    note: "Both solve the same problem: imposing uniform perceptual step-sizes on a physically non-linear space. Equal temperament makes semitones equal; perceptual colour spaces make colour differences equal."
  - domain: mathematics
    concept: "Metric space with uniform distance function"
    rating: structural
    note: "A perceptually uniform colour space is one whose distance metric corresponds to perceived difference \u2014 equal metric distances imply equal perceived differences."
css_implementation:
  - property: "color"
    example: "color: oklch(70% 0.15 180);"
    support: baseline
---

# Quick Definition

A colour space is perceptually uniform when equal numerical distances between colour values correspond to equal perceived differences in appearance.

# Core Definition

A perceptually uniform colour space is one in which the same numerical step produces the same perceived change in colour, regardless of where in the space you start. Ottosson states the goal directly: a perceptual colour space should predict "perceived lightness, chroma and hue well" so that "L, C and h should be perceived as orthogonal, so one can be altered without affecting the other two." It also requires that "blending two colors should result in even transitions. The transition colors should appear to be in between the blended colors."

The test for uniformity is empirical: given pairs of colours that humans judge to be equally different, a uniform space will assign equal distances to every pair.

# Prerequisites

This is a foundational concept with no prerequisites within this source.

# Key Properties

1. Equal numerical distances correspond to equal perceived colour differences.
2. Lightness, chroma, and hue axes are perceptually orthogonal \u2014 changing one does not appear to change the others.
3. Colour interpolation (blending) produces smooth, even-looking transitions without unexpected hue shifts or lightness jumps.

# Construction / Recognition

## To Construct/Create:
1. Choose a reference set of experimental colour-difference judgements (e.g., Munsell data, Luo-Rigg dataset, CAM16 predictions).
2. Optimise a mathematical transform of physical colour values so that distances in the transformed space minimise error against the reference judgements.
3. Verify with held-out data: equal-lightness pairs should have equal L values, equal-chroma pairs equal C, equal-hue pairs equal h.

## To Identify/Recognise:
1. Check whether a constant-hue, constant-chroma gradient appears uniform in perceived brightness across all hues \u2014 non-uniform spaces show yellow and cyan much lighter than red and blue (as HSV does).
2. Check whether blending two colours produces midpoints that appear between the originals in lightness and hue, without passing through an unexpected third colour.

# Context & Application

- **Typical contexts**: Image processing, gradient generation, palette construction, saturation adjustment, greyscale conversion.
- **Common applications**: Turning an image grayscale while preserving perceived lightness; increasing saturation without introducing hue shifts; creating smooth transitions between colours.

## Cross-Domain Connections

**Music \u2192 RIGOROUS**: Equal temperament (12-TET) and perceptual colour uniformity solve the same structural problem \u2014 imposing equal perceptual steps on a physically non-linear space. In equal temperament, frequency ratios are made uniform so that every semitone step sounds equally distant; in Oklab/CIELAB, colour coordinates are transformed so that every unit step looks equally distant.
The mathematical structure is identical: a non-linear (e.g., cube-root) transform of the physical measurement space followed by a linear recombination, producing a space where differences match perception rather than physics.

**Mathematics \u2192 STRUCTURAL**: A perceptually uniform colour space is a metric space in which the distance function is calibrated to human perception rather than to physical signal values. Equal distances in the metric correspond to equal perceived differences \u2014 the key invariant that justifies using Euclidean distance for colour difference calculations.

# Examples

**Example 1** (from source): An Oklab gradient with varying hue, constant lightness and chroma, appears even and uniform across all hues. Compare this to an HSV gradient with constant value and saturation, where yellow, magenta, and cyan appear much lighter than red and blue \u2014 a direct failure of perceptual uniformity. (Section: "Comparing Oklab to HSV")

**Example 2** (from source): The quantitative error table shows Oklab achieving L RMS = 0.20, versus CIELAB at 1.70 and HSV at 11.59, demonstrating Oklab's superior perceptual uniformity in lightness prediction. (Section: "Comparison with other color spaces")

# Relationships

## Builds Upon
- **Human visual perception of lightness, chroma, and hue** \u2014 Uniformity is defined relative to what humans perceive, not to physical measurements.

## Enables
- **Oklab colour space** \u2014 Oklab is defined as a colour space engineered to achieve perceptual uniformity.
- **Colour interpolation (perceptual)** \u2014 Perceptual uniformity is the prerequisite for interpolation that produces visually even transitions.
- **Palette construction** \u2014 Requires uniformity to guarantee predictable lightness steps across hues.

## Related
- **CIELAB** \u2014 CIELAB is an earlier attempt at perceptual uniformity that Oklab improves upon.
- **Colour space comparison** \u2014 The comparison table in the source ranks colour spaces by their approximation to perceptual uniformity.

## Contrasts With
- **HSV** \u2014 HSV uses sRGB coordinates directly and provides no perceptual uniformity; the source notes it "does not meet any of the requirements except having a D65 whitepoint."

# Common Errors

- **Error**: Assuming any Lab-like space is automatically perceptually uniform.
  **Correction**: Uniformity is a matter of degree; CIELAB, CIELUV, and OSA-UCS all have known failures. Uniformity must be verified against experimental data, not assumed from structure.

- **Error**: Treating HSV or HSL hue sweeps as perceptually uniform hue gradients.
  **Correction**: HSV hue gradients are highly non-uniform \u2014 yellow, magenta, and cyan appear far lighter than red and blue at constant V and S.

# Common Confusions

- **Confusion**: "Perceptual uniformity" means the space looks like a rainbow or colour wheel to the human eye.
  **Clarification**: It means that equal steps in the coordinate system correspond to equal perceived differences \u2014 not that the coordinate layout is visually intuitive or aesthetically pleasing.

- **Confusion**: Uniformity applies only to lightness.
  **Clarification**: Perceptual uniformity applies to all three axes: lightness (L), chroma (C), and hue (h) must each be individually uniform, and they must be orthogonal to each other.

# Source Reference

"Motivation and derivation of Oklab" and "Comparison with other color spaces" sections; no page numbers (web article).

# Verification Notes

- Definition source: Synthesised from the requirements list in "Motivation and derivation of Oklab" and from the comparison table and gradient examples throughout.
- Confidence rationale: High \u2014 the source explicitly states the uniformity requirements and provides quantitative evidence; the concept is central to the entire article.
- Uncertainties: The source does not define "perceptual uniformity" with a single sentence; the definition has been synthesised from multiple passages.
- Cross-reference status: Verified against both qualitative descriptions and quantitative error table.
- Rosetta Stone check: Music/equal-temperament mapping added as rigorous per instructions; mathematics/metric-space mapping added as structural.
- OCR issues: HTML div/img/span artifacts present throughout; ignored. LaTeX extracted from context.
