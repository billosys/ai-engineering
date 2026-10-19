---
concept: "Saturation"
slug: "saturation"
category: "colour-theory"
subcategory: "colour-properties"
tier: "foundational"
layer: "2-domain"
source: "Art and Visual Perception: A Psychology of the Creative Eye"
source_slug: "art-and-visual-perception"
authors: "Rudolf Arnheim"
chapter: "VII. Color"
chapter_number: 7
pdf_page: 371
section: "Interaction of Color"
extraction_confidence: "medium"
aliases:
  - "colour intensity"
  - "vividness"
prerequisites:
  - "hue"
extends: []
related:
  - "hue"
  - "tonal-value"
  - "simultaneous-contrast"
  - "colour-constancy"
contrasts_with:
  - "tonal-value"
  - "achromatic-colour"
answers_questions:
  - "What is the difference between hue, saturation/chroma, and lightness/value?"
  - "What are the three components of HSL, and why is HSL more useful than hex notation for palette construction?"
  - "How do you ensure a coloured status badge communicates its meaning without relying solely on colour? What redundant encoding strategies exist?"
rosetta_stone:
  -
    domain: "mathematics"
    concept: "Saturation versus OKLCH chroma (distinct attributes)"
    rating: "rigorous"
    note: "C=hypot(a,b) is an exact Oklab polar-coordinate relation. CIE saturation uses own brightness while CIE chroma uses an achromatic reference; neither is universally equal to C or a perceptually uniform slider."
css_implementation:
  -
    property: "chroma (in oklch)"
    example: "color: oklch(0.6 0.25 150); /* C=0.25 model coordinate; check output gamut */"
    support: "baseline"
  -
    property: "saturation (in hsl)"
    example: "color: hsl(150 80% 45%); /* HSL S=80%, distinct from CIE saturation */"
    support: "baseline"
  -
    property: "filter: saturate()"
    example: "filter: saturate(1.5); /* RGB matrix effect, not a measured appearance gain */"
    support: "baseline"
---

# Quick Definition

Saturation describes colourfulness relative to an area's own brightness in CIE appearance terminology. Ordinary “vividness” and “colour intensity” are search vocabulary, while HSL/HSV S, OKLCH C and purity have distinct model or source meanings.

# Core Definition

This presents the represented Arnheim account. Exact edition, pages, quotations, named examples, figures, experiments, historical claims and physiological explanations remain unassessed against the unavailable original. Current analytic qualifications do not certify source fidelity.

Saturation, chroma and purity are related vocabulary, not interchangeable technical definitions. CIE saturation compares colourfulness with the area's own brightness; CIE chroma uses the brightness of a similarly illuminated achromatic reference. Oklab polar C=hypot(a,b) is an exact coordinate, not a context-free absolute colourfulness measure. HSL S and HSV S are different encoded-RGB parameters.

The represented Arnheim account discusses relations among attributes: "the distinctness of color depends more upon brightness than upon hue" (p. 389); colours can "also be related only through their brightness or saturation, not as hues" (p. 382); and "Relations between hues cannot be described adequately without reference to saturation and brightness" (p. 389). These are source-attributed observations, not proofs of perceptual independence.

Arnheim's represented use of "purity" also concerns hue admixture: "If we examine the raw material of color gradations... we observe that certain colors are distinguished by their purity... an orange or a green looks pure when it is only itself, e.g., without an admixture that would make us speak of a reddish orange or a yellowish green" (p. 379). Hue irreducibility, spectral/colorimetric purity and saturation must therefore remain distinct. The historical passage survives without making purity or chroma a strict alias.

# Prerequisites

- **Hue** — Supplies chromatic character; the appearance/model definition determines how saturation is interpreted.

# Key Properties

1. **Definition/reference** — CIE saturation uses own brightness; CIE chroma uses a similarly illuminated achromatic reference.
2. **Model parameters** — HSL S, HSV S and OKLCH C have different formulas and scales.
3. **Neutral coordinate** — OKLCH C=0 or normalized HSL S=0 defines a model neutral, with hue undefined/powerless.
4. **Gamut dependence** — Available chroma varies with lightness, hue and destination gamut; no universal chroma maximum follows.
5. **Appearance interaction** — Holding numeric L while changing C/S need not preserve perceived lightness or contrast.

# Construction / Recognition

## To Construct/Create:
1. Name the appearance attribute or model parameter being changed.
2. In Oklab polar form compute C=hypot(a,b); varying it at fixed L/h is a coordinate construction.
3. In HSL identify S and L explicitly; HSL exposes relationships for authoring while hex stores the same sRGB colours as encoded channels.
4. Inspect gamut and actual text/background/state pairs after changes; no vividness setting substitutes for redundant meaning.

## To Identify/Recognise:
1. Compare vividness in the stated context, without treating a slider value as an observer measurement.
2. Distinguish a neutral coordinate, a low-chroma colour and a source's use of "pure".

