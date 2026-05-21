---
# === CORE IDENTIFICATION ===
concept: OTP Compatibility
slug: otp-compatibility

# === CLASSIFICATION ===
category: applications-releases
subcategory: support-policy
tier: intermediate

# === PROVENANCE ===
source: "OTP System Principles"
source_slug: otp-system-principles
authors: "Ericsson AB"
chapter: "Support, Compatibility, Deprecations, and Removal"
chapter_number: null
pdf_page: null
section: "Compatibility"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - OTP compatibility guarantees
  - OTP backward compatibility

# === TYPED RELATIONSHIPS ===
prerequisites:
  - otp-supported-releases
extends: []
related:
  - otp-deprecation-policy
  - otp-removal-policy
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What compatibility guarantees does OTP provide between releases?"
  - "Can Erlang nodes of different OTP versions communicate?"
  - "Can compiled BEAM code run on a different OTP version?"
  - "What can trigger incompatible changes in OTP?"
---

# Quick Definition

OTP provides varying levels of compatibility guarantees across releases: Erlang distribution is compatible across at least two preceding and two subsequent releases, compiled BEAM code can load on at least two subsequent releases, and APIs are compatible between releases -- though security issues, bug fixes, and severe design issues may trigger exceptions.

# Core Definition

The OTP team strives to remain as compatible as possible, even in cases where no compatibility guarantees are given. Different parts of the system are handled differently regarding compatibility:

- **Erlang Distribution**: Erlang nodes can communicate across at least two preceding and two subsequent releases.
- **Compiled BEAM Code, NIF Libraries, and Drivers**: Compiled code can be loaded on at least two subsequent releases. Loading on previous releases is not supported.
- **APIs**: Compatible between releases.
- **Compiler Warnings**: New warnings may be issued between releases.
- **Command Line Arguments**: Incompatible changes may occur between releases.
- **OTP Build Procedures**: Incompatible changes may occur between releases.

Under certain circumstances, incompatible changes might be introduced even in parts that should be compatible, triggered by security issues, bug fixes, or severe previous design issues.

# Prerequisites

- Understanding of OTP's supported releases policy

# Key Properties

1. Erlang distribution protocol: compatible across a five-release window (two preceding, current, two subsequent)
2. Compiled BEAM code: forward-compatible for at least two releases, but NOT backward-compatible
3. APIs: fully compatible between releases
4. Compiler warnings: no compatibility guarantee (new warnings may appear)
5. Command line arguments: no compatibility guarantee
6. OTP build procedures: no compatibility guarantee
7. Best performance requires compiling on the same release as the deployment target
8. Peripheral, trace, and debug functionality has greater risk of incompatible changes than core language and library functionality

# Construction / Recognition

## To Construct/Create:
1. Not applicable -- this is a policy description, not a constructed artifact

## To Identify/Recognize:
1. Consult the "Upcoming Potential Incompatibilities" documentation page for planned changes
2. Review release notes for any incompatible changes introduced in a release
3. Test compiled code on the target release before deploying

# Context & Application

Understanding OTP compatibility guarantees is critical for planning cluster upgrades, deployment strategies, and build pipelines. The distribution compatibility window means rolling upgrades across a cluster can span at most two major versions. The forward-only BEAM code compatibility means that pre-compiled releases can be deployed on newer OTP versions (within two releases) but not older ones. The exceptions for security, bugs, and design issues mean that even "guaranteed compatible" areas may occasionally break.

# Examples

**Example 1** (distribution compatibility): An Erlang cluster running OTP 25 can communicate with nodes running OTP 23, 24, 26, or 27 (two preceding and two subsequent releases). Nodes running OTP 22 or OTP 28 would not be guaranteed to interoperate.

**Example 2** (BEAM code compatibility): Code compiled on OTP 25 can be loaded on OTP 26 and OTP 27, but loading it on OTP 24 (a previous release) is not supported. For optimal performance, the code should be compiled on the same version it runs on.

**Example 3** (incompatibility triggers): Security issues may force incompatible changes even in a patch release. Bug fixes may also introduce incompatible changes in patches (OTP will not be "bug-compatible"). Severe design issues may trigger incompatible changes, but these are never introduced in patches -- only in subsequent releases.

# Relationships

## Builds Upon
- **otp-supported-releases** -- the support policy determines which releases are active and therefore relevant for compatibility

## Enables
- Planning rolling upgrades in distributed systems
- Understanding the safe version range for mixed-version clusters

## Related
- **otp-deprecation-policy** -- deprecation is a mechanism for managing compatibility transitions
- **otp-removal-policy** -- removal is the final step when compatibility with old functionality is no longer maintained

## Contrasts With
- None

# Common Errors

- **Error**: Assuming compiled BEAM code can be loaded on previous OTP releases
  **Correction**: Loading on previous releases is explicitly not supported. BEAM code is only forward-compatible (loadable on subsequent releases).

- **Error**: Assuming command line arguments are stable across releases
  **Correction**: Command line arguments have no compatibility guarantee and may change incompatibly between releases.

- **Error**: Expecting no breaking changes within patch releases
  **Correction**: Security issues and bug fixes may introduce incompatible changes even in patch releases.

# Common Confusions

- **Confusion**: API compatibility means nothing ever changes
  **Clarification**: APIs are compatible between releases, but security issues, bug fixes, and severe design issues can trigger exceptions. Additionally, "compatible" does not cover peripheral, trace, and debug APIs, which have greater risk of change.

- **Confusion**: Distribution compatibility means unlimited version mixing in a cluster
  **Clarification**: The guarantee covers exactly two releases in each direction. Nodes more than two releases apart are not guaranteed to communicate.

# Source Reference

"Compatibility" section, "Support, Compatibility, Deprecations, and Removal" chapter, "OTP System Principles" documentation.

# Verification Notes

- Definition source: direct (detailed compatibility table explicitly provided in source text)
- Confidence rationale: The source provides specific, enumerated guarantees for each system component
- Uncertainties: none
- Cross-reference status: references "Upcoming Potential Incompatibilities" documentation page (unverified)
