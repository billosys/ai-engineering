---
# === CORE IDENTIFICATION ===
concept: Depth Levels
slug: depth-levels

# === CLASSIFICATION ===
category: visual-perception
subcategory: spatial-organisation
tier: intermediate
layer: 0-perception

# === PROVENANCE ===
source: "Art and Visual Perception: A Psychology of the Creative Eye"
source_slug: art-and-visual-perception
authors: "Rudolf Arnheim"
chapter: "V. Space"
chapter_number: 5
pdf_page: 141
section: "Depth Levels"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - spatial planes
  - depth planes
  - pictorial layers

# === TYPED RELATIONSHIPS ===
prerequisites:
  - figure-ground
  - overlap-depth-cue
  - pictorial-space
extends:
  - figure-ground
related:
  - overlap-depth-cue
  - transparency-perceptual
  - negative-space
contrasts_with:
  - figure-ground

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What are the gestalt principles of perceptual grouping, and how does each one work?"
  - "What is visual hierarchy, and what visual properties (size, colour, contrast, weight, spacing) establish it?"
  - "A dark-mode implementation simply inverts all colours. Text on some backgrounds becomes unreadable. What went wrong?"
  - "Given a data-rich card (title, status badge, three metrics, timestamp, action button), how do you assign visual hierarchy: what gets the most weight, what gets de-emphasized, and why?"
  - "How do you systematically audit an existing interface for visual design quality? What checklist of principles and patterns do you evaluate, in what order?"

# === VISUAL DESIGN EXTENSIONS ===
rosetta_stone:
  - domain: engineering
    concept: "CSS stacking context / z-index layers"
    rating: rigorous
    note: "CSS stacking contexts directly implement depth levels: each z-index value corresponds to a discrete depth plane, and elements at the same z-index share a depth level."
  - domain: engineering
    concept: "Layered architecture in UI (DOM tree, stacking contexts, compositing layers)"
    rating: rigorous
    note: "The browser rendering pipeline's compositing layers are a direct implementation of depth levels — each composited layer corresponds to one depth plane in the pictorial stack."

css_implementation:
  - property: "z-index"
    example: "z-index: 0; /* ground */ z-index: 1; /* content */ z-index: 100; /* overlay */"
    support: baseline
  - property: "isolation: isolate"
    example: "isolation: isolate; /* creates new stacking context = new depth level */"
    support: baseline
---

# Quick Definition

Depth levels are the discrete planes at different distances from the viewer that together constitute the spatial organisation of a picture. They extend the figure-ground concept from two planes to multiple overlapping layers, each with its own depth position.

# Core Definition

Arnheim extends figure-ground to the broader concept of depth levels: "It seems more adequate to speak of patterns distributed over a number of depth levels, the basic figure-ground pattern being a special case, namely an organization of only two levels" (p. 158).

Key structural principle: the visual system prefers the minimum number of depth levels needed to accommodate the pattern. This is the "principle of economy": "there is a tendency to simplification by economy, which means that the number of depth levels in a given pattern is as small as conditions permit" (p. 160). A circle on a square is perceived as a perforated square (two levels) rather than a disk on top of a square (three levels), because two levels is simpler.

Pictorial space can therefore be described as a "depth relief" — an ordered arrangement of planes at different distances. The relief can be:
- Shallow or deep
- Working with few distance values or many
- Using steep intervals (foreground-background jump) or gradual chromatic scales of fine steps

This spatial structure is the fundamental unit of compositional depth analysis.

# Prerequisites

- **Figure-Ground** — Depth levels extend figure-ground to the multi-plane case.
- **Overlap Depth Cue** — The primary mechanism by which depth levels are established between adjacent planes.
- **Pictorial Space** — Depth levels are the structural description of pictorial space.

# Key Properties

1. Minimum levels principle: the visual system prefers the fewest depth levels that resolve visual tensions adequately.
2. Any element can simultaneously be figure to the plane behind it and ground for elements in front of it.
3. The depth relief of a picture can be characterised by: number of levels, steepness of transitions, range (shallow vs. deep), and symmetry (frontal vs. receding).
4. Pictorial space is best described as a "continuous relief" — depth levels shade into one another rather than being absolutely discrete.
5. The number and arrangement of depth levels is a primary tool for compositional expression and hierarchy.

# Construction / Recognition

## To Construct/Create:
1. Identify the minimum number of planes needed to resolve all visual tensions (overlapping shapes, figure-ground ambiguities).
2. Assign each element to a depth level, with foreground elements assigned lower levels (nearer) and background elements higher levels (farther).
3. Control depth level transitions: steep transitions (large depth jumps) create dramatic spatial contrast; gradual transitions create spatial flow.
4. Avoid unnecessary depth levels — each additional level increases spatial complexity.

