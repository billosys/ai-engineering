---
# === CORE IDENTIFICATION ===
concept: Convexity and Concavity in Depth Perception
slug: convexity-concavity-depth

# === CLASSIFICATION ===
category: visual-perception
subcategory: depth-cues
tier: foundational
layer: 0-perception

# === PROVENANCE ===
source: "Art and Visual Perception: A Psychology of the Creative Eye"
source_slug: art-and-visual-perception
authors: "Rudolf Arnheim"
chapter: "V. Space"
chapter_number: 5
pdf_page: 141
section: "Concavity in Sculpture"

# === CONFIDENCE ===
extraction_confidence: medium

# === VARIANTS ===
aliases:
  - convex-concave figure-ground
  - surface curvature depth cue
  - sculptural depth

# === TYPED RELATIONSHIPS ===
prerequisites:
  - figure-ground
  - pictorial-space
extends:
  - figure-ground
related:
  - contour-rivalry
  - negative-space
  - depth-levels
contrasts_with:
  - flat-pictorial-space

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What are the gestalt principles of perceptual grouping, and how does each one work?"

# === VISUAL DESIGN EXTENSIONS ===
rosetta_stone:
  - domain: engineering
    concept: "CSS convex vs. concave UI elements — raised buttons vs. inset fields"
    rating: structural
    note: "Convex UI elements (raised buttons with top-lit shadows) advance perceptually; concave elements (inset text fields, well/inset containers) recede — directly applying the Arnheim/Rubin convex-figure principle."

css_implementation:
  - property: "box-shadow"
    example: "/* Convex (raised): box-shadow: 0 2px 4px rgba(0,0,0,0.2), 0 -1px 0 rgba(255,255,255,0.1) inset; */"
    support: baseline
  - property: "box-shadow (inset)"
    example: "/* Concave (inset): box-shadow: inset 0 2px 4px rgba(0,0,0,0.2); */"
    support: baseline
---

# Quick Definition

Convexity creates figure character — convex surfaces advance, claim contours, and appear solid. Concavity creates ground character — concave surfaces recede, appear passive, and are invaded by surrounding space. This is a fundamental depth cue operating through surface curvature.

# Core Definition

Arnheim establishes that "convexity makes for figure, concavity for ground" (p. 134, 216). This is one of Rubin's figure-ground rules: regions whose contours are convex relative to their enclosed area tend to be perceived as figure; regions whose contours are concave tend to be perceived as ground.

In three-dimensional application (sculpture), Arnheim extends this principle dramatically. Traditional sculpture uses convex forms — the statue "seems to expand and to rise" (p. 238). Modern sculptors (Archipenko, Moore) introduced concavity as a positive sculptural element, giving the surrounding space figure character — "the surrounding space, instead of passively consenting to be displaced by the statue, assumes an active role. It invades the body and seizes the contour surfaces of the concave units" (p. 230).

The perceptual asymmetry: "Convexity and concavity are not only mutually exclusive, they are also opposites dynamically, the one actively expanding, the other passively withdrawing" (p. 85). This dynamic quality is what gives convexity its figure-determining power.

Application to UI: raised buttons (convex form with top-lit shadows) advance perceptually and invite interaction. Inset fields (concave form with inset shadows) recede and signal "container" or "receptacle" quality. This is a direct perceptual consequence of the convexity principle.

# Prerequisites

- **Figure-Ground** — Convexity is one of the figure-determining factors in figure-ground assignment.
- **Pictorial Space** — Convexity signals depth: convex = closer/active; concave = farther/passive.

# Key Properties

1. Convex contours: the enclosed area bulges outward — strong figure character, advancing.
2. Concave contours: the enclosed area scoops inward — weaker figure character, receding, passive.
3. Convexity is active (expanding, claiming space); concavity is passive (withdrawing, receiving space).
4. The shared contour between convex and concave regions creates rivalry (contour rivalry).
5. In sculpture: concavity can be given positive figure quality through deliberate design — the enclosed space acquires "quasi-solidity."
6. In 2D design: convex buttons advance and invite click; concave fields recede and invite entry.

# Construction / Recognition

