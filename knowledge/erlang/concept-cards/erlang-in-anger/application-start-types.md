---
concept: Application Start Types
slug: application-start-types
category: applications-releases
subcategory: application-lifecycle
tier: intermediate
source: "Stuff Goes Bad: Erlang in Anger"
source_slug: erlang-in-anger
authors: "Fred Hébert"
chapter: "Building Open Source Erlang Software"
chapter_number: 2
pdf_page: null
section: "Application Strategies"
extraction_confidence: high
aliases:
  - "Application strategies"
  - "permanent/transient/temporary"
prerequisites:
  - otp-application
extends: []
related:
  - included-application
  - otp-release
contrasts_with: []
answers_questions:
  - "What are the three application strategies? What do they do?"
  - "What is the difference between permanent, transient, and temporary applications?"
---

# Quick Definition

An application start type — `permanent`, `transient`, or `temporary` — determines what happens to the whole node when that OTP application terminates.

# Core Definition

From Chapter 2, section "Application Strategies": "Each OTP application can be started in 3 ways: temporary, transient, permanent, either by doing it manually in `application:start(Name, Type)`, or in the config file for your release":

- `permanent`: if the app terminates, the entire system is taken down — excluding manual termination via `application:stop/1`.
- `transient`: if the app terminates for reason `normal`, that's fine; any other termination reason shuts down the entire system.
- `temporary`: the application is allowed to stop for any reason; it will be reported, but nothing bad happens.

# Prerequisites

- `otp-application` — start types are a property of how an application is started.

# Key Properties

1. Set via `application:start(Name, Type)` or in the release config file.
2. `permanent` — termination (other than a manual `application:stop/1`) takes the whole node down.
3. `transient` — `normal` termination is tolerated; any other reason takes the node down.
4. `temporary` — any termination is tolerated and merely reported.
5. The choice lets you declare which applications are vital to the node and which are not — "a sequence of failures is not a death sentence for the node."

# Construction / Recognition

When dividing a system into applications, classify each one: vital → `permanent`; allowed to stop cleanly only → `transient`; non-essential → `temporary`. Apply the classification in `application:start/2` or the release config.

# Context & Application

Start types are how a release decides its blast radius: which application failures should crash the node (so a supervisor or operator can restart it cleanly) versus which should be quietly absorbed.

# Examples

From Chapter 2, section "Application Strategies": the three types are defined in a list, prefaced by "Once a system has been divided into various OTP applications, it becomes possible to choose which applications are vital or not to the node."

# Relationships

## Builds Upon
- `otp-application` — the unit being started.

## Enables
Node-level fault-tolerance policy across a release.

## Related
- `included-application` — an alternative to standalone start, with a custom restart strategy.
- `otp-release` — start types are commonly set in release config.

## Contrasts With
Nothing directly — the three types contrast with one another.

# Common Errors

- Marking a non-essential application `permanent`, so that its failure needlessly takes the whole node down.
- Marking a vital application `temporary`, so that its silent death leaves the node running in a broken state.

# Common Confusions

- `transient` does not mean "restarted" — it means a `normal` exit is tolerated; any abnormal exit still crashes the node.
- A manual `application:stop/1` never takes the node down, even for a `permanent` application.

# Source Reference

Chapter 2: Building Open Source Erlang Software, Section "Application Strategies". (No PDF pages — this source has none.)

# Verification Notes

- Definition source: quoted from Chapter 2, section "Application Strategies."
- Confidence rationale: high — all three types defined explicitly.
- Uncertainties: none.
- Cross-reference status: Verified
