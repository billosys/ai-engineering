---
# === CORE IDENTIFICATION ===
concept: Recursion
slug: recursion

# === CLASSIFICATION ===
category: functions-pattern-matching
subcategory: control-flow
tier: foundational

# === PROVENANCE ===
source: "Programming Erlang, Second Edition"
source_slug: programming-erlang
authors: Joe Armstrong
chapter: "Modules and Functions"
chapter_number: 4
pdf_page: null
section: "Simple List Processing"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - recursive function
  - tail recursion
  - tail-call optimization

# === TYPED RELATIONSHIPS ===
prerequisites:
  - function
  - function-clause
  - list
extends: []
related:
  - accumulator
  - server-loop
  - pattern-matching
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do I process a list in Erlang?"
  - "What is tail recursion?"
---

# Quick Definition

Recursion is a function calling itself, typically with a base-case clause and a recursive clause. It is Erlang's standard way to process lists and to write loops; tail-recursive calls run in constant space.

# Core Definition

Erlang has no `for` or `while` loop; iteration is expressed by recursion. A recursive list function "works by a case analysis of the argument": one clause handles the nonempty list `[Head|Tail]` — it does something with the head and "then calls itself to process the tail of the list" — and a second clause handles the empty list `[]` as the base case (Chapter 4, "Back to Shopping"). The book traces `sum([1,3,10])` step by step down to `1 + 3 + 10 + sum([])` and then `+ 0` (Chapter 4, "Simple List Processing"). When the recursive call is the *last* action of a clause, Erlang applies *tail-call optimization*: "this function will run in constant space" — which is why an infinite server loop never exhausts the stack (Chapter 2, "The File Server Process").

# Prerequisites

- **Function** — Recursion is a function that calls itself.
- **Function clause** — Recursive functions use a base-case clause and a recursive clause.
- **List** — The canonical recursive structure: process the head, recurse on the tail.

# Key Properties

1. A recursive function calls itself.
2. It typically has a base-case clause and a recursive clause.
3. List recursion processes the head and recurses on the tail until `[]` is reached.
4. The base case (e.g., `[]`) stops the recursion.
5. When the self-call is the last action, tail-call optimization makes it run in constant space.
6. Recursion replaces `for`/`while` loops, which Erlang does not have.

# Construction / Recognition

## To Write a Recursive List Function:
1. Write a clause matching `[H|T]` that handles `H` and recurses on `T`.
2. Write a base-case clause matching `[]` that returns the terminating value.
3. To run in constant space, make the recursive call the last expression of the clause.

## To Recognize It:
1. A function whose body contains a call to itself.
2. Typically a `[H|T]` clause and a `[]` clause.

# Context & Application

- **Typical contexts**: Iterating over lists; long-lived server loops.
- **Common applications**: `sum/1` totals a list; `map/2` transforms each element; `loop/1` is an infinite server.
- **Historical/stylistic notes**: "We're not going to run out of stack space. Erlang applies a so-called tail-call optimization."

# Examples

**Example 1** (Chapter 4, "Simple List Processing"): `sum([H|T]) -> H + sum(T); sum([]) -> 0.` — the recursive clause adds the head to the recursive sum of the tail; the base clause returns `0`.

**Example 2** (Chapter 2, "The File Server Process"): `loop(Dir)` ends by calling `loop(Dir)`; because that self-call is the last action, tail-call optimization keeps the infinite loop in constant space.

# Relationships

## Builds Upon
- **Function** and **function clause** — Recursion is built from a self-calling, multi-clause function.
- **List** — Lists are the structure most naturally processed by recursion.

## Enables
- **Accumulator** — An accumulator parameter makes recursion single-pass and space-efficient.
- **Server loop** — A tail-recursive loop is the basis of a server process.

## Related
- **Accumulator** — A common refinement of recursive functions.
- **Server loop** — An infinite tail-recursive function.
- **Pattern matching** — Clause patterns separate base case from recursive case.

## Contrasts With
- No directly contrasting concept; Erlang simply has no `for`/`while` loop to contrast with.

# Common Errors

- **Error**: Omitting the base-case clause (e.g., the `[]` clause).
  **Correction**: Always provide a base case, or the recursion never terminates / crashes.

- **Error**: Doing work after the recursive call when constant-space looping is needed.
  **Correction**: Make the recursive call the final expression so tail-call optimization applies.

# Common Confusions

- **Confusion**: Worrying that recursion (especially an infinite loop) will exhaust the stack.
  **Clarification**: Tail-recursive calls run in constant space; a loop whose last action is a self-call is safe.

- **Confusion**: Thinking Erlang needs an explicit loop construct.
  **Clarification**: Erlang has no `for`/`while`; recursion (and higher-order functions) replace them.

# Source Reference

"Programming Erlang, Second Edition," Chapter 4: Modules and Functions, sections "Back to Shopping" and "Simple List Processing"; Chapter 2: A Whirlwind Tour of Erlang, "The File Server Process." EPUB-origin source; no page numbers.

# Verification Notes

- Definition source: Synthesized from Chapter 4 list-processing examples and the Chapter 2 tail-call note.
- Confidence rationale: HIGH — recursion is demonstrated with traced execution and tail-call optimization is explicitly named.
- Uncertainties: The source does not give a single one-sentence definition of "recursion"; the definition is synthesized from consistent usage and the traced `sum` example.
- Cross-reference status: Verified against planned cards.
- Re-extraction notes: Fresh extraction; no pre-existing card.
