---
concept: "Perceptual Grouping by Similarity"
slug: "perceptual-grouping-similarity"
category: "visual-perception"
subcategory: "gestalt laws"
tier: "foundational"
layer: "0-perception"
source: "Art and Visual Perception: A Psychology of the Creative Eye"
source_slug: "art-and-visual-perception"
authors: "Rudolf Arnheim"
chapter: "II. Shape"
chapter_number: 2
pdf_page: 31
section: "Similarity and Difference"
extraction_confidence: "high"
aliases:
  - "gestalt similarity"
  - "grouping by similarity"
  - "homogeneity principle"
  - "similarity grouping"
prerequisites:
  - "praegnanz"
  - "visual-shape"
extends: []
related:
  - "visual-subdivision"
  - "consistent-shape"
  - "contour-and-boundary"
contrasts_with:
  - "visual-subdivision"
answers_questions:
  - "What are the gestalt principles of perceptual grouping, and how does each one work?"
  - "How does the relationship between inter-group and intra-group spacing communicate which elements belong together (gestalt proximity)?"
  - "An icon set mixes outlined and filled styles, some at 16px and some at 24px, some with rounded corners and some with sharp corners. It feels 'off.' What principle was violated?"
rosetta_stone:
  -
    domain: "mathematics"
    concept: "Equivalence classes / partition of a set"
    rating: "structural"
    note: "Equality on a chosen feature can define equivalence classes. Perceptual similarity need not be transitive: on 0, 1, 2 with distance at most 1, 0 resembles 1 and 1 resembles 2 while 0 does not resemble 2. Thus perceptual grouping need not form a mathematical partition."
  -
    domain: "engineering"
    concept: "Type checking / duck typing"
    rating: "loose"
    note: "Duck typing compares available behavior rather than declarations; visual grouping compares selected appearances. The loose match is selective comparison, not an identity between type checking and perception."
  -
    domain: "music"
    concept: "Voice leading by common tone / harmonic proximity"
    rating: "structural"
    note: "The reported Piston tonal voice-leading practice can support continuity through common or nearby pitches. Pitch distance is not literal spatial location, and range, harmony and voice constraints prevent a universal nearest-note rule."
css_implementation:
  -
    property: "Shared colour as one grouping cue"
    example: "/* Use supplied roles; colour alone must not carry action meaning. */ .btn-primary { background: var(--color-brand); } .btn-danger { background: var(--color-danger); }"
    support: "baseline"
  -
    property: "gap / margin for relative proximity grouping"
    example: ".form-group { display: flex; flex-direction: column; gap: 4px; } /* Author inner-gap candidate; compare outer gaps, content and competing cues. */"
    support: "baseline"
---

# Quick Definition

Perceptual grouping by similarity is the gestalt principle by which the visual system unites separate elements that share one or more perceptual properties — shape, size, brightness, colour, orientation, or spatial location — into a perceived group.

# Core Definition

This section presents the represented Arnheim account. Its quotations, page references and historical or experimental reports have not been checked against the unavailable original; current analytic qualifications below do not certify that fidelity.

Arnheim reports that Wertheimer's pioneering 1923 study described several grouping properties, and that Musatti showed they "could be reduced to one, the rule of homogeneity or similarity" (Chapter II, p. 53). Similarity can cause grouping along any perceptual dimension: "Any aspect of percepts—shape, brightness, color, spatial location, movement, etc.—can cause grouping by similarity" (p. 53). Similarity operates alongside subdivision as an opposing tendency: "Similarity and subdivision are opposite poles. Whereas subdivision is one of the prerequisites of sight, similarity can make things invisible... Homogeneity is the limiting case, in which... vision approaches or attains the absence of structure" (p. 52). The account discusses grouping among distinguishable elements. Identical dots can still form two spatially separated clusters: shared appearance does not erase proximity structure; a uniform unsegregated field is a different case. Crucially, comparisons must proceed from a common base: "Similarity is a prerequisite for the noticing of differences" (p. 54).

