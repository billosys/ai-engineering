---
concept: "Colour Temperature"
slug: "colour-temperature"
category: "colour-theory"
subcategory: "colour-properties"
tier: "intermediate"
layer: "2-domain"
source: "Art and Visual Perception: A Psychology of the Creative Eye"
source_slug: "art-and-visual-perception"
authors: "Rudolf Arnheim"
chapter: "VII. Color"
chapter_number: 7
pdf_page: 371
section: "Warm and Cold"
extraction_confidence: "medium"
aliases:
  - "warm/cool colour"
  - "warm and cold (Arnheim's terms)"
  - "chromatic temperature"
prerequisites:
  - "hue"
  - "saturation"
extends: []
related:
  - "hue"
  - "saturation"
  - "colour-harmony"
  - "complementary-colours"
  - "colour-weight"
contrasts_with: []
answers_questions:
  - "How do you construct a colour palette starting from a single brand colour using OKLCH? What systematic steps ensure adequate contrast and accessible combinations?"
rosetta_stone:
  -
    domain: "engineering"
    concept: "Colour temperature in Kelvin (blackbody radiation)"
    rating: "structural"
    note: "Kelvin colour temperature refers to ideal blackbody radiation; CCT approximates another source chromaticity relative to that locus. Artistic warm/cool character is contextual, not a Kelvin coordinate or universal inverse scale."
css_implementation:
  -
    property: "hue angle (oklch)"
    example: "/* Chosen hue candidates need contextual warm/cool comparison; no Kelvin mapping */"
    support: "baseline"
  -
    property: "filter: hue-rotate() (RGB matrix effect)"
    example: "filter: hue-rotate(-20deg); /* RGB matrix; not a Kelvin or exact OKLCH hue shift */"
    support: "baseline"
---

# Quick Definition

Artistic colour temperature describes relative warm/cool character in a composition. Arnheim's admixture-direction hypothesis is an explicitly uncertain account; Kelvin colour temperature and CCT describe different physical references.

# Core Definition

This presents the represented Arnheim account. Exact edition, pages, quotations, named examples, figures, experiments, historical claims and physiological explanations remain unassessed against the unavailable original. Current analytic qualifications do not certify source fidelity.

Colour temperature describes the perceived warmth or coolness of a colour — a quality that correlates with but is not simply determined by hue membership. Arnheim offers an analysis that distinguishes it from simple hue category: "My suggestion is that not the main color but the color toward which it deviates may determine the effect... a reddish blue looks warm whereas a bluish red looks cold" (Chapter VII, p. 394).

This is Arnheim's represented hypothesis: admixture direction — the "leaning" of the colour — may affect its temperature quality. It is not an established universal determinant. A red with a blue tinge reads cold; a blue with a red tinge reads warm. This produces counterintuitive results: reddish blue (warm) vs. bluish red (cold), reddish yellow (warm) vs. bluish yellow (cold).

Arnheim also notes that Itten designated complementary pair red-orange ↔ blue-green as the temperature poles, supporting the idea that red admixture warms and blue admixture chills. He connects colour temperature to broader expressive qualities: warm colours invite and feel outgoing; cool colours feel withdrawn and distant. This connects to Kandinsky's observations about yellow spreading outward and blue contracting inward.

Note: Arnheim explicitly states his account has not been systematically tested and may be wrong; the card preserves this uncertainty while extracting the principle.

# Prerequisites

- **Hue** — Supplies chromatic-character and admixture comparisons.
- **Saturation** — Supplies vividness conditions; low-chroma colours can still appear warm/cool.

# Key Properties

1. **Relative character** — Compare actual neighbouring colours and conditions.
2. **Source hypothesis** — Reddish/bluish admixture is Arnheim's uncertain proposal, not a universal transform.
3. **Model coordinates** — An OKLCH angle identifies a chosen hue coordinate, not Kelvin or a complete appearance.
4. **Expression** — Warm/cool descriptions can inform interpretation without diagnosing emotion, trust or agency.
5. **Depth** — Temperature can interact with spatial cues; warmth does not always advance or weigh more.

# Construction / Recognition

## To Construct/Create:
1. Compare the supplied brand colours in their actual arrangement.
2. Try warmer/cooler relationships only where they serve meaning or composition; a warm CTA is not required.
3. If using OKLCH, choose hue/lightness/chroma candidates, inspect gamut and actual state pairs.
4. Do not treat CSS hue-rotate() as white balance or a Kelvin adjustment.

## To Identify/Recognise:
1. Describe relative warmth/coolness alongside hue, lightness and chroma.
2. When discussing a lamp, distinguish an ideal blackbody temperature from CCT, which approximates a source chromaticity rather than its full spectrum.

# Context & Application

Brand, grading and diverging-data palettes may use warm/cool contrasts. Keep supplied identity, readable state pairs and meaningful labels. Emotional and depth readings depend on context; red/orange is not mandatory for action, nor blue a trust guarantee.

