---
concept: Asynchronous Signals
slug: asynchronous-signals
category: processes-concurrency
subcategory: communication
tier: foundational
source: "ERTS User's Guide"
source_slug: otp-erts
authors: "Ericsson AB"
chapter: "Communication in Erlang"
chapter_number: null
pdf_page: null
section: "Communication in Erlang"
extraction_confidence: high
aliases:
  - "asynchronous signaling"
  - "signal-based communication"
prerequisites:
  - erlang-process
extends: []
related:
  - erlang-signals
  - message-sending
  - message-receiving
  - exit-signals
  - links
  - monitors
contrasts_with: []
answers_questions:
  - "How is communication conceptually performed in Erlang?"
  - "What entities communicate via asynchronous signals?"
  - "Can I rely on implementation details of signal delivery?"
---

# Quick Definition

All communication in Erlang is conceptually performed using asynchronous signaling. Every executing entity -- processes and ports alike -- communicates exclusively through asynchronous signals, with messages being the most commonly used signal type.

# Core Definition

The ERTS User's Guide states: "Communication in Erlang is conceptually performed using asynchronous signaling. All different executing entities, such as processes and ports, communicate through asynchronous signals. The most commonly used signal is a message. Other common signals are exit, link, unlink, monitor, and demonitor signals." (Communication in Erlang chapter).

The guide further warns that while the virtual machine implementation of specific signals may sometimes provide stricter guarantees than the conceptual model describes, "it is of vital importance that such knowledge about the implementation is _not_ used by Erlang code, as the implementation can change at any time without prior notice."

# Prerequisites

- **erlang-process** -- Processes are one of the two primary executing entities that communicate via signals

# Key Properties

1. Communication is conceptually asynchronous -- there is no fundamental synchronous primitive
2. All executing entities (processes and ports) use the same signaling mechanism
3. Messages are the most common signal type
4. Other common signals include exit, link, unlink, monitor, and demonitor
5. The implementation of signals in the VM can vary over time, but the conceptual behavior is preserved
6. Relying on implementation-specific stricter guarantees is explicitly warned against

# Construction / Recognition

## To Construct/Create:

1. Use the `!` operator or `send/2,3` to send a message signal
2. Use `link/1`, `unlink/1` for link/unlink signals
3. Use `monitor/2,3`, `demonitor/1,2` for monitor/demonitor signals
4. Exit signals are sent automatically on process termination or via `exit/2`

## To Identify/Recognize:

1. Any inter-entity communication in Erlang is an asynchronous signal
2. The conceptual model applies uniformly to all signal types
3. If you observe "synchronous" behavior, it is built on top of asynchronous signals

# Context & Application

This concept is the foundational communication model for Erlang. All higher-level patterns -- gen_server calls, monitor notifications, link-triggered exits -- are built on this asynchronous signaling model. Understanding this is essential for reasoning about ordering, timing, and reliability in concurrent Erlang systems.

The ERTS guide emphasizes that major implementation changes have occurred over time:

- As from ERTS 5.5.2, exit signals to processes became truly asynchronously delivered
- As from ERTS 5.10, all signals from processes to ports became truly asynchronously delivered

These changes did not alter the conceptual model, only the implementation -- reinforcing why code must not depend on implementation specifics.

# Examples

**Example 1** (Communication in Erlang, "Implementation" section): The source provides two concrete examples of implementation changes that programs must not rely upon:

```text
- As from ERTS 5.5.2 exit signals to processes are truly asynchronously delivered.
- As from ERTS 5.10 all signals from processes to ports are truly asynchronously delivered.
```

These illustrate that what was once delivered synchronously in the implementation shifted to truly asynchronous delivery, without any change to the documented behavior.

# Relationships

## Builds Upon

- **erlang-process** -- Processes are the primary entities that communicate via signals

## Related

- **erlang-signals** -- The Erlang Reference Manual's detailed breakdown of signal types and ordering guarantees
- **message-sending** -- Messages are the most commonly used signal type
- **message-receiving** -- The receive side of message signals
- **exit-signals** -- Exit signals are one of the common asynchronous signal types
- **links** -- Link/unlink use the asynchronous signaling mechanism
- **monitors** -- Monitor/demonitor use the asynchronous signaling mechanism

# Common Errors

- **Error**: Writing code that depends on a specific signal being delivered synchronously because it appears to work that way in the current implementation
  **Correction**: The ERTS guide explicitly warns that implementation can change "at any time without prior notice"; always code to the asynchronous conceptual model

# Common Confusions

- **Confusion**: Believing that synchronous-looking operations (like `process_info/2`) are truly synchronous at the signal level
  **Clarification**: Synchronous communication is built on top of asynchronous signal pairs; the underlying mechanism is always asynchronous

- **Confusion**: Thinking signals between processes and ports have different fundamental semantics
  **Clarification**: All executing entities -- both processes and ports -- use the same asynchronous signaling model

# Source Reference

"Communication in Erlang" chapter, including "Passing of Signals," "Synchronous Communication," and "Implementation" sections. The chapter notes that detailed signal ordering information has been moved to the Signals section of the Processes chapter in the Erlang Reference Manual.

# Verification Notes

- Definition: Directly quoted from the ERTS User's Guide, "Communication in Erlang" chapter
- Implementation change examples: Verbatim from source
- Warning about not relying on implementation: Direct quote from source
- Confidence: HIGH -- the chapter explicitly states the conceptual model and its constraints
