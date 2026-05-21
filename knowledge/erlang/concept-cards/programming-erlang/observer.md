---
# === CORE IDENTIFICATION ===
concept: Observer
slug: observer

# === CLASSIFICATION ===
category: production-ops
subcategory: runtime-inspection
tier: intermediate

# === PROVENANCE ===
source: Programming Erlang, Second Edition
source_slug: programming-erlang
authors: Joe Armstrong
chapter: "Mnesia: The Erlang Database"
chapter_number: 20
pdf_page: null
section: "The Table Viewer"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "observer application"
  - "Table Viewer"
  - "observer:start()"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - mnesia
extends: []
related:
  - mnesia-table
  - process
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is the observer application?"
  - "How do I view Mnesia tables visually?"
---

# Quick Definition

Observer is a graphical Erlang application for inspecting a running system. Its Table Viewer tab shows ETS and Mnesia tables; it can also examine system state and processes.

# Core Definition

The observer is the application used "to see the data we have stored in Mnesia" via a built-in table viewer ("The Table Viewer"). It is started with `observer:start()`; clicking the Table Viewer tab and choosing View > Mnesia Tables shows a list of Mnesia tables, and clicking a table opens a window showing its contents. "Using the observer, you can view tables, examine the state of the system, view processes, and so on."

# Prerequisites

- **Mnesia** — The chapter introduces observer specifically for viewing Mnesia tables.

# Key Properties

1. Started with `observer:start()`.
2. Provides a graphical, tabbed interface.
3. The Table Viewer tab lists tables; View > Mnesia Tables filters to Mnesia tables.
4. Clicking a table opens a window showing that table's rows.
5. Can also examine the state of the system and view processes.

# Construction / Recognition

## To Use the Observer:
1. Start it with `observer:start()`.
2. Click the Table Viewer tab.
3. Select View > Mnesia Tables in the control menu.
4. Click a table entry (e.g. `shop`) to open a window with its contents.

## To Recognize:
1. Look for `observer:start()` calls or references to the observer GUI.

# Context & Application

Observer is the standard visual tool for live inspection of an Erlang node.

- **Typical contexts**: Inspecting Mnesia/ETS table contents, watching processes, examining system state during development or operations.
- **Common applications**: Quickly checking what data a table actually holds.
- **Historical/stylistic notes**: The book uses it specifically as the Mnesia table viewer.

# Examples

**Example 1** ("The Table Viewer"): Starting the observer and viewing the `shop` table.

```erlang
observer:start()
%% then: Table Viewer tab -> View > Mnesia Tables -> click "shop"
```

# Relationships

## Builds Upon
- (Foundational tool within this chapter's scope.)

## Enables
- (No card depends on this concept.)

## Related
- **Mnesia table** — The Table Viewer displays Mnesia tables.
- **Process** — Observer can view the processes running on a node.

## Contrasts With
- None.

# Common Errors

- **Error**: Expecting the table list to show Mnesia tables by default.
  **Correction**: In the Table Viewer, choose View > Mnesia Tables to switch from the default view.

# Common Confusions

- **Confusion**: Thinking observer is only a Mnesia tool.
  **Clarification**: Observer is a general system-inspection application; viewing Mnesia tables is just one of its features.

# Source Reference

Chapter 20: "Mnesia: The Erlang Database", section "The Table Viewer".

# Verification Notes

- Definition source: Direct quotes from "The Table Viewer".
- Confidence rationale: HIGH — the section explicitly explains how to start and use the observer's table viewer.
- Uncertainties: The book treats observer briefly; deeper features are out of scope.
- Cross-reference status: Verified against planned cards.
- Re-extraction notes: Fresh extraction — no pre-existing card.
