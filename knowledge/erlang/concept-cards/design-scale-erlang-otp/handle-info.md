---
# === CORE IDENTIFICATION ===
concept: Handling Non-OTP Messages (handle_info)
slug: handle-info

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
section: "Other Messages"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - handle_info
  - "handle_info/2"
  - other messages

# === TYPED RELATIONSHIPS ===
prerequisites:
  - gen-server
extends: []
related:
  - unhandled-messages
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How does a gen_server handle non-OTP messages?"
  - "What is the handle_info/2 callback for?"
---

# Quick Definition

`handle_info/2` is the `gen_server` callback that receives messages not sent through `call/2` or `cast/2` — such as `'EXIT'` signals, port/socket data, and monitor messages.

# Core Definition

"OTP behaviors are implemented as Erlang processes. So while communication should ideally occur through the protocols defined in the `gen_server:call/2` and `gen_server:cast/2` functions, that is not always the case" (Cesarini & Vinoski, p. 85). Such non-OTP messages "result in our server receiving Erlang messages that do not comply with the internal OTP messaging protocol. ... Generic servers provide a callback function that takes care of all of these messages. It is the `handle_info(_Msg, LoopData)` callback. When called, it has to return either the tuple `{noreply, NewLoopData}` or, when stopping, `{stop, Reason, NewLoopData}`" (pp. 85-86). "It is common practice, even if you are not expecting any messages, to include this callback function."

# Prerequisites

- **Gen_server** — `handle_info/2` is one of the `gen_server` callbacks.

# Key Properties

1. `handle_info(Msg, LoopData)` receives messages not sent via `call/2` or `cast/2`.
2. Such messages include `'EXIT'` signals, port/socket data, monitor and node-monitor messages.
3. The callback returns `{noreply, NewLoopData}` or `{stop, Reason, NewLoopData}`.
4. It should be included even when no such messages are expected.
5. Omitting it and receiving a non-OTP message causes an undefined-function error and server termination.

# Construction / Recognition

## To Construct:
1. Implement `handle_info(Msg, LoopData)` in the callback module.
2. Match expected messages (e.g., `{'EXIT', Pid, Reason}`) and handle them.
3. End with a catch-all clause returning `{noreply, LoopData}`, optionally logging the message.

## To Recognize:
1. A `handle_info/2` clause set in a `gen_server` callback module.

# Context & Application

- **Typical contexts**: Servers linked to processes/ports, using monitors, or interfacing legacy non-OTP code.
- **Common applications**: A minimal `handle_info(_Msg, LoopData) -> {noreply, LoopData}.` ignoring unexpected messages.
- **Historical/stylistic notes**: A catch-all may be the norm in `handle_info/2` (dealing with ports, sockets, links), unlike `handle_call`/`handle_cast` where unknown messages should crash.

# Examples

**Example 1** (p. 86): The minimal frequency-server `handle_info/2`:

```erlang
handle_info(_Msg, LoopData) ->
    {noreply, LoopData}.
```

**Example 2** (p. 86): Logging abnormal exits of linked processes:

```erlang
handle_info({'EXIT', _Pid, normal}, LoopData) ->
    {noreply, LoopData};
handle_info({'EXIT', Pid, Reason}, LoopData) ->
    io:format("Process: ~p exited with reason: ~p~n",[Pid, Reason]),
    {noreply, LoopData};
handle_info(_Msg, LoopData) ->
    {noreply, LoopData}.
```

# Relationships

## Builds Upon
- **Gen_server** — `handle_info/2` is a `gen_server` callback.

## Enables
- *(none specific in scope)*

## Related
- **Unhandled messages** — `handle_info/2` is where forgotten-message catch-alls belong.

## Contrasts With
- *(none)*

# Common Errors

- **Error**: Omitting `handle_info/2` from a server that may receive non-OTP messages.
  **Correction**: Always include it; otherwise an unexpected message triggers an undefined-function error and terminates the server.

# Common Confusions

- **Confusion**: Thinking a `gen_server` only ever receives `call`/`cast` messages.
  **Clarification**: Being an ordinary process, it can receive `Pid ! Msg` sends, `'EXIT'` signals, port data, and monitor messages — all routed to `handle_info/2`.

# Source Reference

Chapter 3: Generic Servers, Section "Other Messages," pages 85-87.

# Verification Notes

- Definition source: Direct quotes from pp. 85-86.
- Confidence rationale: HIGH — explicit definition with examples.
- Uncertainties: None.
- Cross-reference status: `unhandled-messages` is a planned Chapter 3 card.
- Re-extraction notes: Fresh extraction — no pre-existing card for this source.
</content>
</invoke>
