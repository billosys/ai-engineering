---
# === CORE IDENTIFICATION ===
concept: Default Boot Scripts
slug: default-boot-scripts

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
section: "Default Boot Scripts"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - standard boot scripts
  - shipped boot scripts

# === TYPED RELATIONSHIPS ===
prerequisites:
  - boot-script
  - erl-command
extends:
  - boot-script
related:
  - user-defined-boot-script
  - erlang-runtime-system
contrasts_with:
  - user-defined-boot-script

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What distinguishes start_clean.boot from start_sasl.boot?"
  - "What is a boot script in Erlang/OTP?"
  - "What default boot scripts ship with Erlang/OTP?"
---

# Quick Definition

Erlang/OTP ships with three default boot scripts: `start_clean.boot` (Kernel + STDLIB), `start_sasl.boot` (Kernel + STDLIB + SASL), and `no_dot_erlang.boot` (Kernel + STDLIB, skipping `.erlang` file loading).

# Core Definition

Erlang/OTP comes with three pre-built boot scripts:

1. **`start_clean.boot`** — Loads the code for and starts the applications Kernel and STDLIB.
2. **`start_sasl.boot`** — Loads the code for and starts the applications Kernel, STDLIB, and SASL.
3. **`no_dot_erlang.boot`** — Loads the code for and starts the applications Kernel and STDLIB. Skips loading the file `.erlang`. Useful for scripts and other tools that are to behave the same irrespective of user preferences.

During Erlang/OTP installation using `Install`, the user is asked whether to use a minimal system startup (start_clean) or the SASL startup (start_sasl). The chosen boot script is copied and renamed as `start.boot` and placed into the directory `ROOT/bin`, becoming the default when no `-boot` flag is specified.

Source: "Default Boot Scripts" section of OTP System Principles documentation (Ericsson AB).

# Prerequisites

- **boot-script** — default boot scripts are specific instances of boot scripts
- **erl-command** — default boot scripts are selected via the `-boot` flag or used implicitly

# Key Properties

1. `start_clean.boot` starts only Kernel and STDLIB (minimal startup)
2. `start_sasl.boot` starts Kernel, STDLIB, and SASL (includes release handling and error logging)
3. `no_dot_erlang.boot` is like `start_clean` but skips the `.erlang` file
4. The default is chosen at installation time and copied to `ROOT/bin/start.boot`
5. If no `-boot` flag is given, `ROOT/bin/start.boot` is used
6. The installation choice is made by answering the `Install` prompt about minimal vs SASL startup

# Construction / Recognition

## To Construct/Create:
1. Default boot scripts are pre-built and ship with Erlang/OTP — no construction needed
2. The default (`start.boot`) is configured during installation

## To Identify/Recognize:
1. Look for `start_clean.boot`, `start_sasl.boot`, or `no_dot_erlang.boot` in the Erlang/OTP installation
2. Check `ROOT/bin/start.boot` to see which default is configured (it is a copy of either `start_clean` or `start_sasl`)

# Context & Application

The choice between `start_clean` and `start_sasl` as the default affects what is available at system startup. `start_sasl` includes the SASL application, which provides release handling, error reporting (via SASL error logger), and other operational tools. For production systems that use OTP releases, `start_sasl` is typically preferred. For development and scripting, `start_clean` or `no_dot_erlang` suffice. The `no_dot_erlang` script is specifically designed for escript-based tools and scripts where reproducible behavior is required regardless of per-user `.erlang` configuration.

# Examples

**Example 1** (System Principles section): The three default boot scripts and what they start:

- `start_clean.boot` — Loads and starts Kernel + STDLIB
- `start_sasl.boot` — Loads and starts Kernel + STDLIB + SASL
- `no_dot_erlang.boot` — Loads and starts Kernel + STDLIB, skips `.erlang`

**Example 2** (System Principles section): The installation prompt that determines the default:

```text
Do you want to use a minimal system startup instead of the SASL startup?
```

If the answer is yes, `start_clean` is used; otherwise `start_sasl` is used. The chosen script is copied and renamed as `start.boot` in `ROOT/bin`.

# Relationships

## Builds Upon
- **boot-script** — default boot scripts are concrete instances of the boot script concept

## Enables
- **erlang-runtime-system** — default boot scripts enable the runtime system to start with a standard configuration without requiring custom scripts

## Related
- **user-defined-boot-script** — users create custom boot scripts when the defaults are insufficient

## Contrasts With
- **user-defined-boot-script** — default boot scripts are pre-built and limited to standard applications; user-defined boot scripts are generated from `.rel` files and can include any set of applications

# Common Errors

- **Error**: Assuming SASL is always available at startup.
  **Correction**: SASL is only available if `start_sasl` is the default or if `-boot start_sasl` is explicitly specified. Check which default was configured during installation.

- **Error**: Using `start_clean` or `start_sasl` for scripting tools that should be user-independent.
  **Correction**: Use `no_dot_erlang` for scripts and tools that must behave consistently regardless of user `.erlang` files.

# Common Confusions

- **Confusion**: `start_clean` means "no applications are started."
  **Clarification**: `start_clean` still starts Kernel and STDLIB — it is "clean" of SASL, not of all applications. Kernel and STDLIB are always required.

- **Confusion**: `start.boot` is a distinct fourth boot script.
  **Clarification**: `start.boot` is a copy of either `start_clean.boot` or `start_sasl.boot`, renamed during installation. It is the system default, not a separate script.

# Source Reference

"Default Boot Scripts" subsection of "Boot Scripts" section, "System Principles" chapter, OTP System Principles documentation.

# Verification Notes

- Definition source: direct (source explicitly lists and describes all three default boot scripts)
- Confidence rationale: The source provides complete, explicit descriptions of each default boot script
- Uncertainties: none
- Cross-reference status: verified against source text
