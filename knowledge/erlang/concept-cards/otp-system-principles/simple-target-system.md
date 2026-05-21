---
# === CORE IDENTIFICATION ===
concept: Simple Target System
slug: simple-target-system

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
  - basic-target-system
extends:
  - basic-target-system
related:
  - embedded-target-system
  - target-system-upgrade
contrasts_with:
  - basic-target-system
  - embedded-target-system

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How does a basic target system differ from a simple or embedded target system?"
  - "What is needed for runtime code replacement in a target system?"
---

# Quick Definition

A simple target system extends a basic target system by supporting code replacement in runtime, enabled by the presence of the `releases/RELEASES` file.

# Core Definition

As described in OTP System Principles: "A _simple target system_ that also supports code replacement in runtime." It is started the same way as a basic target system, but "the only difference is that also the file `releases/RELEASES` is present for code replacement in runtime to work."

# Prerequisites

- A target system created and installed with `target_system:create/1` and `target_system:install/2`.
- Understanding of basic target system startup.

# Key Properties

1. Started the same way as a basic target system (via `erl` with `-boot` flag).
2. The `releases/RELEASES` file is present, enabling the `release_handler` to manage code replacement.
3. Supports hot code loading and release upgrades at runtime.
4. Does not include automatic boot at system startup or output logging.

# Construction / Recognition

## To Construct/Create:
1. Install a target system using `target_system:install/2` — the `releases/RELEASES` file is created automatically during installation.
2. Start with the `-boot` flag to boot all applications.

## To Identify/Recognize:
1. A target system started via `bin/erl -boot releases/<version>/start`.
2. The file `releases/RELEASES` exists in the target directory.
3. Runtime code replacement via `release_handler` functions is operational.

# Context & Application

A simple target system is appropriate when you need the ability to upgrade application code at runtime without restarting the entire system, but do not need the automatic boot and logging capabilities of an embedded target system. The `releases/RELEASES` file is what the `release_handler` uses to track installed releases and manage code replacement.

# Examples

**Example 1** (Starting a Target System section): A simple target system is started like a basic target system with `-boot`, but the key difference is the presence of `releases/RELEASES`:

```text
% /usr/local/erl-target/bin/erl -boot /usr/local/erl-target/releases/FIRST/start
```

The file `releases/RELEASES` is created during `target_system:install/2` from the data in `releases/mysystem.rel`.

# Relationships

## Builds Upon
- **basic-target-system** — adds runtime code replacement support to the basic target system

## Enables
- **target-system-upgrade** — the RELEASES file enables the release_handler to manage upgrades

## Related
- **embedded-target-system** — adds automatic boot and logging on top of simple target system capabilities

## Contrasts With
- **basic-target-system** — a basic target system lacks the `releases/RELEASES` file and cannot support runtime code replacement
- **embedded-target-system** — an embedded target system additionally supports automatic boot and logging via `run_erl`/`start_erl`

# Common Errors

- **Error**: Deleting or failing to create the `releases/RELEASES` file, then expecting runtime code replacement to work.
  **Correction**: Ensure `target_system:install/2` completes successfully, which creates the `releases/RELEASES` file.

# Common Confusions

- **Confusion**: Thinking a "simple" target system is simpler than a "basic" target system.
  **Clarification**: The naming is incremental — "simple" is more capable than "basic." A simple target system is a basic target system plus runtime code replacement support.

# Source Reference

"Starting a Target System" section, "OTP System Principles" documentation.

# Verification Notes

- Definition source: Direct from source text.
- Confidence rationale: High — explicitly defined with clear distinguishing characteristic (the RELEASES file).
- Uncertainties: None.
- Cross-reference status: References basic-target-system, embedded-target-system, target-system-upgrade.
