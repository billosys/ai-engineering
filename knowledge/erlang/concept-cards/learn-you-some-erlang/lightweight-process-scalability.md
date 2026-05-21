---
concept: Lightweight Process Scalability
slug: lightweight-process-scalability
category: processes-concurrency
subcategory: concurrency-model
tier: intermediate
source: "Learn You Some Erlang for Great Good!"
source_slug: learn-you-some-erlang
authors: "Fred Hébert"
chapter: "The Hitchhiker's Guide to Concurrency"
chapter_number: 10
pdf_page: null
section: "Scalability"
extraction_confidence: high
aliases:
  - "scalability"
  - "lightweight processes"
prerequisites:
  - process
extends: []
related:
  - scheduler-and-run-queue
  - let-it-crash
contrasts_with: []
answers_questions:
  - "Why are Erlang processes lightweight?"
  - "How does Erlang scale to many thousands of processes?"
---

# Lightweight Process Scalability

## Quick Definition

Erlang processes are deliberately lightweight — tiny to create and destroy — so a program can freely use as many as it needs. This is the foundation of Erlang's scalability.

## Core Definition

Erlang's telephony origins required scaling "to support many thousands of users across many switches." Because users were modeled as processes reacting to events, "an ideal system would support processes doing small computations, switching between them very quickly... it made sense for processes to be started and destroyed very quickly. Having them be lightweight was mandatory to achieve this efficiency." Lightness also avoids the need for *process pools* — "a fixed amount of processes you split the work among" — so programs "could use as many processes as they needed." The chapter quantifies it: an Erlang process "takes about 300 words of memory each and can be created in a matter of microseconds — not something currently doable on major operating systems." Scalability also has a hardware dimension: bypassing hardware limits by adding more computers, which makes distribution part of the language's value (Hébert, ch. 10, "Scalability," "Concurrency Implementation").

## Prerequisites

- **Process** — Lightness is a property of Erlang processes

## Key Properties

1. Processes are designed to be cheap to create and destroy
2. A process takes about 300 words of memory
3. A process can be created in microseconds
4. Lightness removes the need for fixed process pools
5. Programs can use as many processes as the design naturally calls for
6. The VM, not the OS, manages processes — enabling this efficiency
7. Scalability also means adding hardware (distribution), not just better hardware

## Construction / Recognition

## To Exploit Lightweight Processes

1. Model each independent activity as its own process
2. Do not build a fixed process pool — spawn freely as needed
3. Create and destroy processes liberally; both are cheap
4. For scaling beyond one machine, distribute processes across nodes

## Examples

> **Process cost** (ch. 10): "Erlang's processes take about 300 words of memory each and can be created in a matter of microseconds."
>
> **No process pools** (ch. 10): "you didn't want to have things like process pools... it would be much easier to design programs that could use as many processes as they needed."

## Relationships

## Builds Upon

- **Process** — The lightweight unit being described

## Related

- **Scheduler and run queue** — The VM machinery that runs the many lightweight processes
- **Let it crash** — Cheap restart and shutdown depend on lightweight processes

## Common Errors

- **Error**: Designing a fixed worker pool to limit process count
  **Correction**: Processes are cheap; spawn one per logical activity and let the VM schedule

## Common Confusions

- **Confusion**: Equating Erlang processes' cost with OS threads' cost
  **Clarification**: An Erlang process is far lighter (~300 words, microsecond creation) than any OS thread or process

## Source Reference

Chapter 10, "The Hitchhiker's Guide to Concurrency," section "Concurrency Concepts," subsections "Scalability" and "Concurrency Implementation."

## Verification Notes

- Process cost figures and no-pools rationale: directly from ch. 10
- Confidence: HIGH — explicitly discussed
