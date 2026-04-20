---
concept: Synchronous Functions
slug: synchronous-functions
category: concurrency
subcategory: function-design
tier: intermediate
source: "Google Go Style Guide"
source_slug: google-styleguide
authors: "Google Go Style Team"
chapter: "Style Decisions"
chapter_number: 3
pdf_page: null
section: "Synchronous functions"
extraction_confidence: high
aliases:
  - prefer synchronous
  - let caller manage concurrency
prerequisites:
  - go-goroutine-basics
  - goroutine-lifetimes-decisions
related:
  - goroutine-lifetimes-decisions
  - interfaces-decisions
contrasts_with: []
answers_questions:
  - "Should Go functions be synchronous or asynchronous?"
  - "Why are synchronous functions preferred in Go?"
  - "Who should manage goroutines -- the function or the caller?"
---

# Quick Definition

Prefer synchronous functions that return their results directly and finish any callbacks or channel operations before returning. Let the caller add concurrency by calling the function in a separate goroutine. It is much harder to remove unnecessary concurrency than to add it.

# Core Definition

> "Synchronous functions return their results directly and finish any callbacks or channel operations before returning. Prefer synchronous functions over asynchronous functions." -- Google Go Style Guide, "Synchronous functions"

> "Synchronous functions keep goroutines localized within a call. This helps to reason about their lifetimes, and avoid leaks and data races. Synchronous functions are also easier to test, since the caller can pass an input and check the output without the need for polling or synchronization." -- Google Go Style Guide, "Synchronous functions"

> "If necessary, the caller can add concurrency by calling the function in a separate goroutine. However, it is quite difficult (sometimes impossible) to remove unnecessary concurrency at the caller side." -- Google Go Style Guide, "Synchronous functions"

# Prerequisites

- Understanding of goroutines and concurrency in Go
- Knowledge of channels and synchronization primitives

# Key Properties

1. **Return directly**: Synchronous functions return results before the function returns, without requiring the caller to read from channels or poll.
2. **Localized goroutines**: Keeping concurrency within the caller's control makes lifetimes obvious.
3. **Easier to test**: No polling or synchronization needed in tests.
4. **No leaks or races**: Synchronous functions avoid the goroutine leaks and data races that come with async patterns.
5. **Caller adds concurrency**: `go syncFunc()` is trivial; removing embedded concurrency from an async API is not.

# Construction / Recognition

**Good -- synchronous function, caller adds concurrency if needed:**

```go
func Process(data []byte) (*Result, error) {
    // do all work synchronously
    return result, nil
}

// Caller adds concurrency:
go func() {
    result, err := Process(data)
    // ...
}()
```

**Bad -- function that forces concurrency on the caller:**

```go
func Process(data []byte) <-chan *Result {
    ch := make(chan *Result)
    go func() {
        // ... do work ...
        ch <- result
    }()
    return ch
}
```

# Context & Application

The asymmetry between adding and removing concurrency is the core insight. A synchronous function can always be called concurrently by wrapping it in a goroutine. But an asynchronous function that spawns goroutines internally cannot be "un-concurrentified" by callers -- they must deal with channels, synchronization, and goroutine lifecycle management whether they want to or not. This principle is closely related to goroutine lifetime management.

# Examples

See Construction / Recognition above for illustrative examples.

# Relationships

- **goroutine-lifetimes-decisions**: Synchronous functions are the primary tool for making goroutine lifetimes obvious.

# Common Errors

1. Making functions asynchronous by default "for performance."
2. Returning channels instead of values.
3. Spawning goroutines inside library functions when callers could manage concurrency.

# Common Confusions

- **Not anti-concurrency**: The guidance is not against concurrency; it is against embedding concurrency decisions inside library functions. Let the caller decide.
- **When async is necessary**: Some APIs are inherently asynchronous (e.g., event streams). The guidance is about preferring synchronous as the default.

# Source Reference

Google Go Style Guide, "Style Decisions" chapter, "Synchronous functions" section. See also "Rethinking Classical Concurrency Patterns" (Bryan Mills).

# Verification Notes

Confidence: high. All guidance is directly from the source text.