# Prerequisites

- **Praegnanz** — Grouping by similarity is an application of Praegnanz: the visual field organises into the simplest available structure, which includes grouping similar elements.
- **Visual Shape** — Shape similarity is one of the primary dimensions on which grouping operates; understanding shape is prerequisite to understanding shape-based grouping.

# Key Properties

1. **Multi-dimensional** — Grouping can occur along any perceptual dimension: shape, size, brightness, colour, orientation, spatial location (proximity), speed, direction.
2. **Comparison basis** — State the feature and context under comparison; shared reference conditions can make a difference salient without imposing a strict category rule.
3. **Relative judgment** — Whether elements look alike depends on how different they are from their environment: "the round shapes resemble each other compellingly despite their differences because they are surrounded by angular, straight-lined shapes" (p. 67).
4. **Interaction with subdivision** — Distinguishable identical dots can group into two separated clusters; a uniform unsegregated field has no such internal marks. Perfect feature similarity does not itself eliminate grouping.
5. **Top-down and bottom-up** — Similarity operates "from below" (element-to-element) and is supplemented by overall pattern structure "from above."

# Construction / Recognition

## To Construct/Create:
1. Decide which elements should belong to the same perceptual group.
2. Assign a shared perceptual property to all members of that group (consistent colour, shape, weight, size, orientation).
3. Ensure the shared property distinguishes the group from non-members — similarity only works in context of difference.
4. Add reinforcing cues when the task benefits; one clear cue can suffice and extra cues can compete or overstate grouping.
5. Deliberately break one or more similarity cues to signal differentiation within an otherwise similar set (e.g., one different colour in an otherwise monochrome set draws the eye).

## To Identify/Recognise:
1. Which elements share a perceptual property that others don't? Those form a group.
2. Are individual marks distinguishable from their background? Identical marks may still form separate spatial clusters; a uniform unsegregated field is different.
3. Do competing similarity cues conflict, creating ambiguous or multiple groupings?

# Context & Application

- **Typical contexts**: Navigation menus, icon families, form design, data visualisation, typographic hierarchy, colour-coded systems.
- **Common applications**: Supplied action colours can reinforce functional groups, with labels or other signals preserving meaning beyond colour. Similar strokes and corners can support icon-family coherence. Mixed outlined/filled styles or 16px/24px optical sizes may be deliberate role distinctions; unintended variation is a candidate explanation for an incoherent family, not an automatic perceptual-law violation.

## Cross-Domain Connections

**Mathematics → STRUCTURAL**: Equality on a specified feature can partition a set into equivalence classes. Perceptual resemblance need not be transitive: for values 0, 1, 2 with distance at most 1, 0 resembles 1 and 1 resembles 2, but 0 does not resemble 2. Thus grouping can be ambiguous or overlapping rather than a mathematical partition.

**Music → STRUCTURAL**: The reported Piston tonal practice can preserve melodic continuity by held common tones and nearby pitches. It is a comparison with selected pitch relationships, not literal spatial similarity or a universal algorithm overriding harmony, range and voice constraints.

# Examples

**Example 1** (p. 54): In Figure 52, shape, spatial orientation, and brightness are kept constant across all squares. These similarities "knit all the squares together and at the same time forcefully point to their difference in size" — identical similarity cues unite the set while the one differing cue (size) becomes the salient distinction.

**Example 2** (p. 53–54): Grouping by similarity of shape (Figure 53 — circles vs. non-circles), brightness (Figure 54 — black vs. white disks), spatial location/proximity (Figure 55), and spatial orientation (Figure 56) are demonstrated as separate dimensions that each independently produce grouping.

**Example 3** (p. 64–65): In Grünewald's *Crucifixion*, the "bright red is reserved for the clothes of Christ and those of one of the money changers" — colour similarity unites two spatially distant figures, creating a semantic as well as compositional connection.

