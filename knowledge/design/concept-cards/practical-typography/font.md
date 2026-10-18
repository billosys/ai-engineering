---
concept: "Font"
slug: "font"
category: "typography"
subcategory: "type-elements"
tier: "foundational"
layer: "2-domain"
source: "Butterick's Practical Typography"
source_slug: "practical-typography"
authors: "Matthew Butterick"
chapter: "Font Recommendations"
chapter_number: null
pdf_page: null
section: "Font Basics"
extraction_confidence: "high"
aliases:
  - "typeface"
  - "font family"
prerequisites:
  - "body-text"
extends: []
related:
  - "point-size"
  - "kerning"
  - "opentype-features"
  - "font-pairing"
contrasts_with: []
answers_questions:
  - "CQ 6: What distinguishes a serif typeface from a sans-serif, and what are the historical/functional reasons for each?"
  - "CQ 26: How do you evaluate and select a typeface pairing for a web application? What properties should contrast, and what should harmonise?"
rosetta_stone: []
css_implementation:
  -
    property: "font-family"
    example: "@font-face { font-family: 'MyFont'; src: url('font.woff2'); } body { font-family: 'MyFont', serif; }"
    support: "baseline"
---

# Quick Definition

A font is a resource used to render glyphs and typographic behavior; in current usage “font,” “typeface,” “family,” and “face” can refer to related but distinct things, so inspect the actual supplied resource and available styles.

# Core Definition

Butterick describes fonts as controlling the visual appearance of computer-rendered text and discusses glyph shapes, spacing, kerning, and OpenType features. His static-file analogy distinguishes a font resource from an ordinary end-user application, but should not be read as saying every font contains only inert data: TrueType resources can include instructions interpreted by a rasterizer. A variable font resource may expose multiple instances across axes, so one file per style is not universal.

Butterick recommends professional fonts and argues they outperform system or free fonts. That is his source-era preference, not a requirement or a finding about the project's supplied assets. Price, licensing, distribution, durability, and quality depend on the actual resource and its terms; this card does not make legal or security findings.

# Prerequisites

- **Body Text** — The prepared source treats font choice as one control among those used to shape body text; it does not require a particular acquisition route.

# Key Properties

1. **Resource and terminology**: A font resource supplies glyphs and related data; family, face, style, and file should not be assumed to map one-to-one.
2. **Variable resources**: A single resource can provide multiple axis-defined instances; static files can also provide separate styles.
3. **Features and coverage vary**: Available glyphs, scripts, styles, and OpenType features depend on the actual resource and shaping environment.
4. **Supplied assets come first**: Assess what the project already provides before considering another resource.
5. **Terms are resource-specific**: Check the actual license and permitted uses; no general licensing conclusion follows from “professional,” “free,” or “system.”
6. **No quality guarantee by category**: Price, source, and platform labels do not establish suitability or visual quality.

# Construction / Recognition

## To Construct/Create:
1. Inventory supplied families, files, faces, variable axes, and intended uses.
2. Compare glyph and script coverage, available styles/features, and representative project text.
3. Check the actual license and distribution constraints for the intended use.
4. If a web font is needed, use the project's approved delivery mechanism and a truthful family/resource name; the CSS example below is illustrative, not a bundled asset.

## To Identify/Recognise:
1. Inspect the resource metadata and rendered output rather than inferring a roster from a family name.
2. Check whether requested styles/features are supplied or synthesized in the target environment.

# Context & Application

Fonts are used in print, web, and application rendering. `font.woff2` and `MyFont` in the CSS example are placeholders, not repository assets or a prescribed font choice. This card does not prescribe shopping, installation, hosting, or a font-loading framework.

# Examples

**Example 1** (font-basics): Butterick explains the historical family-versus-instance distinction and observes that technology has changed common usage. Preserve the distinction as useful terminology, not as a rigid universal vocabulary.

**Example 2** (font-basics): The source's price and quality recommendation is an attributed example from its publication context, not a current price or quality guarantee.

# Relationships

## Builds Upon
- **Body Text** — Font resources are one input to body-text rendering; other controls and actual content also matter.

## Enables
- **Font Pairing** — Available resources can be compared for roles when a second face solves a need; pairing is optional.
- **Kerning** — A font may provide kerning data, but actual shaping and spacing depend on the resource and rendering stack; broader endpoint claims are unreviewed here.
- **OpenType Features** — Font resources may expose features; availability and behavior require checking the actual font and application.

## Related
- **Point Size** — Apparent size and metrics interact with the selected resource; the endpoint's broader claims are not accepted by this relationship.

# Common Errors

- **Error**: Rejecting supplied system or free resources by category, or assuming paid fonts are automatically better.
  **Correction**: Compare the actual available resources against content, roles, coverage, features, rendering, and license constraints.

# Common Confusions

- **Confusion**: Every style needs a separate file, or fonts are either ordinary programs or entirely inert data.
  **Clarification**: Static and variable resources differ; a variable resource can expose multiple instances. Some font formats can include instructions used by a rasterizer, but this does not make a font an ordinary end-user application.

# Source Reference

"Font Basics" page. "Font Recommendations" chapter.

# Verification Notes

- Five outcomes: distinguish resource terminology; inventory available faces and axes; check coverage/features on actual text; respect project-supplied assets and actual license terms; treat price/category and file-count claims as non-universal.
- Support: the assigned page discusses fonts, glyphs, spacing, kerning, features, and source recommendations. OpenType variations documentation supports multiple variable instances; TrueType documentation supports the limited instruction-stream qualification.
- Limitation: no actual project font inventory, license review, security review, browser support survey, or rendered comparison was performed.
- The CSS mapping is retained as a baseline illustration with placeholder names; it does not identify a bundled resource.
- Confidence records extraction confidence, not current availability, license, or quality.
- Cross-reference identities and the literal source reference are retained. Original capture fidelity remains a Project10-11 dependency.
