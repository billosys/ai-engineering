---
# === CORE IDENTIFICATION ===
concept: Variadic Options (Best Practices)
slug: variadic-options-bp

# === CLASSIFICATION ===
category: api-design
subcategory: function-arguments
tier: advanced

# === PROVENANCE ===
source: "Google Go Style Guide"
source_slug: google-styleguide
authors: "Google Go Style Team"
chapter: "Best Practices"
chapter_number: 4
pdf_page: null
section: "Variadic options"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "functional options"
  - "option functions"
  - "variadic option pattern"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - option-structure
extends: []
related: []
contrasts_with:
  - option-structure

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "When should I use variadic options instead of option structs?"
  - "How do I implement the functional options pattern in Go?"
  - "Should option functions accept parameters or use presence as signal?"
---

# Quick Definition

Variadic option functions are closures passed via `...` parameters that configure a function. Options take no space when not used, can accept multiple parameters, and support third-party extensions. Use when most callers need no options, options are rarely used, or options could fail. Options should accept parameters (not use presence as signal).

# Core Definition

The variadic options pattern uses exported functions that return closures, which are then passed to a function via a variadic (`...`) parameter. Each closure accepts a mutable reference (typically a pointer to an unexported struct) and updates it based on inputs. Benefits include: no space at call sites when no configuration is needed, options are values that can be shared and accumulated, options can accept multiple parameters, named return types group options in godoc, and packages can allow or prevent third-party option definitions. This pattern requires substantial additional code and should only be used when benefits outweigh overhead. Options should accept parameters for their value (e.g., `FailFast(enable bool)`) rather than using presence to signal their value (e.g., `EnableFailFast()`), because the latter makes dynamic composition difficult. When an option is passed multiple times, the last argument should win. The parameter to option functions is generally unexported to restrict option definition to the package.

# Prerequisites

- **option-structure** -- Understanding the simpler option struct pattern

# Key Properties

1. Options are functions returning closures that modify an unexported config struct
2. Zero-cost at call sites when no options are provided
3. Options are values: can be shared, accumulated, composed
4. Options can accept multiple parameters and return errors
5. Named return type groups options together in godoc
6. Options should accept parameters, not use presence as signal
7. Last argument wins when options conflict or are repeated
8. Unexported config struct restricts option definition to the package

# Construction / Recognition

## To Apply:
1. Define an unexported options struct
2. Define an exported option type: `type FooOption func(*fooOptions)`
3. Create exported functions returning option closures
4. Accept `opts ...FooOption` as the last parameter
5. Apply default options first, then caller options
6. Options should accept parameters (e.g., `Enabled(bool)` not `Enable()`)

## To Recognize:
1. Functions with `...Option` as last parameter
2. Option functions that return closures
3. Clean call sites with zero or few options

# Context & Application

Prefer variadic options when: most callers need no options, most options are infrequently used, there are many options, options require arguments, options could fail, or users/other packages can provide custom options. The pattern originates from Rob Pike's blog post on self-referential functions and Dave Cheney's talk on functional options. The substantial boilerplate code means this pattern should only be used when the flexibility is genuinely needed.

# Examples

**Example 1 -- Variadic option implementation**:

```go
// Good:
type replicationOptions struct {
    readonlyCells       []string
    replicateExisting   bool
    overwritePolicies   bool
    replicationInterval time.Duration
    copyWorkers         int
    healthWatcher       health.Watcher
}

type ReplicationOption func(*replicationOptions)

func ReadonlyCells(cells ...string) ReplicationOption {
    return func(opts *replicationOptions) {
        opts.readonlyCells = append(opts.readonlyCells, cells...)
    }
}

func ReplicateExisting(enabled bool) ReplicationOption {
    return func(opts *replicationOptions) {
        opts.replicateExisting = enabled
    }
}

var DefaultReplicationOptions = []ReplicationOption{
    OverwritePolicies(true),
    ReplicationInterval(12 * time.Hour),
    CopyWorkers(10),
}

func EnableReplication(ctx context.Context, config *placer.Config, primaryCells []string, opts ...ReplicationOption) {
    var options replicationOptions
    for _, opt := range DefaultReplicationOptions {
        opt(&options)
    }
    for _, opt := range opts {
        opt(&options)
    }
}
```

**Example 2 -- Call sites**:

```go
// Complex call:
storage.EnableReplication(ctx, config, []string{"po", "is", "ea"},
    storage.ReadonlyCells("ix", "gg"),
    storage.OverwritePolicies(true),
    storage.ReplicationInterval(1*time.Hour),
    storage.CopyWorkers(100),
    storage.HealthWatcher(watcher),
)

// Simple call (no options needed):
storage.EnableReplication(ctx, config, []string{"po", "is", "ea"})
```

# Relationships

## Related
(none)

## Contrasts With
- **option-structure** -- Simpler pattern for when most callers need options; variadic options for when most don't

# Common Errors

- **Error**: Using presence to signal option value (e.g., `EnableFailFast()` instead of `FailFast(true)`)
  **Correction**: Accept parameters so users can dynamically compose options

- **Error**: Using variadic options when an option struct would suffice
  **Correction**: Only use variadic options when the additional code overhead is justified

# Common Confusions

- **Confusion**: Thinking variadic options are always better than option structs
  **Clarification**: Variadic options require substantial code; only use when benefits outweigh overhead

- **Confusion**: Making the config struct exported
  **Clarification**: Keep it unexported to restrict option definition to the package (unless extension is desired)

# Source Reference

Chapter 4: Best Practices, Section "Function argument lists" > "Variadic options".

# Verification Notes

- Definition source: Directly from "Variadic options" section of Best Practices
- Confidence rationale: HIGH -- extensive guidance with full implementation example
- Uncertainties: None
- Cross-reference status: References Rob Pike's blog post, Dave Cheney's talk
