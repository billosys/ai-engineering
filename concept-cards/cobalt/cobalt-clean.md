---
# === CORE IDENTIFICATION ===
concept: cobalt clean
slug: cobalt-clean

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
section: "clean"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "clean command"
  - "prune destination"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - installation
extends: []
related:
  - cobalt-build
  - destination-directory
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do I clean the build output of a Cobalt site?"
---

# Quick Definition

`cobalt clean` removes the contents of the destination directory, clearing all previously built output files.

# Core Definition

The `cobalt clean` command "Cleans/prunes the `destination` directory" (source: Usage doc page, "clean" section). It removes the generated output files produced by `cobalt build`, effectively resetting the destination directory (default: `_site`). This is useful for ensuring a fresh build without leftover artifacts from previous builds.

# Prerequisites

- **Installation** -- Cobalt must be installed

# Key Properties

1. **Prunes destination** -- removes files from the destination directory (source: Usage doc page, "clean" section).
2. **Targets configured destination** -- operates on the destination directory as configured in `_cobalt.yml` (default: `_site`).
3. **Simple operation** -- no additional flags or options are documented.

# Construction / Recognition

## To Construct/Create:
1. Run `cobalt clean` from the project root directory.
2. The destination directory contents are removed.

## To Identify/Recognize:
1. After running `cobalt clean`, the destination directory (`_site` by default) is empty or removed.

# Context & Application

- **Typical contexts**: Performing a clean build, troubleshooting build issues caused by stale output files, resetting the output directory.
- **Common applications**: Running before `cobalt build` to ensure no leftover files from previous builds, cleaning up after experimentation.

# Examples

**Example 1** (source: Usage doc page): Clean the destination directory:
```console
$ cobalt clean
```

**Example 2** (inferred from documentation): Clean then rebuild:
```console
$ cobalt clean
$ cobalt build
```

# Relationships

## Builds Upon
- **Installation** -- Cobalt must be installed

## Enables
- **cobalt build** -- cleaning before building ensures a fresh output

## Related
- **destination-directory** -- clean operates on the destination directory
- **cobalt-build** -- clean is typically used in conjunction with build

## Contrasts With
- No direct contrasts within scope.

# Common Errors

- **Error**: Running `cobalt clean` when the destination directory has been changed from the default without updating `_cobalt.yml`.
  **Correction**: Ensure the `destination` setting in `_cobalt.yml` matches the actual output directory, so `cobalt clean` targets the correct location.

# Common Confusions

- **Confusion**: `cobalt clean` also removes source files.
  **Clarification**: `cobalt clean` only removes files in the destination directory (build output). Source files, layouts, includes, and configuration are not affected.

# Source Reference

Usage doc page, "clean" section. Source: Cobalt documentation.

# Verification Notes

- Definition source: Direct from Usage doc page ("clean" section)
- Confidence rationale: High -- the command is documented, though briefly; its purpose is unambiguous
- Uncertainties: The documentation is brief (one line); exact behavior (whether it deletes the directory or just its contents) is not specified
- Cross-reference status: References to installation, cobalt-build, destination-directory verified against planned card slugs
