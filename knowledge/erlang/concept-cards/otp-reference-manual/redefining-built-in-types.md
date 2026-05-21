---
# === CORE IDENTIFICATION ===
concept: Redefining Built-in Types
slug: redefining-built-in-types

# === CLASSIFICATION ===
category: data-types
subcategory: type-system-rules
tier: intermediate

# === PROVENANCE ===
source: "Erlang Reference Manual"
source_slug: otp-reference-manual
authors: "Ericsson AB"
chapter: "Types and Function Specifications"
chapter_number: null
pdf_page: null
section: "Redefining built-in types"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases: []

# === TYPED RELATIONSHIPS ===
prerequisites:
  - type-declaration
  - predefined-types
extends: []
related:
  - built-in-type-aliases
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What must I know before writing type specifications?"
---

# Quick Definition
Since OTP 26, it is permitted to define a user type with the same name as a built-in type, though it compiles with a warning and is not recommended.

# Core Definition
"Starting from Erlang/OTP 26, it is permitted to define a type having the same name as a built-in type." However, "it is recommended to avoid deliberately reusing built-in names because it can be confusing." The primary motivation is forward compatibility: "when an Erlang/OTP release introduces a new type, code that happened to define its own type having the same name will continue to work" with a warning (Erlang Reference Manual, "Redefining built-in types").

# Prerequisites
- **type-declaration** -- Understanding `-type` declarations
- **predefined-types** -- Understanding what built-in types exist

# Key Properties
1. Permitted since OTP 26
2. Compiles successfully but with a warning
3. The local definition takes precedence over the built-in
4. Dialyzer will not emit additional warnings beyond the compilation warning
5. Designed for forward compatibility, not intentional reuse

# Construction / Recognition
## To Identify/Recognize:
1. A `-type` declaration whose name matches a built-in type
2. Compilation produces a warning about the name conflict

# Context & Application
This feature exists primarily as a safety valve for forward compatibility. When OTP adds new built-in types, existing code that coincidentally used the same name continues to compile (with a warning) rather than breaking. Deliberate reuse is discouraged.

# Examples
**Example 1** (Redefining built-in types):
Hypothetical scenario where OTP 42 introduces:
```erlang
-type gadget() :: {'gadget', reference()}.
```
Existing code with a different definition:
```erlang
-type gadget() :: #{}.
```
The code will still compile with a warning, and Dialyzer will not emit additional warnings.

# Relationships
## Builds Upon
- **type-declaration** -- Redefines a type that collides with a built-in
- **predefined-types** -- The built-in types that might be collided with

## Enables
Forward compatibility when OTP introduces new built-in types.

## Related
- **built-in-type-aliases** -- The aliases that might be accidentally redefined

## Contrasts With
None within this source.

# Common Errors
- **Error**: Deliberately redefining a built-in type to change its meaning
  **Correction**: While permitted, this is confusing and discouraged; use a different name

# Common Confusions
- **Confusion**: Thinking the redefinition silently replaces the built-in everywhere
  **Clarification**: The local definition takes precedence only within the defining module; the compiler issues a warning

# Source Reference
"Types and Function Specifications" chapter, section "Redefining built-in types."

# Verification Notes
- Definition source: Direct from source text with example
- Confidence rationale: High -- explicit change notice and example
- Uncertainties: None
- Cross-reference status: All slugs verified against planned cards
