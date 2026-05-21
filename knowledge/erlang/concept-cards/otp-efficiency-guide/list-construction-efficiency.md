---
concept: List Construction Efficiency
slug: list-construction-efficiency
category: data-structures
subcategory: list-operations
tier: foundational
source: "Erlang Efficiency Guide"
source_slug: otp-efficiency-guide
authors: "Ericsson/OTP Team"
chapter: "List Handling"
chapter_number: null
pdf_page: null
section: "Creating a List"
extraction_confidence: high
aliases:
  - "efficient list construction"
  - "list building"
  - "list accumulation"
prerequisites: []
extends: []
related:
  - append-operator-efficiency
  - list-comprehension-optimization
  - body-vs-tail-recursive-list-functions
  - deep-vs-flat-lists
contrasts_with: []
answers_questions:
  - "How do I efficiently build a list in Erlang?"
---

# Quick Definition

Lists in Erlang can only be built efficiently by prepending elements to the beginning. Using the `++` operator with a growing accumulator on the left side creates copies on every iteration, resulting in quadratic time complexity. The correct pattern is to prepend with `[H|Acc]` and reverse at the end.

# Core Definition

Lists can only be built starting from the end and attaching list elements at the beginning. If you use the `++` operator, a new list is created that is a copy of the elements in the left operand, followed by the right operand. When recursing and building a list, it is important to ensure that you attach new elements to the beginning of the list. In this way, you will build one list, not hundreds or thousands of copies of the growing result list (Ericsson/OTP Team, "List Handling," section "Creating a List").

# Prerequisites

This is a foundational concept with no prerequisites within this source.

# Key Properties

1. Lists are singly-linked: elements can only be efficiently added at the head
2. The `++` operator copies its entire left operand
3. Appending to the end with `++` in a loop produces O(n^2) time complexity
4. Prepending with `[H|Acc]` is O(1) per element
5. Building in reverse order and calling `lists:reverse/1` at the end is the idiomatic pattern
6. `lists:reverse/1` is a BIF implemented in C, making it very efficient

# Construction / Recognition

## The Efficient Pattern

1. Initialize an accumulator as an empty list: `[]`
2. In each recursive step, prepend the new element: `[Current|Acc]`
3. When done, reverse the accumulator: `lists:reverse(Acc)`

## Recognizing the Anti-Pattern

1. Look for `++` with the growing result on the left side inside a loop
2. `Fibs ++ [Current]` -- the growing list `Fibs` is copied on every iteration
3. Any pattern where elements are appended to the end of a growing list

# Context & Application

This is the most fundamental list construction rule in Erlang. Because Erlang lists are singly-linked (cons cells pointing forward), adding to the end requires traversing and copying the entire list. Adding to the beginning is a single cons cell allocation.

**Typical contexts:**
- Building result lists in recursive functions
- Accumulating elements from a data source
- Transforming input lists into output lists

The build-in-reverse-then-reverse pattern is so universal in Erlang that it is considered the standard idiom, not a workaround.

# Examples

**DO NOT** -- Appending with `++` copies the accumulator on every iteration (source: "Creating a List" section):

```erlang
bad_fib(N) ->
    bad_fib(N, 0, 1, []).

bad_fib(0, _Current, _Next, Fibs) ->
    Fibs;
bad_fib(N, Current, Next, Fibs) ->
    bad_fib(N - 1, Next, Current + Next, Fibs ++ [Current]).
```

Each iteration creates a new list that is one element longer than the previous, copying all existing elements.

**DO** -- Prepend and reverse (source: same section):

```erlang
tail_recursive_fib(N) ->
    tail_recursive_fib(N, 0, 1, []).

tail_recursive_fib(0, _Current, _Next, Fibs) ->
    lists:reverse(Fibs);
tail_recursive_fib(N, Current, Next, Fibs) ->
    tail_recursive_fib(N - 1, Next, Current + Next, [Current|Fibs]).
```

Each iteration prepends one element (O(1)). The final `lists:reverse/1` is O(n), giving O(n) total.

# Relationships

## Related

- **append-operator-efficiency** -- Detailed analysis of the `++` operator's copying behavior
- **list-comprehension-optimization** -- List comprehensions are compiled to efficient list construction
- **body-vs-tail-recursive-list-functions** -- Two styles of list construction with similar performance in modern Erlang
- **deep-vs-flat-lists** -- Avoiding unnecessary flattening is another list efficiency concern

# Common Errors

- **Error**: Using `Acc ++ [NewElement]` in a recursive loop
  **Correction**: Use `[NewElement|Acc]` and call `lists:reverse/1` at the end

- **Error**: Forgetting to reverse the accumulator at the end
  **Correction**: Always call `lists:reverse(Acc)` in the base case when order matters

# Common Confusions

- **Confusion**: Thinking `lists:reverse/1` is expensive and should be avoided
  **Clarification**: `lists:reverse/1` is a BIF implemented in C and is O(n). The cost of one reversal at the end is negligible compared to the O(n^2) cost of repeated `++` appending.

- **Confusion**: Believing that Erlang lists support efficient random access or append
  **Clarification**: Erlang lists are singly-linked cons cells. Only head access and head prepending are O(1). All other access patterns are O(n).

# Source Reference

"List Handling," section "Creating a List." The source provides an explicit Erlang implementation of `++` (showing copy behavior), a DO NOT example (`bad_fib`), and a DO example (`tail_recursive_fib`) demonstrating the prepend-and-reverse pattern.

# Verification Notes

- Definition: Directly from source -- "Lists can only be built starting from the end and attaching list elements at the beginning"
- Copy behavior of `++`: Explicitly shown with an Erlang implementation of `append/2`
- Anti-pattern description: Explicitly stated -- "Here more than one list is built. In each iteration step a new list is created that is one element longer"
- Both examples taken directly from source
- Confidence: HIGH -- explicit DO/DO NOT examples with clear explanation in official OTP documentation
