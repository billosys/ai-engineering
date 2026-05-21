---
# === CORE IDENTIFICATION ===
concept: System Configuration Parameters
slug: system-configuration-parameters

# === CLASSIFICATION ===
category: applications-releases
subcategory: configuration
tier: intermediate

# === PROVENANCE ===
source: "OTP System Principles"
source_slug: otp-system-principles
authors: "Ericsson AB"
chapter: "Creating and Upgrading a Target System"
chapter_number: null
pdf_page: null
section: "System Configuration Parameters"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "sys.config"
  - "sys.config.src"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - target-system
extends: []
related:
  - embedded-target-system
  - start-erl
  - target-system-creation
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do I configure system parameters with sys.config?"
  - "What is the difference between sys.config and sys.config.src?"
---

# Quick Definition

System configuration parameters are defined in a `sys.config` file located in the release version directory, which `start_erl` requires to boot an embedded target system. A `sys.config.src` variant allows variable substitution before deployment.

# Core Definition

As described in OTP System Principles: "`start_erl` requires a `sys.config` in the release version directory (`releases/FIRST/sys.config`). If there is no such file, the system start fails." The `sys.config` file contains Erlang terms defining application environment parameters. A `sys.config.src` alternative is also supported for cases requiring variable substitution on the target.

# Prerequisites

- Understanding of Erlang/OTP applications and their environment parameters.
- A target system created and installed.

# Key Properties

1. Located in the release version directory (e.g., `releases/FIRST/sys.config`).
2. Required by `start_erl`; the system will fail to start without it.
3. Must be a valid Erlang term file.
4. Can be created early and included in the tar archive if the configuration is not location- or site-dependent.
5. If a `sys.config` file exists alongside the `.rel` file when `target_system:create/1` is called, it is automatically included in the tar archive.
6. `sys.config.src` is an alternative that allows variable placeholders, but is not required to be a valid Erlang term file.
7. When using `sys.config.src`, an external tool must populate the variables and write a valid `sys.config` before booting.

# Construction / Recognition

## To Construct/Create:
1. Create a `sys.config` file with valid Erlang terms (even if empty: `[].`).
2. Place it in the same directory as the `.rel` file before calling `target_system:create/1` for automatic inclusion.
3. Alternatively, place it in `releases/<version>/` after installation but before starting.
4. For variable substitution, create `sys.config.src` with placeholders and use a tool to generate `sys.config` before boot.

## To Identify/Recognize:
1. A file named `sys.config` in `releases/<version>/`.
2. Contains a list of `{Application, [{Key, Value}]}` tuples (or an empty list `[]`).

# Context & Application

System configuration is essential for embedded target systems. For basic and simple target systems started with `erl`, the `-config` flag can be used to specify configuration. For embedded systems using `start_erl`, the `sys.config` file must be in the release version directory. The `sys.config.src` variant is useful for deployments where configuration varies by site or environment (e.g., database hostnames, port numbers) and must be templated.

# Examples

**Example 1** (Upgrading the Target System section): The simplest possible `sys.config`:

```erlang
%% sys.config
[].
```

**Example 2** (System Configuration Parameters section): If file-location-dependent or site-dependent configuration is needed, `sys.config.src` can contain variable placeholders that are resolved by an external tool before boot. The final `sys.config` must be a valid Erlang term file.

# Relationships

## Builds Upon
- **target-system** — sys.config is a component of a target system

## Enables
- **embedded-target-system** — `start_erl` requires sys.config to boot
- **target-system-upgrade** — new releases can include updated sys.config files

## Related
- **start-erl** — reads sys.config from the release version directory
- **target-system-creation** — automatically includes sys.config if present alongside the .rel file

## Contrasts With
- No direct contrasts in source; `sys.config` (valid Erlang terms, required at boot) implicitly contrasts with `sys.config.src` (template with variables, requires processing before boot).

# Common Errors

- **Error**: Omitting `sys.config` from the release version directory.
  **Correction**: "If there is no such file, the system start fails." Always ensure `sys.config` exists, even if it is just `[].`.

- **Error**: Using `sys.config.src` without processing it into `sys.config` before boot.
  **Correction**: `sys.config.src` is not read directly; you must generate a valid `sys.config` from it before starting the system.

# Common Confusions

- **Confusion**: Thinking `sys.config.src` replaces `sys.config`.
  **Clarification**: `sys.config.src` is a template; a valid `sys.config` must still exist in the release directory at boot time. The `.src` file is for pre-processing convenience, not a runtime alternative.

# Source Reference

"System Configuration Parameters" section, "OTP System Principles" documentation.

# Verification Notes

- Definition source: Direct from source text.
- Confidence rationale: High — explicitly described with clear requirements and consequences.
- Uncertainties: None.
- Cross-reference status: References embedded-target-system, start-erl, target-system-creation.
