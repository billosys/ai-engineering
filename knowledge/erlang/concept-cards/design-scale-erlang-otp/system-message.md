---
# === CORE IDENTIFICATION ===
concept: System Message
slug: system-message

# === CLASSIFICATION ===
category: otp-behaviours
subcategory: behavior-protocol
tier: intermediate

# === PROVENANCE ===
source: Designing for Scalability with Erlang/OTP
source_slug: design-scale-erlang-otp
authors: Francesco Cesarini & Steve Vinoski
chapter: "Controlling OTP Behaviors"
chapter_number: 4
pdf_page: 122
section: "System Messages"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - system event
  - "{in, Msg}"
  - "{out, Msg, To, State}"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - sys-tracing-and-logging
extends: []
related:
  - the-sys-module
  - custom-trace-functions
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How does gen_server message passing work under the hood?"
  - "How do I trace and inspect an OTP process with the sys module?"
---

# Quick Definition

A system message is a logged record of an event in a behavior process — most commonly an inbound message (`{in, Msg}`) or an outbound reply (`{out, Msg, To, State}`) — produced as part of the OTP message protocol and surfaced through `sys` tracing and logging.

# Core Definition

System messages are the events that appear in a behavior's `sys` log. "The forms of the events in the log depend on the processes producing them, but generally each event contains a system message" in one of a few forms (Cesarini & Vinoski, p. 122). The three forms documented are: `{in, Msg}`, triggered when a message (including a timeout) is sent to the `gen_server`, where `Msg` includes OTP protocol constructs like `{'$gen_cast', Msg}` and `{'$gen_call',{Pid,Ref}, Msg}`; `{out, Msg, To, State}`, generated when replying with a `{reply, Reply, NewState}` control tuple (but not for replies via `gen_server:reply/2`); and an arbitrary `term()`, since system messages of any format are allowed — for example `{noreply, NewState}` from `handle_cast/2` (pp. 122-123).

# Prerequisites

- **Behavior tracing and logging** — System messages are observed through `sys` logging; you retrieve them via `sys:log/2` with the `get` flag.

# Key Properties

1. `{in, Msg}` — fires when a message (including a timeout) arrives at the `gen_server`; `Msg` is the OTP construct or any plain Erlang term sent.
2. `{out, Msg, To, State}` — fires when replying via the `{reply, Reply, NewState}` control tuple; `To` is the client pid, `State` equals `NewState`.
3. `{out, ...}` is *not* generated for replies sent via `gen_server:reply/2`.
4. `term()` — any format is allowed; e.g., `{noreply, NewState}` after a `handle_cast/2`.
5. The legacy forms `{in, Msg, From}` and `{out, Msg, To}` are documented (up to Erlang 18) but not used by any standard behavior.

# Construction / Recognition

## To Retrieve System Messages:
1. Enable logging with `sys:log(Name, true)`.
2. Exercise the behavior.
3. Call `sys:log(Name, get)` to get back the list of system events.

## To Recognize System Messages:
1. Look at the elements of the list returned by `sys:log/2` with the `get` flag.
2. Match the leading tag — `in`, `out`, or an arbitrary term — to identify the event type.

# Context & Application

- **Typical contexts**: Inspecting the OTP message protocol while debugging a behavior.
- **Common applications**: Understanding what messages a behavior received and what it replied; feeding events to custom trace functions.
- **Historical/stylistic notes**: The authors warn that documentation through Erlang 18 lists extra forms that no standard behavior actually emits (p. 123).

# Examples

**Example 1** (p. 122): An `{in, {'$gen_call',{<0.33.0>,#Ref<...>}, {allocate,<0.33.0>}}}` event records an inbound `gen_server` call.

**Example 2** (p. 123): The `{noreply,{[10,11,12,13,14,15],[]}}` term in the log of shell command 9 is the result of `handle_cast/2` after a `deallocate` cast; the second element is the new state.

# Relationships

## Builds Upon
- **Behavior tracing and logging** — System messages are the content of trace and log output.

## Enables
- **custom-trace-functions** — Custom trace funs pattern match on system messages.

## Related
- **The sys module** — System messages flow through `sys` facilities.

## Contrasts With
- *(None.)*

# Common Errors

- **Error**: Expecting an `{out, ...}` system message after using `gen_server:reply/2`.
  **Correction**: The `{out, ...}` event is generated only for the `{reply, Reply, NewState}` control tuple, not for explicit `gen_server:reply/2` calls.

# Common Confusions

- **Confusion**: Believing system messages have a fixed, closed set of forms.
  **Clarification**: Any `term()` is a valid system message; `{in, ...}` and `{out, ...}` are just the most common forms produced by standard behaviors.

# Source Reference

Chapter 4: Controlling OTP Behaviors, Section "System Messages," pages 122-123.

# Verification Notes

- Definition source: Direct quotes from pp. 122-123.
- Confidence rationale: HIGH — the source enumerates and names each system message form explicitly.
- Uncertainties: None.
- Cross-reference status: Verified against planned cards in this batch.
- Re-extraction notes: Fresh extraction; no pre-existing card for this source.
