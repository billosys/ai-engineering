---
# === CORE IDENTIFICATION ===
concept: WebTool
slug: webtool

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
section: "5.1.2 The WebTool version of Appmon"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - WebTool
  - WebAppmon

# === TYPED RELATIONSHIPS ===
prerequisites:
  - appmon
extends:
  - appmon
related:
  - pman
  - erlang-toolbar
contrasts_with:
  - appmon

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is WebTool?"
  - "How do you monitor an Erlang system without a graphical environment?"
  - "What is WebAppmon?"
---

# Quick Definition

WebTool is an Erlang application that presents introspection tools through a web browser; WebAppmon is its browser-based version of Appmon, usable even where Appmon itself is not installed.

# Core Definition

WebTool lets you use Appmon another way — through a web browser — which is useful if you do not have a graphical environment (Ch. 5, Section 5.1.2). Calling `webtool:start()` from the Erlang shell prints a URL (e.g. `http://localhost:8888/`); pointing a browser there brings up a page from which you can select one or more tools to start. One of these is **WebAppmon**, which provides an interface similar to the Appmon GUI but presented via the browser. The WebTool version of Appmon can be used even if the Appmon application is not installed on the system being monitored — for example, an embedded system with a minimal Erlang environment. The WebTool version does not allow stopping applications or killing processes.

# Prerequisites

- **Appmon** — WebAppmon is the browser-based version of Appmon.

# Key Properties

1. Started with `webtool:start()`, which prints a browser URL.
2. Presents introspection tools (including WebAppmon) in a web browser.
3. WebAppmon mirrors the Appmon GUI interface.
4. Works even where Appmon itself is not installed (e.g. embedded systems).
5. Cannot stop applications or kill processes (unlike the Appmon GUI).

# Construction / Recognition

## To Use WebTool:
1. Call `webtool:start()` in the Erlang shell.
2. Open the printed URL in a web browser.
3. Select WebAppmon (or another tool) from the welcome page.

# Context & Application

WebTool is for monitoring systems remotely or without a desktop environment — notably embedded systems.

- **Typical contexts**: Monitoring a headless or embedded Erlang node from a browser.
- **Common applications**: Running WebAppmon against a minimal embedded Erlang system.

# Examples

**Example 1** (Ch. 5): `webtool:start()` prints `WebTool is available at http://localhost:8888/`; the browser page lets you start WebAppmon.

# Relationships

## Builds Upon
- **Appmon** — WebAppmon is Appmon presented through a browser.

## Related
- **pman** / **erlang-toolbar** — Other introspection tools.

## Contrasts With
- **Appmon** — The WebTool version cannot stop applications or kill processes; the native Appmon GUI can.

# Common Errors

- **Error**: Expecting to kill processes from WebAppmon.
  **Correction**: The WebTool version is read-mostly; use the native Appmon GUI for stop/kill actions.

# Common Confusions

- **Confusion**: Thinking Appmon must be installed to use WebAppmon.
  **Clarification**: WebAppmon works even on systems where the Appmon application itself is not installed.

# Source Reference

Chapter 5: Using the main graphical introspection tools, Section 5.1.2 "The WebTool version of Appmon."

# Verification Notes

- Definition source: Direct adaptation of Section 5.1.2.
- Confidence rationale: HIGH — explicit treatment in the source.
- Uncertainties: None.
- Cross-reference status: Slugs reference planned cards in this chapter group.
- Re-extraction notes: Fresh extraction; no prior card existed.
