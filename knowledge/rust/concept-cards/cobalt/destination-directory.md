---
# === CORE IDENTIFICATION ===
concept: Destination Directory
slug: destination-directory

# === CLASSIFICATION ===
category: project-structure
subcategory: directories
tier: foundational

# === PROVENANCE ===
source: "Cobalt Static Site Generator Documentation"
source_slug: cobalt
authors: "Cobalt contributors (cobalt-org)"
chapter: "Directory Structure"
chapter_number: null
pdf_page: null
section: null

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "destination"
  - "output directory"
  - "_site"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - directory-structure
extends: []
related:
  - source-directory
  - cobalt-build
  - cobalt-clean
  - cobalt-serve
  - cobalt-configuration-file
contrasts_with:
  - source-directory

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is the directory structure of a Cobalt project?"
  - "How do I build a Cobalt site?"
---

# Quick Definition

The destination directory (`_site` by default) is where Cobalt writes the generated static HTML files and copied assets after building, producing the deployment-ready site output.

# Core Definition

The destination directory is the output location where `cobalt build` writes the generated static site. It defaults to `_site` and can be configured via the `destination` setting in `_cobalt.yml`. The Configuration doc page describes it as: "Directory, relative to `_cobalt.yml`, where the output is written to" (source: Configuration doc page, "Build options" section). The Directory doc page lists `_site` as "The output directory of cobalt. Can be modified in `_cobalt.yml`" (source: Directory doc page). After a successful build, this directory contains all HTML files and assets ready for deployment to a web server. The `cobalt clean` command prunes this directory, and `cobalt serve` uses a temporary directory instead.

# Prerequisites

- **Directory Structure** -- understanding the overall Cobalt project layout

# Key Properties

1. **Default value is `_site`** -- "destination: _site" in the default configuration (source: Configuration doc page).
2. **Configurable** -- "Can be modified in `_cobalt.yml`" (source: Directory doc page).
3. **Deployment-ready output** -- "The site is sitting in `_site` and ready to be uploaded!" (source: Getting Started page).
4. **Mirrors source hierarchy** -- the output structure mirrors the source file hierarchy (source: Directory doc page).
5. **Pruned by clean** -- `cobalt clean` "Cleans/prunes the `destination` directory" (source: Usage doc page, "clean" section).
6. **Not used by serve** -- `cobalt serve` builds to a temporary directory instead, e.g., `/tmp/.tmpgYpScM` (source: Usage doc page, "serve" section).

# Construction / Recognition

## To Construct/Create:
1. Run `cobalt build` to generate the destination directory with all output files.
2. The destination is automatically created if it does not exist.

## To Identify/Recognize:
1. The `_site` directory (or the configured destination) in a Cobalt project contains the generated HTML and asset files.
2. The directory structure within it mirrors the source hierarchy.

# Context & Application

- **Typical contexts**: Deploying a Cobalt site, configuring CI/CD pipelines, understanding build output.
- **Common applications**: Uploading the contents to a static hosting provider (GitHub Pages, Netlify, etc.), inspecting generated HTML for debugging, configuring deployment scripts.

# Examples

**Example 1** (source: Getting Started page): After building, the site is in `_site`:
```console
$ cobalt build
```
"The site is sitting in `_site` and ready to be uploaded!"

**Example 2** (source: Configuration doc page): Default destination configuration:
```yml
destination: _site
```

**Example 3** (source: Directory doc page): In the project tree, `_site` contains output:
```
|- _site
|  |- index.html
```

# Relationships

## Builds Upon
- **directory-structure** -- the destination directory is part of the overall project layout

## Enables
- Site deployment -- the destination directory is what gets deployed

## Related
- **cobalt-build** -- build writes to the destination directory
- **cobalt-clean** -- clean prunes the destination directory
- **cobalt-configuration-file** -- the `destination` setting configures this directory

## Contrasts With
- **source-directory** -- the source directory holds input content; the destination directory holds generated output
- **cobalt-serve** -- serve does not write to the destination directory; it uses a temporary directory instead

# Common Errors

- **Error**: Manually editing files in `_site`, which are then overwritten on the next build.
  **Correction**: Always edit source files, not output files. Changes in `_site` are overwritten by `cobalt build`.

- **Error**: Deploying the project root instead of the `_site` directory.
  **Correction**: Only the destination directory (`_site` by default) should be deployed. The project root contains source files and configuration not meant for public serving.

# Common Confusions

- **Confusion**: `cobalt serve` writes to `_site`.
  **Clarification**: `cobalt serve` builds to a temporary directory (e.g., `/tmp/.tmpgYpScM`), not to `_site`. Only `cobalt build` writes to the configured destination directory.

# Source Reference

Directory Structure doc page; Configuration doc page, "Build options" section; Getting Started page, "Build the site" section. Source: Cobalt documentation.

# Verification Notes

- Definition source: Direct from Directory doc page and Configuration doc page
- Confidence rationale: High -- the destination directory is explicitly documented with its default value, description, and configurability
- Uncertainties: None significant
- Cross-reference status: References to directory-structure, source-directory, cobalt-build, cobalt-clean, cobalt-serve, cobalt-configuration-file verified against planned card slugs
