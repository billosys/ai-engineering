---
# === CORE IDENTIFICATION ===
concept: Top-Level Suppressions
slug: top-level-suppressions

# === CLASSIFICATION ===
category: analyzer
subcategory: suppressions
tier: intermediate

# === PROVENANCE ===
source: "Biome Documentation"
source_slug: biome
authors: "Biome Contributors"
chapter: "analyzer/suppressions.mdx"
chapter_number: null
pdf_page: null
section: "Top-level suppressions"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - biome-ignore-all
  - file-level suppressions

# === TYPED RELATIONSHIPS ===
prerequisites:
  - suppression-comments
extends:
  - suppression-comments
related:
  - inline-suppressions
  - range-suppressions
contrasts_with:
  - inline-suppressions
  - range-suppressions

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do I suppress a lint rule for a line, range, or file?"
  - "What distinguishes inline, top-level, and range suppressions?"
---

# Quick Definition
Top-level suppressions use `biome-ignore-all` at the top of a file to disable a lint rule or assist action for the entire file.

# Core Definition
Top-level suppressions disable a lint rule for an entire file. They must be placed at the top of the file and use the `biome-ignore-all` prefix. They are useful when you want to suppress a rule for a particular file without relying on a configuration override.

# Prerequisites
- suppression-comments (the suppression system and syntax)

# Key Properties
1. Uses the `biome-ignore-all` prefix
2. Must be placed at the top of the file
3. Applies to all lines in the file
4. If not at the top of the file, Biome considers it unused and emits a `suppression/unused` diagnostic
5. Useful for generated files or files that legitimately need blanket rule exemption

# Construction / Recognition
Place `biome-ignore-all` at the very top of the file:
```js
// biome-ignore-all lint/suspicious/noDebugger: reason
debugger;
debugger;
```

# Context & Application
Ideal for generated files, vendor files, or files with known intentional violations throughout. Provides a per-file alternative to configuration overrides.

# Examples
From `analyzer/suppressions.mdx`:
```js
// biome-ignore-all lint/suspicious/noDebugger: reason
debugger;
debugger;
```
Both `debugger` statements are suppressed for the entire file `generated.js`.

When a top-level suppression isn't at the top of the file, Biome emits a diagnostic with category `suppression/unused`.

# Relationships
## Builds Upon
- suppression-comments (shared suppression syntax and engine)

## Enables
- File-wide rule exemption without configuration changes

## Related
- inline-suppressions (per-line suppression)
- range-suppressions (multi-line suppression)

## Contrasts With
- inline-suppressions: only suppress the next line, not the whole file
- range-suppressions: suppress a defined range, not the whole file

# Common Errors
1. Placing `biome-ignore-all` anywhere other than the top of the file — Biome will flag it as unused
2. Using `biome-ignore` (inline) when the entire file needs suppression

# Common Confusions
1. Thinking top-level suppressions work regardless of position — they must be at the top of the file

# Source Reference
- `sources-md/biome/analyzer/suppressions.mdx`, section "Top-level suppressions"

# Verification Notes
Directly extracted. The top-of-file requirement and unused diagnostic behavior are explicitly documented.
