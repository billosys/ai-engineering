---
# === CORE IDENTIFICATION ===
concept: Application Structure
slug: application-structure

# === CLASSIFICATION ===
category: applications-releases
subcategory: applications
tier: intermediate

# === PROVENANCE ===
source: "Designing for Scalability with Erlang/OTP"
source_slug: design-scale-erlang-otp
authors: "Francesco Cesarini & Steve Vinoski"
chapter: "Applications"
chapter_number: 8
pdf_page: 222
section: "The Application Structure"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "application directory structure"
  - "application directory layout"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - otp-application
extends: []
related:
  - application-resource-file
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do I structure an OTP application?"
  - "What is an OTP application?"
---

# Quick Definition

The application structure is the standard directory layout an OTP application follows — a directory named `<name>-<version>` containing the `ebin`, `src`, `priv`, and `include` subdirectories — which tools and release mechanisms depend on.

# Core Definition

Applications are packaged in a directory that follows a special structure and naming convention; tools and release-handling mechanisms depend on this structure (Cesarini & Vinoski, p. 206). The application directory is named after the application followed by its version number, allowing different versions to coexist. Its standard subdirectories are: `ebin` (beam files and the `.app` configuration file), `src` (Erlang source and private include files), `priv` (non-Erlang resources — drivers, scripts, graphics, config), and `include` (exported `.hrl` files usable by other applications). The runtime and tools can reference these standard directories by application name without the version number (pp. 206-208).

# Prerequisites

- **OTP application** — The application structure is the on-disk layout of an OTP application.

# Key Properties

1. The directory is named `<application-name>-<version>`.
2. `ebin` — beam files plus the `.app` (and possibly `.appup`) file.
3. `src` — Erlang source code and non-exported `.hrl` files.
4. `priv` — non-Erlang resources (drivers, NIFs, scripts, graphics, config).
5. `include` — exported `.hrl` files for use by other applications.
6. Standard directories are reachable by application name without the version; nonstandard ones (`doc`, `test`, `examples`) are not.
7. `ebin` and `priv` are usually the only directories shipped to target machines.

# Construction / Recognition

## To Construct/Create:
1. Create a directory named `<name>-<version>`.
2. Add `ebin`, `src`, `priv`, and `include` subdirectories.
3. Place beam files and the `.app` file in `ebin`; source in `src`; resources in `priv`; exported headers in `include`.

## To Identify/Recognize:
1. A `<name>-<version>` directory.
2. The presence of `ebin`, `src`, `priv`, `include` subdirectories.

# Context & Application

- **Typical contexts**: Every OTP application on disk, including those in the Erlang `lib` directory.
- **Common applications**: Locating resources via `code:lib_dir/0`, `code:priv_dir/1`; `-include_lib("App/include/File.hrl")`.
- **Historical/stylistic notes**: The book walks through the `runtime_tools` application in the Erlang `lib` directory as a concrete example (p. 207).

# Examples

**Example 1** (p. 207): `runtime_tools-1.8.10` in the Erlang `lib` directory contains `ebin`, `include`, `priv`, `src` (standard) plus `doc`, `examples`, `info` (nonstandard).

**Example 2** (p. 207): `-include_lib("Application/include/File.hrl")` resolves an exported header without knowing the version.

## Worked Example

Listing an application directory (p. 207):

```text
$ cd runtime_tools-1.8.10/
$ ls
doc       examples  info  src
ebin      include   priv
```

# Relationships

## Builds Upon
- *(none)*

## Enables
- *(none)*

## Related
- **Application resource file** — The `.app` file lives in the `ebin` directory.

## Contrasts With
- *(none)*

# Common Errors

- **Error**: Placing the `.app` resource file in `src` instead of `ebin`.
  **Correction**: The `.app` file belongs in `ebin`, which is one of the directories shipped to target machines.

- **Error**: Relying on nonstandard directories (`doc`, `test`) being present across releases.
  **Correction**: No guarantees exist that nonstandard directories survive between releases; only standard ones are tool-resolvable.

# Common Confusions

- **Confusion**: Thinking the version number must be referenced explicitly to access an application's directories.
  **Clarification**: Standard directories (`ebin`, `priv`, `include`) are reachable by application name; the runtime resolves the version automatically.

# Source Reference

Chapter 8: Applications, "The Application Structure," pages 206-208. See Figure 9-3 (Application structure).

# Verification Notes

- Definition source: Direct adaptation from pp. 206-208.
- Confidence rationale: HIGH — explicitly defined with a directory listing and per-directory descriptions.
- Uncertainties: None.
- Cross-reference status: Verified against planned card slugs for this source.
- Re-extraction notes: Fresh extraction — no pre-existing card for this source.
</content>
