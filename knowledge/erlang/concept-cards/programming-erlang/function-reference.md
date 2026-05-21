---
# === CORE IDENTIFICATION ===
concept: Function Reference
slug: function-reference

# === CLASSIFICATION ===
category: functions-pattern-matching
subcategory: higher-order-functions
tier: intermediate

# === PROVENANCE ===
source: Programming Erlang, Second Edition
source_slug: programming-erlang
authors: Joe Armstrong
chapter: "The Rest of Sequential Erlang"
chapter_number: 8
pdf_page: null
section: "Function References"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "fun Name/Arity"
  - "fun Mod:Func/Arity"
  - named fun reference

# === TYPED RELATIONSHIPS ===
prerequisites:
  - arity
extends: []
related:
  - apply
  - dynamic-code-loading
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do I refer to a function as a value?"
  - "What is the difference between a local and a remote function reference?"
---

# Quick Definition

A function reference is the `fun Name/Arity` or `fun Mod:Func/Arity` notation that names an existing function so it can be passed as a value to higher-order functions.

# Core Definition

To refer to a function defined in the current module or an external module, Erlang uses two notations ("The Rest of Sequential Erlang", *Function References*): `fun LocalFunc/Arity` refers to the local function `LocalFunc` with `Arity` arguments in the current module; `fun Mod:RemoteFunc/Arity` refers to the external function `RemoteFunc` with `Arity` arguments in module `Mod`. For example `fun x1:square/1` means the function `square/1` in module `x1`. Function references that include the module name "provide switch-over points for dynamic code upgrade."

# Prerequisites

- **Arity** — A function reference identifies a function by `Name/Arity`.

# Key Properties

1. `fun Name/Arity` references a local function in the current module.
2. `fun Mod:Func/Arity` references an external function in another module.
3. A function reference is a value that can be passed to higher-order functions.
4. Module-qualified references are switch-over points for dynamic code upgrade.

# Construction / Recognition

## To Construct/Create:
1. Local: `fun square/1`.
2. Remote: `fun x1:square/1`.

## To Identify/Recognize:
1. A `fun` followed by `Name/Arity` (no clause body) is a function reference, not an anonymous function.

# Context & Application

- **Typical contexts**: passing an existing named function to higher-order functions like `lists:map`.
- **Common applications**: `double(L) -> lists:map(fun square/1, L).` and the remote form `lists:map(fun x1:square/1, L)`.
- **Historical/stylistic notes**: the module-qualified form is preferred when dynamic code upgrade matters, since it re-resolves to the latest module version.

# Examples

**Example 1** (*Function References*): a local function reference passed to `lists:map`:

```erlang
double(L) -> lists:map(fun square/1, L).
```

**Example 2** (*Function References*): a remote function reference:

```erlang
double(L) -> lists:map(fun x1:square/1, L).
```

# Relationships

## Builds Upon
- **Arity** — A reference names a function by name and arity.

## Enables
- This concept does not have downstream cards in scope.

## Related
- **apply** — Both concern indirect invocation of named functions.
- **Dynamic code loading** — Module-qualified references are upgrade switch-over points.

## Contrasts With
- No directly contrasting concept in scope.

# Common Errors

- **Error**: Writing `fun square` without the arity.
  **Correction**: A function reference must include the arity, `fun square/1`.

# Common Confusions

- **Confusion**: Confusing `fun Name/Arity` with an anonymous `fun(Args) -> ... end`.
  **Clarification**: A function reference names an existing function; an anonymous fun has its own clause body.

# Source Reference

Chapter 8: "The Rest of Sequential Erlang", section "Function References".

# Verification Notes

- Definition source: Direct quotation and adaptation from *Function References*.
- Confidence rationale: HIGH — the source explicitly defines both reference forms with examples.
- Uncertainties: None.
- Cross-reference status: Slug `arity` extracted in this chapter; `apply`, `dynamic-code-loading` extracted in this chapter.
- Re-extraction notes: Fresh extraction; no prior card existed for this slug.
