---
concept: "Figure-Ground"
slug: "figure-ground"
category: "visual-perception"
subcategory: "perceptual-organisation"
tier: "foundational"
layer: "0-perception"
source: "Art and Visual Perception: A Psychology of the Creative Eye"
source_slug: "art-and-visual-perception"
authors: "Rudolf Arnheim"
chapter: "V. Space"
chapter_number: 5
pdf_page: 141
section: "Figure and Ground"
extraction_confidence: "high"
aliases:
  - "figure/ground"
  - "positive and negative space"
  - "foreground-background"
prerequisites: []
extends: []
related:
  - "depth-levels"
  - "pictorial-space"
  - "contour-rivalry"
  - "negative-space"
contrasts_with:
  - "depth-levels"
answers_questions:
  - "What is visual hierarchy, and what visual properties (size, colour, contrast, weight, spacing) establish it?"
  - "How do you systematically audit an existing interface for visual design quality? What checklist of principles and patterns do you evaluate, in what order?"
rosetta_stone:
  -
    domain: "engineering"
    concept: "z-index layering (foreground vs background elements)"
    rating: "structural"
    note: "Scoped paint order can support occlusion but does not assign perceptual figure-ground ownership."
  -
    domain: "mathematics"
    concept: "Set partitioning (complementary sets)"
    rating: "structural"
    note: "Given domain Ω and a boundary convention, a selected mask F and Ω\\F partition the domain. This mathematical choice does not determine perceptual ownership or every region’s role."
css_implementation:
  -
    property: "z-index"
    example: "position: relative; z-index: 1; /* scoped paint order; inspect geometry */"
    support: "baseline"
  -
    property: "background-color"
    example: "background-color: var(--surface-ground); /* supply project value and actual foreground pair */"
    support: "baseline"
---

# Quick Definition

Figure-ground describes a perceptual distinction between a bounded, object-like region and a surround experienced as continuing behind it. It is an elementary spatial organization in Arnheim’s account, rather than a binary label imposed on every pixel.

# Core Definition

This presents the represented Arnheim account alongside current analytic qualifications. Original edition, pages, quotations, figures, experiments, physiology and historical claims remain unassessed; the technical constructions below do not certify source fidelity.

Arnheim follows Rubin in describing enclosure, relative size, symmetry, convexity, brightness, orientation and motion as factors that can favor figure character. These are reported contextual tendencies: brighter, redder, smaller or convex regions do not universally win. The goblet/faces reversal and Douris’s interlocking red and black shapes illustrate competing or active region readings. A CSS background can itself become a perceptual figure. A local ground can continue behind a bounded figure without requiring that the physical image domain be infinite.

# Prerequisites

No internal prerequisite is recorded in this extraction. This is a pedagogical entry point, not evidence of innateness or absence of learned contributions.

# Key Properties

1. Contour ownership is a perceptual asymmetry.
2. Ground can be experienced as continuing behind figure.
3. A composition can admit reversals, several levels or unresolved local regions.
4. No recorded prerequisite is evidence of no learning.
5. A mathematical partition can describe an assigned mask but does not decide perception.

# Construction / Recognition

## To Construct/Create:

1. Identify the region that needs to be distinguishable for the task.
2. Use enclosure, spacing, contrast or shape when they help that distinction.
3. Preserve intentional reversals when appropriate.
4. Check text, boundaries and interactions separately from region assignment.

## To Identify/Recognise:

1. Locate candidate bounded regions and surrounds.
2. Ask whether the same contour admits another ownership reading.
3. In an audit, inspect foreground/background separation at actual component states.
4. Distinguish a visible hierarchy cue from a complete hierarchy or accessibility result.

# Context & Application

Cards, text, icons and modal surfaces can use figure-ground organization. A darkened scrim can support a dialog reading, but a dialog also needs semantics, keyboard/focus behavior and content. The card contributes local separation and salience to hierarchy/audit questions, not a full ordered audit or every grouping principle.

