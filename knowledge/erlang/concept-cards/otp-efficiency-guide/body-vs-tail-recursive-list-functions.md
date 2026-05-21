---
concept: Body-Recursive vs Tail-Recursive List Functions
slug: body-vs-tail-recursive-list-functions
category: data-structures
subcategory: list-operations
tier: intermediate
source: "Erlang Efficiency Guide"
source_slug: otp-efficiency-guide
authors: "Ericsson/OTP Team"
chapter: "List Handling"
chapter_number: null
pdf_page: null
section: "Recursive List Functions"
extraction_confidence: high
aliases:
  - "body recursion vs tail recursion"
  - "recursive list function performance"
  - "tail recursion myth"
prerequisites:
  - list-construction-efficiency
extends: []
related:
  - list-comprehension-optimization
  - append-operator-efficiency
contrasts_with: []
answers_questions:
  - "How do body-recursive and tail-recursive list functions compare in performance?"
---

# Quick Definition

In modern Erlang, body-recursive and tail-recursive list functions that construct lists have comparable performance. The traditional advice to always prefer tail recursion is outdated. For list-constructing functions, write for clarity first and measure before optimizing. However, for functions that do not construct a list (e.g., summing), tail recursion is still preferred because it uses constant stack space.

# Core Definition

There are two basic ways to write a function that traverses a list and produces a new list: body-recursive (which conses the result in the recursive call) and tail-recursive (which accumulates in reverse and calls `lists:reverse/1` at the end). In early versions of Erlang the tail-recursive function would typically be more efficient. In modern versions of Erlang, there is usually not much difference in performance between a body-recursive list function and tail-recursive function that reverses the list at the end. Therefore, concentrate on writing beautiful code and forget about the performance of your list functions. In the time-critical parts of your code, measure before rewriting your code (Ericsson/OTP Team, "List Handling," section "Recursive List Functions").

The source explicitly notes an important distinction: this applies only to list functions that construct lists. A tail-recursive function that does not construct a list runs in constant space, while the corresponding body-recursive function uses stack space proportional to the length of the list. For non-list-constructing functions (like summing), tail recursion is still preferred.

# Prerequisites

- **list-construction-efficiency** -- Understanding how lists are built (prepend + reverse) is needed to understand why the two styles are comparable

# Key Properties

1. Body-recursive style: conses the new element directly in the recursive call (`[H+42 | f(T)]`)
2. Tail-recursive style: accumulates in reverse order, reverses at the end (`f(T, [H+42|Acc])`)
3. In modern Erlang, both styles have similar performance for list-constructing functions
4. The historical preference for tail recursion in all cases is outdated
5. For non-list-constructing functions (e.g., summing), tail recursion IS preferred (constant space)
6. Body-recursive non-constructing functions use O(n) stack space
7. Measure before optimizing -- write for clarity first

# Construction / Recognition

## Body-Recursive Style

```erlang
f([H|T]) ->
    [transform(H) | f(T)];
f([]) ->
    [].
```

Characteristics: No accumulator parameter. Result is built by consing onto the recursive call. Stack grows with list length.

## Tail-Recursive Style

```erlang
f(List) -> f(List, []).

f([H|T], Acc) ->
    f(T, [transform(H) | Acc]);
f([], Acc) ->
    lists:reverse(Acc).
```

Characteristics: Extra accumulator parameter. Result built in reverse. `lists:reverse/1` called at the end. Constant stack space.

## Choosing Between Them

1. For list-constructing functions: choose whichever is clearer for the specific case
2. For non-list-constructing functions (accumulating a value, not building a list): use tail recursion
3. When in doubt: measure with realistic data before rewriting

# Context & Application

The equivalence of body and tail recursion for list construction is a common source of outdated advice in the Erlang community. Many style guides and older tutorials insist on tail recursion in all cases, but the OTP Efficiency Guide explicitly debunks this for list-constructing functions.

**Typical contexts:**
- Code review discussions about recursion style
- Performance optimization of list-processing code
- Choosing between clarity and supposed efficiency

