---
concept: Mnesia Secondary Index
slug: mnesia-secondary-index
category: performance
subcategory: mnesia
tier: advanced
source: "Erlang Efficiency Guide"
source_slug: otp-efficiency-guide
authors: "Ericsson/OTP Team"
chapter: "Tables and Databases"
chapter_number: null
pdf_page: null
section: "Secondary Index"
extraction_confidence: high
aliases:
  - "Mnesia index"
  - "mnesia:index_read"
  - "mnesia:add_table_index"
prerequisites:
  - ets-key-usage-and-indexing
  - non-persistent-storage-ets-vs-mnesia
extends:
  - ets-key-usage-and-indexing
related:
  - ets-select-match-operations
  - mnesia-transactions-vs-dirty
contrasts_with:
  - ets-key-usage-and-indexing
answers_questions:
  - "How do I use Mnesia secondary indexes for efficient lookups?"
  - "What must I know before choosing between ETS and Mnesia?"
---

# Quick Definition

Mnesia supports automatic secondary indexes on non-key fields, enabling efficient lookups via `mnesia:index_read/3` instead of expensive `mnesia:select/3` or `mnesia:match_object/3` full table scans. Secondary indexes trade memory for read performance.

# Core Definition

The Efficiency Guide states (Tables and Databases chapter, "Secondary Index" section under Mnesia): "If you frequently do lookups on a field that is not the key of the table, you lose performance using `mnesia:select()` or `mnesia:match_object()` as these functions traverse the whole table. Instead, you can create a secondary index and use `mnesia:index_read/3` to get faster access at the expense of using more memory."

Secondary indexes can be defined at table creation time (via the `index` option) or added later with `mnesia:add_table_index/2`. Lookups are performed with `mnesia:index_read/3` (transactional) or `mnesia:dirty_index_read/3` (dirty).

# Prerequisites

- **ets-key-usage-and-indexing** -- Understanding single-key tables and why secondary lookups are expensive
- **non-persistent-storage-ets-vs-mnesia** -- Understanding when Mnesia is the right choice

# Key Properties

1. Secondary indexes enable efficient lookups on non-key fields
2. Without indexes, `mnesia:select/3` and `mnesia:match_object/3` traverse the whole table
3. Indexes can be specified at table creation via the `index` option
4. Indexes can be added dynamically with `mnesia:add_table_index/2`
5. Lookups use `mnesia:index_read/3` or `mnesia:dirty_index_read/3`
6. Indexes trade memory for read performance
7. Mnesia maintains indexes automatically (unlike home-brew ETS indexes)
8. The index field is specified using the record field position (e.g., `#person.age`)

# Construction / Recognition

## Creating a Table with a Secondary Index

```erlang
{atomic, ok} =
    mnesia:create_table(person,
        [{index, [#person.age]},
         {attributes, record_info(fields, person)}]).
```

## Adding an Index to an Existing Table

```erlang
{atomic, ok} = mnesia:add_table_index(person, age).
```

## Performing an Indexed Lookup

```erlang
%% Dirty (faster, no transaction):
PersonsAge42 = mnesia:dirty_index_read(person, 42, #person.age).

%% Transactional:
Fun = fun() -> mnesia:index_read(person, 42, #person.age) end,
{atomic, PersonsAge42} = mnesia:transaction(Fun).
```

# Context & Application

Mnesia secondary indexes serve the same purpose as database indexes in relational databases: they speed up queries on non-primary-key columns at the cost of additional memory and write overhead. Unlike home-brew ETS index tables (which must be manually maintained), Mnesia indexes are automatically maintained when records are inserted, updated, or deleted.

The trade-off between Mnesia automatic indexes and home-brew ETS indexes is explicit in the source: Mnesia indexes are convenient but carry Mnesia's inherent overhead; ETS index tables require manual maintenance but can be more efficient for simple non-persistent use cases.

# Examples

**Complete example** (Tables and Databases chapter, "Secondary Index" section):
```erlang
-record(person, {idno, name, age, occupation}).
        ...
{atomic, ok} =
mnesia:create_table(person, [{index,[#person.age]},
                              {attributes,
                                    record_info(fields, person)}]),
{atomic, ok} = mnesia:add_table_index(person, age),
...

PersonsAge42 =
     mnesia:dirty_index_read(person, 42, #person.age),
```

# Relationships

## Builds Upon

- **ets-key-usage-and-indexing** -- Mnesia indexes solve the same problem as ETS index tables, but automatically

## Related

- **ets-select-match-operations** -- Select/match without indexes causes full table scans
- **mnesia-transactions-vs-dirty** -- Index reads can be transactional or dirty

## Contrasts With

- **ets-key-usage-and-indexing** -- ETS indexes are manual but potentially more efficient; Mnesia indexes are automatic but carry Mnesia overhead

# Common Errors

- **Error**: Using `mnesia:select/3` or `mnesia:match_object/3` for frequent lookups on indexed fields
  **Correction**: Use `mnesia:index_read/3` or `mnesia:dirty_index_read/3` to leverage the secondary index

- **Error**: Forgetting to create the index, then wondering why `mnesia:index_read/3` fails
  **Correction**: Ensure the index is created either at table creation time (via `index` option) or with `mnesia:add_table_index/2`

# Common Confusions

- **Confusion**: Thinking Mnesia secondary indexes are free (no overhead)
  **Clarification**: Indexes use additional memory and add overhead to every write operation

- **Confusion**: Believing you can use `mnesia:index_read/3` without first creating the index
  **Clarification**: The index must be explicitly created; Mnesia does not automatically index all fields

- **Confusion**: Mixing up `mnesia:index_read/3` and `mnesia:dirty_index_read/3`
  **Clarification**: `index_read/3` must be called inside a transaction; `dirty_index_read/3` can be called outside a transaction (faster but no consistency guarantee)

# Source Reference

Tables and Databases chapter, "Secondary Index" section (under "Mnesia" heading). Includes the complete example with table creation, index addition, and dirty index read.

# Verification Notes

- Definition: Directly quoted from source text
- Code example: Verbatim from source
- Confidence: HIGH -- complete code example with explicit guidance in official documentation
