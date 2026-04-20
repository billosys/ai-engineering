---
concept: Musical Interval \u2194 Typographic Ratio (Rosetta Stone)
slug: musical-interval-typographic-ratio
category: design-principles
subcategory: cross-domain-mapping
tier: advanced
layer: 1-principles
source: "More Meaningful Typography"
source_slug: posts
authors: "Tim Brown"
chapter: "Modular scales and how they apply to web design"
chapter_number: null
pdf_page: null
section: null
extraction_confidence: medium
aliases:
  - [harmonic ratios in typography, musical ratios for type, interval-based scale ratios]
prerequisites:
  - scale-ratio
  - modular-scale
  - golden-ratio
extends:
  - scale-ratio
  - ratio-selection-criteria
related:
  - modular-scale-construction
  - typographic-rhythm-modular-scale
contrasts_with:
  - []
answers_questions:
  - "What is the mathematical relationship between musical intervals and typographic scale ratios?"
  - "Why must visual scales be geometric (multiplicative) rather than arithmetic (additive)?"
  - "How do you select an appropriate scale ratio for a given design context?"
rosetta_stone:
  - domain: music
    concept: "Musical interval \u2014 the frequency ratio between two tones (e.g., perfect fifth = 3:2 = 1.5; perfect fourth = 4:3 \u2248 1.333)"
    rating: rigorous
    note: "The numeric ratio defining a musical interval (derived from harmonic series integer ratios) is identical to the numeric ratio used as a typographic scale multiplier. 3:2 applied to frequencies produces a perfect fifth; 1.5 applied to type sizes produces a modular scale step. Same number, different physical domain. Not a metaphor \u2014 a literal numerical identity."
  - domain: mathematics
    concept: "Rational number ratios derived from small integers \u2014 harmonic series ratios n:(n+1) and n:(n+k)"
    rating: rigorous
    note: "Musical interval ratios are ratios of small integers (2:1 octave, 3:2 fifth, 4:3 fourth, 5:4 major third, 9:8 major second). These same ratios, expressed as decimals, are the typographic scale ratios in Tim Brown's framework."
css_implementation:
  - property: "font-size (via scale ratio)"
    example: "/* Perfect fourth scale (ratio 1.333) from 16px */ font-size: 16px; /* step 0 */ font-size: 21.33px; /* step 1: 16 \u00d7 1.333 */ font-size: 28.43px; /* step 2: 16 \u00d7 1.333\u00b2 */ /* Perfect fifth scale (ratio 1.5) from 16px */ font-size: 16px; /* step 0 */ font-size: 24px; /* step 1: 16 \u00d7 1.5 */ font-size: 36px; /* step 2: 16 \u00d7 1.5\u00b2 */"
    support: baseline
---

# Quick Definition

Musical interval ratios (the frequency ratios that define consonant musical intervals) are numerically identical to the ratios used to construct typographic modular scales \u2014 making the correspondence between music theory and type scale construction not a metaphor but a mathematical identity.

# Core Definition

Brown's source text establishes the conceptual bridge in the article's opening: "This and other meaningful ratios rooted in geometry, music, nature, and history can be expressed as modular scales and put to work on the web." The explicit invocation of "music" as a source domain for typographic ratios is the seed of this mapping.

The operational identification is this: a musical interval is defined by the ratio of the frequencies of two tones. The perfect fifth is 3:2 (1.5); the perfect fourth is 4:3 (approximately 1.333); the major third is 5:4 (1.25); the minor third is 6:5 (1.2); the major second is 9:8 (1.125). These ratios are derived from the harmonic series \u2014 integer multiples of a fundamental frequency \u2014 and produce the consonant intervals Western music is built on.

When Tim Brown selects a ratio for a typographic modular scale, he is selecting from exactly this menu of numbers. The ratio 1.333 that produces a "classic" type scale step is the same number as the frequency ratio of a perfect fourth. The ratio 1.5 that produces a "bold" type scale step is the same number as the frequency ratio of a perfect fifth. The mathematical relationship is identical; the physical domain differs.

