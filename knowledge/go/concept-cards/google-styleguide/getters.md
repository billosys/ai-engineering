---
# === CORE IDENTIFICATION ===
concept: Getters
slug: getters

# === CLASSIFICATION ===
category: naming
subcategory: methods
tier: foundational

# === PROVENANCE ===
source: "Google Go Style Guide"
source_slug: google-styleguide
authors: "Google Go Style Team"
chapter: "Style Decisions"
chapter_number: 3
pdf_page: null
section: "Getters"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "getter naming"
  - "accessor methods"

# === TYPED RELATIONSHIPS ===
prerequisites: []
extends: []
related:
  - variable-names
  - repetition-in-naming
  - receiver-names
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "Should Go getter methods use a Get prefix?"
  - "When should I use Compute or Fetch instead of Get in Go?"
  - "How do I name accessor methods in Go?"
---

# Quick Definition

Do not use `Get` or `get` prefix on getter methods. Use the noun directly (e.g., `Counts` not `GetCounts`). Use `Compute` or `Fetch` for expensive operations to signal cost to the caller.

# Core Definition

In Go, function and method names should not use a `Get` or `get` prefix unless the underlying concept itself uses the word "get" (e.g., an HTTP GET request). The preferred convention is to start the name with the noun directly -- for example, `Counts` rather than `GetCounts`. When the function involves a complex computation or a remote call, a word like `Compute` or `Fetch` can replace `Get` to signal to the reader that the function may take time and could block or fail (Google Go Style Guide, "Style Decisions", "Getters").

# Prerequisites

- **Go method naming basics** -- Understanding how methods are named and called in Go
- **Exported vs unexported identifiers** -- Getter methods on exported fields follow the same export rules

# Key Properties

1. No `Get` or `get` prefix on accessor methods
2. Use the noun directly: `Counts()` not `GetCounts()`
3. Exception: when "get" is part of the domain concept (e.g., HTTP GET)
4. Use `Compute` for CPU-intensive operations
5. Use `Fetch` for operations involving network or I/O calls

# Construction / Recognition

## To Apply:
1. Name accessor methods with the noun directly (e.g., `Name()` for a name field)
2. If the operation is expensive (computation), prefix with `Compute`
3. If the operation involves remote calls, prefix with `Fetch`
4. Only use `Get` when "get" is part of the domain vocabulary

## To Recognize:
1. Look for methods prefixed with `Get` that simply return a field -- these should drop the prefix
2. Look for expensive operations named with simple nouns -- these may need `Compute` or `Fetch`

# Context & Application

This convention aligns with Go's preference for brevity and the principle that package-qualified names already provide context. Since you call `obj.Name()` rather than just `Name()`, the receiver makes it clear this is an accessor. The `Compute`/`Fetch` distinction is valuable because it communicates performance characteristics at the call site, helping developers make informed decisions about caching and error handling.

# Examples

**Example 1 -- Good: noun-based getter names** (Decisions, "Getters"):

```go
// Good:
func (t *Timer) Counts() int
func (c *Config) Name() string
```

**Example 2 -- Bad: unnecessary Get prefix** (Decisions, "Getters"):

```go
// Bad:
func (t *Timer) GetCounts() int
func (c *Config) GetName() string
```

**Example 3 -- Good: signaling expensive operations** (Decisions, "Getters"):

```go
// Good: Compute signals CPU-intensive work
func (r *Report) ComputeStatistics() Stats

// Good: Fetch signals a remote call that may block or fail
func (c *Client) FetchUserProfile(id string) (*Profile, error)
```

# Relationships

## Related
- **variable-names** -- Getter return values follow variable naming conventions
- **repetition-in-naming** -- Dropping `Get` reduces redundancy with the receiver type
- **receiver-names** -- Short receiver names used alongside getter methods

# Common Errors

- **Error**: Naming every accessor with `Get` prefix out of habit from Java/C#
  **Correction**: Drop the `Get` prefix and use the noun directly

- **Error**: Using a plain noun for a method that makes a network call
  **Correction**: Use `Fetch` to communicate that the operation may be slow or fail

# Common Confusions

- **Confusion**: Thinking proto-generated `GetField()` methods mean user code should follow the same pattern
  **Clarification**: Proto-generated `Get` methods are a code generation convention; hand-written Go code should not use the `Get` prefix

- **Confusion**: Believing `Set` prefix should also be dropped
  **Clarification**: The guidance specifically targets `Get`; `Set` prefixes are acceptable in Go when a setter is needed

# Source Reference

Chapter 3: Style Decisions, Section "Getters".

# Verification Notes

- Definition source: Directly from the "Getters" section of Google Go Style Decisions
- Confidence rationale: HIGH -- explicit guidance with clear alternatives
- Uncertainties: None
- Cross-reference status: Related slugs verified against planned extractions
