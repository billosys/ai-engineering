---
# === CORE IDENTIFICATION ===
concept: Nominal Type Design Guidelines
slug: nominal-type-design-guidelines

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
  - "when to use nominal types"
  - "nominal type best practices"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - nominal-type
  - opaque-type
extends: []
related:
  - structural-vs-nominal-typing
  - nominal-type-compatibility
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "When should I use -nominal instead of -type?"
  - "When should I use -nominal instead of -opaque?"
  - "What types benefit from being declared nominal?"
---

# Quick Definition
The Erlang Reference Manual provides guidelines for when a type should be declared nominal: when types share structure but should not be mixed, when representing units of measurement, and when an opaque type does not require information hiding.

# Core Definition
The Erlang Reference Manual offers three suggestions for when to make a type nominal (Nominals, "Nominal Type-Checking Rules"): (1) "If there are other types in the same module with the same structure, and they should never be mixed, all of them can benefit from being nominal types." (2) "If a type represents a unit like meter, second, byte, and so on, defining it as a nominal type is always more useful than `-type`. You get the nice guarantee that you cannot mix them up with other units defined as nominal types." (3) "If an opaque type does not require its type information to be hidden, it can benefit from being redefined as a nominal type. This makes Dialyzer's analysis faster."

# Prerequisites
- **nominal-type** -- Must understand what nominal types are and how they work
- **opaque-type** -- Must understand opaques to evaluate the trade-off

# Key Properties
1. Use nominal when multiple types share structure but represent distinct concepts
2. Use nominal for unit types (meter, second, byte, etc.)
3. Prefer nominal over opaque when information hiding is not needed (better Dialyzer performance)
4. Nominal types provide mix-up prevention without the API burden of opaque types
5. Nominal types do not require providing constructor/accessor functions like opaques do

# Construction / Recognition
## Decision Process:
1. Are there multiple types with the same structure that should not be mixed? Use `-nominal`
2. Does the type represent a unit of measurement? Use `-nominal`
3. Is the current type `-opaque` but information hiding is not needed? Consider switching to `-nominal`
4. Is there no risk of accidental mixing? `-type` is sufficient

# Context & Application
These guidelines help developers choose between `-type`, `-nominal`, and `-opaque`. The key trade-off is between convenience and safety. `-type` is the simplest but provides no name-based guarantees. `-nominal` adds name-based distinction without hiding structure. `-opaque` hides structure but requires a complete API of constructor/accessor functions.

# Examples
**Example 1** (same structure, different semantics):
```erlang
%% These should be nominal because mixing them is a logical error
-nominal meter() :: integer().
-nominal foot() :: integer().
-nominal second() :: integer().
```

**Example 2** (opaque to nominal migration):
```erlang
%% Before: opaque hides structure unnecessarily
-opaque user_id() :: integer().

%% After: nominal prevents mixing without hiding structure
-nominal user_id() :: integer().
```
Switching to nominal makes Dialyzer's analysis faster while still preventing `user_id()` from being accidentally mixed with other nominal integer types.

# Relationships
## Builds Upon
- **nominal-type** -- These guidelines apply to nominal type usage
- **opaque-type** -- Understanding opaques is needed to evaluate when nominals are preferred

## Enables
Better type design decisions in Erlang modules.

## Related
- **structural-vs-nominal-typing** -- The guidelines help choose between the two systems

## Contrasts With
None.

# Common Errors
- **Error**: Using `-opaque` when only name-based distinction (not information hiding) is needed
  **Correction**: Use `-nominal` instead -- it provides name-based distinction with less overhead and faster Dialyzer analysis

# Common Confusions
- **Confusion**: Thinking `-nominal` always replaces `-opaque`
  **Clarification**: If consumers should not know the internal structure of the type, `-opaque` is still the right choice. `-nominal` is for when structure visibility is acceptable but accidental type mixing is not.

# Source Reference
"Nominals" chapter, final section with design suggestions.

# Verification Notes
- Definition source: Direct from source text -- three explicit suggestions
- Confidence rationale: High -- explicit recommendations in the source
- Uncertainties: None
- Cross-reference status: All slugs verified
