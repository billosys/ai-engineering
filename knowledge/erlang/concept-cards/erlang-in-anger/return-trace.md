---
concept: Return Trace
slug: return-trace
category: production-ops
subcategory: tracing
tier: intermediate
source: "Stuff Goes Bad: Erlang in Anger"
source_slug: erlang-in-anger
authors: "Fred Hébert"
chapter: "Tracing"
chapter_number: 9
pdf_page: null
section: "Example Sessions"
extraction_confidence: high
aliases:
  - "return_trace()"
  - "{return_trace}"
prerequisites:
  - recon-trace
  - match-specification
related:
  - recon-trace
  - match-specification
contrasts_with: []
answers_questions:
  - "How do I see the return value of a traced function call?"
  - "What is return_trace()?"
---

# Quick Definition

Return tracing makes a trace also report a function's return value: a match-spec fun that calls `return_trace()` (or the raw `{return_trace}` action) generates a second trace message for each call, showing what the function returned.

# Core Definition

From section "Example Sessions": to see the return value of a traced function, "we should change the trace patterns to use a fun that matches on all arguments in a list (`_`) and returns `return_trace()`. This last part will generate a second trace for each call that includes the return value." The two equivalent forms are a match-spec fun ending in `return_trace()` and the raw match-spec list action `{return_trace}`:

```erlang
recon_trace:calls({Mod,Fun,fun(_) -> return_trace() end}, Max, Opts)
recon_trace:calls({Mod,Fun,[{'_', [], [{return_trace}]}]}, Max, Opts)
```

# Prerequisites

- `recon-trace` — return tracing is invoked through a `recon_trace:calls` pattern.
- `match-specification` — `return_trace()` is a match-spec action placed in the matching fun.

# Key Properties

1. `return_trace()` in a match-spec fun (or `{return_trace}` in a raw match-spec list) enables return-value tracing.
2. It produces a *second* trace message per call, in addition to the call trace.
3. The return trace is printed as `Mod:Fun/Arity --> ReturnValue`.
4. The argument-matching fun must match the call before a return trace can be generated.
5. Each traced call therefore counts as (at least) two messages toward the rate limit.

# Construction / Recognition

Write the trace pattern's fun to end in `return_trace()`: `recon_trace:calls({queue, in, fun(_) -> return_trace() end}, 3)`. Each matching call then prints once for the call and once for the return.

# Context & Application

Return tracing is used when the call arguments alone are not enough — you need to see what a function produced. It is invaluable for verifying behaviour of a function on a live system without instrumenting the code.

# Examples

From section "Example Sessions":

```erlang-repl
3> recon_trace:calls({queue, in, fun(_) -> return_trace() end}, 3).
1

13:15:27.655132 <0.44.0> queue:in(a, {[],[]})

13:15:27.655467 <0.44.0> queue:in/2 --> {[a],[]}
```

# Relationships

## Builds Upon
- `recon-trace` — return tracing is set through a `recon_trace:calls` pattern.
- `match-specification` — `return_trace()`/`{return_trace}` are match-spec actions.

## Enables
Nothing — terminal mechanism card.

## Related
- `match-specification` — the fun-based form is itself a match specification.

## Contrasts With
Nothing specific within this source.

# Common Errors

- Forgetting that each traced call now emits two messages, so the rate limit is consumed twice as fast.
- Using a fun that does not match the call, so no return trace is produced.

# Common Confusions

- `return_trace()` does not replace the call trace — it adds a second message; you see both the call and the return.
- The fun form (`fun(_) -> return_trace() end`) and the list form (`[{'_', [], [{return_trace}]}]`) are equivalent ways to express the same match-spec action.

# Source Reference

Chapter 9: Tracing, Section "Example Sessions" (and "Tracing with Recon"). (No PDF pages — this source has none.)

# Verification Notes

- Definition source: quoted from section "Example Sessions."
- Confidence rationale: high — the source shows both forms and a worked session.
- Uncertainties: none.
- Cross-reference status: Verified
