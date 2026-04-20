---
# === CORE IDENTIFICATION ===
concept: Use %q for String Formatting
slug: use-percent-q

# === CLASSIFICATION ===
category: language
subcategory: formatting-verbs
tier: foundational

# === PROVENANCE ===
source: "Google Go Style Guide"
source_slug: google-styleguide
authors: "Google Go Style Team"
chapter: "Style Decisions"
chapter_number: 3
pdf_page: null
section: "Use %q"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "percent q"
  - "%q verb"
  - "quoted string formatting"

# === TYPED RELATIONSHIPS ===
prerequisites: []
extends: []
related:
  - test-failure-messages
  - test-comparisons
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "When should I use %q instead of %s in Go?"
  - "How do I make empty strings visible in Go output?"
  - "How do I detect invisible characters in Go string output?"
  - "What is the best way to format strings in test failure messages?"
---

# Quick Definition

Use Go's `%q` format verb instead of `%s` to print strings inside double-quotation marks, making boundaries visible and invisible characters detectable.

# Core Definition

Go's `fmt` format functions provide a `%q` verb that prints strings enclosed in double-quotation marks with special characters escaped. This is preferred over manually wrapping strings with quotes using `%s`. The `%q` verb is especially recommended in output intended for humans where the input value could be empty or contain control characters. An empty string formatted with `%q` renders as `""`, which stands out clearly, whereas `%s` would produce nothing visible.

# Prerequisites

- **Go fmt package basics** -- Familiarity with `fmt.Printf`, `fmt.Sprintf`, and format verbs

# Key Properties

1. **Automatic quoting**: `%q` wraps the string in double-quotes without manual escaping
2. **Empty string visibility**: An empty string renders as `""` rather than invisible nothing
3. **Control character escaping**: Non-printable characters are escaped so they become visible
4. **Boundary detection**: Quote marks clearly delimit where a string value begins and ends

# Construction / Recognition

## To Apply:
1. Use `%q` whenever printing string values in human-readable output
2. Replace manual quoting patterns like `\"%s\"` or `'%s'` with `%q`
3. Prefer `%q` in test failure messages for string comparisons

## To Recognize:
1. Code using `fmt.Printf("value %q ...", str)` is applying this pattern correctly
2. Code using `fmt.Printf("value \"%s\" ...", str)` or `'%s'` is the anti-pattern

# Context & Application

This pattern is particularly valuable in test failure messages and logging where you need to diagnose issues involving whitespace, empty strings, or invisible characters. When a test fails with `got "" want "hello"`, the empty string is immediately visible. Without `%q`, the output might read `got  want hello`, making it hard to see the empty value.

# Examples

**Example 1 -- Correct usage with %q**:

```go
// Good:
fmt.Printf("value %q looks like English text", someText)
```

**Example 2 -- Anti-pattern with manual quoting**:

```go
// Bad:
fmt.Printf("value \"%s\" looks like English text", someText)
// Also bad:
fmt.Printf("value '%s' looks like English text", someText)
```

# Relationships

## Related
- **test-failure-messages** -- Test failure messages benefit from `%q` for string values
- **test-comparisons** -- When comparing string results, `%q` helps clarify mismatches

# Common Errors

- **Error**: Using `%s` for string values in test failure messages
  **Correction**: Use `%q` to make empty strings and whitespace issues immediately visible.

- **Error**: Manually wrapping strings in quotes with escaped quote characters
  **Correction**: Let `%q` handle quoting automatically; it also escapes control characters.

# Common Confusions

- **Confusion**: Thinking `%q` and `"%s"` produce identical output
  **Clarification**: `%q` also escapes control characters and special characters within the string, whereas manual quoting with `%s` does not.

# Source Reference

Chapter 3: Style Decisions, Section "Use %q".

# Verification Notes

- Definition source: Directly from the "Use %q" section of the Style Decisions document
- Confidence rationale: HIGH -- the guidance is explicit with clear good/bad examples
- Uncertainties: None
- Cross-reference status: Related to test failure message guidance in the same chapter
