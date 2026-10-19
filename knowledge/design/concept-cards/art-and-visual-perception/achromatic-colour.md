---
concept: "Achromatic Colour"
slug: "achromatic-colour"
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
section: "From Light to Color"
extraction_confidence: "medium"
aliases:
  - "neutral colour"
  - "grey scale"
  - "monochrome"
  - "black-white-grey"
prerequisites:
  - "tonal-value"
extends:
  - "tonal-value"
related:
  - "saturation"
  - "hue"
  - "tonal-value"
contrasts_with:
  - "saturation"
  - "hue"
answers_questions:
  - "What is the difference between hue, saturation/chroma, and lightness/value?"
  - "How does the visual-elements concept of 'value' (light-dark range) connect to colour theory's 'lightness' and to contrast as a design principle?"
rosetta_stone:
  -
    domain: "mathematics"
    concept: "The achromatic axis (L axis) in cylindrical colour spaces"
    rating: "rigorous"
    note: "C=0 is the exact neutral-axis construction in polar Oklab; CIELAB uses its own neutral axis. This geometry does not guarantee neutral appearance in every context or identify all lightness coordinates."
css_implementation:
  -
    property: "filter: grayscale()"
    example: "filter: grayscale(1); /* full desaturation */"
    support: "baseline"
  -
    property: "color (neutral values)"
    example: "color: oklch(0.5 0 0); /* chosen neutral coordinate, not a context-free appearance */"
    support: "baseline"
---

# Quick Definition

Achromatic colours have no perceived hue: white, black and greys. A model can define a neutral axis, but a neutral coordinate does not guarantee a context-free neutral appearance.

# Core Definition

This presents the represented Arnheim account. Exact edition, pages, quotations, named examples, figures, experiments, historical claims and physiological explanations remain unassessed against the unavailable original. Current analytic qualifications do not certify source fidelity.

Achromatic colours (Greek: "without colour") describe white, black and intermediate greys. They can vary in light-dark appearance without a discernible hue. Tonal value is a useful pictorial description; CIE brightness and lightness, HSL L and OKLCH L are distinct attributes or coordinates.

Arnheim's represented Chapter VII account connects elementary colour naming to darkness/lightness: "The most elementary nomenclature distinguishes only between darkness and lightness, and all colors are classified according to this simple dichotomy" (p. 373). This reported linguistic example does not prove that all perception begins with an achromatic stage.

Odilon Redon's defence of "his blacks" — "One must respect black. Nothing prostitutes it. It does not please the eye or awaken another sense. It is the agent of the mind even more than the beautiful color of the palette" — preserves the expressive point: achromatic work can carry rich formal meaning.

In Oklab's polar form, C=hypot(a,b)=0 defines its neutral axis and hue is undefined there. CIELAB has a corresponding neutral axis in its own coordinates; CSS HSL uses S=0 for neutral sRGB. These are different models, not one universal lightness or saturation scale.

# Prerequisites

- **Tonal value** — Supplies light-dark appearance comparisons among neutral regions.

# Key Properties

1. **No perceived hue** — The appearance is neutral in the stated context; neighbouring colours and adaptation can change that reading.
2. **Model neutral axes** — OKLCH C=0, CIELAB a*=b*=0 and normalized HSL S=0 describe different coordinate constructions.
3. **Light-dark variation** — Greys differ in appearance; black/white endpoints are relative to the medium and viewing context.
4. **Contrast anchors** — Opaque sRGB black/white is 21:1; a nominal neutral is not automatically an adequate text/background pair.
5. **Expressive register** — Drawing, engraving and black-and-white photography retain form and expressive differences.

# Construction / Recognition

## To Construct/Create:
1. Choose a declared model: OKLCH C=0 or CSS HSL S=0 gives a neutral coordinate.
2. For a neutral sRGB coordinate set encoded R=G=B; physical paint mixtures require material/illumination checks. Equal complements do not guarantee grey.
3. Choose light-dark relationships for the task and check actual rendered pairs.

