---
concept: "Colour Interaction"
slug: "colour-interaction"
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
section: "Interaction of Color"
extraction_confidence: "high"
aliases:
  - "colour instability"
  - "mutual colour modification"
  - "chromatic interdependence"
prerequisites:
  - "hue"
  - "saturation"
  - "tonal-value"
  - "simultaneous-contrast"
extends:
  - "simultaneous-contrast"
related:
  - "simultaneous-contrast"
  - "colour-harmony"
  - "complementary-colours"
contrasts_with: []
answers_questions:
  - "How do you construct a colour palette starting from a single brand colour using OKLCH? What systematic steps ensure adequate contrast and accessible combinations?"
  - "A dashboard uses teal header, red error badges, green success indicators, blue links, yellow warning banners, and purple notification badges. It looks like a 'clown car.' What principle was violated, and how do you fix it?"
  - "How do you systematically audit an existing interface for visual design quality?"
rosetta_stone:
  -
    domain: "mathematics"
    concept: "Mutual dependency / coupled system of equations"
    rating: "structural"
    note: "Coupled equations illustrate contextual dependency. No linear interaction matrix or measured all-to-all coupling law is established for colour appearance here."
  -
    domain: "engineering"
    concept: "Feedback loop / mutual coupling in circuits"
    rating: "structural"
    note: "Circuit coupling illustrates why system context can matter; it is not the same physical mechanism as contextual colour appearance."
css_implementation:
  -
    property: "CSS custom properties for context-aware colour"
    example: "--color-text: oklch(0.2 0.01 270); /* test in all contexts where this appears */"
    support: "baseline"
  -
    property: "color-mix() in a declared interpolation space"
    example: "color-mix(in oklch, var(--primary) 60%, var(--secondary) 40%);"
    support: "baseline"
---

# Quick Definition

Colour interaction describes context-dependent appearance: the same specified colour can look different in different arrangements. It does not mean every colour necessarily changes every other by one fixed law.

# Core Definition

This presents the represented Arnheim account. Exact edition, pages, quotations, named examples, figures, experiments, historical claims and physiological explanations remain unassessed against the unavailable original. Current analytic qualifications do not certify source fidelity.

Colour interaction is Arnheim's central principle governing all colour experience in visual compositions: appearance is evaluated in an arrangement, while specified colour coordinates can remain fixed. "The most impressive demonstration of the fact that the same part in two different wholes is not the same thing. The same color in two different contexts is not the same color" (Chapter VII, p. 387, Arnheim quoting Ruskin).

The principle extends beyond simultaneous contrast (which describes the direction of the modification) to a systemic claim: the entire colour composition is a mutually dependent whole. "Every hue throughout your work is altered by every touch that you add in other places; so that what was warm a minute ago, becomes cold when you have put a hotter color in another place, and what was in harmony when you left it, becomes discordant as you set other colors beside it" (Ruskin/Arnheim).

The represented account distinguishes two effects:
1. **Contrast** — adjacent colours can emphasise differences; complementary direction is a represented pattern, not a universal law.
2. **Assimilation** — adjacent similar or small-area colours merge and approach each other.

The contrast/assimilation comparison is an organisational account, not a verified common physiological mechanism. The practical consequence: colour decisions cannot be made in isolation; the palette as a whole system must be the unit of design.

# Prerequisites

- **Hue, saturation, tonal value** — Supply distinct appearance descriptions.
- **Simultaneous contrast** — Supplies one contextual comparison; broader composition/assimilation elaborates it.

# Key Properties

1. **Contextual appearance** — Surround, adaptation and geometry can matter.
2. **Selective dependencies** — A changed area may affect other appearances; an all-to-all influence is not established.
3. **Contrast/assimilation** — Differences can be emphasised or reduced depending on arrangement; no universal size threshold is supplied.
4. **Composition** — Coherent arrangement can help intentional relationships without proving a stabilising neural law.
5. **Distinct attributes** — Hue, saturation/chroma and light-dark appearance need separate definitions and model conditions.

# Construction / Recognition

## To Construct/Create:
1. Compare supplied colours on actual surfaces and adjacent regions.
2. Change a relevant area and inspect affected regions rather than assume all change.
3. Use a grey reference chip as an appearance comparison under stated conditions.
4. Try spacing, outlines, area or contrast changes, then inspect the actual result.

## To Identify/Recognise:
1. Compare identical specified swatches across different surrounds.
2. Separate coordinate equality from an observed appearance match; a grey surround is a comparison context, not a context-free truth.

# Context & Application

