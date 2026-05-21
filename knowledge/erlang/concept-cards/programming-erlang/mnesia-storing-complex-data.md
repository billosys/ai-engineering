---
# === CORE IDENTIFICATION ===
concept: Storing Complex Data in Mnesia Tables
slug: mnesia-storing-complex-data

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
section: "Storing Complex Data in Tables"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "no impedance mismatch"
  - "storing Erlang terms"
  - "complex objects in Mnesia"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - mnesia
  - mnesia-table
  - record
extends:
  - mnesia-table
related:
  - mnesia-transaction
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "Can Mnesia store arbitrary Erlang data structures?"
  - "What is impedance mismatch and why does Mnesia avoid it?"
---

# Quick Definition

Mnesia can store any Erlang data structure in a table column — arbitrarily nested tuples, lists, and records — and even use an arbitrary term as a key. Because database and program data have the same form, there is no impedance mismatch.

# Core Definition

"Mnesia is designed to store Erlang data structures. In fact, you can store any Erlang data structure you want in an Mnesia table" ("Storing Complex Data in Tables"). A conventional DBMS limits a column to a small set of types (integer, string, float), making it messy to store a complex object. Mnesia has no such restriction: "both the database key and the extracted record can be arbitrary Erlang terms." Armstrong names this property the absence of *impedance mismatch* — "there is no impedance mismatch between the data structures in the database and the data structures in our programming language. This means that inserting and deleting complex data structures into the database is very fast."

# Prerequisites

- **Mnesia** — This property is a defining feature of the Mnesia database
- **Mnesia table** — Complex data is stored as rows (records) in a table
- **Record** — Table rows are records; a field can hold an arbitrarily complex term

# Key Properties

1. Any Erlang term can be stored as a column value — nested tuples, lists, records
2. Keys may also be arbitrary Erlang terms, not just simple scalars
3. No impedance mismatch between database data and in-program data
4. Inserting and extracting complex structures is very fast — no serialization translation
5. Contrasts with conventional DBMSs limited to a fixed set of column types

# Construction / Recognition

## To Store Complex Data:

1. Define a record whose fields can hold complex terms, e.g. `-record(design, {id, plan})`
2. Build records whose fields contain arbitrarily nested terms
3. Write them inside a transaction with `mnesia:write/1`
4. Read them back with `mnesia:read({Table, Key})` inside a transaction — the term is returned intact

## To Recognize:

1. Mnesia records whose fields hold nested tuples/lists rather than flat scalars
2. Non-scalar keys such as `{joe,1}` or `{jane,{house,23}}`

# Context & Application

- **Typical contexts**: Storing domain objects that do not fit a flat relational schema — configurations, plans, tree-structured data
- **Common applications**: The book's example stores architects' building designs as deeply nested terms keyed by arbitrary terms
- **Historical/stylistic notes**: Storing a Java object in a SQL database is "pretty messy"; Mnesia avoids that because it stores native Erlang terms directly

# Examples

**Example 1** (section "Storing Complex Data in Tables"): A `design` record whose `plan` field holds a deeply nested term, and whose key is itself a compound term.

```erlang
-record(design, {id, plan}).

D3 = #design{id   = {jane,{house,23}},
             plan = {house,
                     [{floor,1,[{doors,3},{windows,12},{rooms,5}]},
                      {floor,2,[{doors,2},{rooms,4},{windows,15}]}]}}.
```

**Example 2** (section "Storing Complex Data in Tables"): Reading a plan back returns the full nested structure intact.

```erlang
get_plan(PlanId) ->
    F = fun() -> mnesia:read({design, PlanId}) end,
    mnesia:transaction(F).
%% test_mnesia:get_plan(fred) => {atomic,[{design,fred,{rectangle,10,5}}]}
```

# Relationships

## Builds Upon

- **Mnesia table** — Complex data is stored as rows of a table
- **Record** — Rows are records whose fields can hold any term

## Enables

- (No card depends on this concept.)

## Related

- **Mnesia transaction** — Writes and reads of complex data happen inside transactions

## Contrasts With

- None — this contrasts with conventional SQL DBMSs generally, not with another Erlang concept

# Common Errors

- **Error**: Flattening or serializing complex data before storing it in Mnesia
  **Correction**: Store the Erlang term directly; Mnesia keeps it as-is and returns it intact

# Common Confusions

- **Confusion**: Thinking Mnesia columns are typed like SQL columns
  **Clarification**: An Mnesia column holds any Erlang term; there is no fixed column type system

- **Confusion**: Assuming compound keys are unsupported
  **Clarification**: The primary key may be an arbitrary Erlang term, such as `{jane,{house,23}}`

# Source Reference

Chapter 20: "Mnesia: The Erlang Database," section "Storing Complex Data in Tables." See the `design` record, `add_plans/0`, and `get_plan/1`.

# Verification Notes

- Definition source: Direct quotes from "Storing Complex Data in Tables"
- Confidence rationale: HIGH — explicitly defined with the impedance-mismatch discussion and worked examples
- Uncertainties: None
- Cross-reference status: Slugs verified against existing inventory
- Re-extraction notes: Fresh extraction; new card
