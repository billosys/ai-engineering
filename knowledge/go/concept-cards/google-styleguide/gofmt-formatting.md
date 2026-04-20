---
# === CORE IDENTIFICATION ===
concept: Gofmt Formatting
slug: gofmt-formatting

# === CLASSIFICATION ===
category: language
subcategory: formatting
tier: foundational

# === PROVENANCE ===
source: "Google Go Style Guide"
source_slug: google-styleguide
authors: "Google Go Style Team"
chapter: "Guide"
chapter_number: 2
pdf_page: null
section: "Core guidelines"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "gofmt"
  - "Go formatting"
  - "automatic formatting"

# === TYPED RELATIONSHIPS ===
prerequisites: []
extends: []
related:
  - consistency-principle
  - line-length-philosophy
  - mixedcaps-naming
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "Must all Go source code be formatted with gofmt?"
  - "Should generated Go code also be formatted?"
  - "How is gofmt formatting enforced at Google?"
---

# Quick Definition

All Go source files must conform to the format output by the `gofmt` tool. This is a non-negotiable rule enforced by presubmit checks. Generated code should generally also be formatted.

# Core Definition

All Go source files must conform to the format outputted by the `gofmt` tool. At Google, this is enforced by a presubmit check. Generated code should generally also be formatted (e.g., by using `format.Source`), as it is browsable in Code Search. This is one of the "core guidelines" -- the most important aspects of Go style that all code is expected to follow. These core guidelines are expected to be learned and followed by the time readability is granted and are not expected to change frequently.

# Prerequisites

- **Go toolchain** -- The `gofmt` tool is part of the standard Go distribution

# Key Properties

1. All Go source files must conform to `gofmt` output
2. Enforced by presubmit checks at Google
3. Generated code should also be formatted (using `format.Source`)
4. Part of "Core guidelines" -- highest importance, rarely changes
5. Non-negotiable; no exceptions for stylistic preference

# Construction / Recognition

## To Apply:
1. Run `gofmt` on all Go source files before committing
2. Configure your editor to run `gofmt` on save
3. For generated code, use `format.Source` to format programmatically
4. Set up presubmit checks to enforce formatting

## To Recognize:
1. Files that produce a diff when `gofmt` is run indicate a violation
2. Generated code that is not formatted will appear inconsistent in code browsing tools

# Context & Application

Gofmt eliminates an entire class of style debates (brace placement, spacing, alignment) by providing a single canonical format. As the Go proverb says, "Gofmt's style is no one's favorite, yet gofmt is everyone's favorite." The value is in uniformity, not in any particular formatting choice. This is the mechanical foundation upon which all other style guidance builds.

# Examples

**Example 1 -- Running gofmt**:

```bash
gofmt -w myfile.go
```

This reformats the file in place to match the canonical `gofmt` output.

**Example 2 -- Formatting generated code programmatically**:

```go
import "go/format"

formatted, err := format.Source(generatedCode)
```

# Relationships

## Related
- **consistency-principle** -- Gofmt is the ultimate consistency enforcer for formatting
- **line-length-philosophy** -- Line length is not enforced by gofmt; it is a separate concern
- **mixedcaps-naming** -- Another core guideline alongside gofmt

# Common Errors

- **Error**: Manually formatting code in a style that gofmt would change
  **Correction**: Always run gofmt; do not fight its output

- **Error**: Leaving generated code unformatted
  **Correction**: Use `format.Source` to format generated Go code

# Common Confusions

- **Confusion**: Thinking gofmt handles all style concerns
  **Clarification**: Gofmt handles mechanical formatting (indentation, spacing, braces) but not naming, structure, or other style decisions

- **Confusion**: Believing gofmt is optional or advisory
  **Clarification**: At Google, gofmt conformance is enforced by presubmit checks. It is mandatory.

# Source Reference

Chapter 2: Guide, Section "Core guidelines" > "Formatting".

# Verification Notes

- Definition source: Directly from the "Formatting" section of Core guidelines
- Confidence rationale: HIGH -- a single clear, unambiguous rule
- Uncertainties: None
- Cross-reference status: Related slugs verified against planned extractions
