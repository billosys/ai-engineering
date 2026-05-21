---
# === CORE IDENTIFICATION ===
concept: Mnesia Dirty Operations
slug: mnesia-dirty-operations

# === CLASSIFICATION ===
category: distribution
subcategory: database
tier: advanced

# === PROVENANCE ===
source: Programming Erlang, Second Edition
source_slug: programming-erlang
authors: Joe Armstrong
chapter: "Mnesia: The Erlang Database"
chapter_number: 20
pdf_page: null
section: "Digging Deeper"

# === CONFIDENCE ===
extraction_confidence: medium

# === VARIANTS (authority control) ===
aliases:
  - "dirty_read"
  - "dirty_write"
  - "dirty operations"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - mnesia
  - mnesia-transaction
extends: []
related:
  - mnesia-table
contrasts_with:
  - mnesia-transaction

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What are Mnesia dirty operations?"
  - "When is it safe to bypass an Mnesia transaction?"
---

# Quick Definition

Mnesia dirty operations (`dirty_read`, `dirty_write`, and similar) perform reads and writes outside any transaction context. They are fast but dangerous, because they lack the atomicity and locking guarantees of transactions.

# Core Definition

"Mnesia allows a number of dirty operations (`dirty_read`, `dirty_write`, ...). These are operations that are performed outside a transaction context. They are very dangerous operations that can be used if you know that your application is single-threaded or under other special circumstances. Dirty operations are used for efficiency reasons" ("Digging Deeper"). The book mentions dirty operations only briefly as an omitted topic, presenting them as an efficiency-oriented alternative to transactional access.

# Prerequisites

- **Mnesia** — Dirty operations are an Mnesia access mechanism.
- **Mnesia transaction** — Dirty operations are defined by contrast with transactions; understanding what protections you give up requires knowing transactions.

# Key Properties

1. Performed outside any transaction context.
2. Include `dirty_read`, `dirty_write`, and other `dirty_*` functions.
3. Used purely for efficiency.
4. "Very dangerous" — they lack atomicity and locking guarantees.
5. Safe only when the application is single-threaded or under other special circumstances.

# Construction / Recognition

## To Use Dirty Operations:
1. Confirm the access pattern is single-threaded or otherwise free of concurrent contention.
2. Call the relevant `mnesia:dirty_*` function directly, without a transaction fun.
3. Accept the loss of transactional guarantees in exchange for speed.

## To Recognize:
1. Look for `mnesia:dirty_read`, `mnesia:dirty_write`, or other `dirty_*` calls not wrapped in `mnesia:transaction/1`.

# Context & Application

Dirty operations are a performance escape hatch, not a default.

- **Typical contexts**: Hot paths where transactional overhead is unacceptable and no concurrent access can occur.
- **Common applications**: Single-threaded access to a table.
- **Historical/stylistic notes**: The book deliberately omits a detailed treatment; the Mnesia User's Guide is the reference.

# Examples

The chapter provides no worked code example for dirty operations; it lists them only as an omitted topic in "Digging Deeper", naming `dirty_read` and `dirty_write` as examples of dirty operations performed outside a transaction context.

# Relationships

## Builds Upon
- **Mnesia** — Dirty operations are an alternative Mnesia access path.

## Enables
- (No card depends on this concept.)

## Related
- **Mnesia table** — Dirty operations read and write table rows.

## Contrasts With
- **Mnesia transaction** — Transactions give atomicity and pessimistic locking; dirty operations skip all of that for speed.

# Common Errors

- **Error**: Using dirty operations in a multi-process system with concurrent access to the same data.
  **Correction**: Use transactions; reserve dirty operations for single-threaded or otherwise contention-free access.

# Common Confusions

- **Confusion**: Thinking "dirty" means the data is corrupt.
  **Clarification**: "Dirty" refers to bypassing the transaction's locking and atomicity, not to data quality.

# Source Reference

Chapter 20: "Mnesia: The Erlang Database", section "Digging Deeper" (list of omitted topics).

# Verification Notes

- Definition source: Direct quote from "Digging Deeper".
- Confidence rationale: MEDIUM — the concept is explicitly named and described but only briefly, with no worked example in the chapter.
- Uncertainties: The full set of dirty functions and their exact semantics are left to the Mnesia User's Guide.
- Cross-reference status: Verified against planned cards.
- Re-extraction notes: Fresh extraction — no pre-existing card.
