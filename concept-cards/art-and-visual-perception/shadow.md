---
# === CORE IDENTIFICATION ===
concept: Shadow
slug: shadow

# === CLASSIFICATION ===
category: visual-elements
subcategory: light-and-dark
tier: foundational
layer: 0-perception

# === PROVENANCE ===
source: "Art and Visual Perception: A Psychology of the Creative Eye"
source_slug: art-and-visual-perception
authors: "Rudolf Arnheim"
chapter: "VI. Light"
chapter_number: 6
pdf_page: 356
section: "Shadows"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - attached shadow
  - cast shadow
  - drop shadow (design term)

# === TYPED RELATIONSHIPS ===
prerequisites:
  - tonal-value
  - chiaroscuro
extends:
  - chiaroscuro
related:
  - tonal-contrast
  - luminosity
  - depth-cue
contrasts_with:
  - highlight

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How does the visual-elements concept of 'value' (light-dark range) connect to colour theory's 'lightness' and to contrast as a design principle?"
  - "What are the gestalt principles of perceptual grouping, and how does each one work?"

# === VISUAL DESIGN EXTENSIONS ===
rosetta_stone:
  - domain: engineering
    concept: "Box-shadow / drop-shadow filter in CSS"
    rating: structural
    note: "CSS box-shadow and filter drop-shadow implement the perceptual conventions of cast shadow — offset direction, blur radius (edge softness), and opacity correspond to light-source direction, shadow diffuseness, and transparency."

css_implementation:
  - property: "box-shadow"
    example: "box-shadow: 0 4px 12px rgba(0,0,0,0.25); /* cast shadow */"
    support: baseline
  - property: "filter: drop-shadow()"
    example: "filter: drop-shadow(2px 4px 8px rgba(0,0,0,0.3));"
    support: baseline
  - property: "box-shadow (inset, attached)"
    example: "box-shadow: inset 0 2px 8px rgba(0,0,0,0.2); /* attached shadow */"
    support: baseline
---

# Quick Definition

Shadow is the area of reduced brightness created by an object blocking light — either an attached shadow (lying directly on the object, modelling its form) or a cast shadow (thrown from one object onto another, describing spatial relationships and illumination direction).

# Core Definition

Shadow is the darkened area resulting from an object's obstruction of a light source. Arnheim distinguishes two fundamentally different types with distinct perceptual functions:

**Attached shadows** lie on the object itself, created by the object's own form turning away from the light source. They are integral to the object — "so much so that in practical experience it is generally not noted but simply serves to define volume" (Chapter VI, p. 362). Attached shadows are the mechanism of chiaroscuro modelling.

**Cast shadows** are "thrown from one object onto another, or from one part onto another of the same object" (p. 362). They are perceptually an imposition — one object's darkness reaching across to another, describing spatial relationships between them. A cast shadow's edge quality is crucial: "Experiments have shown that attached shadows maintain their character of a transparent film only when their borders are blurred gradients" (p. 363). Hard edges destroy the perceptual shadow quality and make dark areas read as object colour.

Arnheim also discusses the spatial and depth-creating functions of shadows: "Like attached shadows, they define space. A shadow cast across a surface defines it as plane and horizontal or perhaps as crooked and sloping" (p. 364).

# Prerequisites

- **Tonal value** — Shadow is a region of reduced value.
- **Chiaroscuro** — Shadow is the dark component of the chiaroscuro system.

# Key Properties

1. **Two types** — Attached (on the object, models form) vs. cast (from one object to another, describes space).
2. **Transparent film quality** — Perceptually, shadows overlay object colour as a transparent layer; this requires soft, blurred edges.
3. **Depth-creating** — Both types define spatial relationships: attached shadows model volume; cast shadows define surface planes and distance intervals.
4. **Edge quality determines perception** — Soft/blurred shadow edges read as transparent illumination effect; hard edges read as painted dark patches.
5. **Light-direction information** — Cast shadows encode the direction and position of the light source.

# Construction / Recognition

## To Construct/Create:
1. For attached shadows (volume modelling): use gradient transitions, not hard edges. The shadow boundary must be a smooth darkening.
2. For cast shadows: ensure they connect spatially to the casting object (overlap, direction), use soft edges (blur) for diffuse light sources.
3. Shadow colour: in monochromatic work, shadows are simply darker value. In colour work, shadows typically shift toward the complement of the light colour (coloured shadows).
4. In CSS: `box-shadow` with blur radius controls the perceived light diffuseness; hard/zero blur reads as unrealistic; large blur reads as diffuse ambient light.

