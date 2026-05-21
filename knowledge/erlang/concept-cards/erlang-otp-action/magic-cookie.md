---
# === CORE IDENTIFICATION ===
concept: Magic Cookie
slug: magic-cookie

# === CLASSIFICATION ===
category: distribution
subcategory: nodes-clustering
tier: intermediate

# === PROVENANCE ===
source: "Erlang and OTP in Action"
source_slug: erlang-otp-action
authors: "Martin Logan, Eric Merritt, Richard Carlsson"
chapter: "Introducing distributed Erlang/OTP"
chapter_number: 8
pdf_page: null
section: "8.2.4 The magic cookie security system"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "magic cookie"
  - "Erlang cookie"
  - ".erlang.cookie"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - erlang-node
extends: []
related:
  - connecting-nodes
  - erlang-cluster
  - epmd
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is the magic cookie security system?"
  - "Where is the Erlang cookie stored?"
  - "How do I let nodes on different machines communicate?"
---

# Quick Definition

The magic cookie is a shared secret string used to authorize communication between Erlang nodes; a node refuses traffic from any node that does not present the same cookie.

# Core Definition

The magic cookie is the basis of Erlang distribution's authorization system. An Erlang node does not allow traffic from other nodes unless they know its magic cookie. When a node starts, it reads the `.erlang.cookie` file in the user's home directory and uses the string found there as its cookie; if no such file exists, it creates one containing a randomly generated string. By default a node assumes every other node it talks to uses the same cookie as itself, so nodes started under the same user account on one machine share a cookie file and may communicate. The current cookie can be inspected with `auth:get_cookie()`. To let nodes on different machines communicate, the simplest approach is to copy the cookie file so they match; for complex setups, `set_cookie(Node, Cookie)` lets a node use specific cookies for specific other nodes. The cookie guards against basic attacks and, importantly, against human error — using different cookies keeps two separate clusters from accidentally merging (Ch. 8, Section 8.2.4).

# Prerequisites

- **erlang-node** — The cookie authorizes communication between nodes.

# Key Properties

1. A shared secret string that authorizes node-to-node traffic.
2. Stored in the `.erlang.cookie` file in the user's home directory.
3. Auto-generated randomly if no cookie file exists.
4. A node assumes other nodes share its cookie by default.
5. Inspectable with `auth:get_cookie()`; settable with `set_cookie/2`.
6. Different cookies prevent separate clusters from accidentally merging.

# Construction / Recognition

## To Configure Cookies:
1. For nodes on one machine under one account, the shared `.erlang.cookie` file suffices.
2. For nodes on different machines, copy the cookie file so contents match.
3. For per-node cookies, call `set_cookie(Node, Cookie)`.

## To Recognize:
1. `auth:get_cookie()` returns the node's current magic cookie atom.

# Context & Application

- **Typical contexts**: Securing distributed Erlang on a trusted network.
- **Common applications**: Authorizing cluster membership; isolating clusters by cookie.
- **Historical/stylistic notes**: Erlang's default distribution assumes a trusted network; untrusted links should use direct TCP/SSL/SSH instead. Apart from firewalls, an incorrectly set cookie is the most common reason nodes fail to connect.

# Examples

**Example 1** (Section 8.2.4): `auth:get_cookie()` returns an atom like `'CUYHQMJEJEZLUETUOWFH'`, the same string found in the `.erlang.cookie` file.

**Example 2** (Section 8.2.4): Deleting the `.erlang.cookie` file and restarting the node makes the file reappear with a fresh random string.

# Relationships

## Builds Upon
- **erlang-node** — The cookie controls which nodes a node will talk to.

## Enables
- None.

## Related
- **connecting-nodes** — A wrong cookie causes connection to fail.
- **erlang-cluster** — Cookies determine which nodes may join a cluster.
- **EPMD** — EPMD locates nodes; the cookie authorizes the resulting connection.

## Contrasts With
- None.

# Common Errors

- **Error**: Nodes on two machines failing to connect because their cookie files differ.
  **Correction**: Copy the cookie file so both machines have identical contents (readable only by the owner).

# Common Confusions

- **Confusion**: Treating the magic cookie as strong network security.
  **Clarification**: It guards against basic attacks and human error on a trusted network; untrusted links need TCP/SSL/SSH or a configured secure carrier.

# Source Reference

Chapter 8: Introducing distributed Erlang/OTP, Section 8.2.4 "The magic cookie security system."

# Verification Notes

- Definition source: Directly adapted from Section 8.2.4.
- Confidence rationale: HIGH — the book explicitly defines and demonstrates the cookie system.
- Uncertainties: None.
- Cross-reference status: Verified.
