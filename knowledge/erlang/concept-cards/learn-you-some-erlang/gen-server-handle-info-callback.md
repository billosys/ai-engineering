---
concept: gen_server handle_info Callback
slug: gen-server-handle-info-callback
category: otp-behaviours
subcategory: gen-server-callbacks
tier: intermediate
source: "Learn You Some Erlang for Great Good!"
source_slug: learn-you-some-erlang
authors: "Fred Hébert"
chapter: "An Introduction to OTP"
chapter_number: 14
pdf_page: null
section: "The handle_info Function"
extraction_confidence: high
aliases:
  - "handle_info/2"
  - "handle_info callback"
prerequisites:
  - gen-server
  - synchronous-call-and-cast
extends: []
related:
  - exit-signal
  - process-monitor
contrasts_with: []
answers_questions:
  - "What does the gen_server handle_info/2 callback do?"
  - "How does a gen_server handle messages outside its call/cast interface?"
---

# gen_server handle_info Callback

## Quick Definition

`handle_info/2` is the `gen_server` callback for messages that arrive outside the `call`/`cast` interface — raw `!` sends, monitor `DOWN` notifications, `EXIT` signals, and `init/1` timeouts.

## Core Definition

The hand-written `my_server` "didn't really deal with messages that do not fit our interface. Well, `handle_info/2` is the solution." It "is very similar to `handle_cast/2`, and in fact, returns the same tuples" — `{noreply, NewState}`, `{noreply, NewState, TimeOut}`, `{noreply, NewState, hibernate}`, `{stop, Reason, NewState}`. The difference is the source of the messages it handles: "messages that were sent directly with the `!` operator and special ones like `init/1`'s `timeout`, monitors' notifications, and `EXIT` signals." The chapter's rule of thumb: "always log unexpected messages in `handle_cast/2` and `handle_info/2`" (Hébert, ch. 14, "The handle_info Function").

## Prerequisites

- **gen_server** — `handle_info/2` is a `gen_server` callback
- **Synchronous call and cast** — `handle_info/2` handles what `handle_call`/`handle_cast` do not

## Key Properties

1. Handles messages that do not come through `call` or `cast`
2. Sources include raw `!` sends, monitor `DOWN` messages, `EXIT` signals, and the `init/1` `timeout`
3. Returns the same tuples as `handle_cast/2`: `{noreply, ...}` and `{stop, ...}` variants
4. Cannot send a reply (no `reply` tuple) — the messages it handles have no waiting caller
5. Best practice: always log unexpected messages here

## Construction / Recognition

## To Write handle_info/2

1. Define `handle_info(Message, State)` in the callback module
2. Match the expected out-of-band messages (`{'DOWN', ...}`, `{'EXIT', ...}`, `timeout`)
3. Add a catch-all clause that logs unexpected messages
4. Return `{noreply, NewState}` or a `{stop, Reason, NewState}` tuple

## Examples

> **Logging unexpected messages** (ch. 14): `handle_info(Msg, Cats) -> io:format("Unexpected message: ~p~n",[Msg]), {noreply, Cats}.`
>
> **Triggered by a raw send** (ch. 14): `Pid ! <<"Test handle_info">>` prints `Unexpected message: <<"Test handle_info">>` via `handle_info/2`.

## Relationships

## Builds Upon

- **gen_server** — `handle_info/2` is one of its callbacks

## Related

- **Exit signal** — Trapped `EXIT` signals arrive at `handle_info/2`
- **Process monitor** — Monitor `DOWN` notifications arrive at `handle_info/2`

## Common Errors

- **Error**: Returning a `reply` tuple from `handle_info/2`
  **Correction**: Only `noreply`/`stop` tuples are valid — these messages have no waiting caller
- **Error**: Omitting a catch-all clause, crashing on an unexpected message
  **Correction**: Add a catch-all that logs the message and returns `{noreply, State}`

## Common Confusions

- **Confusion**: Thinking all messages reach `handle_call`/`handle_cast`
  **Clarification**: Only `gen_server:call`/`cast` messages do; everything else goes to `handle_info/2`

## Source Reference

Chapter 14, "An Introduction to OTP," section "Callback to the Future," subsection "The handle_info Function."

## Verification Notes

- Definition, message sources, return tuples: directly from ch. 14
- Confidence: HIGH — explicitly described
