---
# === CORE IDENTIFICATION ===
concept: run_erl and to_erl
slug: run-erl

# === CLASSIFICATION ===
category: production-ops
subcategory: startup
tier: advanced

# === PROVENANCE ===
source: "OTP System Principles"
source_slug: otp-system-principles
authors: "Ericsson AB"
chapter: "Creating and Upgrading a Target System"
chapter_number: null
pdf_page: null
section: "Starting a Target System"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "run_erl"
  - "to_erl"
  - "run_erl wrapper"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - target-system
  - target-system-installation
extends: []
related:
  - start-erl
  - embedded-target-system
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What distinguishes run_erl from to_erl?"
  - "How do I attach to a running embedded target system?"
  - "How is runtime output logged in an embedded target system?"
---

# Quick Definition

`run_erl` is a wrapper program that provides logging of output from the Erlang runtime system to files and creates named pipes for shell attachment. `to_erl` is its companion tool for attaching to the running Erlang shell through those pipes.

# Core Definition

As described in OTP System Principles: "`run_erl` is a wrapper that provides logging of output from the runtime system to file. It also provides a simple mechanism for attaching to the Erlang shell (`to_erl`)." In the embedded startup chain, `bin/start` calls `run_erl`, which in turn calls `start_erl`.

# Prerequisites

- An installed target system with `bin/run_erl` and `bin/to_erl` present.
- Understanding of the embedded target system startup chain.

# Key Properties

1. `run_erl` wraps the Erlang runtime, capturing all output to log files.
2. `run_erl` creates named pipes (e.g., `/tmp/erlang.pipe.1`) for shell attachment.
3. `run_erl` supports the `-daemon` flag to run in the background.
4. `to_erl` connects to a running Erlang node through the named pipe created by `run_erl`.
5. Both are copied from `erts-<version>/bin/` to `bin/` during `target_system:create/1`.
6. Logs are stored in the directory specified as an argument to `run_erl` (typically the `log/` directory).
7. After an upgrade that restarts the node, a new pipe is created (e.g., `erlang.pipe.2`).

# Construction / Recognition

## To Construct/Create:
1. `target_system:create/1` copies `run_erl` and `to_erl` from `erts-<version>/bin/` to `bin/`.
2. The `bin/start` script invokes `run_erl` with arguments for the pipe directory, log directory, and the command to execute.

## To Identify/Recognize:
1. `run_erl` is running as a daemon wrapping the Erlang runtime.
2. Named pipes exist in the specified pipe directory (e.g., `/tmp/erlang.pipe.1`).
3. Log files are being written to the specified log directory.

# Context & Application

`run_erl` and `to_erl` are essential for production embedded target systems. In a production environment, the Erlang node runs as a daemon without an interactive console. `run_erl` ensures that all output (including crash messages) is captured to log files rather than lost. `to_erl` allows operators to attach to the running node for inspection and debugging. The pipe mechanism means you can disconnect and reconnect without affecting the running system.

# Examples

**Example 1** (Upgrading the Target System section): `run_erl` invoked in the `bin/start` script:

```text
$ROOTDIR/bin/run_erl -daemon /tmp/ $ROOTDIR/log "exec $ROOTDIR/bin/start_erl $ROOTDIR\
$RELDIR $START_ERL_DATA -heart"
```

Here `/tmp/` is the pipe directory, `$ROOTDIR/log` is the log directory, and the quoted string is the command to execute.

**Example 2** (Upgrading the Target System section): Attaching to the running node with `to_erl`:

```text
% /usr/local/erl-target/bin/to_erl /tmp/erlang.pipe.1
```

After an upgrade that restarts the node, the new pipe is numbered incrementally:

```text
% /usr/local/erl-target/bin/to_erl /tmp/erlang.pipe.2
```

**Example 3** (Upgrading the Target System section): Logs from the running system can be found in the log directory specified to `run_erl`:

```text
Logs can be found in /usr/local/erl-target/log.
```

# Relationships

## Builds Upon
- **target-system-installation** — `run_erl` and `to_erl` are included in the installed target system

## Enables
- **embedded-target-system** — `run_erl` provides the logging and pipe mechanism that distinguishes embedded from simple target systems

## Related
- **start-erl** — `run_erl` calls `start_erl` in the startup chain

## Contrasts With
- No direct contrasts in source; `run_erl` (output logging wrapper) implicitly contrasts with `to_erl` (shell attachment tool) — they are complementary halves of the same mechanism.

# Common Errors

- **Error**: Using the wrong pipe path when calling `to_erl` after a system restart.
  **Correction**: After an upgrade/restart, a new pipe is created with an incremented number. Check `/tmp/` for the current `erlang.pipe.*` file.

- **Error**: Not specifying a log directory for `run_erl`.
  **Correction**: Always provide a log directory argument so runtime output is captured for later inspection.

# Common Confusions

- **Confusion**: Thinking `run_erl` and `to_erl` do the same thing.
  **Clarification**: `run_erl` is the wrapper that runs the Erlang system as a daemon with logging. `to_erl` is the client that attaches to a running `run_erl`-managed system. `run_erl` starts the system; `to_erl` connects to it afterward.

- **Confusion**: Thinking `to_erl` starts a new Erlang node.
  **Clarification**: `to_erl` only attaches to an already-running node through the named pipe created by `run_erl`. It does not start anything.

# Source Reference

"Starting a Target System" and "Upgrading the Target System" sections, "OTP System Principles" documentation.

# Verification Notes

- Definition source: Direct from source text.
- Confidence rationale: High — explicitly defined with clear functional description.
- Uncertainties: None.
- Cross-reference status: References start-erl, embedded-target-system, target-system-installation.
