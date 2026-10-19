---
concept: "Visual Information Design"
slug: "visual-information-design"
category: "information-architecture"
subcategory: null
tier: "intermediate"
layer: "2-domain"
source: "Art and Visual Perception: A Psychology of the Creative Eye"
source_slug: "art-and-visual-perception"
authors: "Rudolf Arnheim"
chapter: "III. Form"
chapter_number: 3
pdf_page: 65
section: "Visual Information"
extraction_confidence: "high"
aliases:
  - "informational-illustration"
  - "technical-illustration"
  - "scientific-illustration-principles"
prerequisites:
  - "representation-in-art"
  - "visual-form-as-structured-equivalence"
  - "perceptual-simplicity"
extends: []
related:
  - "canonical-view"
  - "structural-skeleton"
  - "levels-of-abstraction-in-representation"
contrasts_with: []
answers_questions:
  - "How do you systematically audit an existing interface for visual design quality? What checklist of principles and patterns do you evaluate, in what order?"
  - "What is visual hierarchy, and what visual properties (size, colour, contrast, weight, spacing) establish it?"
rosetta_stone:
  -
    domain: "engineering"
    concept: "API documentation / technical specification writing"
    rating: "structural"
    note: "Visual and written documentation should expose information needed for the actual use. A tutorial, diagram, screenshot, optical record or complete reference can each be appropriate. Selection must retain required facts, exact quantities, text and appearance rather than equate completeness with noise."
css_implementation: []
---

# Quick Definition

Visual information design arranges images to convey task-relevant facts and relationships clearly. Selection and grouping can help, while exact proportions, angles, textures, text or optical appearance may themselves be required information.

# Core Definition

This section presents the represented Arnheim account. Its quotations, page references and historical, clinical, cultural or experimental reports have not been checked against the unavailable original. The current analytic qualifications do not certify that fidelity.

Arnheim addresses the apparent exception to his representational theory: technical and scientific illustration for reference purposes. The represented discussion favors selective clarity, while its own technical examples explicitly require exact proportions, angles and textures. This is not a rejection of accuracy.

"Recording by photography, the most faithful method of image-making, has not really superseded the human craftsman, and for good reasons. Photography is indeed more authentic in the rendering of a street scene, a natural habitat, a texture, a momentary expression. What counts in these situations is the accidental inventory and arrangement, the overall quality, and the complete detail rather than formal precision. When pictures are to serve technological or scientific purposes — for example, illustrations of machines, microscopic organisms, surgical operations — the preference is for drawings, or at least for photographs retouched by hand." (p. 552)

The represented argument favors making required properties clear. A photograph, drawing or composite can each serve a technical task; the quoted historical preference for drawings is not a universal current rule. The relevant properties must be:
- **Selected**: irrelevant detail omitted
- **Unambiguous**: perceptual factors (simplicity of shape, orderly grouping, clear overlapping, distinction of figure and ground, use of lighting) must ensure the relevant properties are unequivocal
- **Understood by the illustrator**: "A draftsman charged with producing a faithful likeness of an electric clockwork or a frog's heart must invent a pattern that fits the object — exactly as the artist must do."

The reported maxim "All reproduction is visual interpretation." does not rule out detailed optical records or complete references.

Leonardo da Vinci's scientific drawings are exemplary because he understood the structure and function of the objects and organised complex perceptual patterns with maximum clarity.

# Prerequisites

- **Representation in art** — Supplies questions about purpose, medium and what is communicated.
- **Visual form as structured equivalence** — Offers one lens on required relationships alongside exact quantities and optical appearance.
- **Perceptual simplicity** — Offers regularity/grouping as tools that can aid clarity, not a sufficient or necessary recipe for every task.

# Key Properties

1. **Task-relevant accuracy**: Required structure and exact appearance are both eligible information.
2. **Selection and completeness**: Every view has conditions, but a complete reference or detailed optical record may be the purpose.
3. **Clarity**: Grouping, labels and conventions should expose the needed facts unambiguously.
4. **Domain understanding**: Identify what the intended reader must learn or do.
5. **Available tools**: Simplicity, figure/ground, overlap and lighting can help without guaranteeing comprehension.

# Construction / Recognition

## To Construct/Create:

1. Identify all "task-relevant features" and facts, including structural relations, quantities, text, state and optical appearance where required.
2. Choose a photograph, screenshot, diagram, multiple views or a combined treatment according to those facts.
3. Use labels, grouping, depth cues and suitable conventions to make the facts clear.
4. Inspect whether the intended reader can extract the required information; representative-user checks may be needed.

