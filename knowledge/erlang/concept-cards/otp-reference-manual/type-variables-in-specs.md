---
# === CORE IDENTIFICATION ===
concept: Type Variables in Specs
slug: type-variables-in-specs

# === CLASSIFICATION ===
category: functions-pattern-matching
subcategory: type-annotations
tier: intermediate

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
  - "polymorphic specs"
  - "spec type variables"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - function-specification
extends:
  - function-specification
related:
  - when-constraint
  - parameterized-types
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do I write a type specification for a function?"
---

# Quick Definition
Type variables in specs (uppercase identifiers like `X`) specify relationships between argument and return types, enabling polymorphic function specifications such as `-spec id(X) -> X.`.

# Core Definition
"Type variables can be used in specifications to specify relations for the input and output arguments of a function" (Erlang Reference Manual, "Specifications for Functions"). A type variable that appears multiple times constrains those positions to be the same type. For example, `-spec id(X) -> X.` says the return type equals the argument type, which provides "more type information than" a spec where "the type variables are missing" like `-spec id(tuple()) -> tuple().`

# Prerequisites
- **function-specification** -- Type variables extend basic spec syntax

# Key Properties
1. Type variables use uppercase identifiers (same as Erlang variables)
2. Multiple occurrences of the same variable mean the same type
3. `-spec id(X) -> X.` is more informative than `-spec id(tuple()) -> tuple()`
4. Variables can be constrained with `when` clauses
5. It is up to processing tools whether they exploit the extra information

# Construction / Recognition
## To Construct:
1. Use uppercase identifiers in type positions within a spec
2. Repeat the same variable to indicate type equality
3. Optionally add `when Var :: Type` to constrain variables

## To Identify/Recognize:
1. Uppercase identifiers in spec type positions that are not known type names
2. The same identifier appearing in both argument and return positions

# Context & Application
Type variables enable expressing generic function contracts. The classic example is the identity function `-spec id(X) -> X.`, which says "returns the same type it receives." This is essential for utility functions, higher-order functions, and data structure operations.

# Examples
**Example 1** (Specifications for Functions):
Polymorphic identity function:
```text
-spec id(X) -> X.
```

**Example 2** (Specifications for Functions):
The above spec "says that the function takes some tuple and returns _the same_ tuple," which is more precise than:
```erlang
-spec id(tuple()) -> tuple().
```
which only says "takes some tuple and returns some tuple."

**Example 3** (Specifications for Functions):
With constraint:
```erlang
-spec id(X) -> X when X :: tuple().
```

# Relationships
## Builds Upon
- **function-specification** -- Extends specs with variables

## Enables
- **when-constraint** -- Variables can be bounded with constraints

## Related
- **parameterized-types** -- Similar concept of type parameters

## Contrasts With
None within this source.

# Common Errors
- **Error**: Using the same type variable across overloaded spec clauses
  **Correction**: Use different variables in different clauses to avoid confusion

# Common Confusions
- **Confusion**: Thinking `-spec f(X) -> X.` and `-spec f(any()) -> any().` are identical
  **Clarification**: The first says input and output are the same type; the second only says both are unrestricted. The variable version provides strictly more information

# Source Reference
"Types and Function Specifications" chapter, section "Specifications for Functions."

# Verification Notes
- Definition source: Direct from source text with explicit comparison
- Confidence rationale: High -- explicit definition and examples
- Uncertainties: The source notes "it is up to the tools that process the specifications to choose whether to take this extra information into account"
- Cross-reference status: All slugs verified against planned cards
