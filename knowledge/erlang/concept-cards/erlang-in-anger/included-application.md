---
concept: Included Application
slug: included-application
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
extraction_confidence: medium
aliases: []
prerequisites:
  - otp-application
  - application-start-types
extends: []
related:
  - supervisor-restart-strategy
contrasts_with:
  - application-start-types
answers_questions:
  - "What is an included application?"
---

# Quick Definition

An included application is an OTP application started under another application's own supervisor, so the parent controls its restart strategy rather than the application controlling itself.

# Core Definition

From Chapter 2, section "Application Strategies": "It is also possible to start an application as an *included application*, which starts it under your own OTP supervisor with its own strategy to restart it."

# Prerequisites

- `otp-application` — an included application is still an OTP application.
- `application-start-types` — an included application is an alternative to standalone start with a `permanent`/`transient`/`temporary` type.

# Key Properties

1. The application is started under another application's supervisor rather than standalone.
2. The parent supervisor's strategy governs how the included application is restarted.
3. It is an alternative to the standalone `permanent`/`transient`/`temporary` start types.

# Construction / Recognition

Rather than starting the application standalone, embed it under one of your own supervisors, giving you direct control over its restart behaviour through that supervisor's restart strategy.

# Context & Application

Used when you want a finer-grained restart policy for a dependency than the coarse node-level `permanent`/`transient`/`temporary` semantics allow — folding the dependency's lifecycle into your own supervision tree.

# Examples

From Chapter 2, section "Application Strategies": the book mentions the included application as the option that "starts it under your own OTP supervisor with its own strategy to restart it," immediately after defining the three standalone start types.

# Relationships

## Builds Upon
- `otp-application` — the thing being included.

## Enables
Custom, supervisor-driven restart control over an embedded application.

## Related
- `supervisor-restart-strategy` — the parent supervisor's strategy governs the included application.

## Contrasts With
- `application-start-types` — standalone start uses node-level `permanent`/`transient`/`temporary` semantics; an included application is instead governed by a parent supervisor.

# Common Errors

- Expecting node-level `permanent`/`transient`/`temporary` behaviour from an included application — its lifecycle is governed by the parent supervisor instead.

# Common Confusions

- An included application is not a dependency listed in the `applications` tuple in the ordinary sense — it is specifically started under another application's supervisor.

# Source Reference

Chapter 2: Building Open Source Erlang Software, Section "Application Strategies". (No PDF pages — this source has none.)

# Verification Notes

- Definition source: quoted from Chapter 2, section "Application Strategies."
- Confidence rationale: medium — the source mentions the concept only briefly, in a single sentence, without elaboration.
- Uncertainties: the source does not detail the mechanics of declaring an included application.
- Cross-reference status: Verified
