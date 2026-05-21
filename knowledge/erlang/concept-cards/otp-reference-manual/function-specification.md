---
# === CORE IDENTIFICATION ===
concept: Function Specification
slug: function-specification

# === CLASSIFICATION ===
category: functions-pattern-matching
subcategory: type-annotations
tier: foundational

# === PROVENANCE ===
source: "Erlang Reference Manual"
source_slug: otp-reference-manual
authors: "Ericsson AB"
chapter: "Types and Function Specifications"
chapter_number: null
pdf_page: null
section: "Specifications for Functions"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "-spec"
  - "function contract"
  - "type specification"
  - "spec attribute"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - erlang-type-language
  - predefined-types
extends: []
related:
  - type-declaration
  - spec-overloading
  - type-variables-in-specs
  - when-constraint
  - no-return-type
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is a type specification (-spec)?"
  - "How do I write a type specification for a function?"
  - "How does the type specification system relate to Dialyzer?"
---

# Quick Definition
A function specification (`-spec`) declares the argument types and return type of a function, serving as a contract that tools like Dialyzer can verify.

# Core Definition
"A specification (or contract) for a function is given using the `-spec` attribute. The general format is as follows: `-spec Function(ArgType1, ..., ArgTypeN) -> ReturnType.`" An implementation of the function "must exist in the current module, and the arity of the function must match the number of arguments, otherwise the compilation fails" (Erlang Reference Manual, "Specifications for Functions").

# Prerequisites
- **erlang-type-language** -- Specs use the type language to express types
- **predefined-types** -- Specs reference predefined and user-defined types

# Key Properties
1. Basic syntax: `-spec Function(ArgType1, ..., ArgTypeN) -> ReturnType.`
2. The function must exist in the current module with matching arity
3. An optional module prefix form: `-spec Module:Function(ArgTypes) -> ReturnType.`
4. Named arguments for documentation: `-spec Function(ArgName1 :: Type1, ...) -> RT.`
5. Can be overloaded with multiple clauses separated by `;`
6. Supports type variables for polymorphism
7. Supports `when` constraints for bounded quantification

# Construction / Recognition
## To Construct:
1. Write `-spec` followed by the function name
2. List argument types in parentheses
3. Add `->` and the return type
4. Terminate with a period
5. Optionally add named arguments: `ArgName :: Type`
6. Optionally add `when` constraints

## To Identify/Recognize:
1. Lines beginning with `-spec` in module source
2. The function name matches an existing function in the module
3. Contains `->` separating argument types from return type

# Context & Application
Function specifications are the most commonly used part of Erlang's type system. They document the expected inputs and outputs of functions and enable Dialyzer to find type errors. Well-specified modules with comprehensive `-spec` attributes are easier to maintain and less prone to subtle bugs.

# Examples
**Example 1** (Specifications for Functions):
Basic spec:
```text
-spec Function(ArgType1, ..., ArgTypeN) -> ReturnType.
```

**Example 2** (Specifications for Functions):
With module name and named arguments:
```text
-spec Module:Function(ArgType1, ..., ArgTypeN) -> ReturnType.
-spec Function(ArgName1 :: Type1, ..., ArgNameN :: TypeN) -> RT.
```

**Example 3** (Specifications for Functions):
For non-returning functions:
```erlang
my_error(Err) -> throw({error, Err}).
```
```text
-spec my_error(term()) -> no_return().
```

# Relationships
## Builds Upon
- **erlang-type-language** -- Specs are expressed in the type language
- **predefined-types** -- Specs reference type expressions

## Enables
- **spec-overloading** -- Specs can have multiple clauses
- **type-variables-in-specs** -- Type variables enable polymorphic specs
- **when-constraint** -- Constraints can bound type variables

## Related
- **type-declaration** -- Specs reference user-defined types
- **no-return-type** -- Used for functions that never return

## Contrasts With
None within this source.

# Common Errors
- **Error**: Writing a spec for a function that does not exist in the module
  **Correction**: The function must exist with matching arity; otherwise compilation fails

- **Error**: Spec arity not matching function arity
  **Correction**: The number of argument types in the spec must equal the function's arity

# Common Confusions
- **Confusion**: Thinking `-spec` is enforced at runtime
  **Clarification**: Specs are checked by Dialyzer and used for documentation, but not enforced at runtime

- **Confusion**: Thinking specs must be placed directly before the function
  **Clarification**: While conventional to place specs before their function, the compiler only requires they be in the same module

# Source Reference
"Types and Function Specifications" chapter, section "Specifications for Functions."

# Verification Notes
- Definition source: Direct from source text
- Confidence rationale: High -- explicit definition with multiple syntax forms
- Uncertainties: None
- Cross-reference status: All slugs verified against planned cards
