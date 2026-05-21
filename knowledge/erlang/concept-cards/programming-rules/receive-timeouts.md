---
concept: Be Careful With Receive Time-outs
slug: receive-timeouts
category: processes-concurrency
subcategory: processes-servers-messages
tier: intermediate
source: "Program Development Using Erlang — Programming Rules and Conventions"
source_slug: programming-rules
authors: "Klas Eriksson, Mike Williams, Joe Armstrong"
chapter: "Processes, Servers and Messages"
chapter_number: 5
pdf_page: null
section: "5.11 Time-outs"
extraction_confidence: high
aliases:
  - "time-outs"
  - "receive after"
  - "late messages"
prerequisites: []
extends: []
related:
  - flush-unknown-messages
  - tag-messages
contrasts_with: []
answers_questions:
  - "What must I handle when using after in a receive statement?"
---

# Quick Definition

Be careful with `after` in `receive` statements — handle the case where the awaited message arrives later, after the time-out has already fired.

# Core Definition

"Be careful when using `after` in receive statements. Make sure that you handle the case when the message arrives later" (Programming Rules, 5.11). A time-out does not cancel the pending message; if it arrives after the `after` clause has fired, it will sit in the mailbox — which is why the source cross-references "Flush unknown messages".

# Prerequisites

This is a foundational concept with no prerequisites within this source.

# Key Properties

1. An `after` clause in a `receive` fires on time-out but does not cancel the awaited message.
2. A message that arrives after the time-out remains in the mailbox.
3. Such late messages must be handled (e.g. flushed) so they do not accumulate.

# Construction / Recognition

## To Apply

1. When using `receive ... after`, plan for the awaited message arriving late.
2. Ensure a later `receive` (with an `Other` clause) drains such messages.

## To Recognize a Violation

1. A `receive ... after` time-out has no provision for the message arriving afterward.

# Context & Application

A core process-design principle (section 5).

- **Typical contexts**: synchronous request/reply with a deadline.
- **Common applications**: pairing a timed `receive` with later mailbox flushing.

# Examples

The source states the rule briefly and cross-references "Flush unknown messages"; no code listing is given.

# Relationships

## Related

- **Flush unknown messages** — the mechanism for handling a message that arrives after time-out.
- **Tag messages** — tags let a later `receive` recognize and drain the late reply.

# Common Errors

- **Error**: Assuming a timed-out message will never arrive.
  **Correction**: Expect it to arrive late; ensure it is flushed from the mailbox.

# Common Confusions

- **Confusion**: Thinking `after` cancels the pending receive.
  **Clarification**: It only ends the wait — the message itself can still be delivered to the mailbox afterward.

# Source Reference

"Program Development Using Erlang — Programming Rules and Conventions", section 5.11 "Time-outs".

# Verification Notes

- Definition source: Direct adaptation of section 5.11.
- Confidence rationale: HIGH — the rule is stated explicitly.
- Uncertainties: None.
- Cross-reference status: all referenced slugs are planned cards in this extraction.
