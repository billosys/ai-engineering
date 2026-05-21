---
# === CORE IDENTIFICATION ===
concept: Message Receiving
slug: message-receiving

# === CLASSIFICATION ===
category: processes-concurrency
subcategory: null
tier: foundational

# === PROVENANCE ===
source: "Erlang Reference Manual"
source_slug: otp-reference-manual
authors: "Ericsson AB"
chapter: "Processes"
chapter_number: null
pdf_page: null
section: "Receiving Signals"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - receiving messages
  - receive expression

# === TYPED RELATIONSHIPS ===
prerequisites:
  - erlang-process
  - erlang-signals
  - message-sending
extends:
  - erlang-signals
related:
  - message-queue
  - process-aliases
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do I receive messages in an Erlang process?"
  - "How do I send and receive messages between processes?"
---

# Quick Definition
Signal reception in Erlang is asynchronous and automatic -- it happens without the process explicitly doing anything. Message signals are added to the process's message queue, from which they can be fetched using the `receive` expression through pattern matching.

# Core Definition
The Erlang Reference Manual states: "Signals are received asynchronously and automatically. There is nothing a process must do to handle the reception of signals, or can do to prevent it. In particular, signal reception is _not_ tied to the execution of a `receive` expression, but can happen anywhere in the execution flow of a process." When a message signal is received, "the message is added to the message queue. When the message has been added to the message queue, the receiving process can fetch the message from the message queue using the `receive` expression." (Processes chapter, "Receiving Signals" subsection).

# Prerequisites
- **erlang-process** -- Messages are received by processes
- **erlang-signals** -- Message reception is part of the signal system
- **message-sending** -- Must understand how messages arrive

# Key Properties
1. Signal reception is asynchronous and automatic -- not tied to `receive`
2. A `message` signal adds a message to the message queue
3. `receive` expression fetches messages from the queue using pattern matching
4. Messages sent via a deactivated process alias are dropped before reaching the queue
5. Other signal types (exit, down, change) may be converted to messages and added to the queue
6. Link/unlink/monitor/demonitor signals update process-local state without adding messages
7. The `receive` expression selects the first message from the start of the queue that matches

# Construction / Recognition
## To Construct/Create:
1. Use a `receive` expression to fetch messages from the message queue
2. Pattern match on expected message formats within the `receive` clauses
3. Optionally use an `after` clause to specify a timeout

## To Identify/Recognize:
1. The `receive ... end` expression in code indicates message receiving
2. Process info can show the current message queue length

# Context & Application
The distinction between signal reception (automatic) and message fetching (`receive` expression) is important. Many signals other than explicit messages can result in messages being added to the queue -- for example, a monitor's `DOWN` signal or a trapped `EXIT` signal become messages. The `receive` expression uses selective receive: it scans the queue from the beginning and picks the first matching message, not necessarily the first message in the queue.

# Examples
**Example 1** (Processes, "Receiving Signals" section): The source describes the action for a received `message` signal: "If the message signal was sent using a process alias that is no longer active, the message signal will be dropped; otherwise, if the alias is still active or the message signal was sent by other means, the message is added to the message queue."

**Example 2** (Processes, "Receiving Signals" section): Actions for `exit` signals: "Set the receiver in an exiting state, drop the signal, or convert the signal into a message and add it to the message queue."

# Relationships
## Builds Upon
- **erlang-signals** -- Receiving is one side of the signal mechanism
- **message-sending** -- Receiving is the counterpart to sending

## Enables
- **message-queue** -- Understanding how messages enter and are fetched from the queue

## Related
- **process-aliases** -- Aliases can cause message signals to be dropped
- **trap-exit** -- Determines whether exit signals become messages

## Contrasts With
No direct contrasts.

# Common Errors
- **Error**: Assuming that if no `receive` expression is executing, messages are lost
  **Correction**: Messages are buffered in the message queue regardless of what the process is doing. They remain until fetched by a `receive` expression or the process terminates.

# Common Confusions
- **Confusion**: Thinking `receive` is what causes signals to arrive at the process
  **Clarification**: Signal reception happens automatically and asynchronously. The `receive` expression only fetches already-received messages from the queue. "Signal reception is _not_ tied to the execution of a `receive` expression."

# Source Reference
Processes chapter, "Receiving Signals" subsection.

# Verification Notes
- Definition source: Direct from source
- Confidence rationale: High -- explicit description of receiving semantics
- Uncertainties: None
- Cross-reference status: All slugs verified against planned extraction
