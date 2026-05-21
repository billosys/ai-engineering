---
# === CORE IDENTIFICATION ===
concept: Middle Man
slug: middle-man

# === CLASSIFICATION ===
category: core-idioms
subcategory: process-structuring
tier: intermediate

# === PROVENANCE ===
source: Programming Erlang, Second Edition
source_slug: programming-erlang
authors: Joe Armstrong
chapter: "Programming Idioms"
chapter_number: 24
pdf_page: null
section: "Maintaining the Erlang View of the World"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - middleman
  - protocol-translation process
  - translation process

# === TYPED RELATIONSHIPS ===
prerequisites:
  - process
  - message-passing
extends:
  - process
related:
  - unified-erlang-messaging
  - multipurpose-server
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do Erlang processes communicate with each other?"
  - "What concepts are needed before using OTP behaviours?"
---

# Quick Definition

A middle man is a process interposed between an external protocol driver and an Erlang server whose sole job is to translate between the external wire protocol and pure Erlang messages.

# Core Definition

The middle man is a process placed "between the TCP driver that receives messages from the HTTP client and our Erlang server." It parses incoming requests in some external protocol (HTTP, FTP, IRC/DCC, and so on), turns them into Erlang messages, and converts outgoing Erlang terms back into the external protocol's responses. By doing so it lets the server "know nothing about the details of the HTTP protocol" and deal only with pure Erlang messages, while the middle man "knows only how to convert between HTTP and Erlang messages" ("Maintaining the Erlang View of the World"). Armstrong calls this "the most important idea that you should take away from this chapter."

# Prerequisites

- **Process** — A middle man *is* a separate process, so the process concept underpins it.
- **Message-passing** — The middle man exists to convert one message form into another; understanding asynchronous message passing is required.

# Key Properties

1. It is a dedicated process with a single, clearly defined role: protocol translation.
2. It separates protocol handling from request servicing — "Instead of having one process that does two things... we now have two processes, each with a clearly defined role."
3. It increases concurrency: the middle man and the server can execute in parallel.
4. As far as the server is concerned, "the objects in the external world only speak Erlang."
5. The designer must decide how much detail of the underlying protocol to expose to the Erlang application.

# Construction / Recognition

## To Construct/Create:
1. Identify the external protocol the system must speak (HTTP, FTP, etc.).
2. Spawn a process that sits between the protocol driver and the server.
3. In that process, parse incoming protocol data and convert it into Erlang terms/messages.
4. Forward the Erlang messages to the server process.
5. Convert outgoing Erlang terms produced by the server back into the external protocol's response format.

## To Identify/Recognize:
1. Look for a process whose only responsibility is converting between a wire format and Erlang messages.
2. The server it feeds receives only Erlang terms and contains no protocol-parsing logic.

# Context & Application

- **Typical contexts**: Network servers (web, FTP, IRC) where external clients speak non-Erlang protocols.
- **Common applications**: Front-ending an Erlang back-end server with one middle man per external protocol so a single server can serve them all.
- **Historical/stylistic notes**: Armstrong frames the middle man as central "to making components that smoothly fit together," likening it to a world where everybody speaks the same language.

# Examples

**Example 1** ("Maintaining the Erlang View of the World"): A simple `web_server(Client)` loop receives `{Client, {get, Page}}` messages, reads the file, and replies with `{self(), {data, Bin}}`. The code is simple only because it receives and sends pure Erlang terms; a middle man is needed because real clients send fragmented HTTP requests over TCP.

**Example 2** ("Maintaining the Erlang View of the World"): Extending the system to HTTP, FTP, and IRC. Each external protocol gets its own middle man; after translation, "a single Erlang server can be used as the back end to all these different protocols."

# Relationships

## Builds Upon
- **Process** — The middle man is a process specialized for translation.

## Enables
- **Unified Erlang messaging** — Once middle men exist, all external processes effectively speak Erlang.
- **Multipurpose server** — A single back-end server can serve many protocols because middle men normalize their messages.

## Related
- **Message-passing** — The middle man's whole purpose is reformatting messages.

## Contrasts With
- This concept has no direct contrast within the chapter.

# Common Errors

- **Error**: Mixing protocol parsing and request servicing in one process.
  **Correction**: Split into a middle man (parsing/translation) and a server (servicing), each with one role.

- **Error**: Exposing every detail of the wire protocol to the Erlang application.
  **Correction**: Deliberately abstract out detail in the middle man; decide up front how much of the protocol to surface.

# Common Confusions

- **Confusion**: Believing the middle man is just a passive relay.
  **Clarification**: It actively parses and reformats data between two representations; it is a translator, not a pipe.

# Source Reference

Chapter 24: Programming Idioms, Section "Maintaining the Erlang View of the World." See Figure 5 (Web Server Protocol) and Figure 6 (Unified Messages).

# Verification Notes

- Definition source: Direct adaptation from "Maintaining the Erlang View of the World."
- Confidence rationale: HIGH — the source explicitly names and explains the middle man and flags it as the chapter's key idea.
- Uncertainties: None.
- Cross-reference status: Verified concept names exist or are planned (`process`, `message-passing`, `unified-erlang-messaging`, `multipurpose-server`).
- Re-extraction notes: Fresh extraction; no pre-existing card.
