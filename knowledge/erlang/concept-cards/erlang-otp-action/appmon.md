---
# === CORE IDENTIFICATION ===
concept: Appmon
slug: appmon

# === CLASSIFICATION ===
category: production-ops
subcategory: introspection-tools
tier: intermediate

# === PROVENANCE ===
source: "Erlang and OTP in Action"
source_slug: erlang-otp-action
authors: "Martin Logan, Eric Merritt, Richard Carlsson"
chapter: "Using the main graphical introspection tools"
chapter_number: 5
pdf_page: null
section: "5.1 Appmon"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - appmon
  - WebAppmon
  - "Application Monitor"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - otp-application
  - supervision-tree
extends: []
related:
  - pman
  - tv-table-viewer
  - erlang-debugger
  - erlang-toolbar
  - webtool
contrasts_with:
  - pman

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is Appmon?"
  - "How do you visualize an application's supervision structure?"
  - "What actions can Appmon perform on a process?"
---

# Quick Definition

Appmon is the Erlang graphical tool for monitoring OTP applications: it visualizes running applications, their supervisor hierarchies, and process status, and can perform basic operations on processes.

# Core Definition

Appmon is a tool for monitoring OTP applications (Ch. 5, Section 5.1). It lets you visualize the applications running in the system as well as their supervisor hierarchies, see the current status of processes, and perform some basic operations on them. It is started with `appmon:start()` from the Erlang shell. The main window lists running applications and shows overall system load; clicking an application opens a window showing its supervision structure. An application window offers four process actions selected by mode buttons: **Info** (process details — message queue length, memory usage, current function), **Send** (send an arbitrary Erlang term to a process), **Trace** (enable tracing on a process), and **Kill** (send an untrappable `kill` signal). Appmon has an application-centric world view.

# Prerequisites

- **OTP application** — Appmon monitors applications.
- **Supervision tree** — Appmon visualizes supervisor hierarchies.

# Key Properties

1. Started with `appmon:start()`.
2. Has an application-centric world view.
3. Main window lists running applications and shows system load.
4. Application windows show the supervision structure.
5. Four process actions: Info, Send, Trace, Kill.
6. Also available via WebTool as WebAppmon.

# Construction / Recognition

## To Use Appmon:
1. Call `appmon:start()` in the Erlang shell.
2. Click an application name to view its supervision structure.
3. Select an action mode (Info, Send, Trace, Kill).
4. Click a process to perform the action.

# Context & Application

Appmon is the go-to tool for seeing applications and supervisor hierarchies — "living things" — in a running system.

- **Typical contexts**: Inspecting which applications are running and how their processes are supervised.
- **Common applications**: Viewing the `tcp_rpc` supervision structure; killing `tr_sup` to watch the whole application disappear.

# Examples

**Example 1** (Ch. 5): Starting `tcp_rpc` makes it appear beside `kernel` in the Appmon main window; clicking it shows the application masters, `tr_sup`, and `tr_server`.

**Example 2** (Ch. 5): Using Kill on the `tr_sup` process removes all `tcp_rpc` processes, demonstrating supervision-based cleanup.

# Relationships

## Related
- **pman** — A complementary tool with a process-centric world view.
- **tv-table-viewer** / **erlang-debugger** — Other introspection tools.
- **erlang-toolbar** — Can launch Appmon.
- **webtool** — Hosts the WebAppmon variant.

## Contrasts With
- **pman** — Appmon has an application/supervision world view; Pman has a process-only world view.

# Common Errors

- **Error**: Using Kill on system processes in a production system.
  **Correction**: Killing arbitrary processes can destabilize the system; the Kill action is for deliberate testing.

# Common Confusions

- **Confusion**: Expecting Appmon to show process relationships outside applications.
  **Clarification**: Appmon's view is application- and supervision-centric; for a pure process view use Pman.

# Source Reference

Chapter 5: Using the main graphical introspection tools, Section 5.1 "Appmon" (Sections 5.1.1 and 5.1.2).

# Verification Notes

- Definition source: Direct adaptation of Section 5.1.
- Confidence rationale: HIGH — explicit, detailed treatment.
- Uncertainties: None.
- Cross-reference status: Slugs reference planned cards in this chapter group.
- Re-extraction notes: Fresh extraction; no prior card existed.
