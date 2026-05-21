---
# === CORE IDENTIFICATION ===
concept: "gen_event:notify (Event Notification)"
slug: gen-event-notify

# === CLASSIFICATION ===
category: otp-behaviours
subcategory: gen-event
tier: intermediate

# === PROVENANCE ===
source: "OTP Design Principles"
source_slug: otp-design-principles
authors: "Ericsson AB"
chapter: "gen_event Behaviour"
chapter_number: null
pdf_page: null
section: "Notifying about Events"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "gen_event notify"
  - "event notification"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - gen-event
  - event-manager
  - event-handler
extends: []
related:
  - adding-event-handler
contrasts_with:
  - gen-server-call
  - gen-server-cast

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do I send an event to a gen_event event manager?"
  - "What happens when gen_event:notify is called?"
---

# Quick Definition

`gen_event:notify/2` sends an event to an event manager, which dispatches it to all installed event handlers by calling `handle_event/2` on each one in order.

# Core Definition

According to the gen_event Behaviour chapter: "The event is made into a message and sent to the event manager. When the event is received, the event manager calls handle_event(Event, State) for each installed event handler, in the same order as they were added. The function is expected to return a tuple {ok,State1}, where State1 is a new value for the state of the event handler."

# Prerequisites

- **gen_event** — notify is a gen_event mechanism.
- **Event Manager** — the target of the notification.
- **Event Handler** — handlers process the notified event.

# Key Properties

1. `gen_event:notify/2` takes the event manager name/pid and the event term.
2. The event is dispatched to all installed event handlers in installation order.
3. Each handler's `handle_event(Event, State)` is called.
4. `handle_event/2` returns `{ok, State1}` with updated handler state.
5. The notification is asynchronous — `notify/2` returns `ok` immediately.
6. Each handler independently processes the event and updates its own state.

# Construction / Recognition

## To Construct/Create:
1. Call `gen_event:notify(ManagerName, Event)` where Event is any term.
2. Ensure event handlers are installed that implement `handle_event/2`.

## To Identify/Recognize:
1. A call to `gen_event:notify/2`.
2. Event handlers implementing `handle_event(Event, State)`.

# Context & Application

Event notification is the core operation in gen_event's publish-subscribe model. Producers send events without knowing which handlers are installed, and handlers process events without knowing about other handlers. This decoupling allows dynamic reconfiguration: handlers can be added or removed at any time without affecting event producers.

# Examples

**Example 1** (events.md, "Notifying about Events"): Sending an event to the error manager:
```erlang
3> gen_event:notify(error_man, no_reply).
***Error*** no_reply
ok
```
"error_man is the name of the event manager and no_reply is the event."

**Example 2** (events.md, "Notifying about Events"): The terminal_logger handler processes the event:
```erlang
handle_event(ErrorMsg, State) ->
    io:format("***Error*** ~p~n", [ErrorMsg]),
    {ok, State}.
```
The file_logger handler also processes the same event if installed:
```erlang
handle_event(ErrorMsg, Fd) ->
    io:format(Fd, "***Error*** ~p~n", [ErrorMsg]),
    {ok, Fd}.
```

# Relationships

## Builds Upon
- **gen_event** — notify is a gen_event mechanism
- **Event Manager** — notify sends events to the event manager
- **Event Handler** — handlers process the notified events

## Enables
- No specific downstream concepts.

## Related
- **Adding Event Handler** — handlers must be added before they can receive notifications

## Contrasts With
- **gen_server:call** — call is synchronous and targets one server; notify is asynchronous and dispatches to all handlers
- **gen_server:cast** — cast targets one server process; notify dispatches to all installed handlers in one event manager

# Common Errors

- **Error**: Sending events before any handlers are installed.
  **Correction**: Install at least one event handler with `gen_event:add_handler/3` before sending events, or accept that events will be silently dropped.

# Common Confusions

- **Confusion**: Thinking `gen_event:notify/2` blocks until all handlers have processed the event.
  **Clarification**: `notify/2` is asynchronous and returns `ok` immediately. Use `gen_event:sync_notify/2` if synchronous processing is needed.

# Source Reference

OTP Design Principles, "gen_event Behaviour" chapter, "Notifying about Events" section (events.md).

# Verification Notes

- Definition source: Directly quoted from events.md "Notifying about Events" section.
- Confidence rationale: High — explicitly described with shell example and callback code.
- Uncertainties: None.
- Cross-reference status: References gen-event, event-manager, event-handler, adding-event-handler, gen-server-call, gen-server-cast (planned cards).