## To Identify/Recognise:
1. List all elements and ask: which are in front of which?
2. Group elements at the same perceived depth into shared levels.
3. Count levels: how many distinct depth planes are there?
4. Assess transitions: are level changes abrupt (overlap) or gradual (atmospheric gradient)?

# Context & Application

- **Typical contexts**: UI layout hierarchy, illustration composition, photography, web page spatial structure, data visualisation layering.
- **Common applications**: In UI design, depth levels correspond to z-index stacking: background (level 0), content (level 1), navigation (level 2), overlays/modals (level 3+). Each level should have consistent visual treatment (contrast, shadow, blur) to maintain spatial legibility. In data visualisation, primary data is foreground (level 0), secondary data is mid-level (level 1), grid/background is rear (level 2).

## Cross-Domain Connections

**Engineering → RIGOROUS**: CSS z-index stacking contexts implement depth levels directly. Each integer z-index value defines a depth plane. The browser's compositing engine renders these planes in depth order. `isolation: isolate` creates a new stacking context (a new depth level sub-system) — exactly matching Arnheim's observation that depth levels can be nested and locally self-contained.

# Examples

**Example 1** (p. 158): "It seems more adequate to speak of patterns distributed over a number of depth levels, the basic figure-ground pattern being a special case, namely an organization of only two levels." — Arnheim

**Example 2** (p. 160): Disk on square — "The principle of economy would of course favour a one-plane solution as the simplest. This leaves us with a smaller number of planes—that is, with a spatially simpler pattern." — Arnheim

**Example 3** (p. 164): The Arp woodcut analysis — Arnheim describes how the same image can be perceived as a 1-, 2-, 3-, or 4-plane depth arrangement depending on which perceptual factors dominate.

**Example 4** (p. 182): "Pictorial space, therefore, is best described as a continuous relief in which areas at different distances border upon one another." — Arnheim

**Example 5** (UI): A web page typically has: background/wallpaper (level -1), page body (0), sticky header (1), dropdown menu (2), modal scrim (99), modal dialog (100), tooltip (200). This z-index scale is a direct specification of depth levels.

# Relationships

## Builds Upon
- **Figure-Ground** — Depth levels are the generalisation of figure-ground to N planes.
- **Overlap Depth Cue** — Overlap is the primary mechanism creating boundaries between depth levels.
- **Pictorial Space** — Depth levels are the structural vocabulary for describing pictorial space.

## Enables
- **Visual Hierarchy** — Depth levels create hierarchy: foreground elements are more salient than background elements.
- **Spatial Organisation** — The arrangement of depth levels is the fundamental structure of compositional depth.

## Related
- **Perceptual Transparency** — A case where two depth levels share the same spatial location and both remain visible.
- **Negative Space** — The spaces between depth level elements; the "ground" in each layer pair.

## Contrasts With
- **Figure-Ground** — Figure-ground is the two-level special case; depth levels is the general N-level concept. In figure-ground, one plane must be unbounded; in depth levels, all planes can be bounded and shaped.

# Common Errors

- **Error**: Assigning arbitrary z-index values without a coherent depth level system.
  **Correction**: Define a small number of named depth levels (base, content, floating, overlay, critical) with specific z-index ranges. This prevents the common "z-index war" where developers increment z-index arbitrarily, producing an incoherent depth structure.

- **Error**: Using too many depth levels, creating unnecessary spatial complexity.
  **Correction**: Arnheim's economy principle applies: use the minimum number of depth levels that resolves the visual tensions. Typically 3–5 levels suffice for most UI compositions.

# Common Confusions

- **Confusion**: Depth levels = z-index integer values.
  **Clarification**: Depth levels are perceptual concepts — groupings of elements perceived at the same spatial distance. Z-index integer values implement depth levels but are not identical to them. Multiple elements can share a depth level with very different z-index values if they are in different stacking contexts.

- **Confusion**: More depth levels = more spatial richness.
  **Clarification**: Excessive depth levels increase complexity and cognitive load. The economy principle suggests spatial clarity comes from using the minimum viable number of depth levels.

# Source Reference

Chapter V: Space, "Art and Visual Perception," pp. 154–198 (Depth Levels section and Application to Painting).

# Verification Notes

- Definition source: Synthesised from discussion in Chapter V (Space), pp. 154–198; key quote cited directly
- Confidence rationale: High — Arnheim devotes an extended section to depth levels and gives precise examples
- Uncertainties: None significant
- Cross-reference status: Verified
- Rosetta Stone check: Mappings added — CSS stacking context is rigorous
- OCR issues: None significant
