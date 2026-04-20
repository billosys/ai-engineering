---
# === CORE IDENTIFICATION ===
concept: Cobalt
slug: cobalt

# === CLASSIFICATION ===
category: cli
subcategory: overview
tier: foundational

# === PROVENANCE ===
source: "Cobalt Static Site Generator Documentation"
source_slug: cobalt
authors: "Cobalt contributors (cobalt-org)"
chapter: "Getting Started"
chapter_number: null
pdf_page: null
section: null

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "cobalt.rs"
  - "Cobalt SSG"

# === TYPED RELATIONSHIPS ===
prerequisites: []
extends: []
related:
  - installation
  - cobalt-init
  - cobalt-build
  - cobalt-serve
  - cobalt-debug
  - directory-structure
  - cobalt-configuration-file
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is Cobalt?"
  - "What must I know before creating a Cobalt site?"
---

# Quick Definition

Cobalt is a static site generator written in Rust that transforms Markdown and Liquid templates into a complete HTML website ready for deployment.

# Core Definition

Cobalt is a static site generator from the cobalt-org project (hosted at github.com/cobalt-org/cobalt.rs). It takes content written in Markdown and Liquid template files, processes them through a pipeline of template evaluation, Markdown-to-HTML conversion, and layout wrapping, and produces a directory of static HTML files suitable for serving by any web server. Cobalt supports pages, blog posts with draft/publish workflows, layouts, includes, data files, Sass compilation, and syntax highlighting. It runs on Windows, Linux, and macOS (source: Install doc page).

# Prerequisites

Foundational concept with no prerequisites. Cobalt is the root concept for the entire Cobalt static site generator ecosystem.

# Key Properties

1. **Written in Rust** -- Cobalt is implemented in Rust, with the crate name `cobalt-bin` on crates.io.
2. **Markdown and Liquid** -- Content is authored in Markdown; templating uses the Liquid template language.
3. **Convention-based directory structure** -- Cobalt uses underscore-prefixed directories (`_layouts`, `_includes`, `_data`, etc.) for site generation resources, mirroring the source hierarchy in the output (source: Directory doc page).
4. **Draft/publish workflow** -- Posts can be created as drafts and later published, with automatic date stamping (source: Getting Started page).
5. **Cross-platform** -- Supports Windows, Linux, and macOS (source: Install doc page).
6. **CLI-driven** -- All operations (init, build, serve, new, publish, clean, debug) are performed through the `cobalt` command-line tool.

# Construction / Recognition

## To Construct/Create:
1. Install the `cobalt` binary (via OS package, pre-built binary, cargo install, or from source).
2. Run `cobalt init` to scaffold a new site with example pages, posts, and layouts.
3. Author content in Markdown files with Liquid frontmatter.
4. Run `cobalt build` to generate the static site into the destination directory.

## To Identify/Recognize:
1. A project using Cobalt will contain a `_cobalt.yml` configuration file in its root.
2. The directory structure will include underscore-prefixed directories such as `_layouts`, `_includes`, and `_site`.
3. Content files will use `.md` or `.liquid` extensions with YAML frontmatter.

# Context & Application

- **Typical contexts**: Personal blogs, project documentation sites, portfolios, and any scenario where a lightweight static site generator is preferred.
- **Common applications**: Building and deploying static websites from Markdown content, blogging with a draft/publish workflow, generating sites for GitHub Pages or similar static hosting.

# Examples

**Example 1** (source: Getting Started page): A complete workflow from installation to build:
```console
$ mkdir myBlog && cd myBlog
$ cobalt init
$ cobalt serve
$ cobalt new "Cats Around the World"
$ cobalt publish posts/cats-around-the-world.md
$ cobalt build
```
The site is then available in `_site` and ready to be uploaded.

# Relationships

## Builds Upon
- No prerequisites -- this is the root concept.

## Enables
- **Installation** -- must install Cobalt before using it
- **cobalt init** -- initializes a new Cobalt site
- **cobalt build** -- builds the site from source to output
- **cobalt serve** -- serves the site locally for preview
- **Directory Structure** -- understanding the Cobalt project layout

## Related
- **cobalt-configuration-file** -- the `_cobalt.yml` file that configures site-wide options
- **liquid-template-language** -- the templating engine used by Cobalt
- **content-processing-pipeline** -- the transformation pipeline that processes content files

## Contrasts With
- No direct contrasts within the Cobalt documentation scope.

# Common Errors

- **Error**: Trying to use Cobalt commands without first initializing a site.
  **Correction**: Run `cobalt init` in an empty directory before attempting `cobalt build` or `cobalt serve`.

# Common Confusions

- **Confusion**: Cobalt is the same as other Ruby-based static site generators like Jekyll.
  **Clarification**: While Cobalt shares similar concepts (Liquid templates, frontmatter, layouts), it is written in Rust and uses the crate name `cobalt-bin`. Its directory conventions are similar to but distinct from Jekyll.

# Source Reference

Getting Started, Installation, Usage, and Directory Structure pages. Source: Cobalt documentation.

# Verification Notes

- Definition source: Synthesized from multiple documentation pages (Getting Started, Install, Usage, Directory)
- Confidence rationale: High -- Cobalt's identity and purpose are clearly documented across multiple pages
- Uncertainties: The documentation does not include an explicit "What is Cobalt?" definition paragraph; the description is synthesized from context across pages
- Cross-reference status: References to installation, cobalt-init, cobalt-build, cobalt-serve, directory-structure, and cobalt-configuration-file all correspond to planned card slugs