## Cross-Domain Connections

**Engineering → STRUCTURAL**: z-index participates in scoped paint order and can support visible occlusion; it does not assign perceptual figure. **Mathematics → STRUCTURAL**: Given an image domain Ω, a chosen mask F and a stated convention assigning boundary points, F and Ω\F partition that domain. This chosen binary model does not prove every image has one such perceptual partition or determine ownership.

# Examples

Source-specific examples and quotations below are retained as reports with their original wording and locators. They are not independently checked historical, experimental or universal claims. Applied examples are qualified design proposals.

**Example 1** (p. 107): "The surrounded surface tends to be seen as figure, the surrounding, unbounded one as ground." — Arnheim paraphrasing Rubin.

**Example 2** (p. 109): The goblet / two-faces ambiguity — the goblet is an enclosed symmetric form; the two facing profiles are the concave negative spaces. Either region can flip to figure.

**Example 3** (p. 180): Douris's Greek cup — the carefully shaped negative black spaces between the figures are strong enough in figure quality to create a continuous interlocking surface of red and black.

**Example 4** (UI): A modal overlay can use a darkened scrim to support a ground reading around a bounded dialog. The actual pair, boundary and reading need inspection; semantics and interaction remain separate.

# Relationships

These are scoped reading connections. Builds Upon supports understanding; Enables names a possible downstream use; Related is an association; Contrasts With names a comparison. They do not establish universal causes, subtypes or verified historical sequences. Ordinary downstream uses are not invented card identities.

## Builds Upon

- Nothing recorded — No internal prerequisite is recorded; this is not a no-learning claim.

## Enables

- **Depth Levels** — Depth levels elaborate a selected figure-ground description.
- **Overlap Depth Cue** — Contour ownership can support front/behind occlusion when geometry permits.
- **Negative Space** — A chosen surrounding region can function as negative space and can also acquire figure quality.
- **Pictorial Space** — A two-plane reading is one elementary pictorial organization.

## Related

- **Contour Rivalry** — Rivalry describes competing ownership of a shared visible boundary.
- **Pictorial Space** — Pictorial space includes shallow figure-ground and other spatial organizations.

## Contrasts With

- **Depth Levels** — The local two-region account is compared with multiple planes; it is not a binary partition theorem for every picture.

# Common Errors

- **Error**: Treating a background as irrelevant.
  **Correction**: Inspect its shape and relation to the figure.

- **Error**: Using colour alone to convey meaning.
  **Correction**: Check actual pairs and provide the labels or other signals needed for the task; no ranking of figure factors replaces that review.

# Common Confusions

- **Confusion**: A foreground CSS element must be figure.
  **Clarification**: Paint order and perceived ownership differ.

- **Confusion**: Figure-ground is always fixed.
  **Clarification**: Reversible readings can be intended or unintended; inspect them in context.

# Source Reference

Chapter V: Space, "Art and Visual Perception," pp. 101–115 (Figure and Ground section, with depth levels discussion extending to p. 120).

# Verification Notes

The bullets below are preserved historical extraction assertions, not current verification. Frozen confidence, cross-reference, source-reading and OCR claims do not settle original-dependent fidelity. Current same-context review supports only the explicitly scoped technical constructions, contextual teaching and local comparisons; it establishes no browser, observer, comfort or physiological result.

- Definition source: Synthesised from discussion in Chapter V (Space), pp. 101–115; direct references to Rubin's rules are cited explicitly by Arnheim
- Confidence rationale: Figure-ground is one of the most extensively discussed concepts in the chapter; Arnheim's account of Rubin's factors is precise
- Uncertainties: Page numbers approximate (chapter begins at pdf_page 141, section on Figure and Ground follows depth levels intro)
- Cross-reference status: Verified
- Rosetta Stone check: Mapping added — z-index is rigorous; mathematical partition is structural
- OCR issues: None significant
