---
concept: Erlang Abstract Format
slug: erlang-abstract-format
category: tooling
subcategory: compiler-internals
tier: advanced
source: "ERTS User's Guide"
source_slug: otp-erts
authors: "Ericsson AB"
chapter: "The Abstract Format"
chapter_number: null
pdf_page: null
section: "Module Declarations and Forms"
extraction_confidence: high
aliases:
  - "abstract format"
  - "abstract code"
  - "parse tree representation"
  - "abstract syntax tree"
prerequisites: []
extends: []
related:
  - external-term-format
contrasts_with: []
answers_questions:
  - "What is the Erlang abstract format?"
  - "How are Erlang programs represented as parse trees?"
---

# Quick Definition

The abstract format is the standard representation of parse trees for Erlang programs as Erlang terms. It is the intermediate representation used by the compiler, parse transforms, and tools like `erl_parse`, `erl_lint`, `erl_pp`, and `erl_eval`. A mapping function `Rep(C)` defines how each source construct `C` maps to its abstract format representation.

# Core Definition

The abstract format represents every Erlang source construct -- modules, functions, expressions, patterns, guards, types, and clauses -- as Erlang terms (tuples and lists). The representation uses the notation `R = Rep(C)` to denote the mapping from source construct `C` to abstract representation `R` (Ericsson AB, "The Abstract Format").

Each node in the abstract format includes an annotation `ANNO` (typically containing line number information; see `erl_anno` for details). Multiple instances of `ANNO` in the same construct can denote different annotations.

Functions dealing with the abstract format include:
- `compile:forms/1,2` -- Compiles abstract code
- `epp` -- Preprocessor, returns abstract format
- `erl_eval` -- Evaluates abstract format expressions
- `erl_lint` -- Lints abstract format
- `erl_parse` -- Parses source to abstract format
- `erl_pp` -- Pretty-prints abstract format back to source
- `io` -- I/O functions that handle abstract format

The abstract format is also the input and output format for parse transforms (via the `compile` module).

When the `debug_info` compilation option is used, the abstract code is stored in the `abstract_code` chunk of the `.beam` file as `{raw_abstract_v1, AbstractCode}`.

# Prerequisites

- Understanding of Erlang syntax (modules, functions, expressions, patterns, guards)
- Familiarity with Erlang terms (tuples, lists, atoms)

# Key Properties

1. A module is represented as a list of forms: `[Rep(F_1), ..., Rep(F_k)]`
2. A function declaration is `{function, ANNO, Name, Arity, [Clauses]}`
3. Attributes are `{attribute, ANNO, AttrName, AttrValue}` -- for example, `-module(foo)` becomes `{attribute, ANNO, module, foo}`
4. Atomic literals are tagged tuples: `{atom, ANNO, Value}`, `{integer, ANNO, Value}`, `{float, ANNO, Value}`, `{string, ANNO, Chars}`, `{char, ANNO, Value}`
5. Variables are `{var, ANNO, AtomName}` where the atom has the same printname as the variable; `_` is `{var, ANNO, '_'}`
6. Operators are represented as atoms with the same characters as the operator
7. Negative integer and float literals do not exist directly; they are parsed as applications of unary negation
8. Parenthesized expressions/patterns cannot be distinguished from their bodies in the abstract format
9. Parse errors appear as `{error, E}` and warnings as `{warning, W}` in the form list
10. End-of-file is `{eof, LOCATION}`

# Construction / Recognition

## Key Form Representations

| Source Construct | Abstract Format |
| --- | --- |
| `-module(foo).` | `{attribute, ANNO, module, foo}` |
| `-export([f/2]).` | `{attribute, ANNO, export, [{f, 2}]}` |
| `f(X, Y) -> X + Y.` | `{function, ANNO, f, 2, [{clause, ANNO, [{var,ANNO,'X'},{var,ANNO,'Y'}], [], [{op,ANNO,'+',{var,ANNO,'X'},{var,ANNO,'Y'}}]}]}` |
| `42` | `{integer, ANNO, 42}` |
| `hello` | `{atom, ANNO, hello}` |
| `{X, Y}` | `{tuple, ANNO, [{var,ANNO,'X'}, {var,ANNO,'Y'}]}` |
| `[H \| T]` | `{cons, ANNO, {var,ANNO,'H'}, {var,ANNO,'T'}}` |
| `[]` | `{nil, ANNO}` |

## Expression Types

