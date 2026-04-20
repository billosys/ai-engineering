---
concept: Avoid Mutable Globals
slug: avoid-mutable-globals
category: code-safety
subcategory: dependency-injection
tier: intermediate
source: "Uber Go Style Guide"
source_slug: uber-style
authors: "Prashant Varanasi, Simon Newton"
chapter: "Guidelines"
chapter_number: 2
pdf_page: null
section: "Avoid Mutable Globals"
extraction_confidence: high
aliases:
  - no mutable globals
  - dependency injection over globals
prerequisites:
  - go-structs
related:
  - use-uber-atomic
contrasts_with: []
answers_questions:
  - "Why should mutable global variables be avoided in Go?"
  - "How does dependency injection replace mutable globals?"
---

# Quick Definition

Avoid mutating global variables; use dependency injection instead. Mutable globals make code difficult to test (requiring save/restore of global state) and create implicit coupling. Inject dependencies as struct fields so they can be replaced in tests without affecting global state.

# Core Definition

> "Avoid mutating global variables, instead opting for dependency injection. This applies to function pointers as well as other kinds of values." -- Uber Go Style Guide, "Avoid Mutable Globals"

# Prerequisites

- Understanding of Go package-level variables
- Familiarity with struct-based dependency injection
- Knowledge of Go testing patterns

# Key Properties

1. **Global mutation creates test fragility**: Tests must save and restore global state, and parallel tests may interfere with each other.
2. **Function pointers count**: The guidance applies to global function pointers (e.g., `var _timeNow = time.Now`) as well as data values.
3. **Struct fields enable injection**: Moving the dependency to a struct field allows each test (or caller) to provide its own implementation.
4. **Clearer dependencies**: Struct fields make dependencies explicit and visible in the type definition.

# Construction / Recognition

**Bad -- mutable global function pointer:**

```go
// sign.go
var _timeNow = time.Now

func sign(msg string) string {
  now := _timeNow()
  return signWithTime(msg, now)
}
```

```go
// sign_test.go
func TestSign(t *testing.T) {
  oldTimeNow := _timeNow
  _timeNow = func() time.Time {
    return someFixedTime
  }
  defer func() { _timeNow = oldTimeNow }()

  assert.Equal(t, want, sign(give))
}
```

**Good -- dependency injection via struct field:**

```go
// sign.go
type signer struct {
  now func() time.Time
}

func newSigner() *signer {
  return &signer{
    now: time.Now,
  }
}

func (s *signer) Sign(msg string) string {
  now := s.now()
  return signWithTime(msg, now)
}
```

```go
// sign_test.go
func TestSigner(t *testing.T) {
  s := newSigner()
  s.now = func() time.Time {
    return someFixedTime
  }

  assert.Equal(t, want, s.Sign(give))
}
```

# Context & Application

Mutable globals are a common pattern for injecting test doubles in Go, but they introduce shared mutable state at the package level. This breaks test isolation (parallel tests overwrite each other's globals) and makes it harder to reason about what a function depends on. The dependency injection alternative encapsulates dependencies in the struct, making each instance independent.

# Examples

See Construction / Recognition above for the complete source examples showing both the production code and test code patterns.

# Relationships

- **use-uber-atomic**: If globals must exist, atomic access prevents data races. But avoiding mutable globals entirely is the preferred approach.

# Common Errors

1. Forgetting to restore the global in a `defer`, causing test pollution across test cases.
2. Running tests in parallel (`t.Parallel()`) while mutating package-level globals, causing flaky tests.
3. Using `init()` to set up mutable globals, compounding the problem with implicit initialization order.

# Common Confusions

- **Immutable globals are fine**: The guidance is about *mutable* globals. Constants and immutable package-level variables (like compiled regexps or frozen configuration) are acceptable.
- **Dependency injection does not require interfaces**: In the source example, the dependency is a `func() time.Time` field, not an interface. Interfaces are one tool for DI, but concrete function fields work well for simple cases.

# Source Reference

Uber Go Style Guide, "Guidelines" chapter, "Avoid Mutable Globals" section.

# Verification Notes

Confidence: high. The guidance, rationale, and both bad/good code examples (including test code) are directly from the source.
