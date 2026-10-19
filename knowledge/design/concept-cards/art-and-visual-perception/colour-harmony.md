---
concept: "Colour Harmony"
slug: "colour-harmony"
category: "colour-theory"
subcategory: "colour-relationships"
tier: "intermediate"
layer: "2-domain"
source: "Art and Visual Perception: A Psychology of the Creative Eye"
source_slug: "art-and-visual-perception"
authors: "Rudolf Arnheim"
chapter: "VII. Color"
chapter_number: 7
pdf_page: 371
section: "The Fundamental Complementaries"
extraction_confidence: "medium"
aliases:
  - "colour scheme"
  - "chromatic balance"
prerequisites:
  - "hue"
  - "saturation"
  - "complementary-colours"
extends: []
related:
  - "simultaneous-contrast"
  - "complementary-colours"
  - "colour-temperature"
  - "colour-weight"
contrasts_with: []
answers_questions:
  - "How do you construct a colour palette starting from a single brand colour using OKLCH? What systematic steps ensure adequate contrast and accessible combinations?"
  - "A dashboard uses teal header, red error badges, green success indicators, blue links, yellow warning banners, and purple notification badges. It looks like a 'clown car.' What principle was violated, and how do you fix it?"
  - "What is visual hierarchy, and what visual properties (size, colour, contrast, weight, spacing) establish it?"
rosetta_stone:
  -
    domain: "music"
    concept: "Tonal harmony and contextual colour relationships (limited analogy)"
    rating: "loose"
    note: "A chosen pitch-class cycle and hue ordering provide a limited organisational comparison. Frequency ratios, acoustic consonance, colour appearance and aesthetic coherence do not share one metric or mechanism."
css_implementation:
  -
    property: "Custom properties for palette"
    example: "--color-primary: oklch(0.5 0.2 270); --color-accent: oklch(0.6 0.18 90); /* chosen hue opposition; check gamut and actual pairs */"
    support: "baseline"
  -
    property: "color-mix() for palette exploration"
    example: "color-mix(in oklch, var(--color-primary) 70%, var(--color-accent) 30%);"
    support: "baseline"
---

# Quick Definition

Colour harmony is a contextual judgment of coherence among colours. Complementary, analogous or triadic relationships are options for composition; no hue scheme, frequency ratio or quota guarantees harmony.

# Core Definition

This presents the represented Arnheim account. Exact edition, pages, quotations, named examples, figures, experiments, historical claims and physiological explanations remain unassessed against the unavailable original. Current analytic qualifications do not certify source fidelity.

Colour harmony describes the condition in which a set of colours forms a visually satisfying, unified whole. For Arnheim, harmony is not the absence of contrast or tension, but the presence of coherent structure in the relationships among colours. He treats it as the compositional counterpart to the perceptual phenomenon of complementarity: "Goethe describes the interrelation of these six hues in his Theory of Color: 'Single colors affect us, as it were, pathologically... However, the need for totality inherent in our organ guides us beyond this limitation. It sets itself free by producing the opposites of the particulars forced upon it and thus brings about a satisfying completeness'" (Chapter VII, p. 385).

The represented discussion suggests several compositional relationships:
1. **Complementary harmony** — pairs or triplets of hues that produce chromatic completeness (R/G, Y/V, B/O, or the full primary triad R/Y/B).
2. **Structural harmony through mixture** — colours connected by common elements (shared primary components).
3. **Saturation/brightness unity** — colours at similar levels of saturation or brightness can harmonise by tonal consistency.
4. **Compositional resolution** — colours that individually create tension achieve harmony when the composition as a whole achieves balance.

He consistently emphasises that harmony is context-dependent and that the same colours can harmonise or clash depending on their proportions, arrangement, and compositional context.

# Prerequisites

- **Hue** — Supplies a chosen hue ordering.
- **Saturation** — Supplies distinct vividness comparisons.
- **Complementary colours** — Supplies one source-specific opposition/completion family.

# Key Properties

1. **Contextual coherence** — Purpose, arrangement, proportion and viewing context shape the judgment.
2. **Scheme options** — Complementary, analogous and triadic constructions can help exploration without guaranteeing beauty or completeness.
3. **Source-specific primaries** — The represented "three-legged stool" RYB system is distinct from additive RGB, Cleland's Munsell ordering and OKLCH angles.
4. **Multiple attributes** — Lightness and chroma matter alongside hue; coordinates and perceived appearance are distinct.
5. **Meaning before decoration** — Purposeful categorical and semantic colour remains valid; decorative competition can be reduced without banning diversity.

# Construction / Recognition

## To Construct/Create:
1. Start with supplied brand values, task and needed semantic roles.
2. Choose any helpful scheme: a declared OKLCH H+180° opposition, H±120° triad or adjacent-hue set constructs candidates only.
3. Try proportions suitable for the content; 60–70% dominance and similar saturation are optional heuristics.
4. Check output gamut, actual foreground/background/state pairs and non-colour meanings.

