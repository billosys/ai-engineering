---
concept: Don't Panic
slug: dont-panic
category: code-safety
subcategory: error-handling
tier: foundational
source: "Uber Go Style Guide"
source_slug: uber-style
authors: "Prashant Varanasi, Simon Newton"
chapter: "Guidelines"
chapter_number: 2
pdf_page: null
section: "Don't Panic"
extraction_confidence: high
aliases:
  - avoid panic
  - no panic in production
prerequisites:
  - error-types
  - go-error-interface
related:
  - handle-errors-once
  - error-wrapping
  - handle-type-assertion-failures
contrasts_with: []
answers_questions:
  - "When is it acceptable to use panic in Go?"
  - "Why should production Go code avoid panics?"
---

# Quick Definition

Production Go code must return errors instead of panicking. Panics are reserved for truly irrecoverable situations such as nil dereferences, and for program initialization (e.g., `template.Must`). In tests, prefer `t.Fatal` or `t.FailNow` over panics.

# Core Definition

> "Code running in production must avoid panics. Panics are a major source of cascading failures. If an error occurs, the function must return an error and allow the caller to decide how to handle it." -- Uber Go Style Guide, "Don't Panic"

> "Panic/recover is not an error handling strategy. A program must panic only when something irrecoverable happens such as a nil dereference. An exception to this is program initialization: bad things at program startup that should abort the program may cause panic." -- Uber Go Style Guide, "Don't Panic"

# Prerequisites

- Understanding of Go's `panic` and `recover` mechanism
- Knowledge of the `error` interface and error return patterns
- Familiarity with Go testing framework (`t.Fatal`, `t.FailNow`)

# Key Properties

1. **Panics cause cascading failures**: A panic in one goroutine can crash the entire program.
2. **Return errors instead**: Functions should return `error` values and let callers decide how to handle failures.
3. **Acceptable panic uses**: Program initialization (e.g., `template.Must`), truly irrecoverable conditions (nil dereference).
4. **Testing**: Use `t.Fatal` or `t.FailNow` instead of `panic` so tests are properly marked as failed.

# Construction / Recognition

**Bad -- panicking on a handleable error:**

```go
func run(args []string) {
  if len(args) == 0 {
    panic("an argument is required")
  }
  // ...
}

func main() {
  run(os.Args[1:])
}
```

**Good -- returning an error:**

```go
func run(args []string) error {
  if len(args) == 0 {
    return errors.New("an argument is required")
  }
  // ...
  return nil
}

func main() {
  if err := run(os.Args[1:]); err != nil {
    fmt.Fprintln(os.Stderr, err)
    os.Exit(1)
  }
}
```

**Acceptable panic -- program initialization:**

```go
var _statusTemplate = template.Must(template.New("name").Parse("_statusHTML"))
```

**Bad -- panic in tests:**

```go
// func TestFoo(t *testing.T)
f, err := os.CreateTemp("", "test")
if err != nil {
  panic("failed to set up test")
}
```

**Good -- t.Fatal in tests:**

```go
// func TestFoo(t *testing.T)
f, err := os.CreateTemp("", "test")
if err != nil {
  t.Fatal("failed to set up test")
}
```

# Context & Application

Panics bypass Go's explicit error handling model. When a function panics instead of returning an error, callers lose the ability to decide how to handle the failure -- whether to retry, degrade gracefully, or propagate with context. In production services, an unrecovered panic in any goroutine terminates the entire process, potentially causing cascading failures across a distributed system.

# Examples

See Construction / Recognition above for the complete set of source examples.

# Relationships

- **handle-type-assertion-failures**: One common source of panics that the comma-ok idiom prevents.
- **handle-errors-once**: Defines valid strategies for handling errors that are returned instead of panicked.
- **error-wrapping**: Used to add context when returning errors instead of panicking.

# Common Errors

1. Using `panic` for input validation in library code -- callers cannot recover gracefully.
2. Using `panic` in tests instead of `t.Fatal` -- the test framework cannot properly report the failure.
3. Using `panic`/`recover` as a general error handling mechanism akin to try/catch.

# Common Confusions

- **`panic`/`recover` is not try/catch**: Go's `recover` exists for truly exceptional situations, not as a general control flow mechanism.
- **`template.Must` and similar**: These are acceptable because they run at program initialization where failing fast is the correct behavior.

# Source Reference

Uber Go Style Guide, "Guidelines" chapter, "Don't Panic" section.

# Verification Notes

Confidence: high. The guidance, exceptions (initialization, nil dereference), testing recommendation (`t.Fatal`), and all code examples are directly from the source.
