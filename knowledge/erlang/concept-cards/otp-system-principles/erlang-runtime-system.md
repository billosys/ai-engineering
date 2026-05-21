---
# === CORE IDENTIFICATION ===
concept: Erlang Runtime System
slug: erlang-runtime-system

# === CLASSIFICATION ===
category: applications-releases
subcategory: system-startup
tier: foundational

# === PROVENANCE ===
source: "OTP System Principles"
source_slug: otp-system-principles
authors: "Ericsson AB"
chapter: "System Principles"
chapter_number: null
pdf_page: null
section: "Starting the System"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - ERTS
  - "Erlang/OTP runtime"
  - runtime system

# === TYPED RELATIONSHIPS ===
prerequisites: []
extends: []
related:
  - erl-command
  - boot-script
  - init-module
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do I start an Erlang runtime system?"
  - "What is the Erlang runtime system?"
---

# Quick Definition

The Erlang runtime system is the execution environment for Erlang programs, started via the `erl` command, which loads code and starts applications according to a boot script.

# Core Definition

An Erlang runtime system is started with the command `erl`. When launched, it displays the OTP version, ERTS version, system capabilities (64-bit, SMP configuration, JIT), and enters the Erlang shell (Eshell). The runtime system loads code and starts processes and applications as directed by a boot script, and can operate in either interactive or embedded mode.

Source: "System Principles" section of OTP System Principles documentation (Ericsson AB).

# Prerequisites

Foundational concept with no prerequisites. The Erlang runtime system is the base layer upon which all other OTP concepts operate.

# Key Properties

1. Started via the `erl` command from the operating system shell
2. Accepts command-line arguments that configure its behavior
3. Uses a boot script to determine which code to load and which applications to start
4. Provides an interactive shell (Eshell) by default
5. Can operate in interactive mode (default) or embedded mode
6. Terminates if the Erlang shell is terminated

# Construction / Recognition

## To Construct/Create:
1. Install Erlang/OTP on the target system
2. Run the `erl` command from the OS shell
3. Optionally provide command-line flags (e.g., `-boot`, `-mode`, `-pa`)

## To Identify/Recognize:
1. The system prints a banner showing OTP version, ERTS version, and system capabilities
2. An Eshell prompt (e.g., `1>`) appears for interactive use
3. The `init` module is available for querying system state

# Context & Application

The Erlang runtime system is the fundamental execution environment for all Erlang and OTP applications. Every Erlang program, whether a simple script or a complex distributed system, runs within a runtime system instance. Understanding how to start, configure, and stop the runtime system is essential for both development and production deployment.

# Examples

**Example 1** (System Principles section): Starting the runtime system displays version information:

```text
% erl
Erlang/OTP 27 [erts-15.0] [64-bit] [smp:8:8] [ds:8:8:10] [async-threads:1] [jit]

Eshell V15.0 (press Ctrl+G to abort, type help(). for help)
1>
```

# Relationships

## Builds Upon
- No prerequisites — this is the foundational runtime layer.

## Enables
- **erl-command** — the `erl` command is the interface for starting the runtime system
- **boot-script** — the runtime system uses boot scripts to determine startup behavior
- **init-module** — the `init` module provides programmatic access to runtime system state and lifecycle

## Related
- **boot-script** — determines what code and applications the runtime system loads at startup
- **default-boot-scripts** — the pre-packaged boot scripts that ship with Erlang/OTP

## Contrasts With
- No direct contrasts at this foundational level.

# Common Errors

- **Error**: Attempting to run Erlang code without starting a runtime system first.
  **Correction**: Always start the runtime system with `erl` (or `erl` with appropriate flags) before executing Erlang code.

- **Error**: Not realizing the shell termination stops the entire runtime system.
  **Correction**: Understand that the runtime system terminates if the Erlang shell is terminated. Use `heart` or run in embedded mode for production systems.

# Common Confusions

- **Confusion**: The Erlang runtime system and the Erlang shell are the same thing.
  **Clarification**: The shell (Eshell) is an interactive interface running within the runtime system. The runtime system is the underlying execution environment that can run with or without a shell.

# Source Reference

"Starting the System" and "Restarting and Stopping the System" sections, "System Principles" chapter, OTP System Principles documentation.

# Verification Notes

- Definition source: direct (explicitly described in source)
- Confidence rationale: The source directly defines what the Erlang runtime system is and how it is started
- Uncertainties: none
- Cross-reference status: verified against source text
