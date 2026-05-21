---
# === CORE IDENTIFICATION ===
concept: Basic Target System
slug: basic-target-system

# === CLASSIFICATION ===
category: applications-releases
subcategory: deployment
tier: intermediate

# === PROVENANCE ===
source: "OTP System Principles"
source_slug: otp-system-principles
authors: "Ericsson AB"
chapter: "Creating and Upgrading a Target System"
chapter_number: null
pdf_page: null
section: "Starting a Target System"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases: []

# === TYPED RELATIONSHIPS ===
prerequisites:
  - target-system
extends: []
related:
  - simple-target-system
  - embedded-target-system
contrasts_with:
  - simple-target-system
  - embedded-target-system

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How does a basic target system differ from a simple or embedded target system?"
  - "What is the simplest way to start a target system?"
---

# Quick Definition

A basic target system is started by calling the ordinary `erl` script and runs only the Kernel and STDLIB applications, functioning as an ordinary development-like system.

# Core Definition

As described in OTP System Principles: "A _basic target system_ that can be started by calling the ordinary `erl` script." When started this way, "only the Kernel and STDLIB applications are started, that is, the system is started as an ordinary development system." Only two files are needed: `bin/erl` and `bin/start.boot`.

# Prerequisites

- A target system created with `target_system:create/1` and installed with `target_system:install/2`.

# Key Properties

1. Started using the ordinary `erl` script located in `bin/erl`.
2. Only Kernel and STDLIB applications are started by default.
3. Requires only two files: `bin/erl` (from `erts-<version>/bin/erl.src`) and `bin/start.boot` (a copy of `plain.boot`).
4. Can also start a distributed system if `bin/epmd` is present.
5. Does not support runtime code replacement or automatic boot.

# Construction / Recognition

## To Construct/Create:
1. Install a target system using `target_system:install/2`.
2. The `bin/erl` script is automatically generated from `erts-<version>/bin/erl.src` during installation.
3. The `bin/start.boot` file (copy of `plain.boot`) is included in the tar archive during creation.

## To Identify/Recognize:
1. A target system started via `/path/to/target/bin/erl` without `-boot` flags.
2. Only Kernel and STDLIB are running (no application-specific boot).

# Context & Application

A basic target system is useful for development-like usage on the target, interactive debugging, or situations where you want minimal startup. To start all applications defined in the `.rel` file, you must pass the `-boot` flag pointing to the release boot file. This transforms it toward a simple target system.

# Examples

**Example 1** (Starting a Target System section): Starting a basic target system:

```text
% /usr/local/erl-target/bin/erl
```

**Example 2** (Starting a Target System section): Starting with all applications from the `.rel` file:

```text
% /usr/local/erl-target/bin/erl -boot /usr/local/erl-target/releases/FIRST/start
```

# Relationships

## Builds Upon
- **target-system** — a basic target system is the simplest form of a target system

## Enables
- **simple-target-system** — adding the `releases/RELEASES` file to a basic target system enables runtime code replacement

## Related
- **embedded-target-system** — a more advanced form of target system with automatic boot and logging

## Contrasts With
- **simple-target-system** — a simple target system adds support for runtime code replacement via the `releases/RELEASES` file
- **embedded-target-system** — an embedded target system adds automatic boot at system startup and output logging

# Common Errors

- **Error**: Expecting all applications to start when invoking `bin/erl` without the `-boot` flag.
  **Correction**: Without `-boot`, only Kernel and STDLIB are started. Use `-boot releases/FIRST/start` to boot all applications.

# Common Confusions

- **Confusion**: Thinking a basic target system cannot start application-specific code at all.
  **Clarification**: It can start all release applications when given the `-boot` flag; "basic" refers to the default startup behavior, not a limitation of the installed files.

# Source Reference

"Starting a Target System" section, "OTP System Principles" documentation.

# Verification Notes

- Definition source: Direct from source text.
- Confidence rationale: High — explicitly defined and described with concrete file requirements.
- Uncertainties: None.
- Cross-reference status: References target-system, simple-target-system, embedded-target-system.
