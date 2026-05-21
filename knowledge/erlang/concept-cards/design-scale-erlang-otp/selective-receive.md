---
# === CORE IDENTIFICATION ===
concept: Selective Receive
slug: selective-receive

# === CLASSIFICATION ===
category: processes-concurrency
subcategory: messaging
tier: intermediate

# === PROVENANCE ===
source: "Designing for Scalability with Erlang/OTP"
source_slug: design-scale-erlang-otp
authors: "Francesco Cesarini & Steve Vinoski"
chapter: "Introducing Erlang"
chapter_number: 1
pdf_page: 40
section: "Processes and Message Passing"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - receive expression
  - selective message reception

# === TYPED RELATIONSHIPS ===
prerequisites:
  - processes-and-message-passing
  - pattern-matching
extends: []
related:
  - unhandled-messages
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is selective receive in Erlang?"
  - "Can messages be processed out of arrival order?"
---

# Quick Definition

Selective receive lets a process pattern-match the messages it consumes from its mailbox, so messages are processed in the order they are matched rather than the order they arrived.

# Core Definition

Messages "are processed using the receive expression, which pattern matches on the messages in sequential order. Message reception is selective, meaning that messages are not necessarily processed in the order in which they arrive, but rather the order in which they are matched. Each receive clause selects the message it wants to read from the mailbox using pattern matching" (Cesarini & Vinoski, p. 31). When a `receive` runs, it tries each mailbox message in turn against the clause patterns; a message that matches no clause is left in the mailbox for later retrieval.

# Prerequisites

- **Processes and message passing** — Selective receive operates on a process's mailbox, which is populated by message passing.
- **Pattern matching** — Each `receive` clause selects a message by matching a pattern against it.

# Key Properties

1. A `receive` expression contains one or more pattern clauses.
2. Mailbox messages are tried in arrival order against the clauses.
3. The first message matching some clause is removed and that clause's body runs.
4. A non-matching message stays in the mailbox.
5. Successive `receive` expressions can deliberately consume messages out of arrival order.
6. Selective receive removes the need to anticipate every possible message ordering.

# Construction / Recognition

## To Construct:
1. Write `receive` followed by pattern clauses, each `Pattern -> Body`.
2. End with `end`.
3. To force a specific order, use separate `receive` expressions for each message type.

## To Recognize:
1. A `receive ... end` block; multiple clauses indicate selective matching.

# Context & Application

- **Typical contexts**: Server loops; protocol code that must handle replies in a specific order.
- **Common applications**: Matching a reply tagged with a known pid or reference while ignoring unrelated messages.
- **Historical/stylistic notes**: "Without this feature, we'd have to anticipate all the different orders in which messages can arrive" (p. 32).

# Examples

**Example 1** (p. 31): A mailbox holding `foo`, `stop`, `{Pid, hello}`. A `receive` with a `stop` clause skips `foo` (which matches nothing), matches `stop`, and terminates the process.

**Example 2** (p. 32): Two sequential receives deliberately process `message1` then `message2`:

```erlang
receive
    message1 -> ...
end,
receive
    message2 -> ...
end
```

# Relationships

## Builds Upon
- *(none — foundational pair of prerequisites)*

## Enables
- *(none specific in scope)*

## Related
- **Unhandled messages** — Messages that never match a clause accumulate in the mailbox, risking memory leaks.

## Contrasts With
- *(none)*

# Common Errors

- **Error**: Leaving message types unmatched, causing the mailbox to grow unboundedly.
  **Correction**: Handle or explicitly discard every message type the process can receive.

# Common Confusions

- **Confusion**: Thinking messages must be processed strictly in arrival order.
  **Clarification**: They are processed in the order they are *matched*; non-matching messages are skipped and left in the mailbox.

# Source Reference

Chapter 1: Introducing Erlang, Section "Processes and Message Passing," pages 31-32.

# Verification Notes

- Definition source: Direct quotes from pp. 31-32.
- Confidence rationale: HIGH — explicit definition with mailbox walk-through.
- Uncertainties: None.
- Cross-reference status: `unhandled-messages` is a planned Chapter 3 card.
- Re-extraction notes: Fresh extraction — no pre-existing card for this source.
</content>
</invoke>
