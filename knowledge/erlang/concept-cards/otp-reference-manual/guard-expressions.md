---
# === CORE IDENTIFICATION ===
concept: Guard Expressions
slug: guard-expressions

# === CLASSIFICATION ===
category: functions-pattern-matching
subcategory: guards
tier: foundational

# === PROVENANCE ===
source: "Erlang Reference Manual"
source_slug: otp-reference-manual
authors: "Ericsson AB"
chapter: "Expressions"
chapter_number: null
pdf_page: null
section: "Guard Expressions"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "guard expression"
  - "guard BIFs"
  - "type test BIFs"
  - "guard-safe expressions"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - term-comparisons
  - arithmetic-expressions
  - boolean-operators
extends: []
related:
  - guard-sequences
  - short-circuit-operators
  - map-in-guards
  - auto-imported-bifs
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What expressions are valid in Erlang guards?"
  - "Which BIFs can be called in guards?"
  - "Why are guard expressions restricted to a subset of Erlang expressions?"
  - "What type test BIFs are available in guards?"
  - "What happens when a guard expression fails?"
---

# Quick Definition

Guard expressions are a restricted subset of Erlang expressions guaranteed to be free of side effects. They include variables, constants, type test BIFs, certain other BIFs, term comparisons, arithmetic, boolean, and short-circuit expressions.

# Core Definition

The set of valid guard expressions is a subset of valid Erlang expressions, restricted because evaluation of a guard expression must be guaranteed to be free of side effects. Valid guard expressions include: variables; constants (atoms, integers, floats, lists, tuples, records, binaries, maps); construction expressions for those types; map update expressions; record expressions; calls to type test BIFs and other allowed guard BIFs; term comparisons; arithmetic expressions; boolean expressions; and short-circuit expressions (`andalso`/`orelse`). If an arithmetic expression, boolean expression, short-circuit expression, or call to a guard BIF fails due to invalid arguments, the entire guard fails. If the guard was part of a guard sequence, the next guard is evaluated (Erlang Reference Manual, "Guard Expressions" section).

# Prerequisites

- **term-comparisons** — Comparison operators are valid guard expressions.
- **arithmetic-expressions** — Arithmetic operators are valid guard expressions.
- **boolean-operators** — Boolean operators (`not`, `and`, `or`, `xor`) are valid guard expressions.

# Key Properties

1. Must be side-effect-free.
2. Failure of a guard expression causes the entire guard to fail (not a runtime error).
3. Type test BIFs: `is_atom/1`, `is_binary/1`, `is_bitstring/1`, `is_boolean/1`, `is_float/1`, `is_function/1,2`, `is_integer/1`, `is_list/1`, `is_map/1`, `is_number/1`, `is_pid/1`, `is_port/1`, `is_record/2,3`, `is_reference/1`, `is_tuple/1`.
4. Other guard BIFs: `abs/1`, `bit_size/1`, `byte_size/1`, `element/2`, `float/1`, `hd/1`, `is_map_key/2`, `length/1`, `map_get/2`, `map_size/1`, `max/2` (OTP 26+), `min/2` (OTP 26+), `node/0,1`, `round/1`, `self/0`, `size/1`, `tl/1`, `trunc/1`, `tuple_size/1`.
5. User-defined functions cannot be called in guards.
6. Short-circuit operators (`andalso`, `orelse`) are valid in guards.

# Construction / Recognition

## To Construct:
```erlang
f(X) when is_integer(X), X > 0 -> positive.
g(X) when is_list(X), length(X) > 3 -> long_list.
h(X) when is_map(X), map_size(X) =:= 0 -> empty_map.
```

## To Recognize:
1. Expressions after `when` keyword in clause heads.
2. Restricted to the allowed set of expressions and BIFs.

# Context & Application

Guard expressions ensure that guards are pure (no side effects) and always terminate. This guarantee allows the runtime to safely evaluate guards during pattern matching without affecting system state. The restriction to specific BIFs means that type checking, numeric comparisons, and basic data structure inspection are available, but arbitrary computation must be done in the clause body.

# Examples

**Example 1**: Type test BIFs in guards:

```erlang
format(X) when is_integer(X) -> integer_to_list(X);
format(X) when is_atom(X)    -> atom_to_list(X);
format(X) when is_list(X)    -> X.
```

**Example 2**: Other BIFs in guards:

```erlang
f(X) when abs(X) > 10 -> large;
f(X) when abs(X) =< 10 -> small.

g(T) when tuple_size(T) =:= 3 -> triple;
g(T) when tuple_size(T) =:= 2 -> pair.
```

**Example 3**: Guard failure is silent:

```erlang
%% length/1 fails on non-lists, but the guard just fails silently
h(X) when length(X) > 0 -> non_empty;
h(_) -> other.

%% h(42) returns 'other' — no error from length(42) failing in the guard
```

# Relationships

## Builds Upon
- **term-comparisons** — Comparison operators usable in guards.
- **arithmetic-expressions** — Arithmetic operators usable in guards.
- **boolean-operators** — Boolean operators usable in guards.

## Enables
- **guard-sequences** — Guard sequences are composed of guard expressions.

## Related
- **short-circuit-operators** — `andalso`/`orelse` are valid in guards.
- **map-in-guards** — Map operations in guards.
- **auto-imported-bifs** — Many guard BIFs are auto-imported.

# Common Errors

- **Error**: Calling a user-defined function in a guard.
  **Correction**: Only allowed BIFs can be called in guards. Move the check to the clause body or restructure using allowed guard BIFs.

- **Error**: Using older type test BIFs without `is_` prefix in compound boolean guard expressions.
  **Correction**: Old BIFs (e.g., `integer(X)`) are only allowed at top level in guards, not in boolean sub-expressions. Use `is_integer(X)` instead.

# Common Confusions

- **Confusion**: Thinking a guard BIF failure raises an exception.
  **Clarification**: A failing guard expression (including a guard BIF call with bad arguments) causes the entire guard to fail silently. The next guard in the sequence is tried, or the clause is skipped.

- **Confusion**: Expecting `min/2` and `max/2` to work in guards in all OTP versions.
  **Clarification**: `min/2` and `max/2` are allowed in guards starting from OTP 26.

# Source Reference

Erlang Reference Manual, "Expressions" chapter, "Guard Expressions" section.

# Verification Notes

- Definition source: Direct from source text — BIF tables reproduced from source
- Confidence rationale: High — comprehensive BIF listing and semantics from source
- Uncertainties: None
- Cross-reference status: BIF lists verified against source tables
