---
# === CORE IDENTIFICATION ===
concept: Weight of Colour
slug: weight-of-colour

# === CLASSIFICATION ===
category: design-principles
subcategory: balance
tier: intermediate
layer: 1-principles

# === PROVENANCE ===
source: "Art and Visual Perception: A Psychology of the Creative Eye"
source_slug: art-and-visual-perception
authors: "Rudolf Arnheim"
chapter: "I. Balance"
chapter_number: 1
pdf_page: 11
section: "Weight"

# === CONFIDENCE ===
extraction_confidence: medium

# === VARIANTS ===
aliases:
  - chromatic weight
  - hue weight
  - colour balance
  - saturation weight

# === TYPED RELATIONSHIPS ===
prerequisites:
  - visual-weight
  - tonal-weight
extends:
  - visual-weight
related:
  - visual-balance
  - tonal-weight
  - colour-theory
contrasts_with:
  - weight-by-size
  - weight-by-location

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "A dashboard uses teal header, red error badges, green success indicators, blue links, yellow warning banners, and purple notification badges. It looks like a 'clown car.' What principle was violated, and how do you fix it?"
  - "What is visual hierarchy, and what visual properties (size, colour, contrast, weight, spacing) establish it?"
  - "How does the visual-elements concept of 'value' (light-dark range) connect to colour theory's 'lightness' and to contrast as a design principle?"

# === VISUAL DESIGN EXTENSIONS ===
rosetta_stone:
  - domain: music
    concept: "Timbre / tonal colour (klangfarbe)"
    rating: loose
    note: "Musical timbre (the qualitative 'colour' of a sound — oboe vs. violin on the same pitch) is loosely analogous to hue in visual experience: both are qualitative dimensions orthogonal to the basic magnitude dimension (loudness/brightness), both affect the expressive weight or character of an element without necessarily changing its fundamental identity. The analogy is loose because no quantitative mapping between specific hues and timbres is established."
  - domain: mathematics
    concept: "Wavelength / perceptual salience"
    rating: loose
    note: "Longer-wavelength colours (red, orange) are physiologically more activating and perceptually more salient than shorter-wavelength colours (blue, violet) — loosely grounded in the differential sensitivity of retinal cones. The salience difference contributes to hue weight differences, but the mapping is not quantitatively specified."

css_implementation:
  - property: "color / background-color (semantic colour roles)"
    example: "color: hsl(0 80% 45%); /* saturated red: high chromatic weight */"
    support: baseline
  - property: "filter: saturate()"
    example: "filter: saturate(0.3); /* desaturate to reduce chromatic weight */"
    support: baseline
---

# Quick Definition

Hue and saturation contribute to visual weight independently of size and lightness: warm, saturated colours (especially red) are perceptually heavier than cool, desaturated colours (especially blue), and a colour designer must account for chromatic weight when balancing a composition.

# Core Definition

Arnheim notes that colour contributes to visual weight: "As to *color*, red is heavier than blue, and bright colors are heavier than dark ones." This establishes two distinct dimensions: hue weight (red > blue) and tonal/brightness weight (bright > dark). The hue-weight claim — that warm colours are heavier than cool ones — is a well-established perceptual finding. In the St. Michael painting example, the painter used "a large dark patch on the angel's robe" to create visual attraction (weight) — but in the Van Gogh bedroom example it is the redness (saturation + warm hue) of the bedcover that creates "a strong off-center weight." A clown's costume with red on the left and blue on the right "may be asymmetrical to the eye as a color scheme, even though the two halves of the costume...are equal in physical weight." This directly demonstrates chromatic weight: same physical weight, different visual weight due to hue.

# Prerequisites

- **Visual weight** — Chromatic weight is a specific contributor to the general concept of visual weight.
- **Tonal weight** — Tonal weight and chromatic weight are related but distinct; both arise from colour properties but operate differently.

# Key Properties

1. **Hue axis**: warm colours (red, orange, yellow) are heavier than cool colours (blue, violet, green) of equal size and brightness.
2. **Saturation axis**: more saturated colours are heavier than desaturated or grey colours.
3. **Red is the heaviest standard hue**: Arnheim explicitly states "red is heavier than blue" — this is the clearest hue-weight asymmetry.
4. Chromatic weight is independent of physical weight — a red area and a blue area of identical size and lightness differ in visual weight.
5. Colour asymmetry can create compositional imbalance even when all other factors (size, position, shape) are equal.

# Construction / Recognition

## To Identify/Recognise:
1. A composition that looks left-heavy or right-heavy despite equal element sizes may have a warm/cool colour asymmetry contributing to the imbalance.
2. A small red accent that "jumps out" of a composition is exhibiting high chromatic weight disproportionate to its size.
3. A dashboard that feels "loud" despite using moderate-sized elements likely has multiple high-saturation warm colours competing for weight.

