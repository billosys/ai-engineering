---
concept: Avoid Embedding Types in Public Structs
slug: avoid-embedding-types-in-public-structs
category: code-safety
subcategory: type-design
tier: intermediate
source: "Uber Go Style Guide"
source_slug: uber-style
authors: "Prashant Varanasi, Simon Newton"
chapter: "Guidelines"
chapter_number: 2
pdf_page: null
section: "Avoid Embedding Types in Public Structs"
extraction_confidence: high
aliases:
  - no type embedding in public structs
  - composition over embedding
prerequisites:
  - go-structs
  - go-interfaces
related:
  - avoid-using-built-in-names
contrasts_with: []
answers_questions:
  - "What distinguishes embedding from composition via fields?"
  - "Why is type embedding problematic in public structs?"
---

# Quick Definition

Do not embed types in public structs. Embedding leaks implementation details, creates implicit public API surface, and inhibits type evolution. Instead, store the inner type as an unexported field and write explicit delegate methods.

# Core Definition

> "These embedded types leak implementation details, inhibit type evolution, and obscure documentation." -- Uber Go Style Guide, "Avoid Embedding Types in Public Structs"

> "An embedded type is rarely necessary. It is a convenience that helps you avoid writing tedious delegate methods." -- Uber Go Style Guide, "Avoid Embedding Types in Public Structs"

The guide identifies four breaking-change risks from embedding:

- Adding methods to an embedded interface is a breaking change.
- Removing methods from an embedded struct is a breaking change.
- Removing the embedded type is a breaking change.
- Replacing the embedded type, even with one satisfying the same interface, is a breaking change.

# Prerequisites

- Understanding of Go struct embedding vs named fields
- Knowledge of Go's method promotion mechanism
- Familiarity with Go's approach to backward compatibility

# Key Properties

1. **Embedding promotes methods**: All methods of the embedded type become methods of the outer type, expanding the public API implicitly.
2. **Embedding creates a named field**: The embedded type becomes a field accessible by its type name, which is public if the type is public.
3. **Breaking change constraints**: Any change to the embedded type or the embedding relationship can break callers.
4. **Applies to both struct and interface embedding**: Embedding an interface in a struct has similar problems -- it leaks the abstract implementation detail.

# Construction / Recognition

**Bad -- struct embedding:**

```go
// ConcreteList is a list of entities.
type ConcreteList struct {
  *AbstractList
}
```

**Good -- composition via field with delegate methods:**

```go
// ConcreteList is a list of entities.
type ConcreteList struct {
  list *AbstractList
}

// Add adds an entity to the list.
func (l *ConcreteList) Add(e Entity) {
  l.list.Add(e)
}

// Remove removes an entity from the list.
func (l *ConcreteList) Remove(e Entity) {
  l.list.Remove(e)
}
```

**Bad -- interface embedding:**

```go
// ConcreteList is a list of entities.
type ConcreteList struct {
  AbstractList
}
```

**Good -- interface stored as field:**

```go
// ConcreteList is a list of entities.
type ConcreteList struct {
  list AbstractList
}

// Add adds an entity to the list.
func (l *ConcreteList) Add(e Entity) {
  l.list.Add(e)
}

// Remove removes an entity from the list.
func (l *ConcreteList) Remove(e Entity) {
  l.list.Remove(e)
}
```

# Context & Application

Go uses embedding as a compromise between inheritance and composition. While convenient, it creates tight coupling between the outer and inner types. In public structs, this coupling becomes part of the API contract. The delegate method approach is more verbose but provides full control over which methods are exposed and allows the internal implementation to change without breaking callers.

# Examples

See Construction / Recognition above for the source examples covering both struct and interface embedding scenarios.

# Relationships

- **avoid-using-built-in-names**: Both address accidental API surface concerns, though in different dimensions.

# Common Errors

1. Embedding `sync.Mutex` in a public struct, which exposes `Lock()` and `Unlock()` as public API (this is specifically called out in the "Zero-value Mutexes" section of the same chapter).
2. Embedding an interface to avoid writing delegate methods, then discovering that adding methods to the interface breaks all implementors.
3. Assuming embedding is equivalent to inheritance -- it is not; it is mechanical method promotion without polymorphism.

# Common Confusions

- **Embedding vs composition**: Embedding (`AbstractList` as a field name matching the type) promotes methods automatically. Composition via a named field (`list AbstractList`) requires explicit delegate methods. The guide recommends composition.
- **Unexported structs**: The guidance focuses on *public* structs. For unexported structs, the risk of breaking external callers does not apply, though embedding may still obscure documentation.

# Source Reference

Uber Go Style Guide, "Guidelines" chapter, "Avoid Embedding Types in Public Structs" section.

# Verification Notes

Confidence: high. The guidance, the four breaking-change rules, and both struct/interface embedding examples are directly from the source with explicit bad/good comparisons.
