---
# === CORE IDENTIFICATION ===
concept: Special Process System Messages
slug: special-process-system-messages

# === CLASSIFICATION ===
category: otp-behaviours
subcategory: special-processes
tier: advanced

# === PROVENANCE ===
source: "Designing for Scalability with Erlang/OTP"
source_slug: design-scale-erlang-otp
authors: "Francesco Cesarini & Steve Vinoski"
chapter: "Special Processes and Your Own Behaviors"
chapter_number: 9
pdf_page: 260
section: "System Messages"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "system messages"
  - "sys:handle_system_msg"
  - "system_continue and system_terminate"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - special-process
  - proc-lib
extends: []
related:
  - sys-trace-events
  - special-process
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is a special process?"
  - "How does the sys module relate to OTP behaviors?"
  - "How do I trace and inspect an OTP process with the sys module?"
---

# Quick Definition

System messages are opaque `{system, From, Msg}` messages a special process must accept and pass to `sys:handle_system_msg/6`, which handles them behind the scenes and returns control via the `system_continue/3` or `system_terminate/4` callbacks.

# Core Definition

In addition to monitoring parents, special processes need to manage system messages of the format `{system, From, Msg}`, where `From` is the request originator and `Msg` is the system message itself (Cesarini & Vinoski, p. 247). They may originate from a supervisor suspending/resuming the process during software upgrades, or from a client manipulating trace output via the `sys` module — but to the developer they are opaque data, simply passed on. They are handled by `sys:handle_system_message(Msg, From, Parent, Mod, Dbg, Data)`; the call never returns directly — control is handed back through `Mod:system_continue(Parent, Debug, Data)` or `Mod:system_terminate(Reason, Parent, Debug, Data)`. The function invoking `handle_system_msg/6` must be tail recursive, or a memory leak occurs for every system message received (pp. 247-248).

# Prerequisites

- **Special process** — System-message handling is a defining requirement of a special process.
- **proc_lib** — The `Parent` argument needed by `handle_system_msg/6` is captured when the process is started with `proc_lib`.

# Key Properties

1. System messages have the form `{system, From, Msg}` and are opaque to the developer.
2. They are passed to `sys:handle_system_msg(Msg, From, Parent, Mod, Dbg, Data)`.
3. The call never returns; it hands control back via `system_continue/3` or `system_terminate/4`.
4. The function calling `handle_system_msg/6` must be tail recursive — otherwise a memory leak occurs per message.
5. `system_continue/3` returns the process to its loop; `system_terminate/4` triggers cleanup and termination.
6. A special process running dynamic modules must also handle `{get_modules, From}`, replying `From ! {modules, ModuleList}`.

# Construction / Recognition

## To Construct/Create:
1. In the main loop, match `{system, From, Msg}`.
2. Tail-recursively call `sys:handle_system_msg(Msg, From, Parent, ?MODULE, Debug, LoopData)`.
3. Export `system_continue/3` to resume the loop and `system_terminate/4` to clean up and exit.

## To Identify/Recognize:
1. A `{system, From, Msg}` clause in the process loop.
2. Exported `system_continue/3` and `system_terminate/4` callbacks.

# Context & Application

- **Typical contexts**: Every special process and every OTP behavior.
- **Common applications**: Letting supervisors suspend/resume processes during upgrades; serving `sys`-module trace and status requests.
- **Historical/stylistic notes**: The book stresses reusing this code verbatim from the mutex example, ensuring tail recursion when control is handed back (p. 250).

# Examples

**Example 1** (pp. 248-249): The mutex `free`/`busy` states match `{system,From,Msg}` and call `sys:handle_system_msg(Msg, From, Parent, ?MODULE, Debug, {free, Name})` / `{busy,Name,Pid}`.

**Example 2** (p. 249): `system_continue/3` and `system_terminate/4` in the mutex pattern-match the loop data to resume or terminate the correct state.

## Worked Example

Handling a system message in the mutex (pp. 248-249):

```erlang
free(Name, Parent, Debug) ->
    receive
        {system,From,Msg} ->                       %% opaque system message
            sys:handle_system_msg(Msg, From, Parent,
                                   ?MODULE, Debug, {free, Name});
        ...
    end.

system_continue(Parent, Debug, {free,Name}) ->
    free(Name, Parent, Debug).
system_terminate(Reason, _Parent, Debug, {free,Name}) ->
    terminate(Reason, Name, Debug).
```

# Relationships

## Builds Upon
- *(none)*

## Enables
- *(none)*

## Related
- **Sys trace events** — Trace requests arrive as system messages and are handled the same way.
- **Special process** — System-message handling is one of the defining capabilities of a special process.

## Contrasts With
- *(none)*

# Common Errors

- **Error**: Calling `sys:handle_system_msg/6` from a non-tail-recursive position.
  **Correction**: The call must be in tail position; otherwise a memory leak occurs for every system message received.

- **Error**: Forgetting to export `system_continue/3` and `system_terminate/4`.
  **Correction**: `sys:handle_system_msg/6` hands control back through these callbacks; they must be defined and exported.

# Common Confusions

- **Confusion**: Thinking the developer must interpret the contents of `Msg`.
  **Clarification**: `Msg` is opaque — you pass it to `sys:handle_system_msg/6` and only react to the `system_continue`/`system_terminate` callbacks.

# Source Reference

Chapter 9: Special Processes and Your Own Behaviors, "System Messages" and "Putting It Together," pages 247-250; "Summing Up," Table 10-2, p. 261.

# Verification Notes

- Definition source: Direct adaptation from pp. 247-248.
- Confidence rationale: HIGH — explicitly defined with the message format, the handler call, and worked mutex code.
- Uncertainties: None.
- Cross-reference status: Verified against planned card slugs for this source.
- Re-extraction notes: Fresh extraction — no pre-existing card for this source. Slug deliberately prefixed `special-process-` to avoid collision with the chapter-4 `system-message` card from another source area.
</content>
