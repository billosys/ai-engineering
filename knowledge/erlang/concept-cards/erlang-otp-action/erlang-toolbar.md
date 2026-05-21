---
# === CORE IDENTIFICATION ===
concept: Erlang Toolbar
slug: erlang-toolbar

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
section: "5.5 Toolbar"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - Toolbar
  - "Erlang Toolbar"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - appmon
  - pman
  - erlang-debugger
  - tv-table-viewer
extends: []
related:
  - appmon
  - pman
  - erlang-debugger
  - tv-table-viewer
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is the Erlang Toolbar?"
  - "How do you launch the graphical introspection tools from one place?"
  - "Can you add custom tools to the Erlang Toolbar?"
---

# Quick Definition

The Erlang Toolbar is a small window with a button for each available graphical tool (TV, Pman, Debugger, Appmon), letting you launch them from one place; custom tool buttons can also be added.

# Core Definition

The Toolbar application is a small window with a button for each of the available applications (Ch. 5, Section 5.5). If you use the introspection tools often — for example, during a debugging session — it can be easier to start the Toolbar and keep it on your desktop rather than starting the tools individually. It is started with `toolbar:start()`. The first button starts TV, the next Pman, the third the Debugger, and the fourth Appmon. You can add your own custom tool buttons via Tools > Create Tool File, supplying an icon and the module and function used to start the tool (the tool-start function takes no arguments).

# Prerequisites

- **Appmon**, **Pman**, **Erlang Debugger**, **TV (Table Viewer)** — The Toolbar is a launcher for these tools.

# Key Properties

1. Started with `toolbar:start()`.
2. A small window with one button per tool.
3. Buttons launch TV, Pman, Debugger, and Appmon.
4. Custom tool buttons can be added via Tools > Create Tool File.
5. A custom tool's start function must take no arguments.

# Construction / Recognition

## To Use the Toolbar:
1. Call `toolbar:start()` in the Erlang shell.
2. Click a button to launch TV, Pman, Debugger, or Appmon.
3. Optionally use Tools > Create Tool File to add a custom tool (icon, module, function).

# Context & Application

The Toolbar is a convenience launcher, handy during debugging sessions when several tools are used together.

- **Typical contexts**: Keeping all introspection tools one click away during debugging.
- **Common applications**: Launching Appmon, Pman, the Debugger, and TV from a single window.

# Examples

**Example 1** (Ch. 5): `toolbar:start()` opens the Toolbar window; the four buttons start TV, Pman, Debugger, and Appmon respectively.

**Example 2** (Ch. 5): Creating a tool file with module `mymod` and function `myfun` makes a button that calls `mymod:myfun()`.

# Relationships

## Related
- **appmon** / **pman** / **erlang-debugger** / **tv-table-viewer** — The tools the Toolbar launches.

## Contrasts With
- This is a launcher utility; the source draws no direct contrast.

# Common Errors

- **Error**: Giving a custom tool a start function that takes arguments.
  **Correction**: The tool-start function must take no arguments.

# Common Confusions

- **Confusion**: Thinking the Toolbar is itself an introspection tool.
  **Clarification**: It only launches the other tools; it performs no inspection of its own.

# Source Reference

Chapter 5: Using the main graphical introspection tools, Section 5.5 "Toolbar."

# Verification Notes

- Definition source: Direct adaptation of Section 5.5.
- Confidence rationale: HIGH — explicit treatment in the source.
- Uncertainties: None.
- Cross-reference status: Slugs reference planned cards in this chapter group.
- Re-extraction notes: Fresh extraction; no prior card existed.