**External reference:** The source points to Fred Hebert's article "Erlang's Tail Recursion is Not a Silver Bullet" for a thorough discussion.

**Important caveat:** The equivalence only holds for functions that construct lists. For functions that reduce a list to a single value (sum, count, max, etc.), tail recursion remains important because it uses constant stack space.

# Examples

**Body-recursive list construction** (source: "Recursive List Functions" section):

```erlang
%% Add 42 to each integer in the list.
add_42_body([H|T]) ->
    [H + 42 | add_42_body(T)];
add_42_body([]) ->
    [].
```

**Tail-recursive list construction** (source: same section):

```erlang
%% Add 42 to each integer in the list.
add_42_tail(List) ->
    add_42_tail(List, []).

add_42_tail([H|T], Acc) ->
    add_42_tail(T, [H + 42 | Acc]);
add_42_tail([], Acc) ->
    lists:reverse(Acc).
```

Both have similar performance in modern Erlang.

**DO NOT** -- Body-recursive sum (non-constructing, uses O(n) stack) (source: same section):

```erlang
recursive_sum([H|T]) -> H+recursive_sum(T);
recursive_sum([])    -> 0.
```

**DO** -- Tail-recursive sum (non-constructing, constant space) (source: same section):

```erlang
sum(L) -> sum(L, 0).

sum([H|T], Sum) -> sum(T, Sum + H);
sum([], Sum)    -> Sum.
```

For the summing case, tail recursion is explicitly preferred because no list is being constructed and the body-recursive version uses stack proportional to the list length.

# Relationships

## Related

- **list-comprehension-optimization** -- List comprehensions compile to body-recursive form
- **append-operator-efficiency** -- Relevant when considering how the accumulator-based (tail-recursive) pattern builds lists

# Common Errors

- **Error**: Blindly rewriting body-recursive list functions to tail-recursive form for "performance"
  **Correction**: In modern Erlang, both have similar performance for list construction. Measure before rewriting.

- **Error**: Using body recursion for a non-list-constructing function (e.g., summing)
  **Correction**: For functions that accumulate a single value (not a list), tail recursion is preferred because it uses constant stack space.

# Common Confusions

- **Confusion**: Believing tail recursion is always faster than body recursion
  **Clarification**: For list-constructing functions, the performance difference is negligible in modern Erlang. The tail-recursive version has the overhead of `lists:reverse/1`. The body-recursive version uses more stack but avoids the reversal.

- **Confusion**: Applying the "tail recursion doesn't matter" advice to non-list functions
  **Clarification**: The equivalence only applies to functions that construct lists. For functions that do NOT construct a list (summing, counting, etc.), tail recursion is still important because it uses constant space vs. O(n) stack.

- **Confusion**: Thinking list comprehensions are tail-recursive
  **Clarification**: List comprehensions compile to body-recursive form. This is fine because, as noted, both styles have similar performance for list construction.

# Source Reference

"List Handling," section "Recursive List Functions." The source provides paired body-recursive and tail-recursive examples for list construction (`add_42`), a DO NOT/DO pair for non-constructing functions (`recursive_sum` vs `sum`), and an explicit Note distinguishing the two cases. Also references Fred Hebert's "Erlang's Tail Recursion is Not a Silver Bullet."

# Verification Notes

- Definition: Directly from source -- "In modern versions of Erlang, there is usually not much difference in performance between a body-recursive list function and tail-recursive function that reverses the list at the end"
- Advice to write for clarity: Directly quoted -- "concentrate on writing beautiful code and forget about the performance of your list functions"
- Measure advice: Directly quoted -- "In the time-critical parts of your code, measure before rewriting your code"
- Non-constructing caveat: From explicit Note box -- "A tail-recursive function that does not construct a list runs in constant space"
- All examples directly from source
- External reference to Fred Hebert's article explicitly cited in source
- Confidence: HIGH -- explicit guidance with paired examples and a clear caveat in official OTP documentation
