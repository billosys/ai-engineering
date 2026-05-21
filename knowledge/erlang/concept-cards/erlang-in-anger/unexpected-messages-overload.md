---
concept: Unexpected Messages Overload
slug: unexpected-messages-overload
category: production-ops
subcategory: overload
tier: intermediate
source: "Stuff Goes Bad: Erlang in Anger"
source_slug: erlang-in-anger
authors: "Fred Hébert"
chapter: "Planning for Overload"
chapter_number: 3
pdf_page: null
section: "Unexpected Messages"
extraction_confidence: high
aliases:
  - "Unexpected messages"
prerequisites:
  - message-queue-overload
extends: []
related:
  - error-logger-overload
  - blocking-operation-in-hub-process
contrasts_with: []
answers_questions:
  - "Name the common sources of overload in Erlang systems."
  - "Why do unexpected messages accumulate in a process mailbox?"
---

# Quick Definition

Unexpected messages overload is queue growth caused by messages a process does not handle accumulating in its mailbox — rare in OTP behaviours but common in non-behaviour processes.

# Core Definition

From Chapter 3, section "Unexpected Messages": "Messages you didn't know about tend to be rather rare when using OTP applications. Because OTP behaviours pretty much expect you to handle anything with some clause in `handle_info/2`, unexpected messages will not accumulate much. However, all kinds of OTP-compliant systems end up having processes that may not implement a behaviour, or processes that go in a non-behaviour stretch where it overtakes message handling."

# Prerequisites

- `message-queue-overload` — this is a specific cause of it.

# Key Properties

1. Rare in proper OTP behaviours because `handle_info/2` is expected to catch any message.
2. Common in non-behaviour processes, or in processes that temporarily take over their own message handling.
3. Symptom: monitoring tools show a constant memory increase, and inspecting for large queue sizes locates the offending process.
4. Fix: handle the messages as required (add the missing receive clause).

# Construction / Recognition

Recognize it from a steadily climbing memory graph; inspect process message-queue lengths to find the culprit. Fix by adding a clause that handles (or explicitly discards) the previously unhandled message.

# Context & Application

Listed as the third common overload source in Chapter 3. It is a reminder that the OTP behaviours' catch-all `handle_info/2` clause is precisely what protects most processes from this failure mode.

# Examples

From Chapter 3, section "Unexpected Messages": "If you're lucky enough, monitoring tools will show a constant memory increase, and inspecting for large queue sizes will let you find which process is at fault. You can then fix the problem by handling the messages as required."

# Relationships

## Builds Upon
- `message-queue-overload` — a specific cause of it.

## Enables
Nothing.

## Related
- `error-logger-overload`, `blocking-operation-in-hub-process` — the other common overload sources in the same chapter.

## Contrasts With
Nothing directly.

# Common Errors

- Writing a non-behaviour process or a non-behaviour receive stretch without a catch-all clause for unmatched messages.

# Common Confusions

- OTP behaviours do not magically discard unexpected messages — they accumulate unless your `handle_info/2` has a clause for them; the protection comes from the *convention* of writing that clause.

# Source Reference

Chapter 3: Planning for Overload, Section "Unexpected Messages". (No PDF pages — this source has none.)

# Verification Notes

- Definition source: quoted from Chapter 3, section "Unexpected Messages."
- Confidence rationale: high — explicitly described as a common overload source.
- Uncertainties: none.
- Cross-reference status: Verified
