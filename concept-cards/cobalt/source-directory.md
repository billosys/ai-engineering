---
# === CORE IDENTIFICATION ===
concept: Source Directory
slug: source-directory

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
  - "source"
  - "content root"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - directory-structure
extends: []
related:
  - destination-directory
  - cobalt-build
  - cobalt-serve
  - cobalt-configuration-file
contrasts_with:
  - destination-directory

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is the directory structure of a Cobalt project?"
  - "What must I know before creating a Cobalt site?"
---

# Quick Definition

The source directory (`.` by default) is the root directory where all content, templates, and assets for a Cobalt site reside, and its file hierarchy is mirrored in the destination output.

# Core Definition

The source directory is the root from which Cobalt reads all content files, layouts, includes, data, and assets. It defaults to `.` (the current directory, which is also where `_cobalt.yml` lives) and can be changed via the `source` setting in `_cobalt.yml`. The Configuration doc page describes it as: "Directory, relative to `_cobalt.yml`, where content lives" (source: Configuration doc page, "Build options" section). Cobalt "mirrors your source file hierarchy in the destination" (source: Directory doc page), so the organization of files within the source directory directly determines the URL structure of the generated site.

# Prerequisites

- **Directory Structure** -- understanding the overall Cobalt project layout

# Key Properties

1. **Default value is `.`** -- the source defaults to the directory containing `_cobalt.yml` (source: Configuration doc page, default `_cobalt.yml` listing).
2. **Configurable** -- "Can be modified in `_cobalt.yml`" via the `source` setting (source: Directory doc page, Configuration doc page).
3. **Hierarchy mirroring** -- "cobalt mirrors your source file hierarchy in the destination" (source: Directory doc page).
4. **Contains all site resources** -- the source directory encompasses content files, underscore-prefixed special directories, and asset files.
5. **Watched by serve** -- `cobalt serve` watches the source directory for changes: "Watching . for changes" (source: Usage doc page, "serve" section).

# Construction / Recognition

## To Construct/Create:
1. By default, the project root (where `_cobalt.yml` lives) is the source directory.
2. To use a different source, set `source: "path"` in `_cobalt.yml`.

## To Identify/Recognize:
1. The source directory is the location specified by the `source` setting in `_cobalt.yml` (default `.`).
2. It contains content files (`.md`, `.liquid`) and the special underscore-prefixed directories.

# Context & Application

- **Typical contexts**: Understanding where to place content files and resources in a Cobalt project.
- **Common applications**: Organizing site content, configuring build paths, structuring multi-directory projects.

# Examples

**Example 1** (source: Configuration doc page): Default source configuration:
```yml
source: "."
```

**Example 2** (source: Usage doc page): `cobalt serve` output showing the source directory:
```console
$ cobalt serve
Building from `.` into `/tmp/.tmpgYpScM`
Watching . for changes
```

# Relationships

## Builds Upon
- **directory-structure** -- the source directory is the root of the Cobalt directory structure

## Enables
- **cobalt-build** -- build reads from the source directory
- **cobalt-serve** -- serve watches and reads from the source directory

## Related
- **cobalt-configuration-file** -- the `source` setting in `_cobalt.yml` configures the source directory
- **page** -- pages are content files within the source directory
- **post** -- posts live in a subdirectory of the source

## Contrasts With
- **destination-directory** -- the source directory holds input content; the destination directory holds generated output

# Common Errors

- **Error**: Placing `_cobalt.yml` in a different directory than the source and not updating the `source` path.
  **Correction**: Ensure the `source` setting in `_cobalt.yml` is a correct relative path from the config file to the content directory.

# Common Confusions

- **Confusion**: The source directory only contains content files.
  **Clarification**: The source directory contains everything: content files, layouts (`_layouts`), includes (`_includes`), data (`_data`), sass (`_sass`), defaults (`_defaults`), and assets. The underscore-prefixed directories within it are processed specially but are still part of the source.

# Source Reference

Directory Structure doc page; Configuration doc page, "Build options" section. Source: Cobalt documentation.

# Verification Notes

- Definition source: Direct from Directory doc page and Configuration doc page
- Confidence rationale: High -- the source directory concept is clearly defined with its default value and configurability
- Uncertainties: None significant
- Cross-reference status: References to directory-structure, destination-directory, cobalt-build, cobalt-serve, cobalt-configuration-file verified against planned card slugs
