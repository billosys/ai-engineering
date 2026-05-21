---
# === CORE IDENTIFICATION ===
concept: Deleting an Event Handler
slug: deleting-event-handler

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
section: "Deleting an Event Handler"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "gen_event:delete_handler"
  - "removing an event handler"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - gen-event
  - event-manager
  - event-handler
  - adding-event-handler
extends: []
related:
  - gen-event-notify
contrasts_with:
  - adding-event-handler

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do I remove an event handler from a gen_event event manager?"
  - "What happens when an event handler is deleted?"
---

# Quick Definition

`gen_event:delete_handler/3` removes an event handler from an event manager, calling the handler's `terminate/2` callback to allow cleanup before removal.

# Core Definition

According to the gen_event Behaviour chapter: "This function sends a message to the event manager registered as error_man, telling it to delete the event handler terminal_logger. The event manager calls the callback function terminal_logger:terminate([], State), where the argument [] is the third argument to delete_handler. terminate/2 is to be the opposite of init/1 and do any necessary cleaning up. Its return value is ignored."

# Prerequisites

- **gen_event** — delete_handler is a gen_event mechanism.
- **Event Manager** — the event manager hosting the handler.
- **Event Handler** — the callback module being removed.
- **Adding Event Handler** — a handler must be added before it can be deleted.

# Key Properties

1. `gen_event:delete_handler/3` takes the event manager name, handler module name, and a term passed to `terminate/2`.
2. The event manager calls `Module:terminate(Args, State)` before removing the handler.
3. `terminate/2` should clean up resources acquired in `init/1` (close files, etc.).
4. The return value of `terminate/2` is ignored.
5. The handler's `{Module, State}` pair is removed from the event manager's list.
6. Also called on each handler when the event manager itself is stopped.

# Construction / Recognition

## To Construct/Create:
1. Call `gen_event:delete_handler(ManagerName, HandlerModule, Args)`.
2. The handler's `terminate/2` callback is invoked with `Args` and the current state.
3. The handler is removed from the event manager.

## To Identify/Recognize:
1. A call to `gen_event:delete_handler/3`.
2. The handler module's `terminate/2` function being invoked.

# Context & Application

Deleting event handlers enables the dynamic reconfiguration that is central to gen_event's design. The source example shows how a file logger can be removed when file logging is no longer needed, while the terminal logger continues operating. When an event manager is stopped, `terminate/2` is also called on each installed handler, giving all handlers a chance to clean up.

# Examples

**Example 1** (events.md, "Deleting an Event Handler"): Removing the terminal_logger:
```erlang
4> gen_event:delete_handler(error_man, terminal_logger, []).
ok
```

**Example 2** (events.md, "Deleting an Event Handler"): For `terminal_logger`, no cleanup is needed:
```erlang
terminate(_Args, _State) ->
    ok.
```
For `file_logger`, the file descriptor must be closed:
```erlang
terminate(_Args, Fd) ->
    file:close(Fd).
```

# Relationships

## Builds Upon
- **gen_event** — delete_handler is a gen_event mechanism
- **Event Manager** — the event manager from which the handler is removed
- **Event Handler** — the callback module being removed
- **Adding Event Handler** — a handler must be added before it can be deleted

## Enables
- No specific downstream concepts.

## Related
- **gen_event:notify** — after deletion, the handler no longer processes events

## Contrasts With
- **Adding Event Handler** — the inverse operation, installing a handler in the event manager.

# Common Errors

- **Error**: Not implementing proper cleanup in `terminate/2` for handlers that acquired resources.
  **Correction**: The source emphasizes that "terminate/2 is to be the opposite of init/1." For `file_logger`, the file opened in `init/1` must be closed in `terminate/2`.

# Common Confusions

- **Confusion**: Thinking deleting a handler stops a process.
  **Clarification**: No process is stopped. The handler's `{Module, State}` pair is removed from the event manager's internal list, and `terminate/2` is called for cleanup. The event manager process continues running.

# Source Reference

OTP Design Principles, "gen_event Behaviour" chapter, "Deleting an Event Handler" section (events.md).

# Verification Notes

- Definition source: Directly quoted from events.md "Deleting an Event Handler" section.
- Confidence rationale: High — explicitly described with shell examples and callback code.
- Uncertainties: None.
- Cross-reference status: References gen-event, event-manager, event-handler, adding-event-handler, gen-event-notify (planned cards).
