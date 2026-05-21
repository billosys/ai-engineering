---
# === CORE IDENTIFICATION ===
concept: Send Operator
slug: send-operator

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
section: "Send"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "! operator"
  - "bang operator"
  - "message send"

# === TYPED RELATIONSHIPS ===
prerequisites: []
extends: []
related:
  - receive-expression
  - operator-precedence
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do I send messages between processes?"
  - "What does the ! operator do in Erlang?"
  - "What happens if I send a message to a non-existing process?"
---

# Quick Definition

The send operator (`!`) sends a message to a process and returns the message as its value. It is the fundamental mechanism for inter-process communication in Erlang.

# Core Definition

The expression `Expr1 ! Expr2` sends the value of `Expr2` as a message to the process specified by `Expr1`. The value of `Expr2` is also the return value of the expression. `Expr1` must evaluate to a pid, an alias (reference), a port, a registered name (atom), or a tuple `{Name, Node}` where `Name` is an atom and `Node` is a node name (Erlang Reference Manual, "Send" section).

# Prerequisites

This is a foundational concept with no prerequisites within this source.

# Key Properties

1. The return value of the send expression is the value of `Expr2` (the message itself).
2. `Expr1` can be a pid, alias (reference), port, registered name (atom), or `{Name, Node}` tuple.
3. Sending to a registered name that does not exist causes a `badarg` runtime error.
4. Sending to a reference never fails, even if the reference is no longer (or never was) an alias.
5. Sending to a pid never fails, even if the pid identifies a non-existing process.
6. Distributed message sending (to `{Name, Node}` or a remote pid) also never fails.

# Construction / Recognition

## To Send a Message:
1. Identify the target process (by pid, registered name, alias, or `{Name, Node}` tuple).
2. Construct the message term (any Erlang term).
3. Use the `!` operator: `Target ! Message`.

## To Recognize:
1. Look for the `!` operator between two expressions.
2. The left operand identifies the recipient; the right operand is the message.

# Context & Application

The send operator is one of the three fundamental concurrency primitives in Erlang (alongside `spawn` and `receive`). It is used for all inter-process communication, including both local and distributed messaging. Since sending to a pid or reference never fails, the sender cannot know from the send alone whether the message was received; confirmation requires explicit reply messages.

# Examples

**Example 1** (Send section): Sending a busy notification to another process:

```erlang
B ! {busy, self()}
```

**Example 2** (Receive section): A timer process sends a timeout message:

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
- No prerequisites within this source.

## Enables
- **receive-expression** — Messages sent with `!` are retrieved with `receive`.

## Related
- **operator-precedence** — The `!` operator has specific precedence (right-associative, same level as `=`).

## Contrasts With
- No direct contrasts within this source.

# Common Errors

- **Error**: Sending to a registered name that has not been registered.
  **Correction**: Ensure the name is registered with `register/2` before sending, or use the pid directly.

- **Error**: Assuming the send operator will raise an error when the target process is dead.
  **Correction**: Sending to a pid never fails. Use monitors or links to detect process death.

# Common Confusions

- **Confusion**: Believing that a successful send means the message was received.
  **Clarification**: The send operator returns the message value regardless of whether the recipient exists or processes it. Use explicit acknowledgment patterns for confirmation.

- **Confusion**: Thinking the send operator blocks until the message is delivered.
  **Clarification**: The send operator is asynchronous; it returns immediately.

# Source Reference

Erlang Reference Manual, "Expressions" chapter, "Send" section.

# Verification Notes

- Definition source: Direct from source text
- Confidence rationale: High — the source explicitly defines the send operator syntax, semantics, and edge cases
- Uncertainties: None
- Cross-reference status: Related concepts (receive-expression, operator-precedence) verified against planned extractions
