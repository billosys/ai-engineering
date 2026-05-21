---
# === CORE IDENTIFICATION ===
concept: Remote Shell
slug: remote-shell

# === CLASSIFICATION ===
category: distribution
subcategory: nodes-clustering
tier: intermediate

# === PROVENANCE ===
source: "Erlang and OTP in Action"
source_slug: erlang-otp-action
authors: "Martin Logan, Eric Merritt, Richard Carlsson"
chapter: "Introducing distributed Erlang/OTP"
chapter_number: 8
pdf_page: null
section: "8.2.6 Working with remote shells"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "remote shell job"
  - "remote Erlang shell"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - location-transparency
  - erlang-node
extends: []
related:
  - connecting-nodes
  - inter-node-messaging
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is a remote shell?"
  - "How do I start a shell on another node?"
  - "How do I leave a remote shell safely?"
---

# Quick Definition

A remote shell is an Erlang shell process that runs on a remote node but is connected to your local console; it lets you operate a remote node as if sitting at its keyboard.

# Core Definition

A remote shell is a shell process that executes on a remote node while remaining connected to the input/output streams of the local console. It is possible because the shell communicates with its console by message passing and does not care whether it runs on the same node as the console — a direct consequence of location transparency. The feature is built into the Erlang shell's job control: pressing Ctrl-G opens the "User switch command" prompt, where the `r [node [shell]]` command starts a remote shell job on the named node, `j` lists jobs, and `c [nn]` connects to one. Once connected, the prompt shows the remote node's name, and any command — killing processes, compiling and upgrading code, monitoring, debugging — runs on that node (Ch. 8, Section 8.2.6).

# Prerequisites

- **location-transparency** — Remote shells work because the shell's message passing is location transparent.
- **erlang-node** — A remote shell runs on a remote node.

# Key Properties

1. A shell process running on a remote node, wired to the local console.
2. Enabled by location transparency of the shell's message-based I/O.
3. Started via the shell job-control `r` command (after Ctrl-G).
4. The prompt shows the remote node's name when connected.
5. Executes any command on the remote node, including maintenance and code upgrades.
6. Nodes need not be previously connected for `r` to work.

# Construction / Recognition

## To Start a Remote Shell:
1. Press Ctrl-G to open the User switch command prompt.
2. Enter `r 'node@host'` to start a remote shell job on that node.
3. Use `j` to list jobs and `c` (or `c nn`) to connect to the remote job.
4. To leave, use Ctrl-G then `q`, or Ctrl-C / Ctrl-Break then `A`.

## To Recognize:
1. A shell prompt showing a node name different from your local node indicates a remote shell.

# Context & Application

- **Typical contexts**: Operating long-lived production nodes from a temporary local node.
- **Common applications**: Live maintenance, debugging, code upgrades on remote nodes.
- **Historical/stylistic notes**: Typically you start a temporary local node, connect remotely, and discard the temporary node when done.

# Examples

**Example 1** (Section 8.2.6): On node `a`, `r 'b@mybox.home.net'` starts a remote shell job; `j` lists it as `2* {'b@mybox.home.net',shell,start,[]}`, and `c` connects, yielding the prompt `(b@mybox.home.net)1>`.

# Relationships

## Builds Upon
- **location-transparency** — Remote shells are a demonstration of location transparency.
- **erlang-node** — The shell runs on a remote node.

## Enables
- None.

## Related
- **connecting-nodes** — Nodes can be connected for or by the remote shell session.
- **inter-node-messaging** — The shell's I/O is itself message passing across nodes.

## Contrasts With
- None.

# Common Errors

- **Error**: Typing `q()` to leave a remote shell.
  **Correction**: `q()` is `init:stop()` and shuts down the remote node; use Ctrl-G then `Q`, or Ctrl-C/Ctrl-Break then `A`.

# Common Confusions

- **Confusion**: Thinking a remote shell is a separate program like SSH.
  **Clarification**: It is an ordinary Erlang shell process that happens to run on another node, connected via message passing.

# Source Reference

Chapter 8: Introducing distributed Erlang/OTP, Section 8.2.6 "Working with remote shells," Figure 8.5 and the "Quit with care" sidebar.

# Verification Notes

- Definition source: Directly adapted from Section 8.2.6.
- Confidence rationale: HIGH — the book walks through starting and using a remote shell.
- Uncertainties: None.
- Cross-reference status: Verified.
