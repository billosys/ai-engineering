---
# === CORE IDENTIFICATION ===
concept: Draft
slug: draft

# === CLASSIFICATION ===
category: content
subcategory: null
tier: foundational

# === PROVENANCE ===
source: "Cobalt Static Site Generator Documentation"
source_slug: cobalt
authors: "Cobalt contributors (cobalt-org)"
chapter: "Posts"
chapter_number: null
pdf_page: null
section: "Drafts"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "draft post"
  - "draft page"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - post
extends: []
related:
  - is-draft-field
  - cobalt-configuration-file
  - build-options
  - cobalt-build
  - cobalt-publish
  - directory-structure
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is a draft in Cobalt?"
---

# Quick Definition

A draft is a post in Cobalt that is marked as unpublished and excluded from the generated site by default. Drafts are only rendered when Cobalt is run with the `--drafts` flag or when `include_drafts` is set to `true` in the configuration.

# Core Definition

Cobalt supports leaving posts in a "draft" state, meaning they will not be rendered unless explicitly requested. A post can be marked as a draft in two ways: (1) by setting `is_draft: true` in the post's frontmatter, or (2) by placing the post file in the drafts folder (default: `_drafts/`, configurable via `posts.drafts_dir`). Draft posts are excluded from the build output by default. To include drafts, the user must either pass the `--drafts` flag to the `cobalt build` or `cobalt serve` command, or set `include_drafts: true` in `_cobalt.yml`. The `cobalt publish` command can be used to transition a draft to published state. (Source: Cobalt Posts documentation, "Drafts" section)

# Prerequisites

- **[Post](/concept-cards/cobalt/post.md)** -- Drafts are a state that applies to posts specifically.

# Key Properties

1. **Two mechanisms for marking as draft**: Set `is_draft: true` in frontmatter, or place the file in the drafts directory.
2. **Default exclusion**: Drafts are not rendered in the build output by default.
3. **Opt-in rendering**: The `--drafts` command-line flag or `include_drafts: true` configuration enables draft rendering.
4. **Drafts directory**: Default drafts directory is `_drafts/` (configurable via `posts.drafts_dir`).
5. **Filename inference**: Files placed in the drafts folder automatically have `is_draft` inferred as `true`.
6. **Publication workflow**: The `cobalt publish` command transitions drafts to published state.

# Construction / Recognition

## To Construct/Create:
1. Create a post file in the posts directory.
2. Either set `is_draft: true` in the frontmatter, or place the file in the `_drafts/` directory.
3. The post will now be excluded from normal builds.

## To Identify/Recognize:
1. Check the frontmatter for `is_draft: true`.
2. Check if the file resides in the drafts directory (`_drafts/` by default).
3. Either condition marks the post as a draft.

# Context & Application

- **Typical contexts**: Work-in-progress blog posts, content that is not yet ready for publication, staging content for review.
- **Common applications**: Writing posts ahead of time without publishing them, previewing draft content locally using `cobalt serve --drafts`.

# Examples

**Example 1** (source: Posts documentation): A post with frontmatter `is_draft: true` will not appear in the built site unless `cobalt build --drafts` is used.

**Example 2** (source: Posts documentation): A post file placed in the `_drafts/` directory is automatically treated as a draft without needing to set `is_draft` in the frontmatter, because Cobalt infers `is_draft: true` for files in the drafts folder.

# Relationships

## Builds Upon
- **[Post](/concept-cards/cobalt/post.md)** -- Drafts are a state of posts; the draft concept only applies to posts.

## Enables
- **[Cobalt Publish](/concept-cards/cobalt/cobalt-publish.md)** -- The publish command exists to transition drafts to published state.

## Related
- **[Is Draft Field](/concept-cards/cobalt/is-draft-field.md)** -- The frontmatter field that controls draft state.
- **[Build Options](/concept-cards/cobalt/build-options.md)** -- The `include_drafts` build option controls whether drafts are rendered.
- **[Directory Structure](/concept-cards/cobalt/directory-structure.md)** -- The drafts directory is part of Cobalt's directory structure.

## Contrasts With
- No direct contrasts; drafts are a state of posts, not a separate content type.

# Common Errors

- **Error**: Placing a file in `_drafts/` and expecting it to appear in the built site without the `--drafts` flag.
  **Correction**: Either use `cobalt build --drafts` to include drafts, set `include_drafts: true` in `_cobalt.yml`, or use `cobalt publish` to transition the draft to published state.

# Common Confusions

- **Confusion**: Thinking that `_drafts/` directory files and `is_draft: true` frontmatter are different types of drafts with different behaviors.
  **Clarification**: Both mechanisms produce the same result -- the post is excluded from normal builds. Files in `_drafts/` simply have `is_draft: true` inferred automatically.

# Source Reference

Posts, "Drafts" section. Source: Cobalt documentation.

# Verification Notes

- Definition source: Direct from Cobalt Posts documentation, "Drafts" section
- Confidence rationale: The documentation explicitly describes draft behavior and the two mechanisms for creating drafts.
- Uncertainties: None -- the documentation is clear.
- Cross-reference status: Verified against Frontmatter documentation (is_draft field) and Configuration documentation (include_drafts option).
