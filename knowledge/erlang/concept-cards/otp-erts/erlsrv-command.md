---
concept: The erlsrv Command
slug: erlsrv-command
category: production-ops
subcategory: deployment
tier: advanced
source: "ERTS User's Guide"
source_slug: otp-erts
authors: "Ericsson AB"
chapter: "erlsrv"
chapter_number: null
pdf_page: null
section: "erlsrv"
extraction_confidence: high
aliases:
  - "erlsrv"
  - "Erlang Windows service"
  - "erlsrv.exe"
prerequisites:
  - erl-command
  - embedded-system-startup
extends: []
related:
  - erl-command
  - embedded-system-startup
  - init-flags
contrasts_with: []
answers_questions:
  - "How do I run Erlang as a Windows service?"
  - "How do I configure an Erlang Windows service for automatic restart?"
  - "What is erlsrv?"
---

# Quick Definition

`erlsrv` is a Windows-specific utility that allows Erlang emulators to run as Windows services, enabling embedded systems to start without any user needing to log on. It provides both a command-line interface and integration with the Windows service manager for registering, starting, stopping, and configuring Erlang services.

# Core Definition

The documentation states: "This utility is specific to Windows NT/2000/XP (and later versions of Windows). It allows Erlang emulators to run as services on the Windows system, allowing embedded systems to start without any user needing to log on. The emulator started in this way can be manipulated through the Windows services applet in a manner similar to other services."

It is explicitly noted that "erlsrv is not a general service utility for Windows, but designed for embedded Erlang systems."

**Service parameters:**
- `StopAction` -- Erlang shell command to stop the emulator (default: TerminateProcess kill). The emulator has 30 seconds to stop after the command is issued.
- `OnFail` -- Action on unexpected stop: `reboot`, `restart` (with 10-second loop protection), `restart_always`, or `ignore` (default).
- `Machine` -- Path to the Erlang emulator (default: `erl.exe` in same directory as `erlsrv.exe`). Set to `start_erl.exe` when using release handling.
- `Env` -- Extra environment variables added to the system environment block.
- `WorkDir` -- Working directory (must be local drive; default: `%SystemDrive%%SystemPath%`).
- `Priority` -- Process priority: `realtime`, `high`, `low`, or `default`.
- `SName`/`Name` -- Node name (distribution is mandatory; default: `-sname <service name>`).
- `DebugType` -- Shell output destination: `new`, `reuse`, `console`, or `none` (default).
- `Comment` -- Service description text.

**Commands:**
- `erlsrv add <name> [options]` -- Register a new service
- `erlsrv set <name> [options]` -- Modify an existing service
- `erlsrv remove <name>` -- Remove a service (stops it first)
- `erlsrv start <name>` -- Start a service
- `erlsrv stop <name>` -- Stop a service
- `erlsrv start_disabled <name>` -- Atomically enable, start, then disable a service (useful during upgrades)
- `erlsrv enable <name>` / `erlsrv disable <name>` -- Set automatic/disabled state
- `erlsrv list [name]` -- List services or show details for one service

# Prerequisites

- **erl-command** -- erlsrv launches the Erlang emulator
- **embedded-system-startup** -- erlsrv is part of the embedded system startup chain on Windows

# Key Properties

1. Erlang services are always distributed (a node name is mandatory)
2. The service runs as the local administrator by default
3. Service processes can be killed with the Windows task manager (unlike normal services), but this triggers the OnFail action
4. The `start_disabled` command is atomic from an erlsrv user's perspective -- no other erlsrv commands can interleave
5. For release handling, the service name must follow `NodeName_Release` convention
6. Two environment variables are automatically set: `ERLSRV_SERVICE_NAME` and `ERLSRV_EXECUTABLE`
7. Port programs running in service context must handle `CTRL_LOGOFF_EVENT` and `CTRL_SHUTDOWN_EVENT` control events
8. The `console` DebugType does not survive logouts and disables StopAction and OnFail

# Construction / Recognition

## To Construct/Create:

Register and start a service:

```text
erlsrv add myservice -sname mynode -args "-config myapp"
erlsrv start myservice
```

Set up with release handling:

```text
erlsrv add mynode_1.0 -machine "C:\erlang\erts-15.0\bin\start_erl.exe" -args "++ -reldir C:\myapp\releases"
```

Create a heart command file for automatic restart:

```text
@echo off
%ERLSRV_EXECUTABLE% stop %ERLSRV_SERVICE_NAME%
%ERLSRV_EXECUTABLE% start %ERLSRV_SERVICE_NAME%
```

## To Identify/Recognize:

1. Erlang services appear in the Windows Services applet
2. The `ERLSRV_SERVICE_NAME` environment variable is set within a service context
3. `erlsrv list` shows all registered Erlang services

# Context & Application

`erlsrv` is the Windows counterpart to Unix's `run_erl`/`start` combination. It integrates Erlang into the Windows service infrastructure, supporting automatic startup at boot, failure recovery, and service state management.

For production systems using release handling, the documentation prescribes: set `Machine` to `start_erl.exe`, set `OnFail` to `ignore`, and use `heart` for restart management. The `start_disabled` command is specifically designed for release upgrades, providing an atomic sequence of enable-start-disable operations.

# Examples

**Example 1** (erlsrv documentation, "Environment" section): Heart command file for service restart:

```text
@echo off
%ERLSRV_EXECUTABLE% stop %ERLSRV_SERVICE_NAME%
%ERLSRV_EXECUTABLE% start %ERLSRV_SERVICE_NAME%
```

**Example 2** (erlsrv documentation, "Port Programs" section): C code to handle logoff events in service context:

```c
BOOL WINAPI service_aware_handler(DWORD ctrl){
    if(ctrl == CTRL_LOGOFF_EVENT)
        return TRUE;
    if(ctrl == CTRL_SHUTDOWN_EVENT)
        return TRUE;
    return FALSE;
}
```

# Relationships

## Builds Upon

- **erl-command** -- erlsrv starts the Erlang emulator with configured arguments
- **embedded-system-startup** -- Works with start_erl for release-managed Windows deployments

## Related

- **init-flags** -- Service arguments follow the same `-flag` syntax as erl

# Common Errors

- **Error**: Setting OnFail to `restart` when using release handling
  **Correction**: "On a system where release handling is used, this is always to be set to `ignore`. Use `heart` to restart the service on failure instead."

- **Error**: Using `werl` as the Machine parameter
  **Correction**: "Never use the `werl` program for this."

- **Error**: Specifying `-noinput` in the Args parameter
  **Correction**: `-noinput` cannot be specified as it would prevent StopActions from working

# Common Confusions

- **Confusion**: Thinking erlsrv is a general-purpose Windows service wrapper
  **Clarification**: The documentation states it is "not a general service utility for Windows, but designed for embedded Erlang systems"

- **Confusion**: Expecting DebugType logs to be suitable for production logging
  **Clarification**: "The `DebugType` is intended for debugging only. Logs during production are better produced with the standard Erlang logging facilities."

# Source Reference

"erlsrv" command documentation, covering "Description", service parameters, command syntax, "Environment", "Port Programs", and "Notes" sections.

# Verification Notes

- Service parameters and defaults: Directly from "Description" section parameter list
- Command syntax: Directly from command sections
- Heart command example: Verbatim from "Environment" section
- Port program example: Verbatim from "Port Programs" section
- Release handling requirements: Directly from OnFail and Notes sections
- Confidence: HIGH -- all content from explicit documentation
