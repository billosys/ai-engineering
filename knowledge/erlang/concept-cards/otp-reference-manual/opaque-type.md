---
# === CORE IDENTIFICATION ===
concept: Opaque Type
slug: opaque-type

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
  - "opaque"
  - "-opaque type"
  - "opaque type alias"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - type-declaration
  - erlang-type-language
extends:
  - type-declaration
related:
  - opacity-contract
  - opaque-api-design-patterns
  - dialyzer-opacity-enforcement
contrasts_with:
  - type-declaration
  - nominal-type

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is an opaque type in Erlang?"
  - "How do I declare an opaque type?"
  - "What is the purpose of -opaque vs -type?"
---

# Quick Definition
An opaque type, declared with `-opaque`, hides the implementation of a data type from external modules, enabling the API to evolve while minimizing the risk of breaking consumers. The runtime does not enforce opacity; it is a contract enforced by convention and Dialyzer.

# Core Definition
The Erlang Reference Manual states: "The main use case for opacity in Erlang is to hide the implementation of a data type, enabling evolving the API while minimizing the risk of breaking consumers. The runtime does not check opacity. Dialyzer provides some opacity-checking, but the rest is up to convention." (Opaques, "Opaque Type Aliases"). The syntax is identical to `-type` but uses the `-opaque` keyword. Since Erlang/OTP 28, "Dialyzer checks opaques in their defining module in the same way as nominals. Outside of the defining module, Dialyzer checks opaques for opacity violations."

# Prerequisites
- **type-declaration** -- Opaque types extend the concept of user-defined types
- **erlang-type-language** -- Opaque types use the same type expression syntax

# Key Properties
1. Syntax: `-opaque Name(Params) :: Type.`
2. Hides the internal structure of the type from external modules
3. The runtime does not enforce opacity -- it is a contract
4. Dialyzer provides opacity-checking but enforcement is not total
5. The defining module is the only one that should rely on the type's definition
6. Enables safe API evolution -- the internal representation can change without breaking properly-written consumers
7. Since OTP 28, Dialyzer checks opaques nominally within the defining module and for opacity violations outside it

# Construction / Recognition
## To Construct:
1. Write `-opaque` followed by the type name with parentheses and optional type parameters
2. Add `::` followed by the type expression
3. Terminate with a period
4. Example: `-opaque set(Element) :: #set{segs :: segs(Element)}.`

## To Identify/Recognize:
1. Lines beginning with `-opaque` in module source
2. The type is meant to have its internal structure hidden from consumers

# Context & Application
Opaque types are essential for building stable, evolvable APIs in Erlang. The canonical example is `sets:set()`, which changed its internal representation from a record to a map in OTP 24. Code that respected the opacity contract continued to work; code that pattern-matched on the record structure broke. Opaque types require more work than structural or nominal types because the defining module must provide a complete API of constructor, query, and deconstructor functions.

# Examples
**Example 1** (Opaque Type Aliases):
```erlang
-opaque set(Element) :: #set{segs :: segs(Element)}.
```
The original definition of `sets:set()`.

**Example 2** (Opaque Type Aliases -- OTP 24 change):
```erlang
-opaque set(Element) :: #set{segs :: segs(Element)} | #{Element => ?VALUE}.
```
The definition changed in OTP 24 to include a map representation. This was safe because the type was opaque.

# Relationships
## Builds Upon
- **type-declaration** -- Opaque types extend the `-type` mechanism
- **erlang-type-language** -- Uses the same type expression syntax

## Enables
- **opacity-contract** -- The opaque declaration establishes a contract
- **opaque-api-design-patterns** -- Requires a specific API design approach
- **dialyzer-opacity-enforcement** -- Dialyzer checks opacity rules

## Related
- **nominal-type** -- Both provide stronger guarantees than `-type`

## Contrasts With
- **type-declaration** -- `-type` exposes structure; `-opaque` hides it
- **nominal-type** -- `-nominal` enforces name-based distinction without hiding structure; `-opaque` hides structure

# Common Errors
- **Error**: Pattern-matching on an opaque type from another module
  **Correction**: Use the API functions provided by the defining module instead of inspecting the internal structure

- **Error**: Using guards like `is_tuple/1` or `is_map/1` on an opaque from another module
  **Correction**: These reveal the underlying type and violate the opacity contract

# Common Confusions
- **Confusion**: Thinking the runtime enforces opacity
  **Clarification**: "Opacity in Erlang is skin-deep: the runtime does not enforce opacity-checking." A determined consumer can still discover the structure by printing, serializing, or using type-revealing functions.

- **Confusion**: Thinking Dialyzer catches all opacity violations
  **Clarification**: "Dialyzer must make some approximations" and enforcement is not total. Opacity is primarily a convention supported by tooling.

# Source Reference
"Opaques" chapter, "Opaque Type Aliases" section.

# Verification Notes
- Definition source: Direct quotes from source text
- Confidence rationale: High -- explicit definition and extensive discussion in source
- Uncertainties: None
- Cross-reference status: All slugs verified
