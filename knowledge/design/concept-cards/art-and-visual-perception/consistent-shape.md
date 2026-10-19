---
concept: "Consistent Shape (Grouping by Continuation)"
slug: "consistent-shape"
category: "visual-perception"
subcategory: "gestalt laws"
tier: "intermediate"
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
  - "good continuation"
  - "grouping by continuation"
  - "continuity (gestalt)"
  - "consistent contour"
prerequisites:
  - "praegnanz"
  - "perceptual-grouping-similarity"
extends:
  - "perceptual-grouping-similarity"
related:
  - "visual-shape"
  - "structural-skeleton"
  - "visual-subdivision"
contrasts_with:
  - "visual-subdivision"
answers_questions:
  - "What are the gestalt principles of perceptual grouping, and how does each one work?"
  - "How does the relationship between inter-group and intra-group spacing communicate which elements belong together (gestalt proximity)?"
rosetta_stone:
  -
    domain: "mathematics"
    concept: "Smooth curve continuity (C1/C2 continuity in spline design)"
    rating: "structural"
    note: "C1 requires equal first derivatives at the join under the chosen parameter; C2 also requires equal second derivatives. G1 requires positive proportional nonzero tangents. These are exact geometric conditions and useful construction aids, not a theorem of perceptual grouping."
  -
    domain: "music"
    concept: "Voice leading / melodic continuation"
    rating: "structural"
    note: "In the reported Piston tonal practice, holding common tones and choosing nearby remaining tones can support melodic continuity. Harmony, range and voice constraints still matter; this is not a universal nearest-note algorithm or a guarantee of perceived voices."
  -
    domain: "engineering"
    concept: "API consistency / interface coherence"
    rating: "structural"
    note: "Shared naming, parameter and return conventions can make an API family easier to recognize. The match is coherence across instances; disconnected interfaces do not form one continuous visual contour."
css_implementation:
  -
    property: "Candidate border-radius across a component family"
    example: "/* Candidate shared family treatment; inspect with content, mixed styles may be deliberate. */ .btn, .input, .select { border-radius: var(--radius-control); }"
    support: "baseline"
  -
    property: "SVG path continuity (smooth joins)"
    example: "<path d='M 0 0 C 30 0 70 100 100 100 S 170 0 200 0' /> <!-- S = smooth continuation -->"
    support: "baseline"
  -
    property: "CSS easing maps animation progress"
    example: "animation: slide 0.3s cubic-bezier(0.4, 0, 0.2, 1); /* Author timing candidate; no geometric join or perceptual guarantee. */"
    support: "baseline"
---

# Quick Definition

In Arnheim's account, consistent shape is the grouping tendency by which visual elements that share an intrinsic continuity of direction, curvature, or structural character can be perceived as belonging to the same continuous unit, even when interrupted or widely separated.

# Core Definition

This section presents the represented Arnheim account. Its quotations, page references and historical or experimental reports have not been checked against the unavailable original; current analytic qualifications below do not certify that fidelity.

Arnheim introduces consistent shape as a step beyond similarity between separate discrete units: "One step beyond the mere similarity of separate units is the grouping principle of consistent shape. This principle relies on the intrinsic similarity of the elements constituting a line, surface, or volume" (Chapter II, p. 58). The principle explains why interrupted contours are perceived as continuous, and why points arranged along an implicit path are grouped into that path. In Figure 63: "Figure 63a will be seen more easily as a combination of the two parts indicated in b than of the two indicated in c, because b provides the simpler structure" — where two crossing lines meet, the eye prefers to continue each line in its original direction rather than see them exchange directions. "When there is a choice between several possible continuations of lines... the spontaneous preference is for the one that carries on the intrinsic structure most consistently" (p. 59). This is also called "good continuation" in the standard Gestalt literature.

# Prerequisites

- **Praegnanz** — Consistent shape selects the simplest continuation; Praegnanz is the governing principle.
- **Perceptual Grouping by Similarity** — Consistent shape extends similarity grouping from discrete units to continuous paths.

# Key Properties

1. **Direction-preserving** — The eye prefers continuations that preserve the current direction/curvature of a line or surface.
2. **Simplicity-selecting** — In this account a simpler continuation tends to be favored; ambiguity, context and task can leave multiple readings.
3. **Interruption-spanning** — Consistent shape operates across spatial gaps and interruptions: a line perceived as continuing behind an occlusion follows consistent shape.
4. **Implicit path formation** — Even without explicit connecting lines, a sequence of dots or endings arranged along an implicit curve groups into that curve.
5. **Musical parallel** — Reported tonal voice leading offers a comparison for melodic continuity, subject to harmony, range and voice constraints; it is not an equivalent visual mechanism.

# Construction / Recognition

## To Construct/Create:
1. Where two lines or curves cross or meet, ensure each continues in a direction consistent with its previous path (unless a deliberate break is intended).
2. For interrupted lines (dashed, partially occluded): maintain consistent direction so the eye bridges the gap.
3. For icon families, compare intended stroke, curvature and optical-size relationships. Similarity across disconnected members can aid family coherence; deliberate mixed styles can serve roles and are not broken curve joins.
4. For typographic text: consistent letterform construction principles (same contrast axis, same terminal style, same stem-to-stroke ratio) group a typeface's characters into a coherent perceptual family.
5. For visual paths (arrows, guides, flow indicators): ensure each segment continues the direction established by its predecessor.

## To Identify/Recognise:
1. At every junction or intersection: does each line/curve continue in its established direction?
2. For a set of interrupted elements: does the eye naturally bridge the gaps (consistent shape present) or see isolated fragments?
3. In a composition: can you trace continuous visual paths, or does the eye get lost at every junction?

# Context & Application

