---
# === CORE IDENTIFICATION ===
concept: When to Panic
slug: when-to-panic

# === CLASSIFICATION ===
category: error-handling
subcategory: program-termination
tier: advanced

# === PROVENANCE ===
source: "Google Go Style Guide"
source_slug: google-styleguide
authors: "Google Go Style Team"
chapter: "Best Practices"
chapter_number: 4
pdf_page: null
section: "When to panic"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "panic usage"
  - "internal panic recovery"
  - "panic-recover pattern"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - program-checks-and-panics
extends:
  - dont-panic
related:
  - must-functions
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "When is it acceptable to use panic in Go?"
  - "How can panic be used as an internal implementation detail?"
  - "When should I use panic('unreachable')?"
---

# Quick Definition

Panic is appropriate for programming errors (API misuse, like `reflect`), as an internal implementation detail with matching `recover` (never crossing package boundaries), to mark unreachable code after `log.Fatal`, and in `init` functions or "must" functions where fatal logging is unavailable.

# Core Definition

The standard library panics on API misuse (e.g., `reflect` panics when values are misinterpreted), analogous to out-of-bounds slice access. These are programming errors caught by code review and tests. Panic can also be used as an internal implementation detail within a package, provided it always has a matching `recover` in the call chain and panics never escape across package boundaries. This pattern benefits parsers and deeply nested function groups where plumbing error returns adds complexity without value. The `recover` must distinguish between the package's own panics and unexpected ones, re-panicking for the latter. Panic is also used to mark unreachable code after `log.Fatalf` (to satisfy the compiler). In `init` functions or "must" functions where `log` is unavailable (before flags are parsed), panic is acceptable in place of fatal logging.

# Prerequisites

- **program-checks-and-panics** -- Understanding the general preference for log.Fatal over panic

# Key Properties

1. Panic for programming errors (API misuse), not for input validation or expected failures
2. Internal panic+recover pattern: panics must never escape package boundaries
3. The recover must distinguish own panics from foreign ones (re-panic for foreign)
4. `panic("unreachable")` after `log.Fatal` to satisfy the compiler
5. Panic is acceptable in `init` functions and "must" functions where log is unavailable
6. Resources in defer-managed sections must be properly managed (close, free, unlock)

# Construction / Recognition

## To Apply:
1. Use panic only for programming errors caught by code review and tests
2. For internal panic+recover: define a private error type, recover at the public API boundary, re-panic for unrecognized panics
3. Use `panic("unreachable")` after `log.Fatalf` in switch defaults
4. In `init` or "must" functions, use panic when log is unavailable

## To Recognize:
1. Panic used only at API misuse boundaries or internally with matching recover
2. Public API functions with `defer func() { recover() }` that translate panics to errors
3. `panic("unreachable")` after fatal log calls

# Context & Application

The internal panic+recover pattern is uncommon but valuable for parsers and similar deeply nested code where error plumbing adds complexity. The key safety requirement is that panics never cross package boundaries -- the public API always returns errors. Code using this pattern must carefully manage resources in deferred sections. The `encoding/json` standard library parser is an example of this pattern.

# Examples

**Example 1 -- Internal panic+recover pattern**:

```go
// Good:
type syntaxError struct {
    msg string
}

func parseInt(in string) int {
    n, err := strconv.Atoi(in)
    if err != nil {
        panic(&syntaxError{"not a valid integer"})
    }
}

func Parse(in string) (_ *Node, err error) {
    defer func() {
        if p := recover(); p != nil {
            sErr, ok := p.(*syntaxError)
            if !ok {
                panic(p) // Propagate: not our panic.
            }
            err = fmt.Errorf("syntax error: %v", sErr.msg)
        }
    }()
    // ... parse input calling parseInt internally
}
```

**Example 2 -- Unreachable code marker**:

```go
// Good:
func answer(i int) string {
    switch i {
    case 42:
        return "yup"
    case 54:
        return "base 13, huh"
    default:
        log.Fatalf("Sorry, %d is not the answer.", i)
        panic("unreachable")
    }
}
```

# Relationships

## Related
- **must-functions** -- "Must" functions from Decisions that use panic for initialization
- **dont-panic** -- The general rule against panics that this section refines
- **program-checks-and-panics** -- The broader context of program termination

## Contrasts With
(none)

# Common Errors

- **Error**: Using panic for input validation or expected error conditions
  **Correction**: Return errors for expected failures; panic is only for programming errors

- **Error**: Allowing panics to escape across package boundaries
  **Correction**: Always recover at the public API boundary and convert to errors

# Common Confusions

- **Confusion**: Thinking all panics should be recovered to prevent crashes
  **Clarification**: Only recover panics that your code raised; re-panic for unknown panics

- **Confusion**: Believing panic is never appropriate in production code
  **Clarification**: Panic is valid for API misuse, internal parser patterns, unreachable markers, and init functions

# Source Reference

Chapter 4: Best Practices, Section "Error handling" > "When to panic".

# Verification Notes

- Definition source: Directly from "When to panic" section of Best Practices
- Confidence rationale: HIGH -- detailed guidance with code example for panic+recover pattern
- Uncertainties: None
- Cross-reference status: References decisions#dont-panic, decisions#must-functions, GoTip #81
