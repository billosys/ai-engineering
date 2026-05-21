---
# === CORE IDENTIFICATION ===
concept: Distribution Security
slug: distribution-security

# === CLASSIFICATION ===
category: production-ops
subcategory: network-security
tier: advanced

# === PROVENANCE ===
source: "OTP Design Principles"
source_slug: otp-design-principles
authors: "Ericsson AB"
chapter: "Secure Coding Guidelines"
chapter_number: null
pdf_page: null
section: "Rules / Secure Coding Standard"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "Erlang distribution hardening"
  - "DEP-001"
  - "EPMD security"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - erlang-threat-model
  - ssl-tls-security
extends: []
related:
  - crypto-application-security
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How should Erlang distribution be secured for untrusted networks?"
  - "Why is the Erlang distribution cookie not real authentication?"
  - "What risks does EPMD pose?"
  - "How do you disable or replace EPMD?"
  - "What happens when a malicious node joins an Erlang cluster?"
  - "What are alternatives to default Erlang distribution?"
---

# Quick Definition

Erlang distribution is not secure by default -- it uses unencrypted TCP with a cookie mechanism that only prevents accidental cluster mixing, not malicious access. For untrusted networks, distribution must be configured to use TLS with client certificate verification, EPMD should be disabled or replaced, and all nodes in a cluster must be fully trusted since they gain complete access to all other nodes.

# Core Definition

The Secure Coding Guidelines state under DEP-001 (priority: Critical): "The builtin Erlang distribution makes it possible to easily and transparently communicate between Erlang nodes. By default, communication is performed over an unencrypted TCP connection with a rudimentary cookie based authentication only present in order to prevent mistakes. This configuration should only be used in a trusted network." The document further warns: "all nodes admitted into an Erlang cluster must be trusted. Once a node is connected to the cluster, it gains complete access to the resources and operations of all other nodes, making node trustworthiness a critical security consideration."

# Prerequisites

- **Erlang Threat Model** -- understanding that all connected nodes are assumed trusted is fundamental.
- **SSL/TLS Security** -- TLS is the recommended mechanism for securing distribution.

# Key Properties

1. **Not secure by default** -- default distribution uses unencrypted TCP; the cookie mechanism only prevents accidental mixing, not attacks.
2. **All nodes must be trusted** -- once connected, a node has complete, unrestricted access to all resources and operations on all other nodes.
3. **TLS with client certificates** -- for untrusted networks, configure distribution to use TLS with client certificate verification.
4. **EPMD information leak** -- the Erlang Port Mapper Daemon responds to unauthenticated requests and can leak information about what nodes exist and their listening ports (CWE-668, CWE-200).
5. **Disable or replace EPMD** -- implement a custom EPMD module using another port lookup scheme; the simplest approach is a statically assigned port with no registration.
6. **Rule priority: Critical** -- this is one of the highest-priority rules in the secure coding standard.
7. **Alternatives** -- if distribution is not required, the `ssh` and `ssl` applications provide secure communication; incoming data must still be validated and sanitized.
8. **Related CWEs and OWASP risks** -- CWE-200 (Sensitive Information Exposure), CWE-668 (Exposure of Resource to Wrong Sphere), OWASP A01:2025, A02:2025, API2:2023, API6:2023, API8:2023.

# Construction / Recognition

## To Apply:
1. **Never expose default distribution on untrusted networks** -- this is the cardinal rule.
2. **Configure TLS distribution** -- follow `ssl_distribution.html` to set up TLS with client certificate verification.
3. **Disable default EPMD** -- use the `-start_epmd false` flag.
4. **Implement custom EPMD module** -- create a module implementing the `erl_epmd` behaviour with a custom port lookup scheme.
5. **Enable custom EPMD** -- configure via the `epmd_module` kernel application parameter.
6. **Simplest secure approach** -- use a statically assigned port, skip node registration, and assume nodes listen on that port (one node per IP).
7. **Verify node trustworthiness** -- ensure only authorized nodes can join the cluster through TLS client certificates.

