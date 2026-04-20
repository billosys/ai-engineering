---
concept: Type Aliases
slug: type-aliases
category: language
subcategory: type-system
tier: intermediate
source: "Google Go Style Guide"
source_slug: google-styleguide
authors: "Google Go Style Team"
chapter: "Style Decisions"
chapter_number: 3
pdf_page: null
section: "Type aliases"
extraction_confidence: high
aliases:
  - type alias vs type definition
  - type migration
prerequisites:
  - go-type-basics
related:
  - interfaces-decisions
contrasts_with: []
answers_questions:
  - "What is the difference between a type definition and a type alias in Go?"
  - "When should type aliases be used in Go?"
  - "Are type aliases common in Go?"
---

# Quick Definition

Use a type definition (`type T1 T2`) to create a new distinct type. Use a type alias (`type T1 = T2`) only to refer to an existing type without creating a new one, primarily for migrating packages to new source code locations. Type aliases are rare and should not be used when a type definition would be appropriate.

# Core Definition

> "Use a *type definition*, `type T1 T2`, to define a new type. Use a *type alias*, `type T1 = T2`, to refer to an existing type without defining a new type. Type aliases are rare; their primary use is to aid migrating packages to new source code locations. Don't use type aliasing when it is not needed." -- Google Go Style Guide, "Type aliases"

# Prerequisites

- Understanding of Go's type system
- Knowledge of the difference between `type T1 T2` (definition) and `type T1 = T2` (alias)

# Key Properties

1. **Type definition creates a new type**: `type T1 T2` creates a distinct type `T1` that is not interchangeable with `T2`.
2. **Type alias is the same type**: `type T1 = T2` makes `T1` and `T2` identical; they are interchangeable.
3. **Aliases are rare**: The primary legitimate use is package migration.
4. **Prefer type definitions**: For API boundaries, create new types with definitions to get distinct method sets and type safety.

# Construction / Recognition

**Type definition -- new distinct type:**

```go
type UserID string  // UserID is a new type, not interchangeable with string
```

**Type alias -- same type, different name (for migration):**

```go
type UserID = string  // UserID IS string; used during migration
```

**Migration pattern:**

```go
// old package
package old

type Config struct { ... }

// new package (during migration)
package new

import "old"

type Config = old.Config  // alias allows gradual migration
```

# Context & Application

Type aliases were introduced in Go 1.9 specifically for the use case of gradual code migration, where a type needs to move from one package to another without breaking all consumers at once. During the migration, the alias in the old package points to the new location, and consumers can be updated incrementally. Outside of migration scenarios, type definitions are almost always the correct choice because they provide type safety at API boundaries.

# Examples

See Construction / Recognition above for illustrative examples.

# Relationships

- **interfaces-decisions**: Type definitions create new types with their own method sets, relevant to interface satisfaction.

# Common Errors

1. Using a type alias when a type definition is needed for type safety.
2. Using type aliases for convenience instead of defining proper types at API boundaries.
3. Confusing `type T1 T2` (new type) with `type T1 = T2` (alias).

# Common Confusions

- **Definition vs. alias syntax**: The `=` sign is the only syntactic difference. `type T1 T2` defines a new type; `type T1 = T2` creates an alias.
- **Method sets**: A type definition starts with an empty method set. A type alias inherits all methods of the underlying type.

# Source Reference

Google Go Style Guide, "Style Decisions" chapter, "Type aliases" section.

# Verification Notes

Confidence: high. All guidance is directly from the source text.
