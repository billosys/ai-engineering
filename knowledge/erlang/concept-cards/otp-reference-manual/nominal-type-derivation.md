---
# === CORE IDENTIFICATION ===
concept: Nominal Type Derivation
slug: nominal-type-derivation

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
  - "nominal derivation"
  - "derived nominal type"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - nominal-type
  - nominal-type-compatibility
extends:
  - nominal-type
related:
  - dialyzer-nominal-checking
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How can two differently named nominal types be made compatible?"
  - "What does it mean for one nominal type to derive from another?"
  - "Can nominal type derivation span multiple modules?"
---

# Quick Definition
Nominal type derivation is the mechanism by which one nominal type is declared to be based on another nominal type, making the two compatible despite having different names. Derivation can be direct or transitive through a chain of nominal declarations.

# Core Definition
The Erlang Reference Manual states: "There is one exception where two nominal types with different names can be compatible: when one is derived from the other." For nominal types `s()` and `t()`, `s()` can be derived from `t()` in two ways: (1) directly, where `-nominal s() :: t().`, or (2) transitively, through a chain of nominals. "In both cases, `s()` and `t()` are compatible nominal types even though they have different names. Defining them in different modules does not affect compatibility." (Nominals, "Nominal Type-Checking Rules").

# Prerequisites
- **nominal-type** -- Must understand nominal type declarations
- **nominal-type-compatibility** -- Must understand the general compatibility rules

# Key Properties
1. Direct derivation: `-nominal s() :: t().` makes `s()` and `t()` compatible
2. Transitive derivation: a chain of nominal declarations creates compatibility through the chain
3. Cross-module derivation: defining derived types in different modules does not affect compatibility
4. Derivation is the only way two differently named nominal types can be compatible
5. Derivation creates a parent-child relationship, not a bidirectional alias

# Construction / Recognition
## To Create Derivation:
1. Declare a nominal type whose definition references another nominal type
2. Direct: `-nominal s() :: t().`
3. Transitive: `-nominal s() :: n1().` then `-nominal n1() :: n2().` then `-nominal n2() :: t().`

## To Identify Derivation:
1. A `-nominal` declaration whose right-hand side is another nominal type
2. Follow the chain of definitions to find the root nominal type

# Context & Application
Derivation is useful when building type hierarchies or refinements. For example, a `positive_meter()` type could derive from `meter()`, inheriting compatibility while adding semantic specificity. This allows functions expecting `meter()` to accept `positive_meter()` without triggering Dialyzer warnings.

# Examples
**Example 1** (Nominal Type-Checking Rules -- direct derivation):
```erlang
-nominal s() :: t().
```
`s()` is directly derived from `t()`, making them compatible.

**Example 2** (Nominal Type-Checking Rules -- transitive derivation):
```erlang
-nominal s() :: nominal_1().
-nominal nominal_1() :: nominal_2().
-nominal nominal_2() :: t().
```
`s()` is derived from `t()` through a chain, making `s()` and `t()` compatible.

# Relationships
## Builds Upon
- **nominal-type** -- Derivation is defined in terms of nominal type declarations
- **nominal-type-compatibility** -- Derivation is the exception to the rule that different nominals are incompatible

## Enables
Building nominal type hierarchies where more specific types are compatible with more general ones.

## Related
- **dialyzer-nominal-checking** -- Dialyzer follows the derivation chain when checking compatibility

## Contrasts With
None.

# Common Errors
- **Error**: Assuming derivation only works within a single module
  **Correction**: Defining derived nominal types in different modules does not affect compatibility.

# Common Confusions
- **Confusion**: Thinking derivation creates a bidirectional alias (like `-type`)
  **Clarification**: Derivation creates a directed relationship. `s()` derives from `t()`, meaning `s()` is compatible with `t()`, but the relationship is established through the declaration chain, not through structural equivalence.

# Source Reference
"Nominals" chapter, "Nominal Type-Checking Rules" section.

# Verification Notes
- Definition source: Direct from source text with explicit examples
- Confidence rationale: High -- the source provides both definition and examples
- Uncertainties: The exact semantics of "compatibility direction" in derivation (whether s is a subtype of t or vice versa) are not fully detailed
- Cross-reference status: All slugs verified
