---
# === CORE IDENTIFICATION ===
concept: Channel Direction
slug: channel-direction

# === CLASSIFICATION ===
category: concurrency
subcategory: channels
tier: foundational

# === PROVENANCE ===
source: "Google Go Style Guide"
source_slug: google-styleguide
authors: "Google Go Style Team"
chapter: "Best Practices"
chapter_number: 4
pdf_page: null
section: "Channel direction"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "directional channels"
  - "send-only channels"
  - "receive-only channels"

# === TYPED RELATIONSHIPS ===
prerequisites: []
extends: []
related:
  - variable-declarations-bp
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "Why should I specify channel direction in function signatures?"
  - "How does channel direction prevent bugs?"
  - "What does channel direction convey about ownership?"
---

# Quick Definition

Specify channel direction (`<-chan` for receive-only, `chan<-` for send-only) in function signatures where possible. This prevents programming errors (like accidentally closing a channel you only read from) and conveys ownership semantics.

# Core Definition

When a function only reads from or only writes to a channel, specify the direction in the parameter type. Using `<-chan T` for receive-only and `chan<- T` for send-only enables the compiler to catch mistakes like closing a receive-only channel or sending on a receive-only channel. Direction specification also conveys a measure of ownership to the type -- it tells the reader and compiler which operations the function is permitted to perform. Without direction specification, a function receiving `chan int` could accidentally close the channel, causing a panic if another goroutine later tries to close it again.

# Prerequisites

(none)

# Key Properties

1. `<-chan T`: receive-only -- can read and range, but not send or close
2. `chan<- T`: send-only -- can send, but not receive or close
3. Compiler enforces direction constraints, catching bugs at compile time
4. Direction conveys ownership semantics to readers
5. Bidirectional `chan T` automatically converts to directional when passed

# Construction / Recognition

## To Apply:
1. If a function only reads from a channel, declare it as `<-chan T`
2. If a function only writes to a channel, declare it as `chan<- T`
3. Only use bidirectional `chan T` when the function both sends and receives

## To Recognize:
1. Function signatures with `<-chan` or `chan<-` parameters
2. Compile-time errors when direction is violated

# Context & Application

This is a simple but effective practice that catches a class of concurrency bugs at compile time. The classic example is a function that sums values from a channel -- specifying `<-chan int` prevents the function from accidentally closing the channel, which would cause a panic if the sender tried to close it too.

# Examples

**Example 1 -- Good: specified direction**:

```go
// Good:
// sum reads from the channel until it is closed.
func sum(values <-chan int) int {
    // ...
}
```

**Example 2 -- Bad: unspecified direction allows bugs**:

```go
// Bad:
func sum(values chan int) (out int) {
    for v := range values {
        out += v
    }
    // values must already be closed for this code to be reachable, which means
    // a second close triggers a panic.
    close(values)
}
```

# Relationships

## Related
- **variable-declarations-bp** -- Channel direction is part of good variable/parameter declaration

## Contrasts With
(none)

# Common Errors

- **Error**: Using bidirectional `chan T` when only one direction is needed
  **Correction**: Specify `<-chan T` or `chan<- T` to enable compile-time checks

- **Error**: Closing a channel in a function that should only be reading from it
  **Correction**: Using `<-chan T` makes this a compile-time error

# Common Confusions

- **Confusion**: Thinking channel direction is only about documentation
  **Clarification**: The compiler enforces direction constraints, preventing real bugs

- **Confusion**: Not knowing that bidirectional channels convert automatically to directional
  **Clarification**: You can pass a `chan T` to a function expecting `<-chan T` or `chan<- T`

# Source Reference

Chapter 4: Best Practices, Section "Variable declarations" > "Channel direction".

# Verification Notes

- Definition source: Directly from "Channel direction" section of Best Practices
- Confidence rationale: HIGH -- explicit guidance with good/bad examples
- Uncertainties: None
- Cross-reference status: References Bryan Mills' "Rethinking Classical Concurrency Patterns"
