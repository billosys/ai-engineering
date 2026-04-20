---
concept: In-Band Errors
slug: in-band-errors
category: error-handling
subcategory: error-signaling
tier: intermediate
source: "Google Go Style Guide"
source_slug: google-styleguide
authors: "Google Go Style Team"
chapter: "Style Decisions"
chapter_number: 3
pdf_page: null
section: "In-band errors"
extraction_confidence: high
aliases:
  - sentinel values
  - mixed result and error
prerequisites:
  - returning-errors
related:
  - handle-errors-decisions
  - nil-slices-decisions
contrasts_with: []
answers_questions:
  - "What are in-band errors in Go?"
  - "Why should Go functions use separate error returns instead of sentinel values?"
  - "How does Go's multiple return prevent in-band error misuse?"
---

# Quick Definition

Avoid mixing result and error signaling in the same return value (e.g., returning -1 or empty string for failure). Use Go's multiple return values to provide a separate `error` or `bool` return, which the compiler enforces callers to handle.

# Core Definition

> "In C and similar languages, it is common for functions to return values like -1, null, or the empty string to signal errors or missing results. This is known as in-band error handling." -- Google Go Style Guide, "In-band errors"

> "Go's support for multiple return values provides a better solution. Instead of requiring clients to check for an in-band error value, a function should return an additional value to indicate whether its other return values are valid." -- Google Go Style Guide, "In-band errors"

# Prerequisites

- Understanding of Go's multiple return values
- Familiarity with the comma-ok idiom

# Key Properties

1. **No sentinel values**: Do not use special values like -1, "", or nil to signal errors in the primary return value.
2. **Separate error return**: Use a second return value (`error` or `bool`) to indicate success or failure.
3. **Compiler-enforced**: Multiple returns prevent callers from accidentally chaining calls like `Parse(Lookup(key))` without checking errors.
4. **Standard library exceptions**: Some `strings` package functions use in-band errors for simplicity, but this is not the general recommendation.

# Construction / Recognition

**Bad -- in-band error using sentinel value:**

```go
// Lookup returns the value for key or -1 if there is no mapping for key.
func Lookup(key string) int
```

**Bad -- errors attributed to wrong function:**

```go
// The following line returns an error that Parse failed for the input value,
// whereas the failure was that there is no mapping for missingKey.
return Parse(Lookup(missingKey))
```

**Good -- separate boolean return:**

```go
// Lookup returns the value for key or ok=false if there is no mapping for key.
func Lookup(key string) (value string, ok bool)
```

**Good -- explicit error checking:**

```go
value, ok := Lookup(key)
if !ok {
    return fmt.Errorf("no value for %q", key)
}
return Parse(value)
```

# Context & Application

In-band errors are fragile because callers must remember which magic values signal failure. With Go's multiple returns, the compiler prevents composing calls without handling the error. This shifts error detection from runtime to compile time, eliminating an entire class of bugs where sentinel values propagate silently through call chains.

# Examples

See Construction / Recognition above for the complete set of source examples.

# Relationships

- **returning-errors**: The foundational convention for returning errors.
- **handle-errors-decisions**: How to handle errors once they are separate return values.
- **nil-slices-decisions**: Related guidance on not using nil vs. empty as a signaling mechanism.

# Common Errors

1. Returning -1, 0, or "" to signal failure instead of a separate error/bool.
2. Composing function calls without checking intermediate errors.
3. Requiring callers to know undocumented sentinel values.

# Common Confusions

- **When in-band is acceptable**: Some standard library functions (e.g., `strings.Index` returning -1) use in-band errors for simplicity. This is a pragmatic exception, not the recommended pattern.
- **Bool vs. error**: Use `bool` when no explanation is needed; use `error` when the caller needs to know why the operation failed.

# Source Reference

Google Go Style Guide, "Style Decisions" chapter, "In-band errors" section.

# Verification Notes

Confidence: high. All guidance, rationale, and code examples are directly from the source text.
