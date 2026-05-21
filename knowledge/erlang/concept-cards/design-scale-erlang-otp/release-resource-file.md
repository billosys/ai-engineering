---
# === CORE IDENTIFICATION ===
concept: Release Resource File
slug: release-resource-file

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
section: "Release Resource Files"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - rel file
  - ".rel file"
  - release specification

# === TYPED RELATIONSHIPS ===
prerequisites:
  - release
  - otp-application
extends: []
related:
  - boot-file
  - release-and-application-versions
  - erlang-runtime-system
  - release-upgrade-file
  - erlang-otp-file-types
contrasts_with:
  - application-resource-file
  - release-upgrade-file

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is a release resource file?"
  - "How do I package, start, and configure a release?"
  - "How does a release relate to the applications it bundles?"
---

# Quick Definition

A release resource file (`.rel`) is the specification listing the versions of every application and the runtime system that make up a release. The build system uses it to run sanity checks and generate the boot files and target directory structure.

# Core Definition

The release resource file bundles all of a project's OTP applications — standard-distribution, proprietary, and open source alike — into a release specification containing their versions, the system release version and name, and the version of the runtime system (Cesarini & Vinoski, p. 288-290, pdf p. 282). By convention it is named `ReleaseName.rel`. It contains a single Erlang term: a tuple of four elements — the `release` atom, a `{ReleaseName, RelVersion}` tuple, an `{erts, ErtsVersion}` tuple, and a list of application tuples. The build system uses this information to do sanity checks, create the boot files, and create the target directory structure.

# Prerequisites

- **Release** — The `.rel` file defines what a release contains; you must understand the release concept first.
- **OTP application** — The file lists applications and their versions, so the application concept is required.

# Key Properties

1. By convention named `ReleaseName.rel` (convention is not mandatory but eases maintenance).
2. Contains exactly one four-element tuple: `release` atom, `{ReleaseName, RelVersion}`, `{erts, ErtsVersion}`, and a list of application tuples.
3. All version fields are strings.
4. The minimal (and default) release consists of just `kernel` and `stdlib`; most releases also include `sasl`.
5. Application tuples can take four forms: `{App, Vsn}`, `{App, Vsn, Type}`, `{App, Vsn, IncludedAppList}`, `{App, Vsn, Type, IncludedAppList}`.
6. Application `Type` can be `permanent`, `transient`, `temporary`, `load`, or `none`.
7. An `IncludedAppList` must be a subset of the included applications declared in the application's app file.

# Construction / Recognition

## To Create a Release Resource File:
1. Name the file `ReleaseName.rel`.
2. Write the `release` atom followed by `{ReleaseName, RelVersion}` (both strings).
3. Add `{erts, ErtsVersion}` for the runtime system version.
4. List each application as a tuple `{Application, AppVersion}` (optionally with `Type` and `IncludedAppList`).
5. Include at minimum `kernel` and `stdlib`; add `sasl` to enable upgrades.

## To Recognize One:
1. Look for a file with a `.rel` suffix in the `releases` directory.
2. Confirm it holds a single `{release, ...}` tuple.

# Context & Application

- **Typical contexts**: Defining the contents of a release before building boot files and the target structure.
- **Common applications**: Generating boot files via `systools:make_script/2`; generating release upgrade (`relup`) files via `systools:make_relup/3,4`.
- **Historical/stylistic notes**: The `os_mon`, `runtime_tools` (with `dbg`), and logging applications are recommended additions for production troubleshooting.

# Examples

**Example 1** (p. 288): The standard `releases/18/start_sasl.rel` file:

```erlang
{release, {"Erlang/OTP","18"}, {erts, "7.2"},
 [{kernel,"4.1.1"},
  {stdlib,"2.7"},
  {sasl, "2.6.1"}]}.
```

**Example 2** (p. 289): The base station controller release file `basestation.rel`:

```erlang
{release,
 {"basestation","1.0"},
 {erts, "7.2"},
 [{kernel, "4.1.1"},
  {stdlib, "2.7"},
  {sasl, "2.6.1"},
  {bsc, "1.0"}]}.
```

**Example 3** (p. 290): The general form of the application-tuple options:

```erlang
{release,
 {ReleaseName, RelVersion},
 {erts, ErtsVersion},
 [{Application, AppVersion},
  {Application, AppVersion, Type},
  {Application, AppVersion, IncludedAppList},
  {Application, AppVersion, Type, IncludedAppList}]
}.
```

# Relationships

## Builds Upon
- **Release** — The `.rel` file is the formal specification of a release's contents.

## Enables
- **Boot file** — Generated from the `.rel` file by `systools:make_script/2`.
- **Release upgrade file** — The new and old `.rel` files are inputs to `systools:make_relup/3,4`.

## Related
- **Release and application versions** — All versions are strings; the `.rel` ties them together.
- **Erlang runtime system** — The `{erts, Vsn}` tuple names the emulator version.

## Contrasts With
- **Application resource file** — The `.app` file describes a single application; the `.rel` file describes the whole release.
- **Release upgrade file** — The `relup` describes how to move between releases; the `.rel` describes one release's static contents.

# Common Errors

- **Error**: Omitting `sasl` from the `.rel` file when upgrades will later be needed.
  **Correction**: Include `sasl`, since it contains all the tools required for software upgrades; warnings (but not failures) are raised when it is absent.

- **Error**: Listing an application version in the `.rel` that does not match the version in the app file.
  **Correction**: Keep `.rel` and `.app` versions consistent — boot-file generation sanity checks fail otherwise.

# Common Confusions

- **Confusion**: Thinking the `IncludedAppList` can name any application.
  **Clarification**: It must be a subset of the applications declared as included in the application's own app file.

- **Confusion**: Believing the naming convention `ReleaseName.rel` is mandatory.
  **Clarification**: It is conventional, not mandatory, but following it makes life easier for maintainers.

# Source Reference

Chapter 10: System Principles and Release Handling, section "Release Resource Files," pages 288-291 (pdf p. 282). Includes the "What Applications Do You Include in a Standard Release?" subsection.

# Verification Notes

- Definition source: Direct adaptation of pp. 288-290.
- Confidence rationale: HIGH — the source explicitly defines the file, its naming convention, structure, and tuple forms.
- Uncertainties: None.
- Cross-reference status: Verified against planned cards.
- Re-extraction notes: Fresh extraction; no pre-existing card.
