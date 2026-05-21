---
concept: Hide Your Messages
slug: hide-your-messages
category: processes-concurrency
subcategory: application-design
tier: intermediate
source: "Learn You Some Erlang for Great Good!"
source_slug: learn-you-some-erlang
authors: "Fred Hébert"
chapter: "Designing a Concurrent Application"
chapter_number: 13
pdf_page: null
section: "I Said, Hide Your Messages"
extraction_confidence: high
aliases:
  - "interface functions"
  - "message hiding"
  - "API functions"
prerequisites:
  - message-passing
  - process-state-loop
extends:
  - process-state-loop
related:
  - message-protocol
contrasts_with: []
answers_questions:
  - "Why should I hide a process's messages behind interface functions?"
  - "How do I expose a process's functionality cleanly?"
---

# Hide Your Messages

## Quick Definition

"Hide your messages" is the design principle that a process's message protocol should be wrapped in interface functions, so callers invoke ordinary functions instead of constructing and matching raw messages.

## Core Definition

The chapter states the rule emphatically: "Hide messages! If you expect people to build on your code and processes, you must hide the messages in interface functions." For the `evserv` event server it provides `start/0`, `start_link/0`, `terminate/0`, `subscribe/1`, `add_event/3`, and `cancel/1` — each wrapping the underlying `!`/`receive` exchange. Interface functions hide the `{self(), Ref, Message}` wire format, generate references with `make_ref()`, set up monitors where the protocol requires, and apply timeouts. They also let the library author choose error handling — e.g. `add_event/3` forwards `{error, bad_timeout}` while `add_event2/3` instead crashes the caller with `erlang:error(Reason)` (a choice "still debated in the community"). The same chapter also hides process creation behind `start`/`start_link` functions using `register/2` and `?MODULE` (Hébert, ch. 13, "I Said, Hide Your Messages").

## Prerequisites

- **Message passing** — Interface functions wrap raw `!`/`receive`
- **Process state loop** — The hidden loop is what the interface functions front

## Key Properties

1. Every interaction with a process is exposed as an ordinary function call
2. Interface functions hide the message wire format (`{Pid, Ref, Message}`)
3. They generate references, set up monitors, and apply timeouts internally
4. They let the library author centralize error-handling policy (forward vs. crash)
5. `start`/`start_link` functions hide spawning and registration
6. Callers gain a simple API and never depend on protocol internals

## Construction / Recognition

## To Hide a Process's Messages

1. For each protocol message, write an interface function (e.g. `add_event/3`)
2. Inside it, build the message, generate a `make_ref()`, and send via `!`
3. `receive` the reply, matching on the reference, with an `after` timeout
4. Decide whether to forward errors as return values or crash the caller
5. Provide `start`/`start_link` functions that hide spawn and `register`

## Examples

> **add_event/3** (ch. 13): sends `{self(), Ref, {add, Name, Description, TimeOut}}` and receives `{Ref, Msg}` with `after 5000 -> {error, timeout}` — the caller never sees the message format.
>
> **Forward vs. crash** (ch. 13): `add_event/3` forwards `{error, bad_timeout}`; `add_event2/3` does `{Ref, {error, Reason}} -> erlang:error(Reason)` instead.
>
> **Hidden start** (ch. 13): `start() -> register(?MODULE, Pid=spawn(?MODULE, init, [])), Pid.`

## Relationships

## Builds Upon

- **Process state loop** — The interface functions are the public face of the hidden loop

## Related

- **Message protocol** — Interface functions implement the protocol so callers need not

## Common Errors

- **Error**: Letting callers construct protocol messages and send them directly
  **Correction**: Provide interface functions; never expose the wire format
- **Error**: Spreading `spawn`/`register` calls across many call sites
  **Correction**: Hide creation behind `start`/`start_link`

## Common Confusions

- **Confusion**: Thinking message hiding is just cosmetic
  **Clarification**: It decouples callers from protocol internals, enabling the protocol to change without breaking users

## Source Reference

Chapter 13, "Designing a Concurrent Application," section "The Event Server," subsection "I Said, Hide Your Messages."

## Verification Notes

- Principle and `evserv` interface functions: directly from ch. 13
- Confidence: HIGH — explicitly stated and demonstrated
