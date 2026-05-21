---
# === CORE IDENTIFICATION ===
concept: Message Queue
slug: message-queue

# === CLASSIFICATION ===
category: processes-concurrency
subcategory: null
tier: intermediate

# === PROVENANCE ===
source: "Erlang Reference Manual"
source_slug: otp-reference-manual
authors: "Ericsson AB"
chapter: "Processes"
chapter_number: null
pdf_page: null
section: "Adding Messages to the Message Queue"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - mailbox
  - process mailbox

# === TYPED RELATIONSHIPS ===
prerequisites:
  - erlang-process
  - erlang-signals
  - message-receiving
extends:
  - message-receiving
related:
  - priority-messages
  - signal-delivery
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How are messages ordered in an Erlang process's message queue?"
  - "What determines the order of messages in the message queue?"
---

# Quick Definition
Each Erlang process has a message queue where received message signals and certain other signals converted to messages are stored until fetched by a `receive` expression. By default, messages are appended to the end of the queue, preserving the order in which the corresponding signals were received.

# Core Definition
The Erlang Reference Manual states: "When a message signal is received, the action taken is to add the message to the message queue." Unless the process has enabled priority messages, "all messages are added to the end of the message queue. In the case that the receiver has not enabled priority messages, the order of the messages in the message queue will reflect the order in which the signals corresponding to the messages in the queue were received. Messages corresponding to signals from the same sender will then also be ordered in the same order as the signals were sent due to the signal ordering guarantee of the language." (Processes chapter, "Adding Messages to the Message Queue" subsection).

# Prerequisites
- **erlang-process** -- Each process has its own message queue
- **erlang-signals** -- Signals are the mechanism that delivers messages
- **message-receiving** -- Understanding how signals become messages in the queue

# Key Properties
1. Each process has exactly one message queue
2. By default, messages are added to the end of the queue (FIFO for same-sender messages)
3. The queue order reflects the order in which corresponding signals were received
4. Messages from the same sender maintain their sending order (due to signal ordering guarantee)
5. The `receive` expression selects the first matching message from the start of the queue
6. Non-message signals (exit, down, change) may also be converted to messages and added to the queue
7. Priority messages (OTP 28.0+) may be inserted ahead of ordinary messages

# Construction / Recognition
## To Construct/Create:
1. The message queue is created automatically with each new process
2. Messages are added by receiving message signals or signals converted to messages

## To Identify/Recognize:
1. Use `process_info(Pid, message_queue_len)` to check the queue length
2. Use `process_info(Pid, messages)` to inspect the queue contents (for debugging only)

# Context & Application
The message queue is fundamental to Erlang's actor model. Understanding queue ordering is important for designing correct protocols. The guarantee that messages from a single sender arrive in order (but messages from different senders may interleave) shapes how multi-party protocols must be designed. The selective receive mechanism of `receive` allows picking specific messages out of order, but scanning a long queue is expensive.

# Examples
**Example 1** (Processes, "Adding Messages to the Message Queue" section): "Unless the receiving process has enabled priority messages, all messages are added to the end of the message queue."

**Example 2** (Processes, "Adding Messages to the Message Queue" section): "Messages corresponding to signals from the same sender will then also be ordered in the same order as the signals were sent due to the signal ordering guarantee of the language."

# Relationships
## Builds Upon
- **message-receiving** -- Messages enter the queue via signal reception
- **signal-delivery** -- The ordering guarantee determines queue order

## Enables
- **priority-messages** -- A modification to the default queue ordering

## Related
- **erlang-signals** -- Various signal types can result in messages in the queue

## Contrasts With
No direct contrasts.

# Common Errors
- **Error**: Assuming messages from different senders arrive in a globally consistent order
  **Correction**: Only messages from the same sender to the same receiver are guaranteed to be in order. Messages from different senders may interleave in any order.

# Common Confusions
- **Confusion**: Thinking `receive` always processes the oldest message first
  **Clarification**: `receive` scans from the start and selects the first message that matches any clause pattern. If the oldest message does not match, it is skipped and remains in the queue.

# Source Reference
Processes chapter, "Adding Messages to the Message Queue" subsection.

# Verification Notes
- Definition source: Direct from source
- Confidence rationale: High -- explicit description of queue ordering semantics
- Uncertainties: None
- Cross-reference status: All slugs verified against planned extraction
