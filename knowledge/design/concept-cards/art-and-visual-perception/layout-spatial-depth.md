---
# === CORE IDENTIFICATION ===
concept: Spatial Depth in Layout and Interface Design
slug: layout-spatial-depth

# === CLASSIFICATION ===
category: layout-composition
subcategory: depth-and-layering
tier: intermediate
layer: 2-domain

# === PROVENANCE ===
source: "Art and Visual Perception: A Psychology of the Creative Eye"
source_slug: art-and-visual-perception
authors: "Rudolf Arnheim"
chapter: "V. Space"
chapter_number: 5
pdf_page: 141
section: "Application to Painting"

# === CONFIDENCE ===
extraction_confidence: medium

# === VARIANTS ===
aliases:
  - UI depth hierarchy
  - interface layering
  - elevation system

# === TYPED RELATIONSHIPS ===
prerequisites:
  - depth-levels
  - figure-ground
  - overlap-depth-cue
  - atmospheric-perspective
extends:
  - []
related:
  - negative-space
  - depth-levels
  - size-gradient
  - atmospheric-perspective
  - perceptual-transparency
contrasts_with:
  - flat-design

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is visual hierarchy, and what visual properties (size, colour, contrast, weight, spacing) establish it?"
  - "Given a data-rich card (title, status badge, three metrics, timestamp, action button), how do you assign visual hierarchy: what gets the most weight, what gets de-emphasized, and why?"
  - "A dark-mode implementation simply inverts all colours. Text on some backgrounds becomes unreadable. What went wrong?"
  - "How do you systematically audit an existing interface for visual design quality? What checklist of principles and patterns do you evaluate, in what order?"
  - "An admin panel organises its UI by database tables — Users page, Orders page, Products page, each showing all columns in a table. Users complain they can't get their work done efficiently. Diagnose the fundamental mistake and propose the restructuring principle."

# === VISUAL DESIGN EXTENSIONS ===
rosetta_stone:
  - domain: engineering
    concept: "CSS z-index stacking, elevation tokens, shadow scale"
    rating: rigorous
    note: "Design system elevation tokens (0dp to 24dp in Material Design) directly implement depth levels — each elevation value specifies a depth plane with associated shadow rendering."

css_implementation:
  - property: "box-shadow"
    example: "box-shadow: 0 2px 4px rgba(0,0,0,0.1); /* low elevation */ box-shadow: 0 8px 24px rgba(0,0,0,0.2); /* high elevation */"
    support: baseline
  - property: "z-index"
    example: "--z-base: 0; --z-content: 1; --z-nav: 10; --z-modal: 100;"
    support: baseline
  - property: "filter: drop-shadow()"
    example: "filter: drop-shadow(0 4px 8px rgba(0,0,0,0.15));"
    support: baseline
---

# Quick Definition

Spatial depth in layout applies the perceptual principles of pictorial depth to interface and composition design — using overlap, size, shadow, blur, and colour to establish a coherent Z-axis hierarchy that guides attention and communicates element relationships.

# Core Definition

Arnheim's analysis of pictorial space and depth levels in painting maps directly to interface design. His core principle: "In looking at photographs or representational paintings, the viewer is helped somewhat by what he knows about physical space from his own experience. He knows that a large human figure is meant to be closer by than a small house. The artist, however, cannot rely much on mere knowledge. If he wants a figure to stand out against the background, he must use the direct visual effect of perceptual factors" (p. 168).

This applies directly to UI design: the designer cannot rely on users "knowing" that a modal is in front of the page — this must be communicated perceptually through depth cues: shadow, size, blur of background, overlap, higher contrast.

Arnheim's depth relief model: pictorial space is "a continuous relief in which areas at different distances border upon one another" (p. 182). In UI terms, this translates to an elevation system — a systematic set of depth levels with consistent visual treatments.

The depth economy principle: "the number of depth levels in a given pattern is as small as conditions permit" (p. 160). For UI, this means: use the minimum number of distinct elevation levels that communicate the intended hierarchy. Typically 3–5 levels suffice.

Depth and attention: foreground elements (closer depth level) receive more visual weight and attention. The depth hierarchy is therefore also the attention hierarchy — the foreground plane is the primary content plane.

# Prerequisites

- **Depth Levels** — The structural concept that underlies UI elevation systems.
- **Figure-Ground** — The minimal depth relationship: primary content (figure) vs. background (ground).
- **Overlap Depth Cue** — Elements that visually overlap imply depth; used in UI for modals, tooltips, dropdown menus.
- **Atmospheric Perspective** — Background blur/softness (backdrop-filter) implies spatial depth.

# Key Properties

1. Depth levels should be discrete, named, and systematically applied — not ad hoc.
2. Each depth level requires consistent visual treatment: shadow scale, blur, contrast relative to background.
3. The foreground depth level receives the most attention; background levels recede.
4. Dark mode depth requires re-engineering: simple colour inversion breaks depth cues (shadows that work in light mode become invisible or inverted in dark mode).
5. Minimum depth levels: use the fewest that resolve the compositional hierarchy.
6. Depth and visual hierarchy are correlated: what is most important should be on the most foreground plane.

# Construction / Recognition

