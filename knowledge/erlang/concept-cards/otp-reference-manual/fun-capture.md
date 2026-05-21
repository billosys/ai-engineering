---
# === CORE IDENTIFICATION ===
concept: Fun Capture
slug: fun-capture

# === CLASSIFICATION ===
category: functions-pattern-matching
subcategory: anonymous-functions
tier: foundational

# === PROVENANCE ===
source: "Erlang Reference Manual"
source_slug: otp-reference-manual
authors: "Ericsson AB"
chapter: "Expressions"
chapter_number: null
pdf_page: null
section: "Fun Expressions"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "fun Name/Arity"
  - "fun M:F/A"
  - "function reference"
  - "fun capture expression"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - fun-expressions
extends:
  - fun-expressions
related: []
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is a fun (anonymous function)?"
  - "How do I reference an existing function as a fun?"
  - "What does fun M:F/A mean?"
---

# Quick Definition

Fun capture creates a fun from an existing named function using `fun Name/Arity` (local) or `fun Module:Name/Arity` (remote). The remote form always references the latest version of the module.

# Core Definition

The expression `fun Name/Arity` where `Name` is an atom and `Arity` is an integer refers to an existing local function. It is syntactic sugar for `fun (Arg1,...,ArgN) -> Name(Arg1,...,ArgN) end`. The expression `fun Module:Name/Arity` refers to function `Name` with arity `Arity` in the latest version of module `Module`. In this form, `Module`, `Name`, and `Arity` can also be variables (since Erlang/OTP R15). A fun defined with `Module:Name/Arity` is not dependent on the code for the module in which it is defined (Erlang Reference Manual, "Fun Expressions" section).

# Prerequisites

- **fun-expressions** — Must understand funs before learning the capture shorthand.

# Key Properties

1. `fun Name/Arity` — captures a local function as a fun (syntactic sugar for wrapping in an anonymous fun).
2. `fun Module:Name/Arity` — captures a function from a specific module.
3. The remote form (`Module:Name/Arity`) always refers to the latest version of the module.
4. The remote form is not dependent on the module in which it is defined.
5. Since Erlang/OTP R15, `Module`, `Name`, and `Arity` can be variables in the remote form.
6. `Name/Arity` must specify an existing local function when using the local form.

# Construction / Recognition

## To Capture a Function:
1. Local: `fun FunctionName/Arity`.
2. Remote: `fun ModuleName:FunctionName/Arity`.
3. With variables (remote only): `fun M:F/A` where `M`, `F`, `A` are variables.

## To Recognize:
1. Look for `fun` followed by `Name/Integer` or `Module:Name/Integer`.
2. Distinguished from anonymous fun syntax by absence of `->` and `end`.

# Context & Application

Fun capture is the idiomatic way to pass existing functions as arguments to higher-order functions. `fun lists:sort/1` is clearer and more efficient than writing `fun(L) -> lists:sort(L) end`. The remote capture form is particularly useful for dynamic dispatch and hot code upgrades, since it always resolves to the latest module version.

# Examples

**Example 1** (Fun Expressions section): Using a remote capture:

```erlang
2> fun lists:append/2([1,2], [3,4]).
[1,2,3,4]
```

**Example 2**: Local capture:

```erlang
fun Name/Arity
%% is syntactic sugar for:
fun (Arg1,...,ArgN) -> Name(Arg1,...,ArgN) end
```

# Relationships

## Builds Upon
- **fun-expressions** — Fun capture is a shorthand for creating funs.

## Enables
- No directly dependent concepts in this extraction.

## Related
- No additional related concepts.

## Contrasts With
- No direct contrasts within this source.

# Common Errors

- **Error**: Using `fun Name/Arity` when the function does not exist locally.
  **Correction**: Ensure the function is defined or imported in the current module.

- **Error**: Using variables for `Module`, `Name`, or `Arity` in the local capture form.
  **Correction**: Variables are only allowed in the remote form `fun M:F/A`, not in `fun Name/Arity`.

# Common Confusions

- **Confusion**: Thinking `fun M:F/A` is bound to the module version at capture time.
  **Clarification**: The remote form always refers to the *latest* version of the module, enabling hot code upgrades.

- **Confusion**: Conflating `fun Name/Arity` with a local anonymous fun.
  **Clarification**: `fun Name/Arity` references an existing named function; it does not create a new anonymous function body.

# Source Reference

Erlang Reference Manual, "Expressions" chapter, "Fun Expressions" section.

# Verification Notes

- Definition source: Direct from source text
- Confidence rationale: High — explicit syntax and desugaring rule provided
- Uncertainties: None
- Cross-reference status: Prerequisites verified
