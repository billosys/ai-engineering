---
# === CORE IDENTIFICATION ===
concept: Structural vs Nominal Typing
slug: structural-vs-nominal-typing

# === CLASSIFICATION ===
category: data-types
subcategory: type-systems
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
  - "structural typing vs nominal typing"
  - "name-based vs structure-based typing"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - type-declaration
  - erlang-type-language
extends: []
related:
  - nominal-type
  - opaque-type
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is the difference between structural and nominal typing in Erlang?"
  - "Which type system does the Erlang compiler use?"
  - "How does Erlang support both structural and nominal typing?"
---

# Quick Definition
Erlang's compiler uses structural typing by default, where two types are equivalent if their structures match regardless of name. The `-nominal` attribute introduces nominal typing, where equivalence requires the same type name, enforced by Dialyzer.

# Core Definition
The Erlang Reference Manual explains: "For user-defined types defined with `-type`, the Erlang compiler will ignore their type names. This means the Erlang compiler uses a structural type system. Two types are seen as equivalent if their structures are the same. Type comparison is based on the structures of the types, not on how the user explicitly defines them." (Nominals, "Rationale and Syntax"). In contrast, "Nominal typing is an alternative type system. Two nominal types are equivalent if and only if they are declared with the same type name." The structural and nominal systems coexist: nominal types are compatible with structural types that have the same structure, but two distinct nominal types are not compatible with each other.

# Prerequisites
- **type-declaration** -- Understanding `-type` declarations is needed to contrast with `-nominal`
- **erlang-type-language** -- Both systems operate within the Erlang type language

# Key Properties
1. Structural typing: equivalence is determined by structure, not by name
2. Nominal typing: equivalence requires the same declared type name
3. The Erlang compiler uses structural typing; Dialyzer adds nominal checking
4. A nominal type is compatible with a structural type of the same structure (bidirectional)
5. Two distinct nominal types are incompatible even with identical structures
6. These type systems coexist -- code can use both `-type` and `-nominal` in the same module

# Construction / Recognition
## To Identify Structural Typing:
1. Types declared with `-type` are structural
2. Two `-type` declarations with the same structure are interchangeable
3. The compiler treats them as equivalent

## To Identify Nominal Typing:
1. Types declared with `-nominal` are nominal
2. Two `-nominal` declarations are only equivalent if they share the same name
3. Dialyzer enforces the distinction

# Context & Application
The distinction matters when a codebase has multiple types with the same underlying structure representing different domains. For example, `-type meter() :: integer()` and `-type foot() :: integer()` are structurally equivalent and can be freely mixed, which can lead to unit-mismatch bugs. Switching to `-nominal` for these types introduces compile-time (Dialyzer) guarantees that they cannot be accidentally interchanged.

# Examples
**Example 1** (Rationale and Syntax -- structural equivalence):
```erlang
-type meter() :: integer().
-type foot() :: integer().
```
With `-type`, `meter()` and `foot()` are equivalent because their structures are the same.

**Example 2** (Rationale and Syntax -- nominal distinction):
```erlang
-nominal meter() :: integer().
-nominal foot() :: integer().
```
With `-nominal`, `meter()` and `foot()` are no longer compatible. Passing a `foot()` where `meter()` is expected will trigger a Dialyzer warning.

# Relationships
## Builds Upon
- **type-declaration** -- Structural typing is the default for `-type` declarations
- **erlang-type-language** -- Both systems use the same type expression syntax

## Enables
- **nominal-type** -- Understanding the distinction motivates the use of `-nominal`

## Related
- **opaque-type** -- Opaques add a third dimension: hiding internal structure

## Contrasts With
None -- this card describes the contrast itself.

# Common Errors
- **Error**: Assuming the Erlang compiler enforces nominal type rules
  **Correction**: The compiler uses structural typing exclusively. Only Dialyzer checks nominal types.

# Common Confusions
- **Confusion**: Thinking structural typing means "no type checking"
  **Clarification**: Structural typing still checks type structures. It simply does not distinguish types by name. Two types with the same structure are treated as identical.

- **Confusion**: Assuming nominal and structural types cannot interact
  **Clarification**: Nominal types are compatible with structural types of the same structure. The incompatibility is only between two different nominal types.

# Source Reference
"Nominals" chapter, "Rationale and Syntax" section.

# Verification Notes
- Definition source: Direct quotes from source text
- Confidence rationale: High -- the source explicitly contrasts the two systems
- Uncertainties: None
- Cross-reference status: All slugs verified
