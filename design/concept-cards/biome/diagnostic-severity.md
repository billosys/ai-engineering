---
# === CORE IDENTIFICATION ===
concept: Diagnostic Severity
slug: diagnostic-severity

# === CLASSIFICATION ===
category: diagnostics
subcategory: severity
tier: intermediate

# === PROVENANCE ===
source: "Biome Documentation"
source_slug: biome
authors: "Biome Contributors"
chapter: "reference/diagnostics.mdx"
chapter_number: null
pdf_page: null
section: "Diagnostic severity"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - severity levels

# === TYPED RELATIONSHIPS ===
prerequisites:
  - biome-diagnostics
extends:
  - biome-diagnostics
related:
  - diagnostic-tags
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What distinguishes error, warning, and info severity?"
  - "What is a diagnostic in Biome?"
---

# Quick Definition
Diagnostic severity classifies Biome diagnostics into four levels — Fatal, Error, Warning, and Information — which determine their visual presentation and impact on CLI behavior.

# Core Definition
The severity of a diagnostic affects both its visual presentation and CLI behavior. Biome defines four severity levels: Fatal (unexpected internal errors, red text with fatal tag), Error (issues that should be addressed and cause CLI to exit with error code, red text), Warning (issues that should be addressed but are non-blocking, yellow text), and Information (useful context that doesn't block CLI, green text).

# Prerequisites
- biome-diagnostics (the diagnostic system)

# Key Properties
1. **Fatal**: Red text; emitted for unexpected internal Biome errors; carries the fatal tag
2. **Error**: Red text; should be addressed; causes CLI to exit with an error code
3. **Warning**: Yellow text; should be addressed; non-blocking, won't stop the CLI
4. **Information**: Green text; provides useful information; not meant to block the CLI
5. Severity directly affects whether CI/CLI pipelines pass or fail
6. Fatal diagnostics are a superset of Error with the additional fatal tag

# Construction / Recognition
Severity is assigned automatically by the tool emitting the diagnostic. In terminal output:
- Red text = Fatal or Error
- Yellow text = Warning
- Green text = Information

Fatal diagnostics are distinguished from Error diagnostics by the presence of the fatal tag.

# Context & Application
Understanding severity is critical for CI pipeline configuration. Error and Fatal diagnostics will cause non-zero exit codes, failing builds. Warnings provide actionable feedback without blocking. Information diagnostics are purely informational.

# Examples
From `reference/diagnostics.mdx`:

- Fatal diagnostics are "usually emitted when an unexpected error occurred inside Biome"
- Error diagnostics "should be addressed because they will emit an error code when encountered by the CLI"
- Warning diagnostics "are not blockers, and they won't stop the CLI from working"
- Information diagnostics "provide useful information and they aren't meant to block the CLI"

# Relationships
## Builds Upon
- biome-diagnostics (the diagnostic system that carries severity)

## Enables
- Understanding which issues block CI and which are advisory

## Related
- diagnostic-tags (additional metadata like Fixable, Verbose)

## Contrasts With
Each level contrasts with the others in terms of blocking behavior and visual color coding.

# Common Errors
1. Treating warnings as ignorable — they should still be addressed even though they don't block
2. Panicking at Fatal diagnostics — these indicate Biome bugs, not user errors

# Common Confusions
1. Confusing Fatal with Error — Fatal is for unexpected internal Biome errors, Error is for user-addressable issues
2. Assuming warnings will cause CI failure — only Error and Fatal cause non-zero exit codes

# Source Reference
- `sources-md/biome/reference/diagnostics.mdx`, section "Diagnostic severity"

# Verification Notes
All four severity levels and their behaviors are explicitly documented in the source.
