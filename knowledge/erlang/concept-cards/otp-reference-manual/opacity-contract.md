---
# === CORE IDENTIFICATION ===
concept: Opacity Contract
slug: opacity-contract

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
  - "opaque type contract"
  - "opacity convention"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - opaque-type
extends: []
related:
  - opaque-api-design-patterns
  - dialyzer-opacity-enforcement
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What obligations does an opaque type place on consumers?"
  - "What obligations does an opaque type place on the defining module?"
  - "What happens when the opacity contract is violated?"
---

# Quick Definition
The opacity contract is the agreement that only the defining module should rely on the internal definition of an opaque type. Consumers must not pattern-match, use type-revealing guards, or otherwise depend on the underlying structure.

# Core Definition
The Erlang Reference Manual states: "when a module defines an `-opaque`, the contract is that only the defining module should rely on the definition of the type: no other modules should rely on the definition." (Opaques, "Opaque Type Aliases"). This means "code that pattern-matched on `set` as a record/tuple technically broke the contract, and opted in to being potentially broken when the definition of `set()` changed." The contract is enforced by convention and partially by Dialyzer, but "the runtime does not enforce opacity-checking."

# Prerequisites
- **opaque-type** -- Must understand the opaque type mechanism

# Key Properties
1. Only the defining module should rely on the opaque type's definition
2. Consumers must not pattern-match, use type-revealing guards, or inspect structure
3. The contract is not enforced by the runtime -- it is a convention
4. Dialyzer partially enforces the contract but enforcement is not total
5. Violating the contract "opts in" to being broken by future changes
6. `=:=` and `=/=` can be used between two opaques with the same name, or between an opaque and `any()`
7. Subtyping is preserved: `the_opaque(T)` is a subtype of `the_opaque(U)` when T is a subtype of U

# Construction / Recognition
## Consumer Obligations:
1. Do not pattern-match on the opaque type
2. Do not use guards that reveal the type (e.g., `is_tuple/1`, `is_map/1`)
3. Do not use functions that reveal the type (e.g., `tuple_size/1`)
4. Use only the functions provided by the defining module
5. Exception: `=:=` and `=/=` are allowed for comparison without revealing type

## Definer Obligations:
1. Provide constructor functions (e.g., `sets:new/0`, `sets:from_list/1`)
2. Provide query functions (e.g., `sets:is_element/2`)
3. Provide deconstructor functions (e.g., `sets:to_list/1`)
4. Add specs to exported functions that use the opaque type

# Context & Application
The opacity contract is what makes opaque types useful for API evolution. When OTP 24 changed the internal representation of `sets:set()` from a record to include a map variant, code respecting the contract continued to work. Code that violated it -- such as `case sets:new() of Set when is_tuple(Set) -> ...` -- broke. This demonstrates the practical consequence of the contract.

# Examples
**Example 1** (Opaque Type Aliases -- contract violation):
```erlang
case sets:new() of
    Set when is_tuple(Set) ->
        io:format("ok")
end.
```
This code broke the opacity contract by using `is_tuple/1` on a set. Before OTP 24, this printed `ok`. In OTP 24, it may error because sets changed to use maps internally.

**Example 2** (Opaque Type Aliases -- correct usage):
```erlang
Set = sets:new(),
Set2 = sets:add_element(foo, Set),
true = sets:is_element(foo, Set2).
```
This respects the contract by using only the functions provided by the `sets` module.

# Relationships
## Builds Upon
- **opaque-type** -- The contract arises from the `-opaque` declaration

## Enables
- **opaque-api-design-patterns** -- The contract dictates how APIs using opaques should be designed

## Related
- **dialyzer-opacity-enforcement** -- Dialyzer partially enforces the contract

## Contrasts With
None.

# Common Errors
- **Error**: Using `is_tuple/1`, `is_map/1`, or similar guards on an opaque from another module
  **Correction**: Use the API functions provided by the defining module. These guards reveal the underlying type and violate the contract.

- **Error**: Pattern-matching on the internal structure of an opaque type
  **Correction**: Use deconstructor functions provided by the defining module (e.g., `sets:to_list/1`).

# Common Confusions
- **Confusion**: Believing the runtime will prevent opacity violations
  **Clarification**: "Opacity in Erlang is skin-deep: the runtime does not enforce opacity-checking." An `is_map/1` check on a map-based set will pass at runtime. The contract is enforced by convention and Dialyzer, not the runtime.

- **Confusion**: Thinking all structural access to an opaque is forbidden
  **Clarification**: `=:=` and `=/=` comparisons are allowed between two opaques with the same name, or between an opaque and `any()`, because these do not reveal the underlying type.

# Source Reference
"Opaques" chapter, "Opaque Type Aliases" section.

# Verification Notes
- Definition source: Direct quotes from source text
- Confidence rationale: High -- explicit contract description with concrete examples
- Uncertainties: None
- Cross-reference status: All slugs verified
