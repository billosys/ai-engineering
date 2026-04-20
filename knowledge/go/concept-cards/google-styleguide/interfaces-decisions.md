---
concept: Interfaces
slug: interfaces-decisions
category: api-design
subcategory: interface-design
tier: intermediate
source: "Google Go Style Guide"
source_slug: google-styleguide
authors: "Google Go Style Team"
chapter: "Style Decisions"
chapter_number: 3
pdf_page: null
section: "Interfaces"
extraction_confidence: high
aliases:
  - accept interfaces return concrete
  - interface design
prerequisites:
  - go-interface-basics
related:
  - generics
  - receiver-type
contrasts_with: []
answers_questions:
  - "When should Go interfaces be created?"
  - "Should Go functions accept interfaces or concrete types?"
  - "Should Go functions return interfaces or concrete types?"
  - "Who should define the interface -- the producer or consumer?"
---

# Quick Definition

Avoid creating interfaces until a real need exists. Consumers of an interface should define it, including only the methods they use. Functions should accept interfaces but return concrete types. Do not export interfaces before a real consumer exists. Keep interfaces small for easier implementation and composition.

# Core Definition

> "Avoid creating interfaces until a real need exists. Focus on the required behavior rather than just abstract named patterns like 'service' or 'repository' and the like." -- Google Go Style Guide, "Interfaces"

> "There is an adage: Functions should take interfaces as arguments but return concrete types." -- Google Go Style Guide, "Interfaces" (citing GoTip #49)

> "The consumer of the interface should define it (not the package implementing the interface), ensuring it includes only the methods they actually use." -- Google Go Style Guide, "Interfaces"

# Prerequisites

- Understanding of Go interfaces and implicit satisfaction
- Familiarity with Go package design

# Key Properties

1. **No premature abstraction**: Do not create interfaces for "service" or "repository" patterns without real consumers.
2. **Consumer defines the interface**: The package that uses the interface should define it, including only methods it actually calls.
3. **Accept interfaces, return concrete**: Functions take interface parameters but return concrete types, giving callers access to all public methods.
4. **Small interfaces**: Design interfaces to be minimal for easier implementation and composition.
5. **No test-only interfaces**: Do not export interfaces or test doubles solely for testing; test via the public API.
6. **No wrapping RPC clients**: Do not create manual interfaces around RPC clients just for abstraction.
7. **Returning interfaces is sometimes okay**: Acceptable for encapsulation (e.g., `error` interface) and certain patterns (command, chaining, factory, strategy).

# Construction / Recognition

**Good pattern -- consumer defines the interface:**

```go
// In the consumer package:
type Storage interface {
    Get(key string) ([]byte, error)
}

func NewService(s Storage) *Service { ... }
```

**Good pattern -- return concrete type:**

```go
func NewClient(addr string) *Client { ... }
```

**Bad -- premature interface without real consumer:**

```go
// Don't define and export this before someone needs it
type Repository interface {
    Find(id string) (*Entity, error)
    Save(e *Entity) error
    Delete(id string) error
}
```

# Context & Application

Go's implicit interface satisfaction means that producers do not need to declare which interfaces their types implement. This enables the consumer-side interface pattern: the consumer defines exactly the subset of methods it needs, and any concrete type that happens to have those methods satisfies the interface. This prevents interface bloat and keeps coupling minimal. Returning concrete types preserves the full API surface for callers while still allowing them to pass the result into functions that accept interfaces.

# Examples

See Construction / Recognition above for the complete set of source examples.

# Relationships

- **generics**: Interfaces and generics are alternative approaches to polymorphism; prefer interfaces when they model the solution naturally.
- **receiver-type**: Method sets on pointer vs. value receivers affect which interfaces a type satisfies.

# Common Errors

1. Creating interfaces before any consumer exists.
2. Having the producer package export the interface instead of the consumer defining it.
3. Including too many methods in an interface.
4. Returning an interface type when a concrete type would give callers more flexibility.
5. Creating test doubles via exported interfaces instead of testing the real implementation.

# Common Confusions

- **Producer-exported interfaces**: The producer may export the interface when the interface is the product itself (a common protocol), to prevent redefinition bloat.
- **When to return interfaces**: Returning `error` is fine because it is a common protocol interface. Strategy and factory patterns may also warrant interface returns.

# Source Reference

Google Go Style Guide, "Style Decisions" chapter, "Interfaces" section. References GoTip #49 and GoTip #78.

# Verification Notes

Confidence: high. All guidance is directly from the source text.
