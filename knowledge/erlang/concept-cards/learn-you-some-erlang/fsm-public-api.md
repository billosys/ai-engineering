---
concept: FSM Public API
slug: fsm-public-api
category: otp-behaviours
subcategory: state-machines
tier: intermediate
source: "Learn You Some Erlang for Great Good!"
source_slug: learn-you-some-erlang
authors: "Fred Hébert"
chapter: "Rage Against the Finite-State Machines"
chapter_number: 15
pdf_page: null
section: "The Public Interface"
extraction_confidence: high
aliases:
  - FSM interface module
  - FSM API wrapper
prerequisites:
  - gen-fsm
  - fsm-event
extends: []
related:
  - fsm-event
  - gen-fsm
contrasts_with: []
answers_questions:
  - "How does a behaviour relate to its callback module?"
  - "How do I implement a stateful process?"
---

# FSM Public API

## Quick Definition

The FSM public API is the set of named functions a `gen_fsm` module exports for callers, wrapping the raw `gen_fsm:send_event`/`sync_send_event` calls behind a readable interface.

## Core Definition

The book builds a "public API according to the ... protocol definition" for `trade_fsm`, separate from the `gen_fsm` callbacks. There are three kinds of caller — "the player, the `gen_fsm` behavior, and the other player's FSM" — but only the player-facing functions and `gen_fsm` callbacks are exported; the FSM-to-FSM functions stay internal to the module (Ch. 15, "The Public Interface").

## Prerequisites

- **gen_fsm** — The API wraps `gen_fsm` send functions.
- **fsm-event** — The API decides which events are synchronous, asynchronous, or global.

## Key Properties

1. Each public function wraps one `gen_fsm:send_event` / `sync_send_event` / `*_all_state_event` call.
2. It hides the FSM's message protocol from callers.
3. Client-facing functions are often synchronous to limit contradictory inputs; FSM-to-FSM functions are asynchronous.
4. FSM-to-FSM helper functions run inside the same module and need not be exported publicly.
5. It lets the implementation change without breaking callers.

## Construction / Recognition

## To Write an FSM Public API

1. List the actions callers can take.
2. For each, write a named function wrapping the right `gen_fsm` send call.
3. Make client calls synchronous where it simplifies the protocol; FSM-to-FSM calls asynchronous.
4. Export client functions and `gen_fsm` callbacks; keep FSM-to-FSM helpers internal.

## Context & Application

`trade_fsm`'s public API includes `trade/2`, `accept_trade/1`, `make_offer/2`, `retract_offer/2`, `ready/1`, and `cancel/1`. The book notes client functions are synchronous "because we want our client locked and waiting" and "limiting the number of contradicting messages that can be sent one after the other," whereas `cancel/1` is a global event via `sync_send_all_state_event`.

## Examples

**Example 1** (Ch. 15): `make_offer(OwnPid, Item) -> gen_fsm:send_event(OwnPid, {make_offer, Item}).`

**Example 2** (Ch. 15): `trade(OwnPid, OtherPid) -> gen_fsm:sync_send_event(OwnPid, {negotiate, OtherPid}, 30000).`

**Example 3** (Ch. 15): `cancel(OwnPid) -> gen_fsm:sync_send_all_state_event(OwnPid, cancel).`

## Relationships

## Builds Upon

- **gen_fsm** — The API wraps its send functions.

## Related

- **fsm-event** — The API chooses each call's event kind.

## Common Errors

- **Error**: Letting callers send raw `gen_fsm` messages directly.
  **Correction**: Provide named API functions; this hides the protocol and lets the implementation change.

## Common Confusions

- **Confusion**: Thinking all of an FSM module's functions are public.
  **Clarification**: FSM-to-FSM helper functions run within the module and need not be exported for external callers.

## Source Reference

Chapter 15: "Rage Against the Finite-State Machines," sections "The Public Interface" and "FSM-to-FSM Functions."

## Verification Notes

- Definition: Adapted from "The Public Interface."
- Key Properties: Synthesised from the API code and the sync/async rationale.
- Confidence: HIGH — explicitly shown with code.
