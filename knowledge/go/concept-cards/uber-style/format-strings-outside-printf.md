---
concept: Format Strings outside Printf
slug: format-strings-outside-printf
category: style
subcategory: string-formatting
tier: foundational
source: "Uber Go Style Guide"
source_slug: uber-style
authors: "Prashant Varanasi, Simon Newton"
chapter: "Style"
chapter_number: 4
pdf_page: null
section: "Format Strings outside Printf"
extraction_confidence: high
aliases:
  - Printf format string constants
prerequisites: []
extends: []
related:
  - naming-printf-style-functions
contrasts_with: []
answers_questions:
  - "How should I declare Printf format strings outside the call?"
---

# Quick Definition

When declaring format strings for `Printf`-style functions outside a string literal, declare them as `const` values. This enables `go vet` to perform static analysis on the format string.

# Core Definition

The Uber Go Style Guide requires that format strings used with `Printf`-style functions be declared as `const` when stored in a variable. Using `const` instead of `var` allows `go vet` to perform static analysis of the format string, catching mismatches between format verbs and arguments at build time.

# Prerequisites

- Familiarity with `fmt.Printf` and format verbs (`%v`, `%s`, `%d`, etc.)
- Understanding of `go vet` as a static analysis tool

# Key Properties

1. **`const` enables static analysis**: `go vet` can analyze `const` format strings but not `var` format strings.
2. **Catches format/argument mismatches**: Static analysis detects issues like wrong verb types or incorrect argument counts.
3. **Applies to all Printf-style functions**: Not just `fmt.Printf` but any function following the Printf convention.

# Construction / Recognition

**Good -- const format string:**

```go
const msg = "unexpected values %v, %v\n"
fmt.Printf(msg, 1, 2)
```

**Bad -- var format string:**

```go
msg := "unexpected values %v, %v\n"
fmt.Printf(msg, 1, 2)
```

# Context & Application

This applies whenever a format string is extracted into a variable rather than used inline. Inline format strings (passed directly to `Printf`) are already checked by `go vet`. The issue arises only when the format string is stored in a variable before use.

# Examples

See Construction / Recognition above.

# Relationships

- **naming-printf-style-functions**: Complements this guideline by ensuring custom Printf-style functions are named so `go vet` can find and check them.

# Common Errors

1. Declaring format strings with `:=` or `var` -- prevents `go vet` from catching format/argument mismatches.

# Common Confusions

- **Inline format strings are fine**: This guideline only applies when the format string is stored in a variable. `fmt.Printf("unexpected values %v, %v\n", 1, 2)` is already checked by `go vet`.

# Source Reference

Uber Go Style Guide, "Style" chapter, "Format Strings outside Printf" section.

# Verification Notes

Confidence: high. The guideline and code example are directly from the source text with an explicit Bad/Good comparison.