- Function calls: `{call, ANNO, FunExpr, [ArgExprs]}`
- Remote calls: `{call, ANNO, {remote, ANNO, ModExpr, FunExpr}, [ArgExprs]}`
- Case: `{'case', ANNO, Expr, [Clauses]}`
- Try: `{'try', ANNO, Body, CaseClauses, CatchClauses, AfterBody}`
- Receive: `{'receive', ANNO, [Clauses]}` or with timeout `{'receive', ANNO, [Clauses], TimeoutExpr, TimeoutBody}`
- Match: `{match, ANNO, Pattern, Expr}`
- Fun: `{'fun', ANNO, {clauses, [Clauses]}}` or `{'fun', ANNO, {function, Name, Arity}}`
- Map creation: `{map, ANNO, [Associations]}`
- Record: `{record, ANNO, RecordName, [Fields]}`

## Clause Representation

All clause types use the same structure: `{clause, ANNO, Patterns, Guards, Body}`
- Function clause: patterns are the argument list
- Case clause: patterns is a single-element list
- If clause: patterns is empty, guards define the condition
- Catch clause: pattern is `{ExceptionClass, Pattern, Stacktrace}`

# Context & Application

The abstract format is essential for:

- **Parse transforms**: Custom compile-time code transformations that receive and return abstract format
- **Code analysis tools**: `erl_lint`, `dialyzer`, and custom analyzers that inspect program structure
- **Code generation**: Tools that programmatically generate Erlang code
- **Debugging**: The `debug_info` chunk stores abstract code for debugger and cover tool use
- **Pretty printing**: `erl_pp` converts abstract format back to readable source

Developers most commonly encounter the abstract format when writing parse transforms or when inspecting `.beam` files with `beam_lib:chunks/2` to read the `abstract_code` chunk.

# Examples

**Module attribute representations** (source: "The Abstract Format," section "Module Declarations and Forms"):

```erlang
%% -module(foo). becomes:
{attribute, 1, module, foo}

%% -export([start/0, stop/1]). becomes:
{attribute, 2, export, [{start, 0}, {stop, 1}]}

%% -import(lists, [map/2]). becomes:
{attribute, 3, import, {lists, [{map, 2}]}}
```

**Record declaration** (source: section "Record Fields"):

```erlang
%% -record(state, {name, count = 0}). becomes:
{attribute, ANNO, record, {state, [
  {record_field, ANNO, {atom, ANNO, name}},
  {record_field, ANNO, {atom, ANNO, count}, {integer, ANNO, 0}}
]}}
```

**Accessing stored abstract code** (source: section "The Abstract Format after Preprocessing"):

The `debug_info` compilation option stores abstract code in the `.beam` file as `{raw_abstract_v1, AbstractCode}` in the `abstract_code` chunk.

# Relationships

## Related

- **external-term-format** -- The external term format is a different encoding of Erlang terms for serialization, not to be confused with the abstract format which encodes program structure

# Common Errors

- **Error**: Confusing the abstract format with the external term format
  **Correction**: The abstract format represents program _structure_ (parse trees); the external term format represents term _values_ for serialization

- **Error**: Expecting negative literals like `-42` to appear as `{integer, ANNO, -42}`
  **Correction**: Negative literals are represented as unary negation: `{op, ANNO, '-', {integer, ANNO, 42}}`

- **Error**: Trying to distinguish parenthesized expressions from their bodies
  **Correction**: Parentheses are lost in the abstract format -- `(X + Y)` and `X + Y` have identical representations

# Common Confusions

- **Confusion**: The abstract format is an AST produced by a third-party tool
  **Clarification**: It is the _standard_ parse tree representation used internally by the Erlang compiler and all standard tools

- **Confusion**: ANNO is always just a line number
  **Clarification**: ANNO is an annotation that can contain line numbers and other metadata; see `erl_anno` for the full annotation interface

- **Confusion**: The abstract format can represent any Erlang term
  **Clarification**: It represents Erlang _programs_ (source code constructs), not arbitrary runtime data

# Source Reference

"The Abstract Format," all sections including "Module Declarations and Forms," "Atomic Literals," "Patterns," "Expressions," "Clauses," "Guards," "Types," and "The Abstract Format after Preprocessing." The source provides exhaustive `Rep()` mappings for every Erlang source construct. The `debug_info` storage format is documented in the final section.

# Verification Notes

- Rep() mapping notation: Directly from source -- "We use the function Rep to denote the mapping"
- ANNO description: Directly from source -- "The word ANNO in this section represents an annotation"
- Module/function/attribute representations: Directly from source section "Module Declarations and Forms"
- Atomic literal representations: Directly from source section "Atomic Literals"
- Negative literal rule: Directly stated -- "negative integer and float literals do not occur as such; they are parsed as an application of the unary negation operator"
- Parenthesized expression rule: Directly stated -- "parenthesized expressions cannot be distinguished from their bodies"
- debug_info chunk format: Directly from source -- "{raw_abstract_v1, AbstractCode}"
- Tool list (epp, erl_eval, etc.): Directly from source introduction
- Confidence: HIGH -- all content directly from official ERTS documentation
