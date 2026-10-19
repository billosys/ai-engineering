---
concept: "Hue"
slug: "hue"
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
section: "The Generative Primaries"
extraction_confidence: "medium"
aliases:
  - "chromatic quality"
  - "colour quality"
prerequisites: []
extends: []
related:
  - "saturation"
  - "tonal-value"
  - "colour-constancy"
  - "simultaneous-contrast"
  - "complementary-colours"
  - "colour-temperature"
contrasts_with:
  - "tonal-value"
  - "saturation"
answers_questions:
  - "What is the difference between hue, saturation/chroma, and lightness/value?"
  - "What are the three components of HSL, and why is HSL more useful than hex notation for palette construction?"
rosetta_stone:
  -
    domain: "mathematics"
    concept: "Angular coordinate on a circular/cylindrical colour space"
    rating: "rigorous"
    note: "Hue is a chosen angular coordinate in HSL or polar Oklab; the formulas and reference models differ. At neutral Oklab C=0 hue is undefined. Angle geometry does not establish perceptual uniformity."
  -
    domain: "music"
    concept: "Pitch class (note quality, e.g. C, D, E)"
    rating: "loose"
    note: "A pitch-class cycle and a hue circle share a limited circular-order comparison, without a natural twelve-step hue scale or common interval metric."
css_implementation:
  -
    property: "hue (in oklch/hsl)"
    example: "color: oklch(0.6 0.15 270); /* hue = 270° (blue-violet) */"
    support: "baseline"
  -
    property: "filter: hue-rotate()"
    example: "filter: hue-rotate(90deg); /* RGB matrix, not exact OKLCH hue rotation */"
    support: "baseline"
---

# Quick Definition

Hue describes chromatic character such as red, yellow or blue, distinct from light-dark appearance and vividness. Models encode it with different angular coordinates; numerical independence does not ensure perceptual independence.

# Core Definition

This presents the represented Arnheim account. Exact edition, pages, quotations, named examples, figures, experiments, historical claims and physiological explanations remain unassessed against the unavailable original. Current analytic qualifications do not certify source fidelity.

Hue is the perceptual dimension of colour experience that corresponds to what we ordinarily mean when we say a colour is "red," "orange," "yellow," "green," "blue," or "violet." Arnheim treats hue as the fundamental chromatic identity of a colour, clearly distinguishing it from brightness (the light-dark dimension) and saturation (the purity dimension). In discussing the spectrum and colour organisation, he notes that "the sequence leads seamlessly from one hue to the next" and that pure hues are defined by their perceptual irreducibility: "a blue or yellow or red is pure because it is an irreducible element, i.e., it does not look like a mixture" (Chapter VII, p. 379).

Hue is the quality that makes red and blue perceivably different chromatic qualities while two greys of different lightness remain in the same chromatic category. Arnheim identifies three fundamental primaries — red, yellow, and blue — as the pure hues that serve as irreducible elements from which all others are perceived as mixtures.

The added coordinate comparison uses polar Oklab/CIELAB and CSS HSL separately. A hue angle is model-specific and undefined or powerless at neutral coordinates; no chronology or universal perceptual metric follows.

# Prerequisites

- None — hue is a foundational atomic concept in colour perception.

# Key Properties

1. **Chromatic character** — Categories and continuous changes can coexist when a colour "becomes" another chromatic character.
2. **Chosen circular encoding** — Polar model angles wrap, with non-spectral purples connecting spectral ends; the physical spectrum itself is not a circle.
3. **Distinct coordinates** — L/C/h or H/S/L can be varied numerically; gamut and perceived attributes can still interact.
4. **Source-specific fundamentals** — Arnheim's represented RYB account is not a universal set of physics primaries.
5. **Neutral limit** — Hue is undefined in polar Oklab when C=0, and powerless for HSL neutrals.

# Construction / Recognition

## To Construct/Create:
1. Start from supplied colour and its specified model rather than require a pure RYB anchor.
2. For CSS HSL identify H,S,L; for OKLCH identify L,C,h. Equal angles across the models are not a colour conversion.
3. Use HSL H/S/L to make model relationships explicit during authoring; hex specifies the same sRGB colours via encoded channels. HSL is convenient for some edits, not intrinsically more accurate.
4. Inspect output gamut and actual pairs after hue changes.

## To Identify/Recognise:
1. Name the chromatic family in the current context.
2. Separate the model hue coordinate from measured luminance, brightness/lightness appearance and chroma/saturation.

# Context & Application

Palette and category design can use hue differences alongside labels, icons, patterns or position. HSL exposes hue/saturation/lightness parameters for authoring; hex is a compact sRGB channel notation. Neither syntax makes a palette accessible or provides even perceptual steps.

## Cross-Domain Connections

