---
concept: "Natural Colour System (NCS)"
slug: "natural-colour-system"
category: "colour-theory"
subcategory: "colour-ordering-systems"
tier: "intermediate"
layer: "2-domain"
source: "Okhsv and Okhsl"
source_slug: "posts"
authors: "Björn Ottosson"
chapter: "Color picking before computers"
chapter_number: null
pdf_page: null
section: null
extraction_confidence: "medium"
aliases:
  -
    - "NCS"
    - "NCS color system"
prerequisites: []
extends: []
related:
  - "munsell-colour-system"
  - "colour-picker-design-principles"
  - "hsv"
contrasts_with:
  - "munsell-colour-system"
  - "hsl"
  - "hsv"
answers_questions:
  - "What makes a colour picker perceptually well-designed?"
rosetta_stone: []
css_implementation: []
---

# Quick Definition


The Natural Colour System (NCS) describes perceived surface colours using resemblance to elementary colours and a notation for hue and nuance. It is not an RGB primary system or identical to a finite swatch set or display gamut.

# Core Definition


Ottosson summarizes NCS as using resemblance to white, black, yellow, red, green and blue and a hue-specific colour triangle. NCS’s official explanation also describes its elementary colours, hue circle, nuance triangle and notation. In NCS S 1050-Y90R, 1050 gives 10% blackness and 50% chromaticness (so 40% whiteness in the three-part nuance); Y90R describes yellow with hue toward red. These notation coordinates do not themselves specify screen RGB. A defensible screen match needs a specified physical sample/edition or measurement and an identified conversion/output condition. It is not true that every conversion always requires one particular mapping table.

# Prerequisites

- None — NCS is a foundational colour description system

# Key Properties


1. The six NCS elementary colours are perceptual references, not RGB primaries.
2. NCS notation expresses hue and nuance; for the three-part nuance, whiteness, blackness and chromaticness sum to 100%.
3. The official NCS explanation describes a hue circle and a hue-specific nuance triangle; its system is distinct from a display RGB gamut and an individual physical swatch.
4. The article’s NCS/HSV/HWB similarities are structural comparisons, not equivalence or universal conversion rules.

# Construction / Recognition

## To Identify/Recognise:

1. In NCS S 1050-Y90R, 10 is blackness, 50 chromaticness and the remaining 40 whiteness; Y90R places the hue 90% from yellow toward red.
2. Do not interpret the hue suffix as RGB channel mixing or the code as screen RGB.
3. A pictured triangle is an attributed description, not evidence of a particular picker UI.

# Context & Application

- **Typical contexts**: Architectural colour specification, paint and coatings industry (Scandinavian markets especially), interior design
- **Common applications**: Specifying wall paint colours, surface material specifications, design standards in Scandinavian countries

# Examples


**Example 1** (notation): NCS S 1050-Y90R expresses the stated nuance and hue; it is not a screen RGB value.

**Example 2** (source comparison): Ottosson’s table gives NCS an author-assessed profile against picker goals. The judgment is attributed and sRGB-contextual; the app figure was not independently inspected.

# Relationships

## Builds Upon

- **Perceptual colour research** — Ottosson and the NCS explanation describe the system through perceived resemblance; detailed standardization is beyond this bounded review.

## Related

- **Munsell colour system** — Both order colour, with different descriptive constructions in the inspected source.
- **HWB colour model** — Ottosson notes a structural resemblance; HWB is an RGB re-parameterization, not NCS.

## Contrasts With

- **Munsell colour system** — HVC notation and NCS elementary-colour resemblance are distinct.
- **HSV / HWB** — RGB parameter transformations differ from NCS notation and its sample/system context.

# Common Errors


**Error**: Treating NCS as equivalent to sRGB/HSV, or saying every conversion needs a mapping table.
  **Correction**: NCS notation, a physical sample and a display colour are different things. A defensible match needs a specified sample/measurement, conversion method and destination; the exact path depends on available data.

**Error**: Treating NCS elementary colours as additive RGB primaries.
  **Correction**: They are the system’s perceptual references.

# Common Confusions


**Confusion**: NCS and Munsell share an underlying model.
  **Clarification**: The source describes their constructions differently: NCS uses resemblance to elementary colours, while Munsell uses HVC coordinates. This bounded comparison does not establish all technical differences or uniformity.

# Source Reference

"Color picking before computers" and comparison table, Okhsv and Okhsl (Björn Ottosson).

# Verification Notes


This full available-evidence review checked the article’s bounded comparison against the prepared picker text and NCS notation/elementary-colour explanations against the official NCS System page (accessed 2026-10-17). NCS S 1050-Y90R is a notation interpretation, not a screen measurement or converted RGB witness. The article’s app figure was not inspected. Full standard/sample conversion details, original capture fidelity, browser behavior and accessibility were not assessed; extraction-confidence metadata is unchanged.
