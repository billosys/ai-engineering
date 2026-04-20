---
# === CORE IDENTIFICATION ===
concept: Exit in Main
slug: exit-in-main

# === CLASSIFICATION ===
category: code-safety
subcategory: program-lifecycle
tier: foundational

# === PROVENANCE ===
source: "Uber Go Style Guide"
source_slug: uber-style
authors: "Prashant Varanasi, Simon Newton (and Uber Go team)"
chapter: "Guidelines"
chapter_number: 2
pdf_page: null
section: "Exit in Main"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "os.Exit only in main"
  - "log.Fatal only in main"
  - "exit once"

# === TYPED RELATIONSHIPS ===
prerequisites: []
extends: []
related:
  - avoid-init
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How does init() avoidance relate to exit-in-main?"
  - "Why should os.Exit and log.Fatal only be called in main()?"
  - "How do I structure main() to exit cleanly?"
---

# Quick Definition

Only call `os.Exit` or `log.Fatal*` in `main()`; all other functions should return errors to signal failure. Prefer calling exit at most once in `main()`.

# Core Definition

Go programs use `os.Exit` or `log.Fatal*` to exit immediately. The Uber style guide mandates that these calls should appear **only in `main()`**. All other functions must return errors to signal failure, allowing the caller to decide how to handle them. This preserves testability, enables proper cleanup via `defer`, and keeps control flow obvious.

Additionally, programs should prefer to call `os.Exit` or `log.Fatal` **at most once** in `main()`. The recommended pattern is to extract business logic into a `run()` function that returns an error (or exit code), and have `main()` simply call `run()` and handle the single exit point.

# Prerequisites

Understanding Go's `os.Exit`, `log.Fatal`, `defer`, and error return conventions.

# Key Properties

1. **Single exit point** -- Consolidating exit calls into `main()` makes the program's termination behavior obvious.
2. **Testability** -- Functions that call `os.Exit` or `log.Fatal` cannot be tested because they terminate the test process. Functions that return errors can be tested normally.
3. **Defer preservation** -- `os.Exit` and `log.Fatal` skip `defer` statements. Confining exit calls to `main()` ensures deferred cleanup in other functions always runs.
4. **Control flow clarity** -- When any function can exit the program, it becomes difficult to reason about control flow.
5. **The run() pattern** -- Extract business logic into a `run()` function that returns an error or exit code. `main()` calls `run()` and handles the exit.

# Construction / Recognition

## To Construct/Create:
1. Create a `run()` function that contains all program logic and returns an error (or exit code).
2. In `main()`, call `run()` and use `log.Fatal(err)` or `os.Exit(code)` based on the result.
3. Remove all `os.Exit` and `log.Fatal` calls from non-main functions; replace with error returns.

## To Identify/Recognize:
1. Search for `os.Exit` or `log.Fatal` calls outside of `main()` -- these violate the guideline.
2. Functions that call `log.Fatal` on error instead of returning the error.

# Context & Application

- **Typical contexts**: CLI applications, server programs, any Go program with multiple functions that could encounter fatal errors.
- **Common applications**: Structuring `main()` as a thin wrapper around a testable `run()` function; ensuring all cleanup code runs via `defer`.

# Examples

**Example 1** (source: Uber Go Style Guide, Ch 2): Move exit calls out of helper functions:

Bad:
```go
func main() {
  body := readFile(path)
  fmt.Println(body)
}

func readFile(path string) string {
  f, err := os.Open(path)
  if err != nil {
    log.Fatal(err)
  }

  b, err := io.ReadAll(f)
  if err != nil {
    log.Fatal(err)
  }

  return string(b)
}
```

Good:
```go
func main() {
  body, err := readFile(path)
  if err != nil {
    log.Fatal(err)
  }
  fmt.Println(body)
}

func readFile(path string) (string, error) {
  f, err := os.Open(path)
  if err != nil {
    return "", err
  }

  b, err := io.ReadAll(f)
  if err != nil {
    return "", err
  }

  return string(b), nil
}
```

**Example 2** (source: Uber Go Style Guide, Ch 2): Use the run() pattern for a single exit point:

Bad:
```go
package main

func main() {
  args := os.Args[1:]
  if len(args) != 1 {
    log.Fatal("missing file")
  }
  name := args[0]

  f, err := os.Open(name)
  if err != nil {
    log.Fatal(err)
  }
  defer f.Close()

  // If we call log.Fatal after this line,
  // f.Close will not be called.

  b, err := io.ReadAll(f)
  if err != nil {
    log.Fatal(err)
  }

  // ...
}
```

Good:
```go
package main

func main() {
  if err := run(); err != nil {
    log.Fatal(err)
  }
}

func run() error {
  args := os.Args[1:]
  if len(args) != 1 {
    return errors.New("missing file")
  }
  name := args[0]

  f, err := os.Open(name)
  if err != nil {
    return err
  }
  defer f.Close()

  b, err := io.ReadAll(f)
  if err != nil {
    return err
  }

  // ...
}
```

# Relationships

- **Related to** `avoid-init`: Both guidelines push program setup and teardown logic toward `main()`. Avoiding `init()` means explicit initialization in `main()`; exit-in-main means only `main()` terminates the process.

# Common Errors

1. **Calling log.Fatal in library code** -- Library functions should never terminate the process; they should return errors so the caller can decide what to do.
2. **Multiple log.Fatal calls in main()** -- Calling `log.Fatal` after `defer` statements means deferred cleanup is skipped. Use a single exit point after the `run()` pattern.
3. **Using panic as an exit mechanism** -- Panicking is not a proper exit strategy. Use error returns and `os.Exit` in `main()`.

# Common Confusions

1. **log.Fatal vs. log.Println** -- `log.Fatal` calls `os.Exit(1)` after logging; `log.Println` does not exit. Only `log.Fatal*` is restricted to `main()`.
2. **The run() function is not prescriptive** -- The name, signature, and setup of `run()` are flexible. It can accept arguments, return exit codes, or use a custom error type.

# Source Reference

- Source: "Uber Go Style Guide"
- Chapter: "Guidelines" (Ch 2)
- Section: "Exit in Main"

# Verification Notes

- Extraction confidence: high -- Explicitly defined section with clear Bad/Good examples, detailed rationale, and the run() pattern.
