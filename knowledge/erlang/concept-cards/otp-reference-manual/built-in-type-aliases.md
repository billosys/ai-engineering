---
# === CORE IDENTIFICATION ===
concept: Built-in Type Aliases
slug: built-in-type-aliases

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
  - "predefined aliases"
  - "convenience types"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - predefined-types
  - type-union
extends:
  - predefined-types
related:
  - erlang-type-language
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What must I know before writing type specifications?"
---

# Quick Definition
Built-in type aliases are convenience names for common type unions, such as `term()` for `any()`, `boolean()` for `'false' | 'true'`, `number()` for `integer() | float()`, and `string()` for `[char()]`.

# Core Definition
"For convenience, the following types are also built-in. They can be thought of as predefined aliases for the type unions also shown in the table" (Erlang Reference Manual, "Types and their Syntax"). These aliases provide readable, memorable names for frequently used type combinations. Additional types like `non_neg_integer()`, `pos_integer()`, and `neg_integer()` exist but their definitions are not expressible in the standard type syntax.

# Prerequisites
- **predefined-types** -- Aliases are defined in terms of predefined types
- **type-union** -- Most aliases are unions of predefined types

# Key Properties
1. `term()` = `any()` -- the top type
2. `binary()` = `<<_:_*8>>` -- byte-aligned bitstring
3. `boolean()` = `'false' | 'true'`
4. `byte()` = `0..255`
5. `char()` = `0..16#10ffff`
6. `number()` = `integer() | float()`
7. `string()` = `[char()]` -- list of characters
8. `iodata()` = `iolist() | binary()`
9. `timeout()` = `'infinity' | non_neg_integer()`
10. `no_return()` = `none()` -- for functions that never return
11. `module()` = `atom()`
12. `mfa()` = `{module(), atom(), arity()}`
13. `arity()` = `0..255`
14. `identifier()` = `pid() | port() | reference()`
15. `non_neg_integer()` = `0..`, `pos_integer()` = `1..`, `neg_integer()` = `..-1`

# Construction / Recognition
## To Use:
1. Write the alias name followed by parentheses: `string()`, `boolean()`, etc.
2. Use them anywhere a type expression is expected
3. They are interchangeable with their expanded definitions

## To Identify/Recognize:
1. They appear in the built-in types table in the reference manual
2. They do not require a `-type` declaration

# Context & Application
These aliases make type specifications more readable and idiomatic. Using `string()` instead of `[char()]` or `boolean()` instead of `'false' | 'true'` communicates intent more clearly. They are used pervasively in OTP and application code.

# Examples
**Example 1** (Types and their Syntax, built-in types table):
| Built-in type | Defined as |
|---|---|
| `term()` | `any()` |
| `boolean()` | `'false' \| 'true'` |
| `byte()` | `0..255` |
| `string()` | `[char()]` |
| `no_return()` | `none()` |
| `map()` | `#{any() => any()}` |

# Relationships
## Builds Upon
- **predefined-types** -- Aliases are defined in terms of predefined types
- **type-union** -- Most aliases expand to unions

## Enables
- **function-specification** -- Specs commonly use aliases like `string()`, `boolean()`
- **no-return-type** -- `no_return()` is a built-in alias for `none()`

## Related
- **erlang-type-language** -- Part of the type language vocabulary

## Contrasts With
None within this source.

# Common Errors
- **Error**: Using `nil()` when meaning the empty list type in older code
  **Correction**: `nil()` is the alias for `[]` (the empty list singleton); for a possibly-empty list use `list(T)` or `[T]`

# Common Confusions
- **Confusion**: Thinking `string()` is a distinct built-in type rather than an alias
  **Clarification**: `string()` is simply `[char()]` -- a list of characters. Erlang has no dedicated string type at runtime

- **Confusion**: Thinking `map()` and `#{}` are the same
  **Clarification**: `map()` is `#{any() => any()}` (any map), while `#{}` is only the empty map

# Source Reference
"Types and Function Specifications" chapter, section "Types and their Syntax," built-in types tables.

# Verification Notes
- Definition source: Direct from the two built-in types tables in the source
- Confidence rationale: High -- explicit table of definitions
- Uncertainties: None
- Cross-reference status: All slugs verified against planned cards
