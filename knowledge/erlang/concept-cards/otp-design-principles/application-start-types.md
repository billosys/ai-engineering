---
# === CORE IDENTIFICATION ===
concept: Application Start Types
slug: application-start-types

# === CLASSIFICATION ===
category: applications-releases
subcategory: application-runtime
tier: intermediate

# === PROVENANCE ===
source: "OTP Design Principles"
source_slug: otp-design-principles
authors: "Ericsson AB"
chapter: "Applications"
chapter_number: null
pdf_page: null
section: "Application Start Types"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "start type"
  - "permanent/transient/temporary"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - application
  - application-controller
extends: []
related:
  - supervision-tree
  - distributed-application
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is an OTP application?"
---

# Quick Definition

Application start types (permanent, transient, and temporary) determine the consequences when an application terminates: permanent termination brings down the entire runtime system, transient termination does so only on abnormal exit, and temporary termination has no effect on other applications.

# Core Definition

According to the OTP Design Principles "Applications" chapter, the start type is defined when starting an application via `application:start(Application, Type)`. The source defines three types: "If a permanent application terminates, all other applications and the runtime system are also terminated." "If a transient application terminates with reason `normal`, this is reported but no other applications are terminated. If a transient application terminates abnormally, that is with any other reason than `normal`, all other applications and the runtime system are also terminated." "If a temporary application terminates, this is reported but no other applications are terminated." The default type is `temporary`.

# Prerequisites

- **Application** — start types control the behavior when an application terminates.
- **Application Controller** — the controller enforces start type semantics.

# Key Properties

1. **permanent** — if the application terminates (for any reason), all other applications and the runtime system are also terminated.
2. **transient** — if the application terminates normally, only a report is generated. If it terminates abnormally (reason other than `normal`), all other applications and the runtime system are also terminated.
3. **temporary** — if the application terminates (for any reason), only a report is generated. No other applications are affected. This is the default.
4. Specified via `application:start(Application, Type)`.
5. `application:start(Application)` is equivalent to `application:start(Application, temporary)`.
6. Explicit stop via `application:stop/1` never affects other applications, regardless of start type.
7. The transient mode has little practical use because supervision tree termination sets the reason to `shutdown`, not `normal`.

# Construction / Recognition

## To Construct/Create:
1. Start with a specific type: `application:start(myapp, permanent)`.
2. Or use the default (temporary): `application:start(myapp)`.
3. In release boot scripts, the start type can be configured per application.

## To Identify/Recognize:
1. The second argument to `application:start/2`.
2. Determines system behavior on application termination.
3. Visible in boot scripts for release configurations.

# Context & Application

Start types are critical for production systems. Core applications that the system cannot function without should be started as `permanent` — if they crash, the system terminates cleanly rather than running in a degraded state. Optional or auxiliary applications can be started as `temporary`. The `transient` type is noted as having little practical use because supervision trees terminate with reason `shutdown`, which is abnormal.

# Examples

**Example 1** (applications.md, "Application Start Types"): Starting an application with a specific type:
```erlang
application:start(Application, Type)
```
Where `Type` is `permanent`, `transient`, or `temporary`.

**Example 2** (applications.md, "Application Start Types"): The source notes that `application:start(Application)` is the same as `application:start(Application, temporary)`.

**Example 3** (applications.md, "Application Start Types"): An important caveat: "An application can always be stopped explicitly by calling `application:stop/1`. Regardless of the mode, no other applications are affected."

# Relationships

## Builds Upon
- **Application** — start types modify application termination behavior.
- **Application Controller** — the controller enforces the consequences of each start type.

## Enables
- No specific concepts — start types are a configuration choice, not a building block.

## Related
- **Supervision Tree** — the note about `transient` being impractical relates to how supervision trees terminate with reason `shutdown`.
- **Distributed Application** — distributed applications use start types in conjunction with failover and takeover.

## Contrasts With
- The three types contrast with each other: permanent (always fatal), transient (fatal only on abnormal termination), temporary (never fatal).

# Common Errors

- **Error**: Using `transient` expecting it to silently handle supervision tree crashes.
  **Correction**: The source warns: "The transient mode is of little practical use, since when a supervision tree terminates, the reason is set to `shutdown`, not `normal`." A transient application with a crashing supervision tree will bring down the runtime system.

# Common Confusions

- **Confusion**: Thinking `application:stop/1` triggers the start type behavior (e.g., bringing down the system for a permanent app).
  **Clarification**: "An application can always be stopped explicitly by calling `application:stop/1`. Regardless of the mode, no other applications are affected." Start type consequences only apply to unexpected termination.

# Source Reference

OTP Design Principles, "Applications" chapter, "Application Start Types" section (applications.md).

# Verification Notes

- Definition source: Directly quoted from applications.md "Application Start Types" section for all three types.
- Confidence rationale: High — all three types explicitly defined with clear behavioral descriptions.
- Uncertainties: None.
- Cross-reference status: References application, application-controller, supervision-tree, distributed-application.
