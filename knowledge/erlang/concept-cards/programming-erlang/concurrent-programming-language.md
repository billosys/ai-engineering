---
# === CORE IDENTIFICATION ===
concept: Concurrent Programming Language
slug: concurrent-programming-language

# === CLASSIFICATION ===
category: processes-concurrency
subcategory: terminology
tier: foundational

# === PROVENANCE ===
source: "Programming Erlang, Second Edition"
source_slug: programming-erlang
authors: Joe Armstrong
chapter: "Introducing Concurrency"
chapter_number: 1
pdf_page: null
section: "Sequential vs. Concurrent Programming Languages"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - language-based concurrency
  - sequential programming language

# === TYPED RELATIONSHIPS ===
prerequisites: []
extends: []
related:
  - concurrency-vs-parallelism
  - concurrency-oriented-programming
  - process
contrasts_with:
  - concurrency-vs-parallelism

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is a concurrent programming language?"
  - "Why is Erlang concurrency the same on every operating system?"
  - "What distinguishes a sequential language from a concurrent one?"
---

# Quick Definition

A concurrent programming language has explicit, built-in constructs for writing concurrent programs. In Erlang, concurrency is provided by the virtual machine itself, so it behaves identically on every operating system.

# Core Definition

"A *concurrent programming language* is a language that has explicit language constructs for writing concurrent programs. These constructs are an integral part of the programming language and behave the same way on all operating systems" (Chapter 1, "Concurrent Programs and Parallel Computers"). The chapter contrasts two categories: "Sequential languages are languages that were designed for writing sequential programs and have no linguistic constructs for describing concurrent computations. Concurrent programming languages ... were designed for writing concurrent programs and have special constructs for expressing concurrency in the language itself" (Chapter 1, "Sequential vs. Concurrent Programming Languages"). "In Erlang, concurrency is provided by the Erlang virtual machine and not by the operating system or by any external libraries." This matters because OS-based concurrency makes a program "work in different ways on different operating systems," whereas "Erlang concurrency works the same way on all operating systems."

# Prerequisites

This is a foundational terminology concept with no prerequisites within this source.

# Key Properties

1. A concurrent programming language has explicit, built-in concurrency constructs.
2. Those constructs are integral to the language, not an add-on library.
3. A sequential language has no linguistic constructs for concurrency.
4. In Erlang, concurrency is provided by the virtual machine, not the OS or external libraries.
5. Language-based concurrency behaves identically on every operating system.
6. OS-based concurrency, by contrast, varies across operating systems.

# Construction / Recognition

## To Recognize a Concurrent Programming Language:

1. Check whether concurrency is expressed with native language constructs (e.g., `spawn`, `!`, `receive`).
2. Confirm those constructs are part of the language, not an OS interface or library.
3. Confirm concurrency behavior is the same across operating systems.

# Context & Application

- **Typical contexts**: Understanding why Erlang programs are portable in their concurrency behavior.
- **Common applications**: Writing concurrent programs that you only have to understand in terms of Erlang itself, not the host OS.
- **Historical/stylistic notes**: "To write concurrent programs in Erlang, you just have to understand Erlang; you don't have to understand the concurrency mechanisms in the operating system." This also allows fine-grained control of concurrent structure, "something that is extremely difficult using operating system processes."

# Examples

**Example 1** (Chapter 1, "Sequential vs. Concurrent Programming Languages"): "In most sequential programming languages, concurrency is provided as an interface to the concurrency primitives of the host operating system" — so the program behaves differently on different operating systems.

**Example 2** (Chapter 2, "A Whirlwind Tour of Erlang"): The three concurrency primitives `spawn`, `send` (`!`), and `receive` are built into the Erlang language itself and used to create the file-server program.

# Relationships

## Builds Upon

- This is foundational terminology and does not build upon another card in this source.

## Enables

- **Concurrency-oriented programming** — Having native concurrency constructs is what makes COP practical.

## Related

- **Concurrency vs. parallelism** — A concurrent program is "a program written in a concurrent programming language."
- **Process** — The Erlang concurrency construct created by the language's own primitives.

## Contrasts With

- **Concurrency vs. parallelism** — This card distinguishes language-based from OS-based concurrency; that card distinguishes the software property of concurrency from the hardware property of parallelism.

# Common Errors

- **Error**: Assuming concurrency behaves the same across OSes when using OS-based concurrency.
  **Correction**: Only language-based concurrency (as in Erlang) is portable; OS-based concurrency varies.

- **Error**: Reaching for OS-level processes to structure an Erlang program.
  **Correction**: Use Erlang's own lightweight processes; the language's constructs give fine-grained control.

# Common Confusions

- **Confusion**: Thinking any language with a threading library is a concurrent programming language.
  **Clarification**: The defining trait is *explicit language constructs* integral to the language, not a bolted-on library.

- **Confusion**: Believing Erlang concurrency depends on the operating system.
  **Clarification**: It is provided by the Erlang virtual machine and works identically on all operating systems.

# Source Reference

"Programming Erlang, Second Edition," Chapter 1: Introducing Concurrency, sections "Concurrent Programs and Parallel Computers" and "Sequential vs. Concurrent Programming Languages." EPUB-origin source; no page numbers.

# Verification Notes

- Definition source: Direct quotations from Chapter 1, "Concurrent Programs and Parallel Computers" and "Sequential vs. Concurrent Programming Languages."
- Confidence rationale: HIGH — the source gives an explicit definition and a sequential/concurrent contrast.
- Uncertainties: None.
- Cross-reference status: Verified against planned cards.
- Re-extraction notes: Fresh extraction; no pre-existing card.
