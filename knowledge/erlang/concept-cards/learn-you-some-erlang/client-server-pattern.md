---
concept: Client/Server Pattern
slug: client-server-pattern
category: processes-concurrency
subcategory: process-design
tier: intermediate
source: "Learn You Some Erlang for Great Good!"
source_slug: learn-you-some-erlang
authors: "Fred Hébert"
chapter: "An Introduction to OTP"
chapter_number: 14
pdf_page: null
section: "The Basic Server"
extraction_confidence: high
aliases:
  - "client/server model"
  - "basic server"
prerequisites:
  - process-state-loop
  - synchronous-call-and-cast
extends: []
related:
  - gen-server
  - the-otp-way
contrasts_with: []
answers_questions:
  - "What is the client/server pattern in Erlang?"
  - "How does gen_server relate to the client/server pattern?"
---

# Client/Server Pattern

## Quick Definition

The client/server pattern is a recurring Erlang process design where a long-lived server process receives requests from client processes, acts on them, and replies if the protocol requires. It is the pattern `gen_server` abstracts.

## Core Definition

The common pattern explored in chapter 14 "is one we've already used. For the event server we wrote in Chapter 13, we used a *client/server* model. The event server receives calls from the client, acts on them, and then replies to the client if the protocol says to do so." The chapter develops it with a concrete example (the kitty server) and the generic `my_server` abstraction, observing that every server has the same recurring parts: spawning, initialization, a synchronous-call path, an asynchronous-cast path, a main loop, and termination. Extracting these generic parts into a reusable module — leaving only the specific request handling to the application — is the essence of the OTP approach, and `gen_server` is its production-hardened realization (Hébert, ch. 14, "The Basic Server," "Specific vs. Generic").

## Prerequisites

- **Process state loop** — A server is a stateful process with a receive-recurse loop
- **Synchronous call and cast** — Clients interact via synchronous calls and asynchronous casts

## Key Properties

1. A long-lived server process holds state and serves requests
2. Client processes send requests; the server acts and optionally replies
3. Synchronous requests (calls) block the client for a reply; asynchronous ones (casts) do not
4. Every server shares the same generic parts: spawn, init, call path, cast path, loop, terminate
5. The specific part — request handling — changes from application to application
6. Extracting the generic parts yields a reusable server abstraction (`my_server`, then `gen_server`)

## Construction / Recognition

## To Build a Client/Server

1. Write a server module with `start`/`start_link` and an `init` that sets up state
2. Write a main loop that `receive`s requests and recurses with updated state
3. Provide client API functions that hide the message protocol
4. Distinguish synchronous calls from asynchronous casts
5. For production, use `gen_server` instead of hand-writing the generic machinery

## Examples

> **Event server** (ch. 14): "the event server receives calls from the client, acts on them, and then replies to the client if the protocol says to do so."
>
> **Kitty server** (ch. 14): a simple server where you describe a cat and receive that cat — used to expose the pattern's essential parts.

## Relationships

## Related

- **gen_server** — The OTP behaviour that abstracts the client/server pattern
- **The OTP way** — Extracting the generic server is the canonical example of OTP's philosophy

## Common Errors

- **Error**: Re-implementing the generic server machinery for each new server
  **Correction**: Use `gen_server`; write only the specific request handling

## Common Confusions

- **Confusion**: Thinking client/server requires networking
  **Clarification**: Here client and server are just processes; the pattern is purely about message-based request/response

## Source Reference

Chapter 14, "An Introduction to OTP," sections "The Basic Server" and "Specific vs. Generic."

## Verification Notes

- Pattern description: directly from ch. 14
- Confidence: HIGH — explicitly identified as the chapter's central pattern
