---
# === CORE IDENTIFICATION ===
concept: Adapter Pattern
slug: adapter-pattern

# === CLASSIFICATION ===
category: api-design
subcategory: design-patterns
tier: intermediate

# === PROVENANCE ===
source: Programming Erlang, Second Edition
source_slug: programming-erlang
authors: Joe Armstrong
chapter: "Programming Idioms"
chapter_number: 24
pdf_page: null
section: "Adapter Patterns"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - adapter
  - adapter module

# === TYPED RELATIONSHIPS ===
prerequisites:
  - tuple-module
  - pattern-matching
extends:
  - tuple-module
related:
  - intentional-programming
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do I give dissimilar modules a common interface?"
  - "How do I encapsulate state together with a module name in Erlang?"
---

# Quick Definition

The adapter pattern uses a tuple module to present a single, uniform interface over two or more libraries that have similar functionality but different APIs.

# Core Definition

"Adapters are tuple modules that provide a uniform interface toward an application." When several libraries do "more or less the same thing" — for example different key-value store implementations — but have different APIs, choosing one early couples your program to it. The adapter pattern solves this: the adapter exposes a constant interface, and "the code behind the adapter can be changed to reflect different requirements" without changes to the application. Switching back ends becomes a one-line change ("Adapter Patterns").

# Prerequisites

- **Tuple module** — An adapter *is* a tuple module; the call-rewriting mechanism is what carries the back-end choice and its state.
- **Pattern matching** — The adapter's functions pattern match on the `{Mod, Type, Val}` tuple to dispatch to the right back end.

# Key Properties

1. The adapter is a tuple module of the form `{adapter_module, Type, Val}`.
2. A `new(Type)` function creates an adapter for a chosen back end.
3. Each operation pattern matches on `Type` and delegates to the corresponding library, returning a new adapter tuple.
4. The application interface stays constant while back ends vary.
5. Switching back ends is a single change to the `new/1` call.

# Construction / Recognition

## To Construct/Create:
1. Decide the common interface (e.g., `new/1`, `store/3`, `lookup/2`).
2. Write `new(Type)` clauses that return `{?MODULE, Type, InitialState}` for each back end.
3. Write each operation with clauses matching `{_, Type, Val}` that call the appropriate back-end library and return a new adapter tuple.
4. Application code uses tuple-module call syntax and never names a back end except in the `new/1` call.

## To Identify/Recognize:
1. A module returning `{?MODULE, Type, Val}` tuples whose functions branch on `Type`.
2. Application code that switches implementations by changing one argument.

# Context & Application

- **Typical contexts**: Code that depends on a swappable library (key-value stores, caches, persistence layers).
- **Common applications**: Providing identical interfaces to in-memory vs. on-disk stores so a design decision can be revisited later.
- **Historical/stylistic notes**: "Adapters are useful for providing generic interfaces to preexisting code."

# Examples

**Example 1** ("Adapter Patterns" — `adapter_db1.erl`): An adapter giving `dict` and `lists` the same key-value interface:

```erlang
-module(adapter_db1).
-export([new/1, store/3, lookup/2]).

new(dict) ->
    {?MODULE, dict, dict:new()};
new(lists) ->
    {?MODULE, list, []}.

store(Key, Val, {_, dict, D}) ->
    D1 = dict:store(Key, Val, D),
    {?MODULE, dict, D1};
store(Key, Val, {_, list, L}) ->
    L1 = lists:keystore(Key, 1, L, {Key,Val}),
    {?MODULE, list, L1}.

lookup(Key, {_,dict,D}) ->
    dict:find(Key, D);
lookup(Key, {_,list,L}) ->
    case lists:keysearch(Key, 1, L) of
        {value, {Key,Val}} -> {ok, Val};
        false -> error
    end.
```

**Example 2** ("Adapter Patterns"): Application code is back-end-agnostic — `M0 = adapter_db1:new(dict)`, then `M1 = M0:store(Key1, Val2)`, etc. To use the `lists` implementation, "we just change the line of code that created the module to `Mod = adapter_db1:new(lists)`."

# Relationships

## Builds Upon
- **Tuple module** — The adapter is implemented as a tuple module.

## Enables
- This idiom is itself an application-level building block; it does not have downstream prerequisite cards in this chapter.

## Related
- **Intentional programming** — Both are about designing interfaces that communicate intent clearly.

## Contrasts With
- This concept has no direct contrast within the chapter.

# Common Errors

- **Error**: Spreading back-end-specific calls (e.g., `dict:store`) throughout application code.
  **Correction**: Confine all back-end knowledge to the adapter; application code uses only the common interface.

- **Error**: Returning raw back-end state instead of a new adapter tuple from an operation.
  **Correction**: Every operation must return `{?MODULE, Type, NewVal}` so the adapter identity and type tag are preserved.

# Common Confusions

- **Confusion**: Thinking the adapter must unify libraries with identical APIs.
  **Clarification**: Its value is precisely for libraries with *different* APIs — it normalizes dissimilar interfaces.

# Source Reference

Chapter 24: Programming Idioms, Section "Adapter Patterns." See the `adapter_db1.erl` and `adapter_db1_test.erl` listings.

# Verification Notes

- Definition source: Direct adaptation from "Adapter Patterns."
- Confidence rationale: HIGH — the source defines the pattern and gives a complete worked adapter plus its test.
- Uncertainties: Relies on tuple modules, a deprecated OTP feature; the pattern itself remains valid with explicit-argument modules.
- Cross-reference status: Verified concept names exist or are planned.
- Re-extraction notes: Fresh extraction; no pre-existing card.
