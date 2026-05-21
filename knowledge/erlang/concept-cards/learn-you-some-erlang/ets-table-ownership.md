---
concept: ETS Table Ownership and Heir
slug: ets-table-ownership
category: performance
subcategory: in-memory-storage
tier: intermediate
source: "Learn You Some Erlang for Great Good!"
source_slug: learn-you-some-erlang
authors: "Fred Hébert"
chapter: "Bears, ETS, Beets: In-Memory NoSQL for Free!"
chapter_number: 25
pdf_page: null
section: "The Concepts of ETS"
extraction_confidence: high
aliases:
  - "ETS table ownership"
  - "ETS heir"
  - "ETS-TRANSFER"
  - "ets:give_away"
prerequisites:
  - ets-table
  - process
extends: []
related:
  - controlling-process
contrasts_with: []
answers_questions:
  - "Who owns an ETS table?"
  - "What happens to an ETS table when its owner process dies?"
  - "How do I keep an ETS table alive past its owner?"
---

# ETS Table Ownership and Heir

## Quick Definition

An ETS table is owned by the process that created it and disappears when that process dies. Ownership can be transferred, or an heir can be designated to inherit the table on the owner's death.

## Core Definition

"When a process calls a function that starts a new ETS table, that process is the owner of the table" (Ch. 25, "The Concepts of ETS"). The table is intimately linked to its owner: "If the process dies, the table disappears (and so does all of its content)." To preserve a table, it can be given away — similar to sockets and their controlling processes — or an *heir* can be designated. If an heir is set, when the owner dies the heir receives `{'ETS-TRANSFER', TableId, FromPid, Data}` and the table is automatically inherited.

## Prerequisites

- **Ets-table** — Ownership is a property of every ETS table
- **Process** — A table is bound to the lifecycle of a process

## Key Properties

1. The process that creates a table is its owner
2. If the owner dies, the table and all its contents disappear
3. By default no heir is defined
4. An heir is set with the `{heir, Pid, Data}` option to `ets:new/2`, or changed later via `ets:setopts(Table, {heir, Pid, Data})`
5. `{heir, none}` removes the heir
6. When the owner dies, the heir receives `{'ETS-TRANSFER', TableId, FromPid, Data}` and inherits the table
7. `ets:give_away(Tab, Pid, Data)` transfers a table immediately to another process
8. Permission level (`protected`/`public`/`private`) is also tied to the owner

## Construction / Recognition

### To preserve a table past its owner

1. Set an heir at creation: `ets:new(name, [{heir, HeirPid, Data}])`
2. Or assign one later: `ets:setopts(Table, {heir, Pid, Data})`
3. The heir receives `{'ETS-TRANSFER', ...}` and the table when the owner dies

### To hand a table over deliberately

Call `ets:give_away(Tab, Pid, Data)` from the current owner.

## Context & Application

Ownership semantics mirror socket controlling processes. Designating an heir matters when the table's data should survive the owner crashing.

## Examples

**Example** (Ch. 25): The book notes that if your shell crashes while experimenting, "the tables are going to disappear, as their parent process (the shell) has disappeared" — a direct demonstration of ownership tying a table to its process.

## Relationships

### Builds Upon

- **Ets-table** — Ownership and heir are table properties
- **Process** — A table's lifetime is bound to a process

### Related

- **Controlling-process** — Socket ownership transfer is the analogous mechanism the book compares to

## Common Errors

- **Error**: Relying on a table surviving its creating process without setting an heir.
  **Correction**: A table dies with its owner; designate an heir or `give_away` it first.
- **Error**: Forgetting to handle the `{'ETS-TRANSFER', ...}` message in the heir process.
  **Correction**: The heir must be prepared to receive that message when it inherits the table.

## Common Confusions

- **Confusion**: Thinking an ETS table is global and process-independent.
  **Clarification**: It is owned by a process and disappears when that process dies, unless an heir exists.

## Source Reference

Chapter 25, "Bears, ETS, Beets: In-Memory NoSQL for Free!", sections "The Concepts of ETS" and "Creating and Deleting Tables."

## Verification Notes

- Definition: Direct adaptation from the ownership discussion
- Key Properties: All explicit in source
- Confidence: HIGH — the chapter explains ownership, heir, and `give_away` clearly
- Cross-references: `ets-table`, `controlling-process` planned/cross-chapter; `process` shared slug
