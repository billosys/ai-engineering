---
# === CORE IDENTIFICATION ===
concept: Biome Diagnostics
slug: biome-diagnostics

# === CLASSIFICATION ===
category: diagnostics
subcategory: null
tier: foundational

# === PROVENANCE ===
source: "Biome Documentation"
source_slug: biome
authors: "Biome Contributors"
chapter: "reference/diagnostics.mdx"
chapter_number: null
pdf_page: null
section: null

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - diagnostics

# === TYPED RELATIONSHIPS ===
prerequisites:
  - biome
extends: []
related:
  - diagnostic-severity
  - diagnostic-tags
  - biome-linter
  - biome-assist
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is a diagnostic in Biome?"
---

# Quick Definition
Biome diagnostics are structured messages that convey errors, warnings, information, and tips, providing all the context needed to understand and fix issues.

# Core Definition
Biome's diagnostics are rich, structured messages used not only for errors but also for warnings, information, and tips. Each diagnostic can contain several parts: severity, tags (metadata), a category, a location (resource, source code, and span), and advices (additional messages appended after the original message).

# Prerequisites
Requires understanding of Biome as a toolchain.

# Key Properties
1. Diagnostics carry a severity level: Fatal, Error, Warning, or Information
2. Tags attach metadata: Verbose, Internal, Fixable, Deprecated
3. Categories group diagnostics (e.g., `check`, `lint/a11y/noAccessKey`) and may include links
4. Location consists of three optional parts: resource (file path), source code, and span (line and column)
5. Advices are additional messages of various kinds appended after the main message
6. Error diagnostics force the CLI to exit with an error code
7. IDE terminals allow clicking file paths with line/column to navigate to the source

# Construction / Recognition
Diagnostics are emitted automatically by Biome tools (linter, formatter, assist, check). The file path appears at the top left. Line and column appear beside the file path when source code is associated. Advices appear below the main diagnostic message.

# Context & Application
Understanding diagnostic structure is essential for interpreting Biome output in CLI and IDE contexts. The severity determines whether the CI pipeline will fail (errors) or merely warn. Tags provide quick metadata about whether an issue is fixable, internal, or verbose.

# Examples
From `reference/diagnostics.mdx`:

- A diagnostic with category `check` is emitted when running the `check` command
- A diagnostic with category `lint/a11y/noAccessKey` includes a link to the lint rule's documentation
- File path is usually the first information at the top left of the diagnostic
- Clicking `path/to/file.js:2:2` in an IDE terminal opens the file at that location

# Relationships
## Builds Upon
- biome (the toolchain that produces diagnostics)

## Enables
- diagnostic-severity (understanding severity levels)
- diagnostic-tags (understanding metadata tags)

## Related
- biome-linter (produces lint diagnostics)
- biome-assist (produces assist diagnostics)
- suppression-comments (suppress specific diagnostics)

## Contrasts With
None directly.

# Common Errors
1. Ignoring verbose diagnostics that require the `--verbose` flag to see
2. Not recognizing that error-level diagnostics will cause CLI to exit with a non-zero code

# Common Confusions
1. Thinking diagnostics are only for errors — they also carry warnings, information, and tips
2. Confusing the diagnostic category with the diagnostic severity — category groups diagnostics, severity indicates impact

# Source Reference
- `sources-md/biome/reference/diagnostics.mdx`

# Verification Notes
Extracted from the diagnostics reference page. All structural components (severity, tags, category, location, advices) are explicitly documented.