# Context & Application

Palette emphasis, data graphics and states can use vivid/dull differences if they serve the task. Do not convey disabled/error meaning by saturation alone: an unavailable action can show visible “Unavailable” text with its real input state, and an error badge can show “Error” plus a meaningful icon/shape. Preserve legible labels and actual inactive versus active semantics; this small application does not implement or verify a whole widget.

## Cross-Domain Connections

**Mathematics → RIGOROUS**: C=hypot(a,b) and a=Ccos(h), b=Csin(h) are literal Oklab polar-coordinate identities. They do not equate C with CIE saturation or guarantee equal-looking C steps. HSL S derives from encoded-RGB extrema; changing it at fixed HSL L can change relative luminance. Numeric parameter separation is not perceptual orthogonality.

# Examples

These are retained reported examples from the existing extraction, not independently verified quotations, figures, experiments or historical conclusions.

**Example 1** (p. 379): Arnheim's discussion of colour purity — "an orange or a green looks pure when it is only itself, e.g., without an admixture that would make us speak of a reddish orange." This reported purity example concerns hue admixture; it is not a definition equating purity with CIE saturation or OKLCH chroma.

**Example 2** (p. 389): Liebmann's experiment — placing a red figure on a green background of equal brightness makes boundaries "fluid, soft, colloidal." The colour boundary is visible because the hues differ, but the perceptual separation weakens. The represented observation does not establish a universal saturation adjustment or adequate text contrast.

**Example 3** (p. 382): In describing mixtures of primaries, Arnheim notes that pure primaries "can be related only through their brightness or saturation, not as hues" — a reported comparison "through their saturation", not proof of perceptual independence.

# Relationships

## Builds Upon
- **Hue** — Supplies chromatic character for the vividness comparison, not a universal logical dependency for every saturation definition.

## Enables
- **Colour harmony** — Controlled vividness comparisons can serve a palette.
- **Simultaneous contrast** — Context can affect apparent saturation.
- **Colour weight** — Vividness may affect influence without a fixed attention/weight ranking.

## Related
- **Tonal value** — A distinct light-dark description; not universally orthogonal.
- **Achromatic colour** — A neutral appearance/coordinate limit under stated conditions.
- **Simultaneous contrast** — Appearance shifts require actual context.

## Contrasts With
- **Tonal value** — Light-dark appearance versus defined relative colourfulness/model parameter.
- **Achromatic colour** — No perceived hue, distinguished from partial desaturation.

# Common Errors

- **Error**: Equating desaturation with darkening (reducing saturation to make a colour "less prominent").
  **Correction**: They change different model coordinates, but appearance and prominence can interact. Holding HSL L or OKLCH L does not ensure constant relative luminance or perceived lightness.

- **Error**: Assuming maximum HSL saturation (S=100%) means maximum perceptual saturation.
  **Correction**: HSL's parameter is model-specific. OKLCH C is a useful coordinate with hue/lightness/gamut limits, not an equal-intensity guarantee.

# Common Confusions

- **Confusion**: "Saturation and brightness are the same — a bright colour is saturated."
  **Clarification**: Brightness is an appearance attribute; saturation relates colourfulness to own brightness. A model can vary parameters separately without making perception universally independent.

- **Confusion**: "Chroma and saturation are the same thing."
  **Clarification**: Their CIE reference brightnesses differ. HSL/HSV parameters and Oklab C also differ from those appearance terms; no universal C/L or common slider conversion is supplied.

# Source Reference

Chapter VII: Color, "Art and Visual Perception," pp. 379–389 (sections "The Generative Primaries," "Fundamental Primaries," "Syntax of Combinations," "Interaction of Color").

# Verification Notes

Current bounded review separates appearance, model coordinates and rendering operations as explained above. Technical corrections and local relationship/CQ decisions are same-context proposals; original fidelity and actual rendered/observer outcomes remain unassessed. Extraction-confidence metadata is unchanged.

Legacy extraction notes below are preserved as historical assertions from the predecessor card, **not current verification results**. In particular, their equivalence, chronology, physiology and “Verified” claims are not adopted by this review.

- Definition source: Synthesised from distributed discussion. Arnheim treats saturation/purity as a key dimension throughout Chapter VII but does not isolate it in a single definitional passage.
- Confidence rationale: Medium — the concept is clearly present and used technically, but Arnheim's treatment is embedded in broader discussion rather than systematically defined.
- Uncertainties: Arnheim uses "purity" and "saturation" with some terminological overlap; the card normalises to "saturation" (standard design term) with "chroma" as the modern mathematical alias.
- Cross-reference status: Verified — maps to C (chroma) in OKLCH. Arnheim predates CIELAB (1976) and OKLAB (2020).
- Rosetta Stone check: Mapping added (mathematics: chroma in OKLCH, rigorous).
- OCR issues: None detected.
