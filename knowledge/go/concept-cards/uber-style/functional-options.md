---
concept: Functional Options
slug: functional-options
category: patterns
subcategory: constructor-design
tier: intermediate
source: "Uber Go Style Guide"
source_slug: uber-style
authors: "Prashant Varanasi, Simon Newton"
chapter: "Patterns"
chapter_number: 5
pdf_page: null
section: "Functional Options"
extraction_confidence: high
aliases:
  - functional options pattern
  - option interface pattern
  - self-referential functions
prerequisites:
  - go-interfaces
  - go-variadic-functions
extends: []
related:
  - avoid-naked-parameters
contrasts_with: []
answers_questions:
  - "What is the functional options pattern in Go?"
  - "How do I implement the functional options pattern?"
  - "What must I understand before using the functional options pattern?"
  - "When should I use functional options?"
---

# Quick Definition

Functional options is a pattern where an opaque `Option` interface type records configuration on an internal struct. Constructors accept `...Option` variadic parameters, letting callers provide only the options they need while defaults handle the rest.

# Core Definition

The Uber Go Style Guide describes functional options as a pattern for extensible constructors and public APIs. An `Option` interface with an unexported `apply` method records configuration on an unexported `options` struct. Each option is implemented as a type satisfying the `Option` interface, with a public `WithXxx` constructor function.

The guide recommends this pattern when a function already has three or more arguments, or when the API is expected to grow over time. It is preferred over parameter structs for its extensibility and over naked parameters for its readability.

> "Functional options is a pattern in which you declare an opaque `Option` type that records information in some internal struct. You accept a variadic number of these options and act upon the full information recorded by the options on the internal struct." -- Uber Go Style Guide, "Functional Options"

The guide explicitly recommends the interface-based approach over closures, noting that interfaces allow options to be compared in tests and mocks, and can implement additional interfaces like `fmt.Stringer`.

# Prerequisites

- Understanding of Go interfaces and interface satisfaction
- Knowledge of variadic functions (`...Option`)
- Familiarity with unexported types and methods for encapsulation

# Key Properties

1. **Opaque Option type**: The `Option` interface has an unexported method (`apply(*options)`), preventing external implementations.
2. **Variadic acceptance**: Constructors use `...Option` to accept zero or more options.
3. **Defaults in constructor**: The constructor initializes an `options` struct with defaults, then applies each option.
4. **WithXxx constructors**: Each option has a public `WithXxx` function returning an `Option`.
5. **Interface over closures**: The interface approach supports comparison in tests, implements `fmt.Stringer`, and is easier to debug.
6. **Use when 3+ arguments**: Apply this pattern when a function has three or more arguments, especially optional ones.

# Construction / Recognition

**Full implementation pattern:**

```go
type options struct {
  cache  bool
  logger *zap.Logger
}

type Option interface {
  apply(*options)
}

type cacheOption bool

func (c cacheOption) apply(opts *options) {
  opts.cache = bool(c)
}

func WithCache(c bool) Option {
  return cacheOption(c)
}

type loggerOption struct {
  Log *zap.Logger
}

func (l loggerOption) apply(opts *options) {
  opts.logger = l.Log
}

func WithLogger(log *zap.Logger) Option {
  return loggerOption{Log: log}
}

// Open creates a connection.
func Open(
  addr string,
  opts ...Option,
) (*Connection, error) {
  options := options{
    cache:  defaultCache,
    logger: zap.NewNop(),
  }

  for _, o := range opts {
    o.apply(&options)
  }

  // ...
}
```

**Usage -- callers provide only what they need:**

```go
db.Open(addr)
db.Open(addr, db.WithLogger(log))
db.Open(addr, db.WithCache(false))
db.Open(
  addr,
  db.WithCache(false),
  db.WithLogger(log),
)
```

**Bad -- all parameters required even for defaults:**

```go
func Open(
  addr string,
  cache bool,
  logger *zap.Logger
) (*Connection, error) {
  // ...
}

db.Open(addr, db.DefaultCache, zap.NewNop())
db.Open(addr, db.DefaultCache, log)
db.Open(addr, false /* cache */, zap.NewNop())
db.Open(addr, false /* cache */, log)
```

# Context & Application

Use functional options for constructors and public APIs that you foresee needing to expand. The pattern is backward-compatible: adding a new option does not change existing call sites. It is particularly valuable for library APIs where breaking changes must be avoided.

The pattern is overkill for simple functions with few, clear parameters. Reserve it for APIs with optional configuration.

# Examples

See Construction / Recognition above for the complete implementation from the source.

# Relationships

- **avoid-naked-parameters**: Functional options solve the naked parameter problem for constructor functions by replacing opaque positional arguments with named, self-documenting options.

# Common Errors

1. Using closures instead of the interface approach -- closures cannot be compared in tests or implement `fmt.Stringer`.
2. Exporting the `options` struct or the `apply` method -- these should remain unexported to maintain encapsulation.
3. Applying the pattern to simple functions that do not need extensibility -- adds unnecessary complexity.

# Common Confusions

- **Functional options vs parameter structs**: Parameter structs (`Config` structs) are simpler but less extensible. Functional options allow adding new options without changing existing call sites and support validation logic in each option's `apply` method.
- **Interface-based vs closure-based**: The Uber guide specifically recommends the interface approach. Closure-based functional options (where `Option` is `func(*options)`) are simpler but less powerful for testing and debugging.
- **Required vs optional parameters**: Required parameters (like `addr`) remain positional. Only optional parameters become `Option` values.

# Source Reference

Uber Go Style Guide, "Patterns" chapter, "Functional Options" section. See also referenced articles: "Self-referential functions and the design of options" (Rob Pike) and "Functional options for friendly APIs" (Dave Cheney).

# Verification Notes

Confidence: high. The complete pattern implementation, usage examples, rationale for interface over closures, and all code are directly from the source text.
