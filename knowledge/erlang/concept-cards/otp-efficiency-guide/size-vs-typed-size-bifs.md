---
concept: Size vs Typed Size BIFs
slug: size-vs-typed-size-bifs
category: performance
subcategory: type-safety
tier: foundational
source: "Erlang Efficiency Guide"
source_slug: otp-efficiency-guide
authors: "Ericsson/OTP Team"
chapter: "Common Caveats"
chapter_number: null
pdf_page: null
section: "size/1"
extraction_confidence: high
aliases:
  - "size/1 vs tuple_size/1"
  - "size/1 vs byte_size/1"
  - "polymorphic size BIF"
prerequisites: []
extends: []
related:
  - length-function-cost
  - erlang-data-type-memory-sizes
contrasts_with: []
answers_questions:
  - "What distinguishes size/1 from tuple_size/1 and byte_size/1?"
  - "Why should tuple_size/1 and byte_size/1 be preferred over size/1?"
---

# Quick Definition

`size/1` is a polymorphic BIF that returns the size of both tuples and binaries. Using the type-specific BIFs `tuple_size/1` and `byte_size/1` instead gives the compiler and runtime more optimization opportunities and provides Dialyzer with better type information.

# Core Definition

`size/1` returns the size for both tuples and binaries. Using the BIFs `tuple_size/1` and `byte_size/1` gives the compiler and the runtime system more opportunities for optimization. Another advantage is that those BIFs give Dialyzer more type information (Ericsson/OTP Team, "Common Caveats," section "size/1").

# Prerequisites

This is a foundational concept with no prerequisites within this source.

# Key Properties

1. `size/1` works on both tuples (returns element count) and binaries (returns byte count)
2. `tuple_size/1` works only on tuples -- returns the number of elements
3. `byte_size/1` works only on binaries -- returns the number of bytes
4. All three are O(1) operations (constant time)
5. Type-specific BIFs enable better compiler optimizations
6. Type-specific BIFs provide Dialyzer with more precise type information
7. `size/1` obscures the programmer's intent about expected argument type

# Construction / Recognition

## Recognizing the Improvement Opportunity

1. Search for calls to `size/1`
2. Determine whether the argument is expected to be a tuple or a binary
3. Replace with `tuple_size/1` or `byte_size/1` accordingly

## Applying the Fix

1. If the argument is a tuple: replace `size(T)` with `tuple_size(T)`
2. If the argument is a binary: replace `size(B)` with `byte_size(B)`
3. If the argument could be either: consider restructuring to handle each case explicitly

# Context & Application

This is a code quality and optimization concern rather than a correctness issue. Using type-specific BIFs is considered best practice because:

- It makes the code's intent clearer (documenting expected types)
- It helps Dialyzer catch type errors at analysis time
- It gives the compiler more information for optimization
- It helps in guards, where the type-specific variants are more restrictive and informative

**Note:** This caveat is relatively minor in terms of runtime performance impact. The primary benefit is improved static analysis and code clarity.

# Examples

**Prefer type-specific BIFs** (derived from source: "Common Caveats," section "size/1"):

```erlang
%% Instead of:
size(MyTuple)
size(MyBinary)

%% Use:
tuple_size(MyTuple)
byte_size(MyBinary)
```

**In guards:**

```erlang
%% Less informative:
foo(X) when size(X) > 3 -> ...

%% More informative -- Dialyzer knows X is a tuple:
foo(X) when tuple_size(X) > 3 -> ...

%% More informative -- Dialyzer knows X is a binary:
bar(X) when byte_size(X) > 3 -> ...
```

# Relationships

## Related

- **length-function-cost** -- `tuple_size/1` and `byte_size/1` are the O(1) counterparts to the O(n) `length/1`
- **erlang-data-type-memory-sizes** -- Understanding data type representations helps explain why size operations are O(1)

# Common Errors

- **Error**: Using `size/1` out of habit when the argument type is known
  **Correction**: Use `tuple_size/1` for tuples and `byte_size/1` for binaries

# Common Confusions

- **Confusion**: Believing `size/1` is deprecated or will be removed
  **Clarification**: `size/1` is not deprecated; it is simply less informative than the type-specific alternatives

- **Confusion**: Thinking `size/1` is slower at runtime than the typed variants
  **Clarification**: The performance difference is typically negligible at runtime; the main benefits are compile-time optimization opportunities and better Dialyzer analysis

# Source Reference

"Common Caveats," section "size/1." Brief section recommending `tuple_size/1` and `byte_size/1` over `size/1` for optimization and Dialyzer benefits.

# Verification Notes

- Definition: Direct from source -- "size/1 returns the size for both tuples and binaries"
- Optimization/Dialyzer benefits: Explicitly stated in source
- Confidence: HIGH -- explicit recommendation from official OTP guide, though the section is brief
