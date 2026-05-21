---
# === CORE IDENTIFICATION ===
concept: Parameterized Types
slug: parameterized-types

# === CLASSIFICATION ===
category: data-types
subcategory: user-defined-types
tier: intermediate

# === PROVENANCE ===
source: "Erlang Reference Manual"
source_slug: otp-reference-manual
authors: "Ericsson AB"
chapter: "Types and Function Specifications"
chapter_number: null
pdf_page: null
section: "Type Declarations of User-Defined Types"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "generic types"
  - "type parameters"
  - "polymorphic types"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - type-declaration
extends:
  - type-declaration
related:
  - type-variables-in-specs
  - remote-types
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do I write a type specification for a function?"
  - "What must I know before writing type specifications?"
---

# Quick Definition
Parameterized types include type variables between parentheses in their declaration, allowing the type to be instantiated with different concrete types at each use site.

# Core Definition
"Type declarations can also be parameterized by including type variables between the parentheses. The syntax of type variables is the same as Erlang variables, that is, they start with an uppercase letter. These variables are to appear on the RHS of the definition" (Erlang Reference Manual, "Type Declarations of User-Defined Types").

# Prerequisites
- **type-declaration** -- Parameterized types extend the basic type declaration

# Key Properties
1. Type variables use Erlang variable syntax (start with uppercase letter)
2. Type variables must appear on the right-hand side of the definition
3. The arity of a parameterized type includes its parameters (e.g., `orddict/2`)
4. When exported, the arity reflects the number of parameters

# Construction / Recognition
## To Construct:
1. Write `-type Name(Var1, ..., VarN) :: TypeExpr.`
2. Use the type variables on the right-hand side
3. Example: `-type orddict(Key, Val) :: [{Key, Val}].`

## To Identify/Recognize:
1. Type declarations with uppercase identifiers in the parentheses
2. The same variables appear in the type expression body

# Context & Application
Parameterized types are essential for defining generic data structures. Common uses include container types (lists of a specific element type), result types (ok/error tuples with specific value types), and dictionary types. They mirror the concept of generics in other languages.

# Examples
**Example 1** (Type Declarations of User-Defined Types):
```erlang
-type orddict(Key, Val) :: [{Key, Val}].
```

**Example 2** (Type Declarations of User-Defined Types):
Exporting a parameterized type:
```erlang
-export_type([orddict/2]).
```
Using it as a remote type:
```erlang
mod:orddict(atom(), term())
```

# Relationships
## Builds Upon
- **type-declaration** -- Extends basic type declaration with parameters

## Enables
- **remote-types** -- Parameterized types can be exported and used remotely

## Related
- **type-variables-in-specs** -- Similar variable syntax in function specs

## Contrasts With
None within this source.

# Common Errors
- **Error**: Forgetting to include the type variable on the right-hand side of the definition
  **Correction**: All type variables in the parameter list must appear in the type expression body

- **Error**: Using lowercase for type variable names
  **Correction**: Type variables must start with an uppercase letter, like Erlang variables

# Common Confusions
- **Confusion**: Confusing type variable arity with function arity
  **Clarification**: Type arity counts the number of type parameters, e.g., `orddict/2` has arity 2 because it takes two type parameters, not because it is a two-element type

# Source Reference
"Types and Function Specifications" chapter, section "Type Declarations of User-Defined Types."

# Verification Notes
- Definition source: Direct from source text with example
- Confidence rationale: High -- explicit definition and example
- Uncertainties: None
- Cross-reference status: All slugs verified against planned cards