**Critical note on source evidence**: The article establishes that ratios from "music" are candidates and demonstrates the golden ratio in detail. The specific interval names (perfect fourth, perfect fifth, major second, minor third) and their specific ratios are NOT enumerated in this article text. They are part of Tim Brown's broader framework documented at modularscale.com and in his "More Perfect Typography" talk (referenced in the Further Reading section). The musical interval table is established domain knowledge about Brown's framework, not text extracted from this article. Cards for perfect-fourth-ratio and perfect-fifth-ratio are therefore not well-supported by this specific source text and are omitted per the extraction instructions.

Bringhurst's definition (quoted by Brown) makes the structural parallel explicit: "A modular scale, like a musical scale, is a prearranged set of harmonious proportions." The "like a musical scale" is not merely poetic \u2014 it identifies the source domain from which scale ratios can be drawn.

# Prerequisites

- **Scale ratio** \u2014 Understanding what a typographic scale ratio is.
- **Modular scale** \u2014 Understanding the system the ratios generate.

# Key Properties

1. **Numerical identity**: Musical interval ratios and typographic scale ratios carry the same numbers \u2014 not approximately similar, but identical.
2. **Harmonic grounding**: Musical interval ratios are derived from the harmonic series (integer frequency ratios), giving them a physical basis in acoustic consonance.
3. **Perceptual parallel**: Just as consonant musical intervals feel resolved and harmonious to the ear, scales derived from those same ratios may produce proportional relationships that feel visually resolved \u2014 though this perceptual claim is stronger in the music domain than in the visual domain.
4. **Geometric sequence shared**: Both musical scales and typographic modular scales are ordered sequences generated by a consistent ratio \u2014 the same mathematical structure.
5. **The golden ratio exception**: \u03c6 (1.618) is NOT a simple integer ratio and does not correspond to a consonant musical interval. It belongs to the geometric/natural category of ratios, not the musical interval category.

# Construction / Recognition

## To Construct/Create:
1. Identify that you want a typographic scale with harmonic/musical grounding.
2. Select a musical interval whose character matches the design's needed contrast level:
   - Major second (9:8 \u2248 1.125) \u2014 very subtle, dense hierarchy
   - Minor third (6:5 = 1.2) \u2014 moderate, editorial
   - Perfect fourth (4:3 \u2248 1.333) \u2014 classic, most body text
   - Perfect fifth (3:2 = 1.5) \u2014 bold, strong hierarchy
   - (Golden ratio 1.618 \u2014 extreme, not a musical interval)
3. Use that interval's frequency ratio as your typographic scale ratio.
4. Construct the modular scale as normal.

## To Identify/Recognise:
1. Check whether a scale ratio (1.125, 1.2, 1.25, 1.333, 1.5) corresponds to a musical interval ratio.
2. Ask whether the designer explicitly invoked music theory or harmonic ratios as the source of their ratio choice.

# Context & Application

- **Typical contexts**: Ratio selection stage of modular scale construction; design system documentation; teaching the origins of type scale ratios.
- **Common applications**: Selecting a type scale ratio based on the degree of hierarchical contrast needed, using musical interval terminology to communicate the choice to other designers.
- **Historical/stylistic notes**: Robert Bringhurst's *Elements of Typographic Style* is the canonical source for this mapping in print typography. Tim Brown extended it to web typography and built modularscale.com to make the computation accessible.

## Cross-Domain Connections

**Music \u2192 RIGOROUS**: The frequency ratio of a perfect fifth (3:2 = 1.5) is numerically identical to the typographic scale ratio 1.5. Applied to frequencies, it produces the consonant interval; applied to type sizes, it produces a bold modular scale step. The mathematics is identical; only the physical quantity being scaled differs. This is not a metaphor \u2014 it is a literal numerical identity.

**Mathematics \u2192 RIGOROUS**: Both musical interval ratios and typographic scale ratios are rational numbers (ratios of small integers) applied as common ratios of geometric sequences. The harmonic series origin of musical intervals (integer multiples of a fundamental) provides their mathematical grounding; the same numbers applied to type sizes carry that grounding into the visual domain.

