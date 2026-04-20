---
# === CORE IDENTIFICATION ===
concept: Colour Interaction
slug: colour-interaction

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
section: "Interaction of Color"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - colour instability
  - mutual colour modification
  - chromatic interdependence

# === TYPED RELATIONSHIPS ===
prerequisites:
  - hue
  - saturation
  - tonal-value
  - simultaneous-contrast
extends:
  - simultaneous-contrast
related:
  - simultaneous-contrast
  - colour-harmony
  - complementary-colours
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do you construct a colour palette starting from a single brand colour using OKLCH? What systematic steps ensure adequate contrast and accessible combinations?"
  - "A dashboard uses teal header, red error badges, green success indicators, blue links, yellow warning banners, and purple notification badges. It looks like a 'clown car.' What principle was violated, and how do you fix it?"
  - "How do you systematically audit an existing interface for visual design quality?"

# === VISUAL DESIGN EXTENSIONS ===
rosetta_stone:
  - domain: mathematics
    concept: "Mutual dependency / coupled system of equations"
    rating: structural
    note: "Colour interaction means that perceived colour values form a coupled system: each colour's appearance is a function of all other colours, analogous to a system of simultaneous equations where no variable can be solved independently."
  - domain: engineering
    concept: "Feedback loop / mutual coupling in circuits"
    rating: structural
    note: "Colour interaction is like mutual coupling in a circuit: each element affects all others, and changing one element propagates changes throughout the system — palette design must account for system-level effects, not just individual element properties."

css_implementation:
  - property: "CSS custom properties for context-aware colour"
    example: "--color-text: oklch(0.2 0.01 270); /* test in all contexts where this appears */"
    support: baseline
  - property: "color-mix() for predictable blending"
    example: "color-mix(in oklch, var(--primary) 60%, var(--secondary) 40%);"
    support: baseline
---

# Quick Definition

Colour interaction is the fundamental principle that a colour's perceived appearance is never absolute but always modified by the colours surrounding it — making colour an inherently relational and context-dependent phenomenon in visual composition.

# Core Definition

Colour interaction is Arnheim's central principle governing all colour experience in visual compositions: no colour exists as an isolated, fixed entity — every colour is transformed by every other colour present in the composition. "The most impressive demonstration of the fact that the same part in two different wholes is not the same thing. The same color in two different contexts is not the same color" (Chapter VII, p. 387, Arnheim quoting Ruskin).

The principle extends beyond simultaneous contrast (which describes the direction of the modification) to a systemic claim: the entire colour composition is a mutually dependent whole. "Every hue throughout your work is altered by every touch that you add in other places; so that what was warm a minute ago, becomes cold when you have put a hotter color in another place, and what was in harmony when you left it, becomes discordant as you set other colors beside it" (Ruskin/Arnheim).

Arnheim identifies two main mechanisms:
1. **Contrast** — adjacent colours emphasise their differences (in the direction of the complement).
2. **Assimilation** — adjacent similar or small-area colours merge and approach each other.

Both mechanisms are expressions of the same underlying drive toward the most clear-cut perceptual organisation available. The practical consequence: colour decisions cannot be made in isolation; the palette as a whole system must be the unit of design.

# Prerequisites

- **Hue, saturation, tonal value** — Interaction modifies all three dimensions.
- **Simultaneous contrast** — The primary mechanism through which interaction operates at boundaries.

# Key Properties

1. **Context-absolute** — Every colour's appearance is determined by its total context; there is no context-independent colour appearance.
2. **System-level phenomenon** — Changing one colour in a composition changes all others (to varying degrees).
3. **Two opposing mechanisms** — Contrast (emphasising differences at large scale/large areas) and assimilation (merging similar/small-area colours) are antagonistic and context-dependent.
4. **Compositional stabilisation** — Well-organised compositions stabilise colour interactions; poorly organised compositions allow interactions to create visual noise.
5. **Dependency on all colour dimensions** — Interaction affects hue, saturation, and lightness simultaneously.

# Construction / Recognition

## To Construct/Create:
1. Always evaluate colours in context — never finalise a colour decision by looking at the swatch in isolation.
2. Build a palette iteratively: add colours one at a time and observe how each addition changes the appearance of all previous colours.
3. Use a neutral grey reference chip to test for interaction: if the grey looks different on different background colours, the interaction is significant.
4. To control assimilation: increase area size or saturation difference; to control contrast: increase similarity or reduce area.

## To Identify/Recognise:
1. Colour interaction is operating when: a colour looks right in the palette view but wrong in the actual design context; a colour that looked warm becomes cool when a warmer colour is added nearby.
2. Test: isolate any colour element from its context (grey surround) and compare its appearance to in-context.

