---
# === CORE IDENTIFICATION ===
concept: Multipurpose Server
slug: multipurpose-server

# === CLASSIFICATION ===
category: core-idioms
subcategory: server-patterns
tier: intermediate

# === PROVENANCE ===
source: Programming Erlang, Second Edition
source_slug: programming-erlang
authors: Joe Armstrong
chapter: "Programming Idioms"
chapter_number: 24
pdf_page: null
section: "A Multipurpose Server"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - multi_server
  - multiserver
  - universal server

# === TYPED RELATIONSHIPS ===
prerequisites:
  - process
  - message-passing
  - unified-erlang-messaging
extends:
  - unified-erlang-messaging
related:
  - middle-man
  - spawn
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do Erlang processes communicate with each other?"
  - "How does gen_server relate to the client/server pattern?"
---

# Quick Definition

A multipurpose server is a single Erlang server process that handles requests for many different services by pattern matching on the shape of uniformly formatted Erlang messages.

# Core Definition

A multipurpose (or "multi") server is a process whose receive loop matches several distinct message shapes, each corresponding to a different service, and "mimics the essential behavior of a number of well-known services." Because all requests arrive as Erlang terms, "we don't really need many different encodings of client-server requests and responses. One universal format suffices" ("A Multipurpose Server"). The server captures only the *essential* job of each service, abstracting away protocol detail.

# Prerequisites

- **Process** — The server is a long-running process with a receive loop.
- **Message-passing** — Requests and replies travel as messages.
- **Unified Erlang messaging** — A multipurpose server only works because every service uses the one universal term format.

# Key Properties

1. A single receive loop dispatches on multiple message patterns, one per service.
2. Each clause implements only the *essential* behavior of a service (e.g., store an email, tell the user, transfer a file).
3. It recurses on itself after handling each message, remaining alive for the next request.
4. A catch-all `Any` clause handles unrecognized messages gracefully.
5. It removes the need for per-service request/response encodings.

# Construction / Recognition

## To Construct/Create:
1. Define a process function with a `receive` block.
2. Add one clause per service, matching the message tuple shape for that service.
3. Implement the essential behavior of each service in its clause.
4. Add a catch-all `Any` clause to handle unexpected messages.
5. Tail-call the server function to loop.

## To Identify/Recognize:
1. One process with a receive loop containing clauses for multiple unrelated services.
2. All messages are Erlang terms; no service-specific decoding occurs.

# Context & Application

- **Typical contexts**: Back-end servers that must satisfy several different kinds of client request.
- **Common applications**: Acting as the shared back end behind multiple middle men, each translating a different external protocol.
- **Historical/stylistic notes**: Demonstrates Armstrong's point that uniform messaging "really simplifies complex systems, especially if a large number of different external protocols are used."

# Examples

**Example 1** ("A Multipurpose Server"): The `multi_server` module. Lines 8-11 behave like an email client (receive an email, append it to file `mbox`); lines 12-13 behave like an instant-messaging client (print the message to the console); lines 14-15 behave like an FTP/HTTP file server (`Pid ! {self(), file:read_file(File)}`):

```erlang
-module(multi_server).
-export([start/0]).

start() -> spawn(fun() -> multi_server() end).

multi_server() ->
    receive
        {_Pid, {email, _From, _Subject, _Text} = Email} ->
            {ok, S} = file:open("mbox", [write,append]),
            io:format(S, "~p.~n", [Email]),
            file:close(S);
        {_Pid, {im, From, Text}} ->
            io:format("Msg (~s): ~s~n",[From, Text]);
        {Pid, {get, File}} ->
            Pid ! {self(), file:read_file(File)};
        Any ->
            io:format("multi server got:~p~n",[Any])
    end,
    multi_server().
```

# Relationships

## Builds Upon
- **Unified Erlang messaging** — One term format lets a single server cover many services.

## Enables
- This idiom is a leaf application of unified messaging; it is itself a building block for multi-protocol systems.

## Related
- **Middle man** — Middle men feed a multipurpose server by normalizing external protocols.
- **Spawn** — The server is started with `spawn`.

## Contrasts With
- This concept has no direct contrast within the chapter.

# Common Errors

- **Error**: Writing one server process per service when the requests share a uniform format.
  **Correction**: Use a single receive loop with one clause per service.

- **Error**: Omitting a catch-all clause, so unexpected messages accumulate in the mailbox.
  **Correction**: Add an `Any ->` clause to consume and log unrecognized messages.

# Common Confusions

- **Confusion**: Thinking a multipurpose server must implement each service in full.
  **Clarification**: It captures only the *essential* behavior of each service, not the complete real-world product.

# Source Reference

Chapter 24: Programming Idioms, Section "A Multipurpose Server." See the `multi_server.erl` listing.

# Verification Notes

- Definition source: Direct adaptation from "A Multipurpose Server."
- Confidence rationale: HIGH — the source provides a complete worked module and explains each clause.
- Uncertainties: None.
- Cross-reference status: Verified concept names exist or are planned.
- Re-extraction notes: Fresh extraction; no pre-existing card.
