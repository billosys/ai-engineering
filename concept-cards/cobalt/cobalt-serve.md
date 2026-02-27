---
# === CORE IDENTIFICATION ===
concept: cobalt serve
slug: cobalt-serve

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
section: "serve"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "serve command"
  - "local preview"
  - "development server"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - cobalt-init
  - installation
extends: []
related:
  - cobalt-build
  - source-directory
  - destination-directory
contrasts_with:
  - cobalt-build

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do I preview a Cobalt site locally?"
  - "What distinguishes serve from build?"
---

# Quick Definition

`cobalt serve` builds the site to a temporary directory, starts a local static file server, and watches for file changes to automatically rebuild, enabling live local preview during development.

# Core Definition

The `cobalt serve` command provides a local development workflow by building the site into a temporary directory, serving it through a built-in static file server (default: `http://localhost:1024`), and watching the source directory for changes to trigger automatic rebuilds. The command runs continuously until stopped with Ctrl-c. It supports `--host` to change the listen address (default: `localhost`), `--port` (or `-P`) to change the TCP port, and `--drafts` to include draft posts in the preview (source: Usage doc page, "serve" section; Getting Started page, "Preview" section).

# Prerequisites

- **Installation** -- Cobalt must be installed
- **cobalt init** -- a Cobalt site must exist

# Key Properties

1. **Builds to a temporary directory** -- "Building from `.` into `/tmp/.tmpgYpScM`" (source: Usage doc page, "serve" section).
2. **File watching** -- "Watching . for changes" -- automatically rebuilds when source files change (source: Usage doc page).
3. **Built-in static server** -- "Serving /tmp/.tmpgYpScM through static file server" at `http://localhost:1024` by default (source: Usage doc page).
4. **Configurable host and port** -- `--host` changes the listen address (default `localhost`); `--port` or `-P` changes the port (source: Usage doc page, "serve" section).
5. **Draft support** -- `--drafts` flag includes draft posts in the served site (source: Getting Started page, "Preview" section).
6. **Interactive** -- runs until Ctrl-c is pressed (source: Usage doc page).

# Construction / Recognition

## To Construct/Create:
1. Navigate to the Cobalt project root.
2. Run `cobalt serve` to start the development server.
3. Open `http://localhost:1024` in a browser to preview the site.
4. Optionally use `cobalt serve --drafts` to include drafts.
5. Press Ctrl-c to stop.

## To Identify/Recognize:
1. Terminal output shows "Building from", "Watching", "Serving", and "Server Listening on" messages.
2. The process remains running, watching for file changes.

# Context & Application

- **Typical contexts**: Local development and content authoring, previewing changes before publishing.
- **Common applications**: Writing and reviewing blog posts, iterating on layout and styling, testing draft content with `--drafts`.

# Examples

**Example 1** (source: Usage doc page): Basic serve:
```console
$ cobalt serve
Building from `.` into `/tmp/.tmpgYpScM`
Watching . for changes
Serving /tmp/.tmpgYpScM through static file server
Server Listening on http://localhost:1024
Ctrl-c to stop the server
```

**Example 2** (source: Getting Started page): Serve with drafts visible:
```console
$ cobalt serve --drafts
```

# Relationships

## Builds Upon
- **cobalt init** -- a site must be initialized before serving
- **Installation** -- Cobalt must be installed

## Enables
- Local development and preview workflow
- Draft content review (with `--drafts` flag)

## Related
- **cobalt-build** -- both produce HTML output from source, but for different purposes
- **source-directory** -- serve watches and builds from the source directory
- **destination-directory** -- serve uses a temporary destination rather than the configured one

## Contrasts With
- **cobalt build** -- `build` is a one-shot operation that writes to the configured destination directory (`_site` by default) for deployment; `serve` builds to a temporary directory, adds file watching, and runs a local web server for development

# Common Errors

- **Error**: Draft posts do not appear when running `cobalt serve`.
  **Correction**: Pass the `--drafts` flag: `cobalt serve --drafts` (source: Getting Started page).

- **Error**: Port 1024 is already in use.
  **Correction**: Use the `--port` or `-P` flag to specify a different port: `cobalt serve --port 3000`.

# Common Confusions

- **Confusion**: `cobalt serve` writes to the `_site` destination directory.
  **Clarification**: `cobalt serve` builds to a temporary directory (e.g., `/tmp/.tmpgYpScM`), not to `_site`. Use `cobalt build` to write to the configured destination directory.

- **Confusion**: `cobalt serve` is required for deployment.
  **Clarification**: `cobalt serve` is for local development only. For deployment, use `cobalt build` to generate the site in `_site`.

# Source Reference

Usage doc page, "serve" section; Getting Started page, "Preview" section. Source: Cobalt documentation.

# Verification Notes

- Definition source: Direct from Usage doc page ("serve" section) and Getting Started page
- Confidence rationale: High -- the serve command behavior is documented with explicit output examples
- Uncertainties: None significant
- Cross-reference status: References to cobalt-build, cobalt-init, installation, source-directory, destination-directory verified against planned card slugs
