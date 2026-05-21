---
concept: error_logger Overload
slug: error-logger-overload
category: production-ops
subcategory: overload
tier: intermediate
source: "Stuff Goes Bad: Erlang in Anger"
source_slug: erlang-in-anger
authors: "Fred Hébert"
chapter: "Planning for Overload"
chapter_number: 3
pdf_page: null
section: "error_logger Explodes"
extraction_confidence: high
aliases:
  - "error_logger explodes"
prerequisites:
  - message-queue-overload
extends: []
related:
  - blocking-operation-in-hub-process
contrasts_with: []
answers_questions:
  - "Name the common sources of overload in Erlang systems."
  - "Why does the error_logger process blow up?"
---

# Quick Definition

`error_logger` overload is a common Erlang failure in which the default error-logging process, being slow, lets messages pile up in its mailbox until the node runs out of memory.

# Core Definition

From Chapter 3, section "error_logger Explodes": "Ironically, the process in charge of error logging is one of the most fragile ones. In a default Erlang install, the `error_logger` process will take its sweet time to log things to disk or over the network, and will do so much more slowly than errors can be generated."

# Prerequisites

- `message-queue-overload` — `error_logger` overload is a specific instance of queue overload.

# Key Properties

1. The default `error_logger` logs to disk or network slower than errors can be generated.
2. Worst with high-volume user-generated log messages — `error_logger` expects only exceptional traffic, not continual messages.
3. Also worst when large processes crash: the entire process state, including mailboxes, is copied for logging, so a few crash messages can spike memory.
4. The recommended remedy (at time of writing) is the `lager` logging library.
5. `lager` truncates voluminous messages, can drop OTP-generated error messages above a threshold, and switches automatically between asynchronous and synchronous modes for user messages to self-regulate.
6. `lager` cannot handle every case — notably high-volume user messages all from one-off processes — though that is rarer and more controllable.

# Construction / Recognition

Recognize it as a node OOM where the `error_logger` process has a huge mailbox or where logging is far behind. Remedy: replace the default logger with `lager`.

# Context & Application

Listed as the first common overload source in Chapter 3. It is notable because the very process meant to record failures is itself a frequent cause of node death.

# Examples

From Chapter 3, section "error_logger Explodes": for large-process crashes, "the entire state of processes (including their mailboxes) gets copied over to be logged. It only takes a few messages to cause memory to bubble up a lot." The book recommends `lager`, which "will truncate voluminous log messages, optionally drop OTP-generated error messages when they go over a certain threshold, and will automatically switch between asynchronous and synchronous modes."

# Relationships

## Builds Upon
- `message-queue-overload` — a specific case of it.

## Enables
Nothing.

## Related
- `blocking-operation-in-hub-process` — another common overload source listed in the same chapter section.

## Contrasts With
Nothing directly.

# Common Errors

- Logging high-volume user messages through the default `error_logger`, which is built for exceptional traffic only.

# Common Confusions

- `lager` is a mitigation, not a cure-all — it cannot handle very high-volume user messages from many one-off processes.
- The danger from a crashing large process is not the crash itself but the *copying of its entire state and mailbox* into the log.

# Source Reference

Chapter 3: Planning for Overload, Section "error_logger Explodes". (No PDF pages — this source has none.)

# Verification Notes

- Definition source: quoted from Chapter 3, section "error_logger Explodes."
- Confidence rationale: high — explicitly described.
- Uncertainties: `lager` is "the best solution at the time of writing"; modern OTP has `logger`, but the source predates it.
- Cross-reference status: Verified