- **Typical contexts**: Icon design, illustration, typographic system coherence, data visualisation (line charts, flow diagrams), animation path design, logo mark design.
- **Common applications**: Connected line-chart segments can suggest a continuing trend; the connection must suit the data. Shared strokes, corners or padding can support coherence among separate icons and controls, while deliberate role and optical differences remain valid. Family resemblance is not identical to continuation along one contour.

## Cross-Domain Connections

**Mathematics → STRUCTURAL**: For parameterised curves meeting at a shared endpoint, C1 requires equal first derivatives and C2 equal first and second derivatives. G1 requires nonzero tangents in the same direction (positive proportionality). Tangents (1,0) and (2,0) are G1 but not C1. The existing SVG smooth join has derivatives (90,0)/(90,0) and second derivatives (-60,-600)/(60,-600): C1, not C2. These exact construction facts do not formalise a neural grouping law or predict which path a viewer will see.

**Music → STRUCTURAL**: The reported Piston practice holds common tones and moves remaining voices toward nearby available notes in a tonal context. It compares continuity across successive tones, while harmonic function, range and voice constraints still matter. Neither all music nor guaranteed perceived voices follow a nearest-note algorithm.

# Examples

**Example 1** (p. 58): Picasso's painting of a woman: "the right leg of the woman [is seen] as a continuous shape, despite its interruption by the left leg. Even though we know what a woman is expected to look like, the two shapes representing the leg would not unite into one if the contour lines were not related by similarity of direction and location."

**Example 2** (p. 59): The Big Dipper: "What makes us combine the seven stars of the Big Dipper in the particular continuous sequence to which we are accustomed?" The pattern is consistent shape — the stars are connected in the simplest, most continuously directional sequence available. The reported Weiss silver-drop experiment supplies a historical comparison; it does not establish a neural field or prove that culture and familiarity play no role in seeing the Big Dipper.

**Example 3** (p. 59): Figure 63: two curved lines crossing. "Figure 63a will be seen more easily as a combination of the two parts indicated in b than of the two indicated in c, because b provides the simpler structure." Each line continues in its established direction at the crossing point.

**Example 4** (p. 59–60): Piston's voice leading in Figure 64: "if two triads have one or more notes in common, these are repeated in the same voice, the remaining voice or voices moving to the nearest available condition" — consistent shape in the melodic lines.

# Relationships

The following are scoped conceptual reading connections. In the represented account, simplicity, axes and grouping explain one another; these links do not establish causal neural mechanisms. Unnamed downstream uses and ordinary comparisons are not automatically resolved card identities.

## Builds Upon
- **Praegnanz** — Consistent shape selects the continuation that produces the simplest total pattern.
- **Perceptual Grouping by Similarity** — Consistent shape is an extension: similarity between contiguous elements (not just separated units) based on directional and structural continuity.

## Enables
- **Perceptual Unity of Complex Forms** — Consistent shape allows a complex form built from multiple segments to be perceived as a unified whole.
- **Visual Path** — Continuation can suggest a path through a composition; a predicted eye-movement route needs observation and depends on task.

## Related
- **Structural Skeleton** — Continued directions can contribute to a perceived framework of axes; that framework is not necessarily a unique or mathematically shortest description.
- **Shape Completion** — Completion often involves extending a partial shape along its established direction (consistent shape applied to a truncated form).

## Contrasts With
- **Visual Subdivision** — Where subdivision breaks continuous forms into separate parts, consistent shape bridges gaps to maintain continuity.

# Common Errors

- **Error**: Allowing lines and curves to change direction arbitrarily at junctions.
  **Correction**: Check whether a junction suggests the intended path. A deliberate corner or break can communicate a branch; continuity is a useful cue rather than an obligation.

- **Error**: Creating icon sets with inconsistent curvature character (mixing sharp-cornered and round-cornered forms).
  **Correction**: Unexpected curvature differences may weaken intended family similarity. Compare roles, optical sizes and context; deliberate sharp/round or outlined/filled distinctions may be appropriate.

# Common Confusions

- **Confusion**: Consistent shape and proximity are the same principle.
  **Clarification**: Proximity (similarity of spatial location) groups nearby elements regardless of their directional relationship. Consistent shape groups elements along a direction/curvature path regardless of proximity — elements can be widely separated and still be grouped by consistent shape if they lie along a consistent implied path.

- **Confusion**: Good continuation means the eye always prefers straight lines.
  **Clarification**: Established direction and curvature can constrain a likely continuation, whether straight, curved or spiralling. A partial arc does not uniquely determine a circle; context can support another completion.

# Source Reference

Chapter II: Shape, "Art and Visual Perception," pp. 58–61. Section: "Similarity and Difference" (consistent shape subsection).

# Verification Notes

The bullets below preserve historical extraction assertions, including their confidence, cross-reference, OCR and source-reading claims; they are not current verification. The represented original edition/page basis is unavailable, so fidelity of all quotations, locators, figures, experiments and historical claims remains unassessed. Current technical corrections and scoped analogies do not establish a neural mechanism, cultural universality or measured usability.

- Definition source: Direct quote from p. 58 naming "consistent shape" as a grouping principle; pp. 58–60 demonstrate it extensively.
- Confidence rationale: High — Arnheim names the principle explicitly and provides multiple demonstrations including the Picasso figure and the Big Dipper.
- Uncertainties: Arnheim uses "consistent shape" rather than the more standard "good continuation" of Wertheimer; this card uses Arnheim's terminology.
- Cross-reference status: Verified — connects to praegnanz, perceptual-grouping-similarity, visual-shape.
- Rosetta Stone check: Mappings added (mathematics/spline continuity rigorous; music/voice leading structural; engineering/API consistency structural).
- OCR issues: None relevant to this section.
