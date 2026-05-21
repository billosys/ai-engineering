---
# === CORE IDENTIFICATION ===
concept: TV (Table Viewer)
slug: tv-table-viewer

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
section: "5.4 TV, the Table Viewer"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - TV
  - "Table Viewer"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - ets
extends: []
related:
  - appmon
  - pman
  - erlang-debugger
  - erlang-toolbar
contrasts_with:
  - erlang-debugger

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is TV, the Table Viewer?"
  - "How do you inspect ETS and Mnesia tables graphically?"
  - "What kinds of tables can TV display?"
---

# Quick Definition

TV (Table Viewer) is the Erlang graphical tool for inspecting data tables — ETS and Mnesia tables — showing their contents much like a spreadsheet.

# Core Definition

TV, the Table Viewer, is different from the other Chapter 5 tools: whereas Appmon, Pman, and the Debugger are about looking at the code running in a system, TV is for looking at the data (Ch. 5, Section 5.4). It is used to view the two main types of tables in Erlang: ETS tables and Mnesia tables. It is started with `tv:start()`; ETS is the default view. With no user applications running, few or no tables appear; Options > System Tables reveals the system tables. Double-clicking a table (or File > Open Table) opens a window showing the table contents like a spreadsheet, with a key symbol marking the primary-key column. TV's menus and icons allow sorting, polling, searching, and editing or deleting entries.

# Prerequisites

- **ETS** — TV's default view displays ETS tables.

# Key Properties

1. Started with `tv:start()`.
2. Inspects data — ETS tables and Mnesia tables.
3. ETS is the default view.
4. Displays table contents in a spreadsheet-like grid with a marked key column.
5. Options > System Tables reveals system tables (hidden by default).
6. Supports sorting, polling, searching, and editing/deleting entries.

# Construction / Recognition

## To Use TV:
1. Call `tv:start()` in the Erlang shell.
2. Use Options > System Tables to show system tables if needed.
3. Double-click a table to open its contents window.

# Context & Application

TV is the tool to reach for when you want to see what is in your data — useful once you start using ETS tables and Mnesia.

- **Typical contexts**: Inspecting cache or registry data held in ETS.
- **Common applications**: Viewing the `ac_tab` system table owned by the `application_controller`; inspecting an `sc_store`-style ETS table.

# Examples

**Example 1** (Ch. 5): Opening the `ac_tab` system table — owned by the `application_controller` — shows information about the `kernel` and `stdlib` applications.

# Relationships

## Related
- **appmon** / **pman** / **erlang-debugger** — The other Chapter 5 introspection tools.
- **erlang-toolbar** — Can launch TV.

## Contrasts With
- **erlang-debugger** — The debugger (like Appmon and Pman) looks at running code; TV looks at data.

# Common Errors

- **Error**: Expecting to see all tables immediately on starting TV.
  **Correction**: System tables are hidden by default; enable Options > System Tables.

# Common Confusions

- **Confusion**: Thinking TV inspects processes or code.
  **Clarification**: TV is exclusively for data tables — ETS and Mnesia — not code or processes.

# Source Reference

Chapter 5: Using the main graphical introspection tools, Section 5.4 "TV, the Table Viewer."

# Verification Notes

- Definition source: Direct adaptation of Section 5.4.
- Confidence rationale: HIGH — explicit, detailed treatment.
- Uncertainties: None.
- Cross-reference status: References planned `ets` card (owned by this chapter group).
- Re-extraction notes: Fresh extraction; no prior card existed.
