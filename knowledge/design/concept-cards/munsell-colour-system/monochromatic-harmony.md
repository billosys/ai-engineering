---
concept: "Monochromatic Harmony"
slug: "monochromatic-harmony"
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
  - "single-hue harmony"
  - "monochromatic colour scheme"
  - "monochromatic palette"
prerequisites:
  - "hue"
  - "colour-value"
  - "chroma"
extends: []
related:
  - "analogous-harmony"
  - "complementary-harmony"
  - "colour-harmony-as-order"
contrasts_with:
  - "complementary-harmony"
answers_questions:
  - "CQ 23: How do you construct a colour palette starting from a single brand colour using OKLCH?"
rosetta_stone:
  -
    domain: "music"
    concept: "Variation within a single key/mode"
    rating: "loose"
    note: "Keeping one hue while varying other colour coordinates can be loosely compared with variation under a musical constraint. Value is not loudness, chroma is not articulation, and the comparison proves no shared mechanism or aesthetic guarantee."
css_implementation:
  -
    property: "oklch() value/chroma variation"
    example: "/* Monochromatic palette from a single hue */\n--base: oklch(0.5 0.15 240);\n--light: oklch(0.8 0.08 240);\n--dark: oklch(0.3 0.12 240);"
    support: "baseline"
---

# Quick Definition

This named colour-selection strategy uses one hue while varying value and/or chroma. “Harmony” names a historical design preference, not an assured result of the selection rule.

# Core Definition

The earlier extraction attributes the following wording to Cleland; the book and prepared text are unavailable, so quotations, locators, context and historical attribution remain unverified.

Retained reported wording: "another very simple and practically infallible series of color harmonies... made within a single Hue" "a low Value of any Hue with a high Value of the same" "a weak Chroma of any Hue with a stronger Chroma of the same" "a low Value and weak Chroma with a high Value and stronger Chroma or vice versa" "Experiments with the possibilities of single Hues will yield very interesting results in the great variety of colors thus obtainable"

The reported variants hold hue while changing value, chroma or both. These offer useful candidate strategies; “practically infallible” is an unverified attributed judgment, not an established guarantee. Changing chroma is radial, so a fixed-hue V/C path is not only vertical.

# Prerequisites

- **Hue** — Supplies the relevant H/V/C or diagram vocabulary for this card; this is an understanding route, not a claim of physical or historical derivation.
- **Colour Value** — Supplies the relevant H/V/C or diagram vocabulary for this card; this is an understanding route, not a claim of physical or historical derivation.
- **Chroma** — Supplies the relevant H/V/C or diagram vocabulary for this card; this is an understanding route, not a claim of physical or historical derivation.

# Key Properties

1. The defining selection is one hue while varying value and/or chroma; identify the diagram/model in use.
2. Value/chroma variation can create candidates, within the available gamut and reference conditions.
3. Recorded claims of sure or infallible harmony are attributed advice, not established guarantees.
4. No necessary hue-count, three-step threshold or universal area recipe follows.
5. Actual coherence, hierarchy, legibility and accessibility depend on the roles, content, viewing conditions and complete rendered pairs.

# Construction / Recognition

## To Construct/Create:

1. Start with the brief, supplied brand colour/tokens and actual interface roles; preserve their semantics.
2. Explore one hue while varying value and/or chroma in the named model. The recorded Munsell examples are not CSS conversions.
3. For CSS, choose explicit OKLCH candidate values; any fixed hue or ±angle choice is optional, not a mandatory palette.
4. Check destination gamut and rendering, then actual foreground/background pairs and relevant states; adjust for the task.
5. If demonstrating the historical area equation, state its positive-domain approximation separately. It supplies no general neutral-background or harmony rule.

## To Identify/Recognise:

1. Identify the selection relation (one hue while varying value and/or chroma) rather than judging by a vague impression of harmony.
2. Distinguish family proximity from exact coordinate identity; decide which the exercise requires.
3. Check the resulting candidates in their actual task instead of inferring quality from their scheme name.

