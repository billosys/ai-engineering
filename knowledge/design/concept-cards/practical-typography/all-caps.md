---
concept: "All Caps"
slug: "all-caps"
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
section: "All Caps"
extraction_confidence: "high"
aliases:
  - "uppercase"
  - "capitalization"
  - "caps"
prerequisites:
  - "typographic-emphasis"
extends: []
related:
  - "small-caps"
  - "letterspacing"
  - "kerning"
  - "headings"
contrasts_with: []
answers_questions:
  - "CQ 1: What is visual hierarchy, and what visual properties (size, colour, contrast, weight, spacing) establish it?"
  - "CQ 12: How do font weight, colour, and spacing work together with font size to create typographic hierarchy — why is size alone insufficient?"
rosetta_stone: []
css_implementation:
  -
    property: "text-transform"
    example: ".caps { text-transform: uppercase; letter-spacing: 0.05em; }"
    support: "baseline"
---

# Quick Definition

All caps presents text with uppercase forms; use it only when it suits the content, script, and design, and distinguish CSS presentation from the underlying text.

# Core Definition

Butterick recommends avoiding long all-caps passages and adding spacing to caps. He attributes a reading difficulty explanation to familiarity and word-shape research, but this card has not independently reviewed cognitive evidence; fatigue, word-shape causation, and universal legibility claims are not established here. CSS `text-transform: uppercase` is a language-sensitive presentation transform and does not rewrite the source text. Case distinctions and mappings vary across scripts and languages.

# Prerequisites

- **Typographic Emphasis** — All caps is one possible visual treatment; its suitability depends on text and context.

# Key Properties

1. **Presentation**: CSS uppercase changes displayed casing without changing the underlying string.
2. **Language-sensitive**: Use correct language metadata and inspect the transformed text, especially where case mappings are not simple.
3. **Contextual length**: Long uppercase passages may be harder to scan for some readers; the assigned source recommends limiting them, but this slice does not establish a universal threshold.
4. **Spacing is a design choice**: Tracking can affect appearance and readability; a fixed 5–12% range is not a universal requirement.
5. **Actual shaping matters**: Kerning and other spacing behavior depend on the font and rendering environment; their presence is not established by a universal caps rule.

# Construction / Recognition

## To Construct/Create:
1. Preserve the authored text and use presentation styling when uppercase display is intended.
2. Set the correct content language and check the actual transformed strings.
3. Compare spacing and shaping on the supplied font and target output.
4. Keep longer passages and non-Latin scripts in the review; do not infer behavior from English samples alone.

## To Identify/Recognise:
1. Check whether displayed uppercase is a style transform or authored uppercase content.
2. Inspect language-specific mappings and the actual spacing result.

# Context & Application

Short labels and headings are common contexts, but there is no universal one-line limit. Judicial or legal statements in the source remain attributed accounts; this card makes no legal finding about conspicuousness.

# Examples

**Example 1** (all-caps): Butterick's all-caps paragraph is a rhetorical demonstration, not a controlled reader-fatigue study.

**Example 2** (all-caps): The source offers rules, a heading, or larger type as alternatives for paragraph emphasis. Evaluate alternatives against the actual task and structure.

# Relationships

## Builds Upon
- **Typographic Emphasis** — All caps is one possible emphasis treatment, not a universal substitute or mandate.

## Related
- **Small Caps** — A distinct glyph feature can be considered for appropriate text; it is not simply a universally superior all-caps treatment.
- **Letterspacing** — Tracking may be adjusted for a particular string and font; the endpoint's broader requirements are unreviewed here.
- **Kerning** — Kerning may affect a particular rendering; the endpoint's broader mandates are unreviewed here.
- **Headings** — Caps can be used in headings; Butterick's advice against them is contextual rather than a ban.

# Common Errors

- **Error**: Treating CSS uppercase as a rewrite of the source string or assuming one mapping works identically for every language.
  **Correction**: Use language-sensitive text transformation and inspect the actual result.

# Common Confusions

- **Confusion**: Capitalization alone makes content conspicuous or more readable.
  **Clarification**: Appearance and reader response depend on context, wording, script, font, spacing, and output; this slice does not establish a universal effect.

# Source Reference

"All Caps" page. "Text Formatting" chapter.

# Verification Notes

- Five outcomes: distinguish source text from display transform; check language-sensitive mapping; evaluate actual strings and scripts; choose spacing from the actual font/output; attribute source cognitive and legal explanations rather than presenting them as proven findings.
- Support: CSS Text 3 §2.1 describes language-sensitive transformations that do not alter underlying content. Butterick recommends restraint and spacing.
- Limitation: no cognitive study, legal research, browser survey, or rendered comparison was performed. The 5–12% tracking rule and mandatory kerning are not adopted.
- Confidence records extraction confidence, not a universal readability result.
- Cross-reference identities and literal source reference are retained. Original capture fidelity remains a Project10-11 dependency.
