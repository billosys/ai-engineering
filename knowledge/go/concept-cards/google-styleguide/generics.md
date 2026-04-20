---
concept: Generics
slug: generics
category: language
subcategory: type-parameters
tier: advanced
source: "Google Go Style Guide"
source_slug: google-styleguide
authors: "Google Go Style Team"
chapter: "Style Decisions"
chapter_number: 3
pdf_page: null
section: "Generics"
extraction_confidence: high
aliases:
  - type parameters
  - generic functions
prerequisites:
  - go-interface-basics
  - interfaces-decisions
related:
  - interfaces-decisions
contrasts_with: []
answers_questions:
  - "When should generics be used in Go?"
  - "What are the pitfalls of premature generics use?"
  - "Should generics be used for error handling frameworks?"
---

# Quick Definition

Use generics (type parameters) only when they fulfill a real business requirement and reduce boilerplate. Prefer existing language features (slices, maps, interfaces) when they work well. Do not use generics to invent DSLs or error-handling frameworks. Start with a concrete type and generalize later.

# Core Definition

> "Generics (formally called 'Type Parameters') are allowed where they fulfill your business requirements. In many applications, a conventional approach using existing language features (slices, maps, interfaces, and so on) works just as well without the added complexity, so be wary of premature use." -- Google Go Style Guide, "Generics"

> "Do not use generics just because you are implementing an algorithm or data structure that does not care about the type of its member elements. If there is only one type being instantiated in practice, start by making your code work on that type without using generics at all." -- Google Go Style Guide, "Generics"

# Prerequisites

- Understanding of Go's type parameter syntax (Go 1.18+)
- Familiarity with Go interfaces as an alternative to generics
- Knowledge of the "least mechanism" principle

# Key Properties

1. **Real need required**: Do not use generics preemptively; conventional approaches often suffice.
2. **Start concrete**: If only one type is instantiated in practice, write concrete code first. Adding polymorphism later is easier than removing unnecessary abstraction.
3. **No DSLs**: Do not use generics to create domain-specific languages, especially error-handling frameworks.
4. **No assertion libraries**: In testing, avoid generic assertion frameworks that produce less useful test failures.
5. **Interfaces first**: If several types share a useful unifying interface, consider modeling with interfaces instead of generics.
6. **`any` is a smell**: If you find yourself relying on the `any` type with excessive type switching, generics may be appropriate.
7. **Document generics APIs**: Exported generic APIs need thorough documentation and motivating runnable examples.

# Construction / Recognition

**Appropriate use -- multiple types genuinely needed:**

```go
func Map[T, U any](s []T, f func(T) U) []U {
    result := make([]U, len(s))
    for i, v := range s {
        result[i] = f(v)
    }
    return result
}
```

**Premature use -- only one type instantiated:**

```go
// Bad: only ever called with []int in practice
func Sum[T constraints.Integer](s []T) T { ... }

// Better: start concrete
func SumInts(s []int) int { ... }
```

# Context & Application

Go added type parameters in 1.18, but the style guide counsels restraint. The "least mechanism" principle from the core guide applies: use the simplest tool that solves the problem. Generics add cognitive overhead for readers who must understand type constraints. In testing, generic assertion libraries obscure failure messages and make debugging harder. The recommended approach is to write concrete code, discover patterns across multiple concrete implementations, and only then extract a generic version.

# Examples

See Construction / Recognition above for illustrative examples.

# Relationships

- **interfaces-decisions**: Interfaces are often the simpler alternative to generics when types share a common behavior.

# Common Errors

1. Adding type parameters when only one concrete type is ever used.
2. Building generic error-handling or assertion frameworks.
3. Using `any` type with type switches instead of proper constraints.
4. Failing to document generic exported APIs.

# Common Confusions

- **Generics vs. interfaces**: Interfaces model shared behavior; generics model shared algorithms over varying types. If the problem is "I need to call method X on different types," use an interface.
- **"Write code, don't design types"**: Robert Griesemer and Ian Lance Taylor's advice -- focus on solving the problem, not on creating elaborate type hierarchies.

# Source Reference

Google Go Style Guide, "Style Decisions" chapter, "Generics" section. References "Write code, don't design types" (GopherCon talk), "Using Generics in Go" (Ian Lance Taylor).

# Verification Notes

Confidence: high. All guidance is directly from the source text.
