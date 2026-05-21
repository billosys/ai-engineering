---
concept: Match Specification
slug: match-specification
category: production-ops
subcategory: tracing
tier: intermediate
source: "Stuff Goes Bad: Erlang in Anger"
source_slug: erlang-in-anger
authors: "Fred Hébert"
chapter: "Tracing"
chapter_number: 9
pdf_page: null
section: "Tracing with Recon"
extraction_confidence: medium
aliases:
  - "Match spec"
prerequisites:
  - tracing-principles
related:
  - recon-trace
  - return-trace
contrasts_with: []
answers_questions:
  - "How do I constrain a trace to specific function arguments?"
  - "What is a match specification in tracing?"
---

# Quick Definition

A match specification is the constraint language — the same one used by ETS — that lets a trace pattern match on the arguments of a function call, so only calls whose arguments satisfy the constraints are traced.

# Core Definition

From section "Tracing Principles," trace patterns can be specified "with Erlang match specifications to add constraints to arguments." In `recon_trace` (section "Tracing with Recon"), the arity part of a `{Mod, Fun, Arity}` pattern can be replaced "by a function to match on lists of arguments. The function is limited to those usable by match specifications similar to what is available in ETS." `recon_trace` accepts either a literal fun (translated internally) or a raw match-spec list such as `[{'_', [], [{return_trace}]}]`.

# Prerequisites

- `tracing-principles` — match specifications are the argument-constraint half of a trace pattern.

# Key Properties

1. A match specification constrains which function calls are traced based on their arguments.
2. It is the same constraint mechanism used by ETS (`ets:fun2ms/1`).
3. In `recon_trace`, a match spec can be written as a fun over the argument list, e.g. `fun([_,_,2]) -> ok end`.
4. Funs used as match specs are limited to operations match specifications support — not arbitrary Erlang.
5. The match spec can include guards, e.g. `fun([X]) when is_binary(X) -> ok end`.
6. A raw match-spec list form is also accepted: `[{'_', [], [{return_trace}]}]`.

# Construction / Recognition

Write the argument-matching fun directly: `recon_trace:calls({lists, seq, fun([_,_,2]) -> ok end}, 100)` traces only `lists:seq/3` calls whose third argument is 2. Guards narrow further: `fun([X]) when is_binary(X) -> ok end`. The fun body can return `return_trace()` to also trace return values.

# Context & Application

Match specifications make tracing precise enough for production: instead of tracing every call to a function, you trace only the calls whose arguments matter — for example, only `iolist_to_binary/1` calls already given a binary, to find useless conversions.

# Examples

From section "Tracing with Recon":

```erlang
%% All calls to lists:seq(A,B,2) (all sequences increasing by two):
recon_trace:calls({lists, seq, fun([_,_,2]) -> ok end}, 100)

%% iolist_to_binary/1 made with a binary argument already:
recon_trace:calls({erlang, iolist_to_binary,
                   fun([X]) when is_binary(X) -> ok end},
                  10)
```

# Relationships

## Builds Upon
- `tracing-principles` — match specs are the argument-constraint half of a trace pattern.

## Enables
- `return-trace` — `return_trace()`/`{return_trace}` are match-spec actions.

## Related
- `recon-trace` — the tool that accepts match-spec funs and lists.

## Contrasts With
Nothing specific within this source.

# Common Errors

- Writing a match-spec fun with arbitrary Erlang code; only operations supported by match specifications are allowed.

# Common Confusions

- A match-spec fun in `recon_trace` is not executed as ordinary Erlang — it is translated into a match specification, which is why it is restricted to ETS-style operations.

# Source Reference

Chapter 9: Tracing, Sections "Tracing Principles" and "Tracing with Recon". (No PDF pages — this source has none.)

# Verification Notes

- Definition source: synthesized from sections "Tracing Principles" and "Tracing with Recon"; the book references but does not fully define the match-spec language.
- Confidence rationale: medium — the source uses match specifications and shows examples, but defers the full definition to external ETS/match-spec documentation.
- Uncertainties: the complete match-spec grammar is not given in this source.
- Cross-reference status: Verified
