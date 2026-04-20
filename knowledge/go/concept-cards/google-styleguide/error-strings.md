---
concept: Error Strings
slug: error-strings
category: error-handling
subcategory: error-formatting
tier: foundational
source: "Google Go Style Guide"
source_slug: google-styleguide
authors: "Google Go Style Team"
chapter: "Style Decisions"
chapter_number: 3
pdf_page: null
section: "Error strings"
extraction_confidence: high
aliases:
  - error message formatting
  - error string conventions
prerequisites:
  - returning-errors
related:
  - handle-errors-decisions
  - indent-error-flow
contrasts_with: []
answers_questions:
  - "Should Go error strings be capitalized?"
  - "Should Go error strings end with punctuation?"
  - "Why are error strings lowercase in Go?"
---

# Quick Definition

Error strings should not be capitalized (unless starting with an exported name, proper noun, or acronym) and should not end with punctuation, because they are typically wrapped inside other context before being displayed.

# Core Definition

> "Error strings should not be capitalized (unless beginning with an exported name, a proper noun or an acronym) and should not end with punctuation. This is because error strings usually appear within other context before being printed to the user." -- Google Go Style Guide, "Error strings"

# Prerequisites

- Understanding of Go's `fmt.Errorf` and error creation patterns
- Knowledge of error wrapping conventions

# Key Properties

1. **No capitalization**: Error strings start lowercase unless beginning with an exported name, proper noun, or acronym.
2. **No trailing punctuation**: Error strings do not end with a period or other punctuation.
3. **Designed for wrapping**: Errors are composed into larger messages, so consistent casing prevents awkward mid-sentence capitals.
4. **Display messages differ**: Full displayed messages (logs, test failures, API responses) should typically be capitalized.

# Construction / Recognition

**Bad -- capitalized with punctuation:**

```go
err := fmt.Errorf("Something bad happened.")
```

**Good -- lowercase, no punctuation:**

```go
err := fmt.Errorf("something bad happened")
```

**Good -- display messages are capitalized:**

```go
log.Infof("Operation aborted: %v", err)
log.Errorf("Operation aborted: %v", err)
t.Errorf("Op(%q) failed unexpectedly; err=%v", args, err)
```

# Context & Application

When errors are wrapped with `fmt.Errorf("operation failed: %w", err)`, a capitalized inner error produces awkward output like `"operation failed: Something bad happened."`. Keeping error strings lowercase and unpunctuated ensures clean composition at every wrapping level.

# Examples

See Construction / Recognition above for the complete set of source examples.

# Relationships

- **returning-errors**: The convention for how errors are returned from functions.
- **handle-errors-decisions**: How to handle errors once received.

# Common Errors

1. Capitalizing error strings out of habit from other languages.
2. Adding trailing periods to error messages.
3. Treating error strings the same as user-facing log messages.

# Common Confusions

- **Error strings vs. log messages**: Error strings are lowercase and unpunctuated; log/display messages that present errors to users should be capitalized.
- **Exported names are okay**: An error string like `"XML parsing failed"` is fine because `XML` is an acronym.

# Source Reference

Google Go Style Guide, "Style Decisions" chapter, "Error strings" section.

# Verification Notes

Confidence: high. All rules and examples are directly from the source text.
