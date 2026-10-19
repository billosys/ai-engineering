---
concept: "Colour Constancy"
slug: "colour-constancy"
category: "visual-perception"
subcategory: "perceptual-constancy"
tier: "intermediate"
layer: "0-perception"
source: "Art and Visual Perception: A Psychology of the Creative Eye"
source_slug: "art-and-visual-perception"
authors: "Rudolf Arnheim"
chapter: "VII. Color"
chapter_number: 7
pdf_page: 371
section: "Shape and Color"
extraction_confidence: "high"
aliases:
  - "chromatic constancy"
  - "hue constancy"
prerequisites:
  - "hue"
  - "saturation"
  - "tonal-value"
extends: []
related:
  - "brightness-constancy"
  - "simultaneous-contrast"
  - "colour-temperature"
contrasts_with: []
answers_questions:
  - "How does the visual-elements concept of 'value' (light-dark range) connect to colour theory's 'lightness' and to contrast as a design principle?"
  - "How do you ensure a coloured status badge communicates its meaning without relying solely on colour? What redundant encoding strategies exist?"
rosetta_stone:
  -
    domain: "mathematics"
    concept: "Von Kries adaptation model (diagonal matrix in cone space)"
    rating: "rigorous"
    note: "For fixed invertible response basis M and nonzero source-white responses, D=diag((M w_dest)/(M w_source)) gives y=M^-1 D M x and maps source white to destination white. This is a linear model step, not a complete biological account or full nonlinear colour pipeline."
  -
    domain: "engineering"
    concept: "White balance / colour temperature correction in cameras"
    rating: "structural"
    note: "White balance estimates an illuminant and adjusts an image under engineered assumptions; it does not establish identical biological computations or unique reflectance recovery."
css_implementation: []
---

# Quick Definition

Colour constancy is a conditional tendency for object-colour identity to remain relatively stable under changed illumination. It does not recover a unique "true" reflectance or make colour coding reliable by itself.

# Core Definition

This presents the represented Arnheim account. Exact edition, pages, quotations, named examples, figures, experiments, historical claims and physiological explanations remain unassessed against the unavailable original. Current analytic qualifications do not certify source fidelity.

Colour constancy describes a conditional tendency toward stable object-colour appearance across changes in illumination. A red apple can retain its red identity under different illuminants while shade, saturation and light-dark appearance still change. Illumination context and adaptation can contribute; this is not a complete computation specified by the represented account.

Arnheim discusses colour constancy extensively in the context of animal and human behaviour: "Color constancy is aided by the physiological fact that the retina adapts to the given illumination... Confronted with a green light, the eyes decrease their response to greenness" (Chapter VII, p. 376). He cites the Katz and Revesz experiment with chickens — trained to peck white grains, they continued to peck white grains even under blue illumination, demonstrating colour constancy across species.

However, Arnheim also identifies the limits and side effects: adaptation makes us perceive the dominant colour as "normal" (more colourless), and this same mechanism that preserves constancy also causes colour perception to be most vulnerable to environmental change. He describes Helson and Koffka's adaptation effects, where the dominant colour is perceived as grey (neutral) while greys that deviate from average brightness shift toward the complementary.

The current matrix illustration below is an added model. Its exact occurrence, absence or chronology in the unavailable original is not established; no claim that Arnheim predates every von Kries formalisation is made.

# Prerequisites

- **Hue** — Supplies chromatic-character vocabulary.
- **Saturation** — Supplies a distinct appearance comparison.
- **Tonal value** — Supplies light-dark context alongside chromatic stability.

# Key Properties

1. **Conditional stability** — Familiar identity can persist while shade and expression change.
2. **Adaptation** — Selective response changes can contribute without being the whole constancy phenomenon.
3. **Illumination ambiguity** — Observations alone do not uniquely determine reflectance and illuminant.
4. **Viewing conditions** — The represented Monet/Van Gogh example warns that exhibition light can change appearance.
5. **Model assumptions** — The "grey world" and "white patch" estimates are engineered assumptions; they are not universal visual-system laws.

# Construction / Recognition

## To Construct/Create:
1. Compare the actual display/print and ambient illumination. D50/D65 references serve specified workflows, not a universal viewing prescription.
2. If using a camera or image correction, identify its estimated source white and intended target white.
3. Treat an SVG feColorMatrix or a camera transform as engineered filtering, not a CSS implementation of biological constancy.

## To Identify/Recognise:
1. Compare object identity and residual shifts across stated illuminants.
2. Describe missing scene context and extreme casts without assuming a guaranteed failure condition.

# Context & Application

Photography, display/print workflows and gallery lighting require stated illuminants and viewing conditions. For interfaces or data graphics, preserve actual semantic roles and pair checks; colour constancy cannot ensure a badge is understood. Pair an error colour with visible “Error” text, a meaningful icon/shape or a pattern where appropriate, and ensure that the same information remains available without colour.

