---
concept: ETS Delete Efficiency
slug: ets-delete-efficiency
category: data-structures
subcategory: ets
tier: foundational
source: "Erlang Efficiency Guide"
source_slug: otp-efficiency-guide
authors: "Ericsson/OTP Team"
chapter: "Tables and Databases"
chapter_number: null
pdf_page: null
section: "Deleting an Element"
extraction_confidence: high
aliases:
  - "ets:delete efficiency"
  - "ETS delete pattern"
prerequisites: []
extends: []
related:
  - ets-data-fetching-patterns
  - ets-key-usage-and-indexing
contrasts_with: []
answers_questions:
  - "How should I delete elements from ETS tables efficiently?"
---

# Quick Definition

The `ets:delete/2` operation succeeds whether or not the element exists in the table. Pre-checking for existence before deletion is unnecessary and wasteful.

# Core Definition

The Efficiency Guide states (Tables and Databases chapter, "Deleting an Element" section): "The `delete` operation is considered successful if the element was not present in the table. Hence all attempts to check that the element is present in the Ets/Mnesia table before deletion are unnecessary."

This is a simple but commonly violated efficiency principle: do not perform a lookup before a delete, as the delete is idempotent.

# Prerequisites

This is a foundational concept with no prerequisites within this source.

# Key Properties

1. `ets:delete/2` succeeds even if the key does not exist in the table
2. Pre-checking with `ets:lookup/2` before deletion is unnecessary
3. The anti-pattern involves two ETS operations (lookup + conditional delete) instead of one
4. The same principle applies to Mnesia delete operations

# Construction / Recognition

## Correct Delete Pattern

1. Call `ets:delete(Tab, Key)` directly
2. Do not wrap it in a lookup check

## Recognizing the Anti-Pattern

Look for code that:
1. Calls `ets:lookup/2` first
2. Checks if the result is empty
3. Only calls `ets:delete/2` if the element exists

# Context & Application

This is a common pattern in database programming across many languages and systems. ETS delete is idempotent by design -- it is safe to delete a key that does not exist. The overhead of a redundant lookup is especially significant in high-throughput systems where ETS operations are on the hot path.

# Examples

**DO** (Tables and Databases chapter):
```erlang
ets:delete(Tab, Key),
```

**DO NOT** (Tables and Databases chapter):
```erlang
case ets:lookup(Tab, Key) of
    [] ->
        ok;
    [_|_] ->
        ets:delete(Tab, Key)
end,
```

# Relationships

## Related

- **ets-data-fetching-patterns** -- Another pattern about avoiding unnecessary ETS operations
- **ets-key-usage-and-indexing** -- Key-based operations like delete are the most efficient ETS operations

# Common Errors

- **Error**: Checking if an element exists before deleting it
  **Correction**: Call `ets:delete/2` directly; it is a no-op if the key does not exist

# Common Confusions

- **Confusion**: Thinking `ets:delete/2` raises an error if the key is not found
  **Clarification**: `ets:delete/2` always succeeds; it is considered successful even when the element was not present

# Source Reference

Tables and Databases chapter, "Deleting an Element" section. Includes DO/DO NOT code examples demonstrating the correct and incorrect patterns.

# Verification Notes

- Definition: Directly quoted from source text
- Examples: Verbatim from source DO/DO NOT blocks
- Confidence: HIGH -- simple, unambiguous guidance with clear code examples in official documentation