## To Identify/Recognise:
1. Evaluate: does this diagram/illustration make its structurally relevant properties easy to extract?
2. Identify where ambiguity exists — where the perceptual factors (shape, grouping, overlap) are confusing rather than clarifying.
3. Assess whether the level of detail is appropriate — too much detail obscures the structure; too little fails to communicate it.

# Context & Application

- **Typical contexts**: UX documentation (flow diagrams, wireframes, interaction specs); technical manuals; data visualisation; scientific or medical illustration; system architecture diagrams; infographics.
- **Common applications**: A UI wireframe must communicate layout structure unambiguously (not look pretty); a data visualisation should make the declared quantities and relevant relationships clear; an architecture diagram must communicate component relations without being overwhelmed by implementation detail.

## Cross-Domain Connections

**Engineering → STRUCTURAL**: An API tutorial, architecture diagram and complete reference have different information requirements. Standard conventions and selection can aid a diagram; screenshots can document exact text or state, and a complete reference can legitimately retain all fields. The comparison is task-relevant organization, not a rule that documentation showing everything communicates nothing.

# Examples

The following are reported source examples and interpretations, with their original wording and locators retained for inspection. They are not independently checked historical, experimental or universal claims.

**Example 1** (p. 552): "A medical illustration is meant to distinguish between smooth and rough texture, to show the relative size and position of organs, the network of blood vessels, the mechanism of a joint. A technological picture must give exact proportions and angles, establish the concavity or convexity of a given part, and distinguish between units."

**Example 2** (p. 552–553): "This means not only that the better picture is one that omits unnecessary detail and chooses telling characteristics, but also that the relevant facts must be unambiguously conveyed to the eye. This is done by means of perceptual factors, some of which are discussed in this book: simplicity of shape, orderly grouping, clear overlapping, distinction of figure and ground, use of lighting and perspective to interpret spatial values."

**Example 3** (p. 554–555): "Leonardo da Vinci's scientific drawings are remarkable because he thoroughly understood the structure and function of the things he was depicting and at the same time could organize complex perceptual patterns with the utmost clarity."

# Relationships

These are scoped conceptual reading connections. Prerequisites support understanding rather than assert a universal developmental sequence; related links and contrasts specify comparisons, not causal or subtype laws. Unresolved ordinary comparisons below are not invented card identities.

## Builds Upon
- **Representation in art** — Representation supplies questions about medium and intended content.
- **Visual form as structured equivalence** — Preserved relations are one criterion alongside exact appearance and quantities.
- **Perceptual simplicity** — Regular organization can aid clarity without proving understanding.

## Enables
- **Diagram design** — The method can inform flow charts, system diagrams and wireframes for their actual use.
- **Data visualisation** — Declared quantities and relations need faithful encoding, with suitable task comparisons.

## Related
- **Canonical view** — One or multiple views can be chosen according to the facts required; canonical views are not universal.
- **Levels of abstraction** — Selection must retain what the task needs at any abstraction level.

## Contrasts With
- **Photographic documentation** — Photographs and screenshots can preserve task-relevant exact state, texture and arrangement. A drawing may clarify different facts.
- **Decorative illustration** — Expressive and informational goals can coexist; decoration is not inherently opposed to clarity.

# Common Errors

- **Error**: Assuming photographic screenshots are adequate technical documentation.
  **Correction**: A screenshot can be adequate when exact UI text, appearance or state is required. Layout logic, component hierarchy or interaction flow may need annotation, a diagram or another view; choose from the actual documentation task.

- **Error**: Making diagrams too detailed to be "complete."
  **Correction**: Keep all task-relevant properties, including exact data or appearance. A complete reference may need every field; a focused diagram may omit others. "All reproduction is visual interpretation" does not require deleting information that serves the purpose.

# Common Confusions

- **Confusion**: "Accurate" technical illustration means showing as much detail as possible.
  **Clarification**: Accuracy in technical illustration means correctly communicating the structural properties relevant to the user's task — which often requires omitting photographic detail that would obscure those properties.

# Source Reference

Chapter III: Form, "Art and Visual Perception," pp. 549–556 (Visual Information section).

# Verification Notes

The bullets below preserve historical extraction assertions, including confidence, cross-reference, OCR and source-reading claims; they are not current verification. Original-dependent fidelity remains unassessed. Current technical corrections and analogies establish neither a neural mechanism nor cultural universality or measured usability.

- Definition source: Direct quotes from pp. 552–555; synthesised from surrounding discussion.
- Confidence rationale: High — Arnheim makes an explicit, carefully argued case for these principles with clear examples.
- Uncertainties: The engineering/UX applications are mine; Arnheim discusses medical and scientific illustration, not UI documentation.
- Cross-reference status: Verified within text.
- Rosetta Stone check: Engineering API documentation mapping added as structural.
- OCR issues: None significant.
