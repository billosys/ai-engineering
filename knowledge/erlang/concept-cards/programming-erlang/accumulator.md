---
# === CORE IDENTIFICATION ===
concept: Accumulator
slug: accumulator

# === CLASSIFICATION ===
category: functions-pattern-matching
subcategory: list-processing
tier: intermediate

# === PROVENANCE ===
source: "Programming Erlang, Second Edition"
source_slug: programming-erlang
authors: Joe Armstrong
chapter: "Modules and Functions"
chapter_number: 4
pdf_page: null
section: "Accumulators"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - accumulating parameter

# === TYPED RELATIONSHIPS ===
prerequisites:
  - recursion
  - function-clause
  - list
extends: []
related:
  - case-expression
contrasts_with:
  - list-comprehension

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is an accumulator?"
  - "How do I traverse a list only once when building multiple results?"
---

# Quick Definition

An accumulator is an extra parameter threaded through a recursive function that collects partial results as the recursion proceeds. It lets a function build its output in a single pass over the input.

# Core Definition

In Chapter 4, "Accumulators," Armstrong shows two ways to split a list of integers into odds and evens. The first version uses two separate list comprehensions and so "traverse[s] the list *twice*" — fine for short lists but wasteful for long ones. The accumulator version threads two extra arguments through a recursive helper: `odds_and_evens_acc(L, [], [])` starts the helper with two empty *accumulators*; each recursive call adds the current head onto the appropriate output list — "adding the odd and even arguments onto the appropriate output lists (which are called *accumulators*)." "Now this traverses the list only once." The accumulator version "is more *space efficient* than the version with the `[H || filter(H)]` type construction." Because elements are pushed onto the head, the accumulated lists come out reversed; "if we want the list elements in the same order ... all we have to do is reverse the lists in the final clause" with `lists:reverse`.

# Prerequisites

- **Recursion** — An accumulator is a parameter of a recursive function.
- **Function clause** — The recursive and base-case clauses thread and finally return the accumulator.
- **List** — Accumulators are typically lists being built during a traversal.

# Key Properties

1. An accumulator is an extra parameter that collects partial results during recursion.
2. It is initialized (often to `[]`) when the recursion starts.
3. Each recursive step adds to the accumulator and passes it forward.
4. The base-case clause returns the finished accumulator(s).
5. It lets the function traverse the input only once.
6. It is more space-efficient than a comprehension/filter approach.
7. Because elements are pushed onto the head, the result is reversed — use `lists:reverse` to restore order.

# Construction / Recognition

## To Use an Accumulator:
1. Write a wrapper that calls a helper with the input and the initial accumulator(s) (e.g., `[]`).
2. In the recursive clause, add the processed head to the appropriate accumulator and recurse on the tail.
3. In the base-case clause (`[]`), return the accumulator(s).
4. If order matters, apply `lists:reverse` in the base-case clause.

## To Recognize It:
1. A recursive helper with extra "result-so-far" parameters that grow each call.

# Context & Application

- **Typical contexts**: Recursive list functions that build one or more output lists.
- **Common applications**: `odds_and_evens_acc` splitting a list into odds and evens in one pass.
- **Historical/stylistic notes**: The accumulator pattern is the single-pass, space-efficient alternative to multiple comprehensions or filters.

# Examples

**Example 1** (Chapter 4, "Accumulators"): `odds_and_evens2(L) -> odds_and_evens_acc(L, [], []).` then `odds_and_evens_acc([H|T], Odds, Evens)` adds `H` to `Odds` or `Evens` per `H rem 2`, and `odds_and_evens_acc([], Odds, Evens) -> {Odds, Evens}.` returns the pair.

**Example 2** (Chapter 4, "Accumulators"): Running `odds_and_evens2([1,2,3,4,5,6])` gives `{[5,3,1],[6,4,2]}` — reversed because elements were pushed onto the head; changing the base clause to `{lists:reverse(Odds), lists:reverse(Evens)}` restores original order.

# Relationships

## Builds Upon
- **Recursion** — An accumulator is a parameter carried through recursive calls.
- **Function clause** — Recursive and base clauses thread and return the accumulator.
- **List** — The accumulators are usually lists being constructed.

## Enables
- Single-pass, space-efficient list-building functions.

## Related
- **Case expression** — Often used inside the recursive clause to route an element to the right accumulator.

## Contrasts With
- **List comprehension** — Building several results with separate comprehensions traverses the list multiple times; a single accumulator-based pass traverses it once and uses less space.

# Common Errors

- **Error**: Forgetting that head-prepended accumulators come out reversed.
  **Correction**: Apply `lists:reverse` in the base-case clause if original order is required.

- **Error**: Not initializing the accumulator before the recursion.
  **Correction**: Start the recursive helper with the initial accumulator value(s), typically `[]`.

# Common Confusions

- **Confusion**: Thinking an accumulator-based function is harder to read for no benefit.
  **Clarification**: It traverses the list only once and is more space-efficient than multiple comprehensions — a real benefit for long lists.

- **Confusion**: Expecting accumulator output to be in input order.
  **Clarification**: Pushing onto the head reverses order; reverse the result if order matters.

# Source Reference

"Programming Erlang, Second Edition," Chapter 4: Modules and Functions, section "Accumulators." EPUB-origin source; no page numbers.

# Verification Notes

- Definition source: Synthesized from Chapter 4, "Accumulators," with direct quotation naming the output lists "accumulators."
- Confidence rationale: HIGH — the accumulator pattern is explicitly named and contrasted with the two-pass comprehension version.
- Uncertainties: None.
- Cross-reference status: Verified against planned cards.
- Re-extraction notes: Fresh extraction; no pre-existing card.
