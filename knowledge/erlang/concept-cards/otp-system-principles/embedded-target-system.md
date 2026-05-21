---
# === CORE IDENTIFICATION ===
concept: Embedded Target System
slug: embedded-target-system

# === CLASSIFICATION ===
category: applications-releases
subcategory: deployment
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
aliases: []

# === TYPED RELATIONSHIPS ===
prerequisites:
  - target-system
  - simple-target-system
  - start-erl
  - run-erl
extends:
  - simple-target-system
related:
  - system-configuration-parameters
  - target-system-upgrade
contrasts_with:
  - basic-target-system
  - simple-target-system

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How does a basic target system differ from a simple or embedded target system?"
  - "How do I start a target system that boots automatically and logs output?"
---

# Quick Definition

An embedded target system extends a simple target system by supporting automatic startup at boot time and logging of runtime output to files, using `bin/start`, `run_erl`, and `start_erl`.

# Core Definition

As described in OTP System Principles: "An _embedded target system_ that also supports starting automatically at boot time, and logging output from the system to files for later inspection." It is started via the shell script `bin/start`, which "calls `bin/run_erl`, which in turn calls `bin/start_erl` (roughly, `start_erl` is an embedded variant of `erl`)."

# Prerequisites

- A target system created and installed with `target_system:create/1` and `target_system:install/2`.
- Understanding of `run_erl`, `to_erl`, and `start_erl`.
- A `sys.config` file in the release version directory.

# Key Properties

1. Started via the `bin/start` shell script (typically executed when the UNIX system boots).
2. Uses `run_erl` as a wrapper for logging runtime output to files.
3. Uses `start_erl` to determine the correct ERTS and release versions and boot accordingly.
4. Supports attaching to the running Erlang shell via `to_erl`.
5. Requires a `sys.config` file in the release version directory.
6. Supports the `-heart` option for automatic node restart on failure.
7. Logs are stored in the `log/` directory of the target system.

# Construction / Recognition

## To Construct/Create:
1. Install a target system using `target_system:install/2`.
2. Ensure a `sys.config` file exists in `releases/<version>/`.
3. Optionally edit `bin/start` to customize startup (e.g., add `-heart` for automatic restart).
4. Start via `bin/start`.

## To Identify/Recognize:
1. The system is started via `bin/start` rather than `bin/erl`.
2. Output is logged to files in the `log/` directory.
3. The `run_erl` and `start_erl` processes are running.
4. You can attach to the running system using `to_erl`.

# Context & Application

An embedded target system is the standard approach for production Erlang/OTP deployments. The `bin/start` script is generated from `erts-<version>/bin/start.src` during installation and is meant to be customized. It is typically invoked at UNIX boot time. The `-heart` option can be added to enable automatic restart if the Erlang node terminates, which is especially important for upgrades that change core applications (ERTS, Kernel, STDLIB, SASL).

# Examples

**Example 1** (Upgrading the Target System section): A `bin/start` script with `-heart` for automatic restart:

```text
#!/bin/sh
ROOTDIR=/usr/local/erl-target/

if [ -z "$RELDIR" ]
then
   RELDIR=$ROOTDIR/releases
fi

START_ERL_DATA=${1:-$RELDIR/start_erl.data}

$ROOTDIR/bin/run_erl -daemon /tmp/ $ROOTDIR/log "exec $ROOTDIR/bin/start_erl $ROOTDIR\
$RELDIR $START_ERL_DATA -heart"
```

**Example 2** (Starting a Target System section): Attaching to a running embedded target system:

```text
% /usr/local/erl-target/bin/to_erl /tmp/erlang.pipe.1
```

# Relationships

## Builds Upon
- **simple-target-system** — adds automatic boot and logging to the simple target system
- **run-erl** — uses `run_erl` for output logging and pipe-based shell attachment
- **start-erl** — uses `start_erl` to determine versions and boot the correct release

## Enables
- **target-system-upgrade** — embedded target systems with `-heart` support automatic restart during upgrades

## Related
- **system-configuration-parameters** — `start_erl` requires `sys.config` in the release directory

## Contrasts With
- **basic-target-system** — a basic target system is started interactively via `erl` with no logging or auto-boot
- **simple-target-system** — a simple target system supports code replacement but not automatic boot or logging

# Common Errors

- **Error**: Missing `sys.config` in the release version directory when starting an embedded target system.
  **Correction**: Ensure `releases/<version>/sys.config` exists; the system start will fail without it.

- **Error**: Not customizing the `bin/start` script for the deployment environment.
  **Correction**: The generated `bin/start` is only an example; edit it to suit your needs (paths, flags, `-heart`).

# Common Confusions

- **Confusion**: Thinking the `bin/start` script should not be edited.
  **Clarification**: The source explicitly states: "The shell script `start` ... is merely an example. Edit it to suit your needs." In contrast, `start_erl` "is normally not to be altered by the user."

# Source Reference

"Starting a Target System" and "Upgrading the Target System" sections, "OTP System Principles" documentation.

# Verification Notes

- Definition source: Direct from source text.
- Confidence rationale: High — explicitly defined with detailed startup chain description.
- Uncertainties: None.
- Cross-reference status: References start-erl, run-erl, simple-target-system, system-configuration-parameters, target-system-upgrade.