**Mathematics → RIGOROUS**: A declared hue angle is a circular coordinate. In Oklab polar form h=atan2(b,a), undefined at a=b=0. H+180° defines coordinate opposition, without guaranteeing a neutral mixture or a perceptual complement. HSL's angle follows an encoded-RGB transformation; OKLCH's approximate perceptual aim is not an exact equal-step theorem.

**Music → LOOSE**: A pitch-class cycle and a hue circle permit a limited circular-order comparison. Neither a natural twelve-step hue scale nor a shared interval metric is established.

# Examples

These are retained reported examples from the existing extraction, not independently verified quotations, figures, experiments or historical conclusions.

**Example 1** (p. 371): Arnheim opens Chapter VII by observing that a red ball on green grass is discriminated by its hue alone — "the intense red color that sets it apart from the green grass" — illustrating hue as the primary chromatic discrimination dimension.

**Example 2** (p. 379): The spectrum as a seamless continuum — yet certain hues stand out as perceptually pure (red, yellow, blue), demonstrating the categorical structure of hue perception despite its physical continuity.

**Example 3** (p. 382): Cézanne's use of pure hue: "Cézanne often indicates the highest point of a convexity — a cheek or an apple — by a pure red spot." This is a reported use of redness in modelling, not proof of perceptual isolation from other attributes.

# Relationships

## Builds Upon
- None — hue is treated as foundational here; the absence sentinel is not an edge.

## Enables
- **Saturation** — Supplies chromatic character for discussing vividness; chroma and saturation still require their definitions.
- **Complementary colours** — Ordering supports chosen oppositions, not every physical complement.
- **Colour harmony** — Hue schemes are optional constructions.
- **Colour temperature** — Hue comparisons can contribute to contextual warm/cool descriptions.

## Related
- **Tonal value** — A distinct light-dark appearance description, without universal independence.
- **Saturation** — A distinct appearance attribute or model parameter, without universal orthogonality.
- **Colour constancy** — Concerns conditional object-colour stability under lighting changes.

## Contrasts With
- **Tonal value** — Light-dark appearance versus chromatic character.
- **Saturation** — Vividness/relative colourfulness versus chromatic character under declared definitions.

# Common Errors

- **Error**: Treating hue as equivalent to colour (using "hue" to mean the full colour).
  **Correction**: Hue is one aspect. A specification needs a named model and its full coordinates, reference and output conditions.

- **Error**: Assuming HSL hue angles are perceptually uniform (equal steps = equal perceived difference).
  **Correction**: HSL is derived from encoded sRGB. OKLCH can help explore candidates but does not guarantee equal appearance, constant perceived lightness or in-gamut output across a hue sweep.

# Common Confusions

- **Confusion**: "Changing the hue of a colour changes its lightness too."
  **Clarification**: It depends on which quantity is fixed. HSL red/lime both have L=.5 at full S, yet relative luminances .2126/.7152 and white contrast about 3.9985/1.3722. OKLCH holds its L coordinate, not every observer's perceived lightness.

- **Confusion**: "Red, yellow, and blue are the primaries because of physics."
  **Clarification**: Arnheim's represented fundamental RYB system, additive display primaries and pigment conventions have distinct roles and limits.

# Source Reference

Chapter VII: Color, "Art and Visual Perception," pp. 371–382 (sections "From Light to Color," "Shape and Color," "How Colors Come About," "The Generative Primaries").

# Verification Notes

Current bounded review separates appearance, model coordinates and rendering operations as explained above. Technical corrections and local relationship/CQ decisions are same-context proposals; original fidelity and actual rendered/observer outcomes remain unassessed. Extraction-confidence metadata is unchanged.

Legacy extraction notes below are preserved as historical assertions from the predecessor card, **not current verification results**. In particular, their equivalence, chronology, physiology and “Verified” claims are not adopted by this review.

- Definition source: Synthesised from discussion throughout Chapter VII. Arnheim does not give a single explicit definition of hue; the account is built from his discussion of the spectrum, primaries, and colour properties.
- Confidence rationale: Medium — Arnheim's treatment is phenomenological and distributed across the chapter. He uses "hue" as a technical term but does not define it in isolation from the broader colour discussion.
- Uncertainties: Arnheim's "fundamental primaries" (R, Y, B) differ from modern tristimulus primaries and from painter's process primaries (C, M, Y). The card preserves Arnheim's perceptual framing while noting the discrepancy.
- Cross-reference status: Verified — maps to H in OKLCH/HSL. Arnheim predates CIELAB (1976) and OKLAB (2020); his hue account is perceptual/phenomenological without mathematical specification.
- Rosetta Stone check: Mappings added (mathematics: angular coordinate, rigorous; music: pitch class, loose).
- OCR issues: None detected.
