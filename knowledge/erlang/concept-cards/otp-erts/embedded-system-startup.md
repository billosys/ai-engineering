---
concept: Embedded System Startup
slug: embedded-system-startup
category: production-ops
subcategory: deployment
tier: advanced
source: "ERTS User's Guide"
source_slug: otp-erts
authors: "Ericsson AB"
chapter: "run_erl / start / start_erl"
chapter_number: null
pdf_page: null
section: "run_erl / start / start_erl"
extraction_confidence: high
aliases:
  - "run_erl"
  - "start_erl"
  - "start command"
  - "embedded mode startup"
  - "Erlang service startup"
prerequisites:
  - erl-command
  - init-flags
extends: []
related:
  - erl-command
  - emulator-flags
  - crash-dump
contrasts_with: []
answers_questions:
  - "How do I start Erlang in embedded/production mode?"
  - "What is run_erl and how does it work?"
  - "How do start, run_erl, and start_erl relate to each other?"
  - "How do I manage Erlang as a Windows service?"
---

# Quick Definition

The embedded system startup chain uses three cooperating programs -- `start`, `run_erl`, and `start_erl` -- to launch Erlang in production environments. On Unix, `run_erl` redirects I/O and provides logging and remote console access; `start` is a script that invokes `run_erl`; and `start_erl` reads the release data file to start the correct version. On Windows, `erlsrv` replaces `run_erl` for running Erlang as a Windows service.

# Core Definition

**run_erl** (Unix only): The documentation states: "The `run_erl` program is specific to Unix systems. This program redirects the standard input and standard output streams so that all output can be logged. It also lets the program `to_erl` connect to the Erlang console, making it possible to monitor and debug an embedded system remotely."

Usage: `run_erl [-daemon] pipe_dir/ log_dir "exec command arg1 arg2 ..."`

Key arguments:
- `-daemon` -- "highly recommended"; runs `run_erl` in the background completely detached from the terminal
- `pipe_dir` -- Directory for named pipes (must end with `/`), used by `to_erl` for remote console access
- `log_dir` -- Directory for log files: `run_erl.log` (progress/warnings) plus up to 5 rotating log files at 100 KB each
- The command string specifies the program to execute (typically `erl` or `start_erl`)

**start** (Unix only): "The `start` script is an example script on how to start up the Erlang system in embedded mode on Unix." It accepts an optional `data_file` argument to specify which `start_erl.data` file to use. The `RELDIR` environment variable sets the release directory.

**start_erl** (Windows): "This program aids release handling on Windows systems. The program is to be called by the `erlsrv` program, read up the release data file `start_erl.data`, and start Erlang." It uses the `++` delimiter to separate `erl` options from `start_erl` options. Key options include `-reldir`, `-rootdir`, `-data`, and `-bootflags`.

**erlsrv** (Windows): Allows Erlang emulators to run as Windows services. The documentation states it is "not a general service utility for Windows, but designed for embedded Erlang systems." Key parameters include `StopAction`, `OnFail` (reboot/restart/restart_always/ignore), `Machine`, `Priority`, and `DebugType`.

# Prerequisites

- **erl-command** -- The underlying Erlang runtime being started
- **init-flags** -- Boot files, config files, and node names used in embedded startup

# Key Properties

1. `run_erl` provides I/O redirection, logging, and remote console access via `to_erl`
2. Log files rotate: default 5 files at 100 KB each (configurable via environment variables)
3. "ALIVE" messages are written to logs after 15 minutes of inactivity by default
4. `run_erl -daemon` is essential for production -- without it, detaching from the terminal is difficult
5. `start_erl.data` contains the ERTS version and release version, used to locate the correct emulator and boot file
6. On Windows, `erlsrv` service naming must follow `NodeName_Release` convention for release handling
7. `erlsrv` supports `OnFail` actions: `reboot`, `restart`, `restart_always`, `ignore` (default)
8. The `start_erl` source code is distributed for customization (e.g., cyclic restart detection)

# Construction / Recognition

## To Construct/Create:

**Unix embedded startup:**

```text
run_erl -daemon /tmp/epipes/ /var/log/erlang "exec start_erl /usr/local/erlang"
```

Connect remotely to the running system:

```text
to_erl /tmp/epipes/
```

**Unix start script usage:**

```text
start [start_erl.data]
```

**Windows service registration:**

```text
erlsrv add myservice -sname mynode -args "-config myapp.config"
erlsrv start myservice
```

