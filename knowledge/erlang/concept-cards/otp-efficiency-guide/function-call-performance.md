---
concept: Function Call Performance
slug: function-call-performance
category: performance
subcategory: call-dispatch
tier: intermediate
source: "Erlang Efficiency Guide"
source_slug: otp-efficiency-guide
authors: "Ericsson/OTP Team"
chapter: "Functions"
chapter_number: null
pdf_page: null
section: "Function Calls"
extraction_confidence: high
aliases:
  - "function call hierarchy"
  - "apply vs direct call"
  - "call dispatch performance"
prerequisites: []
extends: []
related:
  - pattern-matching-optimization
  - nif-efficiency
contrasts_with: []
answers_questions:
  - "What is the performance hierarchy of Erlang function call types?"
  - "Why is apply/3 slower than a direct function call?"
  - "When should funs be preferred over apply/3 for callbacks?"
---

# Quick Definition

Erlang function calls have a performance hierarchy: local/external calls are fastest, fun calls are slightly slower, `apply/3` with known arity is next, and `apply/3` with unknown arity is slowest. The key factor is whether the runtime needs a hash-table lookup to find the function code.

# Core Definition

The source provides a rough hierarchy of function call performance (Ericsson/OTP Team, "Functions," section "Function Calls"):

1. **Calls to local or external functions** (`foo()`, `m:foo()`) are the fastest calls.
2. **Calling or applying a fun** (`Fun()`, `apply(Fun, [])`) is just a little slower than external calls.
3. **Applying an exported function** (`Mod:Name()`, `apply(Mod, Name, [])`) where the number of arguments is known at compile time is next.
4. **Applying an exported function** (`apply(Mod, Name, Args)`) where the number of arguments is not known at compile time is the least efficient.

A fun contains an indirect pointer to the function that implements it, so fun calls do not involve hash-table lookup. `apply/3` must look up the code for the function in a hash table, making it always slower than a direct call or fun call.

# Prerequisites

This is a foundational concept with no prerequisites within this source.

# Key Properties

1. Local and external calls (`foo()`, `m:foo()`) are fastest -- direct dispatch
2. Fun calls (`Fun()`) are nearly as fast -- indirect pointer, no hash lookup
3. `apply/3` with compile-time known arity (`Mod:Name()`) is moderately fast
4. `apply/3` with runtime arity (`apply(Mod, Name, Args)`) is slowest
5. The performance difference stems from whether a hash-table lookup is needed
6. Funs store an indirect pointer to their implementing function
7. `apply/3` always requires a hash-table lookup for code resolution
8. Caching callback functions into funs can be more efficient than repeated `apply/3` calls

# Construction / Recognition

## Optimizing Call Performance

1. Prefer direct function calls (`mod:fun(Args)`) over `apply/3` whenever possible
2. If the module and function are dynamic, cache the lookup result in a fun
3. If using `apply/3`, ensure the argument count is known at compile time when possible (use `Mod:Name(A, B)` syntax)
4. Avoid `apply(Mod, Name, Args)` where `Args` is a runtime-constructed list

## When apply/3 Is Necessary

1. Plugin/callback systems where module and function names are configured at runtime
2. Generic dispatch where the function name is data-driven
3. Hot code loading scenarios where indirect dispatch is required

# Context & Application

The performance hierarchy is relevant for frequently-called functions in performance-critical paths. For most application code, the difference is negligible, but it matters in:

- Inner loops of data processing pipelines
- High-frequency callback dispatch (e.g., event handlers called thousands of times per second)
- Generic frameworks that dispatch to user-provided functions

**Practical recommendation from source:** Caching callback functions into funs may be more efficient in the long run than `apply` calls for frequently-used callbacks. This converts a hash-table lookup per call into a pointer dereference.

# Examples

**Performance hierarchy** (source: "Functions," section "Function Calls"):

```erlang
%% Fastest: direct local or external call
Result = my_module:my_function(Arg1, Arg2).

%% Nearly as fast: fun call (no hash lookup)
Fun = fun my_module:my_function/2,
Result = Fun(Arg1, Arg2).

%% Slower: apply with known arity
Result = apply(Mod, Name, [Arg1, Arg2]).
%% Or equivalently:
Result = Mod:Name(Arg1, Arg2).

%% Slowest: apply with unknown arity
Args = build_args(),
Result = apply(Mod, Name, Args).
```

**Optimization: caching callbacks as funs** (derived from source: same section):

```erlang
%% Instead of calling apply/3 repeatedly:
loop(Mod, Fun, State) ->
    NewState = apply(Mod, Fun, [State]),
    loop(Mod, Fun, NewState).

%% Cache the callback as a fun:
loop(Callback, State) ->
    NewState = Callback(State),
    loop(Callback, NewState).
%% Where Callback = fun Mod:Fun/1 was created once at initialization
```

# Relationships

## Related

- **pattern-matching-optimization** -- Clause dispatch efficiency interacts with call performance
- **nif-efficiency** -- NIFs have their own call overhead profile

# Common Errors

- **Error**: Using `apply(Module, Function, [Arg1, Arg2])` when `Module:Function(Arg1, Arg2)` would work
  **Correction**: Use the `Mod:Fun(Args)` syntax when module and function names are known, even if they are variables, to give the compiler arity information

- **Error**: Storing module/function pairs instead of funs for frequently-used callbacks
  **Correction**: Create a fun reference (`fun Mod:Fun/Arity`) once and store that instead

# Common Confusions

- **Confusion**: Believing `Mod:Fun(Args)` syntax is the same as `apply(Mod, Fun, [Args])`
  **Clarification**: `Mod:Fun(A, B)` gives the compiler arity information (2 args), enabling better optimization than `apply(Mod, Fun, [A, B])` where the list length may not be known at compile time

- **Confusion**: Thinking fun calls are significantly slower than direct calls
  **Clarification**: Fun calls are "just a little slower" than direct calls -- the difference is minimal because funs use a pointer dereference, not a hash lookup

- **Confusion**: Believing `apply/3` is always slow
  **Clarification**: When the arity is known at compile time (e.g., `Mod:Name(A, B)`), apply is moderately fast. It is only the unknown-arity form that is the least efficient.

# Source Reference

"Functions," section "Function Calls" and subsection "Notes and Implementation Details." The source provides the four-level performance hierarchy and explains the implementation difference (pointer for funs vs. hash lookup for apply).

# Verification Notes

- Performance hierarchy: Verbatim from source (four levels listed explicitly)
- Implementation details: Direct from source -- fun contains indirect pointer, apply uses hash table
- Callback caching recommendation: Explicit in source -- "Caching callback functions into funs may be more efficient in the long run than apply calls for frequently-used callbacks"
- Confidence: HIGH -- explicit performance hierarchy with implementation rationale from official OTP guide
