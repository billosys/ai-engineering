---
# === CORE IDENTIFICATION ===
concept: Callback Attribute
slug: callback-attribute

# === CLASSIFICATION ===
category: otp-behaviours
subcategory: custom-behaviours
tier: advanced

# === PROVENANCE ===
source: "OTP Design Principles"
source_slug: otp-design-principles
authors: "Ericsson AB"
chapter: "sys and proc_lib"
chapter_number: null
pdf_page: null
section: "User-Defined Behaviours"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "-callback"
  - "callback declaration"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - behaviour
extends: []
related:
  - user-defined-behaviour
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What must I know before writing a special process?"
---

# Quick Definition

The `-callback` attribute declares expected callback function signatures with type specifications in a behaviour module, enabling compile-time warnings for missing implementations.

# Core Definition

To have the compiler warn for missing callback functions (as it does for standard OTP behaviours), `-callback` attributes are added to the behaviour module. The syntax mirrors the `-spec` attribute: `-callback Name(Arg1, Arg2, ..., ArgN) -> Result.` where arguments and result are types as described in Types and Function Specifications. Optional callbacks are specified with `-optional_callbacks([OptName1/OptArity1, ..., OptNameK/OptArityK])`. When the compiler encounters `-behaviour(Behaviour)` in a module `Mod`, it calls `Behaviour:behaviour_info(callbacks)` (auto-generated from `-callback` attributes) and compares the result with functions exported from `Mod`, issuing a warning for any missing callback. As an alternative, `behaviour_info/1` can be exported directly, but the `-callback` approach is recommended because its type information supports tooling for documentation and discrepancy detection. (Source: spec_proc.md, "User-Defined Behaviours")

# Prerequisites

- **[Behaviour](/concept-cards/otp-design-principles/behaviour.md)** -- Callback attributes are used within behaviour modules.

# Key Properties

1. **Type-annotated**: Supports the full syntax of `-spec` attributes.
2. **Compiler integration**: The compiler auto-generates `behaviour_info(callbacks)` from `-callback` attributes.
3. **Missing callback warnings**: The compiler warns when a module declares `-behaviour(Mod)` but lacks a required callback.
4. **Optional callbacks**: Declared with `-optional_callbacks([Name/Arity, ...])`.
5. **Tooling support**: Type information enables documentation generation and discrepancy detection.
6. **Contract refinement**: Callback modules can add `-spec` that are subtypes of `-callback` contracts.
7. **Cannot mix with behaviour_info**: `-optional_callbacks` cannot be combined with manually defined `behaviour_info/1`.

# Construction / Recognition

## To Construct/Create:
1. Add `-callback` attributes in the behaviour module:

```erlang
-callback init(State :: term()) -> 'ok'.
-callback handle_req(Req :: term(), State :: term()) -> {'ok', Reply :: term()}.
-callback terminate() -> 'ok'.
```

2. Optionally mark some callbacks as optional:

```erlang
-optional_callbacks([format_state/1]).
```

## To Identify/Recognize:
1. Look for `-callback` attributes in module source.
2. Look for `-optional_callbacks` attributes.
3. Look for `-behaviour(Module)` in consuming modules.

# Context & Application

The `-callback` attribute is the mechanism for defining the contract between a behaviour module and its callback modules. It serves both as documentation and as a compile-time verification mechanism. Tools like Dialyzer can use the type information for static analysis. The alternative `behaviour_info/1` function provides only function name/arity pairs without type information and is considered legacy.

# Examples

**Example 1** (spec_proc.md, "User-Defined Behaviours"): Callback declarations in a behaviour module:

```erlang
-callback init(State :: term()) -> 'ok'.
-callback handle_req(Req :: term(), State :: term()) -> {'ok', Reply :: term()}.
-callback terminate() -> 'ok'.
-callback format_state(State :: term()) -> term().

-optional_callbacks([format_state/1]).
```

**Example 2** (spec_proc.md, "User-Defined Behaviours"): Alternative using behaviour_info/1 (not recommended):

```erlang
behaviour_info(callbacks) ->
    [{init,1},
     {handle_req,2},
     {terminate,0}].
```

**Example 3** (spec_proc.md, "User-Defined Behaviours"): Refining callbacks in the implementing module:

```erlang
-module(db).
-behaviour(simple_server).

-type request() :: {'store', term(), term()};
                   {'lookup', term()}.

-spec handle_req(request(), state()) -> {'ok', term()}.
```

Each `-spec` contract is to be a subtype of the respective `-callback` contract.

# Relationships

## Builds Upon
- **[Behaviour](/concept-cards/otp-design-principles/behaviour.md)** -- Callback attributes define the contract of a behaviour.

## Enables
- **[User-Defined Behaviour](/concept-cards/otp-design-principles/user-defined-behaviour.md)** -- The callback attribute is how user-defined behaviours declare their interface.
- Compile-time verification of callback implementations.
- Tool-based documentation and static analysis.

## Related
- None additional.

## Contrasts With
- `behaviour_info/1` function -- the legacy alternative that lacks type information.

# Common Errors

- **Error**: Combining `-optional_callbacks` with a manually defined `behaviour_info/1` function.
  **Correction**: The `-optional_callbacks` attribute can only be used together with `-callback` attributes. Do not combine it with `behaviour_info/1`.

# Common Confusions

- **Confusion**: `-callback` and `-spec` are the same attribute.
  **Clarification**: `-callback` is used in the behaviour module to define the expected contract. `-spec` is used in the implementing callback module to provide a refined (more specific) contract that must be a subtype of the `-callback` contract.

# Source Reference

spec_proc.md, "User-Defined Behaviours" section.

# Verification Notes

- Definition source: Directly from spec_proc.md, "User-Defined Behaviours" section.
- Confidence rationale: High -- explicitly described with examples and comparison to the alternative.
- Uncertainties: None.
- Cross-reference status: References behaviour, user-defined-behaviour.
