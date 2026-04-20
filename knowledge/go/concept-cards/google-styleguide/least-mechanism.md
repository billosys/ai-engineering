---
# === CORE IDENTIFICATION ===
concept: Least Mechanism
slug: least-mechanism

# === CLASSIFICATION ===
category: principles
subcategory: style-principles
tier: foundational

# === PROVENANCE ===
source: "Google Go Style Guide"
source_slug: google-styleguide
authors: "Google Go Style Team"
chapter: "Guide"
chapter_number: 2
pdf_page: null
section: "Style principles"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "principle of least mechanism"
  - "prefer standard tools"
  - "minimize dependencies"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - simplicity-principle
extends:
  - simplicity-principle
related:
  - maintainability-principle
  - clarity-principle
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "Should I use a third-party library or the standard library?"
  - "When should I add a new dependency in Go?"
  - "What is the preferred order of tools to reach for in Go?"
---

# Quick Definition

When multiple approaches can express the same idea, prefer the most standard one: first core language constructs, then the standard library, then well-known internal libraries, and only then external dependencies.

# Core Definition

Least mechanism is a sub-principle of simplicity. Where several ways exist to express the same idea, prefer the one that uses the most standard tools. Sophisticated machinery should not be employed without reason. The hierarchy is: (1) core language constructs (channels, slices, maps, loops, structs), (2) standard library tools (HTTP client, template engine), (3) core/well-known libraries in the codebase. Adding complexity is easy; removing it after it is found unnecessary is much harder.

# Prerequisites

- **simplicity-principle** -- Least mechanism is a sub-principle of simplicity

# Key Properties

1. Prefer core language constructs (channel, slice, map, loop, struct) when sufficient
2. Next, look for a tool in the standard library
3. Only then consider established codebase libraries or new external dependencies
4. It is easy to add complexity; much harder to remove it
5. Sophisticated machinery should not be employed without reason

# Construction / Recognition

## To Apply:
1. Check if a core language construct (map, slice, channel, struct) solves the problem
2. If not, search the standard library for a suitable tool
3. Only consider external or internal libraries if the above are insufficient
4. Justify any added dependency

## To Recognize:
1. Using a third-party set library when `map[string]bool` would suffice
2. Using `flag.Set` in tests when directly overriding the bound value is simpler
3. Importing a library for functionality already available in the standard library

# Context & Application

This principle directly reduces dependency count and cognitive load. A boolean-valued map (`map[string]bool`) often suffices for set membership checks; set libraries should only be used when more complex operations (intersection, difference) are truly needed. Similarly, in tests, it is simpler to override a flag's bound value directly rather than invoking `flag.Set`, unless testing the CLI interface itself.

# Examples

**Example 1 -- Set membership with a map (from source)**:

```go
// Good: use a map for simple set membership
allowed := map[string]bool{
    "read":  true,
    "write": true,
}
if allowed[action] {
    // ...
}
```

A set library should only be used when operations like intersection or difference are required.

**Example 2 -- Testing flag values (from source)**:

When testing code that uses a flag with a default value, override the bound variable directly rather than calling `flag.Set`, unless the test is specifically exercising the CLI interface.

# Relationships

## Related
- **maintainability-principle** -- Fewer dependencies mean less maintenance burden
- **clarity-principle** -- Standard constructs are more familiar and thus clearer

## Extends
- **simplicity-principle** -- Least mechanism is a specific application of the simplicity principle

# Common Errors

- **Error**: Importing a third-party library for functionality available in the standard library
  **Correction**: Check the standard library first; only add dependencies when truly needed

- **Error**: Using complex abstractions (e.g., generics, reflection) when a simple loop or map suffices
  **Correction**: Reach for the simplest language construct that solves the problem

# Common Confusions

- **Confusion**: Thinking this principle forbids all external dependencies
  **Clarification**: External dependencies are fine when justified. The principle is about preference order, not prohibition.

- **Confusion**: Believing simpler always means fewer lines of code
  **Clarification**: A few more lines using a standard construct is preferred over a one-liner requiring an external library

# Source Reference

Chapter 2: Guide, Section "Style principles" > "Simplicity" > "Least mechanism".

# Verification Notes

- Definition source: Directly from the "Least mechanism" subsection under "Simplicity"
- Confidence rationale: HIGH -- the source provides an explicit three-tier hierarchy with examples
- Uncertainties: None
- Cross-reference status: Related slugs verified against planned extractions
