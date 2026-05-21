---
# === CORE IDENTIFICATION ===
concept: Boot Script
slug: boot-script

# === CLASSIFICATION ===
category: applications-releases
subcategory: system-startup
tier: intermediate

# === PROVENANCE ===
source: "OTP System Principles"
source_slug: otp-system-principles
authors: "Ericsson AB"
chapter: "System Principles"
chapter_number: null
pdf_page: null
section: "Boot Scripts"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - ".script file"
  - ".boot file"
  - binary boot script
  - start script

# === TYPED RELATIONSHIPS ===
prerequisites:
  - erlang-runtime-system
  - erl-command
extends: []
related:
  - default-boot-scripts
  - user-defined-boot-script
  - init-module
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is a boot script in Erlang/OTP?"
  - "What distinguishes a .script file from a .boot file?"
  - "How do boot scripts relate to release resource files (.rel)?"
---

# Quick Definition

A boot script is a file containing instructions on which code to load and which processes and applications to start when the Erlang runtime system is launched. It exists in two forms: a human-readable `.script` file and a binary `.boot` file used by the runtime.

# Core Definition

The Erlang runtime system is started using a boot script. The boot script contains instructions on which code to load and which processes and applications to start. A boot script file has the extension `.script` (human-readable form). The runtime system uses a binary version of the script, called a binary boot script, which has the extension `.boot`. The boot script is specified via the `-boot` command-line flag (with the `.boot` extension omitted). If no boot script is specified, the system defaults to `ROOT/bin/start`, where `ROOT` is the Erlang/OTP installation directory. The `-init_debug` flag causes the `init` process to output debug information while interpreting the boot script.

Source: "Boot Scripts" section of OTP System Principles documentation (Ericsson AB).

# Prerequisites

- **erlang-runtime-system** — boot scripts control how the runtime system starts
- **erl-command** — the `-boot` flag on the `erl` command selects the boot script

# Key Properties

1. Contains instructions on which code to load and which processes/applications to start
2. The `.script` file is the human-readable text form
3. The `.boot` file is the binary form actually used by the runtime system
4. Selected via the `-boot` command-line flag (extension omitted)
5. Defaults to `ROOT/bin/start` if no `-boot` flag is provided
6. The `-init_debug` flag traces boot script interpretation
7. Syntax and contents are documented in the SASL application under `script`

# Construction / Recognition

## To Construct/Create:
1. Define a release resource file (`Name.rel`)
2. Generate the `.script` file using `systools:make_script/1,2`
3. The `.boot` file is generated alongside the `.script` file
4. Alternatively, convert a `.script` to `.boot` with `systools:script2boot/1`

## To Identify/Recognize:
1. Files with `.script` extension are human-readable boot scripts
2. Files with `.boot` extension are binary boot scripts
3. The `-boot` flag in an `erl` command line references a boot script

# Context & Application

Boot scripts are central to Erlang/OTP system startup. Every time the runtime system starts, it executes a boot script to load modules and start applications. For development, the default boot scripts (e.g., `start_clean`) are sufficient. For production deployments, especially in embedded mode, user-defined boot scripts generated from release resource files are used to precisely control which applications are started and in what order.

# Examples

**Example 1** (System Principles section): Specifying a boot script on the command line:

```text
% erl -boot start_all
```

Note that the `.boot` extension is omitted.

**Example 2** (System Principles section): Using `-init_debug` to trace boot script interpretation:

```text
% erl -init_debug
{progress,preloaded}
{progress,kernel_load_completed}
{progress,modules_loaded}
{start,heart}
{start,logger}
  .
  .
  .
```

# Relationships

## Builds Upon
- **erlang-runtime-system** — boot scripts direct the runtime system's startup
- **erl-command** — the `-boot` flag selects the boot script

## Enables
- **default-boot-scripts** — the default boot scripts are specific instances of boot scripts
- **user-defined-boot-script** — custom boot scripts extend the boot script concept for production use

## Related
- **init-module** — the init process interprets the boot script; `-init_debug` traces this

## Contrasts With
- No direct contrasts; `.script` vs `.boot` is a format distinction within this concept.

# Common Errors

- **Error**: Including the `.boot` extension in the `-boot` flag (e.g., `erl -boot start_clean.boot`).
  **Correction**: Omit the `.boot` extension: `erl -boot start_clean`.

- **Error**: Editing the `.boot` file directly instead of the `.script` file.
  **Correction**: The `.boot` file is a binary format. Edit the `.script` file or regenerate both from a `.rel` file using `systools:make_script/1,2`.

# Common Confusions

- **Confusion**: The `.script` file and `.boot` file serve different purposes.
  **Clarification**: They contain the same instructions in different formats. The `.script` file is human-readable text; the `.boot` file is the binary equivalent that the runtime system actually reads. Both represent the same boot script.

- **Confusion**: Boot scripts only load code.
  **Clarification**: Boot scripts both load code (modules) and start processes and applications. They define the complete startup sequence.

# Source Reference

"Boot Scripts" section, "System Principles" chapter, OTP System Principles documentation.

# Verification Notes

- Definition source: direct (source explicitly defines boot scripts, their file types, and usage)
- Confidence rationale: The source provides a clear, explicit definition of boot scripts
- Uncertainties: none — the full syntax specification is in the SASL `script` documentation
- Cross-reference status: verified against source text
