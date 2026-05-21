---
concept: Application Takeover
slug: application-takeover
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
  - "takeover"
  - "taking over"
prerequisites:
  - distributed-otp-application
  - distributed-application-config
related:
  - application-failover
contrasts_with:
  - application-failover
answers_questions:
  - "What is application takeover in distributed OTP?"
  - "What happens when a higher-priority node comes back online?"
---

# Application Takeover

## Quick Definition

Takeover is the act of a higher-priority node, having come back online, gracefully reclaiming a distributed OTP application from a backup node that was running it.

## Core Definition

Taking over is the act of a previously dead node coming back from the dead, being known (by configuration) to be more important than the backup nodes — maybe it has better hardware — and deciding to run the application again. This is usually done by gracefully terminating the backup application and starting the main one instead (Chapter 27, "Taking and Failing Over").

## Prerequisites

- **Distributed OTP application** — Takeover is a behavior provided by distributed applications
- **Distributed application config** — The `distributed` tuple's node list defines which node is "main" (higher priority) and which are backups

## Key Properties

1. Triggered when a node of higher priority than the current runner rejoins the cluster
2. The application is gracefully terminated on the backup node and restarted on the higher-priority node
3. On the higher-priority node, the application callback's `start/2` is invoked as `start({takeover, OtherNode}, [])`, where `OtherNode` is the node it is taking over from
4. Handling the `{takeover, OtherNode}` clause is the only code change required to make a normal application support takeover
5. As with failover, application state is not preserved across the move unless the developer arranges it

## Recognition

When node `a` (the configured main node) is restarted after `c` had taken over via failover, the app is willingly shut down on `c` and restarted on `a`. The `start/2` callback receives `{takeover, _OtherNode}` rather than `normal`.

## Context & Application

Takeover lets a system prefer a designated primary node — for example, one with better hardware — and return work to it once it recovers. The `m8ball` example handles the takeover clause trivially, simply starting its supervisor, because nothing about the app's behavior changes between a normal start and a takeover.

## Examples

**Example** (Chapter 27, "Making the Application Distributed"): The `m8ball` callback module adds `start({takeover, _OtherNode}, []) -> m8ball_sup:start_link().` alongside the `start(normal, [])` clause, so the supervisor starts the same way whether the app starts fresh or takes over.

## Relationships

## Builds Upon

- **Distributed OTP application** — Takeover is one of the two recovery mechanisms a distributed application provides

## Contrasts With

- **Application failover** — Failover moves the app to a backup because the running node died; takeover moves it back to a recovered higher-priority node and is graceful rather than crash-driven

## Common Errors

- **Error**: Forgetting to add the `start({takeover, OtherNode}, [])` clause to the application callback module
  **Correction**: Without that clause, the application crashes when OTP attempts a takeover

## Common Confusions

- **Confusion**: Thinking takeover and failover are the same
  **Clarification**: Failover is a reaction to a crash (a backup steps up); takeover is a planned, graceful return of the app to a preferred node

## Source Reference

Chapter 27: Distributed OTP Applications, section "Taking and Failing Over" and the `start/2` clause in "Making the Application Distributed."

## Verification Notes

- Definition: Direct adaptation from "Taking and Failing Over"
- Key Properties: All explicit in the chapter
- Confidence: HIGH — explicitly defined with a code example
- Cross-references: verified against planned cards in this extraction
