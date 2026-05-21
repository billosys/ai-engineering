---
concept: Message Passing
slug: message-passing
category: processes-concurrency
subcategory: concurrency-primitives
tier: foundational
source: "Learn You Some Erlang for Great Good!"
source_slug: learn-you-some-erlang
authors: "Fred Hébert"
chapter: "The Hitchhiker's Guide to Concurrency"
chapter_number: 10
pdf_page: null
section: "Sending Messages"
extraction_confidence: high
aliases:
  - "send operator"
  - "bang operator"
  - "!"
prerequisites:
  - process
  - spawn
extends: []
related:
  - process-mailbox
  - receive-expression
contrasts_with: []
answers_questions:
  - "How do I spawn a process and send it messages?"
  - "How does selective receive relate to the process mailbox?"
---

# Message Passing

## Quick Definition

Message passing is how Erlang processes communicate. The `!` ("bang") operator sends any Erlang term to a process identified by a pid; the message is copied into that process's mailbox asynchronously.

## Core Definition

Message passing is the second concurrency primitive. The operator `!`, "also known as the *bang* symbol," takes a pid on its left and any Erlang term on its right; "the term is then sent to the process represented by the pid, which can access it." Sending is *asynchronous*: messages are placed in the receiving process's mailbox without checking whether the receiver even exists, "because it would not be useful to do so" — you cannot know if a remote process will crash before receiving. If you need delivery confirmation, you must send a reply message. The return value of `!` is the message itself, so sends can be chained: `self() ! self() ! double` is `self() ! (self() ! double)` (Hébert, ch. 10, "Sending Messages").

## Prerequisites

- **Process** — Messages are sent between processes
- **Spawn** — You need a pid (from `spawn` or `self/0`) to address a message

## Key Properties

1. The `!` operator sends a term to a pid
2. Sending is asynchronous — it does not block or verify the receiver exists
3. The message (any Erlang term) is copied, not shared
4. `!` returns the message sent, so sends can be chained
5. To get a reply, the sender must include its own pid so the receiver can answer
6. Asynchrony makes remote calls safe — no assumption about what happens after sending

## Construction / Recognition

## To Send a Message

1. Obtain the target pid (from `spawn`, `self/0`, or `whereis/1`)
2. Send: `Pid ! Message`
3. To allow a reply, package your pid: `Pid ! {self(), Request}`
4. Then `receive` the reply, matching on your own pid or a reference

## Examples

> **Basic send** (ch. 10): `self() ! hello.` puts `hello` in the current process's mailbox.
>
> **Chained sends** (ch. 10): `self() ! self() ! double.` sends `double` twice.
>
> **Reply address** (ch. 10): `dolphin2` accepts `{From, fish}` and answers with `From ! "So long and thanks for all the fish!"`.

## Relationships

## Builds Upon

- **Process** — Messages travel between processes
- **Spawn** — Provides the pid used to address messages

## Related

- **Process mailbox** — Where sent messages are stored until read
- **Receive expression** — How a process consumes messages from its mailbox

## Common Errors

- **Error**: Assuming a sent message was received because `!` succeeded
  **Correction**: `!` is asynchronous and never confirms delivery; send a reply message if you need confirmation
- **Error**: Sending a request without an address and expecting an answer
  **Correction**: Package `self()` (and ideally a reference) in the message so the receiver can reply

## Common Confusions

- **Confusion**: Thinking the message is shared with the receiver
  **Clarification**: Messages are copied; processes share no memory
- **Confusion**: Believing `!` to a dead process raises an error
  **Clarification**: Sending to a pid does not check existence; the message simply vanishes (sending to a registered name that is absent does raise `badarg`)

## Source Reference

Chapter 10, "The Hitchhiker's Guide to Concurrency," section "So Long and Thanks for All the Fish!", subsection "Sending Messages."

## Verification Notes

- Definition of `!` and asynchrony: directly from ch. 10
- Confidence: HIGH — explicitly defined with examples
