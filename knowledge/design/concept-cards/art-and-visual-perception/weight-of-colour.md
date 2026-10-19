---
concept: "Weight of Colour"
slug: "weight-of-colour"
category: "design-principles"
subcategory: "balance"
tier: "intermediate"
layer: "1-principles"
source: "Art and Visual Perception: A Psychology of the Creative Eye"
source_slug: "art-and-visual-perception"
authors: "Rudolf Arnheim"
chapter: "I. Balance"
chapter_number: 1
pdf_page: 11
section: "Weight"
extraction_confidence: "medium"
aliases:
  - "chromatic weight"
  - "hue weight"
  - "colour balance"
  - "saturation weight"
prerequisites:
  - "visual-weight"
  - "tonal-weight"
extends:
  - "visual-weight"
related:
  - "visual-balance"
  - "tonal-weight"
  - "colour-weight"
contrasts_with:
  - "weight-by-location"
answers_questions:
  - "A dashboard uses teal header, red error badges, green success indicators, blue links, yellow warning banners, and purple notification badges. It looks like a 'clown car.' What principle was violated, and how do you fix it?"
  - "What is visual hierarchy, and what visual properties (size, colour, contrast, weight, spacing) establish it?"
  - "How does the visual-elements concept of 'value' (light-dark range) connect to colour theory's 'lightness' and to contrast as a design principle?"
rosetta_stone:
  -
    domain: "music"
    concept: "Timbre / tonal colour (klangfarbe)"
    rating: "loose"
    note: "Timbre and hue offer a qualitative comparison, without a calibrated translation or independent additive weight dimension."
  -
    domain: "mathematics"
    concept: "Wavelength / perceptual salience"
    rating: "loose"
    note: "Display colours need not have one wavelength. Cone sensitivity alone does not establish a universal longer-wavelength salience or colour-weight order."
css_implementation:
  -
    property: "color / background-color"
    example: "color: hsl(0 80% 45%); /* candidate foreground; no universal semantic or weight role */"
    support: "baseline"
  -
    property: "filter: saturate()"
    example: "filter: saturate(0.3); /* changes rendered colours; no guaranteed reduced prominence */"
    support: "baseline"
---

# Quick Definition

Weight of colour describes the contextual influence of colour attributes on composition. Arnheim’s red/blue comparison does not establish a universal warm-to-cool ranking, an additive hue weight or semantic priority roles.

# Core Definition

This is the represented Arnheim account. Its quotations, page/figure references and historical, experimental or neural claims have not been checked against the unavailable original. The analytic qualifications below do not certify source fidelity.

Arnheim notes that colour contributes to visual weight: "As to *color*, red is heavier than blue, and bright colors are heavier than dark ones." This reports two comparisons; it does not establish independent additive hue and brightness dimensions, a full rainbow ordering or replicated universal warm/cool effects. In the St. Michael painting example, the painter used "a large dark patch on the angel's robe" to create visual attraction (weight) — but in the Van Gogh bedroom example he interprets the bedcover’s colour as creating "a strong off-center weight." A clown's costume with red on the left and blue on the right "may be asymmetrical to the eye as a color scheme, even though the two halves of the costume...are equal in physical weight." This is a reported distinction between physical and compositional weight, not a verified isolation of hue from all appearance/context variables.

# Prerequisites

- **Visual weight** — Supplies the broader compositional vocabulary.
- **Tonal weight** — Distinguishes light-dark appearance from physical area and from a universal weight law.

# Key Properties

1. **Hue**: The reported red/blue comparison is narrower than all warm versus cool colours.
2. **Chroma/saturation**: Vividness may contribute to emphasis; there is no independent additive term or guaranteed ranking.
3. **Red versus blue**: "red is heavier than blue" is the source’s statement, not proof that red is the heaviest hue.
4. Physical mass and compositional influence differ; identical size does not control every perceptual variable.
5. Colour, area, placement, meaning and surround interact in an actual composition.

# Construction / Recognition

## To Identify/Recognise:
1. Compare the actual colour-bearing areas and surrounding context.
2. A small red accent that "jumps out" can be conspicuous, but that does not prove an intrinsic red weight.
3. A loud dashboard may have competing roles, labels or grouping; hue count alone is not a diagnosis.

## To Construct/Create:
1. Preserve supplied identity and semantic colour roles.
2. Compare emphasis using actual foreground/background pairs, size, position and grouping.
3. Use non-colour labels or shape where meaning matters.
4. Inspect states and applicable contrast before reducing chroma or changing hue; warm-primary/cool-secondary is not a required system.

