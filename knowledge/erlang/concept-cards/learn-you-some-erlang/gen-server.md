---
concept: gen_server
slug: gen-server
category: otp-behaviours
subcategory: gen-server
tier: intermediate
source: "Learn You Some Erlang for Great Good!"
source_slug: learn-you-some-erlang
authors: "Fred Hébert"
chapter: "An Introduction to OTP"
chapter_number: 14
pdf_page: null
section: "Callback to the Future"
extraction_confidence: high
aliases:
  - "gen_server"
  - "generic server"
prerequisites:
  - otp-behaviour
  - process-state-loop
extends:
  - otp-behaviour
related:
  - otp-callback-module
  - synchronous-call-and-cast
  - the-otp-way
contrasts_with: []
answers_questions:
  - "What is the gen_server behaviour?"
  - "How does gen_server relate to the client/server pattern?"
  - "How do I write a gen_server?"
---

# gen_server

## Quick Definition

`gen_server` is the OTP behaviour for the client/server pattern. It supplies the generic, battle-tested server machinery; the user provides a callback module implementing `init/1`, `handle_call/3`, `handle_cast/2`, `handle_info/2`, `terminate/2`, and `code_change/3`.

## Core Definition

`gen_server` is "a bit like `my_server` on steroids, except it has years and years of testing and production use behind it." It abstracts the client/server pattern: the server receives calls from clients, acts, and may reply. The chapter builds up to it by hand-writing `my_server` and then notes all the things `my_server` does not handle — named processes, configurable timeouts, debug info, unexpected messages, hot code loading, supervisor integration — "the Erlang/OTP team managed to handle all of that with the `gen_server` behavior." A `gen_server` callback module declares `-behavior(gen_server)` and implements six callbacks. The relationship between API calls and callbacks is fixed: `start`/`start_link` → `init/1`, `call/2-3` → `handle_call/3`, `cast/2` → `handle_cast/2`, plus `handle_info/2`, `terminate/2`, and `code_change/3` for special cases (Hébert, ch. 14, "Specific vs. Generic," "Callback to the Future," ".BEAM Me Up, Scotty!").

## Prerequisites

- **OTP behaviour** — `gen_server` is a behaviour; you must understand the behaviour/callback contract
- **Process state loop** — `gen_server` is the generic form of the hand-written server loop

## Key Properties

1. `gen_server` implements the generic client/server pattern
2. The user provides a callback module declaring `-behavior(gen_server)`
3. Six callbacks: `init/1`, `handle_call/3`, `handle_cast/2`, `handle_info/2`, `terminate/2`, `code_change/3`
4. API functions map fixed-ly to callbacks (call→handle_call, cast→handle_cast, start→init)
5. `gen_server:start_link(Module, Args, Options)` returns `{ok, Pid}` (not a bare pid)
6. `gen_server:call/2-3` has a default 5-second timeout; the call crashes on timeout
7. It handles named processes, debug info, unexpected messages, code loading, and supervisor integration for you
8. Years of production hardening make it safer and faster than hand-rolled servers

## Construction / Recognition

## To Write a gen_server

1. Create a module and declare `-behavior(gen_server).`
2. Write `start_link/0` calling `gen_server:start_link(?MODULE, [], [])`
3. Write client API functions that call `gen_server:call/2` or `gen_server:cast/2`
4. Implement `init/1` returning `{ok, State}`
5. Implement `handle_call/3` returning `{reply, Reply, NewState}` (or `noreply`/`stop` variants)
6. Implement `handle_cast/2` returning `{noreply, NewState}` (or a `stop` variant)
7. Implement `handle_info/2`, `terminate/2`, and `code_change/3`

## Examples

> **Behaviour declaration** (ch. 14): `-module(kitty_gen_server). -behavior(gen_server).`
>
> **start_link** (ch. 14): `start_link() -> gen_server:start_link(?MODULE, [], []).` returns `{ok, Pid}`.
>
> **handle_call** (ch. 14): `handle_call(terminate, _From, Cats) -> {stop, normal, ok, Cats}.`
>
> **handle_info** (ch. 14): `Pid ! <<"Test handle_info">>` prints `Unexpected message: <<"Test handle_info">>` via the `handle_info/2` callback.

## Relationships

## Builds Upon

- **OTP behaviour** — `gen_server` is a specific OTP behaviour
- **Process state loop** — It generalizes the hand-written server loop

## Related

- **OTP callback module** — The user module that supplies the `gen_server` callbacks
- **Synchronous call and cast** — The `call` vs. `cast` distinction `gen_server` formalizes
- **The OTP way** — `gen_server` is the canonical example of OTP's generic/specific split

## Common Errors

- **Error**: Returning `ok` instead of `exit(normal)`/a `stop` tuple from a terminating handler
  **Correction**: Use a `{stop, Reason, ...}` tuple so the server actually stops
- **Error**: Using `noreply` from `handle_call/3` and never calling `gen_server:reply/2`
  **Correction**: With `noreply` you must send the reply yourself, or the call times out and crashes

## Common Confusions

- **Confusion**: Expecting `gen_server:start_link` to return a bare pid like `spawn`
  **Clarification**: It returns `{ok, Pid}`
- **Confusion**: Thinking `gen_server` is fundamentally different from a hand-written server
  **Clarification**: It is the same client/server pattern, just generic, complete, and production-hardened

## Source Reference

Chapter 14, "An Introduction to OTP," sections "The Basic Server," "Specific vs. Generic," "Callback to the Future," ".BEAM Me Up, Scotty!".

## Verification Notes

- Callbacks, call/callback mapping, 5-second timeout: directly from ch. 14
- Confidence: HIGH — the chapter is a worked `gen_server` walkthrough
