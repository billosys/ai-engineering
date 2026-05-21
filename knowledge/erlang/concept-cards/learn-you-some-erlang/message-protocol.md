---
concept: Message Protocol
slug: message-protocol
category: processes-concurrency
subcategory: application-design
tier: intermediate
source: "Learn You Some Erlang for Great Good!"
source_slug: learn-you-some-erlang
authors: "Fred Hébert"
chapter: "Designing a Concurrent Application"
chapter_number: 13
pdf_page: null
section: "Defining the Protocol"
extraction_confidence: high
aliases:
  - "protocol"
  - "process protocol"
prerequisites:
  - message-passing
  - process-monitor
extends: []
related:
  - concurrent-application-design
contrasts_with: []
answers_questions:
  - "How do I define the message protocol between Erlang processes?"
  - "Why are messages tagged with references?"
---

# Message Protocol

## Quick Definition

A message protocol is the explicit specification of every message processes exchange — their shapes and meanings. In Erlang, request messages are typically wrapped as `{Pid, Ref, Message}` so replies can be matched to requests.

## Core Definition

Once the process architecture is known, "it's a good idea to make a list of all messages that will be sent and specify what they will look like." The chapter draws each message between client, event server, and event processes, producing the protocol. It notes the protocol drawing is incomplete on its own — "it helps represent what data will be sent from process to process, but not the intricacies: how the addressing works, whether we use references or names." The convention adopted is to wrap messages as `{Pid, Ref, Message}`, where `Pid` is the sender and `Ref` is "a unique message identifier to help determine which reply came from which sender." Without a reference, "if we were to send many messages before looking for replies, we would not know which reply went with which message." Some messages omit the reference deliberately — e.g. the `{done, Name}` notification expects no specific reply (Hébert, ch. 13, "Defining the Protocol," "An Event Module").

## Prerequisites

- **Message passing** — A protocol is the disciplined use of message passing
- **Process monitor** — Monitors are part of the protocol (e.g. the client monitors the server)

## Key Properties

1. A protocol lists every message exchanged and its exact shape
2. Request/reply messages are wrapped `{Pid, Ref, Message}` — sender pid plus a unique reference
3. The reference matches each reply to its originating request when many are in flight
4. References are created with `make_ref()` or arise from starting a monitor
5. Some messages intentionally omit a reference (fire-and-forget notifications)
6. Drawing processes and their message arrows yields the protocol skeleton
7. Confirmations (e.g. the `ok` atom) and error replies (e.g. `{error, bad_timeout}`) are part of the protocol

## Construction / Recognition

## To Define a Message Protocol

1. List every message between every pair of processes
2. Decide each message's shape — wrap requests as `{Pid, Ref, Message}`
3. Generate a reference per request with `make_ref()` (or via a monitor)
4. Specify the reply for each request, including error and confirmation forms
5. Omit references only for messages with no expected reply
6. Keep protocol documentation updated as messages change

## Examples

> **Wrapped request** (ch. 13): `{Pid, Ref, Message}` — "where `Pid` is the sender and `Ref` is a unique message identifier."
>
> **Reference-tagged event cancel** (ch. 13): `Pid ! {self(), ReplyRef, cancel}` and the reply `{ReplyRef, ok}` so the caller knows the `ok` came from this process.
>
> **Unreferenced notification** (ch. 13): the `{done, Name}` message "is not [referenced], simply because we don't expect it to come from anywhere specific."

## Relationships

## Related

- **Concurrent application design** — Defining the protocol is a step of the overall design method

## Common Errors

- **Error**: Sending many requests without reference tags
  **Correction**: Tag requests with `make_ref()` so replies can be matched to the right request
- **Error**: Letting the protocol documentation drift from the code
  **Correction**: Update the protocol spec whenever messages change

## Common Confusions

- **Confusion**: Thinking a protocol drawing is the complete specification
  **Clarification**: The drawing shows message shapes but not addressing or reference details — those must be specified too

## Source Reference

Chapter 13, "Designing a Concurrent Application," sections "Defining the Protocol" and "An Event Module."

## Verification Notes

- Protocol method and `{Pid, Ref, Message}` convention: directly from ch. 13
- Confidence: HIGH — explicitly described
