---
concept: inet Socket Options
slug: inet-socket-option
category: production-ops
subcategory: networking
tier: intermediate
source: "Learn You Some Erlang for Great Good!"
source_slug: learn-you-some-erlang
authors: "Fred Hébert"
chapter: "Buckets of Sockets"
chapter_number: 23
pdf_page: null
section: "More Control with Inet"
extraction_confidence: high
aliases:
  - "inet module"
  - "inet:setopts"
  - "socket options"
prerequisites:
  - tcp-socket
  - udp-socket
extends: []
related:
  - socket-active-vs-passive-mode
  - gen-tcp
  - gen-udp
contrasts_with: []
answers_questions:
  - "What is the inet module used for?"
  - "How do I change socket options after a socket is open?"
  - "What socket options are common to TCP and UDP?"
---

# inet Socket Options

## Quick Definition

The `inet` module handles operations common to `gen_tcp` and `gen_udp` sockets, most notably `inet:setopts/2`, which changes a socket's options (such as active/passive mode) after it is already open.

## Core Definition

`inet` is "an Erlang module... that takes care of handling all operations that can be common to both `gen_tcp` and `gen_udp` sockets" (Ch. 23, "More Control with Inet"). Its key function is `inet:setopts(Socket, Options)`, where the option list can contain any terms used at socket setup. This avoids the impractical workaround of restarting a socket just to change its options (which would break an active TCP session). The book warns to not confuse `inet` with `inets` — `inets` is an OTP application of services (FTP, HTTP, etc.) built on top of `inet`.

## Prerequisites

- **Tcp-socket** — `inet` options apply to TCP sockets
- **Udp-socket** — `inet` options apply to UDP sockets

## Key Properties

1. `inet:setopts(Socket, Options)` changes options on an already-open socket
2. The option list may contain any term valid at socket setup time
3. Options common to all IP sockets include data type (`list`/`binary`), `{active, true|false|once}`, and IP version (`inet4`/`inet6`)
4. `inet` also offers functions to read statistics, get host information, and inspect sockets
5. `inet` (the socket-options module) is distinct from `inets` (the OTP services application)

## Construction / Recognition

### To change a socket option at runtime

1. Identify the option to change (e.g. switching to active mode)
2. Call `inet:setopts(Socket, [{Option, Value}])`
3. The socket continues without being restarted

## Context & Application

`inet:setopts/2` is the practical way to flip a socket between active and passive mode, or to re-arm `{active, once}` after each message, without tearing down a live connection.

## Examples

**Example** (Ch. 23): Switching a server's accept socket to active mode mid-session —

```erlang
4> inet:setopts(Accept, [{active, true}]).
ok
```

**Example** (Ch. 23): The `sockserv` `send` helper re-arms `{active, once}` after every reply: `ok = inet:setopts(Socket, [{active, once}])`.

## Relationships

### Related

- **Socket-active-vs-passive-mode** — `inet:setopts/2` is how the mode is changed at runtime
- **Gen-tcp** / **Gen-udp** — `inet` handles options common to both modules

## Common Errors

- **Error**: Using the `inets` application when you meant the `inet` module.
  **Correction**: `inet` is socket options; `inets` is services built on top of it.
- **Error**: Restarting a socket just to change an option.
  **Correction**: Use `inet:setopts/2` to change options in place, preserving active sessions.

## Common Confusions

- **Confusion**: Confusing `inet` and `inets`.
  **Clarification**: `inets` = `inet` + services; the option-handling module is `inet`.

## Source Reference

Chapter 23, "Buckets of Sockets," section "More Control with Inet."

## Verification Notes

- Definition: Direct adaptation from "More Control with Inet"
- Key Properties: All explicit in source
- Confidence: HIGH — the section defines `inet` and warns about the `inet`/`inets` distinction
- Cross-references: `socket-active-vs-passive-mode`, `gen-tcp`, `gen-udp`, `tcp-socket`, `udp-socket` planned this chapter
