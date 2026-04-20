---
concept: Colour Picker (UI)
slug: colour-picker
category: interaction-design
subcategory: colour-controls
tier: intermediate
layer: 2-domain
source: "Okhsv and Okhsl"
source_slug: posts
authors: "Bj\u00f6rn Ottosson"
chapter: "What makes a good color picker?"
chapter_number: null
pdf_page: null
section: null
extraction_confidence: high
aliases:
  - ["color picker", "colour selector", "color wheel"]
prerequisites:
  - hsl
  - hsv
  - colour-gamut
extends:
  - []
related:
  - okhsl
  - okhsv
  - colour-picker-design-principles
contrasts_with:
  - []
answers_questions:
  - "What makes a colour picker perceptually well-designed?"
rosetta_stone: []
css_implementation:
  - property: "input[type=color]"
    example: "<input type=\"color\" value=\"#ff0000\">"
    support: baseline
---

# Quick Definition

A colour picker is a user interface control that allows a user to select a colour from a parameterised colour space, typically by navigating a two-dimensional field and one or more sliders.

# Core Definition

Colour pickers are described by Ottosson as a "common operation in many applications" that have "become fairly standardised," with "ubiquitous today" being "color pickers based on HSL and HSV." The design of a colour picker involves two separable concerns: the choice of the underlying colour space (which determines the mathematical parameterisation of colour) and the design of the UI widget used to navigate that space. Ottosson focuses primarily on the former: "The main focus here will be on the choice of color space, rather than the design of the UI widget used for navigating the color space." The most common widget form pairs a two-dimensional square or triangular field (representing two of the three parameters) with a linear slider (representing the third, usually hue).

# Prerequisites

- **HSL colour space** \u2014 The dominant colour space underlying most current pickers
- **HSV colour space** \u2014 The other dominant colour space underlying most current pickers
- **Colour gamut** \u2014 Pickers must confine selections to the target gamut

# Key Properties

1. The colour space choice determines whether adjusting one axis distorts others perceptually
2. A simple geometrical shape (cylinder or triangle) keeps all parameters adjustable without producing out-of-gamut colours
3. Maximum-chroma colours should be easily findable \u2014 ideally at the edge of the colour solid
4. The interface should vary smoothly and evenly so that equal UI movements produce equal perceived colour changes

# Construction / Recognition

## To Construct/Create:
1. Choose a colour space that maps the target gamut to a simple geometric shape
2. Map two dimensions to the two-dimensional field of the picker widget
3. Map the third dimension to a linear slider
4. Optionally expose numeric input fields for precise values

## To Identify/Recognise:
1. A colour picker typically shows a two-dimensional gradient field (hue \u00d7 saturation, or saturation \u00d7 value) with a separate hue strip
2. A crosshair or circle marks the selected colour within the field

# Context & Application

- **Typical contexts**: Graphic design software, web authoring tools, paint applications, CSS developer tools
- **Common applications**: Selecting brand colours, adjusting theme colours, picking accessible foreground/background combinations

# Examples

**Example 1** (from source): Ottosson describes the two most common pickers: an HSV picker (square field with saturation on X, value on Y, hue slider) and an HSL picker (triangular or square field, hue slider). Both are provided as the baseline against which Okhsl and Okhsv are compared.

**Example 2** (from source): Drasner mentions "There is a native browser color selector that you can employ to help your users select colors dynamically" using `<input type="color">`, a built-in HTML colour picker.

# Relationships

## Builds Upon
- **HSL / HSV** \u2014 Foundational colour spaces that nearly all common pickers use

## Enables
- **Okhsl / Okhsv** \u2014 Purpose-built to be drop-in improvements for HSL/HSV pickers

## Related
- **Colour picker design principles** \u2014 The 8-property framework Ottosson articulates for evaluating picker quality
- **NCS colour system** \u2014 An alternative pre-digital colour ordering system also used in picker UIs

## Contrasts With
- **Numeric colour input** \u2014 Raw numeric entry (hex, rgb()) lacks the affordance of spatial navigation

# Common Errors

- **Error**: Treating colour picker design as only a UI/widget problem.
  **Correction**: Ottosson argues the colour space choice is the more consequential decision; the same widget looks and behaves very differently depending on whether it uses HSL, Okhsl, or a Lab-like space.

# Common Confusions

- **Confusion**: A better colour picker just needs better UI design.
  **Clarification**: Ottosson notes that "despite color picking playing a big role in a lot of applications, the design of color pickers isn't a particularly well researched topic" and that the key unresolved question is the choice of colour space, not the widget design.

# Source Reference

"What makes a good color picker?" and "Color picking before computers," Okhsv and Okhsl (Bj\u00f6rn Ottosson).

# Verification Notes

- Definition source: Synthesised from Ottosson's framing; Drasner native input mention
- Confidence rationale: High \u2014 colour picker is the central topic of the Ottosson source
- Uncertainties: Drasner's article doesn't analyse picker design in depth
- Cross-reference status: Verified in both sources
- Rosetta Stone check: No mappings added
- OCR issues: None significant in relevant prose
