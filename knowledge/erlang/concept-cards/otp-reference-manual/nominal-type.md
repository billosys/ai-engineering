---
# === CORE IDENTIFICATION ===
concept: Nominal Type
slug: nominal-type

# === CLASSIFICATION ===
category: data-types
subcategory: user-defined-types
tier: advanced

# === PROVENANCE ===
source: "Erlang Reference Manual"
source_slug: otp-reference-manual
authors: "Ericsson AB"
chapter: "Nominals"
chapter_number: null
pdf_page: null
section: "Rationale and Syntax"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "nominal"
  - "-nominal type"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - type-declaration
  - erlang-type-language
extends:
  - type-declaration
related:
  - opaque-type
  - nominal-type-derivation
  - dialyzer-nominal-checking
contrasts_with:
  - type-declaration
  - opaque-type

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is a nominal type in Erlang?"
  - "How do I declare a nominal type?"
  - "When should I use -nominal instead of -type?"
  - "What is the syntax for nominal type declarations?"
---

# Quick Definition
A nominal type is a user-defined type declared with `-nominal` that uses name-based equivalence rather than structural equivalence. Two nominal types with different names are incompatible even if their underlying structures are identical.

# Core Definition
The Erlang Reference Manual states: "Nominal typing is an alternative type system. Two nominal types are equivalent if and only if they are declared with the same type name. The syntax for declaring nominal types is `-nominal`." (Nominals, "Rationale and Syntax"). Unlike `-type` declarations where "the Erlang compiler will ignore their type names" and uses structural equivalence, `-nominal` ensures that types with the same structure but different names are treated as distinct. Nominal type-checking is performed by Dialyzer; the Erlang compiler does not perform nominal type-checking.

# Prerequisites
- **type-declaration** -- Nominal types extend the concept of user-defined type declarations
- **erlang-type-language** -- Nominal types are part of the Erlang type language

# Key Properties
1. Syntax: `-nominal Name() :: Type.`
2. Two nominal types with different names are incompatible, even if they have the same structure
3. A nominal type is compatible with a non-opaque, non-nominal type with the same structure (bidirectionally)
4. Nominal type-checking is done in Dialyzer, not the Erlang compiler
5. Nominal types can be derived from other nominal types to establish compatibility
6. The main use case is to prevent accidental misuse of types with the same structure

# Construction / Recognition
## To Construct:
1. Write `-nominal` followed by the type name with parentheses
2. Add `::` followed by the type expression
3. Terminate with a period
4. Example: `-nominal meter() :: integer().`

## To Identify/Recognize:
1. Lines beginning with `-nominal` in module source
2. The type name is an atom followed by `()`
3. The right-hand side after `::` is a type expression

# Context & Application
Nominal types are used when multiple types share the same underlying structure but represent semantically distinct concepts that should never be mixed. The canonical example is unit types: meters vs. feet are both integers, but mixing them is a logical error. Nominal types catch these errors at analysis time via Dialyzer. Within OTP, they provide a lighter-weight alternative to opaque types when you need type distinction but not information hiding.

# Examples
**Example 1** (Rationale and Syntax):
```erlang
-nominal meter() :: integer().
-nominal foot() :: integer().
```
With these declarations, `meter()` and `foot()` are incompatible types despite both being integers.

**Example 2** (Nominal Type-Checking Rules):
```erlang
-spec int_to_meter(integer()) -> meter().
int_to_meter(X) -> X.

-spec foo() -> foot().
foo() -> int_to_meter(24).
```
Dialyzer raises a warning because `foo/0` returns `meter()` but the spec says `foot()`.

**Example 3** (Nominal Type-Checking Rules):
```erlang
-spec qaz() -> integer().
qaz() -> int_to_meter(24).
```
No warning -- `meter()` is compatible with `integer()` because `integer()` is a structural type.

# Relationships
## Builds Upon
- **type-declaration** -- Nominal types are an alternative to structural `-type` declarations
- **erlang-type-language** -- Nominal types use the same type expression syntax

## Enables
- **nominal-type-derivation** -- Nominal types can derive from other nominals for compatibility
- **dialyzer-nominal-checking** -- Dialyzer enforces nominal type rules

## Related
- **opaque-type** -- Both provide stronger guarantees than `-type`, but opaques hide structure while nominals enforce name-based equivalence

## Contrasts With
- **type-declaration** -- `-type` uses structural equivalence; `-nominal` uses name-based equivalence
- **opaque-type** -- `-opaque` hides the type's internal structure from external modules; `-nominal` makes the structure visible but enforces name-based distinction

# Common Errors
- **Error**: Expecting the Erlang compiler to enforce nominal type rules
  **Correction**: Only Dialyzer performs nominal type-checking. The Erlang compiler does not.

- **Error**: Assuming a nominal type is incompatible with all other types
  **Correction**: A nominal type is compatible with non-opaque, non-nominal types with the same structure. Only two distinct nominal types are incompatible with each other.

# Common Confusions
- **Confusion**: Thinking nominal types and opaque types serve the same purpose
  **Clarification**: Nominal types enforce name-based distinction without hiding the underlying structure. Opaque types hide the structure and restrict how the type can be inspected. If you do not need information hiding, nominal types are preferred (and make Dialyzer analysis faster).

- **Confusion**: Believing two nominal types with different names can never be compatible
  **Clarification**: Nominal types support derivation -- if `s()` is derived from `t()`, they are compatible even though they have different names.

# Source Reference
"Nominals" chapter, "Rationale and Syntax" and "Nominal Type-Checking Rules" sections.

# Verification Notes
- Definition source: Direct quotes from source text
- Confidence rationale: High -- explicit definitions and examples in source
- Uncertainties: None
- Cross-reference status: All slugs correspond to planned or existing cards
