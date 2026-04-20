---
# === CORE IDENTIFICATION ===
concept: cobalt publish
slug: cobalt-publish

# === CLASSIFICATION ===
category: cli
subcategory: commands
tier: foundational

# === PROVENANCE ===
source: "Cobalt Static Site Generator Documentation"
source_slug: cobalt
authors: "Cobalt contributors (cobalt-org)"
chapter: "Usage"
chapter_number: null
pdf_page: null
section: "publish"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "publish command"
  - "publishing a draft"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - cobalt-new
  - installation
extends: []
related:
  - cobalt-build
  - draft
  - post
  - frontmatter
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do I publish a draft post?"
---

# Quick Definition

`cobalt publish` transitions a draft post to published state by clearing its draft flag, setting the `published_date` to today, and optionally moving it from the `_drafts` folder to the `posts` folder.

# Core Definition

The `cobalt publish` command changes a post from draft to published state. It performs up to three actions: (1) sets the `is_draft` frontmatter field to false, (2) sets the `published_date` to the current date, and (3) if the post is in the `_drafts` folder, moves it to the `posts` folder. As documented: "The page will no longer be a 'draft' and the `published_date` will be set to today" (source: Usage doc page, "publish" section). By default, for posts, the date (`YYYY-MM-DD-`) is prepended to the filename to maintain chronological order; this can be disabled by setting `publish_date_in_filename: false` in the site configuration (source: Usage doc page, "publish" section).

# Prerequisites

- **Installation** -- Cobalt must be installed
- **cobalt new** -- typically, a post has been created (via `cobalt new` or manually) in draft state

# Key Properties

1. **Clears draft status** -- "The page will no longer be a 'draft'" (source: Usage doc page).
2. **Sets published date** -- "the `published_date` will be set to today" (source: Usage doc page).
3. **Moves from drafts folder** -- "You can also publish from the `drafts` folder... It will move it to `posts` folder besides changing 'draft' status and `published_date`" (source: Usage doc page, "publish" section).
4. **Date prefix in filename** -- "by default, the date (`YYYY-MM-DD-`) will be prepend to your posts filename in order to keep them in chronological order" (source: Usage doc page).
5. **Configurable date prefix** -- "This can be disabled by manually setting `publish_date_in_filename: false` in your configuration" (source: Usage doc page).

# Construction / Recognition

## To Construct/Create:
1. Create a post (via `cobalt new` or manually) in draft state.
2. Run `cobalt publish <path-to-post>` to publish it.

## To Identify/Recognize:
1. A published post has `is_draft: false` (or no `is_draft` field) in its frontmatter.
2. A published post has a `published_date` set.
3. A published post filename may have a `YYYY-MM-DD-` prefix if `publish_date_in_filename` is enabled (the default).

# Context & Application

- **Typical contexts**: Moving a completed blog post from draft to published state before building for deployment.
- **Common applications**: Publishing blog posts, managing the editorial workflow of a Cobalt blog.

# Examples

**Example 1** (source: Usage doc page): Publish a post from the posts directory:
```console
$ cobalt publish posts/cats-around-the-world.md
```

**Example 2** (source: Usage doc page): Publish a post from the drafts folder (moves it to posts):
```console
$ cobalt publish drafts/dogs-around-the-world.md
```
This moves the file to the `posts` folder in addition to changing draft status and published_date.

**Example 3** (source: Getting Started page): Publish as part of the full workflow:
```console
$ cobalt new "Cats Around the World"
$ cobalt publish posts/cats-around-the-world.md
$ cobalt build
```

# Relationships

## Builds Upon
- **cobalt new** -- publish acts on posts that were typically created by `cobalt new`
- **draft** -- publish transitions a post out of draft state

## Enables
- **cobalt build** -- published posts are included in the build output

## Related
- **post** -- publish operates on posts
- **frontmatter** -- publish modifies `is_draft` and `published_date` in the frontmatter
- **cobalt-configuration-file** -- `publish_date_in_filename` setting controls date prefix behavior

## Contrasts With
- No direct contrasts within scope; one could manually edit frontmatter instead of using `cobalt publish`, but publish automates the process.

# Common Errors

- **Error**: Running `cobalt build` without first publishing draft posts, then wondering why they are missing from the output.
  **Correction**: Run `cobalt publish <path>` on each draft post before building, or set `is_draft: false` manually in the frontmatter.

# Common Confusions

- **Confusion**: `cobalt publish` deploys the site to a web server.
  **Clarification**: `cobalt publish` only changes a post's draft status and sets its published date. It does not build the site or deploy it. After publishing, run `cobalt build` to generate the site, then deploy the output separately.

- **Confusion**: Publishing from `_drafts` leaves a copy in the drafts folder.
  **Clarification**: Publishing from `_drafts` moves the file to the `posts` folder; it does not leave a copy behind.

# Source Reference

Usage doc page, "publish" section; Getting Started page, "Publish a Post" section. Source: Cobalt documentation.

# Verification Notes

- Definition source: Direct from Usage doc page ("publish" section) and Getting Started page
- Confidence rationale: High -- the publish command behavior is explicitly documented including folder-move semantics and date prefix behavior
- Uncertainties: None significant
- Cross-reference status: References to cobalt-new, cobalt-build, draft, post, frontmatter, cobalt-configuration-file verified against planned card slugs
