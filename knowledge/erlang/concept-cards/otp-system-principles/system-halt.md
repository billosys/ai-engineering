---
# === CORE IDENTIFICATION ===
concept: System Halt
slug: system-halt

# === CLASSIFICATION ===
category: production-ops
subcategory: runtime-lifecycle
tier: intermediate

# === PROVENANCE ===
source: "OTP System Principles"
source_slug: otp-system-principles
authors: "Ericsson AB"
chapter: "System Principles"
chapter_number: null
pdf_page: null
section: "Restarting and Stopping the System"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "halt/0"
  - "halt/1"
  - "halt/2"
  - halting the system

# === TYPED RELATIONSHIPS ===
prerequisites:
  - erlang-runtime-system
extends: []
related:
  - init-module
  - erl-command
contrasts_with:
  - init-module

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do I start/stop/restart an Erlang runtime system?"
  - "What is the difference between halt and init:stop?"
---

# Quick Definition

The runtime system can be immediately terminated by calling `halt/0,1,2`, or it terminates automatically if the Erlang shell process exits.

# Core Definition

The Erlang runtime system is halted by calling `halt/0,1,2` (a BIF in the `erlang` module). This provides immediate termination of the runtime system, in contrast to the graceful shutdown provided by `init:stop/0`. Additionally, the runtime system terminates if the Erlang shell is terminated (e.g., by pressing Ctrl+G followed by `q`, or by closing the terminal).

Source: "Restarting and Stopping the System" section of OTP System Principles documentation (Ericsson AB).

# Prerequisites

- **erlang-runtime-system** — halting terminates a running runtime system

# Key Properties

1. `halt/0` halts the runtime system immediately with a zero exit status
2. `halt/1` accepts a status code (integer) or an abort message (string)
3. `halt/2` accepts a status code and options
4. Halting is immediate — applications do not get a chance to clean up
5. The runtime system also terminates if the Erlang shell is terminated
6. `halt` is a BIF in the `erlang` module, not in the `init` module

# Construction / Recognition

## To Construct/Create:
1. Call `halt()` or `halt(Status)` or `halt(Status, Options)` from Erlang code
2. Alternatively, terminate the Erlang shell to halt the system

## To Identify/Recognize:
1. Any call to `erlang:halt/0,1,2` or the shorthand `halt/0,1,2` triggers system halting
2. Shell termination (Ctrl+G then `q`, Ctrl+C then `a`, or terminal closure) also halts the system

# Context & Application

System halt is used when immediate termination is required, such as during catastrophic failures or when a specific OS exit code must be returned. In production systems, `init:stop/0` is generally preferred because it allows applications to shut down gracefully. However, `halt` is appropriate when the system state is corrupt or when wrapping Erlang in scripts that check exit codes. The shell-termination behavior is important to understand for development environments and for systems that must not rely on the shell remaining active.

# Examples

**Example 1** (System Principles section): The source indicates halting is done via the BIF:

```erlang
%% Halt immediately with exit status 0
halt().

%% Halt with a specific exit status
halt(1).

%% Halt with status and options
halt(0, [{flush, true}]).
```

**Example 2** (System Principles section): The source notes that shell termination also halts the system:

```text
The runtime system terminates if the Erlang shell is terminated.
```

# Relationships

## Builds Upon
- **erlang-runtime-system** — `halt` terminates the runtime system

## Enables
- No downstream concepts depend on halt specifically.

## Related
- **init-module** — provides the alternative graceful shutdown via `init:stop/0`
- **erl-command** — the `erl` command starts the system that `halt` terminates

## Contrasts With
- **init-module** — `halt/0,1,2` terminates immediately without cleanup, while `init:stop/0` performs a graceful shutdown allowing applications to terminate orderly; `init:restart/0` and `init:reboot/0` restart/reboot rather than terminate

# Common Errors

- **Error**: Using `halt/0` in production when applications need to clean up resources (close files, flush logs, deregister from service discovery).
  **Correction**: Use `init:stop/0` for graceful shutdown. Reserve `halt` for emergency termination or scripting scenarios.

- **Error**: Not accounting for shell termination halting the entire runtime system.
  **Correction**: In production, do not rely on an interactive shell. Use embedded mode with a proper boot script, or use `run_erl`/`to_erl` for detached operation.

# Common Confusions

- **Confusion**: `halt/0` and `init:stop/0` are interchangeable.
  **Clarification**: `halt/0` terminates the runtime immediately without allowing applications to shut down. `init:stop/0` initiates a graceful shutdown, giving each application the opportunity to clean up before the system exits.

- **Confusion**: The shell is just an interface and terminating it has no effect on the runtime.
  **Clarification**: The source explicitly states that "the runtime system terminates if the Erlang shell is terminated." This is an important operational consideration.

# Source Reference

"Restarting and Stopping the System" section, "System Principles" chapter, OTP System Principles documentation.

# Verification Notes

- Definition source: direct (source explicitly mentions halt/0,1,2 and shell termination)
- Confidence rationale: The source directly states the halting mechanisms
- Uncertainties: The full options for halt/2 are not detailed in this source; they are in the `erlang` module reference
- Cross-reference status: verified against source text
