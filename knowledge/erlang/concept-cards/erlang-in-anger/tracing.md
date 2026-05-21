---
concept: Tracing
slug: tracing
category: production-ops
subcategory: tracing
tier: intermediate
source: "Stuff Goes Bad: Erlang in Anger"
source_slug: erlang-in-anger
authors: "Fred Hébert"
chapter: "Tracing"
chapter_number: 9
pdf_page: null
section: "Tracing"
extraction_confidence: high
aliases:
  - "BEAM tracing"
prerequisites: []
related:
  - erlang-tracing-tools
  - tracing-principles
  - recon-trace
contrasts_with: []
answers_questions:
  - "Why is tracing preferred over debuggers in Erlang?"
  - "Why is debugger use generally limited on Erlang?"
---

# Quick Definition

Tracing is the BEAM facility for observing running code without interfering with its execution; in Erlang it is preferred over breakpoint debuggers, which break down because pausing one process makes the surrounding processes time out and crash.

# Core Definition

From the chapter introduction: "One of the lesser known and absolutely under-used features of Erlang and the BEAM virtual machine is just about how much tracing you can do on there. Forget your debuggers, their use is too limited. Tracing makes sense in Erlang at all steps of your system's life cycle, whether it's for development or for diagnosing a running production system." A footnote explains why debuggers fail: a breakpoint in one process does not stop the others, so as soon as another process needs to interact with the paused one, "its calls start timing out and crashing, possibly taking down the entire node with it. Tracing, on the other hand, doesn't interfere with program execution, but still gives you all the data you need."

# Prerequisites

This is a foundational framing concept within this source's tracing chapter — it has no prerequisites within this source.

# Key Properties

1. Tracing observes running code without interfering with execution.
2. Breakpoint debuggers are incompatible with Erlang: pausing one process leaves the others running, so they time out and crash around it.
3. Tracing works across the whole system life cycle — development and production diagnosis alike.
4. Tracing can replace the impulse to "add more logging" — it gets the data without deploying code or hurting readability.
5. Sensitive process data can be excluded from traces via `process_flag(sensitive, true)`.

# Construction / Recognition

To trace, pick a tool (`sys`, `dbg`, the trace BIFs, `redbug`, or `recon_trace`), specify which processes and which function calls to observe, and read the resulting trace messages. The chapter focuses on `recon_trace`, but the terminology carries over to any Erlang tracing tool.

# Context & Application

Tracing is used throughout a system's life cycle: during development to understand behaviour, and in production to diagnose a live system without redeploying. It is the recommended alternative to both breakpoint debuggers and ad-hoc logging.

# Examples

From the chapter introduction, footnote on debuggers: "put a break point in one process and the ones around keep going. In practice, this turns debugging into a very limited activity because as soon as a process needs to interact with the one you're debugging, its calls start timing out and crashing."

# Relationships

## Builds Upon
Nothing within this source — it is the chapter's framing premise.

## Enables
- `erlang-tracing-tools`, `tracing-principles`, `recon-trace` — the tools and mechanics of tracing.

## Related
- `tracing-principles` — the pid-specification ∩ trace-pattern model underlying all tracing.

## Contrasts With
Breakpoint debuggers — incompatible with Erlang's concurrency model.

# Common Errors

- Reaching for a breakpoint debugger on a live Erlang node, causing surrounding processes to time out.
- Adding logging statements and redeploying when tracing would have answered the question immediately.

# Common Confusions

- Tracing does not pause or alter the traced program; it passively records, which is precisely why it succeeds where debuggers fail.

# Source Reference

Chapter 9: Tracing, chapter introduction. (No PDF pages — this source has none.)

# Verification Notes

- Definition source: quoted from the chapter introduction and its debugger footnote.
- Confidence rationale: high — the source explicitly contrasts tracing with debuggers.
- Uncertainties: none.
- Cross-reference status: Verified