## Cross-Domain Connections

**Mathematics → RIGOROUS**: Choose an invertible linear-response basis M and source/target whites w_source,w_dest with nonzero source responses. Set D=diag((Mw_dest)/(Mw_source)) componentwise, then y=M⁻¹DMx maps w_source to w_dest. Fixed M,D gives a linear step. It does not estimate a unique illuminant, establish a biological mechanism or make a full colour pipeline linear; encoding and other appearance operations can be nonlinear.

**Engineering → STRUCTURAL**: White balance estimates an illuminant and adjusts image channels under an engineering model. Its assumptions and failure modes need inspection; the analogy does not establish identical biological operations. ICC rendering intent, display calibration and ambient adaptation are separate choices.

# Examples

These are retained reported examples from the existing extraction, not independently verified quotations, figures, experiments or historical conclusions.

**Example 1** (p. 376): Katz and Revesz chicken experiment — chickens trained to peck white grains continued to peck correctly when white grains were illuminated by blue light, demonstrating colour constancy even in non-human animals.

**Example 2** (p. 376): Helson and Koffka's adaptation effect — under red illumination, a grey surface of average brightness appears grey; brighter grey appears reddish; darker grey appears greenish (its complementary). This is a systematic constancy side effect, not a failure.

**Example 3** (p. 377): The practical consequence for art — "When a painting by Monet or Van Gogh done at strong daylight is seen under the color of tungsten lamps, we cannot pretend to perceive the hues intended by the artist; and as the colors change, so does their expression and organization."

# Relationships

## Builds Upon
- **Hue, saturation** — Supply chromatic appearance distinctions.
- **Brightness constancy** — A parallel stability comparison; tonal value supplies the light-dark vocabulary.

## Enables
- **Reliable colour communication** — Constancy can help recognition, but redundancy and actual pair/state checks are still needed.
- **Cross-illuminant colour identification** — Conditional identity across viewing changes.

## Related
- **Brightness constancy** — Achromatic and chromatic stability are related, without one proven shared algorithm.
- **Simultaneous contrast** — Contextual shifts can coexist with identity stability.
- **Colour temperature** — Artistic warmth and physical illuminant chromaticity differ; constancy is not a Kelvin-subtraction rule.

## Contrasts With
- **Adaptation effects** — Sensitivity changes and aftereffects can interact with constancy; they are not simply its opposite or always its failure.

# Common Errors

- **Error**: Assuming colours specified in RGB hex will appear identical across all viewing conditions.
  **Correction**: The specified coordinates, display/print rendering, surrounding field and observer adaptation differ. Check the intended conditions; a profile is not an all-condition guarantee.

- **Error**: Designing data visualisations with colour coding tested only under one ambient condition.
  **Correction**: Check relevant conditions and encode meaning redundantly. A status badge can show visible “Error” text plus a distinct icon/shape; data series can use labels/patterns. Colour alone must not be the only cue. This conceptual repair does not prove keyboard, contrast or rendered accessibility outcomes.

# Common Confusions

- **Confusion**: "Colour constancy means we see colours exactly the same in all conditions."
  **Clarification**: Constancy is partial and approximate. Strong casts, scene context and adaptation can affect identity and appearance; neither a normal-range success nor an extreme-condition failure is guaranteed.

- **Confusion**: "Setting display white point handles colour constancy."
  **Clarification**: Display white point calibration corrects for the display's own colour bias but cannot account for ambient illumination hitting the display surface or the viewer's adaptation state.

# Source Reference

Chapter VII: Color, "Art and Visual Perception," pp. 374–377 (section "Shape and Color").

# Verification Notes

Current bounded review separates appearance, model coordinates and rendering operations as explained above. Technical corrections and local relationship/CQ decisions are same-context proposals; original fidelity and actual rendered/observer outcomes remain unassessed. Extraction-confidence metadata is unchanged.

Legacy extraction notes below are preserved as historical assertions from the predecessor card, **not current verification results**. In particular, their equivalence, chronology, physiology and “Verified” claims are not adopted by this review.

- Definition source: Synthesised from pp. 376–377. The Katz/Revesz example and the Helson/Koffka effects are explicitly discussed. The Monet/Van Gogh consequence is on p. 377.
- Confidence rationale: High — colour constancy is explicitly discussed with multiple experiments cited. Arnheim's phenomenological account is consistent with modern perceptual science.
- Uncertainties: Arnheim does not use the term "chromatic adaptation transform" or describe the mathematical model; the card adds von Kries model reference as a modern formalisation, marked as such.
- Cross-reference status: Verified — Arnheim's account (1954/1974) predates CIELAB (1976), von Kries model formalisation, and CAT02 (2002). The mathematical mappings are added as cross-domain extensions.
- Rosetta Stone check: Mappings added (mathematics: von Kries diagonal matrix, rigorous; engineering: camera white balance, structural).
- OCR issues: None detected.
