---
# === CORE IDENTIFICATION ===
concept: Erlang/OTP File Types
slug: erlang-otp-file-types

# === CLASSIFICATION ===
category: applications-releases
subcategory: release-files
tier: foundational

# === PROVENANCE ===
source: "Designing for Scalability with Erlang/OTP"
source_slug: design-scale-erlang-otp
authors: Francesco Cesarini & Steve Vinoski
chapter: "System Principles and Release Handling"
chapter_number: 10
pdf_page: 282
section: "Wrapping Up"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - OTP file extensions
  - release file types

# === TYPED RELATIONSHIPS ===
prerequisites: []
extends: []
related:
  - release-resource-file
  - boot-file
  - boot-script-file
  - application-upgrade-file
  - release-upgrade-file
  - system-configuration-file
  - application-resource-file
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What are the Erlang/OTP file types involved in a release?"
  - "How do I package, start, and configure a release?"
---

# Quick Definition

The Erlang/OTP file types are the distinct file kinds — by extension — that together make up a release: source and compiled modules, application/release resource files, upgrade files, boot scripts, and configuration files.

# Core Definition

The source consolidates the many file types it has introduced, all held together in a release, into Table 11-1 (Cesarini & Vinoski, p. 311, pdf p. 282). The nine file types are: Erlang module (`.erl`), compiled module (`.beam`), application resource file (`.app`), application upgrade file (`.appup`), release file (`.rel`), release upgrade file (`relup`), start script (`.script`), binary start script (`.boot`), and configuration file (`.config`).

# Prerequisites

This is a foundational, consolidating concept with no prerequisites within this source — it summarizes file types defined throughout the release and upgrade chapters.

# Key Properties

1. `.erl` — Erlang module: file containing Erlang source code.
2. `.beam` — compiled module: compiled source for the BEAM emulator.
3. `.app` — application resource file: application resource and configuration data.
4. `.appup` — application upgrade file: application upgrade data.
5. `.rel` — release file: release-specific application and emulator versions.
6. `relup` — release upgrade file: release upgrade information.
7. `.script` — start script: text-based version of the boot script.
8. `.boot` — binary start script: binary version of the boot script.
9. `.config` — configuration file: application-specific environment variables.
10. `.appup` and `relup` files are used for live upgrades of applications and the emulator.

# Construction / Recognition

## To Recognize the File Types:
1. Match the file extension against the nine types in Table 11-1.
2. `.appup` and `relup` have no leading dot in the table but are still suffix-based.

## To Use Them in a Release:
1. Compile `.erl` -> `.beam`.
2. Describe applications with `.app`, the release with `.rel`.
3. Generate `.script`/`.boot` boot files.
4. For upgrades, write `.appup` files and generate the `relup`.
5. Configure with a `.config` file (`sys.config`).

# Context & Application

- **Typical contexts**: Understanding the artifacts that make up an Erlang release and its upgrades.
- **Common applications**: Navigating a release directory; knowing which file to edit or generate at each step.
- **Historical/stylistic notes**: The book presents the table as a review point at the end of the release chapter, noting `.appup` and `relup` are covered in the upgrades chapter.

# Examples

**Example 1** (p. 311, Table 11-1): The release file `.rel` "contains release-specific application and emulator versions"; the binary start script `.boot` is the "binary version of the script used to boot the system."

**Example 2** (p. 311): `.appup` and `relup` files "are used for live upgrades of the applications and regular upgrades of the emulator."

# Relationships

## Related
- **Release resource file** — The `.rel` file type.
- **Boot file** — The `.boot` file type.
- **Boot script file** — The `.script` file type.
- **Application upgrade file** — The `.appup` file type.
- **Release upgrade file** — The `relup` file type.
- **System configuration file** — The `.config` file type (`sys.config`).
- **Application resource file** — The `.app` file type.

# Common Errors

- **Error**: Editing a `.beam` file directly.
  **Correction**: `.beam` is compiled output; edit the `.erl` source and recompile.

- **Error**: Confusing the `.script` and `.boot` files.
  **Correction**: `.script` is the editable text form; `.boot` is the binary form the runtime actually boots from.

# Common Confusions

- **Confusion**: Thinking `.appup` and `relup` are the same file type.
  **Clarification**: `.appup` holds per-application upgrade data; `relup` holds the generated per-release upgrade information.

- **Confusion**: Believing `.app` and `.config` serve the same role.
  **Clarification**: `.app` is the application resource file; `.config` holds deployment-specific environment-variable overrides.

# Source Reference

Chapter 10: System Principles and Release Handling, section "Wrapping Up," Table 11-1 "Erlang/OTP file types," page 311 (pdf p. 282).

# Verification Notes

- Definition source: Direct adaptation of Table 11-1, p. 311.
- Confidence rationale: HIGH — the source presents an explicit, complete table of the file types.
- Uncertainties: None.
- Cross-reference status: Verified against planned cards; `application-resource-file` is an other-chapter planned slug.
- Re-extraction notes: Fresh extraction; no pre-existing card.
