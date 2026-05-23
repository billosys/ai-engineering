---
concept: Match Specification
slug: match-specification
category: performance
subcategory: ets-tracing
tier: intermediate
source: "ERTS User's Guide"
source_slug: otp-erts
authors: "Ericsson AB"
chapter: "Match Specifications in Erlang"
chapter_number: null
pdf_page: null
section: "Grammar"
extraction_confidence: high
aliases:
  - match_spec
  - "match spec"
  - "match expression"
prerequisites: []
extends: []
related:
  - match-spec-tracing
  - match-spec-ets
contrasts_with: []
answers_questions:
  - "What is a match specification?"
  - "How do match specifications relate to ETS and tracing?"
  - "How do I write a match specification?"
---

# Quick Definition

A match specification (`match_spec`) is an Erlang term describing a small "program" that tries to match something. It is used to control tracing with `trace:function/4` or to search for objects in an ETS table with `ets:select/2`. The runtime system compiles it into something much more efficient than calling an Erlang function.

# Core Definition

A match specification is a list of match functions, where each match function is a three-element tuple `{MatchHead, MatchConditions, MatchBody}`. The MatchHead binds variables against a match target, MatchConditions act like guards (returning `true` or failing), and MatchBody defines actions or return values. The match specification works like a small function in Erlang but is "interpreted/compiled by the Erlang runtime system to something much more efficient than calling an Erlang function" (Ericsson AB, "Match Specifications in Erlang"). It is also much more limited than real Erlang functions.

Match specifications have a distinctive exception model: an exception in the MatchCondition part (which resembles an Erlang guard) generates immediate failure, while an exception in the MatchBody part (which resembles a function body) is implicitly caught and results in the atom `'EXIT'`.

# Prerequisites

- Basic understanding of Erlang pattern matching and guards
- Familiarity with ETS tables or the tracing subsystem (depending on use case)

# Key Properties

1. A match specification is a list of match function tuples: `[{MatchHead, MatchConditions, MatchBody}, ...]`
2. Variables use the form `'$<number>'` (e.g., `'$1'`, `'$2'`), where the number must be between 0 and 100,000,000
3. The special variable `'_'` matches anything and never binds (like `_` in Erlang)
4. `'$_'` expands to the whole match target term; `'$$'` expands to a list of all bound variable values in order
5. MatchConditions work like Erlang guards -- they must evaluate to `true` or the match fails
6. MatchBody semantics differ between ETS (returns a value) and tracing (executes for side effects)
7. Literals in MatchCondition/MatchBody must use double-tuple `{{...}}` or `{const, T}` syntax for tuple values
8. The grammar for tracing and ETS differs: tracing allows action functions (e.g., `return_trace`, `caller`); ETS does not

# Construction / Recognition

## Grammar Structure

```
MatchExpression ::= [ MatchFunction, ... ]
MatchFunction   ::= { MatchHead, MatchConditions, MatchBody }
```

The MatchHead for tracing is a list (matching function arguments): `[Arg1, Arg2, ...]`
The MatchHead for ETS is a tuple (matching table objects): `{Key, Val1, Val2, ...}`

## Building a Match Specification

1. Define the MatchHead to bind variables against the match target
2. Add MatchConditions as guard-like tests on bound variables
3. Specify the MatchBody for return values (ETS) or side effects (tracing)
4. Wrap in a list to form the complete match expression

## Guard and Boolean Functions Available

Both contexts support: `is_atom`, `is_float`, `is_integer`, `is_list`, `is_number`, `is_pid`, `is_port`, `is_reference`, `is_tuple`, `is_map`, `is_binary`, `is_function`, `'and'`, `'or'`, `'not'`, `'xor'`, `'andalso'`, `'orelse'`, plus arithmetic/comparison operators and BIFs like `abs`, `element`, `hd`, `length`, `tl`, `tuple_size`, `map_get`, `self`, etc.

# Context & Application

Match specifications are central to two major Erlang subsystems:

- **ETS**: Used with `ets:select/2` and related functions to efficiently query table contents with complex conditions, returning transformed results. Much more powerful than `ets:match/2` alone.
- **Tracing**: Used with `trace:function/4` to control which function calls generate trace messages and what additional information to include. Enables fine-grained filtering without the overhead of a trace handler function.

The match target format depends on context:

| Context | Type      | Match target               |
| ------- | --------- | -------------------------- |
| ETS     |           | `{Key, Value1, Value2, ...}` |
| Trace   | call      | `[Arg1, Arg2, ...]`         |
| Trace   | send      | `[Receiver, Message]`        |
| Trace   | 'receive' | `[Node, Sender, Message]`    |

# Examples

**Match argument list of three where first and third are equal** (source: "Match Specifications in Erlang," section "Tracing Examples"):

```erlang
[{['$1', '_', '$1'],
  [],
  []}]
```

**Match where second argument is a number greater than 3** (source: same section):

```erlang
[{['_', '$1', '_'],
  [{ '>', '$1', 3}],
  []}]
```

**ETS: Match all objects where first element is 'strider' and arity is 3, return whole object** (source: section "ETS Examples"):

```erlang
[{{strider,'_','_'},
  [],
  ['$_']}]
```

**Literal handling -- double-tuple syntax for constructing tuples from bound variables** (source: section "Variables and Literals"):

| Expression              | Variable Bindings  | Result       |
| ----------------------- | ------------------ | ------------ |
| `{{'$1','$2'}}`         | '$1' = a, '$2' = b | `{a,b}`      |
| `{const, {'$1', '$2'}}` | Irrelevant         | `{'$1','$2'}` |

# Relationships

## Related

- **match-spec-tracing** -- Tracing-specific action functions available only in the MatchBody when tracing
- **match-spec-ets** -- ETS-specific usage patterns and examples for match specifications

# Common Errors

- **Error**: Using a bare tuple literal in MatchCondition/MatchBody
  **Correction**: Tuples must use double-parenthesis `{{...}}` or `{const, T}` syntax; a bare tuple is interpreted as a function call

- **Error**: Writing `self` when you mean `{self}` in the MatchBody
  **Correction**: `self` is the atom; `{self}` calls the function returning the current process pid. All function calls must be tuples, even with no arguments.

- **Error**: Using unbound variables in MatchCondition or MatchBody
  **Correction**: Variables can only be bound in the MatchHead; all variables in later parts must have been previously bound

# Common Confusions

- **Confusion**: Match specifications are Erlang functions or funs
  **Clarification**: Match specifications are Erlang _terms_ (data), not code. They have a different syntax (tuple-based) and are compiled by the runtime into an efficient internal form.

- **Confusion**: The same match specification works identically in ETS and tracing
  **Clarification**: The MatchHead format differs (tuple for ETS, list for tracing), the MatchBody semantics differ (return value vs. side effects), and tracing has additional action functions not available in ETS.

# Source Reference

"Match Specifications in Erlang," sections "Grammar," "Function Descriptions," "Variables and Literals," "Match target," "Execution of the Match," and "Differences between Match Specifications in ETS and Tracing." The source provides the complete informal grammar, a full table of match targets by context, detailed variable binding rules, and multiple examples for both tracing and ETS contexts.

# Verification Notes

- Definition: Directly quoted from source -- "A 'match specification' (match_spec) is an Erlang term describing a small 'program' that tries to match something"
- Grammar structure: Directly from source informal grammar
- Variable rules ($_, $$, $<number>): Verbatim from source section "Variables and Literals"
- Match target table: Verbatim from source section "Match target"
- Exception semantics: Explicitly stated in source introduction
- Examples: Verbatim from source
- Confidence: HIGH -- all content directly from official ERTS documentation
