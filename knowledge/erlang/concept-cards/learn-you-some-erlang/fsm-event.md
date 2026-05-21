---
concept: FSM Event
slug: fsm-event
category: otp-behaviours
subcategory: state-machines
tier: intermediate
source: "Learn You Some Erlang for Great Good!"
source_slug: learn-you-some-erlang
authors: "Fred Hébert"
chapter: "Rage Against the Finite-State Machines"
chapter_number: 15
pdf_page: null
section: "The handle_sync_event Function"
extraction_confidence: high
aliases:
  - event
  - synchronous event
  - asynchronous event
  - global event
prerequisites:
  - gen-fsm
  - finite-state-machine
extends: []
related:
  - fsm-state-function
  - fsm-handle-event
  - fsm-state-data
contrasts_with: []
answers_questions:
  - "What is a finite-state-machine behaviour (gen_fsm / gen_statem)?"
  - "How do I implement a stateful process?"
---

# FSM Event

## Quick Definition

An FSM event is a message sent to a `gen_fsm` process that triggers a state transition. Events are synchronous or asynchronous, and either state-specific or global.

## Core Definition

In an Erlang FSM, events are "messages ... that force a state transition" (Ch. 15, opening). For `gen_fsm`, "rather than handling *calls* and *casts*, we're handling *synchronous* and *asynchronous* events." The book distinguishes events by how they are sent: "Asynchronous events aimed at any `StateName/2` function are sent with `gen_fsm:send_event/2`, and synchronous events to be picked up by `StateName/3` are sent with `gen_fsm:sync_send_event/2-3`. ... The two equivalent functions for global events are `gen_fsm:send_all_state_event/2` and `gen_fsm:sync_send_all_state_event/2-3`" (Ch. 15, "The handle_sync_event Function").

## Prerequisites

- **gen_fsm** — Events are the inputs `gen_fsm` dispatches.
- **finite-state-machine** — Events drive transitions in the FSM model.

## Key Properties

1. **Asynchronous events** — sent with `send_event/2`, fire-and-forget, handled by `StateName/2`.
2. **Synchronous events** — sent with `sync_send_event/2,3`, the caller blocks for a reply, handled by `StateName/3`.
3. **Global events** — handled the same way in every state, sent with `send_all_state_event/2` (async) or `sync_send_all_state_event/2,3` (sync).
4. The *send function* used determines whether an event is state-specific or global.
5. Synchronous global events go to `handle_sync_event/4`; asynchronous global events go to `handle_event/3`.
6. Two FSMs talking to each other should use asynchronous events to avoid deadlock.

## Construction / Recognition

## To Send an Event

1. State-specific async: `gen_fsm:send_event(Pid, Event)`.
2. State-specific sync: `gen_fsm:sync_send_event(Pid, Event)` (optional third arg = timeout).
3. Global async: `gen_fsm:send_all_state_event(Pid, Event)`.
4. Global sync: `gen_fsm:sync_send_all_state_event(Pid, Event)`.

## Context & Application

The book's `trade_fsm` cancel function is a global event: `cancel(OwnPid) -> gen_fsm:sync_send_all_state_event(OwnPid, cancel).` — cancellation must work in any state. By contrast `make_offer/2` uses `send_event` because offering items only matters during negotiation.

**OTP version note:** Under `gen_statem`, all events go through `gen_statem:cast/2`, `gen_statem:call/2,3`, or generic timeout/internal events; there is no separate "all-state" send function — global handling is expressed in the callbacks instead. The synchronous/asynchronous distinction persists.

## Examples

**Example 1** (Ch. 15): `make_offer(OwnPid, Item) -> gen_fsm:send_event(OwnPid, {make_offer, Item}).` — asynchronous, state-specific.

**Example 2** (Ch. 15): `trade(OwnPid, OtherPid) -> gen_fsm:sync_send_event(OwnPid, {negotiate, OtherPid}, 30000).` — synchronous with a 30-second timeout.

**Example 3** (Ch. 15): `notify_cancel(OtherPid) -> gen_fsm:send_all_state_event(OtherPid, cancel).` — asynchronous global event.

## Relationships

## Builds Upon

- **gen_fsm** — Events are how callers interact with a `gen_fsm`.

## Related

- **fsm-state-function** — State-specific events are handled by state functions.
- **fsm-handle-event** — Global events are handled by `handle_event`/`handle_sync_event`.
- **fsm-state-data** — Events update the carried state data.

## Common Errors

- **Error**: Two FSMs both making synchronous calls to each other.
  **Correction**: This causes a deadlock; communicate between FSMs asynchronously.
- **Error**: Expecting a state-specific event handler to receive a globally-sent event.
  **Correction**: The send function must match the handler — `send_event` reaches `StateName/2`, `send_all_state_event` reaches `handle_event/3`.

## Common Confusions

- **Confusion**: Thinking "synchronous" means the FSM processes events one at a time differently.
  **Clarification**: All events are processed one at a time; "synchronous" only means the *caller* waits for a reply.

## Source Reference

Chapter 15: "Rage Against the Finite-State Machines," sections "The handle_event Function," "The handle_sync_event Function," and "The Public Interface" / "FSM-to-FSM Functions."

## Verification Notes

- Definition: Direct quotes on send functions from "The handle_sync_event Function."
- Key Properties: Synthesised from the callback subsections and the deadlock discussion in "Show Me Your Moves."
- Confidence: HIGH — send functions and their pairings are explicitly stated.
