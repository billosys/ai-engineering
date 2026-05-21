---
# === CORE IDENTIFICATION ===
concept: Aborting an Mnesia Transaction
slug: mnesia-transaction-abort

# === CLASSIFICATION ===
category: distribution
subcategory: database
tier: intermediate

# === PROVENANCE ===
source: Programming Erlang, Second Edition
source_slug: programming-erlang
authors: Joe Armstrong
chapter: "Mnesia: The Erlang Database"
chapter_number: 20
pdf_page: null
section: "Aborting a Transaction"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "mnesia:abort/1"
  - "transaction rollback"
  - "transaction abort"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - mnesia
  - mnesia-transaction
extends:
  - mnesia-transaction
related:
  - mnesia-table
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do I abort an Mnesia transaction?"
  - "What happens to database changes when a transaction is aborted?"
---

# Quick Definition

Aborting an Mnesia transaction with `mnesia:abort(Reason)` cancels it and undoes every change made so far inside the transaction fun, restoring the database to its pre-transaction state. The transaction call then returns `{aborted, Reason}`.

# Core Definition

A transaction can be deliberately aborted from inside its fun by calling `mnesia:abort(Reason)` ("Aborting a Transaction"). "When the transaction failed (when we called `mnesia:abort(Reason)`), the changes made by `mnesia:write` were undone. Because of this, the database state was restored to how it was before we entered the transaction." This is the atomicity guarantee in action: even writes performed earlier in the same transaction fun are rolled back. An aborted transaction makes `mnesia:transaction/1` return `{aborted, Reason}` rather than `{atomic, Val}`.

# Prerequisites

- **Mnesia** — Aborting is a transaction-control operation in an Mnesia database
- **Mnesia transaction** — An abort only makes sense within a running transaction; it relies on the transaction's atomicity to undo changes

# Key Properties

1. Triggered explicitly by `mnesia:abort(Reason)` inside the transaction fun
2. Undoes all changes made so far in the transaction, including earlier writes
3. Restores the database to its exact pre-transaction state
4. Causes `mnesia:transaction/1` to return `{aborted, Reason}`
5. Used to express a business-rule failure (e.g. insufficient stock)
6. Transactions also abort automatically on errors or detected deadlock

# Construction / Recognition

## To Abort a Transaction:

1. Inside the transaction fun, check the condition that must hold
2. If the condition fails, call `mnesia:abort(Reason)` with a descriptive reason
3. The transaction unwinds; all writes made so far are undone
4. Match `{aborted, Reason}` from `mnesia:transaction/1` in the caller

## To Recognize:

1. Look for `mnesia:abort/1` inside a transaction fun
2. Look for `{aborted, _}` result handling

# Context & Application

- **Typical contexts**: Enforcing invariants inside a transaction — rejecting an update when a business rule is violated
- **Common applications**: Stock checks, balance checks, validation failures that must leave the database untouched
- **Historical/stylistic notes**: The book's `farmer/1` example deliberately writes the updated apple count *before* checking the orange count, to demonstrate that the write is undone when the transaction aborts

# Examples

**Example 1** (section "Aborting a Transaction"): The `farmer/1` function aborts when there are not enough oranges.

```erlang
if
    NOranges >= Nwant ->
        N1 = NOranges - Nwant,
        Orange1 = Orange#shop{quantity=N1},
        mnesia:write(Orange1);
    true ->
        %% Oops -- not enough oranges
        mnesia:abort(oranges)
end
```

**Example 2** (section "Aborting a Transaction"): Calling `test_mnesia:farmer(100)` when stock is too low returns `{aborted,oranges}`, and a subsequent `select_shop` shows the apple count unchanged — the earlier `mnesia:write` of the apple count was undone.

# Relationships

## Builds Upon

- **Mnesia transaction** — Aborting is a control operation within a transaction; it depends on transactional atomicity to roll back

## Enables

- (No card depends on this concept.)

## Related

- **Mnesia table** — Aborting restores the rows the transaction had modified

## Contrasts With

- None.

# Common Errors

- **Error**: Performing irreversible side effects in the transaction fun, expecting `abort` to undo them
  **Correction**: `mnesia:abort/1` undoes only database changes; external side effects (files, messages) are not rolled back

- **Error**: Catching the exception that `mnesia:abort/1` raises
  **Correction**: Do not catch exceptions thrown by Mnesia access functions — the transaction mechanism relies on them

# Common Confusions

- **Confusion**: Believing earlier writes in the same transaction survive an abort
  **Clarification**: All changes within the transaction are undone, including writes performed before the `abort` call

# Source Reference

Chapter 20: "Mnesia: The Erlang Database," section "Mnesia Transactions," subsection "Aborting a Transaction." See the `farmer/1` worked example.

# Verification Notes

- Definition source: Direct quotes from "Aborting a Transaction"
- Confidence rationale: HIGH — abort behavior and rollback are explicitly demonstrated with the farmer example
- Uncertainties: None
- Cross-reference status: Slugs verified against existing inventory
- Re-extraction notes: Fresh extraction; new card
