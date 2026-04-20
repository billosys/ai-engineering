---
concept: Ratio Selection Criteria
slug: ratio-selection-criteria
category: typography
subcategory: type-scale
tier: intermediate
layer: 2-domain
source: "More Meaningful Typography"
source_slug: posts
authors: "Tim Brown"
chapter: "Creating a modular scale for web design"
chapter_number: null
pdf_page: null
section: null
extraction_confidence: medium
aliases:
  - [choosing a scale ratio, ratio selection, ratio justification]
prerequisites:
  - scale-ratio
  - modular-scale
extends:
  - scale-ratio
related:
  - golden-ratio
  - musical-interval-typographic-ratio
  - modular-scale-construction
contrasts_with:
  - []
answers_questions:
  - "How do you select an appropriate scale ratio for a given design context?"
  - "What makes a type hierarchy feel harmonious vs arbitrary?"
rosetta_stone: []
css_implementation: []
---

# Quick Definition

Ratio selection criteria are the considerations that guide choosing a specific scale ratio: the ratio should be meaningful to the project's design, content, cultural context, and historical associations \u2014 not chosen for computational convenience.

# Core Definition

Brown does not provide a single exhaustive list of ratio selection criteria, but he articulates the principle clearly through his own example: "So it makes sense that modular scales are most effective when the inputs\u2014the starting ratios and starting numbers that beget the entire scale\u2014are meaningful to a project's design, content, or both."

He then demonstrates this in practice: "I chose the golden mean (1:1.618). It is a beautiful proportion with historical and cultural connections that make sense for the typefaces I've chosen and the text I'm setting." His justification is three-part: (1) aesthetic ("beautiful proportion"), (2) historical (Renaissance page proportions; Minion's Renaissance roots), and (3) content-contextual (his text is about typographic tradition and "looking to tradition for guidance").

The article also implicitly establishes a negative criterion: ratios should not be chosen because they are "easily divisible" or because they match "viewport limitations du jour." Brown writes: "Viewport sizes are good to know, but setting a composition's width to one of these exact values...is not ideal. Easily divisible numbers are only good for being easily divisible."

The broader context of the article suggests the full menu of ratio candidates includes: the golden ratio; musical interval ratios (implied by Bringhurst's framing and Brown's subtitle referencing "ratios rooted in geometry, music, nature, and history"); and geometric proportions from architecture, nature, or historical design.

# Prerequisites

- **Scale ratio** \u2014 Understanding what a ratio is and how it generates a scale.
- **Modular scale** \u2014 Understanding what the ratio is being selected for.

# Key Properties

1. **Contextual fit**: The ratio should resonate with the project's subject matter, audience, and design intent.
2. **Cultural/historical grounding**: Ratios with established use in art, architecture, music, or typographic tradition carry legible meaning beyond their mathematical value.
3. **Typographic fit**: The ratio should suit the typefaces chosen \u2014 a Renaissance humanist typeface invites ratios from Renaissance design practice.
4. **Contrast calibration**: The numeric value of the ratio determines how dramatically each scale step differs from the next \u2014 this should match the desired degree of hierarchical contrast in the design.

# Construction / Recognition

## To Construct/Create:
1. Identify the project's cultural, historical, and aesthetic context.
2. Identify the typefaces being used and their design lineage.
3. Consider the subject matter of the content.
4. From these, derive which domain (music, geometry, natural growth, historical design) provides the most contextually relevant proportions.
5. Select a ratio from that domain: golden ratio for classical/Renaissance contexts; musical interval ratios for harmonic/editorial contexts; etc.
6. Verify the ratio produces scale steps with the right degree of contrast for the hierarchy needed.

## To Identify/Recognise:
1. Ask: does the designer provide a stated justification for the ratio choice?
2. Ask: does the ratio correspond to a known harmonic, geometric, or culturally established proportion?
3. Ask: does the ratio produce scale steps that match the design's hierarchical needs?

# Context & Application

- **Typical contexts**: Initial stage of modular scale construction; design system documentation; type system rationale.
- **Common applications**: Justifying ratio choices in design documentation; selecting from a menu of ratios at modularscale.com.
- **Historical/stylistic notes**: The article's opening invokes "ratios rooted in geometry, music, nature, and history" as the full candidate set. Brown's example demonstrates the selection process in detail for one specific ratio (\u03c6). The article does not work through other ratio choices explicitly.

# Examples

**Example 1** (from source, "Creating a modular scale for web design"): "I chose the golden mean (1:1.618). It is a beautiful proportion with historical and cultural connections that make sense for the typefaces I've chosen and the text I'm setting. Although it is a contemporary design, Minion draws upon Renaissance ideals, in everything from its humanist structure to the ways in which parts of letters reveal a history in pen and ink. Page and textblock proportions in Renaissance works were based on the golden mean, too, and because the subject of my text is about the craft of typesetting and looking to tradition for guidance, it made sense to use a proportion meaningful to our typographic roots."

**Example 2** (from source, opening): "This and other meaningful ratios rooted in geometry, music, nature, and history can be expressed as modular scales and put to work on the web." \u2014 establishes the candidate set.

# Relationships

## Builds Upon
- **Scale ratio** \u2014 Selection criteria presuppose knowing what a ratio is.

## Enables
- **Modular scale construction** \u2014 The construction procedure requires a ratio; these criteria guide which ratio to choose.

## Related
- **Golden ratio** \u2014 The specific ratio selected in the article's worked example; the selection process is documented in detail.
- **Musical interval \u2194 typographic ratio** \u2014 Provides the full table of harmonically grounded ratio candidates (beyond \u03c6).

## Contrasts With
- **Arbitrary ratio selection** \u2014 Choosing a ratio for computational convenience or habit rather than contextual fit.

# Common Errors

- **Error**: Selecting a ratio because it is the same one used in a tutorial or a famous example, without considering whether it fits the current project.
  **Correction**: "It is a beautiful proportion with historical and cultural connections that make sense for the typefaces I've chosen and the text I'm setting" \u2014 the justification is specific to this project. Different projects warrant different ratios.

- **Error**: Selecting ratio based only on the visual output of the scale without articulating the contextual rationale.
  **Correction**: The ratio should be justifiable in terms of design, content, and cultural context \u2014 not just "it looks right."

# Common Confusions

- **Confusion**: Any ratio will produce a valid modular scale, so the specific choice doesn't matter much.
  **Clarification**: The scale is only as meaningful as its ratio. An arbitrary ratio produces a sequence of numbers that relate mathematically but carry no cultural or historical resonance \u2014 which Brown distinguishes from "meaningful" ratios that achieve "a visual harmony not found in layouts that use arbitrary, conventional, or easily divisible numbers."

# Source Reference

"Creating a modular scale for web design" \u2014 More Meaningful Typography, Tim Brown (A List Apart, May 2011)

# Verification Notes

- Definition source: Synthesised from Brown's ratio justification in the worked example and the article's opening framing.
- Confidence rationale: Medium \u2014 the criteria are implicit and demonstrated rather than explicitly enumerated. The worked example gives one clear data point (\u03c6 for Renaissance humanist context) but does not systematically compare alternatives.
- Uncertainties: The article does not address what to do when no single ratio fits all contextual factors, or how to trade off competing considerations. The full menu of candidate ratios (musical intervals, geometric proportions) is referenced in the opening but not elaborated.
- Cross-reference status: Verified within source; musical interval candidates require cross-reference to Brown's broader work (modularscale.com, "More Perfect Typography" talk).
- Rosetta Stone check: No mappings \u2014 the criteria themselves are a design judgment framework, not a cross-domain concept.
- OCR issues: None significant.
