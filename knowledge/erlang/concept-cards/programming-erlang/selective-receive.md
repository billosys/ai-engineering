---
# === CORE IDENTIFICATION ===
concept: Selective Receive
slug: selective-receive

# === CLASSIFICATION ===
category: processes-concurrency
subcategory: communication
tier: intermediate

# === PROVENANCE ===
source: "Programming Erlang, Second Edition"
source_slug: programming-erlang
authors: Joe Armstrong
chapter: "Concurrent Programming"
chapter_number: 12
pdf_page: null
section: "Selective Receive"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "selective receive"
  - "priority receive"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - receive
  - mailbox
extends:
  - receive
related:
  - message-passing
  - receive-timeout
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is selective receive?"
  - "How does receive handle messages that do not match any clause?"
  - "How can I receive only a specific message and queue the rest?"
---

# Quick Definition

Selective receive is the behavior of `receive` whereby messages that match no clause are set aside in a save queue and the process waits for a matching message. It lets a process pick a specific message out of its mailbox.

# Core Definition

"`receive` provides what is called selective receive" (Armstrong, "Concurrent Programming," "Introducing Client-Server"). The mechanism, as described in "Selective Receive": (1) on entering a `receive`, a timer starts if an `after` clause is present; (2) the first mailbox message is matched against each pattern; on a match it is removed and the clause body runs; (3) if no pattern matches, that message is moved to a "save queue" and the next message is tried, repeating until a match is found or the mailbox is exhausted; (4) if none match, the process suspends until a new message arrives — saved messages are *not* rematched, only new ones; (5) once a message matches, all saved messages are reentered into the mailbox in arrival order, and any timer is cleared; (6) if the timer elapses first, the `after` expressions run and saved messages are restored. This lets a process wait for one specific message (e.g. `{Pid, Response}`) while queueing all others.

# Prerequisites

- **receive** — Selective receive is the matching behavior of the `receive` primitive.
- **Mailbox** — The mechanism moves messages between the mailbox and a save queue.

# Key Properties

1. Messages are matched against `receive` clauses one at a time, in mailbox order.
2. A non-matching message is moved to a temporary save queue.
3. The process suspends if no current message matches; only newly arriving messages are then tried.
4. On a match, all saved messages return to the mailbox in their original arrival order.
5. It allows binding part of a pattern (e.g. a known `Pid`) so only the intended message matches.
6. With `after 0`, it underpins "priority receive" — preferring one message shape over others.

# Construction / Recognition

## To Construct/Create:
1. Write a `receive` whose pattern is specific enough to match only the wanted message.
2. Bind known values into the pattern (e.g. `{Pid, Response}` with `Pid` already bound) so other messages are queued.
3. For priority receive, nest receives with `after 0` to prefer a high-priority pattern.

## To Identify/Recognize:
1. A `receive` pattern containing an already-bound variable indicates a selective match on a specific sender/message.
2. A nested `receive {alarm, X} -> ... after 0 -> receive Any -> ... end end` is the priority-receive idiom.

# Context & Application

- **Typical contexts**: A client's `rpc` waiting for the server's reply and nothing else; protocols that must process a particular message first.
- **Common applications**: Correctly correlating a request with its response; implementing priority handling.
- **Historical/stylistic notes**: In `area_server1`'s `rpc`, receiving "any message" was a bug — the fix used a `{Pid, Response}` pattern so only the server's reply matches.

# Examples

**Example 1** ("Introducing Client-Server"): Changing `rpc` to `receive {Pid, Response} -> Response end` — with `Pid` bound — matches only the server's reply; "All other messages will be queued."

**Example 2** ("Receive with Timeout Value of Zero"): `priority_receive()` uses `receive {alarm, X} -> {alarm, X} after 0 -> receive Any -> Any end end` so an `{alarm, X}` message, if present, is returned before any other.

**Example 3** ("Selective Receive"): The six-step description of how unmatched messages go to the save queue and are reentered in arrival order once a match occurs.

# Relationships

## Builds Upon
- **receive** — Selective receive is the defining behavior of the `receive` primitive.
- **Mailbox** — It moves messages between the mailbox and the save queue.

## Enables
- **Receive with a timeout** — The `after` clause interacts with the selective-receive algorithm.

## Related
- **Message passing** — Selective receive picks among the messages that `!` delivered.

## Contrasts With
- None.

# Common Errors

- **Error**: Writing `rpc` to `receive Response -> Response end` — it accepts *any* message, not just the server's reply.
  **Correction**: Match `{Pid, Response}` with `Pid` bound so unrelated messages are queued, not misread.

- **Error**: Using priority receive over a large mailbox.
  **Correction**: Keep mailboxes small; scanning a large mailbox for the priority pattern is inefficient.

# Common Confusions

- **Confusion**: Thinking saved (non-matching) messages are rematched as soon as a new message arrives.
  **Clarification**: Only the new message is matched; saved messages are reentered after a successful match.

- **Confusion**: Believing the save queue can reorder messages.
  **Clarification**: Saved messages always return to the mailbox in their original arrival order.

# Source Reference

Chapter 12: "Concurrent Programming," sections "Introducing Client-Server," "Receive with Timeout Value of Zero," and "Selective Receive." EPUB source — no page numbers.

# Verification Notes

- Definition source: Direct adaptation of the six-step "Selective Receive" description and the `rpc` fix.
- Confidence rationale: HIGH — the mechanism is described step by step.
- Uncertainties: None.
- Cross-reference status: Canonical slug `selective-receive`; cross-refs verified.
- Re-extraction notes: Fresh extraction; new card (no prior file).
