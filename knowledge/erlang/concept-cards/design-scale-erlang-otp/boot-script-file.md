---
# === CORE IDENTIFICATION ===
concept: Boot Script File
slug: boot-script-file

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
section: "Script files"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - ".script file"
  - start script (textual)
  - script file

# === TYPED RELATIONSHIPS ===
prerequisites:
  - boot-file
extends: []
related:
  - system-boot-process
  - release-resource-file
  - code-loading-and-code-paths
  - init-module
contrasts_with:
  - boot-file

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is a boot script file?"
  - "How do I package, start, and configure a release?"
---

# Quick Definition

A boot script file (`.script`) is the human-readable textual representation of a boot file, holding an Erlang term that lists every command the runtime executes to start a release. It can be inspected, edited, or hand-written, then compiled into a `.boot` file.

# Core Definition

The boot script file is a text file containing an Erlang term of the format `{script, {ReleaseName, ReleaseVsn}, Actions}` (Cesarini & Vinoski, p. 276, pdf p. 282). It holds the textual representation of the boot file's commands; the `.boot` file is its binary counterpart. The file can be edited or written by hand, and a `.boot` file can be regenerated from it using `systools:script2boot/1` (p. 278).

# Prerequisites

- **Boot file** — The `.script` file is the textual form of the `.boot` file; understanding the boot file's role comes first.

# Key Properties

1. Has the `.script` extension and is a plain-text file.
2. Holds one Erlang term: `{script, {ReleaseName, ReleaseVsn}, Actions}`.
3. Editable and hand-writable, unlike the binary `.boot` file.
4. Action commands include `preLoaded`, `progress`, `kernel_load_completed`, `path`, `primLoad`, `{kernelProcess, Name, {M,F,A}}`, and `{apply, {M,F,A}}`.
5. `primLoad` loads modules via `erl_prim_loader:get_file/1`; failure terminates the start script.
6. `{apply, {M,F,A}}` functions must return — startup is synchronous.
7. Convertible to a `.boot` file with `systools:script2boot/1`.

# Construction / Recognition

## To Obtain a Script File:
1. Run `systools:make_script/2`, which produces both `Name.script` and `Name.boot`.
2. Optionally edit `Name.script` directly to change load order or add progress reports.
3. Regenerate the `.boot` file with `systools:script2boot/1`.

## To Recognize It:
1. Look for a file with the `.script` suffix.
2. Confirm it contains a `{script, {Name, Vsn}, Actions}` term.

# Context & Application

- **Typical contexts**: Inspecting startup behavior; debugging why a node will not start; reducing startup time.
- **Common applications**: Adding progress reports after `primLoad` commands to locate corrupted beam files; loading only specific modules or changing application start order.
- **Historical/stylistic notes**: Hand-editing scripts to add progress reports was a necessity for debugging startup issues; today the `-init_debug` flag makes startup phases visible.

# Examples

**Example 1** (p. 276): A `basestation.script` excerpt:

```erlang
{script,
 {"basestation","1.0"},
 [{preLoaded,
   [erl_prim_loader,erlang,erts_internal,init,otp_ring0,prim_eval,
    prim_file,prim_inet,prim_zip,zlib]},
  {progress,preloaded},
  {path,["$ROOT/lib/kernel-4.1.1/ebin","$ROOT/lib/stdlib-2.7/ebin"]},
  {primLoad,[error_handler]},
  {kernel_load_completed},
  ...
  {apply,{application,start_boot,[bsc,permanent]}},
  {apply,{c,erlangrc,[]}},
  {progress,started}]}.
```

**Example 2** (p. 277): The script calls `application:start_boot/2` (an undocumented function that assumes the application is already loaded) rather than `application:start/1`.

# Relationships

## Builds Upon
- **Boot file** — The `.script` is the editable text form of the binary `.boot`.

## Enables
- **System boot process** — Its action list drives node startup.

## Related
- **Release resource file** — `make_script/2` reads the `.rel` file to generate the `.script`.
- **Code loading and code paths** — `path` and `primLoad` actions populate the code path and load modules.
- **Init module** — Interprets the script's actions at startup.

## Contrasts With
- **Boot file** — The `.boot` is binary and not editable; the `.script` is text and editable.

# Common Errors

- **Error**: Editing the `.script` and forgetting to regenerate the `.boot`.
  **Correction**: Convert the edited `.script` with `systools:script2boot/1`; the runtime boots from the binary `.boot`.

- **Error**: Adding an `{apply, {M,F,A}}` action whose function does not return.
  **Correction**: Startup is synchronous; a non-returning apply prevents the next command from executing.

# Common Confusions

- **Confusion**: Thinking the `.script` file is the file the runtime actually boots from.
  **Clarification**: The runtime boots from the binary `.boot` file; the `.script` is its readable, editable representation.

- **Confusion**: Believing every progress state matters to startup.
  **Clarification**: Only the final `{progress, started}` changes the internal state to `started`; other progress states are for debugging.

# Source Reference

Chapter 10: System Principles and Release Handling, section "Script files," pages 276-279 (pdf p. 282). See Figure 11-4 "Creating boot and release files."

# Verification Notes

- Definition source: Direct adaptation of pp. 276-279.
- Confidence rationale: HIGH — the source explicitly defines the script file's format and contents.
- Uncertainties: None.
- Cross-reference status: Verified against planned cards.
- Re-extraction notes: Fresh extraction; no pre-existing card.