**Example 4** (p. 66–67): In Picasso's *Seated Woman*, "the similarity of the geometric shapes throughout the picture emphasizes the unity of the whole and understates, in the cubist manner, the distinction between the woman and the screen-like background."

# Relationships

The following are scoped conceptual reading connections. In the represented account, simplicity, axes and grouping explain one another; these links do not establish causal neural mechanisms. Unnamed downstream uses and ordinary comparisons are not automatically resolved card identities.

## Builds Upon
- **Praegnanz** — Similarity grouping is Praegnanz applied to sets of segregated elements.
- **Visual Shape** — Shape is one of the primary similarity dimensions for grouping.

## Enables
- **Consistent Shape (Grouping Principle)** — The extension of similarity grouping from discrete elements to continuous lines and curves.
- **Visual Symmetry** — Symmetry is "similarity of location" extended to mirror positions within a whole pattern.
- **Compositional Unity** — Shared features can contribute to unity with spacing, continuation and other cues; similarity is not a unique or sufficient mechanism.

## Related
- **Visual Subdivision** — The opposing pole: subdivision separates, similarity unites. Both are necessary; their balance determines the structure of the visual field.
- **Proximity (Similarity of Location)** — A special case of similarity grouping: elements close in space share a spatial property, which groups them.

## Contrasts With
- **Visual Subdivision** — Subdivision separates elements into distinct units; similarity groups separated units together. They work together but in opposing directions: "Similarity and subdivision are opposite poles."

# Common Errors

- **Error**: Using similarity along only one dimension when trying to establish a clear grouping.
  **Correction**: A single cue can work. Consider additional cues when useful, and compare their effect with competing grouping signals; no monotonic strength guarantee follows from adding cues.

- **Error**: Using similarity globally (everything shares a property) expecting grouping to result.
  **Correction**: Identical dots can form two groups when separated spatially. Distinguish equality of a feature from a uniform unsegregated field, and compare actual within-group and between-group gaps; there is no fixed required gap.

# Common Confusions

- **Confusion**: Proximity is a separate principle from similarity.
  **Clarification**: Arnheim follows Musatti in treating proximity (nearness) as a special case of similarity — specifically, similarity of spatial location. That is the attributed Arnheim/Musatti reduction, not a complete modern catalog. Keeping proximity and similarity distinct is useful when distance and appearance supply competing cues.

- **Confusion**: Similarity grouping operates bottom-up only.
  **Clarification**: Similarity operates both bottom-up (element-to-element) and top-down (overall structural pattern determines which similarities are perceptually relevant). "The approach 'from below'... is quite limited, and must be supplemented by the approach 'from above'" (p. 57).

# Source Reference

Chapter II: Shape, "Art and Visual Perception," pp. 52–58, 64–67. Section: "Similarity and Difference" and "Examples from Art."

# Verification Notes

The bullets below preserve historical extraction assertions, including their confidence, cross-reference, OCR and source-reading claims; they are not current verification. The represented original edition/page basis is unavailable, so fidelity of all quotations, locators, figures, experiments and historical claims remains unassessed. Current technical corrections and scoped analogies do not establish a neural mechanism, cultural universality or measured usability.

- Definition source: Direct quotes from pp. 52–54; concept named explicitly by Arnheim following Wertheimer.
- Confidence rationale: Wertheimer's similarity principle is explicitly named and illustrated; multiple dimensions demonstrated with figures. High confidence.
- Uncertainties: Arnheim's treatment of proximity as a case of similarity (following Musatti) differs from some standard Gestalt presentations that treat them as separate laws — this card follows Arnheim.
- Cross-reference status: Verified — connects to praegnanz, visual-subdivision, consistent-shape.
- Rosetta Stone check: Mappings added (mathematics/equivalence classes structural; music/voice leading structural; engineering/duck typing loose).
- OCR issues: None relevant to this section.
