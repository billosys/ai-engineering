---
# === CORE IDENTIFICATION ===
concept: Target System
slug: target-system

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
  - basic target system
  - simple target system
  - embedded target system

# === TYPED RELATIONSHIPS ===
prerequisites:
  - release
extends: []
related:
  - boot-file
  - release-package
  - start-scripts-and-configuration
  - heart
  - release-handler
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is a target system?"
  - "How do I package, start, and configure a release?"
---

# Quick Definition

A target system is a deployed Erlang release running in a target environment. It comes in three forms — basic, simple, and embedded — distinguished by how the node is started and how much of OTP's startup, supervision, and upgrade machinery it uses.

# Core Definition

A target system is a release as it runs in a deployment environment. The source distinguishes three types (Cesarini & Vinoski, p. 283-284, 283-289, pdf p. 282): a *basic target system* is started by a Unix shell script that calls `erl -s`, suitable only for coding, proofs of concept, or quick hacks; a *simple target system* makes use of a boot script and tools shipped with the `sasl` application, facilitating controlled software upgrades at runtime; and an *embedded target system* is the most solid and flexible deployment, where the target system becomes part of a larger package on the underlying OS, runs as a daemon job without an interactive shell, and streams all I/O through pipes.

# Prerequisites

- **Release** — A target system is a release deployed and running; the release concept comes first.

# Key Properties

1. Three types: basic, simple, embedded.
2. Basic — started via `erl -s module function args`; loses OTP startup, supervision, and upgrade benefits; not for production.
3. Simple — uses a boot script and `sasl` tools; supports controlled runtime upgrades; more robust than basic.
4. Embedded — runs as a background daemon, no interactive shell, I/O streamed through pipes; starts when the OS boots.
5. Embedded systems are connected to via `to_erl`; the `run_erl` binary manages the pipes.
6. Embedded is the preferred deployment for mission-critical systems requiring 24/7 availability.
7. The release handler is intended to work with embedded target systems.

# Construction / Recognition

## To Build an Embedded Target System:
1. Create the release directory structure (`lib`, `releases`, `erts`, `bin`).
2. Generate the boot file with `systools:make_script/2` and the tar with `systools:make_tar/2`.
3. Copy `start`, `start_erl`, `run_erl`, and `to_erl` into `bin`; edit `start` to set `FINAL_ROOTDIR`.
4. Create `start_erl.data` in `releases` with the erts and release versions.
5. Start with `bin/start`; connect with `bin/to_erl`.

## To Recognize the Type:
1. Started by `erl -s ... -noshell` -> basic.
2. Uses a `.boot` file and `sasl` -> simple.
3. Runs as a daemon, connected via `to_erl` -> embedded.

# Context & Application

- **Typical contexts**: Deciding how to deploy a finished Erlang system.
- **Common applications**: Embedded systems for telecom switches and 24/7 services; simple systems for less critical deployments; basic systems for development only.
- **Historical/stylistic notes**: "Embedded" is overloaded in Erlang/OTP — embedded target system vs. embedded code-loading mode are distinct.

# Examples

**Example 1** (p. 283): A basic target system started with `erl -s myprojectsup -noshell` loses all OTP application startup, supervision, and upgrade procedures.

**Example 2** (p. 287): Starting an embedded system and connecting to it:

```
$ bin/start
$ bin/to_erl /tmp/
Attaching to /tmp/erlang.pipe.1 (^D to exit)
1> application:which_applications().
[{bsc,"Base Station Controller","1.0"}, ...]
```

**Example 3** (p. 288): To avoid killing the background job, exit the `to_erl` shell with Ctrl-d, not `q()`, `halt()`, or Ctrl-c a.

# Relationships

## Builds Upon
- **Release** — A target system is a deployed, running release.

## Related
- **Boot file** — Simple and embedded systems boot from a `.boot` file.
- **Release package** — The deployment artifact installed to create a target system.
- **Start scripts and configuration** — `start`/`start_erl` scripts configure an embedded system.
- **Heart** — Recommended for embedded systems to restart a crashed runtime.
- **Release handler** — Intended to work with embedded target systems.

# Common Errors

- **Error**: Shipping a basic target system to production.
  **Correction**: Use an embedded target system so you keep OTP startup, supervision, and upgrade procedures.

- **Error**: Using `/tmp` for the read/write pipes when running multiple embedded nodes on one host.
  **Correction**: Redirect pipes to a subdirectory of the Erlang root directory so multiple nodes can coexist.

# Common Confusions

- **Confusion**: Assuming "embedded" always means the same thing.
  **Clarification**: Erlang/OTP uses "embedded" for the embedded target system and separately for the embedded code-loading mode.

- **Confusion**: Thinking simple target systems are unacceptable.
  **Clarification**: Simple target systems can be acceptable and respectable if they meet requirements; they are used by several popular open source projects.

# Source Reference

Chapter 10: System Principles and Release Handling, sections "System Principles," "Creating a Release Package," and "Start Scripts and Configuring on the Target," pages 283-289 (pdf p. 282).

# Verification Notes

- Definition source: Direct adaptation of pp. 283-284 and pp. 283-289.
- Confidence rationale: HIGH — the source explicitly names and distinguishes the three target-system types.
- Uncertainties: None.
- Cross-reference status: Verified against planned cards.
- Re-extraction notes: Fresh extraction; no pre-existing card.
