---
# === CORE IDENTIFICATION ===
concept: Querying an Event Handler
slug: gen-event-call

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
pdf_page: 174
section: "Retrieving Data"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "gen_event:call"
  - retrieving data from a handler
  - "handle_call/2"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - event-handler
  - notifying-events
extends: []
related:
  - event-manager
contrasts_with:
  - notifying-events

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is an event handler (gen_event)?"
  - "How do I trace and inspect an OTP process with the sys module?"
---

# Quick Definition

`gen_event:call/3` sends a synchronous request to a *specific* event handler in a manager and returns that handler's reply — used to retrieve data from one handler rather than broadcasting to all.

# Core Definition

To retrieve data from one particular handler, "we need to specify the handler to which we want to send our synchronous message, and we do so using the `gen_event:call(NameScope, Mod, Message)` function" (Cesarini & Vinoski, p. 175). Using `sync_notify/2` would not work, because despite being synchronous it forwards the event to *all* handlers and returns only `ok`. "The event handler synchronously receives the request in the `Mod:handle_call/2` callback and returns a tuple of the format `{ok, Reply, NewData}`, where `Reply` is the return value of the request" (pp. 175-176). The default timeout is 5,000 ms, overridable with an integer or `infinity`. If `Mod` is not a handler in the manager, `{error, bad_module}` is returned; if `handle_call/2` crashes, `{error, {'EXIT', Reason}}`; if it returns any term other than `{ok, Reply, NewData}`, `{error, Term}`. In the latter two error cases the handler is removed from the manager.

# Prerequisites

- **Event handler** — A call targets a specific handler's `handle_call/2` callback.
- **Notifying events** — You must understand notification (broadcast) to see why `call/3` (targeted) is needed.

# Key Properties

1. `gen_event:call(NameScope, Mod, Request [,Timeout])` targets one specific handler.
2. Handled in the handler's `Mod:handle_call/2` callback.
3. `handle_call/2` returns `{ok, Reply, NewData}`; `Reply` becomes the call's return value.
4. Default timeout 5,000 ms; overridable with an integer (ms) or `infinity`.
5. `{error, bad_module}` if `Mod` is not an added handler.
6. `{error, {'EXIT', Reason}}` if `handle_call/2` crashes; `{error, Term}` if it returns an invalid term — in both, the handler is removed.

# Construction / Recognition

## To Query a Handler:
1. Implement `handle_call(Request, Data)` in the handler, returning `{ok, Reply, NewData}`.
2. Export a client function that calls `gen_event:call(Pid, Mod, Request)`.
3. The targeted handler runs `handle_call/2` and its `Reply` is returned to the caller.

# Context & Application

- **Typical contexts**: Reading accumulated state from a specific handler.
- **Common applications**: The `counters` handler exposing `get_counters/1`, which calls `gen_event:call(Pid, counters, get_counters)`.
- **Historical/stylistic notes**: The book introduces `call/3` precisely because `sync_notify/2` cannot return per-handler data (p. 175).

# Examples

**Example 1** (p. 174): The `counters` handler's client function and callback:

```erlang
get_counters(Pid) ->
    gen_event:call(Pid, counters, get_counters).

handle_call(get_counters, TableId) ->
    {ok, {counters, ets:tab2list(TableId)}, TableId}.
```

**Example 2** (pp. 176-177): After notifying three events, `counters:get_counters(P)` returns `{counters,[{{event,{frequency_denied,<0.33.0>}},2}, {{set_alarm,{no_frequency,<0.33.0>}},1}]}`.

# Relationships

## Builds Upon
- **Event handler** — A call is handled by a specific handler's `handle_call/2`.

## Enables
- *(No downstream concepts in this scope.)*

## Related
- **event-manager** — The call is addressed to the manager but routed to one handler.

## Contrasts With
- **notifying-events** — `notify`/`sync_notify` broadcast to *all* handlers and return `ok`; `call/3` targets *one* handler and returns its reply.

# Common Errors

- **Error**: Using `sync_notify/2` to retrieve data from a handler.
  **Correction**: `sync_notify/2` returns only `ok`; use `gen_event:call/3` to address a specific handler and get its reply.

# Common Confusions

- **Confusion**: Thinking a crash in `handle_call/2` leaves the handler in place.
  **Clarification**: If `handle_call/2` crashes or returns an invalid term, the handler is removed from the manager (the other handlers are unaffected).

# Source Reference

Chapter 6: Event Handlers, Section "Retrieving Data," pages 174-177. See Figure 7-6.

# Verification Notes

- Definition source: Direct quotes from pp. 175-176.
- Confidence rationale: HIGH — the source explicitly defines `call/3`, the `handle_call/2` callback, and all error returns.
- Uncertainties: None.
- Cross-reference status: Verified against planned cards in this batch.
- Re-extraction notes: Fresh extraction; no pre-existing card for this source.
