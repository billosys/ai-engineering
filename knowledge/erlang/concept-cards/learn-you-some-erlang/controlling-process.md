---
concept: Controlling Process
slug: controlling-process
category: production-ops
subcategory: networking
tier: intermediate
source: "Learn You Some Erlang for Great Good!"
source_slug: learn-you-some-erlang
authors: "Fred Hébert"
chapter: "Buckets of Sockets"
chapter_number: 23
pdf_page: null
section: "TCP Sockets"
extraction_confidence: high
aliases:
  - "controlling_process"
  - "socket ownership"
  - "socket owner"
prerequisites:
  - tcp-socket
  - process
extends: []
related:
  - gen-tcp
  - gen-udp
contrasts_with: []
answers_questions:
  - "What is a socket's controlling process?"
  - "How do I transfer socket ownership to another process?"
  - "Why can only one process read from a socket?"
---

# Controlling Process

## Quick Definition

A socket's controlling process is the process that owns it. Any process can send through a socket, but only the owner can read messages received on it. Ownership is transferred with `controlling_process/2`.

## Core Definition

The book explains there is "some kind of ownership to sockets": UDP sockets, TCP client sockets, and TCP accept sockets "can all have messages sent through them from any process in existence, but messages received can be read only by the process that started the socket" (Ch. 23, "TCP Sockets"). To hand a socket to a different process, both `gen_tcp` and `gen_udp` provide `controlling_process(Socket, Pid)`. This function must be called by the current owner; afterward the named `Pid` is the one that can read and receive messages from the socket.

## Prerequisites

- **Tcp-socket** — Socket ownership is a socket property
- **Process** — Ownership ties a socket to a specific process

## Key Properties

1. The owner is the process that created the socket
2. Any process can *send* through a socket; only the owner can *receive* from it
3. `controlling_process(Socket, Pid)` transfers ownership to `Pid`
4. The transfer call must be made by the current owner
5. After transfer, the new `Pid` reads and receives messages from the socket
6. It exists in both `gen_tcp` and `gen_udp`

## Construction / Recognition

### To delegate socket handling

1. The owner creates the socket and starts a request
2. The owner spawns a worker process to handle the response
3. The owner calls `controlling_process(Socket, WorkerPid)` to give the worker the socket
4. The worker now receives all incoming messages; the owner is free to do other work

## Context & Application

Ownership transfer lets a coordinator process delegate per-request handling to dedicated workers, rather than staying alive solely to relay socket messages. The book notes ETS tables have a similar give-away mechanism.

## Examples

**Example** (Ch. 23): The book's delegation pattern — Process A starts a socket and a request, spawns Process B, "gives ownership of the socket to Process B" via `controlling_process`, and B handles the response while A moves on to the next request.

## Relationships

### Related

- **Gen-tcp** — `gen_tcp:controlling_process/2` transfers TCP socket ownership
- **Gen-udp** — `gen_udp:controlling_process/2` transfers UDP socket ownership

## Common Errors

- **Error**: Calling `controlling_process` from a process that does not own the socket.
  **Correction**: The transfer must be initiated by the current owner.
- **Error**: Expecting a non-owner process to receive socket messages.
  **Correction**: Only the owner receives them; transfer ownership first.

## Common Confusions

- **Confusion**: Thinking any process can read a socket because any process can send through it.
  **Clarification**: Sending is unrestricted, but receiving is limited to the controlling process.

## Source Reference

Chapter 23, "Buckets of Sockets," section "TCP Sockets" (ownership discussion at the end).

## Verification Notes

- Definition: Direct adaptation from the socket ownership discussion in "TCP Sockets"
- Key Properties: All explicit in source
- Confidence: HIGH — the section explicitly describes ownership and `controlling_process`
- Cross-references: `gen-tcp`, `gen-udp`, `tcp-socket` planned this chapter; `process` shared slug
