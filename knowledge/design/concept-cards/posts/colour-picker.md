---
concept: "Colour Picker (UI)"
slug: "colour-picker"
category: "interaction-design"
subcategory: "colour-controls"
tier: "intermediate"
layer: "2-domain"
source: "Okhsv and Okhsl"
source_slug: "posts"
authors: "Björn Ottosson"
chapter: "What makes a good color picker?"
chapter_number: null
pdf_page: null
section: null
extraction_confidence: "high"
aliases:
  -
    - "color picker"
    - "colour selector"
    - "color wheel"
prerequisites:
  - "hsl"
  - "hsv"
  - "colour-gamut"
extends: []
related:
  - "okhsl"
  - "okhsv"
  - "colour-picker-design-principles"
contrasts_with: []
answers_questions:
  - "What makes a colour picker perceptually well-designed?"
rosetta_stone: []
css_implementation: []
---

# Quick Definition


A colour picker is an interface for choosing or entering a colour. Its controls, parameterization, output format and host behavior are design choices; the mathematical model and widget are related but separable.

# Core Definition


Ottosson discusses colour-space choice for picker design and explicitly says the article focuses on the space rather than widget design. That framing scopes the article; it does not establish that widget design, accessibility or interaction is unimportant. The article compares eight proposed goals and the tradeoffs of HSL, HSV, Okhsl and Okhsv, with subjective judgements scoped to sRGB. A picker may use a field, sliders, numeric entry, or other controls; its output and target gamut should be stated. HTML `<input type="color" value="#ff0000">` is an illustrative HTML example, not markup recovered verbatim from Drasner and not evidence that the native control uses HSV or Okhsl. The HTML standard defines a color well/value and says the `colorspace` attribute hints at a desired UI; appearance remains user-agent/host dependent.

# Prerequisites


- **HSL / HSV** — Their encoded-RGB coordinates are examples used in picker controls; their values and tradeoffs are distinct.
- **Colour gamut** — A picker decision should name the destination and account for representability; it need not constrain every intermediate selection to a gamut.

# Key Properties


1. Space, control layout, keyboard/accessibility behavior, value format and target gamut are separate decisions that must be considered together for a real interface.
2. The article proposes eight sometimes-conflicting goals; its ratings are the author’s subjective sRGB comparison, not universal proof.
3. A convenient parameter shape does not guarantee equal perceived changes or accessible interaction.
4. Output checks should cover the specified destination and actual rendered colour pairs where the picker feeds an interface.

# Construction / Recognition

## To Construct/Create:

1. State the task, destination gamut/format and whether users need to locate vivid colours, adjust lightness, enter exact values, or combine these tasks.
2. Compare candidate spaces and controls against the relevant tradeoffs in the source; do not promise a universal drop-in replacement or numeric interchangeability.
3. Choose the widget and interaction separately for the host, users and accessibility requirements.
4. Check resulting values and rendered pairs in the actual destination; this card does not prescribe a new widget.

## To Identify/Recognise:

1. Identify the space/formulas and output encoding independently from a widget’s appearance.
2. Treat an HTML color input as a host-defined control whose standardized value is a serialized CSS color; do not infer its internal selection geometry from the markup.
3. A field-plus-slider is one possible interface, not a necessary property of a colour picker.

# Context & Application

- **Typical contexts**: Graphic design software, web authoring tools, paint applications, CSS developer tools
- **Common applications**: Selecting brand colours, adjusting theme colours, generating candidate foreground/background colours for later contrast and rendering checks

# Examples


**Example 1** (from source): Ottosson compares HSL, HSV, Okhsl and Okhsv against eight named goals. The judgments are subjective, scoped to sRGB and attributed to the author; the figures were not independently inspected.

**Example 2** (illustrative HTML, not a recovered Drasner quote): `<input type="color" value="#ff0000">` demonstrates a native color-well element. It does not show how a particular host draws the picker or which internal model it uses.

# Relationships

## Builds Upon

- **HSL / HSV** — These are examples of models used to parameterize picker controls; the article does not establish that nearly all current pickers use them.

## Enables

- **Okhsl / Okhsv** — The article proposes these as alternative picker coordinate models; no universal drop-in or accessibility result follows.

## Related

- **Colour picker design principles** — The article’s eight proposed criteria provide one comparison vocabulary.
- **NCS colour system** — The article describes an NCS app example; the system and the widget are distinct.

## Contrasts With

- **Numeric colour input** — Direct entry and spatial controls offer different interaction affordances; neither is universally preferable.

# Common Errors


**Error**: Assuming picker design is only widget design, or only colour-space choice.
  **Correction**: The article concentrates on space choice; deployed interactions also need task, control, accessibility, host and output review.

**Error**: Treating an HTML color input as a specific HSV/Okhsl implementation.
  **Correction**: HTML defines a color well and serialized value, with UI details left to the host; inspect the target host when behavior matters.

# Common Confusions


**Confusion**: A better picker can be identified from a model name alone.
  **Clarification**: The article’s model tradeoffs are useful evidence, not a universal ranking. Widget behavior and actual user tasks require their own review.

# Source Reference

"What makes a good color picker?" and "Color picking before computers," Okhsv and Okhsl (Björn Ottosson).

# Verification Notes


This full available-evidence review checked the picker framing against the prepared article, the Drasner HSL/native-control passages and the HTML Living Standard Color state. The input example is illustrative HTML, not recovered literal markup; the standard specifies a serialized CSS-color value and leaves selection UI host-dependent. No browser or accessibility behavior was tested. The article’s figures were not independently inspected; capture fidelity remains unverified. Extraction-confidence metadata is unchanged.
