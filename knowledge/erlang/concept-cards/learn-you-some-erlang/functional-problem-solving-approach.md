---
concept: Functional Problem-Solving Approach
slug: functional-problem-solving-approach
category: functions-pattern-matching
subcategory: methodology
tier: intermediate
source: "Learn You Some Erlang for Great Good!"
source_slug: learn-you-some-erlang
authors: "Fred Hébert"
chapter: "Functionally Solving Problems"
chapter_number: 8
pdf_page: null
section: "Heathrow to London"
extraction_confidence: high
aliases:
  - "decomposition method"
  - "solve-by-hand-first approach"
prerequisites:
  - fold
  - pattern-matching
  - tail-recursion
extends: []
related:
  - reverse-polish-notation-calculator
contrasts_with: []
answers_questions:
  - "How do I approach solving a problem functionally in Erlang?"
  - "How do I choose an accumulator for a fold?"
---

# Functional Problem-Solving Approach

## Quick Definition

A methodology for solving problems in functional Erlang: understand and solve the problem by hand first, break it into small individually-solvable parts, then express the iteration as a fold with a carefully chosen accumulator.

## Core Definition

Chapter 8 presents two worked examples (an RPN calculator and the "Heathrow to London" shortest-path problem) and distills a general method. The key lessons stated in the chapter: do not start coding before you fully understand the problem; solve it by hand to discover the logic; break the problem into small parts solved individually and then composed; prefer abstractions like maps and folds because they decouple your logic from the underlying data structure; and write a few tests so behavior stays stable across implementation changes (Hébert, ch. 8, "Heathrow to London," closing discussion).

For folds specifically, the chapter recommends choosing the accumulator by "imagining yourself in the middle of the algorithm while it runs" and asking what state you would need to make the next decision.

## Prerequisites

- **Fold** — The recommended way to express single-pass iteration over a data structure
- **Pattern matching** — Used to destructure inputs (e.g. grouping a flat list into triples)
- **Tail recursion** — Folds accumulate; results built in reverse must be reversed at the end

## Key Properties

1. Understand the problem fully before writing code
2. Solve a small base case (e.g. one tuple) by hand first, then generalize toward it — the recursion mindset
3. Decompose into small parts that are solved and tested individually, then composed
4. Choose the fold accumulator by imagining the algorithm mid-run and asking what state is needed
5. Folds generalize beyond lists — to trees, dicts, arrays, database tables — so logic stays portable
6. Accumulating in a tail-recursive fold builds results backward; reverse the final result
7. A few tests guard against regressions when the implementation changes

## Construction / Recognition

## To Apply the Approach

1. Write down a precise specification and stick to it
2. Solve the simplest instance (the base case) by hand
3. Extend the example and find how each step reduces toward the base case
4. Identify the per-element function and the accumulator needed for a fold
5. Implement helpers (parsing, grouping) as small tail-recursive functions
6. Compose them and verify with assertion-based tests

## Examples

> **Heathrow to London** (ch. 8): the road map is parsed into `{A,B,X}` triples; the accumulator is `{{DistA,PathA},{DistB,PathB}}`, chosen by imagining the algorithm partway through. `shortest_step/2` plugs into `lists:foldl/2`.
>
> **Accumulator reasoning** (ch. 8): "imagine that we're currently trying to find the shortest path of the second triple... to decide which path is best, we need the result from the previous triple" — this reveals what the accumulator must carry.
>
> **Backward accumulation** (ch. 8): paths are consed as `[{x,X},{b,B}|PathB]` and `lists:reverse/1` is applied at the end.

## Relationships

## Builds Upon

- **Fold** — The central abstraction the methodology recommends

## Related

- **Reverse Polish Notation calculator** — The chapter's first worked example of the method

## Common Errors

- **Error**: Coding before understanding the problem
  **Correction**: Solve it by hand first; diving in early "usually ends up creating more work"
- **Error**: Forgetting to reverse a list accumulated in a fold
  **Correction**: Tail-recursive accumulation reverses order; apply `lists:reverse/1` at the end

## Common Confusions

- **Confusion**: Thinking folds only work on lists
  **Clarification**: Folds are a general accumulator-over-structure concept; they apply to trees, dicts, arrays, and database tables
- **Confusion**: Believing recursion must be written by hand for each problem
  **Clarification**: Most iteration can be expressed with existing higher-order functions like `foldl`

## Source Reference

Chapter 8, "Functionally Solving Problems," section "Heathrow to London" (subsections "Solving the Problem Recursively," "Writing the Code") and the chapter's closing paragraphs.

## Verification Notes

- Methodology points: synthesized from the chapter's explicit advice in the Heathrow example and closing remarks
- Accumulator-choosing heuristic: quoted directly from ch. 8
- Confidence: HIGH — the chapter states this method explicitly
- Cross-references: `fold`, `pattern-matching`, `tail-recursion` owned by Agent 1
