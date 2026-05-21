---
concept: Asynchronous Message Passing
slug: asynchronous-message-passing
category: processes-concurrency
subcategory: concurrency-model
tier: intermediate
source: "Learn You Some Erlang for Great Good!"
source_slug: learn-you-some-erlang
authors: "Fred Hébert"
chapter: "The Hitchhiker's Guide to Concurrency"
chapter_number: 10
pdf_page: null
section: "Fault Tolerance"
extraction_confidence: high
aliases:
  - "asynchronous messages"
  - "async message passing"
prerequisites:
  - message-passing
extends:
  - message-passing
related:
  - process-mailbox
  - shared-nothing-isolation
contrasts_with: []
answers_questions:
  - "Why is Erlang message passing asynchronous?"
  - "How does asynchronous messaging support distribution and fault tolerance?"
---

# Asynchronous Message Passing

## Quick Definition

Asynchronous message passing means a process sends a message and continues immediately, without waiting for or being guaranteed delivery. This design choice makes remote calls and fault tolerance safe.

## Core Definition

The chapter argues asynchronous message passing "was a good design pick" for distribution and reliability. "Under the processes-with-asynchronous-messages model, messages are sent from one process to a second one and stored in a *mailbox* inside the receiving process until they are taken out to be read." Messages are sent "without even checking if the receiving process exists, because it would not be useful to do so" — in a distributed system you cannot know whether a remote process will crash between sending and receiving, or whether it will act on the message. "Asynchronous messages allow safe remote function calls because there is no assumption about what will happen." If delivery confirmation is needed, "you must send a second message as a reply to the original process," which has the same safe semantics (Hébert, ch. 10, "Fault Tolerance").

## Prerequisites

- **Message passing** — Asynchrony is the defining property of Erlang's message passing

## Key Properties

1. Sending a message does not block the sender
2. Messages are not checked against the receiver's existence
3. Delivery is not guaranteed and not confirmed
4. The message is stored in the receiver's mailbox until read
5. Asynchrony makes remote calls safe — no assumption about the remote process's fate
6. Delivery confirmation, if needed, requires an explicit reply message
7. The same safe semantics apply to any library built on this principle

## Construction / Recognition

## To Use Asynchronous Message Passing

1. Send with `!`; do not expect blocking or confirmation
2. If you need to know a message was processed, design an explicit reply
3. Tie request and reply together with a reference so the reply is unambiguous
4. Treat remote and local sends identically — both are asynchronous

## Examples

> **No existence check** (ch. 10): "messages are sent without even checking if the receiving process exists, because it would not be useful to do so."
>
> **Confirmation by reply** (ch. 10): "if you need to have a confirmation of delivery, you must send a second message as a reply to the original process."

## Relationships

## Builds Upon

- **Message passing** — Asynchrony is its core property

## Related

- **Process mailbox** — Where asynchronously-sent messages wait
- **Shared-nothing isolation** — Asynchronous copied messages complement memory isolation

## Common Errors

- **Error**: Assuming a send blocks until the receiver processes the message
  **Correction**: Sending never blocks or confirms; build an explicit reply if confirmation matters

## Common Confusions

- **Confusion**: Thinking asynchrony is a limitation
  **Clarification**: It is a deliberate design choice that makes distribution and fault tolerance safe — no false assumptions about remote processes

## Source Reference

Chapter 10, "The Hitchhiker's Guide to Concurrency," section "Concurrency Concepts," subsection "Fault Tolerance."

## Verification Notes

- Rationale and confirmation-by-reply: directly from ch. 10
- Confidence: HIGH — explicitly discussed
