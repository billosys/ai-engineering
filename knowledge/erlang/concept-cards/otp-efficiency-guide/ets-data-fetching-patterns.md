---
concept: ETS Data Fetching Patterns
slug: ets-data-fetching-patterns
category: performance
subcategory: ets
tier: intermediate
source: "Erlang Efficiency Guide"
source_slug: otp-efficiency-guide
authors: "Ericsson/OTP Team"
chapter: "Tables and Databases"
chapter_number: null
pdf_page: null
section: "Fetching Data"
extraction_confidence: high
aliases:
  - "ETS lookup patterns"
  - "avoid redundant ETS lookups"
prerequisites:
  - ets-key-usage-and-indexing
extends: []
related:
  - ets-delete-efficiency
  - ets-tab2list-avoidance
contrasts_with: []
answers_questions:
  - "How do I avoid redundant ETS lookups?"
  - "What is the correct pattern for fetching and using ETS data?"
---

# Quick Definition

Do not fetch data from ETS that you already have. When an internal function needs data from an ETS record, pass the already-fetched record to the function rather than having each function perform its own lookup.

# Core Definition

The Efficiency Guide states (Tables and Databases chapter, "Fetching Data" section): "Do not fetch data that you already have."

The pattern involves an interface function that looks up a record from ETS once, then passes the record to internal functions that need its fields. The anti-pattern has each internal function independently looking up the same record, resulting in multiple redundant ETS lookups for the same key.

The source notes an important exception: "If the function `print_name/1`, and so on, had been interface functions, the situation would have been different, as you do not want the user of the interface to know about the internal data representation."

# Prerequisites

- **ets-key-usage-and-indexing** -- Understanding ETS lookup operations

# Key Properties

1. Fetch once from ETS, then pass the record to internal functions
2. Each redundant lookup is a separate ETS operation with associated overhead
3. The principle applies when internal functions are not part of the public interface
4. Interface functions may legitimately re-fetch data to maintain encapsulation
5. The pattern reduces ETS table contention in concurrent systems

# Construction / Recognition

## Correct Pattern

1. Perform a single `ets:lookup/2` in the interface function
2. Pass the retrieved record to all internal functions that need its data
3. Internal functions access record fields directly from the passed argument

## Anti-Pattern Recognition

Look for:
1. Multiple functions calling `ets:lookup/2` with the same key
2. Internal (non-exported) functions that each fetch the full record independently
3. Keys being passed to internal functions instead of the already-retrieved records

# Context & Application

This principle is fundamental to efficient ETS usage. Each `ets:lookup/2` involves crossing the ETS table boundary, which -- while fast -- adds up when done repeatedly for the same key. In concurrent systems, each lookup also represents a point of contention on the ETS table.

The encapsulation exception is important: public API functions should take keys (not internal records) to hide implementation details. But within a module's private implementation, passing records is more efficient.

# Examples

**DO** (Tables and Databases chapter):
```erlang
%%% Interface function
print_person(PersonId) ->
    case ets:lookup(person, PersonId) of
        [Person] ->
            print_name(Person),
            print_age(Person),
            print_occupation(Person);
        [] ->
            io:format("No person with ID = ~p~n", [PersonId])
    end.

%%% Internal functions
print_name(Person) ->
    io:format("No person ~p~n", [Person#person.name]).

print_age(Person) ->
    io:format("No person ~p~n", [Person#person.age]).

print_occupation(Person) ->
    io:format("No person ~p~n", [Person#person.occupation]).
```

**DO NOT** (Tables and Databases chapter):
```erlang
%%% Interface function
print_person(PersonId) ->
    case ets:lookup(person, PersonId) of
        [Person] ->
            print_name(PersonId),
            print_age(PersonId),
            print_occupation(PersonId);
        [] ->
            io:format("No person with ID = ~p~n", [PersonId])
    end.

%%% Internal functions
print_name(PersonId) ->
    [Person] = ets:lookup(person, PersonId),
    io:format("No person ~p~n", [Person#person.name]).

print_age(PersonId) ->
    [Person] = ets:lookup(person, PersonId),
    io:format("No person ~p~n", [Person#person.age]).

print_occupation(PersonId) ->
    [Person] = ets:lookup(person, PersonId),
    io:format("No person ~p~n", [Person#person.occupation]).
```

The DO NOT example performs 4 ETS lookups (1 in the interface + 3 in internal functions) instead of 1.

# Relationships

## Related

- **ets-delete-efficiency** -- Another pattern about avoiding unnecessary ETS operations
- **ets-tab2list-avoidance** -- Both cards address efficient data access patterns for ETS

# Common Errors

- **Error**: Passing keys to internal functions instead of the already-fetched record
  **Correction**: Pass the record itself; let internal functions access fields directly

- **Error**: Applying this optimization to interface (exported) functions
  **Correction**: Interface functions should take keys for encapsulation; the optimization applies to internal (unexported) functions

# Common Confusions

- **Confusion**: Thinking that passing records to internal functions violates encapsulation
  **Clarification**: Within a single module, internal functions already have access to the record definition; encapsulation applies at the module boundary (interface functions), not within it

- **Confusion**: Believing ETS lookups are free because ETS is in-memory
  **Clarification**: ETS lookups involve copying data from the ETS table to the process heap, which has measurable cost, especially when done repeatedly

# Source Reference

Tables and Databases chapter, "Fetching Data" section. Includes DO/DO NOT code examples with the Person record pattern and a note about the interface function exception.

# Verification Notes

- Definition: "Do not fetch data that you already have" is a direct quote
- Interface exception: Directly quoted note from the source
- Examples: Verbatim from source DO/DO NOT blocks
- Confidence: HIGH -- clear guidance with detailed code examples in official documentation
