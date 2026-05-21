---
# === CORE IDENTIFICATION ===
concept: Debug Structure
slug: debug-structure

# === CLASSIFICATION ===
category: processes-concurrency
subcategory: otp-compliance
tier: advanced

# === PROVENANCE ===
source: "OTP Design Principles"
source_slug: otp-design-principles
authors: "Ericsson AB"
chapter: "sys and proc_lib"
chapter_number: null
pdf_page: null
section: "Debugging"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "Deb"
  - "debug options"
  - "debug state"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - sys-module
  - special-process
extends: []
related:
  - system-messages
  - proc-lib
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What must I know before writing a special process?"
  - "How do I implement a special process using proc_lib?"
---

# Quick Definition

The debug structure is an opaque term initialized by `sys:debug_options/1` and threaded through a special process's loop, enabling runtime tracing and statistics collection via `sys:handle_debug/4`.

# Core Definition

To support the debug facilities in `sys`, a debug structure is needed. The `Deb` term is initialized using `sys:debug_options/1`, which takes a list of options (an empty list means debugging is initially disabled). For each system event to be logged or traced, `sys:handle_debug(Deb, Func, Info, Event)` is called, which returns an updated debug structure `Deb1`. The `Func` argument is a user-defined format function called as `Func(Dev, Event, Info)` where `Dev` is the I/O device, `Event` is the system event, and `Info` is additional context. Typically, at least incoming and outgoing messages are considered system events, represented by tuples `{in, Msg[, From]}` and `{out, Msg, To[, State]}`. (Source: spec_proc.md, "Debugging")

# Prerequisites

- **[sys Module](/concept-cards/otp-design-principles/sys-module.md)** -- The debug structure is managed by sys functions.
- **[Special Process](/concept-cards/otp-design-principles/special-process.md)** -- Debug structures are explicitly maintained by special processes.

# Key Properties

1. **Opaque term**: Initialized by `sys:debug_options/1`, not meant to be inspected directly.
2. **Threaded through loop**: Must be passed through all iterations of the process loop and updated by `sys:handle_debug/4`.
3. **Initially disabled**: An empty options list `[]` means debugging is off by default.
4. **Custom format function**: The user defines a `Func(Dev, Event, Info)` for formatting trace output.
5. **System event conventions**: Incoming messages as `{in, Msg, From}`, outgoing as `{out, Msg, To}`.
6. **Updated on each event**: `sys:handle_debug/4` returns an updated `Deb1` that must be used for the next call.

# Construction / Recognition

## To Construct/Create:
1. Initialize in the process init function:

```erlang
init(Parent) ->
    ...
    Deb = sys:debug_options([]),
    ...
    loop(Chs, Parent, Deb).
```

2. Call `sys:handle_debug/4` for each system event in the loop:

```erlang
Deb2 = sys:handle_debug(Deb, fun Mod:write_debug/3, Name, {in, Msg, From})
```

## To Identify/Recognize:
1. Look for a variable (typically `Deb`) initialized by `sys:debug_options/1`.
2. Look for `sys:handle_debug/4` calls that update and thread this variable.

# Context & Application

The debug structure is the mechanism by which the `sys` module tracks whether tracing, statistics, and other debugging features are enabled for a specific process. In standard behaviours this is handled internally, but special processes must manage it explicitly. The format function allows custom event representations in trace output.

# Examples

**Example 1** (spec_proc.md, "Debugging"): Initialization and use in a loop:

```erlang
init(Parent) ->
    ...
    Deb = sys:debug_options([]),
    ...
    loop(Chs, Parent, Deb).

loop(Chs, Parent, Deb) ->
    receive
        {From, alloc} ->
            Deb2 = sys:handle_debug(Deb, fun ch4:write_debug/3,
                                    ch4, {in, alloc, From}),
            {Ch, Chs2} = alloc(Chs),
            From ! {ch4, Ch},
            Deb3 = sys:handle_debug(Deb2, fun ch4:write_debug/3,
                                    ch4, {out, {ch4, Ch}, From}),
            loop(Chs2, Parent, Deb3);
        ...
    end.

write_debug(Dev, Event, Name) ->
    io:format(Dev, "~p event = ~p~n", [Name, Event]).
```

# Relationships

## Builds Upon
- **[sys Module](/concept-cards/otp-design-principles/sys-module.md)** -- Debug structures are created and updated by sys functions.

## Enables
- Runtime tracing and statistics for special processes.
- Integration with `sys:trace/2` and `sys:statistics/2`.

## Related
- **[Special Process](/concept-cards/otp-design-principles/special-process.md)** -- Special processes maintain debug structures explicitly.
- **[System Messages](/concept-cards/otp-design-principles/system-messages.md)** -- The debug structure is passed to `sys:handle_system_msg/6`.

## Contrasts With
- None directly.

# Common Errors

- **Error**: Not threading the updated debug structure through the loop, losing debug state changes.
  **Correction**: Each call to `sys:handle_debug/4` returns an updated `Deb`. Always use the returned value for the next call and pass it to the next loop iteration.

- **Error**: Forgetting to pass the debug structure to `sys:handle_system_msg/6`.
  **Correction**: The debug structure must be passed as the `Deb` argument to `sys:handle_system_msg/6` so that system messages can update debug settings.

# Common Confusions

- **Confusion**: The debug structure must be initialized with tracing enabled.
  **Clarification**: An empty list `[]` passed to `sys:debug_options/1` means debugging is initially disabled. Tracing can be enabled at runtime using `sys:trace/2`.

# Source Reference

spec_proc.md, "Debugging" section.

# Verification Notes

- Definition source: Directly from spec_proc.md, "Debugging" section.
- Confidence rationale: High -- explicitly described with initialization and usage patterns.
- Uncertainties: None.
- Cross-reference status: References sys-module, special-process, system-messages.
