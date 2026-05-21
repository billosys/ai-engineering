---
# === CORE IDENTIFICATION ===
concept: Message Sending
slug: message-sending

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
section: "Sending Signals"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - sending messages
  - "send operator: !"
  - message passing

# === TYPED RELATIONSHIPS ===
prerequisites:
  - erlang-process
  - erlang-signals
extends:
  - erlang-signals
related:
  - message-receiving
  - message-queue
  - process-registration
  - process-aliases
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do I send messages between Erlang processes?"
  - "How do I send and receive messages between processes?"
---

# Quick Definition
Message sending in Erlang is done using the send operator (`!`) or the `erlang:send/2,3` BIFs. A message signal is the most common type of asynchronous signal between processes, delivering an arbitrary Erlang term to the recipient's message queue.

# Core Definition
The Erlang Reference Manual identifies message signals as the most common signal type: "A message signal can be sent using the send operator `!`." (Processes chapter, "Signals" section). The message signal type is "Sent when using the send operator `!`, or when calling one of the `erlang:send/2,3` or `erlang:send_nosuspend/2,3` BIFs." (Processes chapter, "Sending Signals" subsection). The receiver can be identified by pid, registered name, or process alias.

# Prerequisites
- **erlang-process** -- Messages are sent between processes
- **erlang-signals** -- Message sending is a specific type of signal

# Key Properties
1. Messages are sent using the `!` operator or `send/2,3` BIFs
2. Messages are asynchronous -- the sender does not wait for delivery
3. The receiver can be identified by pid, registered name, or process alias
4. Any Erlang term can be sent as a message
5. When the receiver is identified by a registered name locally, there is synchronous error checking -- a `badarg` error if the name is not registered
6. Messages sent to ports are also delivered asynchronously (changed from synchronous before OTP 16)

# Construction / Recognition
## To Construct/Create:
1. Use `Pid ! Message` to send `Message` to process identified by `Pid`
2. Use `Name ! Message` to send to a locally registered process
3. Use `{Name, Node} ! Message` to send to a registered process on a remote node
4. Use `erlang:send(Dest, Message)` as an alternative to `!`
5. Use `erlang:send(Dest, Message, Options)` for additional options

## To Identify/Recognize:
1. The `!` operator in code is a message send
2. Calls to `erlang:send/2,3` or `erlang:send_nosuspend/2,3`

# Context & Application
Message passing is the sole mechanism for data exchange between Erlang processes. Since processes share no memory, all coordination happens through messages. This design enables distribution transparency -- the same `!` operator works for both local and remote processes when pids are used. The asynchronous nature means the sender never blocks waiting for the message to be received (though it may block on distribution buffer backpressure).

# Examples
**Example 1** (Processes, "Sending Signals" section): The message signal entry: "`message` -- Sent when using the send operator `!`, or when calling one of the `erlang:send/2,3` or `erlang:send_nosuspend/2,3` BIFs."

**Example 2** (Processes, "Signals" section): "A message signal can be sent using the send operator `!`. A received message can be fetched from the message queue by the receiving process using the `receive` expression."

# Relationships
## Builds Upon
- **erlang-signals** -- Message sending is a specific type of signal
- **erlang-process** -- Messages are exchanged between processes

## Enables
- **message-receiving** -- Sent messages need to be received
- **message-queue** -- Sent messages are added to the receiver's message queue

## Related
- **process-registration** -- Allows sending to a name instead of a pid
- **process-aliases** -- Allows sending to an alias reference

## Contrasts With
No direct contrasts.

# Common Errors
- **Error**: Sending a message to a registered name that does not exist on the local node
  **Correction**: When sending to a registered name locally, there is synchronous error checking -- a `badarg` error will occur if no process is registered under that name. Use `whereis/1` to check first, or send to a pid.

# Common Confusions
- **Confusion**: Thinking message sending is synchronous or blocks until the message is received
  **Clarification**: Message sending is always asynchronous. The `!` operator returns the message itself and does not wait for delivery or receipt.

# Source Reference
Processes chapter, "Signals" section and "Sending Signals" subsection.

# Verification Notes
- Definition source: Direct from source
- Confidence rationale: High -- explicit listing in the signal types
- Uncertainties: None
- Cross-reference status: All slugs verified against planned extraction
