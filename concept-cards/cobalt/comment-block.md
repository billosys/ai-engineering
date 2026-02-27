---
# === CORE IDENTIFICATION ===
concept: Comment Block
slug: comment-block

# === CLASSIFICATION ===
category: liquid-blocks
subcategory: null
tier: foundational

# === PROVENANCE ===
source: "Cobalt Static Site Generator Documentation"
source_slug: cobalt
authors: "Cobalt contributors (cobalt-org)"
chapter: "Liquid Standard Library"
chapter_number: null
pdf_page: null
section: "CommentBlock"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "template comment"
  - "Liquid comment"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - logic-tags
extends: []
related:
  - raw-block
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is a Liquid block?"
---

# Quick Definition

The `comment` block prevents any content between `{% comment %}` and `{% endcomment %}` from being rendered in the output. It is used for template-level comments that should not appear in the generated HTML.

# Core Definition

The `comment` block is implemented in the `liquid_lib` crate as `CommentBlock` (source file: `stdlib/blocks/comment_block.rs`). Content between `{% comment %}` and `{% endcomment %}` is completely suppressed during rendering -- it does not appear in the output HTML. Unlike HTML comments (`<!-- -->`), Liquid comments are stripped during template processing and never reach the browser. Any Liquid code inside a comment block is also not executed. (Source: liquid_lib stdlib CommentBlock)

# Prerequisites

- **[Logic Tags](/concept-cards/cobalt/logic-tags.md)** -- Uses `{% %}` syntax.

# Key Properties

1. **Start tag**: `{% comment %}`.
2. **End tag**: `{% endcomment %}`.
3. **Complete suppression**: No output is generated for the enclosed content.
4. **No execution**: Liquid tags inside comments are not processed or executed.
5. **Server-side**: Comments are removed during build, never sent to the browser.

# Construction / Recognition

## To Construct/Create:
1. Write `{% comment %}` to start the comment.
2. Place the comment text or code to suppress.
3. Close with `{% endcomment %}`.

## To Identify/Recognize:
1. Look for `{% comment %}` opening tags.
2. Closed by `{% endcomment %}`.

# Context & Application

- **Typical contexts**: Documenting template logic, temporarily disabling template code, leaving notes for template developers.
- **Common applications**: Explaining complex Liquid logic, commenting out sections during development, documenting template structure.

# Examples

**Example 1** (source: Liquid Standard Library): Basic comment:
```liquid
{% comment %}
  This is a comment that will not appear in the output.
  It can span multiple lines.
{% endcomment %}
```

**Example 2** (source: Liquid Standard Library): Commenting out template code:
```liquid
{% comment %}
  {% for item in site.data.items %}
    <li>{{ item.name }}</li>
  {% endfor %}
{% endcomment %}
```

# Relationships

## Builds Upon
- **[Logic Tags](/concept-cards/cobalt/logic-tags.md)** -- Uses `{% %}` syntax.

## Enables
- Template documentation and debugging.

## Related
- **[Raw Block](/concept-cards/cobalt/raw-block.md)** -- Raw also modifies Liquid processing behavior, but outputs its content literally.

## Contrasts With
- None directly (HTML comments `<!-- -->` are part of HTML, not Liquid).

# Common Errors

- **Error**: Using HTML comments (`<!-- -->`) for sensitive content, expecting it to be hidden.
  **Correction**: HTML comments are sent to the browser and visible in page source. Use `{% comment %}` for content that should never reach the browser.

# Common Confusions

- **Confusion**: Thinking Liquid code inside comments is still executed.
  **Clarification**: All content inside `{% comment %}...{% endcomment %}` is completely ignored, including any Liquid tags. Nothing is executed or rendered.

# Source Reference

Liquid Standard Library, CommentBlock struct. Source: liquid_lib rustdoc (stdlib/blocks/comment_block.rs).

# Verification Notes

- Definition source: liquid_lib CommentBlock struct documentation
- Confidence rationale: Standard Liquid feature, well-documented.
- Uncertainties: None.
- Cross-reference status: Verified in liquid_lib stdlib.
