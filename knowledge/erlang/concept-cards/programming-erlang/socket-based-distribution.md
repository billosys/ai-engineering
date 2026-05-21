---
# === CORE IDENTIFICATION ===
concept: Socket-Based Distribution
slug: socket-based-distribution

# === CLASSIFICATION ===
category: distribution
subcategory: distribution-models
tier: advanced

# === PROVENANCE ===
source: Programming Erlang, Second Edition
source_slug: programming-erlang
authors: Joe Armstrong
chapter: "Distributed Programming"
chapter_number: 14
pdf_page: null
section: "Socket-Based Distribution"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "lib_chan"
  - "untrusted distribution"
  - "controlled spawning"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - distributed-erlang
  - message-passing
extends: []
related:
  - node
  - magic-cookie
contrasts_with:
  - distributed-erlang

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do I write distributed programs in an untrusted environment?"
  - "What is the difference between distributed Erlang and socket-based distribution?"
  - "How does lib_chan control which processes are spawned on a machine?"
---

# Quick Definition

Socket-based distribution is a model for writing distributed Erlang applications over raw TCP/IP sockets, suitable for untrusted environments where the machine owner must explicitly control which processes may run on their machine.

# Core Definition

Using TCP/IP sockets, you can write distributed applications that run in an *untrusted* environment; the programming model is less powerful than distributed Erlang but more secure (Chapter 14, "Two Models for Distribution"). The main problem with distributed Erlang is that a client can spawn *any* process on the server machine — `rpc:multicall(nodes(), os, cmd, ["cd /; rm -rf *"])` would destroy every node. Socket-based distribution uses a *restricted* form of `spawn` where the owner of a machine has explicit control over what runs on it. The book's `lib_chan` module implements this: a configuration file (`$HOME/.erlang_config/lib_chan.conf`) declares the ports and named, password-protected *services* (`{service, S, password, P, mfa, Mod, Func, Args}`) that the machine permits; a client calls `connect(Host, Port, S, P, ArgsC)` to activate a service. On connection, proxy "middle-man" processes are spawned on both sides; they convert Erlang messages to TCP packet data, trap exits, and handle socket closure (Chapter 14, "Socket-Based Distribution").

# Prerequisites

- **Distributed Erlang** — Socket-based distribution is the alternative model; understanding the trusted model clarifies why this one exists.
- **Message passing** — The middle-man proxies translate between Erlang messages and TCP data.

# Key Properties

1. Runs over raw TCP/IP sockets, suitable for untrusted environments.
2. The programming model is less powerful than distributed Erlang but more secure.
3. Uses a restricted form of `spawn` — the machine owner controls what runs.
4. `lib_chan` services are declared in a config file with port, name, and password.
5. A client connects via `connect/5` with host, port, service name, and password.
6. Proxy middle-man processes on each side convert messages, trap exits, and handle socket closure.

# Construction / Recognition

## To Build a Socket-Based Service:
1. Write a config file declaring `{port, NNNN}` and `{service, S, password, P, mfa, Mod, Func, Args}`.
2. Start the server with `lib_chan:start_server()` (or `start_server(Conf)`).
3. Implement the service module (e.g. `mod_name_server`) following the middle-man protocol: handle `{chan, MM, X}` and `{chan_closed, MM}`, reply with `MM ! {send, X}`.
4. From a client, call `lib_chan:connect(Host, Port, S, P, ArgsC)`.

## To Recognize It:
1. Look for `lib_chan` configuration files and `connect/5` calls.
2. Look for the `{chan, MM, ...}` / `{chan_closed, MM}` middle-man protocol.

# Context & Application

- **Typical contexts**: Distributed applications across machines owned by different parties.
- **Common applications**: The `kvs` name server exposed as a password-protected `nameServer` service over `lib_chan`.
- **Historical/stylistic notes**: `lib_chan`'s full implementation is in the book's Appendix 2 ("A Socket Application"); the chapter only uses its interface.

# Examples

**Example 1** (Chapter 14, "The Server Code"): A config file `{port, 1234}. {service, nameServer, password, "ABXy45", mfa, mod_name_server, start_me_up, notUsed}.` declares a password-protected name service on port 1234.

**Example 2** (Chapter 14): A client runs `{ok, Pid} = lib_chan:connect("localhost", 1234, nameServer, "ABXy45", "")`, then `lib_chan:rpc(Pid, {lookup, joe})` returns `{ok, "writing a book"}`.

# Relationships

## Builds Upon
- **Distributed Erlang** — socket-based distribution is the alternative for cases distributed Erlang's trust model cannot serve.

## Enables
- Distributed applications across mutually untrusting machines.

## Related
- **Node** and **magic cookie** — the trusted-model concepts this model deliberately avoids.

## Contrasts With
- **Distributed Erlang** — distributed Erlang is more powerful but trusts every node fully; socket-based distribution is less powerful but lets each machine owner control exactly what runs.

# Common Errors

- **Error**: Using distributed Erlang across machines owned by different, untrusting parties.
  **Correction**: Use socket-based distribution so each owner controls permitted services.
- **Error**: Omitting or mismatching the service password in `connect/5`.
  **Correction**: The password in the `connect` call must match the one in the server config.

# Common Confusions

- **Confusion**: Socket-based distribution lets a client spawn any process on the server.
  **Clarification**: It uses a restricted `spawn` — only services declared in the server's config file can be started.
- **Confusion**: A socket behaves like an Erlang process.
  **Clarification**: Unlike a port, a socket does not behave like a process; the `lib_chan` middle-man proxies bridge that gap.

# Source Reference

Chapter 14: Distributed Programming, sections "Two Models for Distribution" and "Socket-Based Distribution" (subsections "Controlling Processes with lib_chan" and "The Server Code"). Full `lib_chan` implementation in Appendix 2, "A Socket Application."

# Verification Notes

- Definition source: Direct adaptation of the "Socket-Based Distribution" section and the `lib_chan` interface specs.
- Confidence rationale: HIGH — the model and the `lib_chan` interface are explicitly described and demonstrated.
- Uncertainties: The full `lib_chan` implementation is deferred to Appendix 2 (out of scope).
- Cross-reference status: Slugs match canonical `distributed-erlang`/`message-passing`/`node` and planned chapter cards.
- Re-extraction notes: Fresh extraction; no pre-existing card.
