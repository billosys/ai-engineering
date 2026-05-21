---
# === CORE IDENTIFICATION ===
concept: Doc Signatures
slug: doc-signatures

# === CLASSIFICATION ===
category: documentation
subcategory: entity-documentation
tier: intermediate

# === PROVENANCE ===
source: "Erlang Reference Manual"
source_slug: otp-reference-manual
authors: "Ericsson AB"
chapter: "Documentation"
chapter_number: null
pdf_page: null
section: "Doc signatures"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "documentation signatures"
  - "function signatures"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - doc-attribute
  - function-specification
extends: []
related:
  - documentation-metadata
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How are function signatures determined in Erlang documentation?"
  - "How do I provide a custom documentation signature?"
  - "Where do documentation signatures come from?"
---

# Quick Definition
A doc signature is a short text describing a function and its arguments, derived automatically from the `-spec` or function definition. Custom signatures can be provided as the first line of the `-doc` attribute in the form of a function declaration up to the `->`.

# Core Definition
The Erlang Reference Manual states: "The doc signature is a short text shown to describe the function and its arguments. By default, it is determined by looking at the names of the arguments in the `-spec` or function." (Documentation, "Doc signatures"). For types and callbacks, the signature is derived from the type or callback specification. When a nice signature cannot be easily determined, the MFA syntax is used (e.g., `add/2`). Custom signatures can be provided: "It is possible to supply a custom signature by placing it as the first line of the `-doc` attribute. The provided signature must be in the form of a function declaration up until the `->`." The custom signature is removed from the documentation text.

# Prerequisites
- **doc-attribute** -- Signatures are part of the `-doc` system
- **function-specification** -- Specs provide argument names for auto-generated signatures

# Key Properties
1. Auto-derived from `-spec` argument names (preferred) or function argument names
2. `-spec` names take precedence over function argument names
3. For types/callbacks, derived from the type/callback specification
4. Fallback: MFA syntax (e.g., `add/2`)
5. Custom signatures: first line of `-doc` text in function declaration form (up to `->`)
6. Custom signatures are automatically removed from the documentation text
7. Works for functions, types, and callbacks

# Construction / Recognition
## Auto-derived Signatures:
```erlang
add(One, Two) -> One + Two.
%% Signature: add(One, Two)

-spec sub(One :: integer(), Two :: integer()) -> integer().
sub(X, Y) -> X - Y.
%% Signature: sub(One, Two)  (from spec, not function args)
```

## Custom Signature:
```erlang
-doc """
add(One, Two)

Adds two numbers.
""".
add(A, B) -> A + B.
%% Signature: add(One, Two)
%% Documentation text: "Adds two numbers" (signature line removed)
```

## Type/Callback Signatures:
```erlang
-type number(Value) :: {arith, Value}.
%% Signature: number(Value)

-callback increment(In :: number()) -> Out.
%% Signature: increment(In)
```

# Context & Application
Signatures provide the first thing users see when browsing documentation -- a concise representation of what a function expects. They appear in shell help (`h/1`), IDE tooltips, and generated documentation. The automatic derivation from specs is usually sufficient, but custom signatures are useful when function argument names in the implementation are not descriptive (e.g., internal abbreviations).

# Examples
**Example 1** (Doc signatures -- auto-derived):
```erlang
add(One, Two) -> One + Two.
```
Signature: `add(One, Two)`.

**Example 2** (Doc signatures -- spec-derived):
```erlang
-spec sub(One :: integer(), Two :: integer()) -> integer().
sub(X, Y) -> X - Y.
```
Signature: `sub(One, Two)` -- names come from the spec, not the function.

**Example 3** (Doc signatures -- custom):
```erlang
-doc """
add(One, Two)

Adds two numbers.
""".
add(A, B) -> A + B.
```
Signature: `add(One, Two)`. The first line is consumed as the signature; only "Adds two numbers" remains as documentation.

# Relationships
## Builds Upon
- **doc-attribute** -- Signatures are part of the documentation system
- **function-specification** -- Specs provide argument names for signatures

## Enables
Clear function/type/callback identification in documentation output.

## Related
- **documentation-metadata** -- Metadata complements signatures in documentation display

## Contrasts With
None.

# Common Errors
- **Error**: Writing a custom signature that does not match function declaration form
  **Correction**: The custom signature must be in the form of a function declaration up to `->`. For example, `add(One, Two)`, not `add: One, Two`.

# Common Confusions
- **Confusion**: Thinking the custom signature appears in the documentation text
  **Clarification**: The custom signature is automatically removed from the documentation string. Only the text after the signature line becomes the documentation.

# Source Reference
"Documentation" chapter, "Doc signatures" section.

# Verification Notes
- Definition source: Direct from source text with examples
- Confidence rationale: High -- explicit derivation rules and custom signature syntax
- Uncertainties: None
- Cross-reference status: All slugs verified