# Examples

**Example 1** (from source, opening): "This and other meaningful ratios rooted in geometry, music, nature, and history can be expressed as modular scales and put to work on the web." \u2014 explicitly names music as a source domain for typographic ratios.

**Example 2** (from source, "Modular scales and how they apply to web design"): Bringhurst quoted: "A modular scale, like a musical scale, is a prearranged set of harmonious proportions." \u2014 structural parallel made explicit.

**Example 3** (from source, Further Reading): "More Perfect Typography" (Vimeo) \u2014 Brown's talk explicitly about starting with type and using modular scales; described as "more inspiration than information."

**Note on the interval table**: The specific mapping of interval names to ratios to typographic applications (the table in the extraction prompt) is derived from Brown's modularscale.com tool and broader framework, not from this article's text. The article supports the existence and principle of the mapping; the detailed table requires the modularscale.com source.

# Relationships

## Builds Upon
- **Scale ratio** \u2014 The musical interval mapping provides the source domain from which typographic scale ratios are derived.
- **Modular scale** \u2014 The mapping populates the menu of candidate ratios for scale construction.

## Enables
- **Ratio selection criteria** \u2014 Knowing that musical intervals provide ratios enables principled ratio selection with harmonic grounding.
- **Modular scale construction** \u2014 The mapping provides concrete ratio candidates with established character.

## Related
- **Typographic rhythm via modular scale** \u2014 The music \u2194 typography analogy extends to rhythm: both depend on proportional relationships structured by consistent ratios.
- **Golden ratio** \u2014 The golden ratio occupies a different position in the ratio menu: geometric/natural, not musical interval.

## Contrasts With
- **Arbitrary ratio selection** \u2014 Using a decimal (e.g., 1.4, 1.35) without grounding in musical, geometric, or cultural significance.

# Common Errors

- **Error**: Treating the music \u2194 typography analogy as merely metaphorical or inspirational.
  **Correction**: The correspondence is numerical \u2014 the same rational number (e.g., 3:2) defines both the perfect fifth in music and the typographic scale ratio 1.5. It is a mathematical identity, not a metaphor.

- **Error**: Assuming the golden ratio (1.618) is a musical interval.
  **Correction**: \u03c6 is irrational and does not correspond to a simple integer frequency ratio. It is a geometric/natural proportion, not a harmonic series ratio. The two categories (musical intervals and geometric proportions) are both valid ratio sources but are mathematically distinct.

# Common Confusions

- **Confusion**: A typographic scale "sounds" like music in some mystical sense because it uses musical ratios.
  **Clarification**: The correspondence is mathematical, not perceptual in that direct sense. The claim is that both domains use ratios derived from the same mathematical family (integer ratios), and that this shared mathematical structure may contribute to harmonic coherence in both domains. The perceptual analogy is structural, not literal.

# Source Reference

Opening paragraph; "Modular scales and how they apply to web design" (Bringhurst quote); "Further Reading" (reference to "More Perfect Typography" talk) \u2014 More Meaningful Typography, Tim Brown (A List Apart, May 2011)

# Verification Notes

- Definition source: Synthesised from the article's explicit invocation of "music" as a ratio source domain and Bringhurst's quoted definition. The detailed interval-to-ratio mapping is established domain knowledge about Brown's broader framework, not text from this article.
- Confidence rationale: Medium \u2014 the principle is clearly supported by the source; the specific interval mappings (perfect fourth = 1.333, etc.) require the modularscale.com source or "More Perfect Typography" talk to verify at the detail level.
- Uncertainties: The article does not provide the interval table. Attribution of specific ratio values (1.333, 1.5, etc.) to this source would be inaccurate \u2014 they are from Brown's broader framework. Cards for perfect-fourth-ratio and perfect-fifth-ratio are not well-enough supported by this article text to include.
- Cross-reference status: Partially verified \u2014 principle verified; detail table requires additional source.
- Rosetta Stone check: Mapping added \u2014 music/musical-interval (rigorous), mathematics/harmonic-series-ratios (rigorous).
- OCR issues: None significant.
