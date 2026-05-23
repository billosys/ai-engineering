---
concept: Match Specification ETS Usage
slug: match-spec-ets
category: performance
subcategory: ets
tier: intermediate
source: "ERTS User's Guide"
source_slug: otp-erts
authors: "Ericsson AB"
chapter: "Match Specifications in Erlang"
chapter_number: null
pdf_page: null
section: "Differences between Match Specifications in ETS and Tracing"
extraction_confidence: high
aliases:
  - "ETS match spec"
  - "ets:select match specification"
prerequisites:
  - match-specification
extends:
  - match-specification
related:
  - match-spec-tracing
contrasts_with:
  - match-spec-tracing
answers_questions:
  - "How do match specifications relate to ETS and tracing?"
  - "How do I write a match specification for ETS?"
  - "What is the difference between ETS and tracing match specifications?"
---

# Quick Definition

In ETS, match specifications are used with `ets:select/2` and related functions to query table objects with complex conditions and return transformed results. The MatchHead matches against tuples `{Key, Value1, ...}`, the MatchBody produces a return value (not side effects), and side-effect functions are not allowed.

# Core Definition

ETS match specifications produce a return value from the MatchBody. Usually the MatchBody contains a single `ConditionExpression` defining the return value without side effects. "Calls with side effects are not allowed in the ETS context" (Ericsson AB, "Match Specifications in Erlang," section "Differences between Match Specifications in ETS and Tracing").

Key differences from tracing match specifications:

- The match target is always a full table tuple `{Key, Value1, Value2, ...}`
- The MatchHead must be a tuple (not a list as in tracing)
- The MatchBody evaluates expressions in order and returns the value of the last expression
- Action functions like `return_trace`, `caller`, `message`, `enable_trace`, etc. are not available
- The grammar does not include `is_seq_trace` or trace-specific boolean functions

Efficient ETS queries place key constraints in the MatchHead rather than MatchConditions, because "the search space of the tables is restricted with regards to the MatchHead so that only objects with the matching key are searched" (source: section "ETS Examples").

# Prerequisites

- **match-specification** -- Understanding the base match specification grammar, variables, and literal handling

# Key Properties

1. The match target is always a full ETS table tuple: `{Key, Value1, Value2, ...}`
2. The MatchBody produces a return value, typically a single expression
3. No side-effect functions are allowed
4. `'$_'` returns the whole matched object; `'$$'` returns all bound variable values as a list
5. Key matching in MatchHead restricts the search space -- much more efficient than key tests in MatchConditions
6. `ets:test_ms/2` can be used to test and debug complicated match specifications
7. Multiple match functions in the list act as alternatives (like multiple function clauses)

# Construction / Recognition

## Building an ETS Match Specification

1. Define the MatchHead as a tuple matching the table's record structure
2. Use `'_'` for fields you don't care about
3. Use `'$N'` variables for fields you need to test or return
4. Add MatchConditions for guard-like tests
5. Specify the MatchBody to define what to return: `['$_']` for the whole object, `['$$']` for all bound values, or a custom expression

## Testing Match Specifications

Use `ets:test_ms/2` to validate match specifications against sample tuples before deploying them on real tables.

# Context & Application

ETS match specifications are the most powerful query mechanism for ETS tables, offering capabilities beyond `ets:match/2` and `ets:lookup/2`:

- Complex multi-field conditions with boolean logic
- Computed return values (not just raw matched objects)
- Multiple alternative match clauses
- Guard-style arithmetic and comparison tests

They are used whenever simple key lookup or basic pattern matching is insufficient, such as range queries, multi-condition filtering, or returning projections of table objects.

# Examples

**Match all objects where first element is 'strider' with arity 3, return whole object** (source: "Match Specifications in Erlang," section "ETS Examples"):

```erlang
[{{strider,'_','_'},
  [],
  ['$_']}]
```

**Match objects with arity >= 2 where first element is 'gandalf', return element 2** (source: same section):

```erlang
[{'$1',
  [{'==', gandalf, {element, 1, '$1'}},{'>=',{size, '$1'},2}],
  [{element,2,'$1'}]}]
```

Note from source: "if the first element had been the key, it is much more efficient to match that key in the MatchHead part than in the MatchConditions part."

**Match tuples of three where second element is 'merry' or 'pippin', return whole objects** (source: same section):

```erlang
[{{'_',merry,'_'},
  [],
  ['$_']},
 {{'_',pippin,'_'},
  [],
  ['$_']}]
```

This uses multiple match functions as alternatives, similar to multiple function clauses.

# Relationships

## Extends

- **match-specification** -- ETS match specifications use the base grammar without tracing action functions

## Contrasts With

- **match-spec-tracing** -- Tracing match specifications execute MatchBody for side effects and have additional action functions; ETS match specifications produce return values and forbid side effects

# Common Errors

- **Error**: Placing key conditions in MatchConditions instead of MatchHead
  **Correction**: Match the key in MatchHead to restrict the search space; placing key tests in MatchConditions forces a full table scan

- **Error**: Using tracing-only functions like `return_trace` or `caller` in an ETS match specification
  **Correction**: These functions are not available in the ETS context; the ETS grammar only supports guard functions and condition expressions

- **Error**: Forgetting to wrap the MatchBody return expression in a list
  **Correction**: The MatchBody must be a list of expressions: `['$_']` not `'$_'`

# Common Confusions

- **Confusion**: `ets:match/2` and `ets:select/2` with match specifications are the same
  **Clarification**: `ets:match/2` uses simpler match patterns that can only bind variables and return them; `ets:select/2` with match specifications supports conditions, computed return values, and boolean logic

- **Confusion**: The MatchHead for ETS uses a list like tracing
  **Clarification**: ETS MatchHead must be a tuple matching the table object structure `{Key, Val1, ...}`, while tracing uses a list matching function arguments `[Arg1, Arg2, ...]`

# Source Reference

"Match Specifications in Erlang," sections "Differences between Match Specifications in ETS and Tracing," "ETS Examples," and the ETS-specific grammar. The source provides the complete ETS grammar variant, three ETS examples, and an explicit note about search space optimization when matching keys in the MatchHead. The source also mentions `ets:test_ms/2` as a useful testing tool.

# Verification Notes

- No side effects rule: Directly stated -- "Calls with side effects are not allowed in the ETS context"
- Search space optimization: Directly stated -- "The search space of the tables is restricted with regards to the MatchHead"
- ets:test_ms/2 recommendation: Directly from source -- "Function ets:test_ms/2 can be useful for testing complicated ETS matches"
- All examples: Verbatim from source "ETS Examples" section
- Grammar differences: Explicitly shown in source with separate grammar sections for tracing and ETS
- Confidence: HIGH -- all content directly from official ERTS documentation
