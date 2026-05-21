---
# === CORE IDENTIFICATION ===
concept: Erlang Signals
slug: erlang-signals

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
section: "Signals"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - signal
  - asynchronous signal

# === TYPED RELATIONSHIPS ===
prerequisites:
  - erlang-process
extends: []
related:
  - message-sending
  - message-receiving
  - exit-signals
  - links
  - monitors
  - signal-delivery
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do Erlang processes communicate?"
  - "What is a signal in Erlang?"
---

# Quick Definition
All communication between Erlang processes and ports is done by sending and receiving asynchronous signals. Message signals are the most common type, but signals also include link, unlink, exit, monitor, demonitor, down, and various request/reply pairs.

# Core Definition
The Erlang Reference Manual states: "All communication between Erlang processes and Erlang ports is done by sending and receiving asynchronous signals. The most common signals are Erlang message signals." The manual further explains that "Synchronous communication can be broken down into multiple asynchronous signals" -- for example, `process_info/2` sends an asynchronous request signal and then blocks waiting for the reply signal. (Processes chapter, "Signals" section).

# Prerequisites
- **erlang-process** -- Signals are the communication mechanism between processes

# Key Properties
1. All inter-process and process-port communication uses asynchronous signals
2. Message signals are the most common type, sent via the `!` operator or `send/2,3`
3. Other signal types include: link, unlink, exit, monitor, demonitor, down, change, group_leader, spawn_request/reply, and various port signals
4. Synchronous operations are built on top of asynchronous signal pairs (request + reply)
5. Signals are received asynchronously and automatically -- reception is not tied to `receive`
6. The runtime provides services (clock, name, timer, spawn) implemented as groups of independently executing entities
7. Signal ordering between services and processes is not preserved across multiple entities within a service

# Construction / Recognition
## To Construct/Create:
1. Use the send operator `!` or `send/2,3` to send a message signal
2. Call `link/1` to send a link signal
3. Call `monitor/2,3` to send a monitor signal
4. Call `exit_signal/2` to send an explicit exit signal
5. Various BIFs send request/reply signal pairs

## To Identify/Recognize:
1. Any inter-process communication is a signal
2. Message signals appear in the message queue
3. Link/unlink/monitor/demonitor signals update process-local state
4. Exit/down signals may terminate the process, be dropped, or be converted to messages

# Context & Application
Understanding that everything is a signal is key to understanding Erlang's concurrency semantics. The asynchronous nature of signals means that there are no synchronous operations at the fundamental level -- even seemingly synchronous BIFs like `process_info/2` are built on asynchronous signal exchange. This has important implications for reasoning about ordering and timing in concurrent systems.

# Examples
**Example 1** (Processes, "Sending Signals" section): The source lists the major signal types:
- `message` -- sent via `!` operator or `send/2,3`
- `link`/`unlink` -- sent via `link/1`, `unlink/1`
- `exit` -- sent on linked process termination or via `exit_signal/2`
- `monitor`/`demonitor` -- sent via `monitor/2,3`, `demonitor/1,2`
- `down` -- sent by monitored process/port on termination

**Example 2** (Processes, "Signals" section): Synchronous communication decomposed: "An example of such a synchronous communication is a call to the `erlang:process_info/2` BIF when the first argument does not equal the process identifier of the calling process. The caller sends an asynchronous signal requesting information, and then blocks waiting for the reply signal."

# Relationships
## Builds Upon
- **erlang-process** -- Signals are the mechanism by which processes interact

## Enables
- **message-sending** -- Message signals are the most common signal type
- **message-receiving** -- Received signals may become messages in the queue
- **exit-signals** -- Exit signals are a specific signal type
- **signal-delivery** -- The ordering guarantees for signals

## Related
- **links** -- Link/unlink operations use signals
- **monitors** -- Monitor/demonitor/down operations use signals

## Contrasts With
No direct contrasts.

# Common Errors
- **Error**: Relying on implementation details of how reply signals are delivered (e.g., inspecting message queues for internal signals)
  **Correction**: The source warns that reply signal implementation may change and should not be relied upon: "these are internal implementation details of the runtime system that you should _not_ rely on."

# Common Confusions
- **Confusion**: Thinking that signal reception happens only in `receive` expressions
  **Clarification**: Signals are received asynchronously and automatically. "There is nothing a process must do to handle the reception of signals, or can do to prevent it. In particular, signal reception is _not_ tied to the execution of a `receive` expression."

# Source Reference
Processes chapter, "Signals" section, including "Sending Signals" and "Receiving Signals" subsections.

# Verification Notes
- Definition source: Direct from source
- Confidence rationale: High -- comprehensive section with explicit definitions
- Uncertainties: None
- Cross-reference status: All slugs verified against planned extraction
