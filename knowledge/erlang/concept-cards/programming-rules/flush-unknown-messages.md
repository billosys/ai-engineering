---
concept: Flush Unknown Messages
slug: flush-unknown-messages
category: processes-concurrency
subcategory: processes-servers-messages
tier: intermediate
source: "Program Development Using Erlang — Programming Rules and Conventions"
source_slug: programming-rules
authors: "Klas Eriksson, Mike Williams, Joe Armstrong"
chapter: "Processes, Servers and Messages"
chapter_number: 5
pdf_page: null
section: "5.8 Flush unknown messages"
extraction_confidence: high
aliases:
  - "flush unknown messages"
  - "Other clause in receive"
  - "drain the mailbox"
prerequisites: []
extends: []
related:
  - tag-messages
  - receive-timeouts
  - write-tail-recursive-servers
contrasts_with: []
answers_questions:
  - "How should a server handle messages it does not recognize?"
  - "Why should a server have an Other clause in a receive?"
---

# Quick Definition

Every server should have an `Other` catch-all clause in at least one `receive`, so unknown messages are flushed and do not fill the message queue.

# Core Definition

"Every server should have an `Other` alternative in at least one receive statement. This is to avoid filling up message queues" (Programming Rules, 5.8). Without a catch-all, unrecognized messages accumulate in the mailbox forever; the `Other` clause consumes them (typically logging an error) and continues the loop.

# Prerequisites

This is a foundational concept with no prerequisites within this source.

# Key Properties

1. At least one `receive` in a server has a catch-all `Other` clause.
2. The catch-all prevents unrecognized messages from accumulating in the mailbox.
3. The `Other` clause typically logs the unexpected message before looping.

# Construction / Recognition

## To Apply

1. Add a final `Other ->` clause to the server's main `receive`.
2. Log the unexpected message (e.g. via `error_logger`) and continue the loop.

## To Recognize a Violation

1. A server `receive` matches only its known messages, with no catch-all.

# Context & Application

A core process-design principle (section 5).

- **Typical contexts**: long-lived server `receive` loops.
- **Common applications**: an `Other ->` clause logging `"Process ~w got unknown msg ~w"`.

# Examples

**Example** (from source): `main_loop/0` matches `{msg1, Msg1}` and `{msg2, Msg2}`, then `Other ->` calls `error_logger:error_msg/2` to log the unknown message and loops — "Flushes the message queue."

# Relationships

## Related

- **Tag messages** — together these keep mailboxes from filling and clauses unambiguous.
- **Time-outs** — the source cross-references this rule when discussing `after`.
- **Write tail-recursive servers** — the `Other` clause loops, so it must do so tail-recursively.

# Common Errors

- **Error**: Writing a server `receive` with no catch-all clause.
  **Correction**: Add an `Other ->` clause that logs and loops.

# Common Confusions

- **Confusion**: Thinking unmatched messages are simply discarded.
  **Clarification**: They are *not* — they stay in the mailbox indefinitely until a clause consumes them.

# Source Reference

"Program Development Using Erlang — Programming Rules and Conventions", section 5.8 "Flush unknown messages".

# Verification Notes

- Definition source: Direct adaptation of section 5.8.
- Confidence rationale: HIGH — the rule is stated explicitly with a code example.
- Uncertainties: None.
- Cross-reference status: all referenced slugs are planned cards in this extraction.