## To Identify/Recognise:
1. Judge coherence in the actual arrangement, not just an isolated swatch wheel.
2. Distinguish intentional contrast, data categories and decorative competition.

# Context & Application

Brand, UI and data palettes can use coherent relationships while retaining supplied identity. A dashboard with six meaningful colour roles has not violated a numeric hue quota. Inspect inconsistent meaning, competing emphasis and failing pairs first; consolidate redundant decoration and preserve necessary categories, labels and state distinctions.

## Cross-Domain Connections

**Music → LOOSE**: Frequency ratios can describe musical intervals, but acoustic consonance also depends on timbre and context. A chosen pitch-class cycle and a hue circle offer a limited organisational analogy. They do not share a perception metric, prove opponent-process completion or transfer consonance into visual harmony.

# Examples

These are retained reported examples from the existing extraction, not independently verified quotations, figures, experiments or historical conclusions.

**Example 1** (p. 385): Delacroix's sketchbook triangle — a triangular diagram of the six fundamental hues (three primaries + three secondaries) illustrating the harmonic structure through complementary pairs: "the simplicity of its visual logic" recommends this system to artists.

**Example 2** (p. 382): The secondary triad (orange, purple, green) — "there is unceasing interaction among the three. Each color has a primary in common with each of the other two" — producing a harmonic richness through dynamic tension rather than static balance.

**Example 3** (p. 383): Cézanne's late watercolours avoiding unmixed hues — "the anchorless violets, greens, and reddish yellows seem to move in a constant flux, with no rest anywhere except in the supreme balance of the picture as a whole." Here harmony exists at the compositional level, not within individual colour pairs.

**Example 4** (p. 386): Van Gogh's complementary seasonal pairs as peaceful harmony (used with modulated proportions and low tension deployment), vs. the same system used for terror (equal proportions at maximum saturation). The represented comparison attributes different expression to deployment; it does not supply a universal proportion rule.

# Relationships

## Builds Upon
- **Complementary colours** — Supplies one source-specific relationship family.
- **Hue, saturation** — Supplies distinct descriptive attributes; no scheme is mandatory.

## Enables
- **Palette construction** — Relationships can guide candidate exploration followed by actual role/pair checks.
- **Compositional unity** — Coherence can be judged in arrangement and use.

## Related
- **Simultaneous contrast** — Contextual appearance can affect coherence; it is not harmony's sole mechanism.
- **Colour weight** — Apparent influence may inform proportion without a mass or balance formula.

## Contrasts With
- **Colour discord / clash** — Local aesthetic-description construct; apparent conflict may be deliberate, not proof of missing structure.

# Common Errors

- **Error**: Applying a harmonic colour scheme mechanically (e.g., always using exact complementaries at equal proportions) and expecting harmony.
  **Correction**: Harmonic schemes are starting points, not formulas. Proportion, saturation, lightness, and compositional context all determine whether structural relationships produce harmony or tension.

- **Error**: Mistaking a limited, monotonous palette for harmonic unity.
  **Correction**: Harmony does not require reducing variety — it requires structural coherence. A complex, varied palette with coherent structural relationships achieves harmony; a simple palette with arbitrary choices does not.

# Common Confusions

- **Confusion**: "Colour harmony means all the colours look similar."
  **Clarification**: Similarity or strong contrast may support a composition. Neither adjacent nor opposed hue positions guarantee harmony.

- **Confusion**: "There are fixed rules for colour harmony (the 60-30-10 rule, etc.)."
  **Clarification**: Such proportions are optional heuristics. Preserve supplied identity and meaningful categories; inspect the actual deployment.

# Source Reference

Chapter VII: Color, "Art and Visual Perception," pp. 381–390 (sections "Syntax of Combinations," "The Fundamental Complementaries," "Interaction of Color").

# Verification Notes

Current bounded review separates appearance, model coordinates and rendering operations as explained above. Technical corrections and local relationship/CQ decisions are same-context proposals; original fidelity and actual rendered/observer outcomes remain unassessed. Extraction-confidence metadata is unchanged.

Legacy extraction notes below are preserved as historical assertions from the predecessor card, **not current verification results**. In particular, their equivalence, chronology, physiology and “Verified” claims are not adopted by this review.

- Definition source: Synthesised from multiple sections of Chapter VII. Arnheim does not use "colour harmony" as a section title but treats it throughout the chapter as the goal of colour composition.
- Confidence rationale: Medium — the concept is pervasive but Arnheim's treatment is embedded in broader discussions of composition and interaction rather than isolated as a defined concept.
- Uncertainties: Arnheim's harmonic system is based on the painter's primaries (R/Y/B) and differs from modern colour systems; the card preserves this while noting modern equivalents.
- Cross-reference status: Verified — harmonic schemes are a central topic in practical colour theory; Arnheim's perceptual account provides the theoretical grounding.
- Rosetta Stone check: Mapping added (music: tonal harmony, loose — with explicit note that the analogy is structural, not mechanistic).
- OCR issues: None detected.
