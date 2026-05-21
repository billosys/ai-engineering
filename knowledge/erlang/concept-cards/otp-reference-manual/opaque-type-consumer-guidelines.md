---
# === CORE IDENTIFICATION ===
concept: Opaque Type Consumer Guidelines
slug: opaque-type-consumer-guidelines

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
  - "working with opaque types"
  - "opaque type usage guidelines"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - opaque-type
  - opacity-contract
extends: []
related:
  - opaque-api-design-patterns
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How should I use an opaque type defined in another module?"
  - "What operations are allowed on opaque types from other modules?"
  - "How does subtyping work with opaque types?"
---

# Quick Definition
When working with an opaque type defined in another module, consumers must not inspect the underlying structure. They should use only the API functions provided by the defining module. Equality comparison (`=:=`, `=/=`) is allowed, and standard subtyping rules apply to parameterized opaques.

# Core Definition
The Erlang Reference Manual provides specific recommendations for consumers of opaque types (Opaques, "Opaque Type Aliases"): "Don't examine the underlying type using pattern-matching, guards, or functions that reveal the type, such as `tuple_size/1`. One exception is that `=:=` and `=/=` can be used between two opaques with the same name, or between an opaque and `any()`, as those comparisons do not reveal underlying types." Consumers should "Use functions provided by the module for working with the type." The source also notes: "`sets:set(a)` is a subtype of `sets:set(a | b)` and not the other way around. Generally, you can rely on the property that `the_opaque(T)` is a subtype of `the_opaque(U)` when T is a subtype of U."

# Prerequisites
- **opaque-type** -- Must understand what opaque types are
- **opacity-contract** -- Must understand the obligations placed on consumers

# Key Properties
1. Do not pattern-match on opaque types from other modules
2. Do not use type-revealing guards (`is_tuple/1`, `is_map/1`, etc.)
3. Do not use type-revealing functions (`tuple_size/1`, etc.)
4. Use only the API functions provided by the defining module
5. `=:=` and `=/=` are allowed between two opaques of the same name, or between an opaque and `any()`
6. Subtyping: `opaque(T)` is a subtype of `opaque(U)` when T is a subtype of U
7. Covariant subtyping: `sets:set(a)` is a subtype of `sets:set(a | b)`, not the reverse

# Construction / Recognition
## Allowed Operations:
1. Call API functions from the defining module
2. Compare two instances with `=:=` or `=/=`
3. Pass as arguments to functions expecting the opaque type
4. Store in data structures

## Forbidden Operations:
1. Pattern-matching on the internal structure
2. Guard tests that reveal the type (`is_tuple/1`, `is_map/1`, `is_list/1`)
3. Functions that reveal the type (`tuple_size/1`, `element/2`)
4. Any operation that depends on the internal representation

# Context & Application
These guidelines are critical for writing code that survives API evolution. The `sets:set()` example demonstrates the risk: code that checked `is_tuple(Set)` broke in OTP 24 when the internal representation changed. Following these guidelines ensures that consumer code is resilient to changes in the opaque type's implementation.

# Examples
**Example 1** (Opaque Type Aliases -- correct usage):
```erlang
%% Use API functions only
Set = sets:new(),
Set2 = sets:add_element(foo, Set),
true = sets:is_element(foo, Set2),
List = sets:to_list(Set2).
```

**Example 2** (Opaque Type Aliases -- allowed comparison):
```erlang
%% Equality comparison is allowed
Set1 = sets:new(),
Set2 = sets:new(),
Set1 =:= Set2.  %% OK: does not reveal underlying type
```

**Example 3** (Opaque Type Aliases -- violated contract):
```erlang
%% BAD: reveals internal structure
case sets:new() of
    Set when is_tuple(Set) ->
        io:format("ok")
end.
```
This worked before OTP 24 but broke when the internal representation changed.

# Relationships
## Builds Upon
- **opaque-type** -- These guidelines apply to opaque type usage
- **opacity-contract** -- The contract defines the consumer's obligations

## Enables
Writing robust code that survives internal type representation changes.

## Related
- **opaque-api-design-patterns** -- The definer's complementary obligations

## Contrasts With
None.

# Common Errors
- **Error**: Using `is_map/1` or `is_tuple/1` on an opaque type to determine its representation
  **Correction**: These guards reveal the underlying type. Use the module's API functions instead.

# Common Confusions
- **Confusion**: Thinking subtyping for opaques works backwards
  **Clarification**: `sets:set(a)` is a subtype of `sets:set(a | b)`, not the other way around. A set of atoms is a set of atoms-or-integers, but not vice versa.

# Source Reference
"Opaques" chapter, "Opaque Type Aliases" section, consumer recommendations.

# Verification Notes
- Definition source: Direct from source text -- explicit recommendations
- Confidence rationale: High -- specific do's and don'ts listed
- Uncertainties: None
- Cross-reference status: All slugs verified
