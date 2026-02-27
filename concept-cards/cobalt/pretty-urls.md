---
# === CORE IDENTIFICATION ===
concept: Pretty URLs
slug: pretty-urls

# === CLASSIFICATION ===
category: permalink
subcategory: null
tier: intermediate

# === PROVENANCE ===
source: "Cobalt Static Site Generator Documentation"
source_slug: cobalt
authors: "Cobalt contributors (cobalt-org)"
chapter: "Permalink Templates"
chapter_number: null
pdf_page: null
section: "Pretty URLs"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "clean URLs"
  - "extensionless URLs"
  - "folder-based URLs"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - permalink-templates
extends: []
related:
  - permalink-template-variables
  - page-variable
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is a permalink in Cobalt?"
  - "How do I set up permalink templates?"
  - "What distinguishes path permalink style from custom?"
---

# Quick Definition

Pretty URLs are generated when a permalink template omits the file extension. Cobalt treats the permalink as a folder name and creates `index.html` inside it, resulting in clean URLs without `.html` in the path.

# Core Definition

When a permalink template omits the file extension (e.g., `.html`), Cobalt treats the permalink as a directory and generates an `index.html` file inside that directory. This produces "pretty URLs" where the user-visible URL does not include a file extension. For example, a permalink of `/some/other/file` generates the file at `some/other/file/index.html`, and the page's URL becomes `your-website.com/some/other/file/` (with web servers serving `index.html` by default). The `page.permalink` value retains the extensionless form (e.g., `some/other/file`). This technique is widely used in static site generation to produce cleaner, more user-friendly URLs. (Source: Cobalt Permalink Templates documentation, "Pretty URLs" section)

# Prerequisites

- **[Permalink Templates](/concept-cards/cobalt/permalink-templates.md)** -- Pretty URLs are a behavior of the permalink system.

# Key Properties

1. **Trigger**: Omitting the file extension in the permalink value.
2. **Mechanism**: Cobalt creates a directory and places `index.html` inside it.
3. **User-visible URL**: Clean, without file extensions (e.g., `/blog/my-post/`).
4. **`page.permalink` value**: The extensionless path (e.g., `some/other/file`).
5. **Web server dependency**: Relies on web servers serving `index.html` as the default document for directories.

# Construction / Recognition

## To Construct/Create:
1. Set a permalink without a file extension:
   ```yaml
   permalink: /some/other/file
   ```
2. Or use template variables that produce extensionless paths:
   ```yaml
   permalink: /{{categories}}/{{slug}}
   ```

## To Identify/Recognize:
1. The permalink value does not end with a file extension (e.g., `.html`).
2. The generated output contains a directory with an `index.html` file.

# Context & Application

- **Typical contexts**: Any page or post where clean, user-friendly URLs are desired.
- **Common applications**: Blog post URLs like `/blog/my-post/` instead of `/blog/my-post.html`, creating SEO-friendly URL structures.

# Examples

**Example 1** (source: Permalink Templates documentation): Pretty URL permalink:
```yaml
title: My first Blogpost
layout: posts.liquid
permalink: /some/other/file
```
Result:
- Generated file: `some/other/file/index.html`
- URL: `your-website.com/some/other/file/`
- `page.permalink`: `some/other/file`

**Example 2** (source: Permalink Templates documentation): Template-based permalink producing a pretty URL:
```yaml
title: Corgi
categories:
  - Animals
  - Dogs
permalink: /{{categories}}/{{slug}}
```
Result:
- Generated file: `animals/dogs/corgi/index.html`
- URL: `your-website.com/animals/dogs/corgi/`
- `page.permalink`: `animals/dogs/corgi`

**Contrast** (source: Permalink Templates documentation): With file extension (NOT a pretty URL):
```yaml
permalink: /some/other/file.html
```
Result:
- Generated file: `some/other/file.html`
- URL: `your-website.com/some/other/file.html`
- `page.permalink`: `some/other/file.html`

# Relationships

## Builds Upon
- **[Permalink Templates](/concept-cards/cobalt/permalink-templates.md)** -- Pretty URLs are a behavior of the permalink template system.

## Enables
- No concepts directly enabled.

## Related
- **[Permalink Template Variables](/concept-cards/cobalt/permalink-template-variables.md)** -- The `ext` variable provides the file extension; omitting it creates pretty URLs.
- **[Page Variable](/concept-cards/cobalt/page-variable.md)** -- The `page.permalink` reflects the pretty URL (extensionless) form.

## Contrasts With
- No named contrast concept, but pretty URLs contrast with explicit-extension permalinks (e.g., using `path` style or adding `.html`).

# Common Errors

- **Error**: Using the `path` built-in style and expecting pretty URLs.
  **Correction**: The `path` style uses `/{parent}/{name}{ext}`, which includes the file extension. To get pretty URLs, use a custom permalink template without the extension: `/{parent}/{name}`.

- **Error**: Forgetting that the web server must be configured to serve `index.html` as the default document.
  **Correction**: Most web servers (Apache, Nginx, etc.) serve `index.html` by default, but verify your server configuration if pretty URLs are not working.

# Common Confusions

- **Confusion**: Thinking `page.permalink` for pretty URLs includes `/index.html`.
  **Clarification**: The `page.permalink` value is the clean, extensionless path (e.g., `some/other/file`), not the actual file path (`some/other/file/index.html`).

# Source Reference

Permalink Templates, "Pretty URLs" section. Source: Cobalt documentation.

# Verification Notes

- Definition source: Direct from Cobalt Permalink Templates documentation, "Pretty URLs" section
- Confidence rationale: The documentation provides clear examples comparing pretty URLs with extension-based URLs.
- Uncertainties: None -- the behavior is clearly documented with before/after examples.
- Cross-reference status: Consistent with the permalink template examples throughout the documentation.
