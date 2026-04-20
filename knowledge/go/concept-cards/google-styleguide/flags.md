---
# === CORE IDENTIFICATION ===
concept: Flag Definitions and Conventions
slug: flags

# === CLASSIFICATION ===
category: libraries
subcategory: command-line
tier: intermediate

# === PROVENANCE ===
source: "Google Go Style Guide"
source_slug: google-styleguide
authors: "Google Go Style Team"
chapter: "Style Decisions"
chapter_number: 3
pdf_page: null
section: "Flags"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "command-line flags"
  - "flag package usage"
  - "flag definitions"

# === TYPED RELATIONSHIPS ===
prerequisites: []
extends: []
related:
  - contexts
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "Where should flags be defined in a Go program?"
  - "What naming convention should flag names follow?"
  - "Why shouldn't library packages define flags?"
  - "How should flag variables be named versus flag strings?"
---

# Quick Definition

Define flags only in `package main` or equivalent. Use snake_case for flag names and camelCase for the Go variables that hold them. Never let importing a library register new flags as a side effect.

# Core Definition

Flag names in Go binaries should use underscores to separate words (snake_case), while the Go variables holding flag values should follow standard Go naming conventions (mixedCaps/camelCase). Flags must only be defined in `package main` or equivalent. General-purpose library packages should be configured through Go APIs (function arguments, struct fields), not by registering flags that become global side effects of importing the library. If flags are global variables, they should be placed in their own `var` group following the imports section.

# Prerequisites

- **Go flag package** -- Familiarity with the standard `flag` package interface
- **Package design** -- Understanding of Go package boundaries and import side effects

# Key Properties

1. **Flag name style**: Use snake_case for the flag string (e.g., `"poll_interval"`)
2. **Variable name style**: Use camelCase for the Go variable (e.g., `pollInterval`)
3. **Main package only**: Flags must only be defined in `package main` or equivalent
4. **No library flags**: Libraries should not export flags as side effects of importing
5. **Grouped declarations**: Place flag variables in their own `var` group after imports
6. **Clear naming for exceptions**: If a library must define a flag, the flag name must clearly indicate which package it configures

# Construction / Recognition

## To Apply:
1. Define all flags in `package main`
2. Use snake_case for flag name strings, camelCase for Go variables
3. Configure library packages through explicit function arguments or struct fields
4. Group flag variables together after imports

## To Recognize:
1. Flags defined in non-main packages are a violation
2. Flag names using camelCase (e.g., `"pollInterval"`) violate naming conventions
3. Go variables using snake_case (e.g., `poll_interval`) violate Go naming conventions

# Context & Application

This guidance prevents the "flag pollution" problem where importing a library silently registers command-line flags. This creates tight coupling between packages and makes flag conflicts difficult to diagnose. The separation of concerns keeps command-line interface concerns in main while libraries remain configurable through standard Go APIs.

# Examples

**Example 1 -- Correct flag definition**:

```go
// Good:
var (
    pollInterval = flag.Duration("poll_interval", time.Minute, "Interval to use for polling.")
)
```

**Example 2 -- Incorrect naming and style**:

```go
// Bad:
var (
    poll_interval = flag.Int("pollIntervalSeconds", 60, "Interval to use for polling in seconds.")
)
```

# Relationships

## Related
- **contexts** -- Like flags, contexts address how configuration and state flow through programs

# Common Errors

- **Error**: Defining flags in library packages
  **Correction**: Configure libraries through Go APIs (function arguments, struct fields, or exported global variables under strict scrutiny).

- **Error**: Using camelCase for flag name strings
  **Correction**: Use snake_case for the flag name string; reserve camelCase for the Go variable.

# Common Confusions

- **Confusion**: Thinking the flag name and variable name should match in style
  **Clarification**: They deliberately differ: flag names are snake_case (for CLI convention) while variables are camelCase (for Go convention).

# Source Reference

Chapter 3: Style Decisions, Section "Flags" under "Common libraries".

# Verification Notes

- Definition source: Directly from the "Flags" section of the Style Decisions document
- Confidence rationale: HIGH -- the guidance is explicit with clear good/bad examples
- Uncertainties: None
- Cross-reference status: References Go Tips #10 and #80, and best practices on complex CLIs
