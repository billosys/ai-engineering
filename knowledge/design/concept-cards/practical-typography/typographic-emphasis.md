---
concept: "Typographic Emphasis"
slug: "typographic-emphasis"
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
section: "Bold or Italic"
extraction_confidence: "high"
aliases:
  - "bold or italic"
  - "text emphasis"
prerequisites:
  - "body-text"
  - "font"
extends: []
related:
  - "all-caps"
  - "small-caps"
  - "headings"
  - "typographic-color"
contrasts_with: []
answers_questions:
  - "CQ 1: What is visual hierarchy, and what visual properties (size, colour, contrast, weight, spacing) establish it?"
  - "CQ 12: How do font weight, colour, and spacing work together with font size to create typographic hierarchy — why is size alone insufficient?"
  - "CQ 19: A landing page hero section uses a 14px body font, a 16px heading, and a 14px subheading. Why does it feel like nothing stands out?"
rosetta_stone: []
css_implementation:
  -
    property: "font-weight, font-style"
    example: "em { font-style: italic; } strong { font-weight: bold; }"
    support: "baseline"
---

# Quick Definition

Typographic emphasis makes selected content stand out through visual treatment; choose it for the intended meaning and context rather than enforcing a universal bold-versus-italic rule.

# Core Definition

Butterick recommends using bold and italic sparingly and often treats them as alternatives. He favors italic for gentle emphasis in serif text and bold in sans-serif text, but these are source preferences; actual face design, available styles, text, and output determine whether a treatment is distinct. HTML semantics are separate: `em` indicates stress and `strong` indicates importance, seriousness, or urgency. Both can apply to the same phrase, and neither is defined by italic or bold styling.

# Prerequisites

- **Body Text** — Emphasis is perceived in relation to surrounding text and its baseline.
- **Font** — Available styles and actual appearance affect which treatments can be used.

# Key Properties

1. **Purposeful**: Emphasize only content for which a distinction is useful.
2. **Contextual appearance**: Bold, italic, colour, size, or other styling may work differently across faces and output.
3. **Available styles**: Check for a real bold/italic face and how the rendering system handles a missing style.
4. **Semantic distinction**: `em` marks stress; `strong` marks importance, seriousness, or urgency. CSS appearance does not define either meaning.
5. **Combination is possible**: A phrase may legitimately carry both stress and importance; visual bold italic is not prohibited by this card.

# Construction / Recognition

## To Construct/Create:
1. Decide what meaning or hierarchy needs to be communicated.
2. Choose markup for meaning, then choose CSS appearance for the visual task.
3. Compare the treatment with surrounding text using the actual face and content.
4. Check that emphasis remains useful and does not overwhelm longer passages.

## To Identify/Recognise:
1. Ask whether the markup expresses stress or importance, independently of visual appearance.
2. Check that visual emphasis is perceivable and proportionate in the target output.

# Context & Application

Use for words or phrases that need distinction in prose, interfaces, and other text. Butterick's preference for bold over italic in some sans-serif faces is a useful candidate, not a universal font-class rule. Follow the intended medium's semantic and accessibility requirements; no assistive-technology behavior is claimed here.

# Examples

**Example 1** (bold-or-italic): The source's “overemphasizer” illustrates how highlighting every paragraph can remove contrast. It is a rhetorical example, not evidence of retina damage.

**Example 2** (bold-or-italic): The source compares bold and semibold as possible emphasis. Actual distinction depends on the supplied face and rendered result.

# Relationships

## Builds Upon
- **Body Text** — Surrounding text establishes the visual baseline for emphasis.
- **Font** — Available styles and their actual rendering inform possible treatments; serif/sans labels do not determine the strategy.

## Related
- **All Caps** — Another possible treatment for short text; evaluate language and actual output.
- **Small Caps** — A possible treatment when the needed glyph feature is present; synthesis and fallback must be considered.
- **Headings** — Emphasis can contribute to heading appearance, while structure determines heading semantics.
- **Typographic Color** — Weight may affect apparent text-block density; literal colour and contrast are separate checks.

# Common Errors

- **Error**: Assuming italic and bold have fixed semantic meanings, or that all emphasized text must use one style.
  **Correction**: Separate meaning in markup from appearance in CSS and evaluate the actual face and task.

# Common Confusions

- **Confusion**: HTML `em` means italic and `strong` means bold.
  **Clarification**: Those are common visual treatments, not the element meanings. `em` marks stress; `strong` marks importance, seriousness, or urgency.

# Source Reference

"Bold or Italic" page. "Text Formatting" chapter.

# Verification Notes

- Five outcomes: identify the intended meaning; select semantic markup independently; compare available styles; use emphasis proportionately; permit combined stress and importance when both meanings apply.
- Support: the assigned page supports Butterick's attributed preference for restraint and style selection. HTML Standard definitions support the `em`/`strong` meanings.
- Limitation: no face inventory, actual page, accessibility tree, or assistive-technology output was tested. The source's “retina” wording is not adopted as a physiological finding.
- Confidence records extraction confidence, not a guarantee that any visual style communicates the intended meaning.
- Cross-reference identities and literal source reference are retained. Original capture fidelity remains a Project10-11 dependency.
