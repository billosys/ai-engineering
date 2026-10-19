---
concept: "Colour Weight"
slug: "colour-weight"
category: "design-principles"
subcategory: "visual-weight"
tier: "intermediate"
layer: "1-principles"
source: "Art and Visual Perception: A Psychology of the Creative Eye"
source_slug: "art-and-visual-perception"
authors: "Rudolf Arnheim"
chapter: "VII. Color"
chapter_number: 7
pdf_page: 371
section: "Reactions to Color"
extraction_confidence: "medium"
aliases:
  - "visual weight of colour"
  - "chromatic weight"
prerequisites:
  - "tonal-value"
  - "saturation"
  - "colour-temperature"
extends: []
related:
  - "tonal-contrast"
  - "colour-harmony"
  - "colour-temperature"
  - "simultaneous-contrast"
contrasts_with: []
answers_questions:
  - "What is visual hierarchy, and what visual properties (size, colour, contrast, weight, spacing) establish it?"
  - "A dark theme was implemented by swapping background and foreground colours, but the interface feels 'heavy' and fatiguing. What perceptual principle explains this, and what's the correct approach to dark theme design?"
rosetta_stone:
  -
    domain: "mathematics"
    concept: "Weighted summation / centre of gravity"
    rating: "structural"
    note: "Weighted summation is a qualitative comparison, not calibrated colour mass; no required centred sum or universal dark-heavy law follows."
css_implementation:
  -
    property: "color (OKLCH candidate)"
    example: "color: oklch(0.2 0.15 270); /* example coordinate; not mass, luminance ratio or a required dark theme */"
    support: "baseline"
---

# Quick Definition

Colour weight is a compositional description of a colour-bearing area’s apparent influence. The Chapter VII synthesis calls darker colours heavier; the Chapter I tonal/weight accounts instead report brighter colours as heavier. Their contexts remain distinct, without a universal winner or mass scale.

# Core Definition

This is the represented Arnheim account. Its quotations, page/figure references and historical, experimental or neural claims have not been checked against the unavailable original. The analytic qualifications below do not certify source fidelity.

Colour weight describes the visual "heaviness" or pull of a colour — its capacity to attract attention and exert visual force within a composition. Arnheim discusses this in the context of bodily and perceptual responses to colour, drawing on Goldstein's neurological observations and Kandinsky's spatial descriptions.

The prior Chapter VII synthesis linked darkness, saturation and temperature to weight. That synthesis differs from Chapter I’s brighter-is-heavier account. These are contextual represented accounts, not independently additive variables or a calibrated centre-of-gravity calculation.

Arnheim reports Fere’s (Féré’s) physiological findings — muscular power and blood circulation increase in the sequence from blue through green, yellow, orange, and red — and Goldstein’s reported neurological observation contrasting expansive and constricting responses to warm and cool colours. Display colours need not have a single wavelength, and these reports do not establish a universal present clinical effect. Kandinsky’s spatial description — yellow spreads outward, blue contracts inward — is another reported account, not a verified physiological correlate.

A small coloured area may be influential within a particular composition; darkness, warmth or saturation alone cannot establish its weight or balance.

Note: These are historical accounts represented by the extraction. Replication, failed replication and comparative reliability of Fere’s and Goldstein’s findings were not verified in this review; no present neurological conclusion follows.

# Prerequisites

- **Tonal value** — Supplies a light-dark appearance distinction, not an absolute mass proxy.
- **Saturation** — Supplies a vividness comparison; broader neighboring causal claims are not adopted.
- **Colour temperature** — Supplies a contextual warm/cool description, not a semantic role or wavelength-weight law.

# Key Properties

1. **Darkness**: The darker-is-heavier synthesis is distinct from Chapter I’s brighter-is-heavier account; neither is universal here.
2. **Saturation**: Vividness can matter in context without a universal energy scale.
3. **Temperature**: Warm/cool descriptions do not prove advance or weight for every display colour.
4. **Area**: Physical extent, apparent area and compositional influence differ.
5. **Composition**: Actual arrangement, content and surround need inspection before an influence judgment.

# Construction / Recognition

## To Construct/Create:
1. Preserve supplied identity, theme roles, text and geometry as the starting context.
2. Enumerate actual surfaces and text/control/state pairs; resolve alpha, overlays and filters.
3. Compare hierarchy and grouping for the task, using non-colour signals where needed.
4. Review dark themes with actual states, viewing conditions and preferences. Inversion or a black background alone does not diagnose fatigue or heaviness.

## To Identify/Recognise:
1. Describe the region previously characterised by "sinks" or "pulls" in a particular viewing context, without deriving a mass value.
2. Squinting can reduce detail for a comparison; it is not complete colour or accessibility proof.

# Context & Application

