---
# === CORE IDENTIFICATION ===
concept: Target System
slug: target-system

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
section: "Creating and Upgrading a Target System"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "OTP target system"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - release
extends: []
related:
  - basic-target-system
  - simple-target-system
  - embedded-target-system
  - target-system-creation
  - target-system-installation
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is a target system?"
  - "What must I understand before creating a target system?"
  - "How does a basic target system differ from a simple or embedded target system?"
---

# Quick Definition

A target system is a customized Erlang/OTP system in which dispensable applications have been removed and new application-specific applications have been included, created for deployment to a particular purpose.

# Core Definition

As described in OTP System Principles: "there is a need to be able to create a new system based on a given Erlang/OTP system, where dispensable applications are removed and new applications are included. Documentation and source code is irrelevant and is therefore not included in the new system. This chapter is about creating such a system, which is called a _target system_."

# Prerequisites

- Understanding of Erlang/OTP applications and releases
- A working Erlang/OTP system structured according to OTP design principles

# Key Properties

1. Based on a given Erlang/OTP system but trimmed to only the needed applications.
2. Excludes documentation and source code from the base system.
3. Can include custom, application-specific code alongside original OTP applications.
4. Comes in three levels of functionality: basic, simple, and embedded.
5. Only the UNIX case is considered in the official documentation.

# Construction / Recognition

## To Construct/Create:
1. Create a `.rel` file specifying the ERTS version and all applications to include.
2. Use `target_system:create/1` from the `sasl` application to build the target system tar archive.
3. Use `target_system:install/2` to install the target system into a destination directory.

## To Identify/Recognize:
1. A self-contained Erlang/OTP installation with only the required applications.
2. Contains `bin/`, `erts-<version>/bin/`, `lib/`, `releases/`, and `log/` directories.
3. Has a `releases/start_erl.data` file with ERTS and release version information.

# Context & Application

Target systems are used for production deployment of Erlang/OTP applications. Instead of deploying a full Erlang/OTP development installation plus application code, a target system packages only the necessary runtime components and applications into a deployable artifact. The `sasl` application provides the `target_system` example module that automates the creation and installation process.

# Examples

**Example 1** (Creating a Target System section): A `.rel` file defines the target system contents:

```erlang
%% mysystem.rel
{release,
 {"MYSYSTEM", "FIRST"},
 {erts, "5.10.4"},
 [{kernel, "2.16.4"},
  {stdlib, "1.19.4"},
  {sasl, "2.3.4"},
  {pea, "1.0"}]}.
```

This specifies a system named "MYSYSTEM" version "FIRST" with ERTS 5.10.4, the required Kernel, STDLIB, and SASL applications, plus a custom application `pea`.

# Relationships

## Builds Upon
- **release** — a target system is built from a release specification (`.rel` file)

## Enables
- **basic-target-system** — the simplest form of a target system
- **simple-target-system** — a target system with code replacement support
- **embedded-target-system** — a target system with automatic boot and logging
- **target-system-upgrade** — once a target system is deployed, it can be upgraded

## Related
- **target-system-creation** — the process of building the tar archive
- **target-system-installation** — the process of installing to a directory

## Contrasts With
- No direct contrasts in source; implicitly contrasts with a full Erlang/OTP development installation.

# Common Errors

- **Error**: Including unnecessary applications in the `.rel` file, bloating the target system.
  **Correction**: Only list the applications actually required for the target system's purpose.

- **Error**: Attempting to create a target system without a properly structured OTP application layout.
  **Correction**: Ensure the system is structured according to OTP design principles before creating a target system.

# Common Confusions

- **Confusion**: Thinking a target system is the same as a full Erlang/OTP installation.
  **Clarification**: A target system is a stripped-down, purpose-built system that excludes documentation, source code, and unnecessary applications from the base Erlang/OTP distribution.

# Source Reference

"Creating and Upgrading a Target System" introduction, "OTP System Principles" documentation.

# Verification Notes

- Definition source: Direct from source text.
- Confidence rationale: High — explicitly defined as a named concept with clear description.
- Uncertainties: None.
- Cross-reference status: References basic-target-system, simple-target-system, embedded-target-system, target-system-creation, target-system-installation, target-system-upgrade.
