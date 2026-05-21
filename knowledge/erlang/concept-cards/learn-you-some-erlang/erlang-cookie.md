---
concept: Erlang Cookie
slug: erlang-cookie
category: distribution
subcategory: distribution-infrastructure
tier: advanced
source: "Learn You Some Erlang for Great Good!"
source_slug: learn-you-some-erlang
authors: "Fred Hébert"
chapter: "Distribunomicon"
chapter_number: 26
pdf_page: null
section: "Cookies"
extraction_confidence: high
aliases:
  - "cookie"
  - "Erlang cookie"
  - ".erlang.cookie"
  - "magic cookie"
prerequisites:
  - distributed-node
  - node-connection
extends: []
related:
  - hidden-node
contrasts_with: []
answers_questions:
  - "What is an Erlang cookie?"
  - "How do cookies control which nodes can connect?"
  - "Is the Erlang cookie a security feature?"
---

# Erlang Cookie

## Quick Definition

A cookie is a token value that must be shared between Erlang nodes for them to connect. It is used to divide clusters of nodes, not as a real security mechanism.

## Core Definition

The cookie is "a little unique value that must be shared between nodes to allow them to connect with each other" (Ch. 26, "Cookies"). It exists so that different Erlang node clusters can run on the same hardware without accidentally connecting. The book stresses that, despite documentation filing cookies under "security," they are "closer to the idea of usernames than passwords" — they "make much more sense as a mechanism used to divide clusters of nodes than as an authentication mechanism." Nodes with different cookies refuse to connect.

## Prerequisites

- **Distributed-node** — Each node has a cookie
- **Node-connection** — Cookies must match for a connection to succeed

## Key Properties

1. A cookie is a token that must be shared for two nodes to connect
2. Its real purpose is dividing node clusters, not authentication
3. Set at startup with `erl -setcookie Cookie`
4. Nodes with mismatched cookies fail to connect; the rejecting node logs "Connection attempt from disallowed node"
5. `erlang:set_cookie(OtherNode, Cookie)` sets a cookie used only for connecting to that node
6. `erlang:set_cookie(node(), Cookie)` changes the node's cookie for all future connections
7. `erlang:get_cookie()` returns the current node cookie
8. Without an explicit cookie, Erlang creates a random one and stores it in `~/.erlang.cookie`, reused by future nodes

## Construction / Recognition

### To control cluster membership with cookies

1. Start each node with `-setcookie 'shared_value'` to put it in a cluster
2. To bridge two differently-cookied nodes, call `erlang:set_cookie(OtherNode, ItsCookie)` then connect
3. To change the node's default cookie, call `erlang:set_cookie(node(), NewCookie)`

## Context & Application

Cookies let multiple independent Erlang clusters coexist on one machine. Because they are not real security, sensitive deployments need SSL, tunneling, or a custom protocol on top.

## Examples

**Example** (Ch. 26): Two nodes with different cookies cannot connect —

```erlang
(salad@ferdmbp)1> net_kernel:connect_node(mustard@ferdmbp).
false
```

with `mustard` logging `** Connection attempt from disallowed node salad@ferdmbp **`.

**Example** (Ch. 26): Setting a per-node cookie then connecting —

```erlang
(salad@ferdmbp)3> erlang:set_cookie(mustard@ferdmbp, opensesame).
true
(salad@ferdmbp)5> net_kernel:connect_node(mustard@ferdmbp).
true
```

## Relationships

### Builds Upon

- **Distributed-node** — Each node carries a cookie
- **Node-connection** — Cookie matching gates connections

### Related

- **Hidden-node** — Hidden nodes still need matching cookies to connect

## Common Errors

- **Error**: Treating the cookie as a security guarantee.
  **Correction**: A cookie is like a username, not a password; use SSL or tunneling for real security.
- **Error**: Expecting two nodes with different cookies to connect.
  **Correction**: Cookies must match, or use `erlang:set_cookie/2` to bridge them.

## Common Confusions

- **Confusion**: Thinking `erlang:set_cookie(OtherNode, Cookie)` changes the local node's cookie.
  **Clarification**: That form sets a cookie used only for connecting to `OtherNode`; `erlang:set_cookie(node(), Cookie)` changes the node's own cookie.
- **Confusion**: Believing you must always specify a cookie.
  **Clarification**: Erlang auto-generates one in `~/.erlang.cookie` if you do not.

## Source Reference

Chapter 26, "Distribunomicon," section "Cookies."

## Verification Notes

- Definition: Direct adaptation from "Cookies"
- Key Properties: All explicit in source
- Confidence: HIGH — the section explains cookies and their (non-)security thoroughly
- Cross-references: `distributed-node`, `node-connection`, `hidden-node` planned this chapter
