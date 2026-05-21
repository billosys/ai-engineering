---
# === CORE IDENTIFICATION ===
concept: System Boot Process
slug: system-boot-process

# === CLASSIFICATION ===
category: applications-releases
subcategory: system-principles
tier: advanced

# === PROVENANCE ===
source: "Designing for Scalability with Erlang/OTP"
source_slug: design-scale-erlang-otp
authors: Francesco Cesarini & Steve Vinoski
chapter: "System Principles and Release Handling"
chapter_number: 10
pdf_page: 282
section: "Script files"

# === CONFIDENCE ===
extraction_confidence: medium

# === VARIANTS (authority control) ===
aliases:
  - startup procedure
  - node startup
  - booting a release

# === TYPED RELATIONSHIPS ===
prerequisites:
  - boot-script-file
  - boot-file
extends: []
related:
  - init-module
  - code-loading-and-code-paths
  - erlang-loader
  - target-system
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How does the system boot process work?"
  - "How do I package, start, and configure a release?"
---

# Quick Definition

The system boot process is the sequence the Erlang runtime follows to start a release: preload core modules, load all application modules, start the kernel processes, load applications, then start them. It is driven by the commands in the boot file.

# Core Definition

At startup the runtime executes all the commands in the boot file, interpreted by the `init` module (Cesarini & Vinoski, p. 277, 302, pdf p. 282). The procedure proceeds in stages: (1) preload the `erts` modules and `error_handler`, signalling `{kernel_load_completed}`; (2) for every application in the `.rel` file, add its path and `primLoad` its modules, signalling `modules_loaded`; (3) start the kernel processes `heart`, `error_logger`, and `application_controller`, signalling `init_kernel_started`; (4) call `application:load/1` for every application, signalling `applications_loaded`; (5) start the applications via `application:start_boot/2`; and finally call `c:erlangrc()` and issue the `started` progress report.

# Prerequisites

- **Boot script file** — The boot process executes the actions listed in the `.script`/`.boot` file.
- **Boot file** — The binary boot file is what the runtime actually interprets at startup.

# Key Properties

1. Driven entirely by the boot file, interpreted by the preloaded `init` module.
2. Stage 1: preload `erts` modules plus `kernel`'s `error_handler`.
3. Stage 2: load all application modules via `primLoad`.
4. Stage 3: start kernel processes `heart`, `error_logger`, `application_controller`.
5. Stage 4: `application:load/1` each application in the `.rel` file.
6. Stage 5: start applications with the undocumented `application:start_boot/2`.
7. Final step: `c:erlangrc()` reads and executes the `.erlang` file; `{progress, started}` flips the internal state from `starting` to `started`.
8. Startup is synchronous — a kernel process or `apply` that exits abnormally aborts startup and terminates the node.

# Construction / Recognition

## To Trace the Boot Process:
1. Start the node with the `-init_debug` flag to print every step executed in the boot script.
2. Optionally add the `-emu_args` flag to print all emulator arguments.
3. Call `init:get_status/0` to retrieve `{InternalState, ProgressState}`.

## To Recognize the Stages:
1. Watch for progress reports: `preloaded`, `kernel_load_completed`, `modules_loaded`, `init_kernel_started`, `applications_loaded`, `started`.

# Context & Application

- **Typical contexts**: Diagnosing why a node fails to start or restart.
- **Common applications**: Troubleshooting corrupt beam files, wrong code paths, missing `sys.config`; reducing startup time by trimming the boot script.
- **Historical/stylistic notes**: Before `-init_debug`, developers hand-added progress reports after each `primLoad` to locate a corrupted beam file.

# Examples

**Example 1** (p. 277): The six-step walkthrough of the `basestation` boot script — preload, load application modules, start kernel processes, `application:load`, `application:start_boot`, then `c:erlangrc()`.

**Example 2** (p. 301-302): Booting from a remote boot server with `-loader inet` and `-init_debug` prints `{progress,preloaded}`, `{progress,kernel_load_completed}`, `{progress,modules_loaded}`, `{start,heart}`, `{start,error_logger}`, `{start,application_controller}`, `{progress,init_kernel_started}`, ending with `{progress,started}`.

# Relationships

## Builds Upon
- **Boot script file** — Its action list is the program the boot process runs.
- **Boot file** — The binary form actually interpreted at startup.

## Related
- **Init module** — Interprets the boot file and manages startup/shutdown.
- **Code loading and code paths** — The boot process loads all application modules via `primLoad`.
- **Erlang loader** — `erl_prim_loader` fetches modules during the boot process.
- **Target system** — The boot process differs between interactive and embedded code-loading modes.

# Common Errors

- **Error**: Calling a function via `-s`/`-run` that links to the init process or never returns.
  **Correction**: Startup is synchronous; functions must return, and they should not depend on linking to the init process.

- **Error**: Ignoring startup errors because no shell is visible.
  **Correction**: Check the `log` directory and SASL report logs; a node refusing to start records why there.

# Common Confusions

- **Confusion**: Thinking applications are started with `application:start/1` during boot.
  **Clarification**: The boot script uses the undocumented `application:start_boot/2`, which assumes the application is already loaded.

- **Confusion**: Believing all progress states drive the startup.
  **Clarification**: Only `{progress, started}` flips the internal state to `started`; other phases are purely for debugging.

# Source Reference

Chapter 10: System Principles and Release Handling, section "Script files" and "The init Module," pages 276-279 and 302-303 (pdf p. 282).

# Verification Notes

- Definition source: Synthesized from the step-by-step walkthrough on pp. 277-278 and the `init` module description on pp. 302-303.
- Confidence rationale: MEDIUM — the source describes the stages clearly but does not present "the system boot process" as a single named, formally defined concept; the definition is synthesized.
- Uncertainties: None significant.
- Cross-reference status: Verified against planned cards.
- Re-extraction notes: Fresh extraction; no pre-existing card.
