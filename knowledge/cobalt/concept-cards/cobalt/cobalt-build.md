---
# === CORE IDENTIFICATION ===
concept: cobalt build
slug: cobalt-build

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
section: "build"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "build command"
  - "site generation"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - cobalt-init
  - installation
extends: []
related:
  - source-directory
  - destination-directory
  - cobalt-serve
  - cobalt-publish
  - cobalt-clean
  - content-processing-pipeline
contrasts_with:
  - cobalt-serve

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do I build a Cobalt site?"
  - "What distinguishes serve from build?"
---

# Quick Definition

`cobalt build` compiles all non-draft documents from the source directory into static HTML files in the destination directory, producing a site ready for deployment.

# Core Definition

The `cobalt build` command processes all documents in the Cobalt project that are not in draft state and generates the corresponding static HTML output in the destination directory (default: `_site`). As stated in the Usage doc page: "All the documents not in draft state will be built into a html file ready to be serve by your web server" (source: Usage doc page, "build" section). The build should be performed after documents have been put into their desired published or draft state using `cobalt publish` or by manually setting `is_draft: false` in frontmatter.

# Prerequisites

- **Installation** -- Cobalt must be installed
- **cobalt init** -- a Cobalt site must exist (either from `cobalt init` or manually created)

# Key Properties

1. **Processes non-draft documents only** -- "All the documents not in draft state will be built into a html file ready to be serve by your web server" (source: Usage doc page, "build" section).
2. **Outputs to destination directory** -- by default, output goes to `_site`; configurable via `destination` in `_cobalt.yml` (source: Directory doc page, Configuration doc page).
3. **One-shot generation** -- unlike `cobalt serve`, build runs once and exits without watching for changes.
4. **Deployment-ready output** -- "The site is sitting in `_site` and ready to be uploaded!" (source: Getting Started page).
5. **Verbose logging** -- supports `--verbose` or `-vv` flags for additional build detail (source: Troubleshooting doc page).

# Construction / Recognition

## To Construct/Create:
1. Ensure all desired content is in published (non-draft) state.
2. Run `cobalt build` from the project root directory.
3. The generated site appears in the destination directory (default `_site`).

## To Identify/Recognize:
1. The `_site` directory (or configured destination) contains the generated HTML output after a successful build.
2. Build output mirrors the source file hierarchy with `.html` extensions.

# Context & Application

- **Typical contexts**: Final step before deploying a site, CI/CD pipelines, generating production-ready output.
- **Common applications**: Building the site for deployment to GitHub Pages, Netlify, or any static hosting provider; generating the site after publishing new posts.

# Examples

**Example 1** (source: Usage doc page): Basic build:
```console
$ cobalt build
```

**Example 2** (source: Getting Started page): Build after publishing a post:
```console
$ cobalt publish posts/cats-around-the-world.md
$ cobalt build
```
The site is then in `_site` and ready to be uploaded.

**Example 3** (source: Troubleshooting doc page): Build with verbose output for debugging:
```console
$ cobalt build --verbose
$ cobalt build -vv  # maximum verbosity
```

# Relationships

## Builds Upon
- **cobalt init** -- a site must be initialized before building
- **cobalt publish** -- posts should be published before building for production

## Enables
- **Deployment** -- build output is the deployment artifact
- **cobalt clean** -- cleaning removes the build output

## Related
- **source-directory** -- build reads content from the source directory
- **destination-directory** -- build writes output to the destination directory
- **content-processing-pipeline** -- build invokes the full processing pipeline (Liquid evaluation, Markdown conversion, layout wrapping)

## Contrasts With
- **cobalt serve** -- `serve` builds to a temporary directory, watches for changes, and runs a local web server; `build` runs once and writes to the configured destination directory

# Common Errors

- **Error**: Draft posts do not appear in the built site.
  **Correction**: Draft posts are excluded from `cobalt build` by default. Use `cobalt publish` to change their draft status, or set `is_draft: false` in the frontmatter before building.

# Common Confusions

- **Confusion**: `cobalt build` and `cobalt serve` produce the same output.
  **Clarification**: `cobalt build` writes to the configured destination directory (default `_site`) for deployment. `cobalt serve` builds to a temporary directory and starts a local server with file watching. Use `build` for production output and `serve` for local development.

# Source Reference

Usage doc page, "build" section; Getting Started page, "Build the site" section. Source: Cobalt documentation.

# Verification Notes

- Definition source: Direct from Usage doc page ("build" section) and Getting Started page
- Confidence rationale: High -- the build command is clearly documented with explicit behavior description
- Uncertainties: None significant; the command behavior is straightforward
- Cross-reference status: References to cobalt-init, cobalt-serve, cobalt-publish, cobalt-clean, source-directory, destination-directory, content-processing-pipeline verified against planned card slugs
