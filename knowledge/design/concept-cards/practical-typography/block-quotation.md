---
concept: "Block Quotation"
slug: "block-quotation"
category: "typography"
subcategory: "type-elements"
tier: "intermediate"
layer: "2-domain"
source: "Butterick's Practical Typography"
source_slug: "practical-typography"
authors: "Matthew Butterick"
chapter: "Page Layout"
chapter_number: null
pdf_page: null
section: "Block Quotations"
extraction_confidence: "high"
aliases:
  - "block quote"
  - "extract"
  - "long quotation"
prerequisites:
  - "body-text"
  - "point-size"
  - "line-spacing"
extends: []
related:
  - "first-line-indent"
  - "line-length"
contrasts_with: []
answers_questions:
  - "CQ 1: What is visual hierarchy, and what visual properties (size, colour, contrast, weight, spacing) establish it?"
  - "CQ 13: How does the relationship between inter-group and intra-group spacing communicate which elements belong together (gestalt proximity)?"
rosetta_stone: []
css_implementation:
  -
    property: "margin, font-size, line-height"
    example: "blockquote { margin-block: 1em; margin-inline: 2em; font-size: inherit; line-height: inherit; } /* illustrative; reduce indents when space is tight */"
    support: "baseline"
---

# Quick Definition

A block quotation presents quoted material separately from surrounding prose. Its visual distinction should preserve readability and quotation accuracy; it is not defined by smaller type or a fixed indent.

# Core Definition

Butterick suggests slightly reducing point size and leading, with a left indent of 0.5–1 inch in print or about 2–5 ems on the web, optionally on both sides. He also says to avoid making the line too short and recognizes that accuracy may demand extensive quotation. These are contextual formatting suggestions, not universal requirements.

His writer/reader contrast warns that a large extract intended to signal importance may instead look like unintegrated material. It is his editorial argument, not evidence that readers always skip blocks or that a summary preserves the original evidence. Introduce the quotation, preserve its meaning and context, and retain its full extent when the task requires exact wording.

In [HTML](https://html.spec.whatwg.org/multipage/grouping-content.html#the-blockquote-element), `blockquote` identifies a section quoted from another source. It is not a generic indentation tool. Put attribution outside the quoted content; a surrounding `figure` with a `figcaption` is one option. A `cite` URL attribute may identify the source but does not provide a visible attribution by itself.

# Prerequisites

- **Body Text** — Surrounding prose supplies the comparison for a separately presented extract.
- **Point Size** — Compare actual appearance before choosing a difference; inherited size may be appropriate.
- **Line Spacing** — Check leading with the actual quote, font and measure; reduction is optional.

# Key Properties

1. **Separate presentation**: Distinguish the quoted section without changing what is quoted.
2. **Contextual indents**: Butterick's print/web ranges are candidates; reduce them where available width is tight.
3. **Punctuation**: House style may omit the block's outer quotation delimiters. Preserve quotation punctuation that belongs within the original material.
4. **Editorial integration**: Explain relevance and preserve accuracy; length alone establishes neither care nor laziness.
5. **Readable hierarchy**: Size, spacing and position can distinguish roles. Smaller text is not mandatory.

# Construction / Recognition

## To Construct/Create:
1. Identify the exact quoted passage, source, language and necessary context.
2. Use semantic quotation markup on the web; keep added attribution outside `blockquote`.
3. Try inherited font size and leading, then adjust only if the actual passage benefits.
4. Choose indents and surrounding gaps together with the resulting line length.
5. Apply the house style's outer-delimiter convention without stripping internal punctuation or silently abridging evidence.
6. Review enlarged text, fallback fonts, narrow measures and the relationship to surrounding prose.

## To Identify/Recognise:
1. A separately presented quotation may use indentation, spacing or other visual distinctions.
2. Indentation alone does not make content a quotation; inspect its meaning and markup.

# Examples

**Example 1** (block-quotations): Butterick contrasts the writer's intended importance signal with a reader's imagined decision to skip. This reported illustration motivates explaining a quotation's relevance; it does not measure reader behavior. His same page allows long exact quotation when accuracy requires it.

For grouping, keep paragraphs inside one extract visibly associated and leave a distinguishable gap between that extract and surrounding authorial prose. As a design inference, a smaller gap within the extract than between extract and authorial prose can cue one group inside a larger sequence. Compare those intra/inter-group gaps alongside indentation and attribution placement; an indent number alone does not establish proximity or comprehension.

# Relationships

## Builds Upon
- **Body Text** — The surrounding prose supplies the visual context for the extract.
- **Point Size** — Size is one comparison variable, with no mandatory reduction.
- **Line Spacing** — Leading affects the quoted passage's readable texture; it need not be reduced.

## Related
- **First-Line Indent** — Both use horizontal spacing, but a paragraph-start marker differs from offsetting an entire quotation.
- **Line Length** — Side indents reduce available measure; review actual lines rather than assuming an indent is suitable.

# Common Errors

- **Error**: Using an unexplained extract or replacing necessary exact evidence with an inaccurate summary.
  **Correction**: Explain relevance, quote accurately and edit only with faithful, indicated omissions or additions. Long quotation can be necessary.

# Common Confusions

- **Confusion**: Every indented passage is a block quotation, and smaller type is its defining feature.
  **Clarification**: Quotation is a content role; styling is contextual. Preserve readable size/leading and meaningful punctuation.

# Source Reference

"Block Quotations" page. "Page Layout" chapter.

# Verification Notes

- Available-source comparison: complete prepared block-quotations.md, including accuracy exception and writer/reader illustration; exact original capture/lineage remains unavailable under P10-11.
- Current technical support: HTML quotation/attribution definition above; illustrative CSS inherits size/leading and requires contextual review.
- Local outcome: prerequisite premises and two related distinctions checked against endpoint sections; CQ1 supplies role distinction, CQ13 supplies explicit intra/inter-group reasoning. Neither is global or empirical acceptance.
- Historical metadata: extraction confidence and source/relationship/CQ fields remain prior extraction records, not refreshed verification results. Earlier no-uncertainty/OCR and Rosetta observations do not establish original fidelity or current semantic verification.
- Unrun: actual rendering, enlargement, assistive technology, hosted output and full-corpus reconciliation.
