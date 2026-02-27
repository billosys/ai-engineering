---
# === CORE IDENTIFICATION ===
concept: Is Draft Field
slug: is-draft-field

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
  - "is_draft"
  - "draft flag"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - frontmatter
extends: []
related:
  - draft
  - build-options
  - cobalt-publish
  - directory-structure
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is a draft in Cobalt?"
  - "What is frontmatter in Cobalt?"
---

# Quick Definition

The `is_draft` frontmatter field is a boolean that controls whether a page is treated as a draft. When `true`, the page is excluded from the build output unless drafts are explicitly included.

# Core Definition

The `is_draft` frontmatter field is a boolean value that marks a page (typically a post) as a draft. When set to `true`, the page will not be rendered during a standard `cobalt build`. It defaults to `false`. Cobalt automatically infers `is_draft: true` for files located in the drafts folder (default: `_drafts/`). To include draft pages in the build output, the user must either pass the `--drafts` flag to the build command or set `include_drafts: true` in `_cobalt.yml`. The `cobalt publish` command sets `is_draft: false` to transition a draft to published state. (Source: Cobalt Frontmatter documentation, "Field Descriptions" section; Posts documentation, "Drafts" section)

# Prerequisites

- **[Frontmatter](/concept-cards/cobalt/frontmatter.md)** -- `is_draft` is a frontmatter field.

# Key Properties

1. **Type**: Boolean.
2. **Default**: `false`.
3. **Directory inference**: Automatically inferred as `true` for files in the drafts directory.
4. **Build exclusion**: Pages with `is_draft: true` are excluded from normal builds.
5. **Override mechanisms**: `--drafts` CLI flag or `include_drafts: true` in configuration.
6. **Publish transition**: `cobalt publish` sets this to `false`.

# Construction / Recognition

## To Construct/Create:
1. In frontmatter, add: `is_draft: true` to mark a page as a draft.
2. Alternatively, place the file in the drafts directory for automatic inference.

## To Identify/Recognize:
1. Look for `is_draft:` in the frontmatter.
2. Check if the file is in the drafts directory.

# Context & Application

- **Typical contexts**: Managing work-in-progress posts that should not yet be published.
- **Common applications**: Hiding unpublished content, previewing drafts locally, managing a publication workflow.

# Examples

**Example 1** (source: Posts documentation): Setting `is_draft: true` in frontmatter:
```yaml
---
title: Work in Progress
is_draft: true
---
```
This post will not appear in the built site unless `--drafts` is passed.

**Example 2** (source: Frontmatter documentation): A file placed in the `_drafts/` directory will have `is_draft` inferred as `true` without needing to set it explicitly in frontmatter.

# Relationships

## Builds Upon
- **[Frontmatter](/concept-cards/cobalt/frontmatter.md)** -- `is_draft` is a frontmatter field.

## Enables
- **[Draft](/concept-cards/cobalt/draft.md)** -- The `is_draft` field is the mechanism that implements the draft concept.

## Related
- **[Build Options](/concept-cards/cobalt/build-options.md)** -- The `include_drafts` build option overrides draft exclusion.
- **[Cobalt Publish](/concept-cards/cobalt/cobalt-publish.md)** -- The publish command modifies this field.
- **[Directory Structure](/concept-cards/cobalt/directory-structure.md)** -- The drafts directory triggers automatic inference of this field.

## Contrasts With
- No direct contrast.

# Common Errors

- **Error**: Setting `is_draft: true` on a regular page (not a post) and expecting it to behave differently.
  **Correction**: The `is_draft` field works on any page, but the documentation focuses on its use with posts. Non-post pages with `is_draft: true` will also be excluded from builds.

# Common Confusions

- **Confusion**: Thinking that `is_draft: true` and being in the `_drafts/` directory are different kinds of drafts.
  **Clarification**: Both produce the same behavior. Files in `_drafts/` simply have `is_draft` inferred as `true`.

# Source Reference

Frontmatter, "Field Descriptions" section; Posts, "Drafts" section. Source: Cobalt documentation.

# Verification Notes

- Definition source: Direct from Cobalt Frontmatter and Posts documentation
- Confidence rationale: The field is explicitly described in both documentation pages with consistent behavior.
- Uncertainties: None.
- Cross-reference status: Verified across Frontmatter, Posts, and Configuration documentation.
