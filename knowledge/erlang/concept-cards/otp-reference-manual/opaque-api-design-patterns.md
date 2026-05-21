---
# === CORE IDENTIFICATION ===
concept: Opaque API Design Patterns
slug: opaque-api-design-patterns

# === CLASSIFICATION ===
category: api-design
subcategory: type-abstraction
tier: intermediate

# === PROVENANCE ===
source: "Erlang Reference Manual"
source_slug: otp-reference-manual
authors: "Ericsson AB"
chapter: "Opaques"
chapter_number: null
pdf_page: null
section: "Opaque Type Aliases"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "opaque type design patterns"
  - "designing with opaque types"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - opaque-type
  - opacity-contract
  - function-specification
extends: []
related:
  - nominal-type-design-guidelines
  - dialyzer-opacity-enforcement
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How should I design an API around an opaque type?"
  - "What functions must I provide when defining an opaque type?"
  - "What pitfalls should I avoid when defining opaque types?"
---

# Quick Definition
When defining an opaque type, the module must provide a complete API of constructor, query, and deconstructor functions, since consumers cannot inspect the type's structure. The source provides specific recommendations for both definers and consumers.

# Core Definition
The Erlang Reference Manual provides explicit recommendations for defining opaques (Opaques, "Opaque Type Aliases"): "Since consumers are expected to not rely on the definition of the opaque type, you must provide functions for constructing, querying, and deconstructing instances of your opaque type." The source also warns: "Don't define an opaque with a type variable in parameter position. This breaks the normal and expected behavior that (for example) `my_type(a)` is a subtype of `my_type(a | b)`." Additional guidelines include: "Don't write case statements that can produce either an opaque or a non-opaque output" and "Add specs to exported functions that use the opaque type."

# Prerequisites
- **opaque-type** -- Must understand opaque type declarations
- **opacity-contract** -- Must understand the obligations the contract places on definers
- **function-specification** -- Specs must be added to functions using the opaque

# Key Properties
1. Must provide constructor functions (e.g., `new/0`, `from_list/1`)
2. Must provide query functions (e.g., `is_element/2`)
3. Must provide deconstructor functions (e.g., `to_list/1`)
4. Must add `-spec` to all exported functions using the opaque type
5. Avoid type variables in parameter position in the opaque definition
6. Avoid case statements that produce either opaque or non-opaque outputs
7. Since OTP 28, `opaque_union` Dialyzer option warns on unions of opaque and non-opaque types outside the defining module

# Construction / Recognition
## Designing an Opaque API:
1. Define the opaque type: `-opaque my_type() :: internal_repr().`
2. Provide constructors: `new/0`, `from_list/1`, etc.
3. Provide queries: `is_empty/1`, `size/1`, `is_element/2`, etc.
4. Provide deconstructors: `to_list/1`, `fold/3`, etc.
5. Add specs to all exported functions using the type
6. Verify with Dialyzer that no opacity violations exist

## Anti-patterns to Avoid:
1. Opaque with type variable in parameter position
2. Functions that return either an opaque or a non-opaque in different branches

# Context & Application
Opaque types place a heavier design burden on the module author compared to structural or nominal types, because consumers cannot inspect the type directly. However, this trade-off enables safe API evolution. The `sets` module exemplifies this pattern: `sets:new/0`, `sets:add_element/2`, `sets:is_element/2`, `sets:to_list/1`, and `sets:from_list/1` provide a complete API. The source also notes that "opaques can be harder to work with for consumers" and suggests considering nominal types when information hiding is not required.

# Examples
**Example 1** (Opaque Type Aliases -- complete API pattern):
```erlang
%% Constructor
sets:new() -> set(_).
sets:from_list(List) -> set(Element).

%% Query
sets:is_element(Element, Set) -> boolean().

%% Deconstructor
sets:to_list(Set) -> [Element].

%% Modification
sets:add_element(Element, Set) -> set(Element).
```

**Example 2** (Opaque Type Aliases -- anti-pattern with type variable in parameter position):
```erlang
%% BAD: type variable in parameter position breaks subtyping
-opaque my_type(A) :: {tag, A}.
%% my_type(a) would NOT be a subtype of my_type(a | b)
```

# Relationships
## Builds Upon
- **opaque-type** -- These patterns apply to opaque type definitions
- **opacity-contract** -- The contract dictates the need for these API patterns

## Enables
Robust, evolvable APIs that can change internal representations safely.

## Related
- **nominal-type-design-guidelines** -- Comparable decision framework for nominal types
- **dialyzer-opacity-enforcement** -- Dialyzer validates the API design

## Contrasts With
None.

# Common Errors
- **Error**: Defining an opaque type without providing constructor/deconstructor functions
  **Correction**: Consumers cannot inspect the type, so you must provide a complete API. Include constructors, queries, and deconstructors.

- **Error**: Defining an opaque with a type variable in parameter position
  **Correction**: This breaks expected subtyping behavior. Use the type variable in the body of the type definition, not in parameter position within the underlying structure.

# Common Confusions
- **Confusion**: Thinking any exported function is sufficient for an opaque API
  **Clarification**: The API must be complete -- constructors, queries, and deconstructors. If consumers need to perform an operation, a function must be provided for it.

# Source Reference
"Opaques" chapter, "Opaque Type Aliases" section, recommendations for defining opaques.

# Verification Notes
- Definition source: Direct from source text -- explicit recommendations
- Confidence rationale: High -- the source lists specific do's and don'ts
- Uncertainties: The "type variable in parameter position" warning could use more elaboration in the source
- Cross-reference status: All slugs verified
