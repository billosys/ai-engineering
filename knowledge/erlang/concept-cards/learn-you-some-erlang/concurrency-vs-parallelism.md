---
concept: Concurrency vs. Parallelism
slug: concurrency-vs-parallelism
category: processes-concurrency
subcategory: concurrency-model
tier: foundational
source: "Learn You Some Erlang for Great Good!"
source_slug: learn-you-some-erlang
authors: "Fred Hébert"
chapter: "The Hitchhiker's Guide to Concurrency"
chapter_number: 10
pdf_page: null
section: "Don't Panic"
extraction_confidence: high
aliases:
  - "concurrency and parallelism"
  - "actor model"
prerequisites: []
extends: []
related:
  - process
  - message-passing
contrasts_with: []
answers_questions:
  - "What distinguishes concurrency from parallelism?"
  - "What must I know before writing concurrent programs?"
---

# Concurrency vs. Parallelism

## Quick Definition

In Erlang's vocabulary, concurrency is having many independent actors that run but not necessarily at the same instant; parallelism is having actors running at exactly the same time. Erlang had concurrency from the start; true parallelism arrived later with multicore SMP support.

## Core Definition

The chapter is careful to define these terms, noting "there doesn't seem to be any consensus on these definitions in the computer science world." In the context of Erlang: *concurrency* "refers to having many actors running independently but not necessarily all at the same time," while *parallelism* "is having actors running at exactly the same time." Erlang had concurrency from the beginning, even on single-core 1980s hardware, where each process got a time slice. True parallelism on one machine required multicore SMP support, which Erlang only got mostly right with the R13B release in 2009. Crucially, because Erlang concurrency is built on isolated processes, "it took no conceptual change at the language level to bring true parallelism" — all the changes happened transparently in the VM (Hébert, ch. 10, "Don't Panic").

## Prerequisites

This is a foundational concept with no prerequisites within this source.

## Key Properties

1. Concurrency: many actors running independently, not necessarily simultaneously
2. Parallelism: actors running at exactly the same time
3. Erlang's concurrency model is message passing and the actor model
4. Concurrency existed in Erlang from the 1980s, even on single-core hardware
5. True SMP parallelism arrived later (mostly correct as of R13B, 2009)
6. Because processes are isolated, going parallel needed no language-level change — only VM changes
7. Parallelism is not a cure-all: a purely sequential program using many processes can run slower in parallel (the ring-benchmark example)
8. Amdahl's law: a program is only as fast as its slowest sequential part

## Construction / Recognition

## To Reason About Concurrency vs. Parallelism

1. Ask whether actors merely run independently (concurrency) or literally at the same time (parallelism)
2. Recognize that Erlang code is written the same way regardless — the VM decides scheduling
3. Expect linear scaling only for "embarrassingly parallel" problems with independent logical entities
4. Apply Amdahl's law: identify the sequential bottleneck, since it caps the achievable speedup

## Examples

> **Single-core concurrency** (ch. 10): on 1980s hardware "each Erlang process would have its own slice of time to run, much like desktop applications did before multicore systems."
>
> **Ring benchmark** (ch. 10): thousands of processes pass a token in a circle; only one does useful work at a time, so the program runs slower on many cores than on one.
>
> **Amdahl's law** (ch. 10): code that is 95 percent parallel can be roughly 20 times faster with enough processors; 50 percent parallel can never exceed 2x.

## Relationships

## Related

- **Process** — The isolated actor that makes both concurrency and parallelism possible in Erlang
- **Message passing** — The communication mechanism of the actor model

## Common Errors

- **Error**: Assuming adding cores always speeds up an Erlang program
  **Correction**: A sequential algorithm spread over processes can slow down; only embarrassingly parallel work scales near-linearly

## Common Confusions

- **Confusion**: Treating "concurrency" and "parallelism" as synonyms
  **Clarification**: In Erlang's usage they are distinct — concurrency is structural independence, parallelism is simultaneous execution
- **Confusion**: Believing Erlang was multicore-ready from inception
  **Clarification**: Erlang had concurrency early but true SMP parallelism was only solid from R13B (2009)

## Source Reference

Chapter 10, "The Hitchhiker's Guide to Concurrency," sections "Don't Panic," "Concurrency Concepts," and "Not Entirely Unlike Linear Scaling."

## Verification Notes

- Definitions: quoted directly from ch. 10
- Amdahl's law and ring benchmark: from the chapter's discussion of linear scaling
- Confidence: HIGH — the chapter explicitly defines and contrasts the terms
