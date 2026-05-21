---
concept: Length Function Cost
slug: length-function-cost
category: common-pitfalls
subcategory: list-operations
tier: foundational
source: "Erlang Efficiency Guide"
source_slug: otp-efficiency-guide
authors: "Ericsson/OTP Team"
chapter: "Common Caveats"
chapter_number: null
pdf_page: null
section: "length/1"
extraction_confidence: high
aliases:
  - "length/1 performance"
  - "list length complexity"
prerequisites: []
extends: []
related:
  - append-operator-efficiency
  - size-vs-typed-size-bifs
contrasts_with:
  - size-vs-typed-size-bifs
answers_questions:
  - "What distinguishes length/1 from constant-time size operations?"
  - "When should length/1 be avoided?"
  - "How can pattern matching replace length/1 for minimum-length guards?"
---

# Quick Definition

`length/1` traverses the entire list and runs in O(n) time, unlike `tuple_size/1`, `byte_size/1`, and `bit_size/1` which all execute in constant time. In time-critical code with potentially long lists, pattern matching can sometimes replace `length/1`.

# Core Definition

The time for calculating the length of a list is proportional to the length of the list, as opposed to `tuple_size/1`, `byte_size/1`, and `bit_size/1`, which all execute in constant time. Normally, there is no need to worry about the speed of `length/1`, because it is efficiently implemented in C. In time-critical code, you might want to avoid it if the input list could potentially be very long (Ericsson/OTP Team, "Common Caveats," section "length/1").

Some uses of `length/1` can be replaced by pattern matching, though with a subtle behavioral difference: `length(L)` fails on improper lists, while pattern matching may accept them.

# Prerequisites

This is a foundational concept with no prerequisites within this source.

# Key Properties

1. `length/1` runs in O(n) time -- proportional to list length
2. `tuple_size/1`, `byte_size/1`, and `bit_size/1` run in O(1) time
3. `length/1` is implemented in C, so it is fast for typical lists
4. For time-critical code with very long lists, alternatives should be considered
5. `length(L)` fails with a `badarg` error on improper lists
6. Pattern-matching alternatives may accept improper lists (subtle behavioral difference)

# Construction / Recognition

## Recognizing When to Optimize

1. Identify uses of `length/1` in guards or conditions
2. Check if the comparison is against a small constant (e.g., `length(L) >= 3`)
3. If so, the length check can be replaced with a pattern match
4. Assess whether the input list could be very long in practice

## Replacing length/1 with Pattern Matching

1. For `length(L) >= N` where N is small, use a pattern with N anonymous variables: `[_,_,...|_]=L`
2. For `length(L) =:= 0`, use pattern matching on `[]`
3. For `length(L) > 0`, match on `[_|_]`

# Context & Application

This caveat is most relevant in:

- Guard expressions evaluated frequently (e.g., in hot message-handling loops)
- Recursive functions where `length/1` is called on each iteration
- Functions processing lists that could grow very large

For most code, `length/1` is fast enough. The optimization matters primarily when the function is called in a tight loop or when lists can be very long (thousands to millions of elements).

# Examples

**Before** -- Using `length/1` in a guard (source: "Common Caveats," section "length/1"):

```erlang
foo(L) when length(L) >= 3 ->
    ...
```

**After** -- Pattern matching alternative (source: same section):

```erlang
foo([_,_,_|_]=L) ->
   ...
```

**Behavioral difference:** `length(L)` fails if `L` is an improper list, while the pattern `[_,_,_|_]` accepts an improper list (e.g., `[1,2,3|not_a_list]`).

# Relationships

## Related

- **append-operator-efficiency** -- Another O(n) list operation where the linear cost can be surprising

## Contrasts With

- **size-vs-typed-size-bifs** -- `tuple_size/1` and `byte_size/1` are O(1) operations, in direct contrast to `length/1`

# Common Errors

- **Error**: Using `length(L) =:= 0` to check for an empty list
  **Correction**: Pattern match on `[]` instead -- it is both more idiomatic and O(1)

- **Error**: Calling `length/1` on each iteration of a recursive function to check a shrinking list
  **Correction**: Track the count as a separate variable, or restructure to use pattern matching

# Common Confusions

- **Confusion**: Believing `length/1` is O(1) because lists are a fundamental data type
  **Clarification**: Erlang lists are singly-linked; there is no stored length field. `length/1` must walk the entire chain.

- **Confusion**: Thinking the pattern-matching replacement is exactly equivalent to `length/1`
  **Clarification**: There is a subtle difference: `length/1` rejects improper lists, while the pattern match does not

# Source Reference

"Common Caveats," section "length/1." The source compares `length/1` to the constant-time BIFs, provides a before/after example of pattern-matching replacement, and notes the improper list behavioral difference.

# Verification Notes

- Definition: Direct from source -- "The time for calculating the length of a list is proportional to the length of the list"
- Constant-time alternatives: Explicitly listed in source (tuple_size/1, byte_size/1, bit_size/1)
- Pattern matching example: Verbatim from source
- Improper list caveat: Explicitly noted in source
- Confidence: HIGH -- explicit documentation from official OTP guide
