---
# === CORE IDENTIFICATION ===
concept: Mnesia Queries with QLC
slug: mnesia-query-qlc

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
section: "Database Queries"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - QLC
  - "query list comprehensions"
  - "qlc:q"
  - "qlc:e"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - mnesia
  - mnesia-table
  - mnesia-transaction
  - list-comprehension
  - record
extends:
  - list-comprehension
related:
  - mnesia-transaction
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What are query list comprehensions (QLC)?"
  - "How do I query an Mnesia database?"
  - "How do I join two Mnesia tables?"
---

# Quick Definition

QLC (query list comprehensions) is the module used to query Mnesia tables. A query is written as a list comprehension over `mnesia:table(Name)`, compiled with `qlc:q/1`, and evaluated with `qlc:e/1` inside a transaction.

# Core Definition

Mnesia queries "look a lot like both SQL and list comprehensions" because both are based on mathematical set theory ("Database Queries"). The heart of a query is the call to `qlc:q`, which compiles a list-comprehension literal into an internal form used to query the database; `qlc` "stands for query list comprehensions" and is one of the modules used to access Mnesia data. A query such as `qlc:q([X || X <- mnesia:table(shop)])` means "the list of `X` such that `X` is taken from the `shop` Mnesia table", where each `X` is a `shop` record. The compiled query `Q` is evaluated with `qlc:e(Q)` inside a transaction, which returns all answers as a list. The argument of `qlc:q/1` must be a list-comprehension literal, not a variable that evaluates to one.

# Prerequisites

- **Mnesia** — QLC queries an Mnesia database.
- **Mnesia table** — Queries draw rows from `mnesia:table(Name)`.
- **Mnesia transaction** — `qlc:e/1` must be evaluated inside a transaction.
- **List comprehension** — A QLC query is written as a list comprehension.
- **Record** — Query generators bind record-typed values; fields are accessed with `X#shop.item`.

# Key Properties

1. `qlc:q(ListComprehension)` compiles a query into an internal form.
2. The argument of `qlc:q/1` must be a literal list comprehension, not a variable holding one.
3. `mnesia:table(Name)` is used as the generator source inside the comprehension.
4. `qlc:e(Q)` evaluates a compiled query and returns all answers as a list; it is run inside a transaction fun.
5. Filters in the comprehension act as SQL `WHERE` conditions; multiple generators express joins.
6. Result rows can come out in any order.
7. Generated values are Erlang records; fields are projected with record syntax (`X#shop.item`).

# Construction / Recognition

## To Write a QLC Query:
1. Write a list comprehension over one or more `mnesia:table(Name)` generators.
2. Add filter conditions (e.g. `X#shop.quantity < 250`) as comprehension qualifiers.
3. Compile it with `qlc:q([...])`.
4. Evaluate it with `qlc:e(Q)` inside a `mnesia:transaction/1` fun.
5. Collect the resulting list of answers.

## To Recognize:
1. Look for `qlc:q([...])` wrapping a list comprehension over `mnesia:table/1`.
2. Look for `qlc:e/1` inside a transaction.

# Context & Application

QLC is how programs read data out of Mnesia.

- **Typical contexts**: Selecting all rows, projecting columns, conditional selection, and joining tables.
- **Common applications**: Reporting queries such as "list items with stock below a threshold".
- **Historical/stylistic notes**: Queries are deliberately close to SQL so SQL users have little new to learn.

# Examples

**Example 1** ("Selecting All Data in a Table"): Select every row of `shop`.

```erlang
demo(select_shop) ->
    do(qlc:q([X || X <- mnesia:table(shop)]));
```

**Example 2** ("Conditionally Selecting Data from a Table"): Items with stock below 250.

```erlang
demo(reorder) ->
    do(qlc:q([X#shop.item || X <- mnesia:table(shop),
                             X#shop.quantity < 250]));
```

## Worked Example

From "Selecting Data from Two Tables (Joins)", a join across `shop` and `cost`:

```erlang
demo(join) ->
    do(qlc:q([X#shop.item || X <- mnesia:table(shop),
                             X#shop.quantity < 250,
                             Y <- mnesia:table(cost),
                             X#shop.item =:= Y#cost.name,
                             Y#cost.price < 2
             ])).
```

The condition `X#shop.item =:= Y#cost.name` joins the two tables on item name.

# Relationships

## Builds Upon
- **List comprehension** — A QLC query is a list comprehension extended with a query source.

## Enables
- (Used by application code to read Mnesia data; no card depends on it as a prerequisite.)

## Related
- **Mnesia transaction** — `qlc:e/1` runs inside a transaction.
- **Mnesia table** — Queries iterate over tables.

## Contrasts With
- None.

# Common Errors

- **Error**: Passing a variable to `qlc:q/1` (`Var = [...], qlc:q(Var)`).
  **Correction**: The argument must be a literal list comprehension; inline the comprehension into `qlc:q/1`.

- **Error**: Evaluating `qlc:e(Q)` outside a transaction.
  **Correction**: Run `qlc:e/1` inside a `mnesia:transaction/1` fun.

# Common Confusions

- **Confusion**: Expecting query results in a fixed order.
  **Clarification**: Rows can come out in any order.

- **Confusion**: Thinking `qlc:q/1` runs the query.
  **Clarification**: `qlc:q/1` only compiles the query; `qlc:e/1` evaluates it.

# Source Reference

Chapter 20: "Mnesia: The Erlang Database", section "Database Queries" (subsections "Selecting All Data in a Table", "Choosing Data from a Table", "Conditionally Selecting Data from a Table", "Selecting Data from Two Tables (Joins)") and "The do() Function".

# Verification Notes

- Definition source: Direct quotes from "Database Queries".
- Confidence rationale: HIGH — QLC, `qlc:q/1`, and `qlc:e/1` are explicitly defined and demonstrated.
- Uncertainties: None.
- Cross-reference status: `list-comprehension` is a shared concept from earlier chapters; assumed canonical slug.
- Re-extraction notes: Fresh extraction — no pre-existing card.
