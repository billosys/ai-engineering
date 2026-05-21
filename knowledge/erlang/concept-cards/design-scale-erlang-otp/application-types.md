---
# === CORE IDENTIFICATION ===
concept: Application Types
slug: application-types

# === CLASSIFICATION ===
category: applications-releases
subcategory: applications
tier: intermediate

# === PROVENANCE ===
source: "Designing for Scalability with Erlang/OTP"
source_slug: design-scale-erlang-otp
authors: "Francesco Cesarini & Steve Vinoski"
chapter: "Applications"
chapter_number: 8
pdf_page: 222
section: "Application Types and Termination Strategies"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "application termination strategies"
  - "permanent application"
  - "transient application"
  - "temporary application"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - otp-application
extends: []
related:
  - restart-type
contrasts_with:
  - restart-type

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is an OTP application?"
  - "How do I package, start, and configure a release?"
---

# Quick Definition

An application type — `temporary`, `transient`, or `permanent` — determines what happens to the rest of the node when that application terminates: nothing, or the whole VM coming down.

# Core Definition

The application type determines what happens to the virtual machine and to other applications within it when an application terminates (Cesarini & Vinoski, p. 220). Three types exist: `temporary` (termination, for any reason, does not affect other applications or the VM); `transient` (termination with reason `normal` does not affect others, but an abnormal termination terminates other applications and the VM); and `permanent` (any termination, normal or abnormal, terminates all other applications and the VM). `temporary` is the default assigned by `application:start(Name)`. Stopping an application with `application:stop/1` has no effect on other applications regardless of type (pp. 220-221).

# Prerequisites

- **OTP application** — Application types classify how an application's termination affects the node.

# Key Properties

1. Three types: `temporary`, `transient`, `permanent`.
2. `temporary` — termination never affects other applications or the VM (the default for `application:start/1`).
3. `transient` — normal termination is harmless; abnormal termination brings down other applications and the VM.
4. `permanent` — any termination brings down other applications and the VM.
5. `application:stop/1` is exempt — it never affects other applications, regardless of type.
6. The `transient` type is relevant mainly when writing your own supervisor behavior, since supervisors terminate with reason `shutdown`.

# Construction / Recognition

## To Construct/Create:
1. Set the type when starting an application (e.g. in release start scripts).
2. In proper OTP releases, make all applications `permanent`.

## To Identify/Recognize:
1. The `type:` line in an application's exit info report.
2. The type argument used when starting the application.

# Context & Application

- **Typical contexts**: Release start scripts; the SASL exit info report.
- **Common applications**: Ensuring the node goes down if a critical application dies.
- **Historical/stylistic notes**: The book states that in proper OTP releases all applications tend to be `permanent` — top-level supervisors should never terminate, and when they do the whole node is taken down (p. 221).

# Examples

**Example 1** (p. 220): Stopping `sasl` produces an info report showing `type: temporary` — the default assigned by `application:start(Name)`.

## Worked Example

The exit info report revealing the application type (p. 220):

```text
=INFO REPORT==== 17-Feb-2014::19:51:23 ===
   application: sasl
   exited: stopped
   type: temporary
```

# Relationships

## Builds Upon
- *(none)*

## Enables
- *(none)*

## Related
- **Restart type** — Child restart types reuse the names `permanent`/`transient`/`temporary` with analogous (but distinct) meaning.

## Contrasts With
- **Restart type** — Restart type governs whether a *child process* restarts; application type governs whether the *node* survives an application's termination.

# Common Errors

- **Error**: Leaving business-logic applications as `temporary` in a production release.
  **Correction**: In proper OTP releases make applications `permanent`, so a failed restart strategy takes the node down rather than leaving it degraded.

# Common Confusions

- **Confusion**: Thinking `application:stop/1` triggers the type's termination behavior.
  **Clarification**: `application:stop/1` never affects other applications, irrespective of type; the type matters only for unplanned termination.

- **Confusion**: Confusing the application `transient` type with the child `transient` restart type.
  **Clarification**: They share a name but apply at different scopes — node-wide application termination versus a single child's restart.

# Source Reference

Chapter 8: Applications, "Application Types and Termination Strategies," pages 220-221.

# Verification Notes

- Definition source: Direct adaptation from pp. 220-221.
- Confidence rationale: HIGH — explicitly defined with all three types described.
- Uncertainties: None.
- Cross-reference status: Verified against planned card slugs for this source.
- Re-extraction notes: Fresh extraction — no pre-existing card for this source.
</content>
