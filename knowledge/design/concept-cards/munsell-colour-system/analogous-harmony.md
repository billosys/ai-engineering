---
concept: "Analogous Harmony"
slug: "analogous-harmony"
category: "colour-theory"
subcategory: "colour-harmony"
tier: "intermediate"
layer: "2-domain"
source: "A Practical Description of The Munsell Color System"
source_slug: "munsell-colour-system"
authors: "T. M. Cleland"
chapter: "Color Combinations"
chapter_number: 9
pdf_page: 15
section: null
extraction_confidence: "high"
aliases:
  - "neighbouring hue harmony"
  - "analogous colour scheme"
  - "adjacent hue harmony"
prerequisites:
  - "hue"
  - "munsell-hue-circle"
extends: []
related:
  - "monochromatic-harmony"
  - "complementary-harmony"
  - "colour-harmony-as-order"
contrasts_with:
  - "complementary-harmony"
answers_questions:
  - "CQ 23: How do you construct a colour palette starting from a single brand colour using OKLCH?"
rosetta_stone: []
css_implementation:
  -
    property: "oklch() hue offset"
    example: "/* Analogous palette: base hue ± 30-36 degrees */\n--base: oklch(0.6 0.15 240);\n--warm: oklch(0.6 0.12 210);\n--cool: oklch(0.6 0.12 270);"
    support: "baseline"
---

# Quick Definition

This named colour-selection strategy uses neighbouring hue positions. “Harmony” names a historical design preference, not an assured result of the selection rule.

# Core Definition

The earlier extraction attributes the following wording to Cleland; the book and prepared text are unavailable, so quotations, locators, context and historical attribution remain unverified.

Retained reported wording: "neighboring Hues, that is of any Hue with the Hue which immediately precedes or follows it on the scale — Green with Green-Yellow, Red with Yellow-Red, Yellow with Yellow-Red, etc." "In all of these cases the harmony depends upon proximity rather than contrast, as in the case of opposites" "These may in turn be varied by taking them at different steps of Value and different strengths of Chroma" "In the same way, Hues may be combined with neighboring intermediate Hues"

Neighbouring hues define the reported method. No universal family-count or arc-width threshold is established. Hue proximity does not guarantee harmony, and value/chroma/gamut and actual pair/state use remain separate.

# Prerequisites

- **Hue** — Supplies the relevant H/V/C or diagram vocabulary for this card; this is an understanding route, not a claim of physical or historical derivation.
- **Munsell Hue Circle** — Supplies the relevant H/V/C or diagram vocabulary for this card; this is an understanding route, not a claim of physical or historical derivation.

# Key Properties

1. The defining selection is neighbouring hue positions; identify the diagram/model in use.
2. Value/chroma variation can create candidates, within the available gamut and reference conditions.
3. Recorded claims of sure or infallible harmony are attributed advice, not established guarantees.
4. No necessary hue-count, three-step threshold or universal area recipe follows.
5. Actual coherence, hierarchy, legibility and accessibility depend on the roles, content, viewing conditions and complete rendered pairs.

# Construction / Recognition

## To Construct/Create:

1. Start with the brief, supplied brand colour/tokens and actual interface roles; preserve their semantics.
2. Explore neighbouring hue positions in the named model. The recorded Munsell examples are not CSS conversions.
3. For CSS, choose explicit OKLCH candidate values; any fixed hue or ±angle choice is optional, not a mandatory palette.
4. Check destination gamut and rendering, then actual foreground/background pairs and relevant states; adjust for the task.
5. If demonstrating the historical area equation, state its positive-domain approximation separately. It supplies no general neutral-background or harmony rule.

## To Identify/Recognise:

1. Identify the selection relation (neighbouring hue positions) rather than judging by a vague impression of harmony.
2. Distinguish family proximity from exact coordinate identity; decide which the exercise requires.
3. Check the resulting candidates in their actual task instead of inferring quality from their scheme name.

# Context & Application

For CQ23, begin with the supplied brand value and task, map needed roles, propose optional candidates in an explicit CSS model, inspect gamut/rendering, and check complete pairs and states. No Munsell hue-only conversion or automatic accessible palette is supplied. Scheme names can organize exploration; they do not determine a universal hue/family count.

# Examples

Recorded extraction examples below retain their reported locators; they were not checked against the missing book. Any balance or harmony result is historical advice or conditional arithmetic, not an independently observed mixing or aesthetic result.

**Example 1** (p. 15): "Neighboring Hues — Green with Green-Yellow, Red with Yellow-Red, Yellow with Yellow-Red."

**Example 2** (p. 15): "These may in turn be varied by taking them at different steps of Value and different strengths of Chroma."

# Relationships

## Builds Upon

- **Hue** — The method selects neighbouring hue positions, not a required number of colours.
- **Munsell Hue Circle** — The named circle supplies the adjacency relation, not a universal appearance threshold.

## Enables

- **Colour Harmony as Order** — A short arc can illustrate a selection rule; the path alone proves no harmony.

## Related

- **Monochromatic Harmony** — One-hue selection is a narrower constraint; adjacency remains a separate strategy.

## Contrasts With

- **Complementary Harmony** — Neighbouring versus opposed hue selections is the contrast, not minimum/maximum perceptual contrast.

# Common Errors

- **Error**: Treating the named method as a guarantee or a mandatory palette recipe.
  **Correction**: Use it as a candidate strategy, retaining the brief, supplied values, gamut and actual pair/state checks.
- **Error**: Treating the balance model as a requirement for every scheme.
  **Correction**: If adopted for an exercise, require positive C,V and distinguish its conditional arithmetic from aesthetic judgment.

# Common Confusions

- **Confusion**: “Neighbouring” imposes exactly 2–3 families or a safe arc width.
  **Clarification**: The recorded account says immediately preceding/following hues, without establishing a universal numerical threshold.
- **Confusion**: Hue proximity guarantees harmony.
  **Clarification**: It is the reported strategy, not a perceptual law. Value/chroma choices, gamut, role distinctions and pair/state checks remain necessary.

# Source Reference

Chapter 9: Color Combinations, p. 15.

# Verification Notes

- This revision reviewed the complete available card body and local relationships/CQ components; it did not inspect the missing original book, prepared Cleland text or diagrams. All historical quotations, dates, page claims, named attributions and source-specific efficacy claims remain unassessed for fidelity.
- Extraction-confidence metadata is preserved from the predecessor. Earlier “exact quote,” “verified planned cards” and “0010 checked” notes described historical extraction/navigation observations, not current independent semantic proof.
- Current technical qualifications use the [RIT renotation overview](https://www.rit.edu/science/munsell-color-science-lab-educational-resources#munsell-renotation-data), [CIE appearance terminology](https://cie.co.at/eilvterm/17-22-067) and [CSS Color4](https://www.w3.org/TR/2026/CRD-css-color-4-20261009/), with elementary conditional algebra where stated. These do not establish historical-source fidelity, exact perceptual equality, physical neutralisation or aesthetic guarantees.
- CSS metadata/body examples are model-specific illustrations, not Munsell conversions, checked contrast pairs or mandatory project palettes. No browser, assistive-technology, disc/material experiment or hosted rendering result was produced.
