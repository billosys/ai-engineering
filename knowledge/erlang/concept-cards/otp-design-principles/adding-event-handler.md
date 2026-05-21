---
# === CORE IDENTIFICATION ===
concept: Adding an Event Handler
slug: adding-event-handler

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
section: "Adding an Event Handler"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "gen_event:add_handler"
  - "installing an event handler"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - gen-event
  - event-manager
  - event-handler
extends: []
related:
  - gen-event-notify
contrasts_with:
  - deleting-event-handler

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do I add an event handler to a gen_event event manager?"
  - "What happens when an event handler is added?"
---

# Quick Definition

`gen_event:add_handler/3` installs an event handler callback module in an event manager, calling the handler's `init/1` callback to initialize its state.

# Core Definition

According to the gen_event Behaviour chapter: "This function sends a message to the event manager registered as error_man, telling it to add the event handler terminal_logger. The event manager calls the callback function terminal_logger:init([]), where the argument [] is the third argument to add_handler. init/1 is expected to return {ok, State}, where State is the internal state of the event handler."

# Prerequisites

- **gen_event** — add_handler is a gen_event mechanism.
- **Event Manager** — handlers are added to a running event manager.
- **Event Handler** — the callback module being installed.

# Key Properties

1. `gen_event:add_handler/3` takes the event manager name, handler module name, and init arguments.
2. The event manager calls `Module:init(Args)` to initialize the handler.
3. `init/1` must return `{ok, State}`.
4. The handler's `{Module, State}` pair is added to the event manager's handler list.
5. Handlers can be added at any time during the event manager's lifetime.
6. Multiple handlers (even of the same module) can be installed in one event manager.

# Construction / Recognition

## To Construct/Create:
1. Ensure the event manager is running.
2. Call `gen_event:add_handler(ManagerName, HandlerModule, InitArgs)`.
3. The handler's `init/1` callback initializes with `InitArgs`.

## To Identify/Recognize:
1. A call to `gen_event:add_handler/3`.
2. The handler module's `init/1` function being invoked by the event manager.

# Context & Application

Adding event handlers at runtime is what makes gen_event dynamically extensible. The source's example shows a scenario where error logging to the terminal is always active, but file logging can be added temporarily. This runtime extensibility is a key advantage of gen_event over static designs.

# Examples

**Example 1** (events.md, "Adding an Event Handler"): Adding the terminal_logger handler to the error manager:
```erlang
1> gen_event:start({local, error_man}).
{ok,<0.31.0>}
2> gen_event:add_handler(error_man, terminal_logger, []).
ok
```

**Example 2** (events.md, "Adding an Event Handler"): The `terminal_logger:init/1` callback initializes with empty state:
```erlang
init(_Args) ->
    {ok, []}.
```
For `file_logger`, init opens a file and stores the file descriptor as state:
```erlang
init(File) ->
    {ok, Fd} = file:open(File, read),
    {ok, Fd}.
```

# Relationships

## Builds Upon
- **gen_event** — add_handler is a gen_event mechanism
- **Event Manager** — the target for handler installation
- **Event Handler** — the callback module being installed

## Enables
- **gen_event:notify** — once added, the handler will process events

## Related
- No additional related concepts.

## Contrasts With
- **Deleting Event Handler** — the inverse operation, removing a handler from the event manager.

# Common Errors

- **Error**: Passing the wrong init arguments that cause `init/1` to crash.
  **Correction**: Ensure the init arguments match what the handler's `init/1` expects. For `terminal_logger`, pass `[]`; for `file_logger`, pass a filename.

# Common Confusions

- **Confusion**: Thinking `add_handler` starts a new process for the handler.
  **Clarification**: The handler runs within the existing event manager process. `add_handler` simply adds a new `{Module, State}` entry to the event manager's internal list.

# Source Reference

OTP Design Principles, "gen_event Behaviour" chapter, "Adding an Event Handler" section (events.md).

# Verification Notes

- Definition source: Directly quoted from events.md "Adding an Event Handler" section.
- Confidence rationale: High — explicitly described with shell examples and callback code.
- Uncertainties: None.
- Cross-reference status: References gen-event, event-manager, event-handler, deleting-event-handler, gen-event-notify (planned cards).
