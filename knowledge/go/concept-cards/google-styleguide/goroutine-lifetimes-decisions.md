---
concept: Goroutine Lifetimes
slug: goroutine-lifetimes-decisions
category: concurrency
subcategory: goroutine-management
tier: intermediate
source: "Google Go Style Guide"
source_slug: google-styleguide
authors: "Google Go Style Team"
chapter: "Style Decisions"
chapter_number: 3
pdf_page: null
section: "Goroutine lifetimes"
extraction_confidence: high
aliases:
  - goroutine lifecycle
  - goroutine exit conditions
prerequisites:
  - go-goroutine-basics
  - go-context-basics
related:
  - synchronous-functions
  - dont-panic-decisions
contrasts_with: []
answers_questions:
  - "How should goroutine lifetimes be managed in Go?"
  - "What problems arise from fire-and-forget goroutines?"
  - "How should context be used for goroutine cancellation?"
---

# Quick Definition

When spawning goroutines, make it clear when and whether they exit. Use `context.Context` for cancellation, `sync.WaitGroup` to prevent goroutines from outliving their parent, and keep synchronization logic constrained within function scope. Avoid fire-and-forget goroutines.

# Core Definition

> "When you spawn goroutines, make it clear when or whether they exit." -- Google Go Style Guide, "Goroutine lifetimes"

> "Concurrent code should be written such that the goroutine lifetimes are obvious. Typically this will mean keeping synchronization-related code constrained within the scope of a function and factoring out the logic into synchronous functions." -- Google Go Style Guide, "Goroutine lifetimes"

# Prerequisites

- Understanding of goroutines and channels
- Knowledge of `context.Context` and cancellation
- Familiarity with `sync.WaitGroup`

# Key Properties

1. **Explicit exit conditions**: Every goroutine must have a clear termination condition.
2. **Channel leak risk**: Goroutines blocked on channel sends/receives are not garbage collected, even if no other goroutine holds a reference to the channel.
3. **Context for cancellation**: Use `context.Context` to manage goroutine lifetimes conventionally.
4. **WaitGroup to bound lifetime**: Use `sync.WaitGroup` to ensure spawned goroutines complete before the parent function returns.
5. **No fire-and-forget**: Goroutines without clear exit conditions cause undefined behavior, leak resources, and are difficult to test.

# Construction / Recognition

**Good -- goroutine lifetime managed with context and WaitGroup:**

```go
func (w *Worker) Run(ctx context.Context) error {
    var wg sync.WaitGroup
    // ...
    for item := range w.q {
        // process returns at latest when the context is cancelled.
        wg.Add(1)
        go func() {
            defer wg.Done()
            process(ctx, item)
        }()
    }
    // ...
    wg.Wait()  // Prevent spawned goroutines from outliving this function.
}
```

**Bad -- fire-and-forget goroutine with no exit condition:**

```go
func (w *Worker) Run() {
    // ...
    for item := range w.q {
        // process returns when it finishes, if ever, possibly not cleanly
        // handling a state transition or termination of the Go program itself.
        go process(item)
    }
    // ...
}
```

**Bad -- sending on a closed channel causes panic:**

```go
ch := make(chan int)
ch <- 42
close(ch)
ch <- 13 // panic
```

# Context & Application

Fire-and-forget goroutines create three categories of problems: (1) resource leaks when goroutines block forever on channels, (2) data races when goroutines modify inputs after the caller has moved on, and (3) unpredictable memory usage from arbitrarily long-lived goroutines. Code that manages goroutine lifetimes explicitly is also far easier to test because the caller can wait for all work to complete before making assertions.

# Examples

See Construction / Recognition above for the complete set of source examples.

# Relationships

- **synchronous-functions**: Prefer synchronous functions; let the caller add concurrency.
- **dont-panic-decisions**: Panics in goroutines are especially dangerous -- they crash the process.

# Common Errors

1. Spawning goroutines without any mechanism to wait for their completion.
2. Not using `context.Context` for cancellation, making goroutines impossible to stop.
3. Sending on channels after they are closed.
4. Leaving goroutines in-flight that modify shared state.

# Common Confusions

- **Garbage collection does not stop goroutines**: A blocked goroutine is never collected, even if nothing references its channel.
- **Testing difficulty**: Fire-and-forget goroutines make tests non-deterministic because there is no way to know when work is complete.
- **Multiple mechanisms**: WaitGroups, signal channels (`chan struct{}`), and condition variables are all valid; the key is that the exit condition is evident.

# Source Reference

Google Go Style Guide, "Style Decisions" chapter, "Goroutine lifetimes" section. See also "Never start a goroutine without knowing how it will stop" (Dave Cheney).

# Verification Notes

Confidence: high. All guidance and code examples are directly from the source text.
