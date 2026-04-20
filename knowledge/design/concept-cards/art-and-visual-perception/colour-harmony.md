---
# === CORE IDENTIFICATION ===
concept: Colour Harmony
slug: colour-harmony

# === CLASSIFICATION ===
category: colour-theory
subcategory: colour-relationships
tier: intermediate
layer: 2-domain

# === PROVENANCE ===
source: "Art and Visual Perception: A Psychology of the Creative Eye"
source_slug: art-and-visual-perception
authors: "Rudolf Arnheim"
chapter: "VII. Color"
chapter_number: 7
pdf_page: 371
section: "The Fundamental Complementaries"

# === CONFIDENCE ===
extraction_confidence: medium

# === VARIANTS ===
aliases:
  - colour scheme
  - chromatic balance

# === TYPED RELATIONSHIPS ===
prerequisites:
  - hue
  - saturation
  - complementary-colours
extends: []
related:
  - simultaneous-contrast
  - complementary-colours
  - colour-temperature
  - colour-weight
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do you construct a colour palette starting from a single brand colour using OKLCH? What systematic steps ensure adequate contrast and accessible combinations?"
  - "A dashboard uses teal header, red error badges, green success indicators, blue links, yellow warning banners, and purple notification badges. It looks like a 'clown car.' What principle was violated, and how do you fix it?"
  - "What is visual hierarchy, and what visual properties (size, colour, contrast, weight, spacing) establish it?"

# === VISUAL DESIGN EXTENSIONS ===
rosetta_stone:
  - domain: music
    concept: "Tonal harmony / consonance (complementary frequency ratios)"
    rating: loose
    note: "Musical harmony involves frequency ratios producing acoustic consonance; colour harmony involves hue relationships producing perceptual completion — both are about structured relationships in circular perceptual spaces, but the mechanisms differ entirely."

css_implementation:
  - property: "Custom properties for palette"
    example: "--color-primary: oklch(0.5 0.2 270); --color-accent: oklch(0.6 0.18 90); /* complementary */"
    support: baseline
  - property: "color-mix() for palette exploration"
    example: "color-mix(in oklch, var(--color-primary) 70%, var(--color-accent) 30%);"
    support: baseline
---

# Quick Definition

Colour harmony is the quality of a colour combination in which all constituent hues relate to one another through a coherent underlying structure — producing a whole that feels balanced, complete, and unified rather than arbitrary or chaotic.

# Core Definition

Colour harmony describes the condition in which a set of colours forms a visually satisfying, unified whole. For Arnheim, harmony is not the absence of contrast or tension, but the presence of coherent structure in the relationships among colours. He treats it as the compositional counterpart to the perceptual phenomenon of complementarity: "Goethe describes the interrelation of these six hues in his Theory of Color: 'Single colors affect us, as it were, pathologically... However, the need for totality inherent in our organ guides us beyond this limitation. It sets itself free by producing the opposites of the particulars forced upon it and thus brings about a satisfying completeness'" (Chapter VII, p. 385).

Arnheim identifies several types of harmonic relationship:
1. **Complementary harmony** — pairs or triplets of hues that produce chromatic completeness (R/G, Y/V, B/O, or the full primary triad R/Y/B).
2. **Structural harmony through mixture** — colours connected by common elements (shared primary components).
3. **Saturation/brightness unity** — colours at similar levels of saturation or brightness can harmonise by tonal consistency.
4. **Compositional resolution** — colours that individually create tension achieve harmony when the composition as a whole achieves balance.

He consistently emphasises that harmony is context-dependent and that the same colours can harmonise or clash depending on their proportions, arrangement, and compositional context.

# Prerequisites

- **Hue** — Harmonic relationships are defined in terms of hue relationships.
- **Saturation** — Saturation consistency or contrast is part of harmonic structure.
- **Complementary colours** — The most widely used harmonic schemes are built on complementary relationships.

# Key Properties

1. **Structural, not arbitrary** — Harmony results from coherent structural relationships among colours, not from following fixed rules without understanding.
2. **Context-dependent** — The same colours can harmonise or clash depending on proportion, arrangement, and composition.
3. **Perceptual completeness** — Harmonic combinations satisfy the eye's demand for chromatic wholeness (the "three-legged stool" of R/Y/B).
4. **Multiple harmonic types** — Complementary, analogous, triadic, and split-complementary schemes each produce harmony through different structural relationships.
5. **Saturation and value matter** — Harmony is affected by all three colour dimensions; hue relationships alone do not determine harmony.

# Construction / Recognition

## To Construct/Create:
1. Choose a dominant hue (primary colour of the palette).
2. Select a harmonic scheme:
   - **Complementary**: add 180° to the dominant H in OKLCH.
   - **Triadic**: add 120° and 240°.
   - **Analogous**: ±20°–40° from dominant.
   - **Split-complementary**: ±30° from the complement.
3. Adjust proportions: use the dominant hue for ~60–70% of chromatic area, complement/accents for smaller portions.
4. Unify saturation levels: bring all colours to a similar saturation range unless deliberate contrast is intended.
5. Test in context: all colours must be evaluated together, in the actual design environment.

