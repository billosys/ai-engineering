---
concept: ETS Key Usage and Indexing
slug: ets-key-usage-and-indexing
category: performance
subcategory: ets
tier: intermediate
source: "Erlang Efficiency Guide"
source_slug: otp-efficiency-guide
authors: "Ericsson/OTP Team"
chapter: "Tables and Databases"
chapter_number: null
pdf_page: null
section: "Using Keys of Ets Table"
extraction_confidence: high
aliases:
  - "ETS key lookup"
  - "ETS index table"
  - "ETS secondary index"
prerequisites:
  - ets-delete-efficiency
extends: []
related:
  - ets-select-match-operations
  - ets-tab2list-avoidance
  - mnesia-secondary-index
  - ordered-set-tables
contrasts_with: []
answers_questions:
  - "How do I create an index table for efficient ETS lookups on non-key fields?"
  - "What must I know before choosing between ETS and Mnesia?"
---

# Quick Definition

ETS is a single-key table (hash or tree). Key lookups are O(1) for `set` and O(log N) for `ordered_set`. For lookups on non-key fields, create a secondary index table (a `bag` mapping the secondary field to the primary key) to avoid full table scans.

# Core Definition

The Efficiency Guide states (Tables and Databases chapter, "Using Keys of Ets Table" section): "An Ets table is a single-key table (either a hash table or a tree ordered by the key) and is to be used as one. In other words, use the key to look up things whenever possible."

Performance characteristics:
- Key lookup in a `set` table: constant time
- Key lookup in an `ordered_set` table: O(log N)
- "A key lookup is always preferable to a call where the whole table has to be scanned"

For non-key field lookups, the source recommends creating a secondary index table: "A more general solution would be to create a second table with `name` as key and `idno` as data, that is, to index (invert) the table regarding the `name` field."

The index table must be a `bag` (since the secondary key may not be unique) and must be kept consistent with the master table. The source notes: "Mnesia can do this for you, but a home-brew index table can be very efficient compared to the overhead involved in using Mnesia."

# Prerequisites

- **ets-delete-efficiency** -- Basic understanding of ETS table operations

# Key Properties

1. ETS tables have a single primary key
2. `set` tables use hash-based O(1) key lookup
3. `ordered_set` tables use tree-based O(log N) key lookup
4. Key lookups are always preferable to table scans
5. Non-key field lookups require a full table scan without an index
6. Secondary index tables should be `bag` type (non-unique secondary keys)
7. Index tables must be manually kept consistent with the master table
8. Home-brew index tables can be more efficient than Mnesia's automatic indexes
9. The index table pattern uses `ets:lookup/2` on the index, then `ets:lookup/2` on the master for each match

# Construction / Recognition

## Creating a Secondary Index Table

1. Define an index record: `#index_entry{name, idno}` (secondary field as key, primary key as data)
2. Create the index table as a `bag`: `ets:new(name_index, [bag, {keypos, #index_entry.name}])`
3. When inserting into the master table, also insert into the index table
4. When deleting from the master table, also delete from the index table

## Using the Index Table for Lookups

```erlang
%% Look up all persons named "Bryan":
MatchingIDs = ets:lookup(IndexTable, "Bryan"),
lists:map(fun(#index_entry{idno = ID}) ->
               [#person{age = Age}] = ets:lookup(PersonTable, ID),
               Age
          end,
          MatchingIDs).
```

# Context & Application

This pattern is the ETS equivalent of database indexing. Unlike relational databases where indexes are maintained automatically, ETS index tables must be manually maintained. This manual maintenance introduces complexity but avoids the overhead of Mnesia's automatic index management.

The trade-off is explicit: "Keeping an index table introduces some overhead when inserting records in the table. The number of operations gained from the table must therefore be compared against the number of operations inserting objects in the table."

The pattern is especially valuable for read-heavy workloads where non-key field lookups are frequent but writes are relatively rare.

# Examples

**Index table contents** (Tables and Databases chapter):
```text
[#index_entry{name="Adam", idno=1},
 #index_entry{name="Bryan", idno=2},
 #index_entry{name="Bryan", idno=3},
 #index_entry{name="Carl", idno=4}]
```

**Index-based lookup** (Tables and Databases chapter):
```erlang
MatchingIDs = ets:lookup(IndexTable, "Bryan"),
lists:map(fun(#index_entry{idno = ID}) ->
               [#person{age = Age}] = ets:lookup(PersonTable, ID),
               Age
          end,
          MatchingIDs).
```

The source notes: "this code does not use `ets:match/2`, but instead uses the `ets:lookup/2` call. The `lists:map/2` call is only used to traverse the `idno`s matching the name 'Bryan' in the table; thus the number of lookups in the master table is minimized."

# Relationships

## Related

- **ets-select-match-operations** -- Select/match is the alternative when indexes are not available
- **ets-tab2list-avoidance** -- Both cards address avoiding full table scans
- **mnesia-secondary-index** -- Mnesia provides automatic secondary indexes as an alternative
- **ordered-set-tables** -- Ordered set tables provide partial key optimization

## Contrasts With

- **mnesia-secondary-index** -- Mnesia maintains indexes automatically but with overhead; home-brew ETS indexes are manual but more efficient

# Common Errors

- **Error**: Using `ets:match/2` for index lookups instead of `ets:lookup/2`
  **Correction**: Use `ets:lookup/2` on the index table; it is a direct key lookup, not a table scan

- **Error**: Forgetting to maintain the index table when inserting or deleting from the master table
  **Correction**: Every insert/delete on the master table must have a corresponding insert/delete on the index table

- **Error**: Using a `set` type for the index table when the secondary key is not unique
  **Correction**: Use a `bag` type so multiple entries with the same secondary key can coexist

# Common Confusions

- **Confusion**: Thinking ETS tables support multiple indexes natively
  **Clarification**: ETS tables have a single key; additional indexes must be implemented as separate tables

- **Confusion**: Believing Mnesia automatic indexes are always better than home-brew ETS indexes
  **Clarification**: The source states "a home-brew index table can be very efficient compared to the overhead involved in using Mnesia"

- **Confusion**: Thinking the index table overhead is always worth it
  **Clarification**: The gain from faster reads must be weighed against the overhead of maintaining the index on writes

# Source Reference

Tables and Databases chapter, "Using Keys of Ets Table" section (under "ETS" heading). Includes the index table example with the person/index_entry records, the lookup code, and the trade-off discussion.

# Verification Notes

- Definition: Directly extracted from source text
- Performance characteristics: O(1) for set, O(log N) for ordered_set explicitly stated
- Index pattern: Complete code example from source
- Trade-off discussion: Directly quoted from source
- Mnesia comparison: Directly quoted from source
- Confidence: HIGH -- detailed implementation pattern with code examples in official documentation