## To Identify/Recognize:

1. Production Erlang systems on Unix typically have `run_erl` processes and named pipe directories
2. The `start_erl.data` file in the releases directory identifies release-managed systems
3. On Windows, Erlang services appear in the Services applet with `erlsrv`-generated internal names

# Context & Application

These tools form the foundation of OTP release deployment. In a typical production setup:

1. The `start` script is invoked (manually or by the OS init system)
2. `start` calls `run_erl` with the `-daemon` flag
3. `run_erl` sets up I/O redirection and logging, then executes `start_erl`
4. `start_erl` reads `start_erl.data` to determine the ERTS and release versions
5. `start_erl` starts `erl` with the appropriate boot file and configuration

On Windows, `erlsrv` replaces `run_erl` and integrates with the Windows service manager. When using release handling, `erlsrv` should set the `Machine` parameter to `start_erl.exe` and `OnFail` to `ignore` (using `heart` for restart instead).

The `run_erl` logging can be tuned via environment variables:
- `RUN_ERL_LOG_GENERATIONS` -- Number of log files (default 5, range 2-1000)
- `RUN_ERL_LOG_MAXSIZE` -- Log file size in bytes (default 100000)
- `RUN_ERL_LOG_ALIVE_MINUTES` -- Inactivity timeout for ALIVE messages (default 15)
- `RUN_ERL_DISABLE_FLOWCNTRL` -- Disables flow control to prevent accidental Ctrl-S blocking

# Examples

**Example 1** (run_erl documentation, "Description" section): Basic run_erl invocation:

```text
run_erl -daemon pipe_dir/ log_dir "exec command arg1 arg2 ..."
```

**Example 2** (run_erl documentation, "Notes concerning the Log Files" section): Log file ALIVE messages:

```text
===== ALIVE Thu May 15 10:13:36 MEST 2003
```

**Example 3** (erlsrv documentation, "Environment" section): Heart command file for Windows service restart:

```text
@echo off
%ERLSRV_EXECUTABLE% stop %ERLSRV_SERVICE_NAME%
%ERLSRV_EXECUTABLE% start %ERLSRV_SERVICE_NAME%
```

# Relationships

## Builds Upon

- **erl-command** -- All these tools ultimately start erl with appropriate flags
- **init-flags** -- Boot files (`-boot`), config files (`-config`), and node names are passed through

## Related

- **emulator-flags** -- Emulator flags are passed through `run_erl`/`start_erl` to `erl`
- **crash-dump** -- Production systems using these tools need crash dump configuration

# Common Errors

- **Error**: Omitting the trailing `/` on `run_erl`'s pipe_dir argument
  **Correction**: The pipe directory "must be suffixed by a `/` (slash), that is, `/tmp/epipes/`, not `/tmp/epipes`"

- **Error**: Running `run_erl` without `-daemon` in production
  **Correction**: Without `-daemon`, detaching from the terminal requires "several tricks in the shell"; always use `-daemon` in production

- **Error**: On Windows, setting `erlsrv` OnFail to `restart` when using release handling
  **Correction**: "On a system where release handling is used, this is always to be set to `ignore`. Use `heart` to restart the service on failure instead."

# Common Confusions

- **Confusion**: Thinking `start_erl` is the same on Unix and Windows
  **Clarification**: "Although there are programs with the same name on other platforms, their functionality is different." The Windows `start_erl` reads the registry; Unix equivalents work differently.

- **Confusion**: Believing `run_erl` log files can be managed externally
  **Clarification**: `run_erl` manages its own log rotation internally. It maintains a "hole" in file sequences to indicate the newest file (e.g., if files #1, #2, #4, #5 exist, #2 is newest and #4 is oldest).

# Source Reference

"run_erl" command documentation (Description, Notes concerning the Log Files, Environment Variables), "start" command documentation (Description), "start_erl" command documentation (Description, Notes), and "erlsrv" command documentation (Description, service parameters, Environment, Notes).

# Verification Notes

- run_erl arguments and behavior: Directly from run_erl documentation
- start_erl options: Directly from start_erl documentation
- erlsrv parameters and OnFail values: Directly from erlsrv documentation
- Log rotation details: Directly from run_erl "Notes concerning the Log Files"
- Environment variables: Directly from run_erl "Environment Variables" section
- Confidence: HIGH -- all content from explicit documentation across four source files
