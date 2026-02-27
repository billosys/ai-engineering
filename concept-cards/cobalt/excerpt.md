---
# === CORE IDENTIFICATION ===
concept: Excerpt and Excerpt Separator
slug: excerpt

# === CLASSIFICATION ===
category: frontmatter
subcategory: null
tier: intermediate

# === PROVENANCE ===
source: "Cobalt Static Site Generator Documentation"
source_slug: cobalt
authors: "Cobalt contributors (cobalt-org)"
chapter: "Frontmatter"
chapter_number: null
pdf_page: null
section: "Field Descriptions"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "excerpt_separator"
  - "page excerpt"
  - "post excerpt"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - frontmatter
extends: []
related:
  - page-variable
  - content-processing-pipeline
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is frontmatter in Cobalt?"
---

# Quick Definition

The excerpt system in Cobalt extracts leading content from a page as a summary. The `excerpt_separator` field defines the marker where the excerpt ends (default: `"\n\n"`, a double newline), and the `excerpt` field allows manual override of the extracted text.

# Core Definition

Cobalt provides two related frontmatter fields for managing excerpts. The `excerpt_separator` field is a string that defines a marker for what leading content should be extracted from the page content as an excerpt. Its default value is `"\n\n"` (a double newline), meaning the first paragraph is used as the excerpt. Setting `excerpt_separator` to an empty string (`""`) disables excerpt generation. The `excerpt` field allows manually overriding the automatically extracted excerpt; when set, its value is processed like a page (through the content processing pipeline). Excerpts are commonly used in post listings and RSS feeds to show a preview of the content. (Source: Cobalt Frontmatter documentation, "Field Descriptions" section)

# Prerequisites

- **[Frontmatter](/concept-cards/cobalt/frontmatter.md)** -- Excerpt fields are part of frontmatter.

# Key Properties

1. **`excerpt_separator` type**: String.
2. **`excerpt_separator` default**: `"\n\n"` (double newline, extracting the first paragraph).
3. **Disable excerpt**: Set `excerpt_separator: ""` to generate no excerpt.
4. **`excerpt` type**: String or null.
5. **`excerpt` default**: `~` (null, uses auto-extracted excerpt).
6. **Manual override**: Setting `excerpt` explicitly overrides the auto-extracted value.
7. **Processing**: The excerpt value is processed like a page (through Liquid and Markdown).
8. **Configurable default**: The `excerpt_separator` default can be set site-wide in `_cobalt.yml` via the `default` section.

# Construction / Recognition

## To Construct/Create:
1. By default, the first paragraph (content before `\n\n`) is used as the excerpt.
2. To use a custom separator, set `excerpt_separator: "<!-- more -->"` (or any custom string) in frontmatter.
3. To manually specify the excerpt, set `excerpt: "My custom excerpt text."` in frontmatter.
4. To disable excerpts, set `excerpt_separator: ""`.

## To Identify/Recognize:
1. Look for `excerpt_separator:` or `excerpt:` in the frontmatter.
2. In templates, the excerpt is accessible via `page.excerpt`.

# Context & Application

- **Typical contexts**: Blog post listings, RSS feeds, social media previews.
- **Common applications**: Displaying a summary of posts on index pages, providing content previews in feed readers.

# Examples

**Example 1** (source: Frontmatter documentation): With the default `excerpt_separator: "\n\n"`, a post beginning with:
```
Hey there this is my first blogpost and this is super awesome.

My Blog is lorem ipsum like, yes it is..
```
The excerpt would be: "Hey there this is my first blogpost and this is super awesome."

**Example 2** (source: Frontmatter documentation): Manually overriding the excerpt:
```yaml
---
title: My Post
excerpt: "A brief summary of my post content."
---
```

# Relationships

## Builds Upon
- **[Frontmatter](/concept-cards/cobalt/frontmatter.md)** -- Excerpt fields are frontmatter fields.

## Enables
- No concepts directly enabled.

## Related
- **[Page Variable](/concept-cards/cobalt/page-variable.md)** -- The excerpt is accessible via `page.excerpt` in templates.
- **[Content Processing Pipeline](/concept-cards/cobalt/content-processing-pipeline.md)** -- Manual excerpts are processed through the same pipeline as page content.

## Contrasts With
- No direct contrast.

# Common Errors

- **Error**: Expecting the excerpt to include content after the separator.
  **Correction**: The excerpt is the content BEFORE the separator, not after it.

- **Error**: Setting a custom excerpt separator but not including that separator in the actual content.
  **Correction**: If you set a custom separator like `<!-- more -->`, ensure it actually appears in your content where you want the excerpt to end.

# Common Confusions

- **Confusion**: Thinking the excerpt is always the first paragraph.
  **Clarification**: The excerpt is the content before the `excerpt_separator`. The default separator is `"\n\n"` (double newline), which effectively makes it the first paragraph. But with a custom separator, the excerpt can span multiple paragraphs.

# Source Reference

Frontmatter, "Field Descriptions" section. Source: Cobalt documentation.

# Verification Notes

- Definition source: Direct from Cobalt Frontmatter documentation
- Confidence rationale: The documentation describes both fields clearly, including defaults and behavior.
- Uncertainties: The exact processing pipeline for manual excerpts (whether layouts are applied) is not fully detailed.
- Cross-reference status: The Configuration documentation confirms `excerpt_separator` can be set as a site-wide default.