- **Typical contexts**: Interface composition, dark themes, data visualisation and print.
- **Common applications**: Compare CTA and text emphasis, or saturated accents and surrounding fields. A large dark surface is not inherently oppressive. A dark-theme complaint calls for actual pair/state, typography, geometry, viewing-condition and preference review; no fatigue or usability result is measured by this card.

## Cross-Domain Connections

**Mathematics → STRUCTURAL**: Weighted summation provides a qualitative comparison only. A physical centre of mass requires specified masses and coordinates; no calibrated colour mass or required centred visual sum is supplied. WCAG relative luminance and Oklab L are not mass.

# Examples

The following are reported examples from the existing extraction. Exact quotations, locators, experimental results and historical interpretation remain unassessed against the original; qualifying an example does not verify it.

**Example 1** (p. 392): Fere's experiments — muscular power and blood circulation increase from blue through green, yellow, orange, to red. This is a reported physiological account, not a verified direct bodily weight of display hues.

**Example 2** (p. 392–393): Goldstein's neurological findings — patients' postural balance was disrupted by red (high weight/expansion) but stabilised by green (low weight/contraction), as reported by Arnheim; neither replication nor comparative clinical reliability is established here.

**Example 3** (p. 393): Kandinsky's spatial descriptions — yellow "spreads outward from the center which almost markedly approaches the spectator"; blue "moves away from the spectator." This is a reported spatial description, not a proven advancing-equals-heavier law.

**Example 4** (p. 393): Albers' colour circle — "the realms of cold and warm coincide roughly with those of dark and bright, and Itten associates cold with shady, warm with sunny." The Albers/Itten comparison is reported; it does not establish a universal hue, brightness or weight correlation.

# Relationships

## Builds Upon
- **Tonal value, saturation, colour temperature** — Supply distinct appearance descriptions for comparison; no additive independence or causal law is assumed.

## Enables
- **Compositional balance** — Colour-bearing areas can inform a compensation judgment; conceptual use, not a resolved local endpoint.
- **Visual hierarchy** — Colour can support task-led emphasis without guaranteed first attention; conceptual use, not a resolved local endpoint.

## Related
- **Tonal contrast** — Connects a colour-bearing area to its actual surround and pair requirements.
- **Colour temperature** — Connects contextual warmth/coolness to the represented account, not a universal weight mechanism.

## Contrasts With
- **Visual lightness** — A conceptual comparison without a resolved endpoint; lightness is an appearance attribute, not the literal opposite of compositional weight.

# Common Errors

- **Error**: Inferring weight from area alone or darkness alone.
  **Correction**: Compare the actual composition and intended role; a small accent can matter without a portable mass formula.

- **Error**: Prescribing dark-but-not-black surfaces or OKLCH L 0.12–0.15 for every dark theme.
  **Correction**: Preserve supplied identity and roles, resolve actual state pairs, and consider viewing conditions and preferences. Candidate values are examples; black backgrounds are not categorically forbidden and inversion alone proves no fatigue.

# Common Confusions

- **Confusion**: "More colour = more weight."
  **Clarification**: Area, vividness, meaning and surround interact. No scalar intensity/area rule establishes which region dominates.

- **Confusion**: "Colour weight is the same as tonal value."
  **Clarification**: Tonal value describes light-dark appearance; CIE lightness is brightness relative to a similarly illuminated white. Chroma and temperature are distinct descriptions, while WCAG relative luminance and Oklab L are model-specific quantities. None is physical mass.

# Source Reference

Chapter VII: Color, "Art and Visual Perception," pp. 391–395 (sections "Reactions to Color," "Warm and Cold").

# Verification Notes

The bullets below are frozen historical extraction notes, including their confidence and mapping labels; they are not current verification or independent acceptance. Current supported corrections distinguish analytic geometry/CSS from contextual perceptual reports; original-dependent fidelity remains unassessed.

- Definition source: Synthesised from "Reactions to Color" and "Warm and Cold" sections. Arnheim does not use the term "colour weight" explicitly but constructs the concept through physiological (Fere, Goldstein) and perceptual (Kandinsky) observations.
- Confidence rationale: Medium — the concept is clearly constructed by Arnheim from converging evidence, but the term "colour weight" is a synthesis; Arnheim uses "weight" in the context of composition generally but applies it implicitly to colour through the warmth/advance connection.
- Uncertainties: Fere's physiological measurements have not been robustly replicated; Arnheim treats them as preliminary evidence. Goldstein's neurological observations are more reliable.
- Cross-reference status: Verified — colour weight as a design concept is widely applied in practice; Arnheim's account provides a perceptual/physiological grounding.
- Rosetta Stone check: Mapping added (mathematics: centre of gravity / weighted sum, structural).
- OCR issues: None detected.
