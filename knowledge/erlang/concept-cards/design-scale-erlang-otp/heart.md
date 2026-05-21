---
# === CORE IDENTIFICATION ===
concept: Heart
slug: heart

# === CLASSIFICATION ===
category: production-ops
subcategory: fault-recovery
tier: intermediate

# === PROVENANCE ===
source: "Designing for Scalability with Erlang/OTP"
source_slug: design-scale-erlang-otp
authors: Francesco Cesarini & Steve Vinoski
chapter: "System Principles and Release Handling"
chapter_number: 10
pdf_page: 282
section: "Heart"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - heart program
  - heartbeat monitor
  - HEART_COMMAND

# === TYPED RELATIONSHIPS ===
prerequisites:
  - erlang-runtime-system
extends: []
related:
  - target-system
  - init-module
  - arguments-and-flags
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is heart and how does it restart a crashed Erlang node?"
  - "How do I monitor a production system and provide preemptive support?"
---

# Quick Definition

Heart is an external program that monitors the Erlang virtual machine via regular heartbeats. If a heartbeat is missed, heart terminates the VM and invokes a user-defined command to restart the runtime system.

# Core Definition

Heart can be seen as the supervisor of the node itself (Cesarini & Vinoski, p. 296-298, pdf p. 282). It is an external program that monitors the virtual machine, receiving regular heartbeats sent by an Erlang process through a port. If the external program fails to receive a heartbeat within a predefined interval, it attempts to terminate the virtual machine and invokes a user-defined command to restart the runtime system. Heart is enabled by passing the `-heart` flag, and is configured through OS environment variables `HEART_COMMAND`, `HEART_BEAT_TIMEOUT`, and `ERL_CRASH_DUMP_SECONDS`.

# Prerequisites

- **Erlang runtime system** — Heart monitors the runtime; understanding the runtime comes first.

# Key Properties

1. An external program — the "supervisor of the node itself."
2. Receives heartbeats from an Erlang process through a port.
3. On a missed heartbeat: terminates the VM and invokes `HEART_COMMAND`.
4. `HEART_COMMAND` — the script triggered on timeout; if unset, only a warning is logged and the system is not restarted.
5. `HEART_BEAT_TIMEOUT` — seconds heart waits for a heartbeat (OTP 17+: > 10 and <= 65,535; default 60).
6. `ERL_CRASH_DUMP_SECONDS` — time the VM may spend writing a crash dump (default 0 with heart = no dump; -1 = unlimited).
7. Enabled via the `-heart` flag; on Unix heart kills its target with SIGKILL, which cannot be caught (so no crash dump).
8. Race conditions between heart, heartbeats, and restarts can occur, e.g. under I/O starvation with a low `HEART_BEAT_TIMEOUT`.

# Construction / Recognition

## To Enable Heart:
1. Write a restart script (e.g. `bsc_heart`) that calls `bin/start`.
2. Set the `HEART_COMMAND` environment variable to point to the script.
3. Edit `start_erl` to add the `-heart` flag.
4. Optionally set `HEART_BEAT_TIMEOUT` and `ERL_CRASH_DUMP_SECONDS`.
5. Start the system; heart now restarts the node on any VM crash.

## To Recognize It:
1. The `-heart` flag in the start command.
2. The `heart` binary in `erts-Version/bin`.

# Context & Application

- **Typical contexts**: Embedded Erlang systems run as daemons that must self-recover from VM crashes.
- **Common applications**: Restarting a node after an unexpected memory spike, a top-level supervisor terminating, a dodgy NIF segfault, or a VM hang.
- **Historical/stylistic notes**: The Yaws web server uses heart with extra environment variables (`HEART`, `YAWS_HEART_RESTARTS`, `YAWS_HEART_START`) so its restart script tracks restart counts and refuses to restart after too many.

# Examples

**Example 1** (p. 297): A simple restart script placed in the target `bin` directory:

```
#!/bin/sh
#Basic Heart Script for the Base Station Controller
ROOTDIR=/Users/francescoc/ernie
$ROOTDIR/bin/start
```

**Example 2** (p. 297): Setting environment variables and enabling heart, then killing the node with `halt()` — every reconnect shows command prompt `1` again because heart immediately restarted the process.

**Example 3** (p. 298): Setting variables via flags: `erl -heart -env HEART_BEAT_TIMEOUT 10 -env HEART_COMMAND boot_bsc`.

# Relationships

## Builds Upon
- **Erlang runtime system** — Heart monitors and restarts the runtime.

## Related
- **Target system** — Heart is recommended for embedded target systems.
- **Init module** — `init:reboot/0` interacts with heart, creating a potential race condition.
- **Arguments and flags** — Heart is enabled via the `-heart` flag and configured via `-env`.

# Common Errors

- **Error**: Setting a very low `HEART_BEAT_TIMEOUT` on a heavily loaded system.
  **Correction**: Account for I/O starvation; a too-low timeout makes heart kill a healthy-but-busy VM with SIGKILL, producing no crash dump.

- **Error**: Using `start` directly as the heart command for a blind restart.
  **Correction**: Real-world scenarios need a restart script that tracks restart counts and can stop cyclic restarts (as Yaws does).

# Common Confusions

- **Confusion**: Thinking heart writes a crash dump when it kills the VM.
  **Clarification**: On Unix, heart uses SIGKILL, which the target cannot catch — so no crash dump is generated unless `ERL_CRASH_DUMP_SECONDS` allows it.

- **Confusion**: Believing heart restarts the node even without configuration.
  **Clarification**: If `HEART_COMMAND` is not set, a timeout only logs a warning; the system is not restarted.

# Source Reference

Chapter 10: System Principles and Release Handling, section "Heart" (including "How Does Yaws Use Heart?"), pages 296-300 (pdf p. 282).

# Verification Notes

- Definition source: Direct adaptation of pp. 296-298.
- Confidence rationale: HIGH — the source explicitly defines heart, its mechanism, and its environment variables.
- Uncertainties: None.
- Cross-reference status: Verified against planned cards.
- Re-extraction notes: Fresh extraction; no pre-existing card.
