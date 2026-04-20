---
# === CORE IDENTIFICATION ===
concept: Colour Temperature
slug: colour-temperature

# === CLASSIFICATION ===
category: colour-theory
subcategory: colour-properties
tier: intermediate
layer: 2-domain

# === PROVENANCE ===
source: "Art and Visual Perception: A Psychology of the Creative Eye"
source_slug: art-and-visual-perception
authors: "Rudolf Arnheim"
chapter: "VII. Color"
chapter_number: 7
pdf_page: 371
section: "Warm and Cold"

# === CONFIDENCE ===
extraction_confidence: medium

# === VARIANTS ===
aliases:
  - warm/cool colour
  - warm and cold (Arnheim's terms)
  - chromatic temperature

# === TYPED RELATIONSHIPS ===
prerequisites:
  - hue
  - saturation
extends: []
related:
  - hue
  - saturation
  - colour-harmony
  - complementary-colours
  - colour-weight
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do you construct a colour palette starting from a single brand colour using OKLCH? What systematic steps ensure adequate contrast and accessible combinations?"
  - "How does temperament problem in music theory map to perceptual uniformity problem in colour science?"

# === VISUAL DESIGN EXTENSIONS ===
rosetta_stone:
  - domain: engineering
    concept: "Colour temperature in Kelvin (blackbody radiation)"
    rating: structural
    note: "Physical colour temperature (Kelvin) describes the chromaticity of blackbody radiation: lower K = warmer (reddish), higher K = cooler (bluish) — the same warm/cool vocabulary applies to physical and perceptual colour temperature, though the mechanisms differ."

css_implementation:
  - property: "hue angle (oklch)"
    example: "/* Warm: H ≈ 0–60° (reds, oranges, yellows); Cool: H ≈ 180–270° (greens, blues) */"
    support: baseline
  - property: "filter: hue-rotate() for temperature shift"
    example: "filter: hue-rotate(-20deg); /* shifts toward warm (red) */"
    support: baseline
---

# Quick Definition

Colour temperature is the perceptual quality of colours as warm (typically reds, oranges, yellows) or cool (typically blues, greens, violets), determined primarily by the direction of a colour's deviation toward red (warming) or blue (cooling).

# Core Definition

Colour temperature describes the perceived warmth or coolness of a colour — a quality that correlates with but is not simply determined by hue membership. Arnheim offers an analysis that distinguishes it from simple hue category: "My suggestion is that not the main color but the color toward which it deviates may determine the effect... a reddish blue looks warm whereas a bluish red looks cold" (Chapter VII, p. 394).

This is Arnheim's distinctive contribution to colour temperature theory: it is not the dominant hue but the admixture direction — the "leaning" of the colour — that determines its temperature quality. A red with a blue tinge reads cold; a blue with a red tinge reads warm. This produces counterintuitive results: reddish blue (warm) vs. bluish red (cold), reddish yellow (warm) vs. bluish yellow (cold).

Arnheim also notes that Itten designated complementary pair red-orange ↔ blue-green as the temperature poles, supporting the idea that red admixture warms and blue admixture chills. He connects colour temperature to broader expressive qualities: warm colours invite and feel outgoing; cool colours feel withdrawn and distant. This connects to Kandinsky's observations about yellow spreading outward and blue contracting inward.

Note: Arnheim explicitly states his account has not been systematically tested and may be wrong; the card preserves this uncertainty while extracting the principle.

# Prerequisites

- **Hue** — Temperature is a quality of how a hue deviates toward other hues.
- **Saturation** — Temperature is more pronounced at higher saturation; low-saturation (grey) colours are relatively temperature-neutral.

# Key Properties

1. **Admixture-determined** — Per Arnheim, it is the colour toward which a hue deviates (the admixture), not the main hue, that primarily determines temperature.
2. **Reddish = warm, bluish = cool** — Red admixture warms any colour; blue admixture cools it.
3. **Pure primaries are ambiguous** — Pure red, blue, or yellow cannot be clearly called warm or cold; temperature quality appears in mixtures and deviations.
4. **Expressive** — Warm colours are outgoing, inviting, advancing; cool colours are receding, withdrawing, distancing.
5. **Spatial depth effect** — Warm colours tend to advance (appear closer); cool colours tend to recede. This is used in depth composition.

# Construction / Recognition

## To Construct/Create:
1. Evaluate a colour by asking: toward which direction does it deviate? If toward red → warmer; if toward blue → cooler.
2. Use colour temperature deliberately: warm foreground elements against cool backgrounds create depth and advance foreground.
3. For consistent palette temperature: ensure accent colours are in the same temperature range as the dominant unless deliberate temperature contrast is intended.
4. In OKLCH: H angles near 0°–60° (reds, oranges) and 60°–90° (yellows) are typically warm; H angles near 180°–270° (greens, blues, blue-violets) are typically cool.

## To Identify/Recognise:
1. Ask: does this colour feel like it comes toward you or recedes? (warm = advancing, cool = receding).
2. Ask: if there are two similar colours, which appears warmer? The one with more red/orange admixture.
3. In a colour picker: check the hue angle and assess whether any secondary admixture is toward red or blue.

# Context & Application

- **Typical contexts**: Brand colour selection (warm brands feel friendly/energetic; cool brands feel professional/trustworthy), photography colour grading (warm vs. cool tones), UI design (call-to-action warmth vs. informational coolness), data visualisation diverging scales.
- **Common applications**: Warm/cool palette split for emotional differentiation; using temperature contrast for depth in flat design; colour grading in film/photography to set emotional tone; diverging colour scales in data visualisation (warm colours for positive/high values, cool for negative/low).

## Cross-Domain Connections

**Engineering → STRUCTURAL**: Physical colour temperature, measured in Kelvin (K), describes the spectral output of an ideal blackbody radiator. Counterintuitively, higher K = cooler-looking light (blue-white at 6500K, e.g. daylight) and lower K = warmer-looking light (orange-red at 2700K, e.g. candlelight). The same warm/cool vocabulary applies to both physical and perceptual temperature, but the scales run in opposite directions for physical and perceptual usage (low K = perceptually "warm"). This shared vocabulary between physical photometry and perceptual psychology creates a persistent source of confusion.

# Examples

**Example 1** (pp. 393–394): Arnheim's counterintuitive analysis — "a reddish blue looks warm whereas a bluish red looks cold." The admixture direction, not the dominant hue, determines temperature. This challenges the common assumption that all reds are warm and all blues are cool.

**Example 2** (p. 394): Itten's temperature poles — red-orange ↔ blue-green as the maximum warm/cool contrast pair, supporting the role of red admixture in warming and blue admixture in cooling.

**Example 3** (pp. 392–393): Kandinsky's colour responses — a yellow circle "reveals a spreading movement outwards from the center"; a blue circle "develops a concentric movement." This spatial expansion/contraction quality is the experiential correlate of warm (advancing) vs. cool (receding).

**Example 4** (p. 394): "Warm colors seem to invite us whereas cold ones keep us at a distance. Warm colors are outgoing, cold ones draw back." The temperature quality connects to social/emotional qualities of openness vs. distance.

# Relationships

## Builds Upon
- **Hue** — Temperature is a property of hue relationships (deviation direction).

## Enables
- **Spatial depth in composition** — Warm/cool opposition creates perceptual depth (warm advances, cool recedes).
- **Emotional palette design** — Temperature is a key tool for establishing emotional register.

## Related
- **Colour harmony** — Temperature consistency is one component of harmonic unity.
- **Colour weight** — Temperature interacts with weight: warm colours tend to feel heavier and advance; cool colours feel lighter and recede.
- **Complementary colours** — Complementary pairs are often also warm/cool pairs (e.g., red/green, orange/blue).

## Contrasts With
- **Colour harmony through completion** — Harmony through completeness (complementarity) is distinct from harmony through temperature consistency, though they often align.

# Common Errors

- **Error**: Assuming all reds and oranges are warm and all blues and greens are cool.
  **Correction**: Per Arnheim, temperature depends on admixture direction: a bluish red is cooler than a reddish yellow; a reddish blue is warmer than a bluish green. Temperature is about deviation direction, not hue category membership.

- **Error**: Using warm/cool to describe physical colour temperature (Kelvin) and perceptual temperature interchangeably.
  **Correction**: Physical and perceptual colour temperature scales run in opposite directions (low K = warm-appearing light; perceptual warmth = toward red). The vocabulary is shared but the reference systems differ.

# Common Confusions

- **Confusion**: "Warm colours are always better for friendly/approachable brands."
  **Clarification**: Temperature is expressive but not deterministic. Cool colours (blue) are associated with trust and reliability; warm colours (red/orange) with energy and urgency. Context, saturation, and combinations determine the actual emotional effect.

- **Confusion**: "Adjusting colour temperature in photo editing is the same as adjusting perceived colour warmth."
  **Clarification**: Adjusting the Kelvin value of white balance shifts the entire image's colour balance; perceived warmth of specific elements will shift accordingly. They are related but not identical operations.

# Source Reference

Chapter VII: Color, "Art and Visual Perception," pp. 392–395 (section "Warm and Cold").

# Verification Notes

- Definition source: Synthesised from the "Warm and Cold" section. Arnheim's admixture-direction hypothesis is directly stated, with his own acknowledgment of uncertainty ("it has not been tested systematically and may turn out to be quite wrong").
- Confidence rationale: Medium — Arnheim states the hypothesis explicitly but with explicit uncertainty; the card preserves this uncertainty. The warm/cool distinction itself is well-established; Arnheim's specific admixture-direction mechanism is his own speculative contribution.
- Uncertainties: Arnheim's admixture-direction account is not standard colour theory and has not been widely confirmed; noted in the card.
- Cross-reference status: Verified — warm/cool colour temperature is a widely used practical concept. Arnheim's specific mechanism adds nuance not found in most accounts.
- Rosetta Stone check: Mapping added (engineering: physical colour temperature in Kelvin, structural — noting the paradoxical opposite scales).
- OCR issues: None detected.
