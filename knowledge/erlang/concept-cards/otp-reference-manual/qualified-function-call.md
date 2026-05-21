---
# === CORE IDENTIFICATION ===
concept: Qualified Function Call
slug: qualified-function-call

# === CLASSIFICATION ===
category: functions-pattern-matching
subcategory: function-calls
tier: foundational

# === PROVENANCE ===
source: "Erlang Reference Manual"
source_slug: otp-reference-manual
authors: "Ericsson AB"
chapter: "Expressions"
chapter_number: null
pdf_page: null
section: "Function Calls"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "remote function call"
  - "external function call"
  - "fully qualified function call"
  - "Module:Function call"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - function-call
  - function-arity
extends:
  - function-call
related:
  - fun-capture
  - auto-imported-bifs
contrasts_with:
  - function-call

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do I call a function in another module in Erlang?"
  - "What is a fully qualified function call?"
  - "How does a remote function call differ from a local call during hot code loading?"
  - "Can Module and Function be variables in a qualified call?"
---

# Quick Definition

A qualified function call has the form `ExprM:ExprF(Expr1,...,ExprN)` where `ExprM` and `ExprF` are atoms (or expressions evaluating to atoms) specifying the module and function. This form always refers to the latest loaded version of the module.

# Core Definition

In the fully qualified function call form `ExprM:ExprF(Expr1,...,ExprN)`, each of `ExprM` and `ExprF` must be an atom or an expression that evaluates to an atom. The function is said to be called by using the fully qualified function name, often referred to as a remote or external function call. Unlike local function calls, a fully qualified call always refers to the latest version of the module. This is significant during hot code loading, where a qualified call will use the newly loaded module code (Erlang Reference Manual, "Function Calls" section).

# Prerequisites

- **function-call** — Understanding local calls provides context for why qualified calls exist.
- **function-arity** — Function identity requires both name and arity.

# Key Properties

1. `ExprM:ExprF(Expr1,...,ExprN)` — the fully qualified form.
2. `ExprM` and `ExprF` must be atoms or evaluate to atoms.
3. Always refers to the latest loaded version of the target module.
4. Essential for hot code upgrades (calling into the new version).
5. Can be used to call any exported function in any loaded module.

# Construction / Recognition

## To Construct:
```erlang
lists:keyfind(Name, 1, List)
io:format("Hello ~p~n", [World])
```

## To Recognize:
1. Look for the `Module:Function(Args)` form with the `:` separator.
2. Both module and function parts must evaluate to atoms.

# Context & Application

Qualified function calls are used to invoke functions from other modules and are the standard way to use library functions. They are also critical during hot code upgrades: a module can call itself using `?MODULE:Function(Args)` to ensure it transitions to the latest loaded version. The distinction between local and qualified calls is one of Erlang's mechanisms for seamless runtime code upgrades.

# Examples

**Example 1** (Function Calls section): Calling a function in another module:

```erlang
lists:keyfind(Name, 1, List)
```

**Example 2**: Self-qualified call for hot code loading:

```erlang
loop(State) ->
    receive
        upgrade ->
            ?MODULE:loop(State);  %% switches to latest module version
        Msg ->
            NewState = handle(Msg, State),
            loop(NewState)        %% stays on current version
    end.
```

# Relationships

## Builds Upon
- **function-call** — The qualified form extends the concept of function calls.
- **function-arity** — The called function is identified by module, name, and arity.

## Enables
- **fun-capture** — `fun Module:Function/Arity` creates a fun from a qualified reference.

## Related
- **auto-imported-bifs** — BIFs can be called with explicit `erlang:F(Args)` qualification.

## Contrasts With
- **function-call** — Local calls use the current module version; qualified calls use the latest version.

# Common Errors

- **Error**: Using a non-atom value for the module or function name.
  **Correction**: Ensure `ExprM` and `ExprF` evaluate to atoms. Variables are allowed if they hold atom values at runtime.

- **Error**: Calling a non-exported function via a qualified call.
  **Correction**: The target function must be exported from its module. Use `-export([F/A])` in the target module.

# Common Confusions

- **Confusion**: Thinking local and qualified calls to the same module behave identically.
  **Clarification**: They differ during hot code loading. A local call stays on the current module version; a qualified call (`?MODULE:F(Args)`) switches to the latest loaded version.

# Source Reference

Erlang Reference Manual, "Expressions" chapter, "Function Calls" section.

# Verification Notes

- Definition source: Direct from source text
- Confidence rationale: High — clear definition and distinction from local calls in source
- Uncertainties: None
- Cross-reference status: Contrast with function-call verified in source
