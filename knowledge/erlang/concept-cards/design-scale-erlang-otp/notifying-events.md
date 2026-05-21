---
# === CORE IDENTIFICATION ===
concept: Notifying Events
slug: notifying-events

# === CLASSIFICATION ===
category: otp-behaviours
subcategory: event-handling
tier: intermediate

# === PROVENANCE ===
source: Designing for Scalability with Erlang/OTP
source_slug: design-scale-erlang-otp
authors: Francesco Cesarini & Steve Vinoski
chapter: "Event Handlers"
chapter_number: 6
pdf_page: 172
section: "Sending Synchronous and Asynchronous Events"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "gen_event:notify"
  - "gen_event:sync_notify"
  - sending events
  - event notification

# === TYPED RELATIONSHIPS ===
prerequisites:
  - event-manager
  - event-handler
extends: []
related:
  - gen-event-call
  - event
contrasts_with:
  - gen-event-call

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is an event handler (gen_event)?"
  - "How do I handle synchronous versus asynchronous messages in a gen_server?"
  - "What is the difference between synchronous and asynchronous message passing?"
---

# Quick Definition

Notifying an event sends it to an event manager, which then invokes every added handler's `handle_event/2` callback; `notify/2` is asynchronous (returns `ok` at once) while `sync_notify/2` returns `ok` only after all handlers have run.

# Core Definition

"Events can be sent to the manager and forwarded to the handlers synchronously or asynchronously depending on the need to control the rate at which producers generate events" (Cesarini & Vinoski, p. 172). "The `gen_event:notify/2` function sends an asynchronous event to all handlers and immediately returns `ok`. The callback function `Mod:handle_event/2` is called for every handler that has been added to the manager, one at a time. `gen_event:sync_notify/2` also invokes the `Mod:handle_event/2` callback function for all handlers. The difference from its asynchronous variant is that `ok` is returned only when all callbacks have been executed" (p. 172). Non-OTP-compliant messages (exit signals, monitors, node monitoring, `Pid ! Msg`) are handled by each handler's `handle_info/2` callback instead. A handler's `handle_event/2`/`handle_info/2` returns `{ok, NewData}`, `{ok, NewData, hibernate}`, `remove_handler`, or a `swap_handler` tuple.

# Prerequisites

- **Event manager** — Events are notified *to* a manager.
- **Event handler** — Notified events are dispatched to handlers' `handle_event/2` callbacks.

# Key Properties

1. `gen_event:notify(NameScope, Event)` — asynchronous; returns `ok` immediately.
2. `gen_event:sync_notify(Name, Event)` — synchronous; returns `ok` only after all handlers have executed.
3. Both invoke `Mod:handle_event/2` for *every* handler, one at a time.
4. `handle_event/2` returns `{ok, NewData}`, `{ok, NewData, hibernate}`, `remove_handler`, or `{swap_handler, ...}`.
5. Returning `remove_handler` triggers `Mod:terminate(remove_handler, Data)` and deletes the handler.
6. Non-OTP messages are routed to each handler's `handle_info/2`.

# Construction / Recognition

## To Notify an Event:
1. Choose `notify/2` (fire-and-forget) or `sync_notify/2` (wait for all handlers).
2. Call it with the manager name/pid and the event term.
3. Each handler's `handle_event/2` runs in turn; ensure it returns `{ok, NewData}`.

# Context & Application

- **Typical contexts**: Pushing system events into a monitoring manager.
- **Common applications**: Sending `set_alarm`/`clear_alarm` events; routing junk messages through `handle_info/2`.
- **Historical/stylistic notes**: Use `sync_notify/2` when producers must be throttled to the handlers' processing rate, to avoid an unbounded message queue (p. 172).

# Examples

**Example 1** (p. 169): The `logger` handler's `handle_event/2`:

```erlang
handle_event(Event, {Fd, Count}) ->
    print(Fd, Count, Event, "Event"),
    {ok, {Fd, Count+1}}.
```

**Example 2** (p. 171, shell commands 3-4): `gen_event:notify(P, {set_alarm, {no_frequency, self()}})` and `gen_event:sync_notify(P, {clear_alarm, no_frequency})` both return `ok`, but command 4 only returns after all handlers ran.

# Relationships

## Builds Upon
- **Event manager** — Notifications are delivered to a manager.
- **Event handler** — Notified events run each handler's `handle_event/2`.

## Enables
- *(No downstream concepts in this scope.)*

## Related
- **event** — A notification carries an event.
- **gen-event-call** — A synchronous query to a *specific* handler, contrasted with notifications to *all* handlers.

## Contrasts With
- **gen-event-call** — `notify`/`sync_notify` reach *every* handler and return `ok`; `gen_event:call/3` targets *one* handler and returns its reply.

# Common Errors

- **Error**: Using `notify/2` for high-rate producers with slow handlers, growing the manager's message queue.
  **Correction**: Use `sync_notify/2` to throttle producers to the handlers' processing rate.

# Common Confusions

- **Confusion**: Thinking `sync_notify/2` returns a handler's result.
  **Clarification**: `sync_notify/2` still returns only `ok`; it merely waits until all handlers finish. To get a result from a specific handler, use `gen_event:call/3`.

# Source Reference

Chapter 6: Event Handlers, Section "Sending Synchronous and Asynchronous Events," pages 172-174. See Figure 7-5.

# Verification Notes

- Definition source: Direct quotes from p. 172.
- Confidence rationale: HIGH — the source explicitly defines both notify functions and the `handle_event/2` callback.
- Uncertainties: None.
- Cross-reference status: Verified against planned cards in this batch.
- Re-extraction notes: Fresh extraction; no pre-existing card for this source.
