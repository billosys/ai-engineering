---
# === CORE IDENTIFICATION ===
concept: Arguments and Flags
slug: arguments-and-flags

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
section: "Arguments and Flags"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - emulator flags
  - command-line flags
  - plain arguments
  - erl flags

# === TYPED RELATIONSHIPS ===
prerequisites:
  - erlang-runtime-system
extends: []
related:
  - boot-file
  - system-configuration-file
  - init-module
  - start-scripts-and-configuration
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What types of arguments can be passed to the Erlang runtime?"
  - "How do I package, start, and configure a release?"
---

# Quick Definition

When starting Erlang you can pass three kinds of arguments: emulator flags (prefixed `+`, controlling the VM), flags (prefixed `-`, passed to the Erlang side of the runtime), and plain arguments (user-defined, not interpreted by the runtime).

# Core Definition

When starting Erlang, three different types of arguments can be passed to the runtime system (Cesarini & Vinoski, p. 290-296, pdf p. 282): *emulator flags*, recognized by their initial `+` character, control the behavior of the virtual machine — system limits, memory management, scheduler options; *flags*, starting with `-`, are passed to the Erlang part of the runtime system and include code search paths, configuration files, environment variables, and distributed-Erlang settings; and *plain arguments* are user-defined, not interpreted by the runtime, and usable in application business logic.

# Prerequisites

- **Erlang runtime system** — Arguments and flags configure the runtime; understanding the runtime comes first.

# Key Properties

1. Three argument types: emulator flags (`+`), flags (`-`), plain arguments.
2. Emulator flags control the VM: `+Bc`/`+Bd`/`+Bi` (break handler), `+e Num` (max ETS tables), `+P Num` (max processes), `+Q Num` (max ports), `+t Num` (max atoms), `+R Rel` (distribution compatibility).
3. Flags include `-boot`, `-config`, `-name`/`-sname`, `-setcookie`, `-pa`/`-pz`, `-mode`, `-heart`, `-detached`, `-init_debug`, `-emu_args`, `-remsh`, `-args_file`, `-eval`, `-s`/`-run`, `-loader`.
4. `+Bc` is recommended for all live systems — Ctrl-c a terminates and restarts only the shell, not the VM.
5. `-mode embedded` is recommended for all production systems — all modules load at startup.
6. Flags are retrieved with `init:get_arguments/0` and `init:get_argument(Flag)`.
7. Plain arguments are retrieved with `init:get_plain_arguments/0`; they appear before flags, after `-extra`, or between `--` and the next flag.

# Construction / Recognition

## To Pass and Use Arguments:
1. Place emulator flags (`+...`), flags (`-...`), and plain arguments on the `erl` command line, or in an `-args_file`.
2. Use `-args_file FileName` (recommended) to keep arguments under version control.
3. Retrieve flags with `init:get_argument/1`, plain arguments with `init:get_plain_arguments/0`.

## To Recognize the Type:
1. `+` prefix -> emulator flag.
2. `-` prefix -> flag.
3. No prefix (before flags, after `-extra`, or between `--` and next flag) -> plain argument.

# Context & Application

- **Typical contexts**: Configuring system limits, code paths, and behavior of a deployed node.
- **Common applications**: Disabling the break handler with `+Bc` on live systems; running in embedded mode; connecting to remote nodes with `-remsh`; debugging startup with `-init_debug` and `-emu_args`.
- **Historical/stylistic notes**: Keeping `-emu_args` on permanently in production is recommended — its overhead is negligible and the information is invaluable.

# Examples

**Example 1** (p. 291): A command using several argument types:

```
erl -pa patches -boot basestation -config bsc -init_debug +Bc
```

This adds `patches` to the front of the code path, uses `basestation.boot` and `bsc.config`, sets `init_debug`, and uses `+Bc` to disable the break handler so Ctrl-c a only restarts the shell.

**Example 2** (p. 296): Retrieving arguments — `erl one -two three -pa bin/bsc -- four five -extra 6 7 eight` makes `init:get_plain_arguments()` return `["one","four","five","6","7","eight"]` and `init:get_argument(two)` return `{ok,[["three"]]}`.

# Relationships

## Builds Upon
- **Erlang runtime system** — Arguments configure the runtime.

## Related
- **Boot file** — Selected via the `-boot` flag.
- **System configuration file** — Selected via the `-config` flag.
- **Init module** — Retrieves flags and plain arguments.
- **Start scripts and configuration** — Arguments are set in the start scripts or an args file.

# Common Errors

- **Error**: Leaving the break handler enabled on a live system.
  **Correction**: Use `+Bc` so Ctrl-c a terminates and restarts only the shell, not the whole VM.

- **Error**: Hand-editing start scripts every time arguments change.
  **Correction**: Use `-args_file FileName` to keep arguments in a version-controlled file.

# Common Confusions

- **Confusion**: Thinking all `erl` arguments are interpreted by the runtime.
  **Clarification**: Plain arguments are user-defined and not interpreted; they are for application business logic.

- **Confusion**: Confusing emulator flags with flags.
  **Clarification**: Emulator flags start with `+` and control the VM; flags start with `-` and go to the Erlang side of the runtime.

# Source Reference

Chapter 10: System Principles and Release Handling, section "Arguments and Flags," pages 290-296 (pdf p. 282).

# Verification Notes

- Definition source: Direct adaptation of pp. 290-296.
- Confidence rationale: HIGH — the source explicitly defines the three argument types and lists their members.
- Uncertainties: None.
- Cross-reference status: Verified against planned cards.
- Re-extraction notes: Fresh extraction; no pre-existing card.
