---
# === CORE IDENTIFICATION ===
concept: Nominal Type Compatibility
slug: nominal-type-compatibility

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
section: "Nominal Type-Checking Rules"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "nominal type-checking rules"
  - "nominal type matching"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - nominal-type
  - type-declaration
extends:
  - nominal-type
related:
  - nominal-type-derivation
  - dialyzer-nominal-checking
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "When are two nominal types compatible?"
  - "Can a nominal type be used where a structural type is expected?"
  - "What are the complete rules for nominal type-checking?"
---

# Quick Definition
Nominal type compatibility rules determine when types can be used interchangeably. Two distinct nominal types are incompatible unless one derives from the other, but a nominal type is always compatible with a structural type of the same structure (in both directions).

# Core Definition
The Erlang Reference Manual summarizes the rules: "A function that has a `-spec` that states an argument or a return type to be nominal type `a/0` (or any other arity), accepts or may return: Nominal type `a/0`, A compatible nominal type `b/0`, A compatible structural type." And: "A function that has a `-spec` that states an argument or a return type to be a structural type `b/0` (or any other arity), accepts or may return: A compatible structural type, A compatible nominal type." (Nominals, "Nominal Type-Checking Rules"). The key insight is that "a nominal type is compatible with a non-opaque, non-nominal type with the same structure. This compatibility goes both ways."

# Prerequisites
- **nominal-type** -- Must understand what nominal types are
- **type-declaration** -- Must understand structural types for the compatibility contrast

# Key Properties
1. Two nominal types with different names are incompatible (unless derived)
2. A nominal type is compatible with a structural type of the same structure
3. Compatibility between nominal and structural types is bidirectional
4. A structural type accepts any compatible nominal type
5. A nominal type accepts the same nominal type, derived nominals, and compatible structural types
6. Defining nominal types in different modules does not affect compatibility

# Construction / Recognition
## To Determine Compatibility:
1. If both types are the same nominal type -- compatible
2. If one nominal derives from the other -- compatible
3. If one is nominal and the other is structural with the same structure -- compatible
4. If both are different nominal types with no derivation relationship -- incompatible

# Context & Application
Understanding compatibility rules is essential for designing APIs that use nominal types. The bidirectional compatibility with structural types means nominal types can be introduced gradually into a codebase without breaking existing code that uses structural types. Functions accepting `integer()` will still work with `meter()`, and functions returning `meter()` can have their results used as `integer()`.

# Examples
**Example 1** (Nominal Type-Checking Rules -- incompatible nominals):
```erlang
-spec int_to_meter(integer()) -> meter().
int_to_meter(X) -> X.

-spec foo() -> foot().
foo() -> int_to_meter(24).
```
Dialyzer warning: `foo/0` returns `meter()` but spec says `foot()`. These are incompatible nominal types.

**Example 2** (Nominal Type-Checking Rules -- nominal-structural compatibility):
```erlang
-spec qaz() -> integer().
qaz() -> int_to_meter(24).
```
No warning: `meter()` is compatible with `integer()` because `integer()` is a structural type.

# Relationships
## Builds Upon
- **nominal-type** -- These are the rules governing nominal type interactions

## Enables
- **nominal-type-derivation** -- Derivation creates compatibility between distinct nominal types

## Related
- **dialyzer-nominal-checking** -- Dialyzer enforces these compatibility rules

## Contrasts With
None.

# Common Errors
- **Error**: Assuming a nominal type cannot be used where a plain `integer()` is expected
  **Correction**: Nominal types are compatible with structural types of the same structure. A `meter()` can be used anywhere `integer()` is expected.

# Common Confusions
- **Confusion**: Thinking compatibility is only one-way (nominal to structural but not reverse)
  **Clarification**: Compatibility is bidirectional. A structural type can be passed where a nominal is expected, and a nominal can be passed where a structural type is expected.

# Source Reference
"Nominals" chapter, "Nominal Type-Checking Rules" section.

# Verification Notes
- Definition source: Direct from source text
- Confidence rationale: High -- rules are explicitly enumerated in the source
- Uncertainties: None
- Cross-reference status: All slugs verified
