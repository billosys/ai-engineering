---
# === CORE IDENTIFICATION ===
concept: Diagnostic Tags
slug: diagnostic-tags

# === CLASSIFICATION ===
category: diagnostics
subcategory: tags
tier: intermediate

# === PROVENANCE ===
source: "Biome Documentation"
source_slug: biome
authors: "Biome Contributors"
chapter: "reference/diagnostics.mdx"
chapter_number: null
pdf_page: null
section: "Diagnostic tags"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - diagnostic metadata

# === TYPED RELATIONSHIPS ===
prerequisites:
  - biome-diagnostics
extends:
  - biome-diagnostics
related:
  - diagnostic-severity
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is a diagnostic in Biome?"
---

# Quick Definition
Diagnostic tags are metadata labels attached to Biome diagnostics that convey additional properties such as whether the issue is fixable, verbose, internal, or involves deprecated code.

# Core Definition
Tags are metadata attached to a diagnostic that can affect how clients display or handle the diagnostic. Biome defines four tag types: Verbose (hidden by default, shown with `--verbose`), Internal (indicates an internal Biome error, users should file a bug), Fixable (the issue has a code action that can fix it), and Deprecated (the code involves deprecated features).

# Prerequisites
- biome-diagnostics (the diagnostic system)

# Key Properties
1. **Verbose**: Hidden by default; shown only with the `--verbose` CLI option
2. **Internal**: Indicates an internal Biome error; users are encouraged to file a bug report
3. **Fixable**: Indicates the diagnostic has an associated code action that can fix the issue
4. **Deprecated**: Indicates the code contains deprecated features
5. Tags are additive metadata — a diagnostic can carry multiple tags
6. Tags affect client behavior (e.g., IDEs may render fixable diagnostics with a quick-fix icon)

# Construction / Recognition
Tags are assigned automatically by Biome. In CLI output:
- Verbose diagnostics require `--verbose` to appear
- Internal diagnostics suggest filing a bug
- Fixable diagnostics indicate an available code action
- Deprecated diagnostics flag deprecated code usage

# Context & Application
Tags help users quickly triage diagnostics. The Fixable tag is especially useful because it indicates automated resolution is available. The Verbose tag filters noise in default output. The Internal tag distinguishes Biome bugs from user code issues.

# Examples
From `reference/diagnostics.mdx`:

- Verbose: "Via CLI, you can show these diagnostics using the `--verbose` option"
- Internal: "Users are usually encouraged to file a bug when they see one"
- Fixable: "Usually used for lint diagnostics that have a code action"
- Deprecated: "Diagnostics that contain code that is deprecated"

# Relationships
## Builds Upon
- biome-diagnostics (the diagnostic system that carries tags)

## Enables
- Efficient triage of diagnostics by metadata
- IDE integration (fixable tags trigger quick-fix UI)

## Related
- diagnostic-severity (severity is a separate axis from tags)

## Contrasts With
None directly; tags complement severity rather than competing with it.

# Common Errors
1. Missing verbose diagnostics because `--verbose` was not passed
2. Ignoring the Fixable tag and manually fixing something that has an automated fix

# Common Confusions
1. Confusing the Internal tag with Error severity — Internal means a Biome bug, not a user code error
2. Thinking Fixable means the fix has been applied — it means a fix is available but must be triggered

# Source Reference
- `sources-md/biome/reference/diagnostics.mdx`, section "Diagnostic tags"

# Verification Notes
All four tag types are explicitly documented with descriptions in the source.
