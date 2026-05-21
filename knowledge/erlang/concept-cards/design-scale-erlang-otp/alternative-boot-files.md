---
# === CORE IDENTIFICATION ===
concept: Alternative Boot Files
slug: alternative-boot-files

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
section: "Alternative Boot Files"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - start_clean.boot
  - start_sasl.boot
  - no_dot_erlang.boot
  - start.boot

# === TYPED RELATIONSHIPS ===
prerequisites:
  - boot-file
extends: []
related:
  - boot-script-file
  - release-resource-file
  - system-boot-process
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What are the standard alternative boot files in an Erlang installation?"
  - "How do I package, start, and configure a release?"
---

# Quick Definition

Alternative boot files are the standard boot files shipped in the Erlang/OTP `releases` directory — `start_clean.boot`, `start_sasl.boot`, and `no_dot_erlang.boot` — each starting a different set of applications. `start.boot` is a copy of whichever was selected as the default.

# Core Definition

In the `releases` directory of a standard Erlang/OTP distribution you will find four boot files and three rel files that start and load different applications (Cesarini & Vinoski, p. 278, pdf p. 282): `start_clean.boot` starts the `kernel` and `stdlib` applications as defined in `start_clean.rel`; `start_sasl.boot` starts `kernel`, `stdlib`, and `sasl` as defined in `start_sasl.rel`; `no_dot_erlang.boot` starts `kernel` and `stdlib` but does not execute commands in the `.erlang` file, which is useful when determinism is important; and `start.boot` is a copy of whichever of the preceding files was selected as the default when Erlang was installed.

# Prerequisites

- **Boot file** — Alternative boot files are specific boot files; the boot-file concept comes first.

# Key Properties

1. Four standard boot files: `start_clean.boot`, `start_sasl.boot`, `no_dot_erlang.boot`, `start.boot`.
2. `start_clean.boot` -> `kernel` + `stdlib`.
3. `start_sasl.boot` -> `kernel` + `stdlib` + `sasl`.
4. `no_dot_erlang.boot` -> `kernel` + `stdlib`, skipping the `.erlang` file (deterministic startup).
5. `start.boot` -> a copy of whichever of the three was made the default at install time.
6. Any of the three named files can be renamed to `start.boot` to change the default.
7. Three corresponding `.rel` files exist (`start_clean.rel`, `start_sasl.rel`, `no_dot_erlang.rel`).

# Construction / Recognition

## To Use an Alternative Boot File:
1. Inspect the `releases` directory of the standard Erlang/OTP distribution.
2. Rename the desired file (e.g. `start_sasl.boot`) to `start.boot` to make it the default.
3. Or pass it explicitly with the `-boot` flag to `erl`.

## To Recognize Them:
1. Look in the `releases` directory for `start_clean.boot`, `start_sasl.boot`, `no_dot_erlang.boot`, and `start.boot`.

# Context & Application

- **Typical contexts**: Choosing how an Erlang installation starts up.
- **Common applications**: Using `start_sasl.boot` so SASL logs are available; using `no_dot_erlang.boot` when determinism matters and code-path manipulation must be prevented.
- **Historical/stylistic notes**: It is recommended to always generate a second boot file similar to `start_sasl.boot` for your target system, so SASL crash/error logs are viewable locally when the main node refuses to start.

# Examples

**Example 1** (p. 278): `start_sasl.boot` starts `kernel`, `stdlib`, and `sasl` as defined in `start_sasl.rel`.

**Example 2** (p. 278): `no_dot_erlang.boot` is useful when determinism is important because it does not allow the code search paths to be manipulated or other user preferences to be modified via the `.erlang` file.

# Relationships

## Builds Upon
- **Boot file** — Alternative boot files are concrete instances of the boot-file concept.

## Related
- **Boot script file** — Each alternative boot file has a textual `.script` counterpart.
- **Release resource file** — Each is generated from a corresponding `.rel` file.
- **System boot process** — The chosen boot file drives the startup sequence.

# Common Errors

- **Error**: Shipping a target system with no `start_sasl`-equivalent boot file.
  **Correction**: Always generate a second boot file that starts `kernel`, `stdlib`, and `sasl` so SASL logs are accessible when the main node will not start.

- **Error**: Expecting `start.boot` to always start the same applications.
  **Correction**: `start.boot` is just a copy of whichever file was chosen as default at install time; check which one.

# Common Confusions

- **Confusion**: Thinking `start.boot` is its own distinct boot file.
  **Clarification**: It is a copy of one of `start_clean.boot`, `start_sasl.boot`, or `no_dot_erlang.boot`.

- **Confusion**: Believing `no_dot_erlang.boot` differs in which applications it starts.
  **Clarification**: It starts the same `kernel` and `stdlib` as `start_clean.boot`; the difference is that it skips the `.erlang` file.

# Source Reference

Chapter 10: System Principles and Release Handling, section "Alternative Boot Files," page 278 (pdf p. 282).

# Verification Notes

- Definition source: Direct adaptation of p. 278.
- Confidence rationale: HIGH — the source explicitly lists and describes the standard boot files.
- Uncertainties: None.
- Cross-reference status: Verified against planned cards.
- Re-extraction notes: Fresh extraction; no pre-existing card.