Multi-colour UI, data graphics and grading benefit from comparisons in actual arrangements. For an audit, inventory roles and surfaces, compare repeated colours and meaningful categories, inspect actual text/non-text pairs and non-colour labels, then revise inconsistent or decorative competition. The colour part of an audit does not supply a complete interface audit or an all-hues quota.

## Cross-Domain Connections

**Mathematics → STRUCTURAL**: Coupled equations illustrate why a local change may have contextual consequences. No interaction matrix, linearity or measured all-to-all dependency is established here; perceived_colour=matrix×specified_colour is not an implemented model.

**Engineering → STRUCTURAL**: Circuit coupling offers a comparison between local and system-level decisions. Image pixels do not electrically couple through palette tokens; the analogy concerns review of dependencies, not an identical mechanism.

# Examples

These are retained reported examples from the existing extraction, not independently verified quotations, figures, experiments or historical conclusions.

**Example 1** (p. 387): Ruskin's warning — "Every hue throughout your work is altered by every touch that you add in other places." Arnheim endorses this as the foundational principle of colour composition.

**Example 2** (p. 387): Kandinsky's observation — "I saw that there was nothing magical about any large surface by itself and that any such surface revealed at once its derivation from the palette; but through another surface, opposed to it, this surface acquired indeed a magic power, so that its origin on the palette seemed unbelievable at first impression." Context transforms colour identity.

**Example 3** (p. 388): Von Allesch — "the pregnancy or variability of any color is reduced when it is put in a context." This is a reported contextual-stability observation, not a general maximum-instability theorem.

**Example 4** (p. 388): The greenish yellow / reddish yellow experiment — individually they both appear pure yellow; placed together they emphasise their differences, each appearing distinctly coloured. Two colours that appear identical in isolation are revealed as different by interaction.

# Relationships

## Builds Upon
- **Simultaneous contrast** — Supplies one contextual-shift account; this card elaborates broader composition and assimilation.
- **Hue, saturation, tonal value** — Supply distinct appearance descriptions.

## Enables
- **Colour composition** — Evaluate arrangements and roles in context.
- **Josef Albers' "Interaction of Color"** — A named source/work connection reported by this extraction, not a separate resolved card.

## Related
- **Colour harmony** — Coherence is an aesthetic/task judgment affected by context.
- **Complementary colours** — A chosen opposition can inform a comparison but does not predict every shift.

## Contrasts With
- **Colour in isolation** — Local comparison-condition construct: a swatch on a reference field is still viewed in a context.

# Common Errors

- **Error**: Finalising palette colours by looking at individual swatches on white backgrounds.
  **Correction**: Include their actual surfaces, neighbours, text and states in the review. White is one context, not all contexts.

- **Error**: Fixing a "wrong" colour by adjusting only that colour without considering how the change propagates.
  **Correction**: Inspect affected neighbours and roles. Some need adjustment; neither universal propagation nor automatic compensation is established.

# Common Confusions

- **Confusion**: "Colour interaction only matters for subtle colour work; primary colours don't interact much."
  **Clarification**: Primary labels do not rank interaction strength. A red CTA on green is not automatically "safe primary red"; it needs the same contextual appearance, semantic and actual pair checks as other colours.

- **Confusion**: "Colour interaction is unpredictable and therefore uncontrollable."
  **Clarification**: Contrast and assimilation provide useful comparisons, while exact magnitude requires the actual arrangement and evidence. Inspect changes rather than promise a universal predictive formula.

# Source Reference

Chapter VII: Color, "Art and Visual Perception," pp. 387–390 (section "Interaction of Color").

# Verification Notes

Current bounded review separates appearance, model coordinates and rendering operations as explained above. Technical corrections and local relationship/CQ decisions are same-context proposals; original fidelity and actual rendered/observer outcomes remain unassessed. Extraction-confidence metadata is unchanged.

Legacy extraction notes below are preserved as historical assertions from the predecessor card, **not current verification results**. In particular, their equivalence, chronology, physiology and “Verified” claims are not adopted by this review.

- Definition source: Synthesised from the "Interaction of Color" section. Arnheim's formulation is explicit and built directly from Ruskin and von Allesch, with his own analytical framework added.
- Confidence rationale: High — colour interaction is Arnheim's most central and explicitly stated colour principle in Chapter VII.
- Uncertainties: The contrast/assimilation distinction is Arnheim's, consistent with Gestalt perceptual organisation principles.
- Cross-reference status: Verified — Josef Albers' "Interaction of Color" (1963) is the definitive practical treatment; Arnheim's account provides the theoretical perceptual grounding.
- Rosetta Stone check: Mappings added (mathematics: coupled system, structural; engineering: mutual coupling, structural).
- OCR issues: None detected.
