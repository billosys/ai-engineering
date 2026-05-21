---
# === CORE IDENTIFICATION ===
concept: System Messages
slug: system-messages

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
section: "Handling System Messages"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "system message"
  - "{system, From, Request}"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - special-process
  - sys-module
extends: []
related:
  - proc-lib
  - debug-structure
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is a special process?"
  - "How do I implement a special process using proc_lib?"
  - "What must I know before writing a special process?"
---

# Quick Definition

System messages are specially formatted messages (`{system, From, Request}`) used within supervision trees for process management tasks like tracing, suspending, resuming, and code changes.

# Core Definition

System messages are messages with a special meaning, used in the supervision tree. Typical system messages are requests for trace output, and requests to suspend or resume process execution (used during release handling). They are received in the format `{system, From, Request}`. The content and meaning of these messages are not to be interpreted by the process. Instead, `sys:handle_system_msg(Request, From, Parent, Module, Deb, State)` is to be called, which does not return. It handles the system message and eventually calls either `Module:system_continue(Parent, Deb, State)` if process execution is to continue, or `Module:system_terminate(Reason, Parent, Deb, State)` if the process is to terminate. While handling the message, it may also call `Module:system_get_state(State)`, `Module:system_replace_state(StateFun, State)`, or `system_code_change(Misc, Module, OldVsn, Extra)`. A process in a supervision tree is expected to terminate with the same reason as its parent. (Source: spec_proc.md, "Handling System Messages")

# Prerequisites

- **[Special Process](/concept-cards/otp-design-principles/special-process.md)** -- System messages must be handled by special processes.
- **[sys Module](/concept-cards/otp-design-principles/sys-module.md)** -- `sys:handle_system_msg/6` dispatches system messages.

# Key Properties

1. **Format**: `{system, From, Request}` tuple.
2. **Opaque**: The process must not interpret `Request` directly; delegate to `sys:handle_system_msg/6`.
3. **Non-returning handler**: `sys:handle_system_msg/6` does not return; it calls `system_continue` or `system_terminate`.
4. **Required callbacks**: `system_continue/3`, `system_terminate/4`, `system_get_state/1`, `system_replace_state/2`.
5. **Release handling**: Suspend/resume messages are used during release handling for hot code upgrades.
6. **Automatic in behaviours**: Standard behaviours handle system messages automatically.

# Construction / Recognition

## To Construct/Create:
1. Match `{system, From, Request}` in the receive loop.
2. Call `sys:handle_system_msg(Request, From, Parent, Module, Deb, State)`.
3. Implement the required callback functions.

## To Identify/Recognize:
1. Look for `{system, From, Request}` pattern matches in receive clauses.
2. Look for `sys:handle_system_msg/6` calls.
3. Look for exports of `system_continue/3`, `system_terminate/4`, etc.

# Context & Application

System messages are the mechanism by which OTP infrastructure communicates with running processes for management and debugging. They enable features like hot code upgrade (suspend/resume), remote debugging, and state inspection. Every OTP-compliant process must handle them, either automatically (via behaviours) or explicitly (in special processes).

# Examples

**Example 1** (spec_proc.md, "Handling System Messages"): Handling system messages in a special process loop:

```erlang
loop(Chs, Parent, Deb) ->
    receive
        ...
        {system, From, Request} ->
            sys:handle_system_msg(Request, From, Parent,
                                  ch4, Deb, Chs)
    end.

system_continue(Parent, Deb, Chs) ->
    loop(Chs, Parent, Deb).

system_terminate(Reason, _Parent, _Deb, _Chs) ->
    exit(Reason).

system_get_state(Chs) ->
    {ok, Chs}.

system_replace_state(StateFun, Chs) ->
    NChs = StateFun(Chs),
    {ok, NChs, NChs}.
```

# Relationships

## Builds Upon
- **[sys Module](/concept-cards/otp-design-principles/sys-module.md)** -- Provides `handle_system_msg/6` for dispatching.
- **[Special Process](/concept-cards/otp-design-principles/special-process.md)** -- System message handling is a core requirement.

## Enables
- Hot code upgrades via suspend/resume.
- Remote debugging and state inspection.
- Release handling integration.

## Related
- **[Debug Structure](/concept-cards/otp-design-principles/debug-structure.md)** -- Passed through system message handling.
- **[proc_lib](/concept-cards/otp-design-principles/proc-lib.md)** -- Provides the process startup that enables system message handling.

## Contrasts With
- None directly.

# Common Errors

- **Error**: Trying to interpret or respond to system messages directly instead of delegating to `sys:handle_system_msg/6`.
  **Correction**: The content of system messages is not to be interpreted by the process. Always delegate to `sys:handle_system_msg/6`.

- **Error**: Expecting `sys:handle_system_msg/6` to return.
  **Correction**: It does not return. It eventually calls `system_continue` or `system_terminate`. The process loop must resume from `system_continue`.

# Common Confusions

- **Confusion**: `system_terminate` should do cleanup specific to system messages.
  **Clarification**: `system_terminate` simply exits the process with the given reason: `exit(Reason)`. A process in a supervision tree is expected to terminate with the same reason as its parent.

# Source Reference

spec_proc.md, "Handling System Messages" section.

# Verification Notes

- Definition source: Directly from spec_proc.md, "Handling System Messages" section.
- Confidence rationale: High -- explicitly described with complete callback signatures and example.
- Uncertainties: None.
- Cross-reference status: References sys-module, special-process, debug-structure, proc-lib.
