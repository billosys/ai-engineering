---
# === CORE IDENTIFICATION ===
concept: Munsell Colour Solid
slug: munsell-colour-solid

# === CLASSIFICATION ===
category: colour-theory
subcategory: colour-systems
tier: intermediate
layer: 2-domain

# === PROVENANCE ===
source: "A Practical Description of The Munsell Color System"
source_slug: munsell-colour-system
authors: "T. M. Cleland"
chapter: "III. Chroma"
chapter_number: 6
pdf_page: 7
section: null

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "Munsell colour space"
  - "colour tree"
  - "colour sphere"
  - "Munsell color solid"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - hue
  - colour-value
  - chroma
  - neutral-axis
  - munsell-hue-circle
extends:
  - munsell-colour-system
related:
  - munsell-colour-notation
  - colour-balance
  - complementary-colours
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "CQ 3: What is the difference between hue, saturation/chroma, and lightness/value?"

# === VISUAL DESIGN EXTENSIONS ===
rosetta_stone:
  - domain: mathematics
    concept: "3D cylindrical coordinate system with irregular boundary"
    rating: rigorous
    note: "The Munsell solid is a cylindrical coordinate system (r, θ, z) where the ideal sphere constrains r to a constant maximum and the practical colour tree allows r_max to vary as a function of θ (hue) and z (value), defining an irregular gamut boundary surface."

css_implementation: []
---

# Quick Definition

The Munsell Colour Solid is the three-dimensional model of colour space in two forms: the ideal Colour Sphere (all chromas equal, enabling automatic balance) and the practical Colour Tree (asymmetric branches reflecting each hue's actual chroma range at each value level).

# Core Definition

Cleland describes two complementary 3D models. The **Colour Sphere** is "a globe, the north pole of which represents white, the south pole black, and the axis made up of a sequence of grays extending from white to black. Around the equator is a band of hues whose value is 5/ and chroma /5" (footnote, p. 8).

However, "in the actual measurement of pigment colors... all of the paths of Chroma would not be of the same length nor would they all be comprised within a sphere. Certain of them would extend to points outside of it" (p. 8). To represent actual pigment gamuts, Munsell conceived the **Colour Tree**: "a 'Color Tree' with a vertical trunk for the scale of Value and branches representing the different Hues, these branches varying in length with the Chroma Strength of each Hue" (p. 9).

The sphere is limited to the shortest chroma path: "The sphere is limited in size to this shortest axis" — Blue-Green at /5. Within this sphere, "all opposite colors will balance because being all of equal length at each level of Value no Chroma path can be longer than another or outbalance it" (p. 12).

# Prerequisites

- **Hue** — The angular dimension.
- **Colour Value** — The vertical dimension.
- **Chroma** — The radial dimension.
- **Neutral Axis** — The structural spine.
- **Munsell Hue Circle** — The equatorial cross-section.

# Key Properties

1. **Cylindrical structure**: Hue (angular), Value (vertical), Chroma (radial).
2. **Sphere (ideal)**: Equal chroma paths at all hue/value combinations. Guarantees automatic balance.
3. **Tree (practical)**: Asymmetric — "Colors differ by nature in their Chroma Strength" (p. 8). Red extends to /10, Blue-Green to /5.
4. **Value-dependent chroma maxima**: "All colors do not reach their maximum Chroma Strength at the same level of Value" — strongest yellow is high-value, strongest blue is low-value (p. 8).
5. **Open boundary**: Chroma is "limited only by the strength of pigments" — the tree can grow (p. 9).
6. **Rotation test**: "Upon rotating the sphere each band of hues turns to gray" — confirming correct centring on the neutral axis (footnote, p. 8).

# Construction / Recognition

## To Construct/Create:
1. Erect a vertical neutral axis from black (0) to white (10).
2. At each value level, arrange the hue circle horizontally.
3. **For the sphere**: Extend all hue paths to equal length (shortest maximum, 5 steps).
4. **For the tree**: Extend each hue path to its actual maximum chroma at each value level.
5. The result is a 3D solid — symmetric (sphere) or asymmetric (tree).

## To Identify/Recognise:
1. A 3D colour model with value on a vertical axis, hue angularly, chroma radially.
2. Symmetric = idealised sphere. Asymmetric = practical tree.

# Context & Application

- **Typical contexts**: Colour science, gamut mapping, understanding pigment limitations, colour education.
- **Common applications**: Visualising the complete colour space; understanding why some combinations require area adjustments; predicting gamut boundaries.

## Cross-Domain Connections

**Mathematics → Rigorous**: The Munsell solid is a cylindrical coordinate system (r, θ, z) applied to perceptual colour space. The ideal sphere represents the constraint r = constant; the tree represents the gamut boundary where r_max = f(θ, z). This is a literal geometric identity, not an analogy.

# Examples

**Example 1** (p. 8): "The strongest red pigment... is twice as powerful as the strongest blue-green pigment... The Chroma path of Red is the longest... being ten measured steps from the neutral pole; while Blue-Green is the shortest, being only five steps."

**Example 2** (p. 9): "Mr. Munsell has conceived this as a 'Color Tree' with a vertical trunk for the scale of Value and branches representing the different Hues."

**Example 3** (p. 12): "Within a sphere thus limited, all opposite colors will balance."

# Relationships

## Builds Upon
- **Hue**, **Colour Value**, **Chroma**, **Neutral Axis**, **Munsell Hue Circle** — The five structural components.

## Enables
- **Colour Balance** — The sphere guarantees balance; the tree requires calculations.
- **Munsell Balance Formula** — Compensates for the tree's asymmetry.

## Related
- **Munsell Colour Notation** — Addresses points within this solid.
- **Complementary Colours** — Lines through the centre of the solid.

## Contrasts With
No contrasting solid models are described in this source. The Munsell solid contrasts with the HSL double-cone, which lacks perceptual uniformity.

# Common Errors

- **Error**: Treating sphere and tree as contradictory models.
  **Correction**: They are complementary — the sphere is the idealised, balanced form; the tree maps real pigments. The sphere is contained within the tree.

# Common Confusions

- **Confusion**: The sphere is "wrong" because it excludes some pigment colours.
  **Clarification**: The sphere is deliberately limited to guarantee balance. It is a design tool, not a comprehensive map.

- **Confusion**: The colour tree has a fixed shape.
  **Clarification**: The tree grows as new pigments are discovered or display technologies advance.

# Source Reference

Chapter 6: III. Chroma, pp. 7-9. Chapter 8: Balance, pp. 11-12.

# Verification Notes

- Definition source: Direct quotes from Ch 6, pp. 8-9 and footnote.
- Confidence rationale: High — explicit descriptions of both forms with clear rationale.
- Uncertainties: The footnote on p. 8 cites Munsell's own book, not Cleland's text directly.
- Cross-reference status: Verified against Ch 8.
- Rosetta Stone check: Mathematics (cylindrical coordinates with irregular boundary) rated RIGOROUS.