## To Identify/Recognise:
1. Attached shadow: lies on the object and follows its form; its boundary follows the object's surface curvature.
2. Cast shadow: lies on a different surface from the casting object; its shape is determined by the projecting object and light-source geometry.

# Context & Application

- **Typical contexts**: UI depth cues (material design, neumorphism, card elevation), illustration, photography, product rendering, icon design.
- **Common applications**: Card elevation in UI (drop shadow communicates z-height/depth level); button press state (shadow changes to imply physical press); illustration volume (attached shadows on 3D forms); photography post-processing.

## Cross-Domain Connections

**Engineering → STRUCTURAL**: CSS `box-shadow` is a direct implementation of the cast shadow concept. The parameters map to perceptual shadow properties:
- Offset (x, y) = light source direction
- Blur radius = shadow diffuseness (large blur = diffuse/ambient; zero blur = harsh directional light)
- Spread = shadow size relative to object
- Opacity/colour = shadow density

The perceptual rules for effective shadow (soft edges, correct direction, appropriate opacity) translate directly to CSS parameter choices. Hard-edged shadows (`blur: 0`) violate the "transparent film" principle and read as shape elements rather than depth cues.

# Examples

**Example 1** (p. 362): Arnheim's core distinction — "Attached shadows lie directly on the objects by whose shape, spatial orientation, and distance from the light source they are created. Cast shadows are thrown from one object onto another... Perceptually they are quite different."

**Example 2** (p. 363): Hering's experiment — surrounding a soft shadow with a hard black line converts it from a transparent overlay into an opaque dark patch. The same applies to spotlight shadows vs. diffuse-light shadows.

**Example 3** (p. 364): Cast shadow and spatial definition — the shadow cast across a surface defines that surface as planar/horizontal; it "operates like an additional object creating a ground by lying on it."

**Example 4** (p. 364–365): Mach's Figures (Figure 228) — showing how the presence of a cast shadow rectangle dramatically increases the perceived three-dimensionality of a bar, because the shadow completes the spatial interpretation.

# Relationships

## Builds Upon
- **Tonal value** — Shadow is reduced value; the value scale is the shadow's raw material.
- **Chiaroscuro** — Shadow is the dark component of the chiaroscuro system.

## Enables
- **Depth perception** — Both attached and cast shadows are primary depth cues.
- **Form perception** — Attached shadows make volume and curvature visible.
- **Spatial relationships** — Cast shadows describe the spatial relationships between objects.

## Related
- **Highlight** — The complementary component of the chiaroscuro system (bright = highlight; dark = shadow).
- **Tonal contrast** — Shadow creates the dark pole of tonal contrast.

## Contrasts With
- **Highlight** — Highlight is the brightest area of illuminated form; shadow is the darkest.

# Common Errors

- **Error**: Using hard-edged drop shadows in UI to suggest depth.
  **Correction**: Hard-edged shadows violate the perceptual transparency principle. They read as shapes (dark rectangles) rather than depth cues. Soft, blurred shadows with gentle opacity more effectively suggest z-height.

- **Error**: Making cast shadows the same colour as the object or its complement.
  **Correction**: In most lighting conditions, shadows are a darker, slightly cooler version of the local colour (or of the ambient light's colour). Pure black shadows are rarely perceptually correct.

# Common Confusions

- **Confusion**: "Attached shadows and cast shadows are the same thing."
  **Clarification**: They differ fundamentally in both physical origin and perceptual function. Attached shadows define form; cast shadows define spatial relationships. Conflating them leads to incoherent lighting in illustration or UI.

- **Confusion**: "A shadow should always be black."
  **Correction**: Monochromatic shadows are a convention, not a perceptual truth. Colour work typically uses coloured shadows (often the complement of the light colour) to maintain chromatic organisation and avoid muddying local colours.

# Source Reference

Chapter VI: Light, "Art and Visual Perception," pp. 361–365 (section "Shadows").

# Verification Notes

- Definition source: Synthesised from the "Shadows" section. Arnheim's distinction between attached and cast shadows is explicit and central.
- Confidence rationale: High — the shadow discussion is detailed, with multiple examples and clear perceptual analysis.
- Uncertainties: Arnheim's discussion of shadow symbolism and cultural beliefs (pp. 363–364) is interesting but not included in this card, which focuses on the perceptual/design properties.
- Cross-reference status: Verified — the CSS box-shadow mapping is direct and commonly applicable.
- Rosetta Stone check: Mapping added (engineering: CSS box-shadow, structural).
- OCR issues: None detected.
