---
concept: Setelement Optimization
slug: setelement-optimization
category: compiler-optimization
subcategory: tuple-operations
tier: intermediate
source: "Erlang Efficiency Guide"
source_slug: otp-efficiency-guide
authors: "Ericsson/OTP Team"
chapter: "Common Caveats"
chapter_number: null
pdf_page: null
section: "setelement/3"
extraction_confidence: high
aliases:
  - "setelement/3 coalescing"
  - "tuple update optimization"
  - "setelement compiler optimization"
prerequisites:
  - erlang-data-type-memory-sizes
extends: []
related:
  - pattern-matching-optimization
contrasts_with: []
answers_questions:
  - "When does the compiler optimize multiple setelement/3 calls?"
  - "What conditions must be met for setelement/3 coalescing?"
  - "Why does setelement/3 copy the tuple on each call?"
---

# Quick Definition

`setelement/3` copies the entire tuple it modifies, so using it in a loop creates a new tuple copy on each iteration. The compiler can coalesce multiple consecutive `setelement/3` calls into a single copy-and-update operation under specific conditions.

# Core Definition

`setelement/3` copies the tuple it modifies. Therefore, updating a tuple in a loop using `setelement/3` creates a new copy of the tuple on each iteration (Ericsson/OTP Team, "Common Caveats," section "setelement/3").

Under certain conditions, the compiler can coalesce multiple calls to `setelement/3` into a single operation, avoiding the cost of copying the tuple for each call. Starting with Erlang/OTP 26, the following conditions must all be met for coalescing:

1. The tuple argument must be known at compile time to be a tuple of a specific size
2. The element indices must be integer literals, not variables or expressions
3. There must be no intervening expressions between the `setelement/3` calls
4. The tuple returned from one `setelement/3` call must be used only in the subsequent `setelement/3` call

Before OTP 26, an additional condition applied: `setelement/3` calls had to be made in descending order of indices.

# Prerequisites

- **erlang-data-type-memory-sizes** -- Understanding that tuples are contiguous memory blocks (2 words + element sizes) explains why setelement must copy

# Key Properties

1. `setelement/3` always copies the entire tuple (without compiler optimization)
2. In a loop, this means O(n * tuple_size) total copying work
3. The compiler can coalesce consecutive `setelement/3` calls into one copy
4. Coalescing requires compile-time-known tuple size
5. Coalescing requires literal integer indices (not variables)
6. No intervening expressions allowed between coalesced calls
7. Each intermediate tuple must only feed into the next `setelement/3`
8. Before OTP 26, descending index order was also required

# Construction / Recognition

## Recognizing the Optimization Opportunity

1. Find multiple consecutive `setelement/3` calls on the same tuple
2. Verify the tuple size is known at compile time (e.g., via a guard like `tuple_size(T0) =:= 9`)
3. Verify indices are integer literals
4. Verify no side-effecting expressions between calls
5. Verify each intermediate result feeds only into the next call

## Recognizing the Anti-Pattern

1. Look for `setelement/3` inside a loop (recursion or list comprehension)
2. Each iteration creates a full tuple copy
3. Consider restructuring to build the tuple once or use a different data structure

# Context & Application

This optimization is most relevant when updating multiple fields of a record (which compiles to a tuple) in a single function clause. The Erlang compiler automatically recognizes the coalescing opportunity when conditions are met.

**Typical contexts:**
- Record updates that modify multiple fields simultaneously
- State transformation functions in OTP behaviors
- Any code that performs multiple tuple element updates in sequence

Record syntax (e.g., `State#state{field1 = V1, field2 = V2}`) typically generates coalesced `setelement/3` calls automatically.

# Examples

**Coalesced setelement/3** (source: "Common Caveats," section "setelement/3"):

```erlang
multiple_setelement(T0) when tuple_size(T0) =:= 9 ->
    T1 = setelement(5, T0, new_value),
    T2 = setelement(7, T1, foobar),
    setelement(9, T2, bar).
```

The compiler replaces the three `setelement/3` calls with code that copies the tuple once and updates elements at positions 5, 7, and 9.

# Relationships

## Related

- **pattern-matching-optimization** -- Another compiler optimization for Erlang code

# Common Errors

- **Error**: Using `setelement/3` in a loop to update one element per iteration
  **Correction**: Accumulate all updates and apply them in a single batch, or build a new tuple directly

- **Error**: Using variable indices in `setelement/3` calls and expecting coalescing
  **Correction**: Indices must be integer literals for the compiler to coalesce

# Common Confusions

- **Confusion**: Believing record update syntax avoids the copying overhead
  **Clarification**: Record updates compile to `setelement/3` calls, but the compiler typically coalesces them, so multi-field record updates are usually efficient

- **Confusion**: Thinking `setelement/3` modifies the tuple in place
  **Clarification**: Erlang data is immutable; `setelement/3` always creates a new tuple (the compiler may optimize away redundant intermediate copies, but the semantics remain immutable)

# Source Reference

"Common Caveats," section "setelement/3" and subsection "Compiler optimizations of setelement/3." The source provides the coalescing example and lists all four conditions required for optimization in OTP 26+, plus the additional descending-index requirement for pre-OTP 26.

# Verification Notes

- Definition: Direct from source -- "setelement/3 copies the tuple it modifies"
- Coalescing conditions (4 items): All explicitly listed in source for OTP 26+
- Pre-OTP 26 condition: Explicitly noted in source
- Example: Verbatim from source
- Confidence: HIGH -- explicit documentation with detailed conditions from official OTP guide
