---
# === CORE IDENTIFICATION ===
concept: Start Scripts and Target Configuration
slug: start-scripts-and-configuration

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
section: "Start Scripts and Configuring on the Target"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - start script
  - start_erl
  - start_erl.data
  - target configuration

# === TYPED RELATIONSHIPS ===
prerequisites:
  - target-system
  - release-package
extends: []
related:
  - boot-file
  - system-configuration-file
  - heart
  - erlang-runtime-system
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What are start scripts and how do I configure a release on the target?"
  - "How do I package, start, and configure a release?"
---

# Quick Definition

Start scripts are the shell scripts (`start`, `start_erl`, `run_erl`) that boot an embedded Erlang target system, configured with deployment-specific values such as the root directory, code paths, and boot file. They are accompanied by the `start_erl.data` file naming the erts and release versions.

# Core Definition

The start scripts are created and edited in the target directory's `bin` directory to boot the system (Cesarini & Vinoski, p. 286-289, pdf p. 282). The `start` script initializes the environment for the embedded system, then calls `start_erl`, which in turn starts Erlang via the `run_erl` script. `start_erl` is an embedded version of `erl`; `start` is a script you can customize freely. They are derived from the `.src` files (`start.src`, `start_erl.src`) in the runtime's `bin` directory. The `start_erl.data` file, placed in the `releases` directory, contains two space-separated items: the version of the Erlang runtime system and the release directory containing the boot scripts and config files.

# Prerequisites

- **Target system** — Start scripts boot an embedded target system; the target-system concept comes first.
- **Release package** — The scripts are configured after the package is unpacked into the target directory.

# Key Properties

1. Live in the target directory's `bin` directory.
2. `start` initializes the embedded environment and calls `start_erl`; `start_erl` calls `run_erl`; `to_erl` connects to the embedded shell.
3. Derived from `.src` files (`start.src`, `start_erl.src`) in the runtime's `bin`.
4. `start` must be edited to replace `%FINAL_ROOTDIR%` with the absolute path to the new Erlang root directory.
5. `start_erl.data` (in `releases`) holds the erts version and the release directory, space-separated.
6. A `log` directory receives all debug output from the start scripts — the first place to look on a startup failure.
7. It is good practice to include the `erl` command in the target `bin` directory for recovery when a node will not restart.

# Construction / Recognition

## To Configure Start Scripts on the Target:
1. Create a `bin` directory in the target directory.
2. Copy `start.src` -> `start`, `start_erl.src` -> `start_erl`, plus `run_erl` and `to_erl`.
3. Create a `log` directory for start-script debug output.
4. Edit `start`, replacing `%FINAL_ROOTDIR%` with the absolute Erlang root path.
5. Create `start_erl.data` in `releases` with the erts and release versions.
6. Ensure a (possibly empty) `sys.config` is in the release version directory.

## To Recognize Them:
1. Look for `start`, `start_erl`, `run_erl`, `to_erl` in the target `bin`.
2. Look for `start_erl.data` in `releases`.

# Context & Application

- **Typical contexts**: Configuring an embedded target system for a specific deployment.
- **Common applications**: Booting a node as a background daemon; redirecting I/O pipes to a subdirectory of the root so multiple nodes can run on one host.
- **Historical/stylistic notes**: The boundary between what the build does and what the on-target install scripts do varies among users; there is no one-size-fits-all approach.

# Examples

**Example 1** (p. 287): Editing the `start` script in place:

```
$ perl -i -pe "s#%FINAL_ROOTDIR%#$PWD#" bin/start
$ echo '7.2 1.0' > releases/start_erl.data
$ bin/start
$ bin/to_erl /tmp/
```

**Example 2** (p. 288): Redirecting the pipes — the last line of the `start` script shows where to replace `/tmp/` with an absolute path under the root directory: `$ROOTDIR/bin/run_erl -daemon /tmp/ $ROOTDIR/log "exec ..."`.

# Relationships

## Builds Upon
- **Target system** — Start scripts boot an embedded target system.
- **Release package** — They are configured after the package is unpacked.

## Related
- **Boot file** — The start scripts point the emulator at the `.boot` file.
- **System configuration file** — Start scripts reference `sys.config` via `-config`.
- **Heart** — `start_erl` is edited to add `-heart`; `HEART_COMMAND` often calls `start`.
- **Erlang runtime system** — `start_erl` is an embedded version of the runtime's `erl`.

# Common Errors

- **Error**: Forgetting to replace `%FINAL_ROOTDIR%` in the `start` script.
  **Correction**: Edit `start` to set `ROOTDIR` to the absolute path of the new Erlang root directory.

- **Error**: Leaving the I/O pipes in `/tmp` when running multiple embedded nodes on one host.
  **Correction**: Redirect the pipes to a subdirectory of the Erlang root directory so nodes do not collide.

# Common Confusions

- **Confusion**: Thinking `start_erl` and `erl` are unrelated.
  **Clarification**: `start_erl` is essentially an embedded version of `erl`; `start` is a customizable wrapper.

- **Confusion**: Believing startup errors are lost when there is no shell.
  **Clarification**: All start-script errors are recorded in the `log` directory.

# Source Reference

Chapter 10: System Principles and Release Handling, section "Start Scripts and Configuring on the Target," pages 286-289 (pdf p. 282).

# Verification Notes

- Definition source: Direct adaptation of pp. 286-289.
- Confidence rationale: HIGH — the source walks through start-script configuration step by step.
- Uncertainties: None.
- Cross-reference status: Verified against planned cards.
- Re-extraction notes: Fresh extraction; no pre-existing card.
