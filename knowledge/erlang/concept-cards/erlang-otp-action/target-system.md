---
# === CORE IDENTIFICATION ===
concept: Target System
slug: target-system

# === CLASSIFICATION ===
category: applications-releases
subcategory: deployment
tier: intermediate

# === PROVENANCE ===
source: "Erlang and OTP in Action"
source_slug: erlang-otp-action
authors: "Martin Logan, Eric Merritt, Richard Carlsson"
chapter: "Packaging, services, and deployment"
chapter_number: 10
pdf_page: null
section: "10.1. Applications from a system viewpoint"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - embedded system
  - standalone Erlang system

# === TYPED RELATIONSHIPS ===
prerequisites:
  - erlang-release
  - otp-application
extends: []
related:
  - release-package
  - boot-script
  - sys-config
contrasts_with:
  - erlang-release

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is a target system?"
  - "How do you start a target system?"
  - "What is the difference between interactive and embedded mode?"
---

# Quick Definition

A target system is the running Erlang runtime system that results from installing a release on a host machine — stripped down to run only the applications that release needs.

# Core Definition

A target system is an Erlang runtime system, the result of installing a release on some host machine. It generally only includes those applications that are needed for it to work as a service, as opposed to a standard Erlang/OTP distribution that contains a large number of applications including graphical runtime tools. Minimally, a target system must contain the `stdlib` and `kernel` applications (apart from your own applications), and often `sasl` is also needed to support logging ("Erlang and OTP in Action," Ch. 10, chapter introduction).

# Prerequisites

- **Erlang release** — A target system is produced by installing a release; you must know what a release is.
- **OTP application** — A target system consists of running applications.

# Key Properties

1. Consists of a number of running applications, all with similar structure and metadata, managed in the same way.
2. Minimally contains `kernel` and `stdlib`, often also `sasl`.
3. It is stripped down relative to a full Erlang/OTP distribution — only the applications the service needs.
4. Started by specifying a `.boot` file and a `.config` file on the `erl` command line.
5. Can be run in the foreground (with a shell) or detached as a background daemon.
6. Can run in interactive mode (default, loads code on the fly) or embedded mode (`-mode embedded`, loads all code at startup).

# Construction / Recognition

## To Construct/Create:
1. Build and package a release.
2. Install the release package on a compatible host machine.
3. Start it by giving `erl` the `-boot` and `-config` flags, e.g. `erl -sname cache -boot ./simple_cache -config ./sys`.
4. Add `-detached` to run it as a background daemon, or `-mode embedded` to disable runtime code loading.

## To Identify/Recognize:
1. A running Erlang node started from a boot file that contains only the release's applications, not the full OTP toolset.

# Context & Application

- **Typical contexts**: Production deployment of an Erlang service.
- **Common applications**: Running the Simple Cache as a system-level service.
- **Historical/stylistic notes**: In production you typically run detached (no shell) and connect via a remote shell from another node when you need to log in.

# Examples

**Example 1** (Section 10.2.6): `erl -sname cache -boot ./simple_cache -config ./sys` starts the target system in the foreground.

**Example 2** (Section 10.2.6): Adding `-detached` runs the same system in the background as a daemon; `init:stop()` from a remote shell shuts it down.

# Relationships

## Builds Upon
- **Erlang release** — A target system is an installed release.

## Enables
- (Terminal deployment artifact — nothing builds on it within this source.)

## Related
- **Release package** — The tarball that is unpacked to install a target system.
- **Boot script** — The boot file the target system starts from.
- **sys.config** — The configuration file passed to the target system at startup.

## Contrasts With
- **Erlang release** — The release is the versioned package/specification; the target system is the live installed result.

# Common Errors

- **Error**: Starting a target system without at least one required contact node running.
  **Correction**: Start the contact node(s) first, using matching short names (`-sname`).

- **Error**: Expecting to load extra modules at runtime in an embedded-mode target system.
  **Correction**: In embedded mode all code is loaded at boot; calls to unloaded modules fail. Use interactive mode if dynamic loading is required.

# Common Confusions

- **Confusion**: Thinking a target system is a full Erlang/OTP installation.
  **Clarification**: A target system is deliberately minimal — only the release's applications plus `kernel`, `stdlib`, and usually `sasl`.

# Source Reference

Chapter 10: "Packaging, services, and deployment," chapter introduction and Section 10.2.6 "Starting a target system." See Figure 10.4 (Appmon showing the running release).

# Verification Notes

- Definition source: Direct adaptation of the chapter introduction and Section 10.2.6.
- Confidence rationale: HIGH — the book explicitly defines a target system and describes how to start it.
- Uncertainties: None.
- Cross-reference status: Verified against planned slugs.
- Re-extraction notes: Fresh extraction; no prior card existed.
