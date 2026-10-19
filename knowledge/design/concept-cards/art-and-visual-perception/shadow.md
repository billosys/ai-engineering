---
concept: "Shadow"
slug: "shadow"
category: "visual-elements"
subcategory: "light-and-dark"
tier: "foundational"
layer: "0-perception"
source: "Art and Visual Perception: A Psychology of the Creative Eye"
source_slug: "art-and-visual-perception"
authors: "Rudolf Arnheim"
chapter: "VI. Light"
chapter_number: 6
pdf_page: 356
section: "Shadows"
extraction_confidence: "high"
aliases:
  - "attached shadow"
  - "cast shadow"
  - "drop shadow (design term)"
prerequisites:
  - "tonal-value"
  - "chiaroscuro"
extends:
  - "chiaroscuro"
related:
  - "tonal-contrast"
  - "luminosity"
  - "depth-cue"
contrasts_with:
  - "highlight"
answers_questions:
  - "How does the visual-elements concept of 'value' (light-dark range) connect to colour theory's 'lightness' and to contrast as a design principle?"
rosetta_stone:
  -
    domain: "engineering"
    concept: "Box-shadow / drop-shadow filter in CSS"
    rating: "structural"
    note: "CSS box-shadow is box-based and drop-shadow uses an alpha silhouette. Offsets and blur can suggest a lighting convention without calibrated geometry, universal edge rules or a guaranteed depth percept."
css_implementation:
  -
    property: "box-shadow"
    example: "box-shadow: 0 4px 12px rgba(0,0,0,0.25); /* optional box-based cast-shadow convention */"
    support: "baseline"
  -
    property: "filter: drop-shadow()"
    example: "filter: drop-shadow(2px 4px 8px rgba(0,0,0,0.3));"
    support: "baseline"
  -
    property: "box-shadow (inset, attached)"
    example: "box-shadow: inset 0 2px 8px rgba(0,0,0,0.2); /* inset box treatment, not a full lighting model */"
    support: "baseline"
---

# Quick Definition

A shadow is a reduced-illumination region associated with occlusion or surface orientation. Attached and cast shadows can suggest form or spatial relations, but depicted shadows can also be stylised, misleading or purely expressive.

# Core Definition

This presents the represented Arnheim account. Exact edition, pages, quotations, named examples, figures, experiments, historical claims and physiological explanations remain unassessed against the unavailable original. Current analytic qualifications do not certify source fidelity.

Shadow is the darkened area resulting from an object's obstruction of a light source. Arnheim distinguishes two fundamentally different types with distinct perceptual functions:

**Attached shadows** lie on the object itself, created by the object's own form turning away from the light source. They are integral to the object — "so much so that in practical experience it is generally not noted but simply serves to define volume" (Chapter VI, p. 362). Attached shadows are the mechanism of chiaroscuro modelling.

**Cast shadows** are "thrown from one object onto another, or from one part onto another of the same object" (p. 362). They are perceptually an imposition — one object's darkness reaching across to another, describing spatial relationships between them. The represented discussion of edge quality includes an attached-shadow statement: "Experiments have shown that attached shadows maintain their character of a transparent film only when their borders are blurred gradients" (p. 363). That reported experiment concerns attached-shadow transparency under a particular border manipulation. It does not prove that all hard cast-shadow edges read as paint: point-like illumination can produce sharp shadows.

Arnheim also discusses the spatial and depth-creating functions of shadows: "Like attached shadows, they define space. A shadow cast across a surface defines it as plane and horizontal or perhaps as crooked and sloping" (p. 364).

# Prerequisites

- **Tonal value** — Supplies light-dark comparison.
- **Chiaroscuro** — Supplies a pictorial context elaborated by attached/cast-shadow distinctions.

# Key Properties

1. **Attached/cast** — Attached shading follows a surface; cast shadows relate occluder, source and receiving surface.
2. **Transparency reading** — Surface and lighting can be perceived together without physical transmission.
3. **Conditional depth cue** — A depicted shadow can suggest relations without calibrating distance or z-height.
4. **Edge conditions** — Softness depends on source extent, geometry and materials; a point source can cast a hard shadow.
5. **Direction** — A shadow can suggest light direction under a model, but a CSS offset is not a recovered source position.

# Construction / Recognition

## To Construct/Create:
1. For an attached-shadow study, compare the surface orientation and intended lighting; soft transitions can model a rounded form.
2. For a cast shadow, choose source extent/direction and receiving geometry; sharp and diffuse cases are both possible.
3. Choose colours for material, illumination and intended expression. A cooler shadow or light-colour complement is not universally required.
4. Use CSS box-shadow for a box-based effect or drop-shadow() for an alpha silhouette; parameters illustrate a convention rather than simulate full light transport.