## To Identify/Recognise:
1. Does the palette feel unified even if varied? Are there clear structural relationships among hues?
2. Does removing any one colour leave the others feeling incomplete (pointing to a complementary or triadic structure)?
3. Do the colours interact productively (enhancing each other) or destructively (creating noise)?

# Context & Application

- **Typical contexts**: Brand identity palette construction, UI colour systems, data visualisation categorical palettes, interior design, fashion, editorial design.
- **Common applications**: Primary/secondary/accent colour systems in design tokens; categorical data palettes in information visualisation; brand colour guidelines specifying relationships between primary and accent colours.

## Cross-Domain Connections

**Music → LOOSE**: Musical harmony refers to the consonance of simultaneously sounding tones, grounded in simple frequency ratios (octave = 2:1, perfect fifth = 3:2). The analogy to colour harmony is structural — both involve relationships among elements in a circular perceptual space — but mechanically different. Acoustic consonance results from the absence of beating between close overtones; colour harmony results from complementary opponent-process completion and coherent structural relationships. The 12-hue colour wheel does not map to 12 equal-temperament semitones in any rigorous way (Arnheim does not claim it does; those who do are making a loose structural analogy).

# Examples

**Example 1** (p. 385): Delacroix's sketchbook triangle — a triangular diagram of the six fundamental hues (three primaries + three secondaries) illustrating the harmonic structure through complementary pairs: "the simplicity of its visual logic" recommends this system to artists.

**Example 2** (p. 382): The secondary triad (orange, purple, green) — "there is unceasing interaction among the three. Each color has a primary in common with each of the other two" — producing a harmonic richness through dynamic tension rather than static balance.

**Example 3** (p. 383): Cézanne's late watercolours avoiding unmixed hues — "the anchorless violets, greens, and reddish yellows seem to move in a constant flux, with no rest anywhere except in the supreme balance of the picture as a whole." Here harmony exists at the compositional level, not within individual colour pairs.

**Example 4** (p. 386): Van Gogh's complementary seasonal pairs as peaceful harmony (used with modulated proportions and low tension deployment), vs. the same system used for terror (equal proportions at maximum saturation). Same structural scheme, opposite harmonic effect — determined by deployment.

# Relationships

## Builds Upon
- **Complementary colours** — The foundation of the most prominent harmonic schemes.
- **Hue, saturation** — All dimensions participate in harmonic relationships.

## Enables
- **Palette construction** — Practical palette design applies harmonic principles systematically.
- **Compositional unity** — Harmonic colour relationships contribute to the unity of a visual composition.

## Related
- **Simultaneous contrast** — Contrast is the mechanism; harmony is the controlled use of contrast toward aesthetic ends.
- **Colour weight** — Weight imbalance disrupts harmony; harmonic palettes typically manage visual weight through proportion.

## Contrasts With
- **Colour discord / clash** — When colours lack structural relationship and interact destructively (mutual repulsion without resolution).

# Common Errors

- **Error**: Applying a harmonic colour scheme mechanically (e.g., always using exact complementaries at equal proportions) and expecting harmony.
  **Correction**: Harmonic schemes are starting points, not formulas. Proportion, saturation, lightness, and compositional context all determine whether structural relationships produce harmony or tension.

- **Error**: Mistaking a limited, monotonous palette for harmonic unity.
  **Correction**: Harmony does not require reducing variety — it requires structural coherence. A complex, varied palette with coherent structural relationships achieves harmony; a simple palette with arbitrary choices does not.

# Common Confusions

- **Confusion**: "Colour harmony means all the colours look similar."
  **Clarification**: Analogous schemes (similar hues) are harmonious, but complementary and triadic schemes achieve harmony through structural completeness, not similarity. Maximum contrast can be maximally harmonic.

- **Confusion**: "There are fixed rules for colour harmony (the 60-30-10 rule, etc.)."
  **Clarification**: These rules of thumb (e.g., 60% dominant / 30% secondary / 10% accent) are practical heuristics, not perceptual laws. Arnheim's analysis shows harmony is contextual and compositional, not formula-dependent.

# Source Reference

Chapter VII: Color, "Art and Visual Perception," pp. 381–390 (sections "Syntax of Combinations," "The Fundamental Complementaries," "Interaction of Color").

# Verification Notes

- Definition source: Synthesised from multiple sections of Chapter VII. Arnheim does not use "colour harmony" as a section title but treats it throughout the chapter as the goal of colour composition.
- Confidence rationale: Medium — the concept is pervasive but Arnheim's treatment is embedded in broader discussions of composition and interaction rather than isolated as a defined concept.
- Uncertainties: Arnheim's harmonic system is based on the painter's primaries (R/Y/B) and differs from modern colour systems; the card preserves this while noting modern equivalents.
- Cross-reference status: Verified — harmonic schemes are a central topic in practical colour theory; Arnheim's perceptual account provides the theoretical grounding.
- Rosetta Stone check: Mapping added (music: tonal harmony, loose — with explicit note that the analogy is structural, not mechanistic).
- OCR issues: None detected.
