---
# === CORE IDENTIFICATION ===
concept: Raw Block
slug: raw-block

# === CLASSIFICATION ===
category: liquid-blocks
subcategory: null
tier: intermediate

# === PROVENANCE ===
source: "Cobalt Static Site Generator Documentation"
source_slug: cobalt
authors: "Cobalt contributors (cobalt-org)"
chapter: "Liquid Standard Library"
chapter_number: null
pdf_page: null
section: "RawBlock"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "raw tag"
  - "escape block"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - logic-tags
extends: []
related:
  - comment-block
  - liquid-template-language
contrasts_with:
  - comment-block

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is a Liquid block?"
---

# Quick Definition

The `raw` block disables Liquid template processing for its enclosed content, outputting it literally as-is. This is essential for displaying Liquid code examples or including content that contains `{{ }}` or `{% %}` delimiters that should not be interpreted.

# Core Definition

The `raw` block is implemented in the `liquid_lib` crate as `RawBlock` (source file: `stdlib/blocks/raw_block.rs`). Content between `{% raw %}` and `{% endraw %}` is output verbatim without any Liquid processing. This means `{{ }}` and `{% %}` delimiters within the raw block are treated as plain text and rendered as-is in the output. The Cobalt documentation itself uses `{% raw %}` extensively to display Liquid code examples (as seen in layouts.md, variables.md, and data.md). (Source: liquid_lib stdlib RawBlock, Cobalt documentation)

# Prerequisites

- **[Logic Tags](/concept-cards/cobalt/logic-tags.md)** -- Uses `{% %}` syntax (for the raw/endraw tags themselves).

# Key Properties

1. **Start tag**: `{% raw %}`.
2. **End tag**: `{% endraw %}`.
3. **Literal output**: All enclosed content is output as plain text.
4. **No processing**: `{{ }}` and `{% %}` delimiters inside are not interpreted.
5. **Preserves content**: The exact text between the tags is preserved in the output.

# Construction / Recognition

## To Construct/Create:
1. Write `{% raw %}` before the content to preserve.
2. Place the literal content (which may include Liquid-like syntax).
3. Close with `{% endraw %}`.

## To Identify/Recognize:
1. Look for `{% raw %}` opening tags.
2. Closed by `{% endraw %}`.

# Context & Application

- **Typical contexts**: Documentation pages showing Liquid code examples, templates that contain JavaScript frameworks using `{{ }}` syntax (like Vue.js or Angular).
- **Common applications**: Writing tutorials about Liquid, embedding JavaScript template syntax, displaying code samples that contain curly braces.

# Examples

**Example 1** (source: Cobalt Layouts documentation): The Cobalt docs use raw to show Liquid syntax examples:
```
{% raw %}{{ page.content }}{% endraw %}
```
This outputs the literal text `{{ page.content }}` instead of the page content value.

**Example 2** (source: Cobalt Data Files documentation): Displaying a for loop example:
```
{% raw %}{% for breed in site.data.animals.dogs %}{% endraw %}
```

# Relationships

## Builds Upon
- **[Logic Tags](/concept-cards/cobalt/logic-tags.md)** -- The raw/endraw tags themselves use logic tag syntax.

## Enables
- Displaying Liquid code examples in generated pages.

## Related
- **[Comment Block](/concept-cards/cobalt/comment-block.md)** -- Comments suppress content entirely; raw outputs it literally.
- **[Liquid Template Language](/concept-cards/cobalt/liquid-template-language.md)** -- Raw is used to escape Liquid syntax.

## Contrasts With
- **[Comment Block](/concept-cards/cobalt/comment-block.md)** -- Comments suppress content from the output entirely; raw preserves and outputs content literally without Liquid processing.

# Common Errors

- **Error**: Nesting `{% raw %}` blocks (not supported).
  **Correction**: Only a single level of raw is needed. The `{% endraw %}` tag ends the raw block.

# Common Confusions

- **Confusion**: Thinking raw is the same as comment.
  **Clarification**: `{% raw %}` outputs content literally; `{% comment %}` suppresses content entirely.

# Source Reference

Liquid Standard Library, RawBlock struct. Source: liquid_lib rustdoc (stdlib/blocks/raw_block.rs); Cobalt documentation uses raw extensively.

# Verification Notes

- Definition source: liquid_lib RawBlock struct documentation
- Confidence rationale: Standard Liquid feature, extensively used in Cobalt's own documentation.
- Uncertainties: None.
- Cross-reference status: Verified by observing `{%raw%}` usage throughout Cobalt documentation source files.
