---
concept: IO List
slug: io-list
category: data-types
subcategory: text-data
tier: intermediate
source: "Learn You Some Erlang for Great Good!"
source_slug: learn-you-some-erlang
authors: "Fred Hébert"
chapter: "Buckets of Sockets"
chapter_number: 23
pdf_page: null
section: "IO Lists"
extraction_confidence: high
aliases:
  - "iolist"
  - "io lists"
prerequisites:
  - process
extends: []
related:
  - tcp-socket
  - udp-socket
contrasts_with: []
answers_questions:
  - "What is an IO list?"
  - "How do I efficiently build strings for output?"
  - "Why use IO lists instead of strings or binaries?"
---

# IO List

## Quick Definition

An IO list is a list whose elements are bytes (integers 0-255), binaries, or other IO lists. Functions that output data accept IO lists and flatten them automatically into a byte sequence.

## Core Definition

The book defines IO lists as "a weird type of data structure... lists of bytes (integers from 0 to 255), binaries, or other IO lists" (Ch. 23, "IO Lists"). They exist to avoid the inefficiency of immutable data structures when dynamically building output. Strings (lists of integers) are expensive to append to because each append rewrites the whole list; binaries are better but still cost to modify and split. IO lists let you mix strings, binaries, and characters freely without converting between types, and the VM flattens the nested structure when it needs the actual byte sequence.

## Prerequisites

- **Process** — IO lists are commonly built to send through sockets owned by processes

## Key Properties

1. An IO list may contain integers 0-255 (bytes), binaries, or nested IO lists
2. The VM flattens an IO list into a byte sequence when output is needed
3. Functions accepting IO lists include all of the `io` and `file` modules, TCP and UDP sockets, and many `unicode` and `re` module functions
4. IO lists avoid the cost of rewriting immutable strings when appending content
5. They let strings, binaries, and individual characters be mixed without type conversion

## Construction / Recognition

### To recognize an IO list

It is any (possibly deeply nested) list whose leaves are integers 0-255 or binaries.

### To build output efficiently

1. Accumulate fragments (strings, binaries, characters) into a nested list rather than concatenating
2. Pass the resulting IO list directly to an output function — no flattening needed

## Context & Application

IO lists are the idiomatic way to assemble dynamic output (e.g. responses to send over a socket) without garbage from repeated string concatenation.

## Examples

**Example** (Ch. 23): The value `[$H, $e, [$l, <<"lo">>, " "], [[["W","o"], <<"rl">>]] | [<<"d">>]]` is a valid IO list that the VM flattens to the byte sequence "Hello World". Running `io:format("~s~n", [IoList])` on it prints "Hello World".

## Relationships

### Related

- **Tcp-socket** — `gen_tcp:send` accepts IO lists as the message
- **Udp-socket** — `gen_udp:send` likewise accepts IO lists

## Common Errors

- **Error**: Flattening an IO list manually before passing it to an output function.
  **Correction**: Output functions flatten it for you; manual flattening just wastes work.
- **Error**: Putting integers above 255 into an IO list.
  **Correction**: Elements must be bytes (0-255), binaries, or nested IO lists.

## Common Confusions

- **Confusion**: Thinking an IO list is just a flat list of characters.
  **Clarification**: It can be deeply nested and mix bytes and binaries.
- **Confusion**: Believing IO lists are a separate primitive type.
  **Clarification**: They are ordinary lists; "IO list" is a usage convention recognized by output functions.

## Source Reference

Chapter 23, "Buckets of Sockets," section "IO Lists." See the Hello World IO list example.

## Verification Notes

- Definition: Direct adaptation from "IO Lists"
- Key Properties: All explicit in source
- Confidence: HIGH — the section defines and demonstrates IO lists clearly
- Cross-references: `tcp-socket`, `udp-socket` planned this chapter; `process` shared slug