## To Construct/Create:
1. For advancing, active elements: use convex forms (outward curving edges, rounded shapes).
2. For recessive, receptive elements: use concave forms (inward curving edges, inset treatments).
3. Apply lighting consistently: top-lit shadows reinforce convexity; bottom-lit or inset shadows reinforce concavity.

## To Identify/Recognise:
1. Find contours that curve: do they bulge outward (convex) or inward (concave) from the center of the shape?
2. Convex shapes tend to claim their surrounding contour and advance.
3. Concave shapes tend to feel like holes, receptacles, or empty volumes.

# Context & Application

- **Typical contexts**: Button design, form field design, card design, icon relief, skeuomorphic UI, neumorphic design.
- **Common applications**: Neumorphic design explicitly exploits convexity/concavity: raised elements (convex) use light top shadow + dark bottom shadow; inset elements (concave) reverse this. This mirrors the physical light-from-above convention and the perceptual convex=figure rule. The same principle underlies why inset inputs "feel" like they invite content entry (concave = receptacle).

## Cross-Domain Connections

**Engineering → STRUCTURAL**: CSS `box-shadow` can simulate both convexity and concavity. A raised element uses an outward shadow (larger, diffuse, on the bottom) to suggest it casts a shadow downward (top-lit convex surface). An inset element uses `box-shadow: inset` to suggest the shadow is cast inside the element (top-lit concave surface). This is a direct engineering implementation of the convex/concave depth principle.

# Examples

**Example 1** (p. 134): "Convexity makes for figure, concavity for ground." — Arnheim, citing Rubin's rule.

**Example 2** (p. 85): "Convexity and concavity are not only mutually exclusive, they are also opposites dynamically, the one actively expanding, the other passively withdrawing." — Arnheim

**Example 3** (p. 228): Henry Moore's sculpture — "The convexity of all form in the Maillol preserves an active element in spite of the essentially passive subject matter. In Moore's work a passive and receptive quality is obtained not only through the attitude of the woman, but even more compellingly through the hollowness of shape." — Arnheim

**Example 4** (neumorphic UI): A neumorphic button uses light shadow on top-left and dark shadow on bottom-right to simulate a convex surface raised above the background plane. An inset field reverses this to simulate a concave receptacle. This is a literal perceptual implementation of Arnheim's convexity principle.

# Relationships

## Builds Upon
- **Figure-Ground** — Convexity/concavity are figure-determining factors in figure-ground assignment.

## Enables
- **Active vs. Passive Surface Design** — Convex elements advance, invite, expand; concave elements recede, receive, contain.
- **Tactile UI Affordances** — The convex/concave distinction in UI shadow systems creates implicit affordances.

## Related
- **Contour Rivalry** — Shared boundaries between convex and concave regions are subject to rivalry.
- **Negative Space** — Concave regions in a design often function as negative space.

## Contrasts With
- **Flat Pictorial Space** — Flat design eliminates convexity/concavity depth cues by suppressing shadows.

# Common Errors

- **Error**: Using inset shadows to create "depth" on buttons.
  **Correction**: Inset shadows signal concavity (receptacle quality), not depth/advancement. Buttons should use outward shadows to signal that they advance (convex), inviting press/click. Inset shadows on buttons create a perceptual contradiction — the element appears "pressed" rather than "pressable."

# Common Confusions

- **Confusion**: Concave shapes have no figure quality.
  **Clarification**: Arnheim shows that concavity can acquire strong figure quality through deliberate design (Moore's sculptures, enclosed negative spaces). The key is that the concave form must be bounded and purposefully shaped. Shapeless concave areas remain passive ground.

# Source Reference

Chapter V: Space, "Art and Visual Perception," pp. 130–135, 214–254 (Figure and Ground rules; Concavity in Sculpture section).

# Verification Notes

- Definition source: Synthesised from discussion in Chapter V, primarily the concavity in sculpture section and figure-ground rules
- Confidence rationale: Medium — convexity principle is stated precisely in the context of figure-ground rules; application to sculpture is extended; application to 2D design and UI is my synthesis
- Uncertainties: Arnheim does not discuss UI directly; UI application is an original synthesis
- Cross-reference status: Verified (principles); UI application is synthesised
- Rosetta Stone check: Mapping added — CSS inset/outset shadows is structural
- OCR issues: None significant