## To Recognize:
1. Erlang distribution running without TLS on a network that is not fully trusted.
2. EPMD running and accessible on a network-facing interface.
3. Cookie-based authentication used as the sole security measure for distribution.

# Context & Application

Distribution security is referenced more frequently than any other concept in the CWE and OWASP commentary sections of the Secure Coding Guidelines. It appears in the discussions of CWE-862 (Missing Authorization), CWE-863 (Incorrect Authorization), CWE-200 (Sensitive Information Exposure), CWE-306 (Missing Authentication), CWE-276 (Incorrect Default Permissions), CWE-287 (Improper Authentication), CWE-732 (Incorrect Permission Assignment), OWASP A01:2025, A02:2025, API2:2023, API6:2023, and API8:2023. This pervasive referencing underscores that insecure distribution is the single most impactful security misconfiguration in Erlang systems.

# Examples

**Example 1** (secure_coding.md, DEP-001): "By default, communication is performed over an unencrypted TCP connection with a rudimentary cookie based authentication only present in order to prevent mistakes. This configuration should only be used in a trusted network."

**Example 2** (secure_coding.md, DEP-001): "Note that the Erlang Port Mapper Daemon (EPMD) service will respond to unauthenticated requests, and can by this leak information about what Erlang nodes exist and what ports they are listening on. You are therefore advised to disable the default EPMD and implement your own EPMD module using another port lookup scheme."

**Example 3** (secure_coding.md, DEP-001): "The simplest solution, assuming only one Erlang node per IP address, would be to use a statically assigned port, skip registration of nodes, and just assume that a node will be listening on that port."

# Relationships

## Builds Upon
- **Erlang Threat Model** -- distribution security requirements flow directly from the threat model's assumption that all connected nodes are trusted
- **SSL/TLS Security** -- TLS is the recommended mechanism for securing distribution

## Enables
- No concepts directly enabled.

## Related
- **Crypto Application Security** -- TLS distribution depends on properly configured cryptographic infrastructure

## Contrasts With
- No direct contrasts in source.

# Common Errors

- **Error**: Exposing default Erlang distribution on a network accessible to untrusted parties.
  **Correction**: Configure TLS with client certificate verification for all distribution on untrusted networks. This is a Critical-priority rule.

- **Error**: Relying on the cookie mechanism as a security measure.
  **Correction**: The cookie "merely prevents the unintentional mixing of Erlang clusters on the same network." It is not authentication. Use TLS client certificates for actual authentication.

- **Error**: Leaving EPMD running on a network-facing interface.
  **Correction**: Disable the default EPMD and implement a custom EPMD module, or use statically assigned ports.

# Common Confusions

- **Confusion**: Thinking that distribution can be partially secured by trusting some nodes more than others.
  **Clarification**: "Once a node is connected to the cluster, it gains complete access to the resources and operations of all other nodes." There is no concept of partial trust within a cluster. All nodes must be fully trusted.

- **Confusion**: Believing the Erlang cookie provides meaningful security analogous to a password.
  **Clarification**: The cookie is a shared secret that prevents accidental connections, not a security mechanism. It is transmitted in a simple protocol without encryption by default.

# Source Reference

OTP Design Principles, Secure Coding Guidelines, DEP-001 rule (secure_coding.md, lines 558-601). Also referenced in multiple CWE entries (CWE-862, CWE-863, CWE-200, CWE-306, CWE-276, CWE-287, CWE-732) and OWASP entries (A01:2025, A02:2025, API2:2023, API6:2023, API8:2023).

# Verification Notes

- Definition source: Directly quoted from the DEP-001 rule section.
- Confidence rationale: High -- Critical-priority rule, most-referenced concept in the CWE and OWASP sections.
- Uncertainties: None.
- Cross-reference status: Referenced by CWE-200, CWE-668, CWE-862, CWE-863, CWE-306, CWE-276, CWE-287, CWE-732, OWASP A01:2025, A02:2025, API2:2023, API6:2023, API8:2023.
