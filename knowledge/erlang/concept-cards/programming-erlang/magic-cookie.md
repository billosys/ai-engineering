---
# === CORE IDENTIFICATION ===
concept: Magic Cookie
slug: magic-cookie

# === CLASSIFICATION ===
category: distribution
subcategory: distribution-security
tier: intermediate

# === PROVENANCE ===
source: Programming Erlang, Second Edition
source_slug: programming-erlang
authors: Joe Armstrong
chapter: "Distributed Programming"
chapter_number: 14
pdf_page: null
section: "The Cookie Protection System"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "cookie"
  - "cookie protection system"
  - ".erlang.cookie"
  - "-setcookie"
  - "erlang:set_cookie"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - node
extends: []
related:
  - distributed-erlang
  - distribution-bifs
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How are distributed Erlang nodes authenticated?"
  - "How do I set the magic cookie?"
  - "What defines an Erlang cluster?"
---

# Quick Definition

The magic cookie is a shared secret atom that authenticates connections between Erlang nodes; two nodes can communicate only if they have the same cookie, and the set of connected nodes sharing a cookie defines an Erlang cluster.

# Core Definition

Access to a node or set of nodes is secured by a *cookie* system (Chapter 14, "The Cookie Protection System"). Each node has a single cookie, and this cookie must be the same as the cookie of any node it talks to. The set of connected nodes having the same cookie defines an *Erlang cluster*. For two distributed Erlang nodes to communicate, they must have the same *magic cookie*. The cookie can be set in three ways: (1) store the same cookie in the file `$HOME/.erlang.cookie` (created automatically with a random string the first time Erlang runs, and copyable to other machines); (2) start Erlang with the command-line argument `-setcookie C`; (3) call the BIF `erlang:set_cookie(node(), C)` to set the local node's cookie. The cookie protection system was designed for LANs protected from the Internet by a firewall; cookies are never sent across the network in the clear and are used only for the initial authentication of a session.

# Prerequisites

- **Node** — Cookies authenticate connections between nodes; you must understand nodes first.

# Key Properties

1. Each node has exactly one cookie.
2. Two nodes can communicate only if they share the same cookie.
3. The set of connected nodes with the same cookie defines an Erlang cluster.
4. Cookies can be set via `$HOME/.erlang.cookie`, the `-setcookie` flag, or `erlang:set_cookie/2`.
5. Cookies are never transmitted in the clear — used only for initial session authentication.
6. The system assumes a firewalled LAN; Internet use should add secure channels first.

# Construction / Recognition

## To Set the Cookie:
1. Method 1: Put the same cookie string in `$HOME/.erlang.cookie` on every machine (`chmod 400` to protect it).
2. Method 2: Start Erlang with `erl -setcookie AFRTY12ESS3412735ASDF12378 ...`.
3. Method 3: Evaluate `erlang:set_cookie(node(), C)` to set the local node's cookie.

## To Recognize It:
1. Look for `-setcookie` flags on `erl` command lines.
2. Look for the `$HOME/.erlang.cookie` file or `erlang:set_cookie` calls.

# Context & Application

- **Typical contexts**: Authenticating nodes in a distributed Erlang cluster.
- **Common applications**: Same-cookie startup of cooperating nodes; protecting nodes from unauthorized connections.
- **Historical/stylistic notes**: Method 2 (`-setcookie`) is useful only for testing, since on Unix anyone can see the cookie with `ps`; methods 1 and 3 are better for insecure environments.

# Examples

**Example 1** (Chapter 14, "Stage 3"): Both nodes are started with `-setcookie abc` so they share a cookie; when two nodes run on the same machine they can instead share the same `$HOME/.erlang.cookie` file.

**Example 2** (Chapter 14, "The Cookie Protection System," Method 1): On Linux, `cd; cat > .erlang.cookie` (entering `AFRTY12ESS3412735ASDF12378`) then `chmod 400 .erlang.cookie` sets and protects the cookie file.

# Relationships

## Builds Upon
- **Node** — cookies are a per-node property.

## Enables
- **Distributed Erlang** — node-to-node communication requires matching cookies.

## Related
- **Distribution BIFs** — `erlang:set_cookie/2` is the BIF form.

## Contrasts With
- A foundational security concept; no commonly confused counterpart in this chapter.

# Common Errors

- **Error**: Starting two nodes with different cookies and expecting them to connect.
  **Correction**: Ensure all nodes in a cluster share the same cookie.
- **Error**: Using `-setcookie` on a shared Unix host for production.
  **Correction**: Use the `.erlang.cookie` file or `erlang:set_cookie/2`, since `ps` reveals command-line cookies.

# Common Confusions

- **Confusion**: The cookie encrypts distributed Erlang traffic.
  **Clarification**: It only authenticates the initial session; sessions are not encrypted and need a secure channel for Internet use.
- **Confusion**: The cookie is sent over the network as proof each message.
  **Clarification**: Cookies are never sent in the clear and are used only for initial authentication.

# Source Reference

Chapter 14: Distributed Programming, section "The Cookie Protection System" (the three methods of setting the cookie and the cluster definition).

# Verification Notes

- Definition source: Direct adaptation of "The Cookie Protection System" section.
- Confidence rationale: HIGH — the cookie system, cluster definition, and three setting methods are explicitly described.
- Uncertainties: None.
- Cross-reference status: Slugs match canonical `node` and planned chapter cards.
- Re-extraction notes: Fresh extraction; no pre-existing card.
