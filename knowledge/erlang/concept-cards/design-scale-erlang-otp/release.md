---
# === CORE IDENTIFICATION ===
concept: Release
slug: release

# === CLASSIFICATION ===
category: applications-releases
subcategory: system-principles
tier: intermediate

# === PROVENANCE ===
source: "Designing for Scalability with Erlang/OTP"
source_slug: design-scale-erlang-otp
authors: Francesco Cesarini & Steve Vinoski
chapter: "System Principles and Release Handling"
chapter_number: 10
pdf_page: 282
section: "System Principles"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - standalone node
  - OTP release

# === TYPED RELATIONSHIPS ===
prerequisites:
  - otp-application
  - supervision-tree
extends: []
related:
  - release-resource-file
  - release-directory-structure
  - erlang-runtime-system
  - target-system
  - boot-file
contrasts_with:
  - otp-application

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is a release?"
  - "How does a release relate to the applications it bundles?"
  - "What distinguishes an OTP application from a release?"
---

# Quick Definition

A release is a standalone Erlang node that bundles a set of OTP applications, the configuration and boot files needed to start them, and a copy of the Erlang runtime system. It is the unit of packaging and deployment for an Erlang system.

# Core Definition

An Erlang release is defined as a standalone node consisting of: a set of OTP applications written or reused as part of the project (typically containing the system's business logic), the OTP applications from the standard distribution that those applications depend on, a set of configuration and boot files together with a start script, and the Erlang runtime system including a copy of the virtual machine (Cesarini & Vinoski, p. 282, pdf p. 282). A system consists of one or more possibly different releases, and each node runs a release, either on a single host or in a distributed environment. Standard releases let a system follow a generic structure that is target independent and can be managed and upgraded with tools independent of the underlying operating system.

# Prerequisites

- **OTP application** — A release is built by grouping applications together; you must understand the application as the unit being bundled.
- **Supervision tree** — Applications in a release start supervision trees; the release groups these into a single startable node.

# Key Properties

1. A release is a standalone node, startable as one unit.
2. It bundles project applications, their standard-distribution dependencies, configuration and boot files, a start script, and the runtime system.
3. The packaging hierarchy in Erlang is: function -> module -> application -> release.
4. Releases all share the same directory structure; the Erlang installation itself is a "standard release."
5. The runtime system does not differentiate user-defined applications from Erlang/OTP-distribution applications.
6. A release is target independent, though the package built from it may be OS- and hardware-specific.

# Construction / Recognition

## To Create a Release:
1. Define a release resource file (`.rel`) listing applications and their versions plus the erts version.
2. Create a binary boot file containing commands to load modules and start applications.
3. Create the release directory structure (`lib`, `releases`, `bin`, optionally `erts`).
4. Create a start script defining configurations, system limits, and code paths.
5. Build a deployment package (tar file, OS package, container) for the target environment.

## To Recognize a Release:
1. Look for the four mandatory directories: `lib`, `erts`, `releases`, `bin`.
2. Look for `.rel`, `.script`, and `.boot` files under the `releases` directory.

# Context & Application

In many programming languages, packaging is handled by the operating system; in Erlang, OTP handles it by creating a release. Releases are used to deploy an Erlang node as a single deployable unit.

- **Typical contexts**: Packaging a finished system for production deployment.
- **Common applications**: Building target systems (basic, simple, embedded) for deployment; shipping a node with or without its own runtime system.
- **Historical/stylistic notes**: When you install Erlang you install the "standard release"; the only difference between it and your own releases is the applications loaded and started and their configuration.

# Examples

**Example 1** (p. 282): When you installed Erlang, you installed the standard release. The runtime treats user-defined and distribution applications identically.

**Example 2** (p. 287): The `basestation` release (version "1.0") groups the standard `kernel`, `stdlib`, and `sasl` applications with the proprietary `bsc` application version 1.0.

# Relationships

## Builds Upon
- **OTP application** — A release is a set of loosely coupled applications grouped together.

## Enables
- **Target system** — Releases are deployed as basic, simple, or embedded target systems.
- **Release upgrade** — A properly packaged release is the baseline for live upgrades.

## Related
- **Release resource file** — The `.rel` file specifies what the release contains.
- **Boot file** — Generated from the release specification; starts the release.
- **Release directory structure** — The on-disk layout every release shares.
- **Erlang runtime system** — Bundled into the release.

## Contrasts With
- **OTP application** — An application is one component; a release groups many applications plus boot/config files and the runtime into a startable node.

# Common Errors

- **Error**: Shipping a basic target system (`erl -s myprojectsup -noshell`) to production.
  **Correction**: Ship an embedded target system built from a proper release so you keep OTP startup, supervision, and upgrade procedures.

- **Error**: Assuming the release's runtime is automatically present on the target.
  **Correction**: Decide explicitly whether to include `erts` in the package, or rely on a runtime already installed on the target machine.

# Common Confusions

- **Confusion**: Believing a release is the same as an application.
  **Clarification**: An application is a component; a release is a complete, standalone node bundling many applications, boot/config files, and the runtime.

- **Confusion**: Thinking Erlang's release process is fundamentally different from non-Erlang packaging.
  **Clarification**: Creating a release is as easy as (if not easier than) creating a non-Erlang package; it just follows a generic, target-independent structure.

# Source Reference

Chapter 10: System Principles and Release Handling, section "System Principles," pages 282-283 (pdf p. 282). See also "Release Directory Structure" (p. 284) and Figure 11-2 "Creating an OTP release" (p. 273).

# Verification Notes

- Definition source: Direct adaptation of the bulleted definition on p. 282.
- Confidence rationale: HIGH — the source gives an explicit, enumerated definition of a release.
- Uncertainties: None.
- Cross-reference status: Verified against planned cards in this extraction.
- Re-extraction notes: Fresh extraction; no pre-existing card.
