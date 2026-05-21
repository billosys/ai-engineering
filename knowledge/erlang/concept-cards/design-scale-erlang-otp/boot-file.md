---
# === CORE IDENTIFICATION ===
concept: Boot File
slug: boot-file

# === CLASSIFICATION ===
category: applications-releases
subcategory: release-files
tier: intermediate

# === PROVENANCE ===
source: "Designing for Scalability with Erlang/OTP"
source_slug: design-scale-erlang-otp
authors: Francesco Cesarini & Steve Vinoski
chapter: "System Principles and Release Handling"
chapter_number: 10
pdf_page: 282
section: "Creating the Boot File"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - ".boot file"
  - binary boot file
  - binary start script

# === TYPED RELATIONSHIPS ===
prerequisites:
  - release-resource-file
extends: []
related:
  - boot-script-file
  - system-boot-process
  - release-directory-structure
  - alternative-boot-files
  - init-module
contrasts_with:
  - boot-script-file

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is a boot file?"
  - "How do I package, start, and configure a release?"
---

# Quick Definition

A boot file (`.boot`) is a binary file containing all the commands the Erlang runtime system executes to load modules and start applications when a release is first started. It is the binary representation of the textual `.script` file.

# Core Definition

The `.boot` file is a binary representation of the `.script` file, which contains commands to load and start applications when the system is first started (Cesarini & Vinoski, p. 287, pdf p. 282). It is created by `systools:make_script/2`, which produces a binary boot file used by a start script to boot Erlang and the system (p. 273-275). The boot file must be a binary because it contains the commands that load the modules that allow the runtime system to parse and interpret text files — so it cannot itself be a text file (p. 276).

# Prerequisites

- **Release resource file** — `systools:make_script/2` reads the `.rel` file to determine which applications and versions to load.

# Key Properties

1. Has the `.boot` extension and is a binary file.
2. Created by `systools:make_script/2` (also creatable from a `.script` file via `systools:script2boot/1`).
3. Must be binary because it loads the modules needed to parse text files.
4. Contains all commands executed by the runtime to start the release.
5. Used by the start script via the `-boot` flag; without an absolute path, the emulator looks in `$ROOT/bin`.
6. Boot-file generation runs sanity checks (application consistency/dependencies, presence of permanent `kernel` and `stdlib`, registered-name clashes, beam files matching app files).
7. The textual counterpart is the `.script` file, which is human-readable and editable.

# Construction / Recognition

## To Create a Boot File:
1. Place the `.rel` file and the application directories where `systools` can find them.
2. Add application `ebin` directories to the code path (`-pa`, `-pz`, or the `{path, DirList}` option).
3. Call `systools:make_script(Name, OptionsList)`.
4. The call produces `Name.script` and `Name.boot`.

## To Recognize It:
1. Look for a file with the `.boot` suffix in the release directory.
2. Confirm it is binary (the editable text form is the `.script` file).

# Context & Application

- **Typical contexts**: Building a release; starting a node with `erl -boot ReleaseName`.
- **Common applications**: Booting simple and embedded target systems; generating a `start_sasl`-like boot file so SASL logs are available when a node refuses to start.
- **Historical/stylistic notes**: Before `make_script/2` existed (OTP R1, 1996), boot files were hand-written.

# Examples

**Example 1** (p. 274): Generating and using the boot file:

```erlang
1> systools:make_script("basestation", [{path, ["bsc/ebin"]}]).
ok
```

```
$ erl -pa bsc/ebin -boot basestation
```

**Example 2** (p. 273): The four sanity checks run during boot-file creation — consistency/dependencies of applications, presence of permanent `kernel` and `stdlib`, registered-process-name clashes, and beam files matching app files.

**Example 3** (p. 274): A clash detected during generation — `Duplicated register names: overload registered in sasl and bsc`, fixed by renaming `overload` to `freq_overload` in `bsc.app`.

# Relationships

## Builds Upon
- **Release resource file** — The `.boot` file is generated from the `.rel` file.

## Enables
- **System boot process** — The boot file's commands drive node startup.

## Related
- **Boot script file** — The `.script` file is the editable text counterpart of the `.boot` file.
- **Alternative boot files** — `start_clean.boot`, `start_sasl.boot`, `no_dot_erlang.boot`, `start.boot`.
- **Init module** — The `init` module interprets the boot file at startup.

## Contrasts With
- **Boot script file** — The `.script` is text and editable; the `.boot` is binary and not directly editable.

# Common Errors

- **Error**: Editing the `.boot` file directly.
  **Correction**: Edit the `.script` file (or regenerate it), then convert with `systools:script2boot/1`.

- **Error**: Passing `-boot` a relative path expecting it found anywhere.
  **Correction**: Without an absolute path the emulator assumes the boot file is in `$ROOT/bin`; supply an absolute path otherwise.

# Common Confusions

- **Confusion**: Thinking the boot file could just be a text file.
  **Clarification**: It must be binary because it contains the commands that load the modules needed to parse and interpret text files.

- **Confusion**: Confusing the `.boot` file with the `.rel` file.
  **Clarification**: The `.rel` file is the specification of what is in the release; the `.boot` file is the executable command sequence generated from it.

# Source Reference

Chapter 10: System Principles and Release Handling, sections "Creating the Boot File" and "Script files," pages 273-277 (pdf p. 282). See Figure 11-4 "Creating boot and release files."

# Verification Notes

- Definition source: Direct adaptation of pp. 273-277.
- Confidence rationale: HIGH — the source explicitly describes the boot file, how it is created, and why it must be binary.
- Uncertainties: None.
- Cross-reference status: Verified against planned cards.
- Re-extraction notes: Fresh extraction; no pre-existing card.
