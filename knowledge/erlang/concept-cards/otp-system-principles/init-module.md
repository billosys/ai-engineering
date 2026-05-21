---
# === CORE IDENTIFICATION ===
concept: The init Module
slug: init-module

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
section: "Starting the System / Restarting and Stopping the System"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - init
  - "init process"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - erlang-runtime-system
  - erl-command
extends: []
related:
  - system-halt
  - boot-script
contrasts_with:
  - system-halt

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do I start/stop/restart an Erlang runtime system?"
  - "How can I access command-line arguments from within Erlang?"
---

# Quick Definition

The `init` module provides functions for accessing command-line arguments and controlling the lifecycle of the Erlang runtime system, including restarting, rebooting, and stopping it.

# Core Definition

The `init` module serves two primary roles in the Erlang runtime system. First, it provides functions to access the values of command-line arguments passed to `erl`: `init:get_argument(Key)` retrieves a specific argument, `init:get_arguments()` retrieves all arguments, and `init:get_plain_arguments()` retrieves non-flag arguments. Second, it provides lifecycle control functions: `init:restart()` restarts the system, `init:reboot()` reboots it, and `init:stop()` stops it. The `init` process also interprets the boot script at system startup, and the `-init_debug` flag enables tracing of this interpretation.

Source: "Starting the System" and "Restarting and Stopping the System" sections of OTP System Principles documentation (Ericsson AB).

# Prerequisites

- **erlang-runtime-system** — the `init` module operates within and controls the runtime system
- **erl-command** — command-line arguments accessed by `init` are passed via `erl`

# Key Properties

1. Provides `get_argument/1` to retrieve a specific command-line argument by key
2. Provides `get_arguments/0` to retrieve all command-line arguments
3. Provides `get_plain_arguments/0` to retrieve non-flag (plain) arguments
4. Provides `restart/0` to restart the runtime system
5. Provides `reboot/0` to reboot the runtime system
6. Provides `stop/0` to stop the runtime system gracefully
7. The init process interprets the boot script during system startup
8. Boot script interpretation can be traced with the `-init_debug` flag

# Construction / Recognition

## To Construct/Create:
1. The `init` module is always available — it is part of the ERTS application
2. No construction needed; call its functions directly

## To Identify/Recognize:
1. Any call to `init:restart()`, `init:reboot()`, `init:stop()` is using this module
2. Any call to `init:get_argument/1`, `init:get_arguments/0`, `init:get_plain_arguments/0` is querying command-line arguments through this module
3. The `-init_debug` flag traces the init process's boot script interpretation

# Context & Application

The `init` module is used whenever an application needs to programmatically control the runtime system lifecycle or inspect the command-line arguments that were used to start the system. In production, `init:stop/0` is the preferred way to perform a graceful shutdown, while `init:restart/0` and `init:reboot/0` are used for runtime system recovery. The argument-access functions are commonly used by application configuration code that needs to read custom command-line parameters.

# Examples

**Example 1** (System Principles section): The three argument-access functions are listed for application use:

```erlang
%% Retrieve a specific command-line argument
init:get_argument(home).

%% Retrieve all command-line arguments
init:get_arguments().

%% Retrieve plain (non-flag) arguments
init:get_plain_arguments().
```

**Example 2** (System Principles section): The three lifecycle control functions:

```erlang
%% Restart the runtime system (re-executes the boot script)
init:restart().

%% Reboot the runtime system
init:reboot().

%% Stop the runtime system gracefully
init:stop().
```

# Relationships

## Builds Upon
- **erlang-runtime-system** — `init` controls the lifecycle of the runtime system
- **erl-command** — the command-line arguments that `init` retrieves are passed to `erl`

## Enables
- **boot-script** — the init process interprets boot scripts at startup

## Related
- **system-halt** — `halt/0,1,2` provides an alternative (immediate) way to terminate the system, contrasting with `init:stop/0`

## Contrasts With
- **system-halt** — `init:stop/0` performs a graceful shutdown while `halt/0` terminates immediately; `init:restart/0` and `init:reboot/0` have no equivalent in `halt`

# Common Errors

- **Error**: Confusing `init:restart/0` with `init:reboot/0`.
  **Correction**: Consult the `init` module documentation for the specific semantics of each — `restart` re-executes the boot script within the same OS process, while `reboot` terminates and restarts the entire emulator.

- **Error**: Using `halt/0` when a graceful shutdown is needed.
  **Correction**: Use `init:stop/0` for graceful shutdown, which allows applications to clean up. Use `halt/0` only for immediate termination.

# Common Confusions

- **Confusion**: The `init` module is only for stopping the system.
  **Clarification**: The `init` module has a dual role: argument access (get_argument, get_arguments, get_plain_arguments) and lifecycle control (restart, reboot, stop). It also interprets the boot script at startup.

# Source Reference

"Starting the System" and "Restarting and Stopping the System" sections, "System Principles" chapter, OTP System Principles documentation.

# Verification Notes

- Definition source: direct (source explicitly lists the functions and their roles)
- Confidence rationale: All six functions are directly named and linked in the source text
- Uncertainties: The precise behavioral difference between restart and reboot is not elaborated in this source section; full details are in the init module reference
- Cross-reference status: verified against source text
