---
concept: ETS tab2list Avoidance
slug: ets-tab2list-avoidance
category: performance
subcategory: ets
tier: intermediate
source: "Erlang Efficiency Guide"
source_slug: otp-efficiency-guide
authors: "Ericsson/OTP Team"
chapter: "Tables and Databases"
chapter_number: null
pdf_page: null
section: "tab2list"
extraction_confidence: high
aliases:
  - "ets:tab2list anti-pattern"
  - "tab2list vs select"
prerequisites:
  - ets-select-match-operations
extends:
  - ets-select-match-operations
related:
  - ets-key-usage-and-indexing
  - ets-data-fetching-patterns
contrasts_with: []
answers_questions:
  - "How does `ets:select/2` compare to `ets:tab2list/1` for data retrieval?"
  - "How do I use `ets:select/2` instead of `ets:tab2list/1`?"
---

# Quick Definition

Using `ets:tab2list/1` to extract all table data and then filtering with list operations is expensive and should be replaced with `ets:select/2`, which filters data within the ETS engine without copying the entire table to the process heap.

# Core Definition

The Efficiency Guide states (Tables and Databases chapter, "tab2list" section): "If you _must_ return all data stored in the Ets table, you can use `ets:tab2list/1`. However, usually you are only interested in a subset of the information in which case `ets:tab2list/1` is expensive."

The section provides three concrete scenarios showing how `ets:select/2` replaces `ets:tab2list/1` plus list processing:

1. Extracting a single field from all records
2. Extracting a field from records matching a condition on another field
3. Extracting full records matching a condition

In all cases, `ets:select/2` performs the filtering inside the ETS engine, avoiding copying unneeded data to the process heap.

# Prerequisites

- **ets-select-match-operations** -- Understanding how `ets:select/2` and match specifications work

# Key Properties

1. `ets:tab2list/1` copies the entire table to the process heap
2. `ets:select/2` filters within the ETS engine, copying only matching data
3. Match specifications allow field extraction (projecting specific fields)
4. Match specifications allow filtering (selecting records by field values)
5. `ets:select/2` combines projection and filtering in a single operation
6. `ets:tab2list/1` is only appropriate when all data is genuinely needed
7. Use `'$1'` in the result part of a match spec to project a single field
8. Use `'$_'` in the result part to return the full matching record

# Construction / Recognition

## Replacing tab2list with select

### Extract a single field from all records

```erlang
%% DO: Extract age from all persons
ets:select(Tab, [{#person{idno='_', name='_', age='$1', occupation='_'},
                  [],
                  ['$1']}]).

%% DO NOT:
TabList = ets:tab2list(Tab),
lists:map(fun(X) -> X#person.age end, TabList).
```

### Extract a field with a filter condition

```erlang
%% DO: Extract age of all persons named "Bryan"
ets:select(Tab, [{#person{idno='_', name="Bryan", age='$1', occupation='_'},
                  [],
                  ['$1']}]).

%% DO NOT:
TabList = ets:tab2list(Tab),
lists:foldl(fun(X, Acc) ->
    case X#person.name of
        "Bryan" -> [X#person.age|Acc];
        _ -> Acc
    end
end, [], TabList).
```

### Extract full records with a filter condition

```erlang
%% DO: Get all person records named "Bryan"
ets:select(Tab, [{#person{idno='_', name="Bryan", age='_', occupation='_'},
                  [],
                  ['$_']}]).

%% DO NOT:
TabList = ets:tab2list(Tab),
lists:filter(fun(X) -> X#person.name == "Bryan" end, TabList).
```

# Context & Application

The `ets:tab2list/1` anti-pattern is one of the most common ETS performance mistakes in Erlang applications. The fundamental issue is that `tab2list` copies every record from the ETS table (which lives outside the process heap) into the calling process's heap, regardless of how much data is actually needed. For large tables, this can cause significant memory pressure and garbage collection overhead.

`ets:select/2` performs the filtering and projection inside the ETS engine, only copying the relevant results to the process heap. This is analogous to the difference between `SELECT * FROM table` followed by client-side filtering versus `SELECT age FROM table WHERE name = 'Bryan'` in SQL.

# Examples

All three DO/DO NOT examples above are from the Tables and Databases chapter, "tab2list" section. They use a person table:

```text
[#person{idno = 1, name = "Adam",  age = 31, occupation = "mailman"},
 #person{idno = 2, name = "Bryan", age = 31, occupation = "cashier"},
 #person{idno = 3, name = "Bryan", age = 35, occupation = "banker"},
 #person{idno = 4, name = "Carl",  age = 25, occupation = "mailman"}]
```

# Relationships

## Builds Upon

- **ets-select-match-operations** -- `ets:select/2` is the preferred alternative to `tab2list`

## Related

- **ets-key-usage-and-indexing** -- Key lookups are even faster than select; use them when possible
- **ets-data-fetching-patterns** -- Both cards address efficient ETS data access

# Common Errors

- **Error**: Using `ets:tab2list/1` followed by `lists:map/2` to extract a single field
  **Correction**: Use `ets:select/2` with a match specification that projects the desired field

- **Error**: Using `ets:tab2list/1` followed by `lists:filter/2` to select matching records
  **Correction**: Use `ets:select/2` with a match specification that includes the filter condition

- **Error**: Using `ets:tab2list/1` followed by `lists:foldl/3` for combined filter-and-project
  **Correction**: Use `ets:select/2` with a match specification that does both in one operation

# Common Confusions

- **Confusion**: Thinking `ets:select/2` is just syntactic sugar for `tab2list` + filtering
  **Clarification**: `ets:select/2` performs filtering inside the ETS engine, avoiding the cost of copying all records to the process heap

- **Confusion**: Believing `ets:tab2list/1` is acceptable for small tables
  **Clarification**: While the cost is lower for small tables, `ets:select/2` is still more efficient and should be the default choice; only use `tab2list` when genuinely all data is needed

# Source Reference

Tables and Databases chapter, "tab2list" section. Includes three complete DO/DO NOT code example pairs and the sample data table.

# Verification Notes

- Definition: Directly quoted from source text
- All three example pairs: Verbatim from source DO/DO NOT blocks
- Sample data: Directly from source
- Confidence: HIGH -- detailed examples with clear anti-patterns in official documentation
