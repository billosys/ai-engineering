---
# === CORE IDENTIFICATION ===
concept: Context Usage Conventions
slug: contexts

# === CLASSIFICATION ===
category: libraries
subcategory: context-propagation
tier: foundational

# === PROVENANCE ===
source: "Google Go Style Guide"
source_slug: google-styleguide
authors: "Google Go Style Team"
chapter: "Style Decisions"
chapter_number: 3
pdf_page: null
section: "Contexts"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "context.Context usage"
  - "context propagation"
  - "context parameter conventions"

# === TYPED RELATIONSHIPS ===
prerequisites: []
extends: []
related:
  - flags
  - logging
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "Where should context.Context appear in a function signature?"
  - "Should I store context in a struct field?"
  - "When should I use context.Background()?"
  - "Can I create custom context types?"
  - "How should context be used in tests?"
---

# Quick Definition

Pass `context.Context` as the first parameter to functions. Do not store it in struct fields. Do not create custom context types. Use `context.Background()` only at entrypoints (main, init). In tests, prefer `(testing.TB).Context()` over `context.Background()`.

# Core Definition

`context.Context` carries security credentials, tracing information, deadlines, and cancellation signals across API and process boundaries. Unlike languages that use thread-local storage, Go passes contexts explicitly along the entire call chain. The context must always be the first parameter in a function signature. It should not be stored as a struct member -- instead, pass it to each method that needs it. Custom context types must never be created, as they undermine interoperability between packages. Use `context.Background()` only at entrypoints like `main` or `init`; mid-callchain code should always receive context from its caller.

# Prerequisites

- **Go context package** -- Basic understanding of `context.Context`, `context.Background()`, and `context.WithCancel`
- **Go function signatures** -- Understanding of parameter ordering conventions

# Key Properties

1. **First parameter**: `context.Context` is always the first parameter in a function signature
2. **No struct storage**: Do not add a context field to struct types; pass context per-call
3. **No custom contexts**: Never create custom context types or use interfaces other than `context.Context`
4. **Entrypoint-only Background**: Use `context.Background()` only in `main`, `init`, or equivalent entrypoints
5. **Immutable sharing**: Since contexts are immutable, the same context can safely be passed to multiple calls
6. **Test contexts**: In Go 1.24+, prefer `(testing.TB).Context()` over `context.Background()` in tests
7. **Exception: HTTP handlers**: Context comes from `req.Context()`, not as a parameter
8. **Exception: streaming RPCs**: Context comes from the stream's `Context()` method

# Construction / Recognition

## To Apply:
1. Place `context.Context` as the first parameter: `func F(ctx context.Context, ...)`
2. Pass context through the call chain; never store it in a struct
3. At entrypoints, create context with `context.Background()`
4. In tests, use `t.Context()` (Go 1.24+)
5. Never define a custom context type

## To Recognize:
1. Functions with `ctx context.Context` not as the first parameter
2. Structs with a `context.Context` field
3. Custom types implementing context interfaces
4. `context.Background()` called in the middle of a call chain (not at an entrypoint)

# Context & Application

Go's explicit context passing (versus thread-local storage) means that context propagation is visible in every function signature. This makes cancellation, deadline, and credential flow auditable. The prohibition on custom context types prevents the combinatorial explosion of needing to convert between `p.Context` and `q.Context` for every pair of packages. The struct storage prohibition ensures context lifetimes are scoped to individual operations rather than object lifetimes.

# Examples

**Example 1 -- Standard context parameter**:

```go
func F(ctx context.Context /* other arguments */) {}
```

**Example 2 -- Context in test helpers**:

```go
// Good:
func readTestFile(ctx context.Context, t *testing.T, path string) string {}
```

**Example 3 -- Why custom contexts are forbidden**:

Every pair of packages would need conversion logic between custom context types, making automated refactorings nearly impossible and creating error-prone manual conversions.

# Relationships

## Related
- **flags** -- Both address how configuration and state flow through Go programs
- **logging** -- Contexts often carry trace information relevant to log correlation

# Common Errors

- **Error**: Storing `context.Context` in a struct field
  **Correction**: Pass context as a parameter to each method that needs it.

- **Error**: Creating a custom context type for application-specific data
  **Correction**: Use `context.WithValue` to attach data to a standard `context.Context`.

- **Error**: Using `context.Background()` in library code
  **Correction**: Accept context from the caller. Only entrypoints should create base contexts.

# Common Confusions

- **Confusion**: Thinking HTTP handler functions should take `ctx context.Context` as the first parameter
  **Clarification**: HTTP handlers get context from `req.Context()`; this is a recognized exception.

- **Confusion**: Assuming `context.Background()` is fine anywhere a context is needed
  **Clarification**: Mid-callchain code should always receive context from its caller. Using `context.Background()` there breaks cancellation and deadline propagation.

# Source Reference

Chapter 3: Style Decisions, Sections "Contexts" and "Custom contexts" under "Common libraries".

# Verification Notes

- Definition source: Directly from the "Contexts" and "Custom contexts" sections
- Confidence rationale: HIGH -- the guidance is detailed and explicit with multiple rules and exceptions
- Uncertainties: None
- Cross-reference status: References the Go blog post "Contexts and structs" and issue #40221
