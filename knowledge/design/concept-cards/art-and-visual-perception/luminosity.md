---
concept: "Luminosity"
slug: "luminosity"
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
  - "glow"
  - "self-luminosity"
prerequisites:
  - "tonal-value"
extends:
  - "tonal-value"
related:
  - "brightness-constancy"
  - "surface-colour"
  - "chiaroscuro"
contrasts_with:
  - "surface-colour"
answers_questions:
  - "How does the visual-elements concept of 'value' (light-dark range) connect to colour theory's 'lightness' and to contrast as a design principle?"
rosetta_stone: []
css_implementation:
  -
    property: "mix-blend-mode: screen / lighten"
    example: "mix-blend-mode: screen;"
    support: "baseline"
  -
    property: "box-shadow (glow effect)"
    example: "box-shadow: 0 0 16px 4px rgba(255,255,200,0.8);"
    support: "baseline"
---

# Quick Definition

Luminosity here is an apparent glow or self-luminous reading. It differs from physical emitted radiance, measured luminance and CSS luminosity blending; high lightness alone does not establish it.

# Core Definition

This presents the represented Arnheim account. Exact edition, pages, quotations, named examples, figures, experiments, historical claims and physiological explanations remain unassessed against the unavailable original. Current analytic qualifications do not certify source fidelity.

Luminosity (or glow) is a perceptual quality distinct from simple high tonal value. Arnheim identifies it as a relational threshold effect: an object appears luminous not by virtue of its absolute brightness but by surpassing the average brightness established for its location by the total field. "A glowing object is seen as a source sending out light energy of its own... To do so the object must display a brightness well above that which corresponds to its expected place in the scale established by the rest of the field" (Chapter VI, p. 358).

This distinguishes the represented glow account from ordinary brightness: changing the field can alter the reading, without guaranteeing that every bright surface on dark appears luminous. The extraction also associates luminosity with David Katz's "film colour" — an indefinite, depth-penetrating appearance contrasted with surface colour. That reported association is retained without treating the terms as strict synonyms.

# Prerequisites

- **Tonal value** — Supplies the contextual light-dark comparison, not a universal glow threshold.

# Key Properties

1. **Relational reading** — The represented account links glow to surrounding values, without a universal numeric threshold.
2. **Source appearance** — A region can appear light-emitting without physically emitting extra radiance.
3. **Surface cues** — Texture, shading and edges can influence the reading; luminous objects can also have sharp edges or cast light/shadows.
4. **Distinct quantities** — Physical radiance/luminance, appearance and model coordinates differ.
5. **Context** — A change of field can change a reading without guaranteeing glow for every bright-on-dark pair.

# Construction / Recognition

## To Construct/Create:
1. Try a bright region within a darker field as one pictorial approach.
2. Compare texture, edges and neighbouring highlights; soft falloff is optional rather than mandatory.
3. For UI, treat box-shadow/screen as chosen effects and preserve actual contrast and semantic signals.

## To Identify/Recognise:
1. Ask whether the actual region appears to emit light or merely reflect it.
2. Separate that observation from a white colour value, blur declaration or blend-mode name.

# Context & Application

Painting, emissive rendering and interface effects can use glow for expression. The represented Rembrandt/newspaper examples show contextual appearance; no card alone verifies a rendered dark-theme reading or a universal salience result.

# Examples

These are retained reported examples from the existing extraction, not independently verified quotations, figures, experiments or historical conclusions.

**Example 1** (p. 358): Rembrandt's glowing gold tones — "quite low absolute brightness but shine through the dust of three centuries" because they exceed the average of their very dark surroundings.

**Example 2** (p. 358): "In a blacked-out street a piece of newspaper glows like a light" — the same paper that appears mundane in daylight becomes luminous against near-total darkness.

**Example 3** (p. 370): Rembrandt's technique described precisely: objects placed in dark fields, kept nearly free of shadow, so the light appears to originate within the object. "Glow is also associated with a lack of surface texture."

# Relationships

## Builds Upon
- **Tonal value** — Supplies contextual light-dark comparison; luminosity elaborates an appearance mode, not a numeric subtype.

## Enables
- **Symbolic use of light** — Glow can support the represented expressive reading.
- **Compositional focus** — Glow may contribute to emphasis without guaranteed attention.

## Related
- **Chiaroscuro** — Can provide a surrounding field for glow.
- **Brightness constancy** — Contextual expectations can relate stability and apparent self-luminosity, without one proven threshold mechanism.

## Contrasts With
- **Surface colour** — Local appearance-mode construct: material-colour versus light-emitting reading. The related/contrast roles compare the same construct in different ways, not two fictional cards.

# Common Errors

- **Error**: Assuming that making an element white or high-brightness will make it appear luminous.
  **Correction**: Inspect the actual context and appearance. Bright-on-dark is one useful trial, not a sufficient law or measured threshold.

- **Error**: Adding sharp highlights or texture to a would-be luminous element.
  **Correction**: These cues can change a pictorial reading but do not universally prevent glow. Preserve the intended material, lighting and expression rather than mandate blur.

# Common Confusions

- **Confusion**: "Luminosity and high lightness are the same."
  **Clarification**: Luminosity is an appearance mode, not a value coordinate or measured emission.

- **Confusion**: "In CSS, luminosity blend mode creates a glowing effect."
  **Clarification**: The non-separable blend is B(Cb,Cs)=SetLum(Cb,Lum(Cs)): it takes the specified luminosity-like component from the source with backdrop colour components, under the specification's helpers. It is not physical luminance, emission or an automatic glow. Screen and box-shadow are also engineered effects whose actual result needs inspection.

# Source Reference

Chapter VI: Light, "Art and Visual Perception," pp. 357–358, 369–370 (sections "Relative Brightness" and "Symbolism of Light").

# Verification Notes

Current bounded review separates appearance, model coordinates and rendering operations as explained above. Technical corrections and local relationship/CQ decisions are same-context proposals; original fidelity and actual rendered/observer outcomes remain unassessed. Extraction-confidence metadata is unchanged.

Legacy extraction notes below are preserved as historical assertions from the predecessor card, **not current verification results**. In particular, their equivalence, chronology, physiology and “Verified” claims are not adopted by this review.

- Definition source: Synthesised from pp. 357–358 and the later Rembrandt discussion (pp. 369–370). The relational definition is explicit.
- Confidence rationale: High — Arnheim's account of glow/luminosity as a relational threshold is precise and repeatedly exemplified.
- Uncertainties: The distinction between Katz's "film colour" and Arnheim's "luminosity" is terminological; treated as equivalent here.
- Cross-reference status: Verified — relevant to dark-mode UI design: dark themes that fail to consider luminosity thresholds can produce either muddy contrast or unintended glow artifacts.
- Rosetta Stone check: No strong rigorous cross-domain mappings identified.
- OCR issues: None detected.
