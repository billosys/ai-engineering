---
# === CORE IDENTIFICATION ===
concept: Option Structure
slug: option-structure

# === CLASSIFICATION ===
category: api-design
subcategory: function-arguments
tier: intermediate

# === PROVENANCE ===
source: "Google Go Style Guide"
source_slug: google-styleguide
authors: "Google Go Style Team"
chapter: "Best Practices"
chapter_number: 4
pdf_page: null
section: "Option structure"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "option struct"
  - "options pattern"
  - "configuration struct"

# === TYPED RELATIONSHIPS ===
prerequisites: []
extends: []
related:
  - variadic-options-bp
contrasts_with:
  - variadic-options-bp

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "When should I use an option struct instead of many function parameters?"
  - "What are the benefits of option structs?"
  - "Should contexts be included in option structs?"
---

# Quick Definition

Use an option struct to collect many optional parameters into a single struct argument. Fields are self-documenting, irrelevant fields can be omitted (using zero-value defaults), and the struct can grow without breaking call sites. Never include `context.Context` in an option struct.

# Core Definition

An option structure is a struct that collects some or all arguments of a function, passed as the last argument. The struct should be exported only if used in an exported function. Benefits include: struct literal fields are self-documenting and harder to swap, irrelevant fields can be omitted (zero values act as defaults), callers can share and compose option structs, fields have cleaner per-field documentation than function arguments, and the struct can grow over time without impacting call sites. This pattern is preferred when all callers need to specify one or more options, many callers provide many options, or options are shared between multiple functions. Contexts are never included in option structs.

# Prerequisites

(none)

# Key Properties

1. Struct fields are self-documenting with names and values
2. Zero values serve as defaults -- irrelevant fields can be omitted
3. Callers can share and compose option structs
4. Per-field documentation is cleaner than function argument documentation
5. The struct can grow over time without breaking call sites
6. Context must not be included -- it remains a separate parameter

# Construction / Recognition

## To Apply:
1. Identify functions with many parameters, especially optional ones
2. Create a struct with fields for each option
3. Pass as the last parameter after required params (like context)
4. Export the struct only if the function is exported
5. Design zero values as sensible defaults

## To Recognize:
1. Function signatures like `func Foo(ctx context.Context, opts FooOptions)`
2. Call sites using struct literals with named fields
3. Some fields omitted in simpler call sites

# Context & Application

Option structs are the simpler of two patterns for managing many parameters (the other being variadic options). Choose option structs when most callers need to specify options and the options are relatively straightforward. The primary consideration is how the call site looks across all expected use cases.

# Examples

**Example 1 -- Bad: too many parameters**:

```go
// Bad:
func EnableReplication(ctx context.Context, config *replicator.Config, primaryRegions, readonlyRegions []string, replicateExisting, overwritePolicies bool, replicationInterval time.Duration, copyWorkers int, healthWatcher health.Watcher) {
```

**Example 2 -- Good: option struct**:

```go
// Good:
type ReplicationOptions struct {
    Config              *replicator.Config
    PrimaryRegions      []string
    ReadonlyRegions     []string
    ReplicateExisting   bool
    OverwritePolicies   bool
    ReplicationInterval time.Duration
    CopyWorkers         int
    HealthWatcher       health.Watcher
}

func EnableReplication(ctx context.Context, opts ReplicationOptions) {
    // ...
}
```

**Example 3 -- Call sites**:

```go
// Complex call:
storage.EnableReplication(ctx, storage.ReplicationOptions{
    Config:              config,
    PrimaryRegions:      []string{"us-east1", "us-central2", "us-west3"},
    ReadonlyRegions:     []string{"us-east5", "us-central6"},
    OverwritePolicies:   true,
    ReplicationInterval: 1 * time.Hour,
    CopyWorkers:         100,
    HealthWatcher:       watcher,
})

// Simple call (zero-value defaults):
storage.EnableReplication(ctx, storage.ReplicationOptions{
    Config:         config,
    PrimaryRegions: []string{"us-east1", "us-central2", "us-west3"},
})
```

# Relationships

## Related
- **variadic-options-bp** -- Alternative pattern for extensible APIs with many rarely-used options

## Contrasts With
- **variadic-options-bp** -- Option structs are simpler; variadic options are more flexible but require more code

# Common Errors

- **Error**: Including context.Context in the option struct
  **Correction**: Context is always a separate parameter, never part of an option struct

- **Error**: Using option structs when most callers use default values
  **Correction**: If most callers don't need options, variadic options may be more appropriate

# Common Confusions

- **Confusion**: Thinking option structs should always be exported
  **Clarification**: Export only if the function is exported; keep unexported for internal APIs

- **Confusion**: Not realizing zero values of the struct fields serve as defaults
  **Clarification**: Design fields so that zero values are sensible defaults

# Source Reference

Chapter 4: Best Practices, Section "Function argument lists" > "Option structure".

# Verification Notes

- Definition source: Directly from "Option structure" section of Best Practices
- Confidence rationale: HIGH -- detailed examples with good/bad patterns
- Uncertainties: None
- Cross-reference status: References decisions#contexts
