---
# === CORE IDENTIFICATION ===
concept: Receive Expression
slug: receive-expression

# === CLASSIFICATION ===
category: processes-concurrency
subcategory: message-passing
tier: foundational

# === PROVENANCE ===
source: "Erlang Reference Manual"
source_slug: otp-reference-manual
authors: "Ericsson AB"
chapter: "Expressions"
chapter_number: null
pdf_page: null
section: "Receive"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "receive block"
  - "receive...after"
  - "selective receive"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - send-operator
extends: []
related:
  - guard-sequences
  - operator-precedence
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do I receive messages between processes?"
  - "How do I add a timeout to a receive expression?"
  - "What happens if no message matches in a receive?"
---

# Quick Definition

The `receive` expression retrieves a message from the process mailbox by pattern matching against clauses. It suspends the process until a matching message arrives or an optional timeout expires.

# Core Definition

The `receive` expression searches the message queue for a message matching one of the patterns in its clauses. Patterns are matched against each message from top to bottom, and the first matching message from the start of the queue is selected. When a match succeeds and the optional guard sequence is true, the matching message is fetched from the queue and the corresponding body is evaluated. All other messages remain unchanged in the queue. The return value of the body is the return value of the `receive` expression. `receive` never fails; execution is suspended, possibly indefinitely, until a matching message arrives (Erlang Reference Manual, "Receive" section).

# Prerequisites

- **send-operator** — Messages must be sent (via `!`) before they can be received; understanding the send mechanism is essential for understanding receive.

# Key Properties

1. Pattern matching is performed sequentially from top clause to bottom clause.
2. Messages in the queue are checked from the start of the queue for each clause.
3. When a message matches and the guard is true, it is removed from the queue; other messages remain.
4. `receive` never fails — it suspends until a match is found.
5. The time complexity is O(N) where N is the number of messages preceding the matching message.
6. An optimization exists for matching on a freshly created reference — only messages received after reference creation need inspection.
7. The `after` clause provides a timeout mechanism with a value in milliseconds (0 to 4294967295) or `infinity`.
8. A `receive...after` with no clauses and only a timeout can be used as a simple timer.

# Construction / Recognition

## To Construct:
1. Write the `receive` keyword.
2. Add one or more pattern clauses with optional guards: `Pattern [when Guard] -> Body`.
3. Separate clauses with semicolons.
4. Optionally add an `after ExprT -> BodyT` clause for timeout.
5. End with the `end` keyword.

## To Recognize:
1. Look for the `receive ... end` block structure.
2. May contain an `after` clause for timeout behavior.

# Context & Application

`receive` is one of Erlang's three fundamental concurrency primitives. It implements selective receive: the process can choose which messages to handle based on pattern matching, leaving unmatched messages in the queue for later processing. This is central to the actor model of concurrency used in Erlang.

**Performance consideration**: If the patterns only match specific messages and the queue is large, `receive` can become expensive (O(N)). The compiler optimizes the case where a freshly created reference is matched in all clauses.

# Examples

**Example 1** (Receive section): Waiting for specific messages:

```erlang
wait_for_onhook() ->
    receive
        onhook ->
            disconnect(),
            idle();
        {connect, B} ->
            B ! {busy, self()},
            wait_for_onhook()
    end.
```

**Example 2** (Receive section): Receive with timeout:

```erlang
wait_for_onhook() ->
    receive
        onhook ->
            disconnect(),
            idle();
        {connect, B} ->
            B ! {busy, self()},
            wait_for_onhook()
    after
        60000 ->
            disconnect(),
            error()
    end.
```

**Example 3** (Receive section): Using receive as a timer (no pattern clauses):

```erlang
timer(Pid) ->
    receive
    after
        5000 ->
            Pid ! timeout
    end.
```

# Relationships

## Builds Upon
- **send-operator** — Receives messages that were sent via the `!` operator.

## Enables
- No directly dependent concepts in this extraction.

## Related
- **guard-sequences** — Guard sequences can be used in receive clauses to constrain matching.

## Contrasts With
- No direct contrasts within this source.

# Common Errors

- **Error**: Forgetting to handle unexpected messages, causing the mailbox to grow unboundedly.
  **Correction**: Add a catch-all clause or periodically flush the mailbox.

- **Error**: Using `after 0` assuming it is cheap with a large mailbox.
  **Correction**: `after 0` still requires scanning the entire mailbox if no message matches, making it O(N).

- **Error**: Setting a timeout value outside the allowed range (0 to 4294967295 or `infinity`).
  **Correction**: Use values within the allowed range; `infinity` makes the process wait indefinitely.

# Common Confusions

- **Confusion**: Believing `receive` processes messages in order of arrival and removes all checked messages.
  **Clarification**: `receive` performs selective matching — only the first matching message is removed; all others remain in the queue in their original order.

- **Confusion**: Thinking `after 0` means "don't wait at all with zero cost."
  **Clarification**: `after 0` means the timeout triggers immediately if no match exists, but the entire queue must be scanned first.

# Source Reference

Erlang Reference Manual, "Expressions" chapter, "Receive" section.

# Verification Notes

- Definition source: Direct from source text
- Confidence rationale: High — explicit syntax and semantics provided with multiple examples
- Uncertainties: None
- Cross-reference status: Related concepts verified against planned extractions
