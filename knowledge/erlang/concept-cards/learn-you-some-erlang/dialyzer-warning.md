---
concept: Dialyzer Warning
slug: dialyzer-warning
category: tooling
subcategory: static-analysis
tier: advanced
source: "Learn You Some Erlang for Great Good!"
source_slug: learn-you-some-erlang
authors: "Fred Hébert"
chapter: "Type Specifications and Dialyzer"
chapter_number: 30
pdf_page: null
section: "Type Inference and Discrepancies"
extraction_confidence: high
aliases:
  - "no local return"
  - "discrepancy warning"
prerequisites:
  - dialyzer
  - success-typing
related:
  - type-specification
contrasts_with: []
answers_questions:
  - "What do common Dialyzer warnings mean?"
  - "What does 'has no local return' mean?"
---

# Dialyzer Warning

## Quick Definition

A Dialyzer warning is a discrepancy message Dialyzer emits when analysis proves a piece of code cannot work — such as "has no local return" or "breaks the contract."

## Core Definition

When Dialyzer's analysis proves a discrepancy, it emits a warning naming the file, line, and nature of the problem. The most common is `Function Name/Arity has no local return` — emitted whenever a function provably does not return (other than perhaps raising an exception) because a function it calls trips the type-error detector or raises an exception. When this happens, the set of possible return values is empty, and the "no local return" error propagates up to callers. Other warnings report calls that "will never return since [they differ] ... from the success typing arguments," calls that "break the contract" of a `-spec`, patterns that "can never match," contracts with "overlapping domains," and functions that "will never be called" (Chapter 30, "Type Inference and Discrepancies" and "Typing Functions").

## Prerequisites

- **Dialyzer** — Warnings are Dialyzer's output
- **Success typing** — Warnings are emitted only when a use violates the inferred success typing

## Key Properties

1. `Function Name/Arity has no local return` — the function provably never returns a value; propagates to callers
2. `The call ... will never return since it differs ... from the success typing arguments` — an argument's type contradicts the inferred typing
3. `The call ... breaks the contract` — a call violates a user-supplied `-spec`
4. `The pattern ... can never match the type ...` — a pattern is unreachable given the inferred type
5. `Overloaded contract has overlapping domains` — alternative `-spec` clauses have overlapping input sets and are ignored
6. `Function ... will never be called` — code is unreachable
7. Warnings are emitted only for discrepancies guaranteed to be real (Dialyzer never cries wolf)

## Construction / Recognition

## To Interpret a Warning

1. Read the file, line, and message
2. For "no local return," look for the downstream function that actually trips the error — that root cause propagates upward
3. For "breaks the contract," check whether the `-spec`, the call, or the expected return value is wrong
4. For "overlapping domains," tighten the `-spec` clauses (e.g., replace `list()` with `nonempty_list()`)

## Context & Application

"No local return" is the warning seen most when using Dialyzer; it is rarely the root cause itself — the real problem is in a called function. The chapter walks through interpreting the `fifo_types.erl` warnings: an overlapping-domains warning is fixed by replacing `list()` with `nonempty_list()` (since `list()` includes `[]`), and a "breaks the contract" warning about an improper list is fixed by correcting the call.

## Examples

**Example** (Chapter 30, "Typing Practice"): `fifo_types.erl:16: Overloaded contract has overlapping domains` — the `empty/1` spec uses `list()`, which overlaps `[]`; fixed with `nonempty_list()`.

**Example** (Chapter 30, "Typing Functions"): `cards.erl:15: The call cards:kind({'rubies',4}) breaks the contract (card()) -> 'face' | 'number'`.

## Relationships

## Builds Upon

- **Dialyzer** — Warnings are what Dialyzer produces
- **Success typing** — A warning means a use provably violates the success typing

## Related

- **Type specification** — Several warnings ("breaks the contract," "overlapping domains") arise from `-spec` declarations

## Common Errors

- **Error**: Trying to fix the function named in a "no local return" warning directly
  **Correction**: The named function is usually fine; trace to the called function that actually trips the error

## Common Confusions

- **Confusion**: Reading "no local return" as "this function is unused"
  **Clarification**: It means the function provably cannot return a value (it always crashes/raises); "will never be called" is the separate unreachable-code warning

## Source Reference

Chapter 30: Type Specifications and Dialyzer, sections "Type Inference and Discrepancies," "Typing Functions," and "Typing Practice."

## Verification Notes

- Definition: Synthesized from the warning explanations spread across three sections
- Key Properties: Each warning form quoted directly from the chapter's Dialyzer output
- Confidence: HIGH — warnings are explicitly shown and explained
- Cross-references: verified against planned cards in this extraction
