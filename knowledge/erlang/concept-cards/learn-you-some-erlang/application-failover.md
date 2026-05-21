---
concept: Application Failover
slug: application-failover
category: fault-tolerance
subcategory: distribution
tier: advanced
source: "Learn You Some Erlang for Great Good!"
source_slug: learn-you-some-erlang
authors: "Fred Hébert"
chapter: "Distributed OTP Applications"
chapter_number: 27
pdf_page: null
section: "Taking and Failing Over"
extraction_confidence: high
aliases:
  - "failover"
  - "failing over"
prerequisites:
  - distributed-otp-application
  - distributed-application-config
related:
  - application-takeover
contrasts_with:
  - application-takeover
answers_questions:
  - "What is application failover in distributed OTP?"
  - "What happens when the node running a distributed application dies?"
---

# Application Failover

## Quick Definition

Failover is the act of restarting a distributed OTP application somewhere other than where it was running, after the node running it has died.

## Core Definition

A failover is the idea of restarting an application somewhere other than where it stopped running. When the node running a distributed OTP application dies, the backup nodes notice (after a configured timeout), and the next-highest-priority backup node starts running the application instead. This avoids interruption of services by moving subsystems around. Failover is a particularly valid strategy when you have redundant hardware: you run something on a main server, and if it fails, the work moves to a backup (Chapter 27, "Taking and Failing Over").

## Prerequisites

- **Distributed OTP application** — Failover is a behavior provided by distributed applications
- **Distributed application config** — The `distributed` kernel tuple's node list determines which backup node takes over and the timeout before it does

## Key Properties

1. Triggered when the node currently running the application dies
2. The application restarts on the next node in the configured priority/node list
3. There is a brief window during which nothing runs, governed by the `TimeOutBeforeRestart` value in the `distributed` config tuple
4. Failover cascades: if the backup also dies, the next backup takes over
5. The application's `start/2` callback is invoked with `start(normal, [])` on the new node

## Recognition

In the `m8ball` example, killing node `a` (the main node) leaves nothing running for a brief moment; after the 5000 ms timeout, node `b` shows the application as running via `application:which_applications()`. Killing `b` next causes `c` to start running it.

## Context & Application

Failover is most interesting in deployments with dedicated main and backup machines. In larger deployments with many servers absorbing each other's load, failover is less central. The author warns that constantly restarting applications this way risks losing important state, which the developer must plan for.

## Examples

**Example** (Chapter 27, "Making the Application Distributed"): With `{distributed, [{m8ball, 5000, [a@ferdmbp, {b@ferdmbp, c@ferdmbp}]}]}`, killing `a` causes `b` to take over after 5 seconds; `application:which_applications()` on `b` then lists `m8ball`.

## Relationships

## Builds Upon

- **Distributed OTP application** — Failover is one of the two recovery mechanisms a distributed application provides

## Contrasts With

- **Application takeover** — Takeover happens when a *more important* node comes back and reclaims the app; failover happens when the running node *dies* and a backup picks it up

## Common Errors

- **Error**: Expecting zero downtime during failover
  **Correction**: There is a brief gap (the configured restart timeout) during which nothing runs

## Common Confusions

- **Confusion**: Confusing failover with takeover
  **Clarification**: Failover moves the app to a backup because the running node died; takeover moves it back to a higher-priority node that has come back online

## Source Reference

Chapter 27: Distributed OTP Applications, section "Taking and Failing Over" and the demonstration in "Making the Application Distributed."

## Verification Notes

- Definition: Direct adaptation from "Taking and Failing Over"
- Key Properties: All explicit in the chapter or the m8ball demonstration
- Confidence: HIGH — explicitly defined and demonstrated
- Cross-references: verified against planned cards in this extraction
