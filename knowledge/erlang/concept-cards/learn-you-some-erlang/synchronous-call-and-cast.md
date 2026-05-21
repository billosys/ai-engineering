---
concept: Synchronous Call and Cast
slug: synchronous-call-and-cast
category: otp-behaviours
subcategory: gen-server
tier: intermediate
source: "Learn You Some Erlang for Great Good!"
source_slug: learn-you-some-erlang
authors: "Fred Hébert"
chapter: "An Introduction to OTP"
chapter_number: 14
pdf_page: null
section: "Generalizing the Server Loop"
extraction_confidence: high
aliases:
  - "call and cast"
  - "synchronous and asynchronous calls"
  - "gen_server:call/cast"
prerequisites:
  - message-passing
  - process-monitor
extends: []
related:
  - gen-server
  - receive-timeout
contrasts_with: []
answers_questions:
  - "What distinguishes a synchronous call from an asynchronous cast?"
  - "How do gen_server call and cast differ?"
---

# Synchronous Call and Cast

## Quick Definition

A *call* is a synchronous request: the caller sends a message and blocks waiting for a reply. A *cast* is an asynchronous request: the caller fires a message and returns immediately without waiting.

## Core Definition

While generalizing the server, the chapter makes the synchronous/asynchronous distinction explicit. A synchronous `call` "would be pretty helpful if our generic server implementation could provide a clear way to know which kind of call is which." It tags messages: `call/2` sends `{sync, self(), Ref, Msg}`, monitors the server, and `receive`s `{Ref, Reply}` with a 5-second timeout that crashes on expiry. A `cast/2` sends `{async, Msg}` and immediately returns `ok` — no reply. The server loop matches `{sync, Pid, Ref, Msg}` and `{async, Msg}` separately, dispatching to `handle_call` and `handle_cast`. A `reply/2` function (`reply({Pid, Ref}, Reply) -> Pid ! {Ref, Reply}`) hides the reference. In `gen_server` these become `gen_server:call/2-3` and `gen_server:cast/2`, mapping to `handle_call/3` and `handle_cast/2` (Hébert, ch. 14, "Generalizing the Server Loop," ".BEAM Me Up, Scotty!").

## Prerequisites

- **Message passing** — Both call and cast are built on `!`
- **Process monitor** — A synchronous call monitors the server to detect a crash while waiting

## Key Properties

1. A call is synchronous — the caller blocks until a reply arrives
2. A cast is asynchronous — the caller returns immediately, no reply
3. A call monitors the target so a server crash surfaces as an error instead of a hang
4. A call uses a timeout (default 5 seconds in `gen_server`); expiry crashes the caller
5. A cast returns `ok` immediately regardless of the server's outcome
6. Calls map to `handle_call/3` (which returns a `reply` tuple); casts map to `handle_cast/2`
7. A reply may be deferred: `handle_call` can return `noreply` and reply later via `gen_server:reply/2`

## Construction / Recognition

## To Choose and Use Call vs. Cast

1. Use a *call* when you need the result or confirmation that the work completed
2. Use a *cast* when you only need to fire-and-forget and do not need a reply
3. For a call: `gen_server:call(Pid, Request)` (optionally with a timeout)
4. For a cast: `gen_server:cast(Pid, Request)` — returns `ok` immediately
5. In the callback, handle calls in `handle_call/3` and casts in `handle_cast/2`
6. To answer a call later, return `noreply` and use `gen_server:reply/2`

## Examples

> **Tagged messages** (ch. 14): `call/2` sends `{sync, self(), Ref, Msg}`; `cast/2` sends `{async, Msg}` and returns `ok`.
>
> **Kitty server** (ch. 14): `order_cat/4` is a synchronous `gen_server:call`; `return_cat/2` is an asynchronous `gen_server:cast`.
>
> **reply hides the reference** (ch. 14): `reply({Pid, Ref}, Reply) -> Pid ! {Ref, Reply}.`

## Relationships

## Related

- **gen_server** — Provides `call/2-3` and `cast/2` as the standard API
- **Receive timeout** — A synchronous call uses a timeout to avoid waiting forever

## Common Errors

- **Error**: Using a cast when the caller actually needs the result
  **Correction**: A cast returns `ok` immediately and gives no result; use a call
- **Error**: Returning `noreply` from `handle_call/3` and never replying
  **Correction**: With `noreply` you must call `gen_server:reply/2`, or the call times out and crashes

## Common Confusions

- **Confusion**: Thinking a cast confirms the server received and processed the message
  **Clarification**: A cast is fire-and-forget; its `ok` only means the message was sent
- **Confusion**: Believing a call's timeout means the request failed
  **Clarification**: The timeout only means no reply arrived in time; the request's actual outcome is unknown

## Source Reference

Chapter 14, "An Introduction to OTP," sections "Generalizing the Server Loop," "Callback to the Future" (handle_call / handle_cast), ".BEAM Me Up, Scotty!".

## Verification Notes

- sync/async tagging, reply, gen_server mapping: directly from ch. 14
- Confidence: HIGH — explicitly demonstrated
