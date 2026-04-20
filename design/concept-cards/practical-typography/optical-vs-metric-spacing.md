---
# === CORE IDENTIFICATION ===
concept: Optical vs. Metric Spacing
slug: optical-vs-metric-spacing

# === CLASSIFICATION ===
category: typography
subcategory: type-formatting
tier: advanced
layer: 2-domain

# === PROVENANCE ===
source: "Butterick's Practical Typography"
source_slug: practical-typography
authors: "Matthew Butterick"
chapter: "Text Formatting"
chapter_number: null
pdf_page: null
section: "Metrics vs. Optical Spacing"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "metrics vs optical"
  - "InDesign spacing modes"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - kerning
  - font
extends: []
related:
  - letterspacing
  - typographic-color
  - body-text
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "CQ 5: What are the basic anatomical parts of a letterform (baseline, x-height, cap height, ascender, descender, counter)?"
  - "CQ 12: How do font weight, colour, and spacing work together with font size to create typographic hierarchy — why is size alone insufficient?"

# === VISUAL DESIGN EXTENSIONS ===
rosetta_stone: []
css_implementation: []
---

# Quick Definition

Always use metrics spacing (which preserves the font designer's built-in character widths and kerning); optical spacing applies a patented algorithm that "completely junks" this information and produces uneven body text — reserve it only for emergencies with badly-spaced fonts.

# Core Definition

Butterick, himself a type designer, explains the two InDesign spacing modes: "Metrics spacing relies on the character-spacing information inside the font — that is, the information about character widths and kerning pairs that the font designer put there." Optical spacing, by contrast, "completely junks all this character-spacing information. Instead, it applies a patented spacing algorithm that guesses what the width and kerning of every character should be."

His verdict is unequivocal: "optical spacing will mangle your font. It is akin to putting your finest cashmere sweater in the washing machine."

The deeper principle: "the spacing of a font — that is, the design of the white spaces — is far more consequential to its appearance than the design of the black shapes." Using optical spacing on a professional font means "you're throwing away most of what you paid for."

# Prerequisites

- **Kerning** — Metrics spacing preserves the designer's kerning pairs; optical discards them.
- **Font** — Understanding font internals (spacing tables) is essential context.

# Key Properties

1. **Metrics = designer intent**: Uses spacing and kerning data built into the font.
2. **Optical = synthetic override**: Replaces all spacing with an algorithmic guess.
3. **Asymmetric letters suffer**: Optical does passably with symmetric letters (H, n) but fails with asymmetric ones (a, r, t) that occur frequently.
4. **Accumulation at body size**: Small spacing errors compound across hundreds of letter pairs, making body text "jittery and uneven."
5. **Emergency only**: Use optical only for badly-spaced free fonts or fonts pressed beyond their designed purpose.
6. **Misleading names**: Butterick blames Adobe — "if these options had been named accurately — e.g., 'original spacing' and 'synthetic spacing' — InDesign users would likely have made better choices."

# Construction / Recognition

## To Construct/Create:
1. In InDesign, set spacing to "Metrics" (the default for most setups).
2. Only switch to "Optical" if working with a font that has genuinely bad built-in spacing.
3. If optical is used, judge with your eyes whether it actually helps.

## To Identify/Recognise:
1. Body text that looks jittery or has uneven dark/light spots may be using optical spacing.
2. Compare nu/un pairs: metrics keeps them visually balanced; optical pushes letters unevenly.

# Context & Application

- **Typical contexts**: Adobe InDesign layout work.
- **Common applications**: Book design, magazine layout, any professional typesetting in InDesign.
- **Historical note**: Butterick notes the "optical spacing is better" belief became a cargo cult, possibly spread by Adobe trainers.

# Examples

**Example 1** (metrics-vs-optical-spacing): Enlarged letter pairs showing metrics (balanced nu/un spacing) vs. optical (u pushed left, rounded letters squished closer to flat letters).

**Example 2** (metrics-vs-optical-spacing): "Abuse of optical spacing is especially pronounced among American book designers" while magazine and newspaper designers tend to use metrics.

# Relationships

## Builds Upon
- **Kerning** — Metrics preserves kerning pair data; optical replaces it.
- **Font** — The entire argument rests on respecting font-internal spacing data.

## Related
- **Letterspacing** — Both concern inter-character spacing, but letterspacing is additive while optical is a wholesale replacement.
- **Typographic Color** — The goal of good spacing is even color; optical spacing disrupts it.
- **Body Text** — Spacing errors accumulate most visibly at body text sizes.

# Common Errors

- **Error**: Using optical spacing by default because the name sounds sophisticated.
  **Correction**: "Always use the 'metrics' option." Optical "completely junks" the designer's spacing work.

# Common Confusions

- **Confusion**: Optical spacing improves on the font designer's work.
  **Clarification**: "Humans outperform the machine on font spacing." The algorithm does well with easy symmetric letters but fails on the asymmetric letters that matter most in running text.

# Source Reference

"Metrics vs. Optical Spacing" page. "Text Formatting" chapter.

# Verification Notes

- Definition source: Direct quotes from metrics-vs-optical-spacing.md.
- Confidence rationale: High — strong opinion backed by technical analysis and specific examples.
- Uncertainties: InDesign-specific; not applicable to other tools.
- Cross-reference status: All referenced slugs correspond to existing cards.
- Rosetta Stone check: Checked against 0010 tables. No direct mappings found.
- OCR issues: None — HTML conversion.