## To Construct/Create:
1. Define 3–5 named depth levels: background / base surface / raised surface / floating / modal.
2. For each level, specify: shadow scale (dp/blur/opacity), background lightness relative to base, z-index range, any blur (backdrop-filter) treatment.
3. Apply consistently across the entire interface — never override individual component depths without design rationale.
4. For dark mode: redesign shadow and contrast system — do not invert. Shadows in dark mode typically require luminance changes rather than opacity shadows (light surfaces on dark backgrounds).

## To Identify/Recognise (audit):
1. Map all UI elements to depth levels — can you clearly assign each element to a level?
2. Is the depth system consistent? Do all elements at the same depth level have the same shadow/contrast/blur treatment?
3. Are depth cues coherent — does the shadow direction, diffusion, and opacity tell a consistent spatial story?
4. In dark mode: are depth levels still visible? (Shadows on dark backgrounds are often invisible.)

# Context & Application

- **Typical contexts**: Web/mobile UI design systems, component libraries, dashboard design, modal/overlay design, navigation design.
- **Common applications**: Material Design's elevation system (0–24dp), Apple's Human Interface Guidelines layered surface model, Figma's auto-layout and shadow conventions, CSS box-shadow conventions in design tokens.

## Cross-Domain Connections

**Engineering → RIGOROUS**: Material Design's elevation system defines 5 canonical elevation levels (0, 1, 2, 3, 4 in Material 3), each with specific shadow properties. These directly implement Arnheim's depth levels. CSS shadow tokens in a design system are a direct translation of the pictorial depth principles into engineering artifacts.

# Examples

**Example 1** (p. 168): "The artist, however, cannot rely much on mere knowledge. If he wants a figure to stand out against the background, he must use the direct visual effect of perceptual factors." — Arnheim (principle of active depth cueing)

**Example 2** (p. 182): "Pictorial space, therefore, is best described as a continuous relief in which areas at different distances border upon one another." — Arnheim (the depth relief model)

**Example 3** (p. 160): Economy principle: "the number of depth levels in a given pattern is as small as conditions permit." — Arnheim (minimum viable depth complexity)

**Example 4** (UI): A data-rich card containing title, status badge, three metrics, timestamp, and action button requires:
  - Title: most prominent (highest in visual hierarchy = most foreground reading)
  - Status badge: secondary level (elevated above card surface slightly, or high contrast)
  - Metrics: mid-level (same surface as card)
  - Timestamp: recessive (lower contrast, smaller — pushed to background)
  - Action button: elevated (shadow, border — calls attention at foreground level)

**Example 5** (dark mode failure): "A dark-mode implementation simply inverts all colours. Text on some backgrounds becomes unreadable." — This is Arnheim's depth cue failure: shadows (which rely on darker-than-background areas) become lighter-than-background areas when colours are inverted, reversing the depth signal and often reducing contrast to WCAG-failing levels.

# Relationships

## Builds Upon
- **Depth Levels** — The conceptual basis for UI elevation systems.
- **Figure-Ground** — The foundational depth relationship in every UI.
- **Overlap Depth Cue** — Modals, dropdowns, tooltips use overlap to establish depth.
- **Atmospheric Perspective** — Blur, desaturation, and reduced contrast signal background depth levels.

## Enables
- **Consistent Visual Hierarchy** — A depth system creates spatial hierarchy that maps to information hierarchy.
- **Elevation Design Tokens** — Systematic engineering implementation of depth levels.

## Related
- **Negative Space** — Spacing between depth levels.
- **Size Gradient** — Size as depth/hierarchy signal; larger elements are foreground.
- **Perceptual Transparency** — Glass morphism uses transparency to signal depth within a flat design approach.

## Contrasts With
- **Flat Design** — Suppresses all depth cues in favour of purely 2D visual organisation.

# Common Errors

- **Error**: Inventing ad hoc z-index values without a systematic depth level plan.
  **Correction**: Define a named depth level system with z-index ranges before building. This prevents z-index wars and incoherent spatial structures.

- **Error**: Using identical shadow treatment for all elevated elements.
  **Correction**: Different elevation levels need different shadow scales — shadows should grow in spread and softness (and slightly in opacity) with increasing elevation.

- **Error**: Simply inverting light-mode shadows for dark mode.
  **Correction**: Shadows in dark mode must be redesigned. Dark-on-dark shadows are often invisible. Material Design uses surface tint (lighter surface = higher elevation) instead of shadows for dark mode depth.

# Common Confusions

- **Confusion**: Visual hierarchy = depth hierarchy.
  **Clarification**: They are correlated but not identical. Visual hierarchy is about attention order; depth hierarchy is about spatial layering. Foreground depth typically coincides with top of attention hierarchy, but elements can be spatially flat while being visually prominent through size, colour, and contrast.

# Source Reference

Chapter V: Space, "Art and Visual Perception," pp. 154–200 (Depth Levels, Application to Painting sections); applied synthesis with UI design practice.

# Verification Notes

- Definition source: Synthesised and extended from Arnheim's discussion; application to UI design is an original synthesis, not a direct Arnheim claim
- Confidence rationale: Medium — core concepts are from Arnheim; UI application is my synthesis
- Uncertainties: Arnheim does not directly discuss UI design; the mapping is conceptually rigorous but attributable to Arnheim only at the level of source principles
- Cross-reference status: Verified (principles); application synthesised
- Rosetta Stone check: Mapping added — elevation tokens/CSS shadows is rigorous
- OCR issues: None significant
