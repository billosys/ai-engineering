---
concept: FSM Deadlock Avoidance
slug: fsm-deadlock-avoidance
category: otp-behaviours
subcategory: state-machines
tier: advanced
source: "Learn You Some Erlang for Great Good!"
source_slug: learn-you-some-erlang
authors: "Fred Hébert"
chapter: "Rage Against the Finite-State Machines"
chapter_number: 15
pdf_page: null
section: "Show Me Your Moves"
extraction_confidence: high
aliases:
  - deadlock avoidance
  - peer FSM communication
prerequisites:
  - finite-state-machine
  - fsm-event
extends: []
related:
  - fsm-event
  - gen-fsm
contrasts_with: []
answers_questions:
  - "What is a finite-state-machine behaviour (gen_fsm / gen_statem)?"
  - "How do I implement a stateful process?"
---

# FSM Deadlock Avoidance

## Quick Definition

When two FSMs communicate as peers, they must use asynchronous events. If both make synchronous calls to each other simultaneously, each blocks waiting for the other — a deadlock.

## Core Definition

"The first thing to notice when we have two identical processes communicating with each other is that we need to avoid synchronous calls as much as possible. If Jim's FSM sends a message to your FSM and then waits for its reply, while at the same time, your FSM sends a message over to Jim's FSM and waits for its own specific reply, both end up waiting for the other without ever replying. ... We have a *deadlock*" (Ch. 15, "Show Me Your Moves").

## Prerequisites

- **Finite-state machine** — The problem arises when two FSMs interact.
- **FSM event** — The fix uses asynchronous events.

## Key Properties

1. Two peers each making a blocking synchronous call to the other deadlock.
2. The solution is to go fully asynchronous between the two FSMs.
3. A timeout-then-continue workaround leaves leftover messages in mailboxes and corrupts the protocol — it is rejected.
4. A client may still call its *own* FSM synchronously, since the FSM never calls back into the client — no cycle exists.
5. Asynchronous peer communication requires intermediary "wait" states to synchronise the two FSMs.

## Construction / Recognition

## To Avoid Deadlock Between FSMs

1. Identify any cycle of synchronous calls between processes.
2. Make all FSM-to-FSM messages asynchronous (`gen_fsm:send_event`).
3. Keep client-to-own-FSM calls synchronous where it simplifies logic — there is no cycle there.
4. Add intermediary states (e.g. `idle_wait`, `wait`) to coordinate the async exchange.

## Context & Application

The `trade_fsm` design is "fully asynchronous" between the two players' FSMs precisely to avoid this deadlock, while each player may still call their own FSM synchronously. The asynchronous design forces extra states and careful handling of race conditions — e.g. both players asking to trade at the same instant, or item offers arriving after a "ready" declaration.

## Examples

**Example 1** (Ch. 15): Jim's FSM and your FSM each `sync_send_event` to the other and block — neither ever replies; the protocol is designed asynchronously to prevent this.

**Example 2** (Ch. 15): `trade/2` is synchronous (`sync_send_event`) because it is a *client* calling its *own* FSM; `ask_negotiate/2` is asynchronous (`send_event`) because it is FSM-to-FSM.

## Relationships

## Builds Upon

- **Finite-state machine** — Deadlock is a hazard of inter-FSM communication.

## Related

- **fsm-event** — Asynchronous events are the deadlock-free choice between FSMs.
- **gen-fsm** — The behaviour whose `send_event` vs `sync_send_event` choice matters here.

## Common Errors

- **Error**: Using `sync_send_event` for FSM-to-FSM messages.
  **Correction**: Use `send_event`; reserve synchronous calls for the non-cyclic client-to-own-FSM direction.
- **Error**: "Fixing" a deadlock with a timeout.
  **Correction**: Timeouts leave stale messages in mailboxes and corrupt the protocol; redesign asynchronously instead.

## Common Confusions

- **Confusion**: Thinking all FSM communication must be asynchronous.
  **Clarification**: Only the *cyclic* peer-to-peer direction must be async; a client calling its own FSM synchronously is safe because no cycle exists.

## Source Reference

Chapter 15: "Rage Against the Finite-State Machines," section "Show Me Your Moves."

## Verification Notes

- Definition: Direct quote from "Show Me Your Moves."
- Key Properties: Synthesised from the deadlock discussion and the `trade_fsm` API design.
- Confidence: HIGH — explicitly discussed.
