---
# === CORE IDENTIFICATION ===
concept: Effective Interfaces
slug: effective-interfaces

# === CLASSIFICATION ===
category: api-design
subcategory: interfaces
tier: advanced

# === PROVENANCE ===
source: "Google Go Style Guide"
source_slug: google-styleguide
authors: "Google Go Style Team"
chapter: "Best Practices"
chapter_number: 4
pdf_page: null
section: "Interfaces"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "interface design"
  - "accept interfaces return concrete"
  - "interface ownership"

# === TYPED RELATIONSHIPS ===
prerequisites: []
extends:
  - interfaces
related:
  - package-size
  - documentation-conventions
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "When should I create an interface in Go?"
  - "Should the producer or consumer define the interface?"
  - "When should I return an interface instead of a concrete type?"
  - "How do I avoid unnecessary interfaces?"
---

# Quick Definition

Do not create interfaces before a real need exists. The consumer typically defines the interface (not the producer). Accept interfaces, return concrete types. Return interfaces only for encapsulation, runtime polymorphism (factory/strategy patterns), or breaking circular dependencies. Keep interfaces small. Do not export interfaces only for testing.

# Core Definition

Go interfaces are satisfied implicitly, making them a structural tool rather than a declarative one. The most common mistake is creating an interface before a real need exists. Do not create an interface just because you are designing a "service" or "repository" -- focus on behavior and concrete implementation first. Reuse existing interfaces (especially generated ones like RPC clients). Do not export test double interfaces that only exist for testing. Create interfaces when: there are multiple implementations that must be handled by the same logic, you need to decouple packages (break circular dependencies), or when hiding a massive API surface behind a focused subset. The consumer should define the interface (in the package that uses it), defining only the methods it actually uses. Exceptions where the producer defines the interface include: when the interface is the product (like `io.Writer` or protobuf generated interfaces), to prevent interface bloat across many packages, and to resolve circular dependencies. Accept interfaces, return concrete types -- except for encapsulation (like returning `io.Reader` to hide a `ThrottledReader`'s `Refill` method), factory/strategy patterns, and breaking import cycles. Keep interfaces small: the bigger the interface, the weaker the abstraction.

# Prerequisites

(none)

# Key Properties

1. Do not create interfaces before a real need exists
2. Consumer defines the interface; producer exceptions: protocol interfaces, bloat prevention, cycle breaking
3. Accept interfaces, return concrete types as the default
4. Return interfaces for: encapsulation, runtime polymorphism, breaking circular dependencies
5. Keep interfaces small -- the bigger the interface, the weaker the abstraction
6. Do not export interfaces only for testing -- design APIs testable via public API
7. Unexported interfaces for internal use only -- exporting commits to maintenance

# Construction / Recognition

## To Apply:
1. Start with concrete types; add interfaces only when a second implementation appears
2. Define interfaces in the consumer package with only the methods needed
3. Return concrete types from constructors unless encapsulation or polymorphism is needed
4. Keep interfaces to one or two methods when possible
5. Document interfaces proportionally to their cognitive load

## To Recognize:
1. Small, focused interfaces in consumer packages
2. Concrete return types from constructors
3. Interfaces introduced to solve specific problems (multiple implementations, decoupling)

# Context & Application

This section synthesizes Go's interface philosophy: implicit satisfaction enables consumers to define interfaces without coordination with producers. The standard library exemplifies this: `database/sql` exports a concrete `DB` type rather than an interface, and consumers define their own interfaces for the methods they use. When returning interfaces for encapsulation, ask whether exposing the concrete type would actually break system integrity or limit maintainability. Introducing interfaces to break dependency cycles is often a signal of improperly structured packages -- consider consolidating packages first.

# Examples

**Example 1 -- Return interface for encapsulation**:

```go
// Good:
type ThrottledReader struct {
    source  io.Reader
    limit   int
    balance int
}

func (t *ThrottledReader) Read(p []byte) (int, error) { ... }
func (t *ThrottledReader) Refill(amount int) { ... } // internal use only

func New(r io.Reader, bytesPerSec int) io.Reader {
    return &ThrottledReader{...} // hides Refill from callers
}
```

**Example 2 -- Breaking circular dependencies**:

```go
// package plugin -- returns interface to avoid importing package app
type Configurer interface {
    APIKey() string
}

func New() Configurer {
    return &localConfig{key: "secret"}
}
```

**Example 3 -- Factory pattern returning interface**:

```go
// Good:
func NewWriter(format string) io.Writer {
    switch format {
    case "json":
        return &jsonWriter{}
    case "xml":
        return &xmlWriter{}
    default:
        return &textWriter{}
    }
}
```

# Relationships

## Related
- **package-size** -- Improper package structure can force unnecessary interfaces
- **documentation-conventions** -- Interfaces require thorough documentation proportional to cognitive load
- **interfaces** -- The Decisions chapter summary on interfaces

## Contrasts With
(none)

# Common Errors

- **Error**: Creating an interface before having two concrete implementations
  **Correction**: Start with concrete types; add an interface when a real second use case appears

- **Error**: Exporting an interface solely for test mocking
  **Correction**: Design APIs testable via public API; use test doubles from test helper packages

# Common Confusions

- **Confusion**: Thinking the producer should always define the interface
  **Clarification**: In Go, the consumer typically defines the interface; producer-defined interfaces are for protocols and contracts

- **Confusion**: Always returning concrete types without exception
  **Clarification**: Return interfaces for encapsulation, polymorphism, and breaking import cycles

- **Confusion**: Thinking introducing interfaces to break cycles is always correct
  **Clarification**: It is often a signal of improperly structured packages; consider consolidation first

# Source Reference

Chapter 4: Best Practices, Section "Interfaces" (including "Avoid unnecessary interfaces", "Interface ownership and visibility", and "Designing effective interfaces" subsections).

# Verification Notes

- Definition source: Synthesized from all three interface subsections in Best Practices
- Confidence rationale: HIGH -- extensive guidance with detailed examples
- Uncertainties: None
- Cross-reference status: References decisions#interfaces, GoTip #49, GoTip #78, Go proverbs