# Context & Application

- **Typical contexts**: Palette review, interface hierarchy and data visualisation.
- **Common applications**: A CTA need not be red or orange. A dashboard may correctly use teal headers, red errors, green success, blue links, yellow warnings and purple notifications. Review meaning, competition, grouping, labels and actual pairs; no hue-count law was violated merely by those six hues.
- **Historical/stylistic notes**: The Chapter I discussion is brief and is kept distinct from the Chapter VII colour-weight synthesis. The darker-is-heavier and brighter-is-heavier accounts are contextual representations, not one universal law.

## Cross-Domain Connections

**Music → LOOSE**: Timbre (instrumental "colour") offers a qualitative comparison with hue, without a pitch/loudness-to-hue mapping or common weight scale.

Display colours need not correspond to a single wavelength. Differential cone sensitivity alone does not establish longer wavelengths as more activating or salient in every task.

# Examples

The following are reported examples from the existing extraction. Exact quotations, locators, experimental results and historical interpretation remain unassessed against the original; qualifying an example does not verify it.

**Example 1** (p. 19): "As to *color*, red is heavier than blue, and bright colors are heavier than dark ones." The clearest direct statement on hue weight.

**Example 2** (p. 19): "The patch of a bright red bedcover in Van Gogh's painting of his bedroom creates a strong off-center weight." This bedcover interpretation is reported, not a decomposition into measured hue and brightness weights.

**Example 3** (p. 20): The clown costume example: "A clown's costume — red on the left side, blue on the right — may be asymmetrical to the eye as a color scheme, even though the two halves of the costume, and indeed of the clown, are equal in physical weight." This clown example compares physical and compositional weight; exact experimental isolation is not established here.

# Relationships

## Builds Upon
- **Visual weight** — Colour elaborates the general compositional vocabulary.

## Enables
- **Colour hierarchy** — Possible task-led emphasis, not fixed warm/high-priority roles; no resolved local endpoint.
- **Visual balance** — Colour can inform comparisons alongside tone, area and placement, without mass arithmetic.

## Related
- **Tonal weight** — Appearance dimensions differ but interact; the represented accounts are contextual.
- **Visual balance** — Connects colour-bearing areas to compensation judgments.

## Contrasts With
- **Weight by size** — A conceptual comparison without a resolved endpoint: colour and area can influence emphasis differently, without a universal override law.

# Common Errors

- **Error**: Treating multiple saturated colours as proof of hierarchy failure.
  **Correction**: Inspect actual roles and competing emphasis. No red/orange > yellow > green > blue > violet ranking follows from the red/blue example.

- **Error**: Calling "I like how these colours look together" perceptual physics.
  **Correction**: Describe the task, identity and observed context; distinguish reported accounts from measured effects.

# Common Confusions

- **Confusion**: Colour weight = brightness, with hue supplying a separate additive correction.
  **Clarification**: Brightness, lightness, chroma and contrast are distinct and interacting. CIE lightness is relative to a similarly illuminated white; model coordinates and WCAG relative luminance are different. A maroon and a bright blue need actual surroundings and task context before an emphasis judgment.

# Source Reference

Chapter I: Balance, "Art and Visual Perception," pp. 18-20. The "Weight" section mentions colour within the broader enumeration of weight determinants.

# Verification Notes

The bullets below are frozen historical extraction notes, including their confidence and mapping labels; they are not current verification or independent acceptance. Current supported corrections distinguish analytic geometry/CSS from contextual perceptual reports; original-dependent fidelity remains unassessed.

- Definition source: Direct quotes from p. 19 ("red is heavier than blue"; "bright colors are heavier than dark ones"; clown costume example). Synthesised from the "Weight" section.
- Confidence rationale: Medium — Arnheim's statements on colour weight are brief and not systematically developed in this chapter. The extraction is reliable but the card synthesises more than Arnheim explicitly develops here.
- Uncertainties: Arnheim does not distinguish hue weight from saturation weight; both are implicit in his colour-weight claims. The separation into hue vs. saturation axes is an editorial elaboration justified by colour theory but not fully present in the source text.
- Cross-reference status: Generic slug; will harmonise with colour-weight concepts from colour theory sources.
- Rosetta Stone check: Music/timbre mapping identified as LOOSE. Mathematics/wavelength-salience mapping identified as LOOSE. No rigorous or structural mappings found for chromatic weight specifically.
- OCR issues: None significant.