## To Construct/Create:
1. Limit saturated, warm colours to elements that should carry the most weight (primary actions, alerts, key data points).
2. Use cool, desaturated colours for secondary elements to reduce their weight without reducing their size.
3. When balancing a warm-coloured element, provide a cooler, larger counterbalancing area — or use spatial position to leverage the warm element's weight at a distance.
4. In a multi-colour system, assign chromatic weight deliberately: the heaviest colour role should correspond to the highest hierarchy level.

# Context & Application

- **Typical contexts**: Colour palette design, UI colour system design, data visualisation colour encoding, information hierarchy through colour.
- **Common applications**: In UI design, a primary CTA in saturated red or orange carries maximum chromatic weight — justified if it is the single most important action. Using multiple saturated warm colours for different UI elements (as in the "clown car" problem) distributes heavy weight to too many elements, destroying hierarchy. In data visualisation, encoding the most important data series in a warm saturated colour and secondary series in cool desaturated colours creates a natural visual hierarchy without size differences.
- **Historical/stylistic notes**: Arnheim's discussion of colour weight is brief; he treats colour as one of several weight determinants rather than giving it extended treatment. His fuller treatment of colour appears in other chapters of the book (not covered in these assignments).

## Cross-Domain Connections

**Music → LOOSE**: Musical timbre (the qualitative "colour" of different instruments) shares a structural role with hue — both are qualitative dimensions that affect the expressive weight or character of an element. But the analogy is loose: we cannot translate a specific hue into a specific timbre with any precision, and the perceptual mechanisms are entirely different.

# Examples

**Example 1** (p. 19): "As to *color*, red is heavier than blue, and bright colors are heavier than dark ones." The clearest direct statement on hue weight.

**Example 2** (p. 19): "The patch of a bright red bedcover in Van Gogh's painting of his bedroom creates a strong off-center weight." Size is moderate; weight is generated by the combination of red (warm hue) and brightness.

**Example 3** (p. 20): The clown costume example: "A clown's costume — red on the left side, blue on the right — may be asymmetrical to the eye as a color scheme, even though the two halves of the costume, and indeed of the clown, are equal in physical weight." This isolates chromatic weight from physical weight and from size.

# Relationships

## Builds Upon
- **Visual weight** — Chromatic weight is a specific contributor to the general concept of visual weight.

## Enables
- **Colour hierarchy** — Deliberate assignment of chromatic weight creates a colour-based hierarchy: warm/saturated = high priority, cool/desaturated = low priority.
- **Visual balance** — Chromatic weight must be accounted for in compositional balance calculations alongside size, location, and tone.

## Related
- **Tonal weight** — Brightness/darkness is a related but distinct weight factor; the two often act together but can be separated.
- **Visual balance** — Weight of colour is one variable in the balance equation.

## Contrasts With
- **Weight by size** — A small red element can outweigh a large blue element — chromatic weight can override size weight.

# Common Errors

- **Error**: Assigning saturated colours to multiple elements of different hierarchy levels.
  **Correction**: Reserve high chromatic weight (warm, saturated) for the highest-priority elements. Use the hierarchy of hue weight deliberately: red/orange > yellow > green > blue > violet, and saturated > desaturated.

- **Error**: Treating colour balance as purely aesthetic ("I like how these colours look together").
  **Correction**: Colour balance has a perceptual structure independent of aesthetic preference. Warm-heavy layouts systematically feel different from cool-heavy ones, and this is not personal taste but perceptual physics.

# Common Confusions

- **Confusion**: Colour weight = colour brightness (the brighter the heavier).
  **Clarification**: Brightness (lightness) and hue are independent weight contributors. A dark red (maroon) has high hue weight (red) but low tonal weight (dark). A bright blue has high tonal weight but lower hue weight. The net visual weight depends on both contributions.

# Source Reference

Chapter I: Balance, "Art and Visual Perception," pp. 18-20. The "Weight" section mentions colour within the broader enumeration of weight determinants.

# Verification Notes

- Definition source: Direct quotes from p. 19 ("red is heavier than blue"; "bright colors are heavier than dark ones"; clown costume example). Synthesised from the "Weight" section.
- Confidence rationale: Medium — Arnheim's statements on colour weight are brief and not systematically developed in this chapter. The extraction is reliable but the card synthesises more than Arnheim explicitly develops here.
- Uncertainties: Arnheim does not distinguish hue weight from saturation weight; both are implicit in his colour-weight claims. The separation into hue vs. saturation axes is an editorial elaboration justified by colour theory but not fully present in the source text.
- Cross-reference status: Generic slug; will harmonise with colour-weight concepts from colour theory sources.
- Rosetta Stone check: Music/timbre mapping identified as LOOSE. Mathematics/wavelength-salience mapping identified as LOOSE. No rigorous or structural mappings found for chromatic weight specifically.
- OCR issues: None significant.
