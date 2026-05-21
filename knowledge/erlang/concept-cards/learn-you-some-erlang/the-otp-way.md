---
concept: The OTP Way
slug: the-otp-way
category: otp-behaviours
subcategory: otp-fundamentals
tier: intermediate
source: "Learn You Some Erlang for Great Good!"
source_slug: learn-you-some-erlang
authors: "Fred Hébert"
chapter: "An Introduction to OTP"
chapter_number: 14
pdf_page: null
section: "Specific vs. Generic"
extraction_confidence: high
aliases:
  - "OTP framework"
  - "Open Telecom Platform"
  - "specific vs generic"
prerequisites:
  - otp-behaviour
extends: []
related:
  - gen-server
  - otp-callback-module
contrasts_with: []
answers_questions:
  - "What is the OTP framework and why use it?"
  - "What concepts precede building an OTP application?"
---

# The OTP Way

## Quick Definition

The OTP way is the philosophy of separating the generic, reusable parts of concurrent code into well-tested behaviour libraries, leaving developers to write only the application-specific callbacks.

## Core Definition

OTP stands for Open Telecom Platform, "though these days it's more about software that has the properties of telecom applications than telecom itself." The chapter frames it: doing concurrency manually — links, monitors, servers, timeouts, trapping exits, hot code loading, naming, supervision — "is time consuming and error prone." OTP "takes care of this by grouping these essential practices into a set of libraries that have been carefully engineered and battle hardened over the years." The core idea, stated in "Specific vs. Generic," is "taking all the generic components, extracting them in libraries, making sure they work well, and then reusing that code when possible. Then all that's left to do is focus on the specific stuff." Benefits: reduced complexity, fewer bugs (fixed once for all users), easier testing, instant recognizability, and shared optimization — when the common backend is improved, every process using it speeds up (Hébert, ch. 14, "An Introduction to OTP," "Specific vs. Generic").

## Prerequisites

- **OTP behaviour** — Behaviours are the concrete mechanism by which the OTP way is realized

## Key Properties

1. OTP = Open Telecom Platform; now about software with telecom-grade properties
2. The OTP way separates generic process code from application-specific code
3. Generic parts are extracted into behaviour libraries, tested, and reused
4. Developers focus only on the specific callbacks
5. Benefits: less complexity, fewer bugs (fixed once), easier testing, instant recognizability
6. Shared backend means a single optimization benefits every process using it
7. OTP behaviours have years of production hardening behind them

## Construction / Recognition

## To Follow the OTP Way

1. Recognize the common pattern your process implements (server, FSM, event handler, supervisor)
2. Use the matching OTP behaviour instead of hand-writing the machinery
3. Write only the specific callbacks in your module
4. Rely on the behaviour for spawning, the loop, timeouts, error handling, and code loading
5. Trust the battle-tested generic code rather than re-implementing it

## Examples

> **Generic/specific split** (ch. 14): the hand-written `my_server` plus `kitty_server2` callback module "demonstrates the core of OTP (conceptually speaking)."
>
> **Fewer bugs** (ch. 14): "if all these servers share the same common `my_server` abstraction, you substantially reduce that complexity... do it in one place for all servers."
>
> **Shared optimization** (ch. 14): "when someone optimizes that single backend to make it a little faster, every process using it out there will run a little faster, too."

## Relationships

## Builds Upon

- **OTP behaviour** — The vehicle through which the OTP way is applied

## Related

- **gen_server** — The canonical OTP behaviour demonstrating the generic/specific split
- **OTP callback module** — The "specific" code the OTP way leaves to the developer

## Common Errors

- **Error**: Hand-writing process machinery for every server in a system
  **Correction**: Use shared behaviours so there is one generic implementation to test and maintain
- **Error**: Treating OTP as optional boilerplate
  **Correction**: OTP encodes hard-won practices; "every Erlang programmer should use them"

## Common Confusions

- **Confusion**: Thinking OTP is only for telecom software
  **Clarification**: OTP is now about general software with telecom-grade reliability properties
- **Confusion**: Believing abstraction here is "abstraction for abstraction's sake"
  **Clarification**: For a single small server it may look so, but for larger systems it cuts complexity, bugs, and test effort substantially

## Source Reference

Chapter 14, "An Introduction to OTP," opening section and "Specific vs. Generic."

## Verification Notes

- OTP philosophy and benefits: directly from ch. 14
- Confidence: HIGH — explicitly stated as the chapter's thesis
