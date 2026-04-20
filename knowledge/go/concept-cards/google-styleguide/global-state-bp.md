---
# === CORE IDENTIFICATION ===
concept: Global State (Best Practices)
slug: global-state-bp

# === CLASSIFICATION ===
category: global-state
subcategory: dependency-management
tier: advanced

# === PROVENANCE ===
source: "Google Go Style Guide"
source_slug: google-styleguide
authors: "Google Go Style Team"
chapter: "Best Practices"
chapter_number: 4
pdf_page: null
section: "Global state"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "package-level state"
  - "dependency injection"
  - "mutable globals"
  - "avoiding global state"

# === TYPED RELATIONSHIPS ===
prerequisites: []
extends: []
related:
  - package-size
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "Why should Go libraries avoid global mutable state?"
  - "What are the major forms of problematic global state?"
  - "When is global state acceptable?"
  - "How do I provide a default instance without forcing global state?"
---

# Quick Definition

Libraries should not force clients to use global mutable state. Instead, allow clients to create and use instance values, passing dependencies explicitly. Global state breaks test hermeticity, prevents parallel execution, and creates ordering dependencies. Limited global state is acceptable when the state is logically constant, behavior is stateless, or there is no expectation of predictable behavior.

# Core Definition

Libraries should not expose APIs that rely on package-level mutable state. Instead, allow clients to create instance values and pass them as explicit dependencies. Global state causes problems: tests interfere with each other through shared state, parallel test execution breaks, ordering dependencies emerge (e.g., must call `Register` before flags are parsed), and different clients cannot maintain independent instances. Problematic forms include: top-level mutable variables, service locator patterns, callback registries, and thick-client singletons. Global state is safe only when: the state is logically constant, behavior is stateless (caches where hits are indistinguishable from misses), state does not bleed externally, or there is no expectation of predictable behavior (e.g., `math/rand`). If convenience requires a default instance, provide it as a thin proxy over the instance-based API, restrict its use to binary targets (not libraries), document invariants, and provide reset mechanisms for testing.

# Prerequisites

(none)

# Key Properties

1. Libraries must not force global mutable state on clients
2. Allow clients to create isolated instances and pass dependencies explicitly
3. Problematic forms: mutable top-level vars, service locators, callback registries, singletons
4. Global state breaks test hermeticity, parallel execution, and creates ordering bugs
5. Safe when: logically constant, stateless, no external bleed, no predictability expectation
6. Default instances must be thin proxies over instance APIs, restricted to binary targets

# Construction / Recognition

## To Apply:
1. Create types that encapsulate state: `type Registry struct { ... }`
2. Provide constructors: `func New() *Registry { ... }`
3. Pass dependencies explicitly through constructors, function params, or struct fields
4. If a default instance is needed, make it a thin proxy over the real API

## To Recognize:
1. Package types with constructors, no package-level mutable variables
2. Dependencies passed via function parameters or struct fields
3. Tests that can run in isolation without shared state

# Context & Application

This is one of the longest and most detailed sections in Best Practices. Global state has cascading effects on codebase health. The section provides litmus tests: if multiple independent functions interact through global state, if tests interfere, if users are tempted to swap state for testing, or if special ordering is required -- the API is unsafe. Standard library examples like `image.RegisterFormat` pass the litmus tests because decoders are stateless, idempotent, and pure. Legacy APIs that use global state should not be used as precedent.

# Examples

**Example 1 -- Good: instance-based API**:

```go
// Good:
package sidecar

type Registry struct { plugins map[string]*Plugin }

func New() *Registry { return &Registry{plugins: make(map[string]*Plugin)} }

func (r *Registry) Register(name string, p *Plugin) error { ... }
```

```go
// Good:
func main() {
    sidecars := sidecar.New()
    if err := sidecars.Register("Cloud Logger", cloudlogger.New()); err != nil {
        log.Exitf("Could not setup cloud logger: %v", err)
    }
    cfg := &myapp.Config{Sidecars: sidecars}
    myapp.Run(context.Background(), cfg)
}
```

**Example 2 -- Bad: global state causing test interference**:

```go
// Bad:
package sidecar

var registry = make(map[string]*Plugin)

func Register(name string, p *Plugin) error { /* registers in global registry */ }
```

Tests that call `Register` pollute state for subsequent tests.

# Relationships

## Related
- **package-size** -- Proper package structure reduces temptation for global state

## Contrasts With
(none)

# Common Errors

- **Error**: Using package-level mutable variables as the primary API
  **Correction**: Provide instance-based APIs with explicit dependency passing

- **Error**: Using a singleton pattern for backend clients
  **Correction**: Allow clients to create their own instances

# Common Confusions

- **Confusion**: Thinking all package-level variables are bad
  **Clarification**: Logically constant values (like registered decoders) are acceptable when they pass litmus tests

- **Confusion**: Following legacy standard library patterns that use global state
  **Clarification**: Legacy patterns should not be used as precedent; invest in proper API design

# Source Reference

Chapter 4: Best Practices, Section "Global state" (including "Major forms", "Litmus tests", and "Providing a default instance" subsections).

# Verification Notes

- Definition source: Synthesized from entire "Global state" section with all subsections
- Confidence rationale: HIGH -- extensive guidance with examples and litmus tests
- Uncertainties: None
- Cross-reference status: References GoTip #5, #24, #36, #40, #41, #44, #71, #80
