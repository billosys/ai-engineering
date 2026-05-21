---
# === CORE IDENTIFICATION ===
concept: Receive
slug: receive

# === CLASSIFICATION ===
category: processes-concurrency
subcategory: communication
tier: foundational

# === PROVENANCE ===
source: "Programming Erlang, Second Edition"
source_slug: programming-erlang
authors: Joe Armstrong
chapter: "Concurrent Programming"
chapter_number: 12
pdf_page: null
section: "The Concurrency Primitives"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "receive ... end"
  - "receive expression"
  - "receive statement"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - process
  - mailbox
  - pattern-matching
extends: []
related:
  - message-passing
  - selective-receive
  - receive-timeout
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How does a process receive messages?"
  - "What is the syntax of a receive expression?"
  - "How do patterns and guards work in receive?"
---

# Quick Definition

`receive ... end` is the primitive that extracts messages from a process's mailbox by pattern matching. It is the only point at which a process examines its mailbox.

# Core Definition

`receive ... end` "receives a message that has been sent to a process" (Armstrong, "Concurrent Programming," "The Concurrency Primitives"). Its syntax is a series of clauses, each `Pattern [when Guard] -> Expressions`, between `receive` and `end`. "When a message arrives at the process, the system tries to match it against `Pattern1` (with possible guard `Guard1`); if this succeeds, it evaluates `Expressions1`. If the first pattern does not match, it tries `Pattern2`, and so on. If no pattern matches, the message is saved for later processing, and the process waits for the next message." "The patterns and guards used in a receive statement have exactly the same syntactic form and meaning as the patterns and guards that we use when we define a function." The mailbox is examined *only* when a `receive` is evaluated.

# Prerequisites

- **Process** — `receive` operates within a process.
- **Mailbox** — `receive` extracts messages from the process's mailbox.
- **Pattern matching** — Receive clauses match messages with the same patterns and guards used in function definitions.

# Key Properties

1. Syntax: `receive Pattern1 [when Guard1] -> Exprs1; Pattern2 -> Exprs2; ... end`.
2. Clause patterns and guards have the same form and meaning as function clauses.
3. Messages are matched against clauses in order; the first match wins.
4. A message that matches no clause is kept in the mailbox (saved) for later.
5. If no message matches, the process suspends until a new message arrives.
6. The mailbox is only inspected when a `receive` is evaluated.
7. An optional `after Time -> ...` clause adds a timeout.

# Construction / Recognition

## To Construct/Create:
1. Decide which message shapes the process should handle.
2. Write a `receive` clause `Pattern [when Guard] -> Expressions` for each.
3. End with `end`; for a server, the clauses' expressions typically call the loop function again (tail recursion).

## To Identify/Recognize:
1. The `receive` keyword followed by clauses and `end`.
2. A trailing `after Time ->` clause marks a receive with a timeout.

# Context & Application

- **Typical contexts**: Server loops; any process that reacts to incoming messages.
- **Common applications**: Tail-recursive `loop()` functions that `receive` a request, act, and call `loop()` again.
- **Historical/stylistic notes**: A concurrent-program template starts with a `receive` loop matching `Any` and printing it, then patterns are added as the program grows.

# Examples

**Example 1** ("The Concurrency Primitives"): The `area_server0` `loop/0` uses `receive {rectangle, Width, Ht} -> ...; {square, Side} -> ... end` to handle two message shapes.

**Example 2** ("Introducing Client-Server"): A receive clause `{From, {rectangle, Width, Ht}} -> From ! Width * Ht, loop()` matches a request and replies to `From`.

**Example 3** ("A Concurrent Program Template"): A development loop `receive Any -> io:format("Received:~p~n",[Any]), loop() end` prints any unmatched message.

# Relationships

## Builds Upon
- **Process** and **Mailbox** — `receive` reads the process's mailbox.
- **Pattern matching** — Receive clauses are pattern-matched.

## Enables
- **Selective receive** — The clause-by-clause matching, with saving of unmatched messages, *is* selective receive.
- **Receive with a timeout** — The `after` clause extends `receive`.

## Related
- **Message passing** — `receive` consumes the messages that `!` sends.

## Contrasts With
- None.

# Common Errors

- **Error**: Sending a message that matches no `receive` clause, so it sits unread in the mailbox forever.
  **Correction**: Add a catch-all clause (e.g. `{From, Other} -> ...`) to ensure every message is received.

- **Error**: Calling another function *after* the recursive loop call inside a receive clause.
  **Correction**: Make the loop call the last expression (tail-recursive) so the process loops without growing the stack.

# Common Confusions

- **Confusion**: Thinking `receive` continuously scans the mailbox in the background.
  **Clarification**: The mailbox is examined only when a `receive` expression is evaluated.

- **Confusion**: Believing a non-matching message is discarded.
  **Clarification**: It is kept in the mailbox (saved) and rechecked on later `receive` calls.

# Source Reference

Chapter 12: "Concurrent Programming," sections "The Concurrency Primitives," "Introducing Client-Server," and "Selective Receive." EPUB source — no page numbers.

# Verification Notes

- Definition source: Direct quotes of the `receive` description from "The Concurrency Primitives."
- Confidence rationale: HIGH — the primitive's syntax and semantics are defined explicitly.
- Uncertainties: None.
- Cross-reference status: Canonical slugs `process`, `mailbox`, `pattern-matching` used; verified.
- Re-extraction notes: Fresh extraction; new card (no prior file).
