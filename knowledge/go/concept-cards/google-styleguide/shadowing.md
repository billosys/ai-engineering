---
# === CORE IDENTIFICATION ===
concept: Variable Shadowing
slug: shadowing

# === CLASSIFICATION ===
category: language
subcategory: variable-declarations
tier: intermediate

# === PROVENANCE ===
source: "Google Go Style Guide"
source_slug: google-styleguide
authors: "Google Go Style Team"
chapter: "Best Practices"
chapter_number: 4
pdf_page: null
section: "Shadowing"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "variable shadowing"
  - "stomping vs shadowing"
  - "short variable declaration pitfalls"

# === TYPED RELATIONSHIPS ===
prerequisites: []
extends: []
related:
  - variable-declarations-bp
  - import-renaming
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is the difference between stomping and shadowing in Go?"
  - "How can short variable declarations introduce subtle bugs?"
  - "Why should I avoid naming variables after standard packages?"
---

# Quick Definition

Shadowing occurs when a short variable declaration (`:=`) in a new scope creates a new variable that hides an outer variable of the same name. Stomping reuses an existing variable. Shadowing can introduce subtle bugs; avoid shadowing builtins and package names.

# Core Definition

Go distinguishes between two informal concepts: stomping and shadowing. Stomping occurs when `:=` reuses an existing variable in the same scope (acceptable when the original is no longer needed). Shadowing occurs when `:=` in a new scope (e.g., inside an `if` block) creates an entirely new variable that hides the outer one -- code after the block refers to the original, not the shadowed version. This is a common source of bugs, particularly with `context.Context` and `cancel` functions. Intentional shadowing can be useful, but using a new name is always an option if it improves clarity. Variables should not share names with standard packages, as this makes the package's functions inaccessible.

# Prerequisites

(none)

# Key Properties

1. Stomping: `:=` reuses an existing variable in the same scope -- the value changes but the variable is the same
2. Shadowing: `:=` in a new scope creates a new variable that hides the outer one
3. After the inner scope ends, the outer variable retains its original value (a common source of bugs)
4. With shadowing, the new variable can have a different type
5. Do not name variables after standard packages (e.g., don't use `url` as a variable name in code that needs `net/url`)

# Construction / Recognition

## To Apply:
1. When you need to modify an outer variable inside a block, use `=` (assignment) not `:=` (declaration)
2. Pre-declare variables that need assignment inside conditional blocks
3. Avoid naming variables the same as standard library packages
4. Use `go vet` to detect shadowing issues

## To Recognize:
1. A `:=` inside an `if`/`for` block using the same name as an outer variable
2. Bug: outer variable unchanged after the inner block completes
3. A variable name that matches a standard library package name

# Context & Application

The most common shadowing bug involves `context.Context` where a deadline-capped context inside an `if` block does not affect the outer context. The fix is to use simple assignment (`=`) with a pre-declared `cancel` variable. Intentional shadowing is acceptable when it improves code clarity, but always consider whether a new variable name would be clearer. Avoid package-name collisions especially in longer functions where the package may be needed later.

# Examples

**Example 1 -- Buggy shadowing of context**:

```go
// Bad:
func (s *Server) innerHandler(ctx context.Context, req *pb.MyRequest) *pb.MyResponse {
    if *shortenDeadlines {
        ctx, cancel := context.WithTimeout(ctx, 3*time.Second)
        defer cancel()
        ctxlog.Info(ctx, "Capped deadline in inner request")
    }
    // BUG: "ctx" here is the original context, not the capped one.
}
```

**Example 2 -- Correct fix using assignment**:

```go
// Good:
func (s *Server) innerHandler(ctx context.Context, req *pb.MyRequest) *pb.MyResponse {
    if *shortenDeadlines {
        var cancel func()
        ctx, cancel = context.WithTimeout(ctx, 3*time.Second)  // = not :=
        defer cancel()
        ctxlog.Info(ctx, "Capped deadline in inner request")
    }
    // ctx is correctly the capped context here.
}
```

**Example 3 -- Avoid shadowing package names**:

```go
// Bad:
func LongFunction() {
    url := "https://example.com/"
    // Oops, now we can't use net/url in code below.
}
```

# Relationships

## Related
- **variable-declarations-bp** -- General guidance on variable declaration forms
- **import-renaming** -- Package names that conflict with common variable names may need import renaming

## Contrasts With
(none)

# Common Errors

- **Error**: Using `:=` inside an `if` block thinking it modifies the outer variable
  **Correction**: Use `=` with a pre-declared variable when you need the change to persist

- **Error**: Naming a local variable `url`, `path`, or `context` and then needing the package
  **Correction**: Choose a different variable name or limit usage to very small scopes

# Common Confusions

- **Confusion**: Thinking stomping and shadowing are the same
  **Clarification**: Stomping reuses the same variable (same scope); shadowing creates a new one (new scope)

- **Confusion**: Believing all shadowing is bad
  **Clarification**: Intentional shadowing can be useful; the key is that it should be deliberate and clear

# Source Reference

Chapter 4: Best Practices, Section "Naming" > "Shadowing".

# Verification Notes

- Definition source: Directly from the "Shadowing" section of Best Practices
- Confidence rationale: HIGH -- explicit guidance with detailed good/bad examples
- Uncertainties: None
- Cross-reference status: References guide#clarity, decisions#import-renaming
