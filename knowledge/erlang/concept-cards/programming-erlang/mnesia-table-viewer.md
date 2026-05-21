---
# === CORE IDENTIFICATION ===
concept: Mnesia Table Viewer
slug: mnesia-table-viewer

# === CLASSIFICATION ===
category: production-ops
subcategory: runtime-inspection
tier: foundational

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
  - "Table Viewer tab"
  - "observer table viewer"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - mnesia
  - mnesia-table
  - observer
extends: []
related:
  - observer
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do I view the contents of an Mnesia table?"
  - "What is the Mnesia table viewer?"
---

# Quick Definition

The Mnesia Table Viewer is a feature of the graphical observer application that lets you browse the contents of Mnesia tables visually, without writing any query code.

# Core Definition

"To see the data we have stored in Mnesia, we can use the table viewer that is built into the 'observer' application" ("The Table Viewer"). You start the observer with `observer:start()`, click the Table Viewer tab, then select `View > Mnesia Tables` in the observer's control menu. This shows a list of Mnesia tables; clicking a table entry (for example `shop`) opens a new window displaying that table's rows. Beyond Mnesia tables, the observer lets you "view tables, examine the state of the system, view processes, and so on."

# Prerequisites

- **Mnesia** — the viewer displays tables of a running Mnesia database
- **Mnesia table** — the unit the viewer browses
- **Observer** — the Table Viewer is a tab within the observer application

# Key Properties

1. Built into the observer application
2. Reached via the Table Viewer tab, then `View > Mnesia Tables`
3. Lists all Mnesia tables; clicking one opens a window with its rows
4. Read-only visual inspection — no query code required
5. Part of observer's broader system-inspection capabilities

# Construction / Recognition

## To Use the Table Viewer:

1. Start the observer with `observer:start()`
2. Click the Table Viewer tab
3. Select `View > Mnesia Tables` in the control menu
4. Click a table entry (e.g. `shop`) to open a window showing its contents

## To Recognize:

1. Use of `observer:start()` followed by navigation to Mnesia tables

# Context & Application

- **Typical contexts**: Quickly checking what data an Mnesia table actually holds during development or debugging
- **Common applications**: Verifying that writes landed, inspecting row values without a QLC query
- **Historical/stylistic notes**: The book introduces it specifically as a convenient way to see stored Mnesia data

# Examples

**Example 1** (section "The Table Viewer"): Starting the observer and opening the `shop` table.

```erlang
observer:start()
%% then: Table Viewer tab -> View > Mnesia Tables -> click "shop"
```

# Relationships

## Builds Upon

- **Observer** — the Table Viewer is a tab of the observer application
- **Mnesia table** — it displays the rows of Mnesia tables

## Enables

- (No card depends on this concept.)

## Related

- **Observer** — the host application providing the Table Viewer

## Contrasts With

- None.

# Common Errors

- **Error**: Expecting Mnesia tables to appear in the Table Viewer by default
  **Correction**: Choose `View > Mnesia Tables` to switch from the default ETS view

# Common Confusions

- **Confusion**: Thinking the Table Viewer is a separate program
  **Clarification**: It is a tab inside the observer application, started with `observer:start()`

# Source Reference

Chapter 20: "Mnesia: The Erlang Database," section "The Table Viewer."

# Verification Notes

- Definition source: Direct quotes from "The Table Viewer"
- Confidence rationale: HIGH — the section explicitly describes how to reach and use the viewer
- Uncertainties: None
- Cross-reference status: Slugs verified against existing inventory
- Re-extraction notes: Fresh extraction; new card. Distinct from the `observer` card, which covers the application as a whole
