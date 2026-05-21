---
concept: Receive Expression
slug: receive-expression
category: processes-concurrency
subcategory: concurrency-primitives
tier: foundational
source: "Learn You Some Erlang for Great Good!"
source_slug: learn-you-some-erlang
authors: "Fred Hébert"
chapter: "The Hitchhiker's Guide to Concurrency"
chapter_number: 10
pdf_page: null
section: "Receiving Messages"
extraction_confidence: high
aliases:
  - "receive"
  - "receive ... end"
prerequisites:
  - process-mailbox
  - pattern-matching
extends: []
related:
  - message-passing
  - receive-timeout
  - selective-receive
contrasts_with: []
answers_questions:
  - "How does a process receive messages?"
  - "How do I spawn a process and send it messages?"
---

# Receive Expression

## Quick Definition

The `receive` expression is the third concurrency primitive: it pulls a message out of the process mailbox by pattern matching. It is syntactically like `case ... of` but matches against mailbox messages and can have guards.

## Core Definition

The `receive` expression is "syntactically similar to `case ... of`. In fact, the patterns work exactly the same way, except they bind variables coming from messages rather than the expression between `case` and `of`." A `receive` can also have guards. Its general syntax is a series of `Pattern when Guard -> Expr` clauses ending with `end`. When a process reaches `receive` and its mailbox is empty, it waits until a matching message arrives; the matched message is removed from the mailbox. To keep serving messages, the receiving function must call itself recursively (tail recursion so the stack does not grow) (Hébert, ch. 10, "Receiving Messages").

## Prerequisites

- **Process mailbox** — `receive` pulls from the mailbox
- **Pattern matching** — `receive` clauses match message patterns

## Key Properties

1. Pulls one message from the mailbox by pattern matching
2. Syntactically like `case ... of`; clauses may have guards
3. If the mailbox is empty (or has no match), the process blocks until a matching message arrives
4. The matched message is removed from the mailbox
5. To handle further messages, the function loops by calling itself, tail-recursively
6. A catch-all `_` clause matches any otherwise-unmatched message

## Construction / Recognition

## To Receive Messages

1. Write `receive` followed by `Pattern -> Expression` clauses
2. Optionally add guards: `Pattern when Guard -> Expression`
3. End with `end`
4. To serve repeatedly, recurse into the loop function in each clause (tail call)
5. Include a `_ -> ...` clause if you want to handle unexpected messages

## Examples

> **General syntax** (ch. 10):
> `receive Pattern1 when Guard1 -> Expr1; Pattern2 -> Expr2 end`
>
> **Dolphin receiver** (ch. 10): `dolphin1/0` matches `do_a_flip`, `fish`, and a catch-all `_`.
>
> **Looping to stay alive** (ch. 10): `dolphin3/0` calls `dolphin3()` after handling a message so the process keeps receiving — and notes the call is tail recursive so it "will not blow the stack."

## Relationships

## Builds Upon

- **Process mailbox** — The source of messages `receive` consumes
- **Pattern matching** — The matching mechanism of each clause

## Related

- **Message passing** — `receive` is the counterpart to the `!` send operator
- **Receive timeout** — The `after` clause that gives `receive` a deadline
- **Selective receive** — Using `receive` to prioritize particular messages

## Common Errors

- **Error**: Not recursing after handling a message, so the process serves only once
  **Correction**: Call the loop function again in each clause to keep receiving
- **Error**: Recursing in a non-tail position, growing the stack
  **Correction**: Make the recursive loop call a tail call

## Common Confusions

- **Confusion**: Thinking `receive` polls and returns immediately if no message
  **Clarification**: Without an `after` clause, `receive` blocks until a matching message arrives

## Source Reference

Chapter 10, "The Hitchhiker's Guide to Concurrency," section "So Long and Thanks for All the Fish!", subsection "Receiving Messages."

## Verification Notes

- Definition, syntax, blocking behavior: directly from ch. 10
- Confidence: HIGH — explicitly defined with examples
