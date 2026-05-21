---
concept: sys Module Introspection
slug: sys-module-introspection
category: otp-behaviours
subcategory: live-debugging
tier: intermediate
source: "Stuff Goes Bad: Erlang in Anger"
source_slug: erlang-in-anger
authors: "Fred Hébert"
chapter: "Runtime Metrics"
chapter_number: 5
pdf_page: null
section: "Digging In > OTP Processes"
extraction_confidence: medium
aliases:
  - sys module
  - OTP process inspection
prerequisites:
  - process-inspection
extends:
  - process-inspection
related:
  - otp-behaviour
contrasts_with: []
answers_questions:
  - "How do I safely inspect a process?"
  - "What features does the sys module give OTP processes?"
---

# Quick Definition

The `sys` module provides extra introspection and control for OTP processes — logging, statistics, and inspection or replacement of process state — capabilities that plain processes do not offer.

# Core Definition

"When processes in question are OTP processes (most of the processes in a production system should definitely be OTP processes), you instantly win more tools to inspect them. In general the `sys` module is what you want to look into" (Chapter 5, "Digging In > OTP Processes").

# Prerequisites

- `process-inspection`: the `sys` module extends generic process inspection with OTP-specific facilities.

# Key Properties

The `sys` module offers, for any OTP process:

1. Logging of all messages and state transitions — to the shell, a file, or an internal queryable buffer.
2. Statistics — reductions, message counts, time, and so on.
3. Fetching the *status* of a process (metadata including the state).
4. Fetching the *state* of a process (e.g. the `#state{}` record).
5. Replacing that state.
6. Custom debugging functions usable as callbacks.
7. Suspending and resuming process execution.

# Construction / Recognition

Identify that the suspect process is an OTP process (gen_server, gen_statem, etc.), then use `sys` functions to log its activity, read its state, or suspend it. The book advises reading the `sys` documentation rather than memorizing the API.

# Context & Application

Used to inspect and manipulate OTP processes in a live system — for instance, dumping a stuck gen_server's state, recording its message traffic, or pausing it. Because most production processes should be OTP processes, `sys` is broadly applicable.

# Examples

From Chapter 5, "Digging In > OTP Processes": the book lists the feature set above and notes "It also provides functionality to suspend or resume process execution. I won't go into a lot of details about these functions, but be aware that they exist."

# Relationships

## Builds Upon
- process-inspection

## Enables

## Related
- otp-behaviour

## Contrasts With

# Common Errors

- Trying to use `sys` introspection on non-OTP processes — these facilities depend on the OTP behaviour machinery.
- Replacing or suspending a process's state in production without understanding the consequences.

# Common Confusions

- `sys` does not replace generic `process_info` inspection — it adds OTP-specific powers (state, logging, suspend/resume) on top.

# Source Reference

Chapter 5: Runtime Metrics, Section "Digging In > OTP Processes". (No PDF pages — this source has none.)

# Verification Notes

- Definition source: synthesized from the chapter feature list.
- Confidence rationale: medium — the chapter lists the features but deliberately omits API detail, deferring to the `sys` docs.
- Uncertainties: exact function names and signatures are not given in this source.
- Cross-reference status: Verified
