---
# === CORE IDENTIFICATION ===
concept: systools
slug: systools

# === CLASSIFICATION ===
category: tooling
subcategory: release-tooling
tier: intermediate

# === PROVENANCE ===
source: "Designing for Scalability with Erlang/OTP"
source_slug: design-scale-erlang-otp
authors: Francesco Cesarini & Steve Vinoski
chapter: "System Principles and Release Handling"
chapter_number: 10
pdf_page: 282
section: "Creating a Release"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - sys_tools
  - "systools:make_script"
  - "systools:make_tar"
  - "systools:make_relup"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - release-resource-file
extends: []
related:
  - boot-file
  - release-package
  - release-upgrade-file
  - rebar3
contrasts_with:
  - rebar3

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is systools?"
  - "How do I package, start, and configure a release?"
  - "How do I perform a release upgrade?"
---

# Quick Definition

`systools` is the Erlang library, shipped with the `sasl` application, used to build releases — generating boot files, release packages, and release upgrade files. It is the toolchain for integrating release creation into an existing build process.

# Core Definition

`systools` is an Erlang library used when integrating the creation of releases into an existing tool chain or build process (Cesarini & Vinoski, p. 283, pdf p. 282). It comes as part of the `sasl` application in the OTP distribution. Its three core functions are `make_script/2` (creates a binary boot file and its `.script` counterpart from a `.rel` file), `make_tar/2` (creates the release package tar file), and `make_relup/3,4` (creates the release upgrade `relup` file from `.rel` and `.appup` files). It also provides `script2boot/1` to convert a `.script` file into a `.boot` file.

# Prerequisites

- **Release resource file** — All `systools` functions take a release name pointing to a `.rel` file.

# Key Properties

1. Shipped as part of the `sasl` application in Erlang/OTP.
2. `make_script(Name, OptionsList)` -> generates `Name.script` and `Name.boot`; runs sanity checks.
3. `make_tar(Name, OptionsList)` -> generates `Name.tar.gz`, the release package.
4. `make_relup(RelName, UpFromList, DownToList, [Options])` -> generates the `relup` file.
5. `script2boot(File)` -> converts a `.script` file into a `.boot` file.
6. Common options: `{path, DirList}`, `{outdir, Dir}`, `src_tests`, `exref`, `silent`, `warnings_as_errors`.
7. The `silent` option returns `{ok, ..., Warnings}` / `{error, Module, Error}` instead of printing — used when scripting.

# Construction / Recognition

## To Use systools to Build a Release:
1. `systools:make_script("Name", [{path, ["App/ebin"]}])` to create the boot file.
2. `systools:make_tar("Name", [{erts, Dir}, {path, ...}, {outdir, Dir}])` to create the package.
3. For upgrades, `systools:make_relup("Name", UpFromList, DownToList, [Options])` to create the `relup`.

## To Recognize It:
1. Calls of the form `systools:make_*` in build scripts or shell sessions.

# Context & Application

- **Typical contexts**: Integrating release creation into an existing tool chain or build process.
- **Common applications**: Building boot files, tar packages, and `relup` files for non-greenfield projects.
- **Historical/stylistic notes**: For greenfield projects or complicated dependency management, `rebar3` is recommended instead; `rebar3` itself uses `relx` rather than `systools`/`reltool`.

# Examples

**Example 1** (p. 274): `systools:make_script("basestation", [{path, ["bsc/ebin"]}])` produces `basestation.script` and `basestation.boot`.

**Example 2** (p. 284): `systools:make_tar("basestation", [{erts, "/usr/local/lib/erlang/"}, {path, ["bsc/ebin"]}, {outdir, "ernie"}])` produces `basestation.tar.gz`.

**Example 3** (p. 339): Generating a `relup`:

```erlang
2> systools:make_relup("coffee-1.1", ["coffee-1.0"], ["coffee-1.0"],
     [{path, ["coffee*/ebin"]}]).
ok
```

# Relationships

## Enables
- **Boot file** — `make_script/2` generates it.
- **Release package** — `make_tar/2` generates it.
- **Release upgrade file** — `make_relup/3,4` generates it.

## Related
- **Release resource file** — All `systools` functions read `.rel` files.
- **Rebar3** — A higher-level tool that automates the same tasks.

## Contrasts With
- **Rebar3** — `systools` is the low-level OTP library for existing tool chains; `rebar3` is the recommended higher-level tool for greenfield projects (and uses `relx`, not `systools`).
- **Reltool** — Another OTP release tool, widely viewed as hard to configure correctly.

# Common Errors

- **Error**: Relying on `systools` printing results when calling it from a build script.
  **Correction**: Pass the `silent` option so the call returns a result tuple you can handle programmatically.

- **Error**: Assuming beam files are current when they may be stale.
  **Correction**: Pass `src_tests` so `systools` verifies beam files are newer than their sources and none are missing.

# Common Confusions

- **Confusion**: Thinking `systools` is a standalone command-line tool.
  **Clarification**: It is an Erlang library; its functions are called from the Erlang shell or from build code.

- **Confusion**: Believing `rebar3` uses `systools` internally.
  **Clarification**: `rebar3` uses `relx`, not `systools` or `reltool`, for release generation.

# Source Reference

Chapter 10: System Principles and Release Handling, sections "Creating a Release," "The make_script parameters," and "Creating a Release Package," pages 273-286 (pdf p. 282); and Chapter 11 "Release Upgrade Files," pages 339-341.

# Verification Notes

- Definition source: Direct adaptation of p. 283 and the function descriptions on pp. 274-286 and 339-341.
- Confidence rationale: HIGH — the source describes `systools` and its functions explicitly and at length.
- Uncertainties: None.
- Cross-reference status: Verified against planned cards.
- Re-extraction notes: Fresh extraction; no pre-existing card.
