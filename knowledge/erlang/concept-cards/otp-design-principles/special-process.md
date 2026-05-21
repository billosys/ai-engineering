---
# === CORE IDENTIFICATION ===
concept: Special Process
slug: special-process

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
section: "Special Processes"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "special processes"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - behaviour
  - supervision-tree
  - proc-lib
  - sys-module
extends: []
related:
  - system-messages
  - debug-structure
  - user-defined-behaviour
contrasts_with:
  - gen-server
  - gen-statem
  - gen-event

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is a special process?"
  - "How do I implement a special process using proc_lib?"
  - "What must I know before writing a special process?"
---

# Quick Definition

A special process is a process that complies with OTP design principles (fits in a supervision tree, handles system messages, supports sys debugging) without using a standard behaviour like gen_server or gen_statem.

# Core Definition

A special process is a process that complies with the OTP design principles without using a standard behaviour. Such a process must: (1) be started in a way that makes it fit into a supervision tree (using `proc_lib`), (2) support the `sys` debug facilities, and (3) take care of system messages. System messages are messages with special meaning used in the supervision tree, including requests for trace output and requests to suspend or resume process execution during release handling. Processes implemented using standard behaviours automatically understand these messages; special processes must handle them explicitly. (Source: spec_proc.md, "Special Processes")

# Prerequisites

- **[Behaviour](/concept-cards/otp-design-principles/behaviour.md)** -- Understanding what standard behaviours provide helps explain what a special process must implement manually.
- **[Supervision Tree](/concept-cards/otp-design-principles/supervision-tree.md)** -- Special processes must fit into supervision trees.
- **[proc_lib](/concept-cards/otp-design-principles/proc-lib.md)** -- Used to start the process.
- **[sys Module](/concept-cards/otp-design-principles/sys-module.md)** -- Used for debugging support.

# Key Properties

1. **No standard behaviour**: Does not use `gen_server`, `gen_statem`, `gen_event`, or `supervisor`.
2. **OTP-compliant**: Fits into supervision trees despite not using a standard behaviour.
3. **Three requirements**: Must use `proc_lib` for starting, support `sys` debugging, and handle system messages.
4. **Manual message loop**: Implements its own receive loop rather than using behaviour callbacks.
5. **Explicit system message handling**: Must match `{system, From, Request}` messages and delegate to `sys:handle_system_msg/6`.
6. **Must implement callbacks**: `system_continue/3`, `system_terminate/4`, `system_get_state/1`, `system_replace_state/2`.
7. **Trap exits awareness**: If configured to trap exits, must handle `{'EXIT', Parent, Reason}` and terminate with the same reason.

# Construction / Recognition

## To Construct/Create:
1. Start the process using `proc_lib:start_link/3,4,5` or `proc_lib:spawn_link/3,4`.
2. In the init function, call `proc_lib:init_ack(Parent, {ok, self()})` to acknowledge startup.
3. Initialize the debug structure with `sys:debug_options([])`.
4. In the main loop, match `{system, From, Request}` and call `sys:handle_system_msg/6`.
5. Use `sys:handle_debug/4` for each system event (incoming/outgoing messages).
6. Implement `system_continue/3`, `system_terminate/4`, `system_get_state/1`, `system_replace_state/2`.

## To Identify/Recognize:
1. A process that uses `proc_lib` for starting but does not declare `-behaviour(gen_server)` or similar.
2. The module exports `system_continue/3`, `system_terminate/4`, etc.
3. The receive loop matches `{system, From, Request}`.

# Context & Application

Special processes are used when the standard behaviours do not fit the process's communication pattern. They are relatively rare in production code, as `gen_server` and `gen_statem` cover most use cases. Special processes are also the foundation for implementing user-defined behaviours. If a special process traps exits, it must handle `{'EXIT', Parent, Reason}` messages from its parent and terminate with the same reason.

# Examples

**Example 1** (spec_proc.md, "Special Processes / Example"): A complete special process implementation:

```erlang
-module(ch4).
-export([start_link/0]).
-export([alloc/0, free/1]).
-export([init/1]).
-export([system_continue/3, system_terminate/4,
         write_debug/3,
         system_get_state/1, system_replace_state/2]).

start_link() ->
    proc_lib:start_link(ch4, init, [self()]).

init(Parent) ->
    register(ch4, self()),
    Chs = channels(),
    Deb = sys:debug_options([]),
    proc_lib:init_ack(Parent, {ok, self()}),
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
        {free, Ch} ->
            Deb2 = sys:handle_debug(Deb, fun ch4:write_debug/3,
                                    ch4, {in, {free, Ch}}),
            Chs2 = free(Ch, Chs),
            loop(Chs2, Parent, Deb2);
        {system, From, Request} ->
            sys:handle_system_msg(Request, From, Parent,
                                  ch4, Deb, Chs)
    end.
```

**Example 2** (spec_proc.md, "Special Processes"): Trap exit handling:

```erlang
init(Parent) ->
    ...,
    process_flag(trap_exit, true),
    ...,
    loop(Parent).

loop(Parent) ->
    receive
        ...
        {'EXIT', Parent, Reason} ->
            %% Clean up here, if needed.
            exit(Reason);
        ...
    end.
```

# Relationships

## Builds Upon
- **[proc_lib](/concept-cards/otp-design-principles/proc-lib.md)** -- Used for process startup.
- **[sys Module](/concept-cards/otp-design-principles/sys-module.md)** -- Used for debug facilities.

## Enables
- **[User-Defined Behaviour](/concept-cards/otp-design-principles/user-defined-behaviour.md)** -- User-defined behaviours are built on top of special process techniques.

## Related
- **[System Messages](/concept-cards/otp-design-principles/system-messages.md)** -- Must be handled by special processes.
- **[Debug Structure](/concept-cards/otp-design-principles/debug-structure.md)** -- Must be maintained for sys debugging support.

## Contrasts With
- **[gen_server](/concept-cards/otp-design-principles/gen-server.md)** -- Handles system messages and debugging automatically.
- **[gen_statem](/concept-cards/otp-design-principles/gen-statem.md)** -- Handles system messages and debugging automatically.

# Common Errors

- **Error**: Forgetting to call `proc_lib:init_ack/2` in the init function, causing the caller to hang.
  **Correction**: `proc_lib:start_link/3` is synchronous and waits for `proc_lib:init_ack/1,2` or `proc_lib:init_fail/2,3` before returning.

- **Error**: Not matching `{system, From, Request}` in the receive loop.
  **Correction**: System messages must be handled for OTP compliance. Match the tuple and delegate to `sys:handle_system_msg/6`.

# Common Confusions

- **Confusion**: Special processes are not OTP-compliant because they do not use behaviours.
  **Clarification**: Special processes are fully OTP-compliant. They manually implement the same responsibilities that standard behaviours handle automatically.

- **Confusion**: `sys:handle_system_msg/6` returns normally.
  **Clarification**: It does not return. It eventually calls either `Module:system_continue/3` (to resume) or `Module:system_terminate/4` (to terminate).

# Source Reference

spec_proc.md, "Special Processes" section including subsections on starting, debugging, and handling system messages.

# Verification Notes

- Definition source: Directly from spec_proc.md, "Special Processes" section.
- Confidence rationale: High -- explicitly defined with complete code example.
- Uncertainties: None.
- Cross-reference status: References proc-lib, sys-module, system-messages, debug-structure, user-defined-behaviour, gen-server, gen-statem.
