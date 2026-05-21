---
# === CORE IDENTIFICATION ===
concept: The init Module
slug: init-module

# === CLASSIFICATION ===
category: applications-releases
subcategory: system-principles
tier: intermediate

# === PROVENANCE ===
source: "Designing for Scalability with Erlang/OTP"
source_slug: design-scale-erlang-otp
authors: Francesco Cesarini & Steve Vinoski
chapter: "System Principles and Release Handling"
chapter_number: 10
pdf_page: 282
section: "The init Module"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - init
  - "init:restart"
  - "init:reboot"
  - "init:stop"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - system-boot-process
extends: []
related:
  - boot-file
  - arguments-and-flags
  - heart
  - erlang-runtime-system
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is the init module and how does it manage system startup and shutdown?"
  - "How does the system boot process work?"
---

# Quick Definition

The `init` module is the preloaded module that manages a node's arguments and its startup and shutdown procedures. It interprets the boot file at startup and provides functions to restart, reboot, and stop the system.

# Core Definition

The `init` module is preloaded in the Erlang runtime system; it manages arguments and the startup and shutdown procedures of a release (Cesarini & Vinoski, p. 302-303, pdf p. 282). At startup it executes all the commands in the boot file. It provides the ability to restart the system, cleanly shut down all applications and stop the node, and reboot the virtual machine, plus functions to query system status and retrieve command-line arguments.

# Prerequisites

- **System boot process** — `init` drives the boot process; understanding the process comes first.

# Key Properties

1. Preloaded in the runtime; interprets the boot file at startup.
2. `init:restart/0` — restarts the system in the node without restarting the emulator (applications taken down smoothly, modules unloaded, ports closed, boot file re-executed).
3. `init:reboot/0` — like restart, but also shuts down and restarts the emulator; can race with heart.
4. `init:stop/0` — takes the system down smoothly and stops the emulator; stops heart too; the correct way to stop a node.
5. `init:stop(Status)` has the same effect as `halt(Status)`.
6. `init:get_status/0` — returns `{InternalStatus, ProvidedStatus}` where `InternalStatus` is `starting`, `started`, or `stopping`.
7. `init:get_arguments/0`, `init:get_argument/1`, `init:get_plain_arguments/0` retrieve flags and plain arguments.
8. The `-shutdown_time` flag limits time spent taking down supervision trees during restart/reboot/stop.

# Construction / Recognition

## To Use the init Module:
1. Call `init:restart/0` to restart the node without restarting the emulator.
2. Call `init:reboot/0` to also restart the emulator.
3. Call `init:stop/0` to cleanly stop the node.
4. Call `init:get_status/0` to check startup/shutdown progress.

## To Recognize Its Use:
1. Calls of the form `init:restart/0`, `init:reboot/0`, `init:stop/0`, or `init:get_*`.

# Context & Application

- **Typical contexts**: Cleanly restarting, rebooting, or stopping a node; querying boot progress.
- **Common applications**: `init:stop/0` for graceful shutdown; `init:restart/0` after a release install that is not made permanent (reverts to the old version).
- **Historical/stylistic notes**: `init:reboot/0` can create a race condition with heart, which resolves when heart kills and restarts the emulator.

# Examples

**Example 1** (p. 303): `init:get_status()` returns `{InternalStatus, ProvidedStatus}`; `ProvidedStatus` is derived from the last `{progress, Info}` term interpreted by the boot script.

**Example 2** (Ch. 11, p. 344): After installing release 1.1 without making it permanent, `init:restart()` restarts the node back at version 1.0 because the install was not made permanent.

# Relationships

## Builds Upon
- **System boot process** — `init` executes the boot file's commands.

## Related
- **Boot file** — `init` interprets the boot file at startup.
- **Arguments and flags** — `init` retrieves flags and plain arguments.
- **Heart** — `init:reboot/0` interacts with heart.
- **Erlang runtime system** — `init` manages the runtime's startup and shutdown.

# Common Errors

- **Error**: Using `halt()` or `q()` to stop a node that needs a graceful shutdown.
  **Correction**: Use `init:stop/0`, which lets applications terminate and clean up properly and stops heart first.

- **Error**: Expecting `init:restart/0` to keep an installed-but-not-permanent release.
  **Correction**: A restart re-executes the original boot file; a release not made permanent reverts to the old version.

# Common Confusions

- **Confusion**: Thinking `init:restart/0` and `init:reboot/0` are equivalent.
  **Clarification**: `restart` re-runs the boot file in the same emulator; `reboot` also shuts down and restarts the emulator itself.

- **Confusion**: Believing `init` is an ordinary loadable module.
  **Clarification**: `init` is preloaded — it must exist before any other module can be loaded, since it interprets the boot file.

# Source Reference

Chapter 10: System Principles and Release Handling, section "The init Module," pages 302-303 (pdf p. 282).

# Verification Notes

- Definition source: Direct adaptation of pp. 302-303.
- Confidence rationale: HIGH — the source explicitly describes the `init` module and its key functions.
- Uncertainties: None.
- Cross-reference status: Verified against planned cards.
- Re-extraction notes: Fresh extraction; no pre-existing card.
