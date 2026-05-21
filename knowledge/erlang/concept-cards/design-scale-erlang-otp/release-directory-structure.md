---
# === CORE IDENTIFICATION ===
concept: Release Directory Structure
slug: release-directory-structure

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
  - Erlang root directory layout
  - release file structure

# === TYPED RELATIONSHIPS ===
prerequisites:
  - release
extends: []
related:
  - erlang-runtime-system
  - release-resource-file
  - boot-file
  - code-loading-and-code-paths
  - releases-file
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is the release directory structure?"
  - "How do I package, start, and configure a release?"
---

# Quick Definition

The release directory structure is the on-disk layout shared by every OTP release, organized around four mandatory directories: `lib`, `erts`, `releases`, and `bin`. Your own releases use the same structure as the Erlang root directory.

# Core Definition

Every OTP release has the same directory and file structure as the Erlang root directory (the location where Erlang is installed); the only differences between the root and your own releases are the applications loaded and started, their versions, and the runtime system version (Cesarini & Vinoski, p. 284-286, pdf p. 282). Four directories are mandatory in every OTP release: `lib` (all applications, with version numbers appended to directory names), `erts` (binaries for the Erlang runtime system, with the erts version appended), `releases` (a subdirectory per installed release, plus `RELEASES`, `start_erl.data`, and the `.rel`/`.script`/`.boot` files), and `bin`.

# Prerequisites

- **Release** — The directory structure is the physical form of a release; you must understand what a release is first.

# Key Properties

1. Four mandatory directories: `lib`, `erts`, `releases`, `bin`.
2. `lib` contains application directories named `AppName-Version`; after upgrades, multiple versions of one application can coexist.
3. `erts` contains the runtime-system binaries; its `bin` subdirectory holds executables (`erl`, `erlexec`, `erlc`, `epmd`, `escript`, `start`, `run_erl`, `to_erl`, `werl`, `start_erl`, `erlsrv`, `heart`, `dialyzer`, `typer`).
4. `releases` has one subdirectory per installed release, plus `RELEASES`, `RELEASES.src`, and `start_erl.data`.
5. There is normally a one-to-one mapping between `erts` directories and `releases` subdirectories.
6. The code search path created at release time usually points to the `ebin` directory of the latest version of each application.
7. The `releases` directory location can be overridden via the `sasl` config variable `releases_dir` or the OS environment variable `RELDIR`; the runtime needs write permission there for upgrades.

# Construction / Recognition

## To Create the Structure:
1. Create a target directory and add `releases` and `lib` to it.
2. Populate `lib` with the application versions specified in the `.rel` file.
3. Create the release version directory under `releases` with boot scripts and `sys.config`.
4. Copy the `erts` executable and binaries to the target directory (if shipping the runtime).
5. Create a `bin` directory and copy configuration files and start scripts to it.

## To Recognize It:
1. Find the Erlang root directory by calling `code:root_dir()` in the shell.
2. Confirm `lib`, `erts`, `releases`, and `bin` are present.

# Context & Application

- **Typical contexts**: Building a target release; inspecting an existing Erlang installation.
- **Common applications**: Manual release packaging; understanding why `systools:make_tar/2` lays out files the way it does.
- **Historical/stylistic notes**: Multiple `erts-*` and `lib/App-*` directory instances accumulate as a system is upgraded over the years.

# Examples

**Example 1** (p. 284): Listing the Erlang root directory after several upgrades:

```
$ cd /usr/local/lib/erlang
$ ls
Install   erts-6.4  erts-7.1  misc
bin       erts-6.3  erts-7.2  releases
erts-6.2  erts-7.0  lib       usr
```

**Example 2** (p. 287): The `releases` directory and a `start_erl.data` file:

```
$ cd releases
$ ls
17  18  RELEASES  RELEASES.src  start_erl.data
$ cat start_erl.data
7.2 18
```

**Example 3** (p. 285): Finding the root directory from the shell:

```erlang
1> code:root_dir().
"/usr/local/lib/erlang"
```

# Relationships

## Builds Upon
- **Release** — The directory structure is the physical layout of a release.

## Related
- **Erlang runtime system** — The `erts` directory holds the runtime binaries.
- **Release resource file** — `.rel` files live under `releases`.
- **Boot file** — `.boot`/`.script` files live under `releases`.
- **RELEASES file** — Lives in `releases` and tracks installed releases for upgrades.
- **Code loading and code paths** — The search path points into `lib/App-Vsn/ebin`.

# Common Errors

- **Error**: Placing application beam files in `App/ebin` instead of `$ROOT/lib/App-Vsn/ebin`.
  **Correction**: The generated boot scripts assume the standard `$ROOT/lib/AppName-Version/ebin` layout; follow it or fix the code path explicitly.

- **Error**: Pointing `releases_dir`/`RELDIR` at a directory the runtime cannot write.
  **Correction**: Ensure the runtime has write permission, because upgrades update the `RELEASES` file there.

# Common Confusions

- **Confusion**: Believing your releases differ structurally from the Erlang installation.
  **Clarification**: They are structurally identical; only the applications, versions, and runtime version differ.

- **Confusion**: Thinking only one version of an application or `erts` can exist on disk.
  **Clarification**: After upgrades, multiple versions coexist, distinguished by the version number in the directory name.

# Source Reference

Chapter 10: System Principles and Release Handling, section "Release Directory Structure," pages 284-287 (pdf p. 282). See Figure 11-1 "Release directory structure."

# Verification Notes

- Definition source: Direct adaptation of pp. 284-287.
- Confidence rationale: HIGH — the source explicitly enumerates the four mandatory directories and their contents.
- Uncertainties: None.
- Cross-reference status: Verified against planned cards.
- Re-extraction notes: Fresh extraction; no pre-existing card.