# Context & Application

For CQ23, begin with the supplied brand value and task, map needed roles, propose optional candidates in an explicit CSS model, inspect gamut/rendering, and check complete pairs and states. No Munsell hue-only conversion or automatic accessible palette is supplied. Scheme names can organize exploration; they do not determine a universal hue/family count.

## Cross-Domain Connections

**Music → Loose**: Keeping one hue can evoke variation under a musical constraint. It does not equate hue with key, value with dynamics or chroma with articulation. In the diagram, changing V is vertical and changing C is radial; fixed hue with both changes is not merely a vertical path.

# Examples

Recorded extraction examples below retain their reported locators; they were not checked against the missing book. Any balance or harmony result is historical advice or conditional arithmetic, not an independently observed mixing or aesthetic result.

**Example 1** (p. 15): Value contrast — "a low Value of any Hue with a high Value of the same" — e.g., dark blue with light blue.

**Example 2** (p. 15): Chroma contrast — "a weak Chroma of any Hue with a stronger Chroma of the same" — e.g., grayish blue with vivid blue.

**Example 3** (p. 15): Combined — "a low Value and weak Chroma with a high Value and stronger Chroma" — e.g., dark muted blue with light vivid blue.

# Relationships

## Builds Upon

- **Hue**, **Colour Value**, **Chroma** — The method fixes hue while V and/or C change; realizability remains reference/gamut dependent.

## Enables

- **Colour Harmony as Order** — Fixed hue with changing V/C moves vertically and radially, not only along a vertical line.

## Related

- **Analogous Harmony** — Allowing neighbouring hues relaxes the one-hue constraint; no harmony theorem follows.
- **Colour Balance** — The historical area approximation is optional and does not extend into a physical monochromatic mixing law.

## Contrasts With

- **Complementary Harmony** — One-hue versus opposed-hue selection distinguishes strategies, not guaranteed contrast or pleasure.

# Common Errors

- **Error**: Treating the named method as a guarantee or a mandatory palette recipe.
  **Correction**: Use it as a candidate strategy, retaining the brief, supplied values, gamut and actual pair/state checks.
- **Error**: Treating the balance model as a requirement for every scheme.
  **Correction**: If adopted for an exercise, require positive C,V and distinguish its conditional arithmetic from aesthetic judgment.

# Common Confusions

- **Confusion**: A method called “harmony” is always harmonious or accessible.
  **Clarification**: That historical label cannot establish either outcome; assess the actual use.
- **Confusion**: Scheme membership determines precise colour conversion or contrast.
  **Clarification**: Models differ; hue alone leaves V/C and conversion conditions unknown. Check the rendered pair.

# Source Reference

Chapter 9: Color Combinations, p. 15.

# Verification Notes

- This revision reviewed the complete available card body and local relationships/CQ components; it did not inspect the missing original book, prepared Cleland text or diagrams. All historical quotations, dates, page claims, named attributions and source-specific efficacy claims remain unassessed for fidelity.
- Extraction-confidence metadata is preserved from the predecessor. Earlier “exact quote,” “verified planned cards” and “0010 checked” notes described historical extraction/navigation observations, not current independent semantic proof.
- Current technical qualifications use the [RIT renotation overview](https://www.rit.edu/science/munsell-color-science-lab-educational-resources#munsell-renotation-data), [CIE appearance terminology](https://cie.co.at/eilvterm/17-22-067) and [CSS Color4](https://www.w3.org/TR/2026/CRD-css-color-4-20261009/), with elementary conditional algebra where stated. These do not establish historical-source fidelity, exact perceptual equality, physical neutralisation or aesthetic guarantees.
- CSS metadata/body examples are model-specific illustrations, not Munsell conversions, checked contrast pairs or mandatory project palettes. No browser, assistive-technology, disc/material experiment or hosted rendering result was produced.
