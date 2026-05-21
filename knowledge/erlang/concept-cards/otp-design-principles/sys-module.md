---
# === CORE IDENTIFICATION ===
concept: sys Module
slug: sys-module

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
section: "Simple Debugging"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "sys"
  - "sys debugging"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - behaviour
extends: []
related:
  - special-process
  - proc-lib
  - debug-structure
  - system-messages
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is a special process?"
  - "What must I know before writing a special process?"
---

# Quick Definition

The `sys` module provides functions for simple debugging of OTP processes (tracing, statistics, status inspection) and is used by special processes to handle system messages and maintain debug state.

# Core Definition

The `sys` module has functions for simple debugging of processes implemented using behaviours. It also has functions that, together with functions in the `proc_lib` module, can be used to implement a special process that complies to the OTP design principles without using a standard behaviour. Key debugging functions include: `sys:statistics/2` for enabling/retrieving process statistics, `sys:trace/2` for enabling trace output, and `sys:get_status/1` for retrieving process status. For special processes, `sys:debug_options/1` initializes a debug structure, `sys:handle_debug/4` logs system events, and `sys:handle_system_msg/6` handles system messages. Both `sys` and `proc_lib` belong to the STDLIB application. (Source: spec_proc.md, "Simple Debugging" and "sys and proc_lib")

# Prerequisites

- **[Behaviour](/concept-cards/otp-design-principles/behaviour.md)** -- sys debugging works with processes that use behaviours or implement special process requirements.

# Key Properties

1. **Debugging functions**: `sys:statistics/2`, `sys:trace/2`, `sys:get_status/1`.
2. **Debug structure management**: `sys:debug_options/1` initializes, `sys:handle_debug/4` logs events.
3. **System message handling**: `sys:handle_system_msg/6` dispatches system messages for special processes.
4. **Part of STDLIB**: Belongs to the STDLIB application.
5. **Works with all behaviours**: Standard behaviours support sys debugging automatically.
6. **Extensible**: Custom format functions can be provided to `sys:handle_debug/4`.

# Construction / Recognition

## To Construct/Create:
1. For standard behaviours, use sys functions directly on the process:

```erlang
sys:statistics(ProcessName, true).
sys:trace(ProcessName, true).
sys:get_status(ProcessName).
```

2. For special processes, initialize and maintain the debug structure in the process loop.

## To Identify/Recognize:
1. Look for calls to `sys:` functions in the codebase.
2. For special processes, look for `sys:debug_options/1`, `sys:handle_debug/4`, and `sys:handle_system_msg/6`.

# Context & Application

The `sys` module serves two roles: (1) as an external debugging interface for inspecting any OTP process, and (2) as a building block for implementing the debugging and system message infrastructure within special processes. When used with standard behaviours, no special code is needed -- just call the sys functions on the process. When building special processes, the module provides the primitives needed for OTP compliance.

# Examples

**Example 1** (spec_proc.md, "Simple Debugging"): Using sys functions on a gen_statem process:

```erlang
1> code_lock:start_link([1,2,3,4]).
{ok,<0.90.0>}
2> sys:statistics(code_lock, true).
ok
3> sys:trace(code_lock, true).
ok
4> code_lock:button(1).
*DBG* code_lock receive cast {button,1} in state locked
ok
```

**Example 2** (spec_proc.md, "Simple Debugging"): Getting statistics:

```erlang
8> sys:statistics(code_lock, get).
{ok,[{start_time,{{2024,5,3},{8,11,1}}},
     {current_time,{{2024,5,3},{8,11,48}}},
     {reductions,4098},
     {messages_in,5},
     {messages_out,0}]}
```

**Example 3** (spec_proc.md, "Special Processes / Example"): Using sys in a special process:

```erlang
2> sys:statistics(ch4, true).
ok
3> sys:trace(ch4, true).
ok
4> ch4:alloc().
ch4 event = {in,alloc,<0.88.0>}
ch4 event = {out,{ch4,1},<0.88.0>}
1
```

# Relationships

## Builds Upon
- **[Behaviour](/concept-cards/otp-design-principles/behaviour.md)** -- Works with any OTP behaviour process.

## Enables
- **[Special Process](/concept-cards/otp-design-principles/special-process.md)** -- sys provides the debugging and system message infrastructure.
- **[Debug Structure](/concept-cards/otp-design-principles/debug-structure.md)** -- sys creates and manages debug structures.
- **[System Messages](/concept-cards/otp-design-principles/system-messages.md)** -- sys handles system messages in special processes.

## Related
- **[proc_lib](/concept-cards/otp-design-principles/proc-lib.md)** -- Together, sys and proc_lib enable special process implementation.

## Contrasts With
- None directly.

# Common Errors

- **Error**: Forgetting to call `sys:handle_debug/4` for incoming and outgoing messages in a special process.
  **Correction**: Every system event (at least incoming and outgoing messages) should be passed through `sys:handle_debug/4` to enable tracing.

# Common Confusions

- **Confusion**: The `sys` module is only for special processes.
  **Clarification**: `sys` provides debugging for any OTP behaviour process (gen_server, gen_statem, gen_event). Special processes use additional sys functions to build the infrastructure that behaviours provide automatically.

# Source Reference

spec_proc.md, "Simple Debugging" section and "sys and proc_lib" introduction.

# Verification Notes

- Definition source: Directly from spec_proc.md, introduction and "Simple Debugging" section.
- Confidence rationale: High -- explicitly described with interactive examples.
- Uncertainties: None.
- Cross-reference status: References behaviour, special-process, proc-lib, debug-structure, system-messages.
