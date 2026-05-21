---
concept: Recon Trace
slug: recon-trace
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
extraction_confidence: high
aliases:
  - "recon_trace:calls"
prerequisites:
  - tracing-principles
  - erlang-tracing-tools
related:
  - match-specification
  - trace-rate-limiting
  - return-trace
contrasts_with: []
answers_questions:
  - "How do I trace function calls safely in production?"
  - "How do I use recon_trace:calls?"
---

# Quick Definition

`recon_trace` is recon's production-safe tracing module; its main function `recon_trace:calls(TSpec, Max, Opts)` traces function calls matching a pattern, with built-in rate limiting and no external dependencies.

# Core Definition

From section "Tracing with Recon": recon by default matches all processes, which is often good enough. The interesting part is the trace pattern. "The most basic form is `{Mod, Fun, Arity}`, where `Mod` is a literal module, `Fun` is a function name, and `Arity` is the number of arguments of the function to trace. Any of these may also be replaced by wildcards (`'_'`)." Recon forbids patterns matching too widely (such as `{'_','_','_'}`). A fancier form replaces the arity with a match-spec fun over argument lists; multiple patterns can be combined in a list. Each `recon_trace:calls` call overrides the previous one, and all traces are cancelled with `recon_trace:clear/0`.

# Prerequisites

- `tracing-principles` — `recon_trace` is built on the pid ∩ trace-pattern model.
- `erlang-tracing-tools` — `recon_trace` is one of the tracing tools, chosen for production safety.

# Key Properties

1. By default `recon_trace` matches all processes.
2. The basic trace pattern is `{Mod, Fun, Arity}`; any part can be a wildcard `'_'`.
3. Patterns that match too widely (e.g. `{'_','_','_'}`) are forbidden as dangerous in production.
4. Arity can be replaced by a match-spec fun; multiple patterns can be listed to broaden scope.
5. Each `recon_trace:calls/2,3` call overrides the previous; `recon_trace:clear/0` cancels all tracing.
6. Options include `{pid, PidSpec}`, `{timestamp, formatter|trace}`, `{args, arity|args}`, and `{scope, global|local}`.
7. `{scope, local}` is needed to trace non-exported (locally-called) functions.

# Construction / Recognition

1. Call `recon_trace:calls(TSpec, Max)` or `recon_trace:calls(TSpec, Max, Opts)`.
2. Use `{Mod, Fun, Arity}` with wildcards, a match-spec fun, or a list of patterns.
3. Add `Opts` such as `{pid, new}`, `{scope, local}`, or `{args, arity}` as needed.
4. Start restrictive with low limits, then widen progressively.
5. Stop with `recon_trace:clear/0`.

# Context & Application

`recon_trace` is the chapter's recommended way to trace function calls on a live production node. It replaces the impulse to add logging and redeploy. The `{scope, local}` option lets it trace non-exported functions called as `Fun(Args)` rather than `Module:Fun(Args)`.

# Examples

From section "Tracing with Recon":

```erlang
%% All calls from the queue module, with 10 calls printed at most:
recon_trace:calls({queue, '_', '_'}, 10)

%% All calls to lists:seq(A,B), with 100 calls per second at most:
recon_trace:calls({lists, seq, 2}, {100, 1000})

%% Matching filter/2 of both dict and lists, across new processes only:
recon_trace:calls([{dict,filter,2},{lists,filter,2}], 10, [{pid, new}])
```

# Relationships

## Builds Upon
- `tracing-principles` — the pid ∩ pattern model.
- `erlang-tracing-tools` — `recon_trace` is one such tool.

## Enables
- `trace-rate-limiting` — the `Max`/`{Count, Time}` argument.
- `return-trace` — return-value tracing via match-spec funs.

## Related
- `match-specification` — supplies the argument-matching funs.

## Contrasts With
Nothing specific within this source.

# Common Errors

- Trying `{'_','_','_'}` — recon forbids such over-broad patterns.
- Tracing a non-exported function without `{scope, local}` and seeing no output.
- Forgetting that each `calls/2,3` call overrides the previous trace.

# Common Confusions

- `recon_trace` traces function *calls* only, never inter-process messages.
- A new `recon_trace:calls` does not add to existing traces — it replaces them.

# Source Reference

Chapter 9: Tracing, Section "Tracing with Recon". (No PDF pages — this source has none.)

# Verification Notes

- Definition source: quoted from section "Tracing with Recon."
- Confidence rationale: high — the source documents the interface, options, and examples in detail.
- Uncertainties: none.
- Cross-reference status: Verified