# Context & Application

- **Typical contexts**: Multi-colour UI systems, brand palette implementation, data visualisation, colour grading, complex illustration.
- **Common applications**: Testing all colour combinations in the design system before finalising; adjusting individual colours after the system is assembled; understanding why a "clown car" palette (too many competing saturated colours) fails — all colours mutually destabilise each other; auditing existing interfaces for colour coherence.

## Cross-Domain Connections

**Mathematics → STRUCTURAL**: Colour interaction creates a coupled system where each colour's appearance is a function of all others. This is analogous to a system of simultaneous equations: no variable (colour) can be solved independently of all the others. In matrix terms: perceived_colour_vector = interaction_matrix × specified_colour_vector. The interaction matrix is determined by the composition's geometry (area sizes, adjacency, spatial frequency).

**Engineering → STRUCTURAL**: In circuit design, mutual coupling between inductors or amplifier stages means changing one element's value propagates effects throughout the circuit. The system must be analysed as a whole, not as independent components. Colour interaction is the visual analogue: design systems must account for how colours behave in combination, not just in isolation.

# Examples

**Example 1** (p. 387): Ruskin's warning — "Every hue throughout your work is altered by every touch that you add in other places." Arnheim endorses this as the foundational principle of colour composition.

**Example 2** (p. 387): Kandinsky's observation — "I saw that there was nothing magical about any large surface by itself and that any such surface revealed at once its derivation from the palette; but through another surface, opposed to it, this surface acquired indeed a magic power, so that its origin on the palette seemed unbelievable at first impression." Context transforms colour identity.

**Example 3** (p. 388): Von Allesch — "the pregnancy or variability of any color is reduced when it is put in a context." Composition stabilises colour interaction; without compositional organisation, colours are maximally unstable (ambiguous, changing).

**Example 4** (p. 388): The greenish yellow / reddish yellow experiment — individually they both appear pure yellow; placed together they emphasise their differences, each appearing distinctly coloured. Two colours that appear identical in isolation are revealed as different by interaction.

# Relationships

## Builds Upon
- **Simultaneous contrast** — The primary mechanism through which interaction operates.
- **Hue, saturation, tonal value** — Interaction modifies all three.

## Enables
- **Colour composition** — The entire practice of colour composition depends on understanding and controlling interaction.
- **Josef Albers' "Interaction of Color"** — Arnheim explicitly references Albers' work as the definitive systematic study of this principle.

## Related
- **Colour harmony** — Harmony is the state in which colour interactions are aesthetically productive; discord is when they are destructive.
- **Complementary colours** — Understanding complementary relationships enables predicting the direction of interaction.

## Contrasts With
- **Colour in isolation** — The (incorrect) assumption that a colour's appearance is fixed by its specification; colour interaction refutes this.

# Common Errors

- **Error**: Finalising palette colours by looking at individual swatches on white backgrounds.
  **Correction**: Colours must always be evaluated in their actual context — on the actual backgrounds they will appear against, next to the actual other colours they will be combined with.

- **Error**: Fixing a "wrong" colour by adjusting only that colour without considering how the change propagates.
  **Correction**: Changing any colour in a composition changes all others (to varying degrees). Adjustments to one element may require compensating adjustments to others.

# Common Confusions

- **Confusion**: "Colour interaction only matters for subtle colour work; primary colours don't interact much."
  **Clarification**: Primary colours interact most strongly — they have the greatest complementary contrast. A red CTA button on a green background is not "safe primary red"; it is dramatically altered by the green background through maximum complementary interaction.

- **Confusion**: "Colour interaction is unpredictable and therefore uncontrollable."
  **Clarification**: Colour interaction follows systematic principles (contrast and assimilation) and can be predicted and controlled. Arnheim's principle is not a counsel of despair but a call for systemic thinking about palettes.

# Source Reference

Chapter VII: Color, "Art and Visual Perception," pp. 387–390 (section "Interaction of Color").

# Verification Notes

- Definition source: Synthesised from the "Interaction of Color" section. Arnheim's formulation is explicit and built directly from Ruskin and von Allesch, with his own analytical framework added.
- Confidence rationale: High — colour interaction is Arnheim's most central and explicitly stated colour principle in Chapter VII.
- Uncertainties: The contrast/assimilation distinction is Arnheim's, consistent with Gestalt perceptual organisation principles.
- Cross-reference status: Verified — Josef Albers' "Interaction of Color" (1963) is the definitive practical treatment; Arnheim's account provides the theoretical perceptual grounding.
- Rosetta Stone check: Mappings added (mathematics: coupled system, structural; engineering: mutual coupling, structural).
- OCR issues: None detected.
