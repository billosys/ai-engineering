---
concept: Pattern Matching Optimization
slug: pattern-matching-optimization
category: performance
subcategory: clause-ordering
tier: intermediate
source: "Erlang Efficiency Guide"
source_slug: otp-efficiency-guide
authors: "Ericsson/OTP Team"
chapter: "Functions"
chapter_number: null
pdf_page: null
section: "Pattern Matching"
extraction_confidence: high
aliases:
  - "clause ordering optimization"
  - "pattern matching compilation"
  - "function clause optimization"
prerequisites: []
extends: []
related:
  - function-call-performance
  - setelement-optimization
contrasts_with: []
answers_questions:
  - "What distinguishes pattern matching errors from clause ordering issues?"
  - "When does clause ordering affect pattern matching performance?"
  - "How do variable clauses prevent compiler optimization of pattern matching?"
---

# Quick Definition

The Erlang compiler optimizes pattern matching in function heads, `case`, and `receive` clauses, and clause order rarely matters. However, a variable clause placed between specific-value clauses prevents the compiler from rearranging clauses, forcing suboptimal sequential matching.

# Core Definition

Pattern matching in function heads as well as in `case` and `receive` clauses is optimized by the compiler. With a few exceptions, there is nothing to gain by rearranging clauses (Ericsson/OTP Team, "Functions," section "Pattern Matching").

The key exceptions are:

1. **Binary matching**: The compiler does not rearrange clauses that match binaries. Placing the clause matching the empty binary last is usually slightly faster than placing it first.

2. **Variable clauses between specific-value clauses**: When a clause with a variable pattern appears between clauses with specific values, the compiler cannot rearrange subsequent specific-value clauses into the optimized binary-search dispatch. This forces sequential matching for the clauses after the variable.

# Prerequisites

This is a foundational concept with no prerequisites within this source.

# Key Properties

1. The compiler optimizes pattern matching automatically -- manual clause reordering is usually unnecessary
2. For atom/integer dispatch, the compiler generates a binary-search instruction (efficient even for many values)
3. A variable clause between specific-value clauses splits the match into two groups
4. The first group (before the variable) uses optimized binary search
5. Clauses after the variable require sequential matching only after the variable's guard fails
6. Binary pattern matching clauses are not rearranged by the compiler
7. For binaries, placing the empty-binary clause last is slightly faster
8. A variable in all clauses at the same position is not a problem (e.g., `_Map` in all clauses)

# Construction / Recognition

## Recognizing the Problem

1. Look for function clauses where a variable pattern appears between specific-value patterns at the same argument position
2. Check if the variable clause has a guard (e.g., `when is_integer(Int)`)
3. If the variable clause is in the middle, clauses after it cannot participate in the optimized dispatch

## Fixing the Problem

1. Move the variable clause to the beginning or end of the clause list
2. If moved to the end: specific values get full binary-search optimization
3. If moved to the beginning: the guard is checked first, then specific values are searched
4. Both orderings produce better code than having the variable in the middle

# Context & Application

This optimization matters primarily for functions with many clauses matching atoms or integers, where the compiler's binary-search dispatch provides significant speedup over linear scanning.

**When it matters:**
- Dispatch functions mapping atoms to values (e.g., atom_map examples)
- Protocol parsers matching on message types
- Functions with many specific-value clauses and a catch-all

**When it does not matter:**
- Functions with only a few clauses (linear scan is fine)
- Functions where all clauses use variables in the same position (compiler handles this)
- Pure variable-based matching (no optimization opportunity either way)

# Examples

**DO NOT** -- Variable clause splits the dispatch (source: "Functions," section "Pattern Matching"):

```erlang
atom_map1(one) -> 1;
atom_map1(two) -> 2;
atom_map1(three) -> 3;
atom_map1(Int) when is_integer(Int) -> Int;
atom_map1(four) -> 4;
atom_map1(five) -> 5;
atom_map1(six) -> 6.
```

The compiler must: (1) binary-search `one`, `two`, `three`; (2) try the variable clause with guard; (3) if guard fails, binary-search `four`, `five`, `six`.

**DO** -- Variable clause at end (source: same section):

```erlang
atom_map2(one) -> 1;
atom_map2(two) -> 2;
atom_map2(three) -> 3;
atom_map2(four) -> 4;
atom_map2(five) -> 5;
atom_map2(six) -> 6;
atom_map2(Int) when is_integer(Int) -> Int.
```

**DO** -- Variable clause at beginning (source: same section):

```erlang
atom_map3(Int) when is_integer(Int) -> Int;
atom_map3(one) -> 1;
atom_map3(two) -> 2;
atom_map3(three) -> 3;
atom_map3(four) -> 4;
atom_map3(five) -> 5;
atom_map3(six) -> 6.
```

**DO NOT** -- Variable in middle argument prevents rearrangement (source: same section):

```erlang
map_pairs1(_Map, [], Ys) ->
    Ys;
map_pairs1(_Map, Xs, []) ->
    Xs;
map_pairs1(Map, [X|Xs], [Y|Ys]) ->
    [Map(X, Y)|map_pairs1(Map, Xs, Ys)].
```

The variable `Xs` in the second clause's second argument prevents clause rearrangement.

**DO** -- Constrain the variable with a pattern (source: same section):

```erlang
map_pairs2(_Map, [], Ys) ->
    Ys;
map_pairs2(_Map, [_|_]=Xs, []) ->
    Xs;
map_pairs2(Map, [X|Xs], [Y|Ys]) ->
    [Map(X, Y)|map_pairs2(Map, Xs, Ys)].
```

Replacing `Xs` with `[_|_]=Xs` lets the compiler rearrange clauses and generate nested case-style dispatch, which is faster for the common case of non-empty lists.

# Relationships

## Related

- **function-call-performance** -- Call type performance interacts with pattern matching optimization
- **setelement-optimization** -- Another compiler optimization in the same source

# Common Errors

- **Error**: Placing a catch-all variable clause between specific-value clauses
  **Correction**: Move the catch-all to the beginning or end of the clause list

- **Error**: Using a bare variable where a constrained pattern would work (e.g., `Xs` instead of `[_|_]=Xs`)
  **Correction**: Constrain variables with patterns when possible to enable compiler rearrangement

# Common Confusions

- **Confusion**: Believing that clause ordering always matters for performance
  **Clarification**: The compiler optimizes clause ordering automatically in most cases; manual ordering only matters in the specific exceptions described above

- **Confusion**: Thinking that a variable in any argument position disables optimization
  **Clarification**: A variable that appears in the same position across all clauses (like `_Map` in all three clauses of `map_pairs`) is not a problem. The issue is a variable in one clause where other clauses have specific patterns.

- **Confusion**: Conflating clause ordering with match errors
  **Clarification**: Pattern matching errors (function_clause exceptions) are about the absence of a matching clause, not about clause ordering for performance

# Source Reference

"Functions," section "Pattern Matching." The source provides two detailed examples (atom_map with six atoms plus integer guard, and map_pairs with list matching), including the compiler-generated code for the optimized version of map_pairs.

# Verification Notes

- Definition: Direct from source -- "Pattern matching in function head as well as in case and receive clauses is optimized by the compiler"
- Binary search instruction: Described in source as "a single instruction that does a binary search"
- All examples: Verbatim from source with DO/DO NOT annotations
- Compiler-generated code: Source shows the equivalent explicit_map_pairs case expression
- Dialyzer benefit noted for map_pairs2: Source explicitly mentions "Dialyzer can deduce a better type for the Xs variable"
- Confidence: HIGH -- detailed explanation with multiple examples from official OTP guide
