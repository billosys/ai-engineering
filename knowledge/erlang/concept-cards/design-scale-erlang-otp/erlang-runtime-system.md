---
# === CORE IDENTIFICATION ===
concept: Erlang Runtime System
slug: erlang-runtime-system

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
section: "Release Directory Structure"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - ERTS
  - erts
  - Erlang virtual machine
  - emulator
  - BEAM

# === TYPED RELATIONSHIPS ===
prerequisites:
  - release
extends: []
related:
  - release-directory-structure
  - release-resource-file
  - boot-file
  - heart
  - arguments-and-flags
  - upgrading-the-emulator-and-core-applications
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is the Erlang runtime system?"
  - "How do I package, start, and configure a release?"
---

# Quick Definition

The Erlang runtime system (ERTS) is the layer that runs Erlang code, including a copy of the virtual machine and the executables and shell scripts in the `erts/bin` directory. Each release carries its own copy, version-stamped in the `erts-Version` directory.

# Core Definition

The Erlang runtime system is one of the four components of a release: the runtime system, including a copy of the virtual machine (Cesarini & Vinoski, p. 282, pdf p. 282). On disk it occupies the `erts` directory, which contains the binaries for the runtime system; after an installation has been upgraded, multiple `erts` instances may exist, distinguished by the erts version number appended to the directory name (p. 285). Its `bin` subdirectory contains executables and shell scripts for the virtual machine and the tools that can be invoked from the shell.

# Prerequisites

- **Release** — The runtime system is one component of a release; you must understand the release concept first.

# Key Properties

1. It is one of the four components of a release (applications, dependency applications, config/boot files, runtime system).
2. Lives in the `erts` directory, version-stamped as `erts-Version`.
3. Its `bin` subdirectory holds `erl`, `erlexec`, `erlc`, `epmd`, `escript`, `start`, `run_erl`, `to_erl`, `werl`, `start_erl`, `erlsrv`, `heart`, `dialyzer`, and `typer`.
4. `erl` is a script/program that starts the runtime and provides an interactive shell; it ultimately executes `erlexec`.
5. The runtime does not differentiate user-defined applications from Erlang/OTP-distribution applications.
6. A single runtime-system version may be shared by multiple nodes, or each release may ship its own.
7. The emulator version is reported by `erlang:system_info(otp_release)` and recorded in the `.rel` file's `{erts, Vsn}` tuple.

# Construction / Recognition

## To Include the Runtime in a Release:
1. Pass the `{erts, Dir}` directive to `systools:make_tar/2`, naming the directory of the runtime binaries.
2. The version is extracted automatically from the `.rel` file.
3. Ensure the binaries were compiled and tested on the target OS and hardware.

## To Recognize It:
1. Look for the `erts-Version` directory in the release.
2. Inspect `erts-Version/bin` for the runtime executables.

# Context & Application

- **Typical contexts**: Bundling the runtime into a self-contained deployment package.
- **Common applications**: Shipping an embedded target system that does not depend on a pre-installed Erlang; or omitting `erts` to share one runtime across many nodes.
- **Historical/stylistic notes**: The `erts-version/bin` directory contains links and copies of the scripts/executables of the default runtime version; environment variables redirect `erl` to the version in use.

# Examples

**Example 1** (p. 286): The `erl` script sets `ROOTDIR` and `BINDIR` and ends with `exec "$BINDIR/erlexec" ${1+"$@"}`, where `BINDIR` points to `$ROOTDIR/erts-7.2/bin`.

**Example 2** (p. 285): The startup banner reports the runtime: `Erlang/OTP 18 [erts-7.2] [smp:8:8] [async-threads:10] [kernel-poll:false]`.

**Example 3** (p. 284): `systools:make_tar("basestation", [{erts, "/usr/local/lib/erlang/"}, ...])` includes the runtime binaries, producing the `erts-7.2` directory.

# Relationships

## Builds Upon
- **Release** — The runtime is bundled into a release.

## Related
- **Release directory structure** — The `erts` directory holds the runtime.
- **Release resource file** — Names the erts version via `{erts, Vsn}`.
- **Boot file** — Interpreted by the runtime's `init` module at startup.
- **Heart** — An external program that monitors the runtime's heartbeat.
- **Upgrading the emulator and core applications** — Replacing the runtime version requires special upgrade handling.

# Common Errors

- **Error**: Including `erts` binaries compiled for a different OS/hardware than the target.
  **Correction**: Make sure the runtime binaries are compiled and tested on the target operating system and hardware platform.

- **Error**: Always shipping a runtime with every node when one shared installation would do.
  **Correction**: Omit `{erts, Dir}` when the runtime is already installed on the target or shared across nodes.

# Common Confusions

- **Confusion**: Thinking "embedded" runtime always means the same thing.
  **Clarification**: Erlang/OTP uses "embedded" in several contexts (embedded target system, embedded code-loading mode); they are distinct.

- **Confusion**: Believing the runtime treats your applications differently from standard ones.
  **Clarification**: It treats user-defined and Erlang/OTP-distribution applications identically.

# Source Reference

Chapter 10: System Principles and Release Handling, section "Release Directory Structure," pages 282-287 (pdf p. 282). See the `erts/bin` executable listing on pp. 285-287.

# Verification Notes

- Definition source: Synthesized from the release-component definition (p. 282) and the `erts` directory description (pp. 285-287).
- Confidence rationale: HIGH — the source describes the runtime system, its directory, and its contents in detail.
- Uncertainties: None.
- Cross-reference status: Verified against planned cards.
- Re-extraction notes: Fresh extraction; no pre-existing card.
