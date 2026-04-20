---
# === CORE IDENTIFICATION ===
concept: "Don't Fire-and-Forget Goroutines"
slug: dont-fire-and-forget-goroutines

# === CLASSIFICATION ===
category: concurrency
subcategory: goroutine-lifecycle
tier: intermediate

# === PROVENANCE ===
source: "Uber Go Style Guide"
source_slug: uber-style
authors: "Prashant Varanasi, Simon Newton (and Uber Go team)"
chapter: "Guidelines"
chapter_number: 2
pdf_page: null
section: "Don't fire-and-forget goroutines"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "goroutine lifecycle management"
  - "no fire-and-forget goroutines"
  - "controlled goroutine lifetimes"

# === TYPED RELATIONSHIPS ===
prerequisites: []
extends: []
related:
  - avoid-init
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is a fire-and-forget goroutine?"
  - "How do I manage goroutine lifetimes properly?"
  - "How do I wait for goroutines to exit?"
  - "Why should goroutines not be spawned in init()?"
---

# Quick Definition

Every goroutine must have a controlled lifetime: either a predictable stop time or a mechanism to signal it to stop. There must always be a way to wait for the goroutine to finish. Never launch a goroutine without a plan for its termination.

# Core Definition

A "fire-and-forget" goroutine is one that is spawned with `go func()` without any mechanism to stop it or wait for it to complete. The Uber style guide prohibits this pattern because goroutines are not free -- they consume memory for their stack and CPU for scheduling. Unmanaged goroutines can cause:

- Significant performance issues when spawned in large numbers
- Memory leaks by preventing garbage collection of referenced objects
- Resource leaks by holding onto resources no longer needed

Every goroutine must satisfy two requirements:

1. **Predictable termination**: It must have a predictable time at which it stops, or there must be a way to signal it to stop.
2. **Waitable**: There must be a way for code to block and wait for the goroutine to finish.

The guide recommends using `go.uber.org/goleak` to test for goroutine leaks inside packages that may spawn goroutines.

# Prerequisites

Understanding of Go goroutines, channels, `sync.WaitGroup`, and the `select` statement.

# Key Properties

1. **Stop signal** -- Every goroutine should accept a stop signal, typically via a `chan struct{}` or `context.Context`.
2. **Done signal** -- Every goroutine should signal when it has finished, via a `chan struct{}` or `sync.WaitGroup`.
3. **No goroutines in init()** -- `init()` functions must never spawn goroutines. Background goroutines should be managed by objects with explicit lifecycle methods.
4. **Two waiting patterns** -- Use `sync.WaitGroup` for multiple goroutines; use a done channel for a single goroutine.
5. **Object-managed lifecycle** -- Packages that need background goroutines should expose an object with `Close`, `Stop`, or `Shutdown` methods.

# Construction / Recognition

## To Construct/Create:
1. Create a stop channel (`chan struct{}`) and a done channel for the goroutine.
2. In the goroutine, use `select` to listen for the stop signal alongside normal work.
3. Close the done channel (via `defer close(done)`) when the goroutine exits.
4. Provide a shutdown method that closes the stop channel and waits on the done channel.

## To Identify/Recognize:
1. Look for `go func()` or `go someFunc()` calls without corresponding wait mechanisms.
2. Check for goroutines that loop forever (`for { ... }`) without a stop condition.
3. Look for `init()` functions that spawn goroutines.

# Context & Application

- **Typical contexts**: Background workers, periodic flush/sync operations, event listeners, long-running tasks.
- **Common applications**: HTTP servers with background cleanup, message queue consumers, periodic metric reporters.

# Examples

**Example 1** (source: Uber Go Style Guide, Ch 2): Add stop/done channels to a background goroutine:

Bad:
```go
go func() {
  for {
    flush()
    time.Sleep(delay)
  }
}()
```

Good:
```go
var (
  stop = make(chan struct{}) // tells the goroutine to stop
  done = make(chan struct{}) // tells us that the goroutine exited
)
go func() {
  defer close(done)

  ticker := time.NewTicker(delay)
  defer ticker.Stop()
  for {
    select {
    case <-ticker.C:
      flush()
    case <-stop:
      return
    }
  }
}()

// Elsewhere...
close(stop)  // signal the goroutine to stop
<-done       // and wait for it to exit
```

**Example 2** (source: Uber Go Style Guide, Ch 2): Waiting for multiple goroutines with WaitGroup:

```go
var wg sync.WaitGroup
for i := 0; i < N; i++ {
  wg.Go(...)
}

// To wait for all to finish:
wg.Wait()
```

**Example 3** (source: Uber Go Style Guide, Ch 2): Object-managed goroutine lifecycle instead of init():

Bad:
```go
func init() {
  go doWork()
}

func doWork() {
  for {
    // ...
  }
}
```

Good:
```go
type Worker struct{ /* ... */ }

func NewWorker(...) *Worker {
  w := &Worker{
    stop: make(chan struct{}),
    done: make(chan struct{}),
    // ...
  }
  go w.doWork()
  return w
}

func (w *Worker) doWork() {
  defer close(w.done)
  for {
    // ...
    case <-w.stop:
      return
  }
}

// Shutdown tells the worker to stop
// and waits until it has finished.
func (w *Worker) Shutdown() {
  close(w.stop)
  <-w.done
}
```

# Relationships

- **Related to** `avoid-init`: The guide explicitly states that `init()` functions should not spawn goroutines. Background goroutines should be managed by objects with explicit lifecycle methods (Close/Stop/Shutdown).

# Common Errors

1. **Launching goroutines without wait mechanisms** -- `go doSomething()` without any way to wait for completion leads to goroutine leaks.
2. **Spawning goroutines in init()** -- This creates uncontrollable background work that starts as soon as the package is imported.
3. **Using time.Sleep instead of ticker with select** -- `time.Sleep` in a loop cannot be interrupted; use `time.NewTicker` with a `select` on a stop channel.
4. **Forgetting to defer close(done)** -- If the done channel is not closed on exit, callers waiting on `<-done` will block forever.

# Common Confusions

1. **"Fire-and-forget" definition** -- A fire-and-forget goroutine is one launched with no mechanism to stop it or detect when it finishes. It is not about whether the goroutine does useful work.
2. **WaitGroup vs. done channel** -- Use `sync.WaitGroup` when managing multiple goroutines that should all complete before proceeding. Use a done channel for a single goroutine.
3. **Goroutines are cheap but not free** -- While goroutines have low overhead individually, they still cost memory (stack) and CPU (scheduling). Unbounded spawning causes real performance problems.

# Source Reference

- Source: "Uber Go Style Guide"
- Chapter: "Guidelines" (Ch 2)
- Section: "Don't fire-and-forget goroutines"

# Verification Notes

- Extraction confidence: high -- Explicitly defined section with detailed rationale, multiple Bad/Good examples, and sub-sections on waiting patterns and init() restrictions.
