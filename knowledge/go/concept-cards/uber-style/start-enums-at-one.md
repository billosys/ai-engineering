---
# === CORE IDENTIFICATION ===
concept: Start Enums at One
slug: start-enums-at-one

# === CLASSIFICATION ===
category: data-structures
subcategory: enumerations
tier: foundational

# === PROVENANCE ===
source: "Uber Go Style Guide"
source_slug: uber-style
authors: "Prashant Varanasi, Simon Newton"
chapter: "Guidelines"
chapter_number: 2
pdf_page: null
section: "Start Enums at One"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "iota starts at one"
  - "enum zero value"
  - "iota + 1"

# === TYPED RELATIONSHIPS ===
prerequisites: []
extends: []
related: []
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "Why should Go enums start at 1 instead of 0?"
  - "When is it appropriate to start enums at 0?"
  - "How do I declare enums with iota starting at a non-zero value?"
---

# Quick Definition

Start `iota` enums at 1 (using `iota + 1`) so that the zero value of the enum type is distinguishable from any valid enum value. Use zero-based enums only when the zero value is the desired default.

# Core Definition

The Uber Go Style Guide explains that the standard way of introducing enumerations in Go is to declare a custom type and a `const` group with `iota`. Since variables have a 0 default value, you should usually start your enums on a non-zero value. This ensures that an uninitialized variable of the enum type does not accidentally correspond to a valid enum value. However, there are cases where using the zero value makes sense -- for example, when the zero value case is the desirable default behavior (Uber Go Style Guide, "Start Enums at One").

# Prerequisites

This is a foundational concept. Understanding Go's `iota` constant generator and zero-value initialization is helpful but not strictly required.

# Key Properties

1. Go variables default to their zero value (0 for integer types)
2. If an enum starts at 0, an uninitialized variable silently becomes a valid enum value
3. Starting at `iota + 1` makes the zero value invalid/distinguishable from all defined values
4. Exception: start at 0 when the zero value is a meaningful, desirable default
5. The pattern uses `const` blocks with a custom type and `iota`

# Construction / Recognition

## To Apply:
1. Declare a custom type (usually `int`): `type Operation int`
2. Define constants using `iota + 1` for the first value: `Add Operation = iota + 1`
3. Subsequent constants auto-increment from there
4. If the zero value should be a valid default, use plain `iota` instead

## To Recognize:
1. Look for `const` blocks where the first value uses plain `iota` without an offset -- consider whether the zero value default is intentional
2. If the zero value has no meaning for the enum, it should use `iota + 1`

# Context & Application

This pattern prevents a class of bugs where uninitialized enum variables silently match a valid value. For example, if `Add` is 0, then any `Operation` variable that was never explicitly set will appear to be `Add`, which is almost certainly not the intended behavior. Starting at 1 means uninitialized values remain at 0, which does not match any defined enum value and can be detected as an error.

The exception is when the zero value IS meaningful. The source gives the example of `LogOutput`, where `LogToStdout` as the default (zero value) is sensible behavior.

# Examples

**Example 1** (Guidelines, "Start Enums at One"):

Bad -- enum starts at 0:
```go
type Operation int

const (
  Add Operation = iota
  Subtract
  Multiply
)

// Add=0, Subtract=1, Multiply=2
```

Good -- enum starts at 1:
```go
type Operation int

const (
  Add Operation = iota + 1
  Subtract
  Multiply
)

// Add=1, Subtract=2, Multiply=3
```

**Example 2** (Guidelines, "Start Enums at One"): Exception -- zero value is a valid default:

```go
type LogOutput int

const (
  LogToStdout LogOutput = iota
  LogToFile
  LogToRemote
)

// LogToStdout=0, LogToFile=1, LogToRemote=2
```

Here, `LogToStdout` as the zero value is the desired default behavior.

# Relationships

## Builds Upon
- **Go iota** -- The `iota` constant generator is the mechanism for declaring enums in Go

## Enables
- Safer code that detects uninitialized enum values
- Clearer distinction between "not set" and "set to the first value"

## Related
- None specific within this extraction scope

## Contrasts With
- Starting enums at 0 (appropriate only when zero value is a meaningful default)

# Common Errors

- **Error**: Starting an enum at 0 when the zero value has no meaningful semantic
  **Correction**: Use `iota + 1` so that uninitialized variables do not silently match a valid value

- **Error**: Always starting at 1 even when the zero value is the natural default
  **Correction**: If the zero value is the desired default (e.g., `LogToStdout`), use plain `iota`

# Common Confusions

- **Confusion**: Believing all enums in Go must start at 1
  **Clarification**: Start at 1 by default, but use 0 when the zero value represents a valid, desirable default

- **Confusion**: Thinking `iota + 1` changes how `iota` increments
  **Clarification**: `iota` still starts at 0 and increments by 1 for each constant; the `+ 1` is applied to each value, so the results are 1, 2, 3, etc.

# Source Reference

Chapter 2: Guidelines, Section "Start Enums at One".

# Verification Notes

- Definition source: Directly from the "Start Enums at One" section with Bad/Good examples and a documented exception
- Confidence rationale: HIGH -- explicit guideline with clear examples and exception case
- Uncertainties: None
- Cross-reference status: No cross-references needed
