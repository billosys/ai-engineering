---
concept: Distribution Cookie
slug: distribution-cookie
category: distribution
subcategory: clustering
tier: foundational
source: "Stuff Goes Bad: Erlang in Anger"
source_slug: erlang-in-anger
authors: "Fred Hébert"
chapter: "Connecting to Remote Nodes"
chapter_number: 4
pdf_page: null
section: null
extraction_confidence: medium
aliases:
  - cookie
  - magic cookie
prerequisites:
  - remote-shell-connection
extends: []
related:
  - job-control-mode
  - remsh
contrasts_with:
  - ssh-daemon-shell
  - named-pipe-connection
answers_questions:
  - "How do I connect to a remote node?"
  - "Can I connect to a node that wasn't given a name?"
---

# Quick Definition

A distribution cookie is a shared secret atom that two Erlang nodes must both possess in order to connect over Erlang distribution; named nodes plus a matching cookie are the precondition for distribution-based remote shells.

# Core Definition

The chapter states: "Most common usages will depend on a cookie being present on the two nodes you want to connect together, but there are ways to do it that do not include it. Most usages will also require the use of named nodes, and all of them will require *a priori* measures to make sure you can contact the node" (Chapter 4, intro).

The cookie can be supplied on the command line with `-setcookie $COOKIE`.

# Prerequisites

- `remote-shell-connection`: the cookie is the authentication mechanism that enables distribution-based shells.

# Key Properties

1. Required for the *common* connection methods (JCL mode and `-remsh`), which use Erlang distribution.
2. Both nodes must have the *same* cookie to connect.
3. Distribution-based methods also require *named* nodes (`-name`/`-sname`).
4. Supplied via the `-setcookie $COOKIE` command-line argument when starting `erl`.
5. Some connection methods (SSH daemon, named pipes) do *not* need a cookie at all.
6. All connection methods require *a priori* setup — the cookie and node name must be in place before you need to connect.

# Construction / Recognition

Start both nodes with matching names and cookies, e.g. `erl -name node@host -setcookie SECRET`. With matching cookies in place, JCL mode `r`/`c` or `-remsh` can connect.

# Context & Application

Used to authenticate Erlang distribution links. In the connection chapter it is the gating requirement for the JCL and `-remsh` methods. The SSH daemon and named pipes are the alternatives when you cannot or do not want to use cookies/distribution.

# Examples

From Chapter 4, "Remsh": "All other Erlang arguments (such as `-hidden` and `-setcookie $COOKIE`) are also valid."

From Chapter 4 intro: "Most common usages will depend on a cookie being present on the two nodes you want to connect together, but there are ways to do it that do not include it."

# Relationships

## Builds Upon
- remote-shell-connection

## Enables
- job-control-mode
- remsh

## Related

## Contrasts With
- ssh-daemon-shell
- named-pipe-connection

# Common Errors

- Connecting two nodes with mismatched cookies — the distribution handshake fails.
- Forgetting that distribution-based connection also requires *named* nodes, not just a cookie.

# Common Confusions

- A cookie is not encryption — it is a shared-secret access check; it does not secure the traffic.
- Not every connection method needs a cookie: SSH daemon and named pipes bypass distribution entirely.

# Source Reference

Chapter 4: Connecting to Remote Nodes, intro section (cookie and named-node requirements); Section "Remsh" (`-setcookie`). (No PDF pages — this source has none.)

# Verification Notes

- Definition source: synthesized from the chapter intro and Remsh section; the book refers readers to external sources for cookie details.
- Confidence rationale: medium — the chapter mentions cookies repeatedly but does not give a full standalone definition, deferring to external references.
- Uncertainties: full mechanics of cookie matching are out of scope for this chapter.
- Cross-reference status: Verified
