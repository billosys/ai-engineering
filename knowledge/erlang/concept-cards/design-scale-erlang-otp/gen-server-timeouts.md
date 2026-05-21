---
# === CORE IDENTIFICATION ===
concept: Generic Server Timeouts
slug: gen-server-timeouts

# === CLASSIFICATION ===
category: otp-behaviours
subcategory: gen-server
tier: intermediate

# === PROVENANCE ===
source: "Designing for Scalability with Erlang/OTP"
source_slug: design-scale-erlang-otp
authors: "Francesco Cesarini & Steve Vinoski"
chapter: "Generic Servers"
chapter_number: 3
pdf_page: 96
section: "Generic Server Timeouts"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - server-side timeout
  - timeout message
  - internal timeout

# === TYPED RELATIONSHIPS ===
prerequisites:
  - gen-server
extends: []
related:
  - handle-info
  - hibernating-behaviors
contrasts_with:
  - call-timeouts

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is a server-side timeout in a gen_server?"
  - "How does a gen_server trigger periodic actions?"
---

# Quick Definition

A generic-server timeout is a server-side timer set by adding a `Timeout` value to a callback's return tuple. If no message arrives within `Timeout` ms, the server receives a `timeout` message in `handle_info/2`.

# Core Definition

A server-side timeout is created "by adding a timeout value in the control tuples sent back as a result of the behavior callback functions" (Cesarini & Vinoski, p. 95): `init/1` → `{ok, LoopData, Timeout}`, `handle_call/3` → `{reply, Reply, LoopData, Timeout}`, `handle_cast/2`/`handle_info/2` → `{noreply, LoopData, Timeout}`. "The value Timeout is either an integer in milliseconds or the atom infinity. If the server does not receive a message in Timeout milliseconds, it receives a timeout message in its `handle_info/2` callback function" (p. 96). "We send a timeout message only if a message has not been received by the behavior. If a message is received ... the timer is reset."

# Prerequisites

- **Gen_server** — Server-side timeouts are configured through `gen_server` callback return tuples.

# Key Properties

1. A `Timeout` is added as an extra element of a callback's return tuple.
2. Valid on `init/1`, `handle_call/3`, `handle_cast/2`, and `handle_info/2` returns.
3. `Timeout` is an integer in milliseconds or the atom `infinity`.
4. If no message arrives within `Timeout` ms, the server gets a `timeout` message in `handle_info/2`.
5. Any incoming message resets the timer.
6. Returning `infinity` is equivalent to setting no timeout.
7. For timers that must fire regardless of incoming messages, use `erlang:send_after/3` or the `timer` module.

# Construction / Recognition

## To Construct:
1. Append a `Timeout` value to the callback's return tuple.
2. Implement `handle_info(timeout, LoopData)` to react when the timer fires.
3. Re-arm by including `Timeout` again in subsequent return tuples.

## To Recognize:
1. Callback return tuples with a trailing integer/`infinity`, plus a `handle_info(timeout, ...)` clause.

# Context & Application

- **Typical contexts**: A server that pings a device if it has heard nothing recently.
- **Common applications**: The `ping` example prints the current seconds every 5,000 ms of silence.
- **Historical/stylistic notes**: Server-side timeouts are reset by activity, so they are not regular-interval timers — use `timer` functions for that.

# Examples

**Example 1** (p. 96): The `ping` server timing out every 5 seconds:

```erlang
-define(TIMEOUT, 5000).
init(_Args) ->
    {ok, undefined, ?TIMEOUT}.
handle_call(start, _From, LoopData) ->
    {reply, started, LoopData, ?TIMEOUT};
handle_call(pause, _From, LoopData) ->
    {reply, paused, LoopData}.
handle_info(timeout, LoopData) ->
    {_Hour,_Min,Sec} = time(),
    io:format("~2.w~n",[Sec]),
    {noreply, LoopData, ?TIMEOUT}.
```

The `pause` clause omits the timeout, suspending the timer; `start` re-arms it.

# Relationships

## Builds Upon
- **Gen_server** — Server-side timeouts are part of the `gen_server` callback protocol.

## Enables
- *(none specific in scope)*

## Related
- **Handle_info** — The `timeout` message is delivered to `handle_info/2`.
- **Hibernating behaviors** — `hibernate` is an alternative value returned in the same tuple position.

## Contrasts With
- **Call timeouts** — Call timeouts are client-side limits on `gen_server:call`; server-side timeouts fire when the *server* hears nothing.

# Common Errors

- **Error**: Expecting a server-side timeout to fire at regular intervals.
  **Correction**: Any received message resets it; for fixed-interval timers use `erlang:send_after/3` or `timer` functions.

# Common Confusions

- **Confusion**: Confusing a server-side timeout with a `gen_server:call` timeout.
  **Clarification**: A server-side timeout fires when the server receives no messages; a call timeout limits how long a client waits for a reply.

# Source Reference

Chapter 3: Generic Servers, Section "Generic Server Timeouts," pages 95-97.

# Verification Notes

- Definition source: Direct quotes from pp. 95-96.
- Confidence rationale: HIGH — explicit treatment with the `ping` example.
- Uncertainties: None.
- Cross-reference status: Verified against planned cards.
- Re-extraction notes: Fresh extraction — no pre-existing card for this source.
</content>
</invoke>
