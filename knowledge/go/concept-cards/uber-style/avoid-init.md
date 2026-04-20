---
# === CORE IDENTIFICATION ===
concept: Avoid init()
slug: avoid-init

# === CLASSIFICATION ===
category: code-safety
subcategory: initialization
tier: intermediate

# === PROVENANCE ===
source: "Uber Go Style Guide"
source_slug: uber-style
authors: "Prashant Varanasi, Simon Newton (and Uber Go team)"
chapter: "Guidelines"
chapter_number: 2
pdf_page: null
section: "Avoid init()"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "no init functions"
  - "avoid init functions"
  - "init() avoidance"

# === TYPED RELATIONSHIPS ===
prerequisites: []
extends: []
related:
  - exit-in-main
  - dont-fire-and-forget-goroutines
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How does init() avoidance relate to exit-in-main?"
  - "When is init() acceptable to use?"
  - "Why should init() functions be avoided?"
  - "What are the risks of using init() in Go?"
---

# Quick Definition

Avoid `init()` where possible; when unavoidable, ensure `init()` is deterministic, does not depend on ordering of other `init()` functions, avoids global/environment state, and performs no I/O.

# Core Definition

The `init()` function in Go runs automatically at package initialization time, before `main()`. The Uber style guide recommends avoiding `init()` because it introduces implicit behavior that is hard to reason about, test, and maintain. When `init()` functions depend on each other or interact with global state, code becomes brittle and error-prone. Instead, prefer explicit initialization through variable declarations, helper functions, or initialization logic called from `main()`.

When `init()` is unavoidable, the code should:

1. Be completely deterministic, regardless of program environment or invocation.
2. Avoid depending on the ordering or side-effects of other `init()` functions.
3. Avoid accessing or manipulating global or environment state (machine info, env vars, working directory, program arguments).
4. Avoid I/O, including filesystem, network, and system calls.

Libraries intended to be used by other programs should take special care to be completely deterministic and not perform "init magic."

# Prerequisites

No strict prerequisites, though understanding Go's package initialization model and the relationship between `init()` and `main()` is helpful.

# Key Properties

1. **Implicit execution** -- `init()` runs automatically before `main()`, making its effects invisible at the call site.
2. **Non-deterministic ordering** -- While `init()` ordering is well-defined within a package, cross-package ordering depends on import order and can change as code evolves.
3. **Global state coupling** -- `init()` functions that modify global state create hidden dependencies between packages.
4. **Testing difficulty** -- Code initialized in `init()` cannot be easily overridden or controlled in tests.
5. **Acceptable exceptions** -- Complex expressions that cannot be single assignments, pluggable hooks (e.g., `database/sql` dialects, encoding registries), and deterministic precomputation (e.g., Google Cloud Functions optimizations).

# Construction / Recognition

## To Construct/Create:
1. Replace `init()` with explicit variable initialization using `var _x = value` or `var _x = helperFunc()`.
2. Move I/O and environment-dependent logic into named functions called from `main()`.
3. For testability, prefer constructor functions that return initialized values.

## To Identify/Recognize:
1. Look for `func init()` declarations, especially those performing I/O, reading environment variables, or modifying global state.
2. Check for `init()` functions that depend on ordering with other `init()` functions across packages.

# Context & Application

- **Typical contexts**: Package initialization, global variable setup, configuration loading.
- **Common applications**: Replacing `init()` with explicit helper functions or variable declarations for deterministic, testable initialization.

# Examples

**Example 1** (source: Uber Go Style Guide, Ch 2): Replace init() with direct variable initialization:

Bad:
```go
type Foo struct {
    // ...
}

var _defaultFoo Foo

func init() {
    _defaultFoo = Foo{
        // ...
    }
}
```

Good:
```go
var _defaultFoo = Foo{
    // ...
}

// or, better, for testability:

var _defaultFoo = defaultFoo()

func defaultFoo() Foo {
    return Foo{
        // ...
    }
}
```

**Example 2** (source: Uber Go Style Guide, Ch 2): Replace init() that performs I/O with an explicit function:

Bad:
```go
type Config struct {
    // ...
}

var _config Config

func init() {
    // Bad: based on current directory
    cwd, _ := os.Getwd()

    // Bad: I/O
    raw, _ := os.ReadFile(
        path.Join(cwd, "config", "config.yaml"),
    )

    yaml.Unmarshal(raw, &_config)
}
```

Good:
```go
type Config struct {
    // ...
}

func loadConfig() Config {
    cwd, err := os.Getwd()
    // handle err

    raw, err := os.ReadFile(
        path.Join(cwd, "config", "config.yaml"),
    )
    // handle err

    var config Config
    yaml.Unmarshal(raw, &config)

    return config
}
```

# Relationships

- **Related to** `exit-in-main`: Both guidelines push initialization and termination logic toward `main()` for clarity and testability. Avoiding `init()` means explicit setup in `main()`, while exit-in-main means only `main()` calls `os.Exit` or `log.Fatal`.
- **Related to** `dont-fire-and-forget-goroutines`: The guide explicitly states that `init()` functions should not spawn goroutines; background goroutines should be managed by objects with explicit lifecycle methods.

# Common Errors

1. **Using init() for configuration loading** -- Loading config files, reading environment variables, or performing I/O in `init()` makes the program non-deterministic and hard to test.
2. **Relying on init() ordering across packages** -- Code changes can alter import order, breaking assumptions about which `init()` runs first.
3. **Silently ignoring errors in init()** -- Since `init()` cannot return errors, developers often use `_` to discard errors, hiding failures.

# Common Confusions

1. **"init() is always bad"** vs. **"init() should be avoided where possible"** -- There are legitimate uses for `init()`, such as `database/sql` driver registration and `template.Must()` calls. The guidance is to prefer alternatives, not to ban `init()` entirely.
2. **Package-level var initialization vs. init()** -- Simple `var _x = expr` runs at package init time too, but is preferred because it is explicit, visible, and does not hide side effects.

# Source Reference

- Source: "Uber Go Style Guide"
- Chapter: "Guidelines" (Ch 2)
- Section: "Avoid init()"

# Verification Notes

- Extraction confidence: high -- This section is explicitly defined in the source with clear Bad/Good examples and detailed rationale.