## To Identify/Recognise:
1. Ask whether a hue is discernible in the viewing context, such as "reddish" or "bluish."
2. In OKLCH, C=0 makes hue undefined; in HSL S=0 makes hue powerless. A stored hue angle alone does not establish chromatic appearance.

# Context & Application

Black-and-white photography, engraving and neutral interface palettes use light-dark relations without requiring chromatic accents. Neutral surfaces can still alter neighbouring appearance; check actual text, icons and states instead of assuming neutrality removes interaction.

# Examples

These are retained reported examples from the existing extraction, not independently verified quotations, figures, experiments or historical conclusions.

**Example 1** (p. 371–372): Odilon Redon's three decades of "blacks" — charcoal drawings and lithographs — demonstrating that achromatic media sustain complete expressive and formal richness without colour.

**Example 2** (p. 373): Berlin and Kay's anthropological data — the most elementary colour nomenclature systems distinguish only dark from light, a reported colour-naming comparison, not proof of a universal perceptual foundation.

**Example 3** (p. 374): "Shape and Color" section — Arnheim notes that a black triangle is as black as a black square, a reported comparison of shape and colour descriptions, not universal independence from context.

# Relationships

## Builds Upon
- **Tonal value** — Supplies the light-dark comparison; this card elaborates its achromatic case, not a physical subtype.

## Enables
- **Tonal contrast** — Neutral pairs isolate a light-dark comparison without proving every boundary clear.
- **Chromatic neutrality** — A local appearance construct: absence of a discernible hue in the stated context, not immunity to induction.

## Related
- **Saturation** — Contrasts chromatic appearance with its neutral limit under a declared definition/model.
- **Tonal value** — Describes light-dark differences, including those among neutral regions.

## Contrasts With
- **Chromatic colour** — Local appearance construct with discernible hue, rather than a separate resolved card.
- **Hue** — A neutral has no perceived hue; a nominal model neutral may appear tinted in context.

# Common Errors

- **Error**: Treating "achromatic" as equivalent to "colourless" or "not a colour."
  **Correction**: Achromatic colours are full members of the colour space; they are experienced as visual qualities (brightness, darkness) and carry full expressive and compositional weight.

- **Error**: Assuming an achromatic neutral background is "safe" or invisible in colour compositions.
  **Correction**: Achromatic colours interact with chromatic neighbours through simultaneous contrast on the lightness axis and can shift perceived brightness of adjacent chromatic areas.

# Common Confusions

- **Confusion**: "Grey is just a dark white or a light black."
  **Clarification**: A grey can occupy a neutral model axis while differing in perceived lightness, texture and expressive role. The greyscale is a useful expressive medium.

- **Confusion**: "Desaturating a colour makes it achromatic."
  **Clarification**: A partial reduction can retain chromatic content. HSL S=0 or OKLCH C=0 defines a neutral coordinate in that model; neither is an observer test.

# Source Reference

Chapter VII: Color, "Art and Visual Perception," pp. 371–374 (sections "From Light to Color," "Shape and Color").

# Verification Notes

Current bounded review separates appearance, model coordinates and rendering operations as explained above. Technical corrections and local relationship/CQ decisions are same-context proposals; original fidelity and actual rendered/observer outcomes remain unassessed. Extraction-confidence metadata is unchanged.

Legacy extraction notes below are preserved as historical assertions from the predecessor card, **not current verification results**. In particular, their equivalence, chronology, physiology and “Verified” claims are not adopted by this review.

- Definition source: Synthesised from the opening sections of Chapter VII. Arnheim does not define "achromatic colour" as a term but clearly treats the dark/light dichotomy as the foundational level of colour organisation.
- Confidence rationale: Medium — the concept is clearly implied and exemplified; explicit definitional treatment requires synthesis from several passages.
- Uncertainties: Arnheim uses "darkness and lightness" rather than "achromatic"; the card uses the standard colour theory term.
- Cross-reference status: Verified — maps to the L axis with C = 0 in OKLCH.
- Rosetta Stone check: Mapping added (mathematics: achromatic axis in OKLCH, rigorous).
- OCR issues: None detected.
