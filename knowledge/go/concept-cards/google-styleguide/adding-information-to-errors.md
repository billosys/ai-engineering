---
# === CORE IDENTIFICATION ===
concept: Adding Information to Errors
slug: adding-information-to-errors

# === CLASSIFICATION ===
category: error-handling
subcategory: error-wrapping
tier: intermediate

# === PROVENANCE ===
source: "Google Go Style Guide"
source_slug: google-styleguide
authors: "Google Go Style Team"
chapter: "Best Practices"
chapter_number: 4
pdf_page: null
section: "Adding information to errors"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "error annotation"
  - "error wrapping"
  - "error context"
  - "%v vs %w in errors"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - error-structure
extends: []
related:
  - placement-of-w-in-errors
  - logging-errors
  - documentation-conventions
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "When should I use %v vs %w when wrapping errors?"
  - "How do I add context to an error without being redundant?"
  - "When should I wrap errors vs create fresh ones?"
---

# Quick Definition

When annotating errors, add context the caller does not already have and avoid duplicating information the underlying error provides. Use `%v` to create fresh errors (especially at system boundaries) and `%w` to preserve the error chain for programmatic inspection within your application.

# Core Definition

When adding information to a returned error, avoid redundancy with the underlying error. For example, `os.Open` already includes the file path, so wrapping it with the path again is redundant. Instead, add the context specific to the current function (e.g., "launch codes unavailable"). Do not add annotations whose sole purpose is to indicate a failure occurred -- just return `err` directly. The choice between `%v` and `%w` in `fmt.Errorf` is significant: `%v` embeds only the string representation (dropping structured information), suitable for logging, display, and system boundaries where internal errors should be translated to canonical error spaces. `%w` preserves the error chain via `Unwrap()`, enabling `errors.Is` and `errors.As` inspection, suitable for internal helpers where callers need to check underlying error types. At system boundaries (RPC, IPC, storage), prefer `%v` or status codes to avoid leaking internal error details.

# Prerequisites

- **error-structure** -- Understanding sentinel values and custom error types

# Key Properties

1. Add context the underlying error does not already provide
2. Do not duplicate information (e.g., file paths already in `os` errors)
3. Do not add "failed:" annotations that add no new information -- just return `err`
4. `%v`: creates a fresh error string; drops structured information from original
5. `%w`: wraps the error preserving the chain for `errors.Is`/`errors.As` inspection
6. Use `%v` at system boundaries (RPC, IPC, storage) to translate to canonical error spaces
7. Use `%w` within internal helpers where callers need programmatic error inspection

# Construction / Recognition

## To Apply:
1. Check what information the underlying error already contains
2. Add only the context specific to the current function's domain
3. Choose `%v` for system boundaries and display; `%w` for internal error chaining
4. If wrapping adds no new information, just return the error directly

## To Recognize:
1. Error messages that add domain-specific context without repeating underlying details
2. Appropriate use of `%w` for internal functions, `%v` at boundaries

# Context & Application

This is one of the most nuanced areas of Go error handling. The decision between `%v` and `%w` determines whether callers can programmatically inspect the error chain. At system boundaries, wrapping with `%w` can leak internal implementation details to external callers who may come to depend on them. Within a package or application, `%w` enables callers to handle specific error conditions. The documentation conventions section recommends documenting which errors are returned and whether they are wrapped.

# Examples

**Example 1 -- Good: adding domain context**:

```go
// Good:
if err := os.Open("settings.txt"); err != nil {
    return fmt.Errorf("launch codes unavailable: %v", err)
}
// Output: launch codes unavailable: open settings.txt: no such file or directory
```

**Example 2 -- Bad: redundant path information**:

```go
// Bad:
if err := os.Open("settings.txt"); err != nil {
    return fmt.Errorf("could not open settings.txt: %v", err)
}
// Output: could not open settings.txt: open settings.txt: no such file or directory
```

**Example 3 -- Bad: useless annotation**:

```go
// Bad:
return fmt.Errorf("failed: %v", err) // just return err instead
```

**Example 4 -- %w for internal chaining**:

```go
// Good:
func (s *Server) internalFunction(ctx context.Context) error {
    if err != nil {
        return fmt.Errorf("couldn't find remote file: %w", err)
    }
}
// Allows: errors.Is(err, fs.ErrNotExist)
```

**Example 5 -- %v at system boundary**:

```go
// Good:
func (*FortuneTeller) SuggestFortune(ctx context.Context, req *pb.SuggestionRequest) (*pb.SuggestionResponse, error) {
    if err != nil {
        return nil, fmt.Errorf("couldn't find fortune database: %v", err)
    }
}
```

# Relationships

## Related
- **placement-of-w-in-errors** -- Where to position %w within the format string
- **logging-errors** -- Complementary guidance on when to log vs return errors
- **documentation-conventions** -- Documenting which errors are returned and wrapped

## Contrasts With
(none)

# Common Errors

- **Error**: Wrapping with `%w` at an RPC boundary, leaking internal error details
  **Correction**: Use `%v` or status codes at system boundaries

- **Error**: Adding "failed to X:" prefix that only restates the obvious
  **Correction**: Either add meaningful context or return the error directly

# Common Confusions

- **Confusion**: Thinking `%w` is always better than `%v`
  **Clarification**: `%w` creates an API contract -- callers may depend on the wrapped error type. Use `%v` when that contract is inappropriate.

- **Confusion**: Using `errors.Unwrap` to inspect error chains
  **Clarification**: Prefer `errors.Is` and `errors.As` which handle multi-errors correctly

# Source Reference

Chapter 4: Best Practices, Section "Error handling" > "Adding information to errors".

# Verification Notes

- Definition source: Directly from the "Adding information to errors" section
- Confidence rationale: HIGH -- detailed guidance with examples for both %v and %w
- Uncertainties: None
- Cross-reference status: References Go blog on error wrapping, documentation conventions
