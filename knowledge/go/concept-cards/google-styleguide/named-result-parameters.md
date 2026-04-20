---
# === CORE IDENTIFICATION ===
concept: Named Result Parameters
slug: named-result-parameters

# === CLASSIFICATION ===
category: commentary
subcategory: function-signatures
tier: intermediate

# === PROVENANCE ===
source: "Google Go Style Guide"
source_slug: google-styleguide
authors: "Google Go Style Team"
chapter: "Style Decisions"
chapter_number: 3
pdf_page: null
section: "Named result parameters"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "named return values"
  - "named returns"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - doc-comments
extends: []
related:
  - repetition-in-naming
  - variable-names
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "When should Go functions use named result parameters?"
  - "Should I name return values to enable naked returns?"
  - "How do named result parameters affect Godoc?"
---

# Quick Definition

Use named result parameters when same-type returns need disambiguation or when names improve Godoc clarity (e.g., signaling required caller actions). Do not use named results just to avoid declaring variables or to enable naked returns.

# Core Definition

Named result parameters should be used when a function returns two or more parameters of the same type and naming them helps disambiguate, or when the name conveys important information about what the caller must do with the result (e.g., a `cancel` function). Named results should not be used when names produce unnecessary repetition (e.g., `(node *Node)` on a function that clearly returns a Node), nor should they be used solely to avoid declaring a variable inside the function. Naked returns are acceptable only in small functions; in medium-sized or larger functions, be explicit with returned values. It is always acceptable to name a result parameter if its value must be changed in a deferred closure (Google Go Style Guide, "Style Decisions", "Named result parameters").

# Prerequisites

- **doc-comments** -- Named result parameters appear in Godoc documentation
- **Go function signatures** -- Understanding how return types and names work in Go

# Key Properties

1. Use when same-type returns need disambiguation: `(left, right *Node, err error)`
2. Use when names suggest required caller action: `(ctx Context, cancel func())`
3. Do not use when names repeat the type: `(node *Node)` on an obvious Node-returning function
4. Do not use solely to avoid variable declarations
5. Naked returns only in small functions
6. Always acceptable when deferred closures modify the result
7. Types can often be clearer than names (use named types like `CancelFunc`)

# Construction / Recognition

## To Apply:
1. If returns are different types and self-explanatory, omit names
2. If returns are same type, add names to disambiguate
3. If a return value requires specific caller action, name it to suggest the action
4. If naming would repeat the type, omit the name
5. Prefer named types (e.g., `CancelFunc`) over raw types with names

## To Recognize:
1. Look for same-type return values without names -- they may need naming
2. Look for named returns that just repeat the type -- they should be unnamed
3. Look for naked returns in large functions -- they should be explicit

# Context & Application

Named result parameters serve two purposes: improving Godoc documentation and enabling naked returns. Google style prioritizes the documentation purpose over the syntactic convenience. The `context.WithTimeout` function is a canonical example where naming the `cancel` return value communicates critical information about resource cleanup that the caller must perform.

# Examples

**Example 1 -- Good: names unnecessary when types are clear** (Decisions, "Named result parameters"):

```go
// Good:
func (n *Node) Parent1() *Node
func (n *Node) Parent2() (*Node, error)
```

**Example 2 -- Good: names needed for same-type disambiguation** (Decisions, "Named result parameters"):

```go
// Good:
func (n *Node) Children() (left, right *Node, err error)
```

**Example 3 -- Good: names suggest required caller action** (Decisions, "Named result parameters"):

```go
// Good:
// WithTimeout returns a context that will be canceled no later than d duration
// from now.
//
// The caller must arrange for the returned cancel function to be called when
// the context is no longer needed to prevent a resource leak.
func WithTimeout(parent Context, d time.Duration) (ctx Context, cancel func())
```

**Example 4 -- Bad: names that repeat the type** (Decisions, "Named result parameters"):

```go
// Bad:
func (n *Node) Parent1() (node *Node)
func (n *Node) Parent2() (node *Node, err error)
```

# Relationships

## Related
- **repetition-in-naming** -- Named results that repeat the type violate the repetition principle
- **variable-names** -- Named results follow the same naming conventions as variables
- **doc-comments** -- Named results improve Godoc output

# Common Errors

- **Error**: Naming result parameters solely to enable naked returns
  **Correction**: Only use naked returns in small functions; prefer explicit returns in medium/large functions

- **Error**: Naming results to avoid declaring local variables
  **Correction**: Declare variables explicitly; named results are for documentation, not convenience

# Common Confusions

- **Confusion**: Thinking all result parameters should be named for consistency
  **Clarification**: Only name results when it adds information -- same-type disambiguation or caller action guidance

- **Confusion**: Believing named results always require naked returns
  **Clarification**: You can name results for documentation purposes and still use explicit return statements

# Source Reference

Chapter 3: Style Decisions, Section "Named result parameters".

# Verification Notes

- Definition source: Directly from the "Named result parameters" section of Google Go Style Decisions
- Confidence rationale: HIGH -- detailed guidance with multiple good/bad examples
- Uncertainties: None
- Cross-reference status: Related slugs verified against planned extractions
