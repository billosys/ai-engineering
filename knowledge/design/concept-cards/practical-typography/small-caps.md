---
concept: "Small Caps"
slug: "small-caps"
category: "typography"
subcategory: "type-formatting"
tier: "intermediate"
layer: "2-domain"
source: "Butterick's Practical Typography"
source_slug: "practical-typography"
authors: "Matthew Butterick"
chapter: "Text Formatting"
chapter_number: null
pdf_page: null
section: "Small Caps"
extraction_confidence: "high"
aliases:
  - "SC"
  - "smcp"
prerequisites:
  - "typographic-emphasis"
  - "font"
extends: []
related:
  - "all-caps"
  - "letterspacing"
  - "kerning"
  - "opentype-features"
  - "typographic-color"
contrasts_with: []
answers_questions:
  - "CQ 12: How do font weight, colour, and spacing work together with font size to create typographic hierarchy — why is size alone insufficient?"
rosetta_stone: []
css_implementation:
  -
    property: "font-variant-caps, font-synthesis"
    example: ".sc { font-variant-caps: small-caps; font-synthesis: none; } /* inspect supplied font support and actual output; no synthetic small caps */"
    support: "baseline"
---

# Quick Definition

Small caps are capital-shaped glyphs designed for use alongside lowercase text; whether genuine forms are available depends on the supplied font, script, and rendering environment.

# Core Definition

Butterick distinguishes designed small caps from mechanically reduced capitals and recommends checking glyph design. CSS `font-variant-caps: small-caps` requests small-cap forms (commonly OpenType `smcp`) but does not guarantee the font provides them. Missing support can lead to synthesized forms. `font-synthesis: none` suppresses synthesis, including bold and oblique as well as small caps; it does not create missing glyphs and may change other requested styles. Check a truthful fallback and inspect the actual text and output. Support is not determined by whether a font is paid or system-supplied.

# Prerequisites

- **Typographic Emphasis** — Small caps can be considered as a visual treatment for a particular task.
- **Font** — Feature availability and glyph design must be checked in the actual font and rendering environment.

# Key Properties

1. **Designed versus scaled forms**: A font may supply dedicated small-cap glyphs; reduced capitals are not proof of genuine forms.
2. **Feature request, not guarantee**: `small-caps` requests lowercase small-cap forms; `all-small-caps` additionally maps capitals to small capitals (`c2sc`).
3. **Synthesis control has wider effects**: `font-synthesis: none` can suppress synthesized bold and oblique as well as caps.
4. **Fallback remains necessary**: Disabling synthesis does not supply missing glyphs or ensure a suitable fallback.
5. **Spacing is contextual**: Butterick recommends tracking and kerning; fixed percentages and universal mandates are not established here.

# Construction / Recognition

## To Construct/Create:
1. Inspect the supplied font's small-cap feature and coverage for the actual script and string.
2. Request the feature only when it is suitable; consider a fallback if the feature is unavailable.
3. If synthetic caps are unacceptable, scope `font-synthesis: none` with awareness that it also affects other styles.
4. Compare actual rendered forms, weight, spacing, and fallback behavior.

## To Identify/Recognise:
1. Do not infer genuine forms from a CSS declaration or a word-processor control.
2. Inspect font support and actual output; the visual appearance alone may not identify how forms were produced.

# Context & Application

Abbreviations, acronyms, headings, and citations are source examples, not universal recommendations. The optional CSS mapping requests small caps and disables synthesis; it does not identify a font or prove glyph support.

# Examples

**Example 1** (small-caps): Butterick compares scaled and designed forms. The prepared illustration is not newly rendered evidence for this review.

**Example 2** (small-caps): A bibliographic citation illustrates one possible use; verify the font feature and actual output before relying on it.

# Relationships

## Builds Upon
- **Typographic Emphasis** — Small caps are one possible visual treatment, not inherently a refined or required option.
- **Font** — The actual font's feature and glyph coverage determine whether genuine forms may be used; paid status is irrelevant.

## Related
- **All Caps** — Small caps and uppercase are distinct treatments; their suitability depends on text and output.
- **Letterspacing** — Tracking may be useful in a particular rendering; no fixed value is required here.
- **Kerning** — Shaping may affect the result; no universal endpoint mandate is accepted here.
- **OpenType Features** — `smcp` is a relevant feature tag; availability and behavior require inspection of the font and application.
- **Typographic Color** — Stroke weight and density can be considered when comparing forms, but visual density is not literal colour contrast.

# Common Errors

- **Error**: Assuming the word-processor button or CSS declaration guarantees genuine small caps.
  **Correction**: Check feature availability, actual string/script, synthesis behavior, fallback, and rendered output.

# Common Confusions

- **Confusion**: `font-synthesis: none` creates real small caps or disables only cap synthesis.
  **Clarification**: It suppresses synthesis across several style categories and does not provide missing glyphs.

# Source Reference

"Small Caps" page. "Text Formatting" chapter.

# Verification Notes

- Five outcomes: distinguish designed and scaled forms; identify the requested OpenType feature; check actual font/script support; understand synthesis suppression and its wider effects; choose fallback and inspect actual output.
- Support: CSS Fonts 4 draft §§6.6 and 2.8 describe feature mapping and synthesis. The specification is a draft and this card claims no browser support survey.
- Limitation: no actual font lacking small caps, real supported font, browser, or output was tested. The prepared comparison image is not newly observed evidence.
- Existing `css_implementation[0].property` and `.example` are corrected to the exact prompt-authorized values; `support` and all other metadata remain frozen.
- Confidence records extraction confidence, not a guarantee of genuine glyphs in any target environment.
- Cross-reference identities and literal source reference are retained. Original capture fidelity remains a Project10-11 dependency.