## Cross-Domain Connections

**Engineering → STRUCTURAL**: Ideal blackbody colour temperature is a Kelvin reference; CCT relates another source's chromaticity to that locus. A lower-K source can appear warm and a higher-K source cool, but this is not an inverse numerical scale for artistic warmth. CSS hue-rotate() is a specified RGB matrix: neutral (.5,.5,.5) remains neutral even at −20deg, so it cannot universally warm a photograph or rotate every OKLCH hue by that angle.

# Examples

These are retained reported examples from the existing extraction, not independently verified quotations, figures, experiments or historical conclusions.

**Example 1** (pp. 393–394): Arnheim's counterintuitive analysis — "a reddish blue looks warm whereas a bluish red looks cold." In this represented hypothesis, admixture direction rather than dominant hue is proposed to affect temperature. This challenges the common assumption that all reds are warm and all blues are cool.

**Example 2** (p. 394): Itten's temperature poles — red-orange ↔ blue-green as the maximum warm/cool contrast pair, supporting the role of red admixture in warming and blue admixture in cooling.

**Example 3** (pp. 392–393): Kandinsky's colour responses — a yellow circle "reveals a spreading movement outwards from the center"; a blue circle "develops a concentric movement." This spatial expansion/contraction quality is the experiential correlate of warm (advancing) vs. cool (receding).

**Example 4** (p. 394): "Warm colors seem to invite us whereas cold ones keep us at a distance. Warm colors are outgoing, cold ones draw back." The temperature quality connects to social/emotional qualities of openness vs. distance.

# Relationships

## Builds Upon
- **Hue** — Supplies chromatic-family comparisons; saturation supplies a distinct vividness condition.

## Enables
- **Spatial depth in composition** — Warm/cool differences can contribute, without a fixed direction.
- **Emotional palette design** — Contextual expressive choice, not a reliable psychological diagnosis.

## Related
- **Colour harmony** — Temperature consistency or contrast is one option.
- **Colour weight** — Apparent influence is distinct from warmth, wavelength and depth.
- **Complementary colours** — Some chosen pairs contrast warm/cool; this is not required for complementarity.

## Contrasts With
- **Colour harmony through completion** — Source-specific completion and temperature consistency are distinct compositional ideas, not incompatible systems.

# Common Errors

- **Error**: Assuming all reds and oranges are warm and all blues and greens are cool.
  **Correction**: Arnheim's explicitly uncertain admixture hypothesis supplies those comparisons, not a proven rule. Compare actual neighbours and viewing conditions rather than classify every red as warm or every blue as cool.

- **Error**: Using warm/cool to describe physical colour temperature (Kelvin) and perceptual temperature interchangeably.
  **Correction**: Low Kelvin blackbody references can appear warm, but artistic warmth is not an inverse numerical Kelvin scale. CCT concerns source chromaticity; contextual warm/cool comparisons concern appearance.

# Common Confusions

- **Confusion**: "Warm colours are always better for friendly/approachable brands."
  **Clarification**: No temperature category ensures an emotional result. Preserve the supplied brand and assess its particular audience, content and combinations.

- **Confusion**: "Adjusting colour temperature in photo editing is the same as adjusting perceived colour warmth."
  **Clarification**: A white-balance control acts on an image under a model; particular elements may change appearance differently. CSS hue-rotate() is neither Kelvin correction nor exact OKLCH hue rotation.

# Source Reference

Chapter VII: Color, "Art and Visual Perception," pp. 392–395 (section "Warm and Cold").

# Verification Notes

Current bounded review separates appearance, model coordinates and rendering operations as explained above. Technical corrections and local relationship/CQ decisions are same-context proposals; original fidelity and actual rendered/observer outcomes remain unassessed. Extraction-confidence metadata is unchanged.

Legacy extraction notes below are preserved as historical assertions from the predecessor card, **not current verification results**. In particular, their equivalence, chronology, physiology and “Verified” claims are not adopted by this review.

- Definition source: Synthesised from the "Warm and Cold" section. Arnheim's admixture-direction hypothesis is directly stated, with his own acknowledgment of uncertainty ("it has not been tested systematically and may turn out to be quite wrong").
- Confidence rationale: Medium — Arnheim states the hypothesis explicitly but with explicit uncertainty; the card preserves this uncertainty. The warm/cool distinction itself is well-established; Arnheim's specific admixture-direction mechanism is his own speculative contribution.
- Uncertainties: Arnheim's admixture-direction account is not standard colour theory and has not been widely confirmed; noted in the card.
- Cross-reference status: Verified — warm/cool colour temperature is a widely used practical concept. Arnheim's specific mechanism adds nuance not found in most accounts.
- Rosetta Stone check: Mapping added (engineering: physical colour temperature in Kelvin, structural — noting the paradoxical opposite scales).
- OCR issues: None detected.
