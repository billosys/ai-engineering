---
# === CORE IDENTIFICATION ===
concept: Predefined Types
slug: predefined-types

# === CLASSIFICATION ===
category: data-types
subcategory: type-primitives
tier: foundational

# === PROVENANCE ===
source: "Erlang Reference Manual"
source_slug: otp-reference-manual
authors: "Ericsson AB"
chapter: "Types and Function Specifications"
chapter_number: null
pdf_page: null
section: "Types and their Syntax"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "built-in types"
  - "primitive types"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - erlang-type-language
extends: []
related:
  - type-union
  - built-in-type-aliases
  - type-lattice
  - singleton-types
contrasts_with:
  - type-declaration

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What must I know before writing type specifications?"
---

# Quick Definition
Predefined types are the built-in type constructors that represent typically infinite sets of Erlang terms, such as `integer()`, `atom()`, `pid()`, `float()`, `list()`, `tuple()`, and `map()`.

# Core Definition
"Types consist of, and are built from, a set of predefined types, for example, `integer()`, `atom()`, and `pid()`. Predefined types represent a typically infinite set of Erlang terms that belong to this type. For example, the type `atom()` denotes the set of all Erlang atoms" (Erlang Reference Manual, "Types and their Syntax"). The predefined types form the atomic building blocks from which all other types are constructed via unions and type declarations.

# Prerequisites
- **erlang-type-language** -- Predefined types are the primitive elements of the type language

# Key Properties
1. Core predefined types: `any()`, `none()`, `dynamic()`, `pid()`, `port()`, `reference()`, `atom()`, `float()`, `integer()`, `list()`, `tuple()`, `map()`, `fun()`
2. `[]` (nil) is a predefined singleton type for the empty list
3. Integer types support singleton values, ranges (`Integer..Integer`), and expressions
4. Atom types support singleton atom values (e.g., `'foo'`)
5. Bitstring types use the syntax `<<>>`, `<<_:M>>`, `<<_:_*N>>`, `<<_:M, _:_*N>>`
6. Function types: `fun()`, `fun((...) -> Type)`, `fun(() -> Type)`, `fun((TList) -> Type)`
7. Map types: `#{}` (empty map), `#{AssociationList}` with mandatory (`:=`) and optional (`=>`) associations
8. Tuple types: `tuple()` (any size), `{}`, `{TList}`
9. Starting from OTP 26, it is permitted to define a type with the same name as a built-in type (with a warning)

# Construction / Recognition
## To Construct:
1. Write the type name followed by parentheses, e.g., `integer()`
2. For parameterized types, pass type arguments, e.g., `list(integer())`
3. For singleton types, use the literal value, e.g., `'ok'` or `42`
4. For ranges, use `Lower..Upper`, e.g., `1..100`

## To Identify/Recognize:
1. Predefined types use the `name()` syntax
2. They appear without any `-type` declaration in the module
3. They represent fundamental Erlang data categories

# Context & Application
Predefined types are the vocabulary of Erlang's type system. Every `-spec` and `-type` declaration ultimately bottoms out in predefined types. Understanding them is essential before writing any type annotations.

# Examples
**Example 1** (Types and their Syntax):
The full type syntax grammar shows how predefined types are the leaves:
```text
Type :: any() | none() | dynamic() | pid() | port() | reference()
      | [] | Atom | Bitstring | float() | Fun | Integer | List | Map | Tuple | Union | UserDefined
```

**Example 2** (Types and their Syntax):
List shorthands:
```text
[T]       %% shorthand for list(T)
[T,...]   %% shorthand for nonempty_list(T)
[]        %% singleton type for empty list (NOT list/0)
[_]       %% shorthand for list/0 (list of unknown type)
```

# Relationships
## Builds Upon
- **erlang-type-language** -- Predefined types are the atoms of the type language

## Enables
- **type-union** -- Unions compose predefined types
- **type-declaration** -- User-defined types are built from predefined types
- **function-specification** -- Specs reference predefined types
- **built-in-type-aliases** -- Convenience aliases for common predefined type combinations

## Related
- **singleton-types** -- Atoms and integers can be singleton types
- **type-lattice** -- Predefined types have positions in the subtype lattice

## Contrasts With
- **type-declaration** -- User-defined types vs. built-in predefined types

# Common Errors
- **Error**: Using `[]` to mean "list of any type"
  **Correction**: `[]` is the singleton empty list type. Use `[_]` or `[any()]` for list of unknown element type

- **Error**: Using `#{}` to mean "any map"
  **Correction**: `#{}` is the singleton empty map type. Use `map()` (equivalent to `#{any() => any()}`) for any map

# Common Confusions
- **Confusion**: Thinking `list()` and `[]` are the same type
  **Clarification**: `list()` is `[any()]` (proper list of any elements), while `[]` is only the empty list

# Source Reference
"Types and Function Specifications" chapter, section "Types and their Syntax," including the predefined types grammar and built-in types tables.

# Verification Notes
- Definition source: Direct from source text and grammar specification
- Confidence rationale: High -- explicit grammar and definitions
- Uncertainties: None
- Cross-reference status: All slugs verified against planned cards