## To Identify/Recognise:
1. Locate the object, receiving surface and suggested source.
2. Separate observed appearance from measured geometry; a painted shadow shape can create or contradict a depth reading.

# Context & Application

Illustration, photography and UI may use shadows, flat borders or calm surfaces. A shadow can reinforce a layer or pressed treatment, but must not be the sole cue to input state or semantic priority. Resolve actual text/control pairs independently; no blur radius establishes distance or accessibility.

## Cross-Domain Connections

**Engineering → STRUCTURAL**: CSS shadows are engineered image effects. Offset suggests a direction; blur/spread/colour affect the rendered shape. Box-shadow is box-based, drop-shadow() uses the filtered alpha silhouette, and inset is a box treatment rather than a complete attached-lighting model. Neither zero blur nor soft blur uniquely determines realistic lighting, perceptual transparency or z-height.

# Examples

These are retained reported examples from the existing extraction, not independently verified quotations, figures, experiments or historical conclusions.

**Example 1** (p. 362): Arnheim's core distinction — "Attached shadows lie directly on the objects by whose shape, spatial orientation, and distance from the light source they are created. Cast shadows are thrown from one object onto another... Perceptually they are quite different."

**Example 2** (p. 363): Hering's experiment — surrounding a soft shadow with a hard black line converts it from a transparent overlay into an opaque dark patch. This border manipulation does not classify all spotlight/diffuse shadows; source extent and geometry matter.

**Example 3** (p. 364): Cast shadow and spatial definition — the shadow cast across a surface defines that surface as planar/horizontal; it "operates like an additional object creating a ground by lying on it."

**Example 4** (p. 364–365): Mach's Figures (Figure 228) — showing how the presence of a cast shadow rectangle dramatically increases the perceived three-dimensionality of a bar, because the shadow completes the spatial interpretation.

# Relationships

## Builds Upon
- **Tonal value** — Supplies light-dark comparison.
- **Chiaroscuro** — A pictorial context this card elaborates; shadow is not merely a subtype of that technique.

## Enables
- **Depth perception** — Shadow is one cue among several.
- **Form perception** — Attached shading can suggest curvature.
- **Spatial relationships** — Cast shadows can connect object and receiving surface under a chosen interpretation.

## Related
- **Highlight** — Local depiction/illumination-feature construct: a relatively bright illuminated region, not necessarily specular or physically calibrated.
- **Tonal contrast** — A shadow can provide one darker region.

## Contrasts With
- **Highlight** — Compares darker shading with a relatively bright region; local extrema are contextual, not always absolute darkest/brightest values.

# Common Errors

- **Error**: Using hard-edged drop shadows in UI to suggest depth.
  **Correction**: A hard edge can be coherent for a point-like source or expressive style. Inspect actual geometry and intent; softness alone does not establish depth.

- **Error**: Making cast shadows the same colour as the object or its complement.
  **Correction**: There is no universal alternative recipe. Consider surface, ambient illumination, source spectrum and the chosen rendering or pigment operation.

# Common Confusions

- **Confusion**: "Attached shadows and cast shadows are the same thing."
  **Clarification**: Attached shading models a surface's orientation; cast shadows arise from occlusion onto a receiving region, which can be another part of the same object.

- **Confusion**: "A shadow should always be black."
  **Clarification**: Black and coloured shadows are both choices. Physical colour depends on materials and illumination; pictorial work may choose either for expression.

# Source Reference

Chapter VI: Light, "Art and Visual Perception," pp. 361–365 (section "Shadows").

# Verification Notes

Current bounded review separates appearance, model coordinates and rendering operations as explained above. Technical corrections and local relationship/CQ decisions are same-context proposals; original fidelity and actual rendered/observer outcomes remain unassessed. Extraction-confidence metadata is unchanged.

Legacy extraction notes below are preserved as historical assertions from the predecessor card, **not current verification results**. In particular, their equivalence, chronology, physiology and “Verified” claims are not adopted by this review.

- Definition source: Synthesised from the "Shadows" section. Arnheim's distinction between attached and cast shadows is explicit and central.
- Confidence rationale: High — the shadow discussion is detailed, with multiple examples and clear perceptual analysis.
- Uncertainties: Arnheim's discussion of shadow symbolism and cultural beliefs (pp. 363–364) is interesting but not included in this card, which focuses on the perceptual/design properties.
- Cross-reference status: Verified — the CSS box-shadow mapping is direct and commonly applicable.
- Rosetta Stone check: Mapping added (engineering: CSS box-shadow, structural).
- OCR issues: None detected.
