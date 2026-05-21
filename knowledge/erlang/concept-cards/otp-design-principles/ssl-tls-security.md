---
# === CORE IDENTIFICATION ===
concept: SSL/TLS Security
slug: ssl-tls-security

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
section: "Application-Specific Guidelines"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "Erlang ssl application"
  - "OTP TLS hardening"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - crypto-application-security
extends: []
related:
  - distribution-security
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How is the Erlang ssl application configured securely?"
  - "Should TLS 1.2 be disabled in favor of TLS 1.3?"
  - "What is the cert_keys option for?"
  - "What legacy ssl functionality should be avoided?"
  - "What does 'secure by default' mean for the ssl application?"
---

# Quick Definition

The Erlang `ssl` application is secure by default and should remain so by following its documentation. Legacy functionality should only be enabled when absolutely necessary as it weakens security. Where possible, TLS 1.2 should be disabled in favor of TLS 1.3, and the `cert_keys` option can configure multiple certificate/key pairs for interoperability with legacy systems.

# Core Definition

As stated in the Secure Coding Guidelines: "The ssl application is secure by default and remains so if the recommendations in its documentation is followed. One must be especially careful when enabling legacy functionality, as it weakens security. It should only be done when absolutely necessary." The document further recommends: "If you control both the server and the client, consider disabling the (now old) TLS 1.2 in favor of TLS 1.3."

# Prerequisites

- **Crypto Application Security** -- the ssl application depends on the crypto application for cryptographic primitives.

# Key Properties

1. **Secure by default** -- the ssl application is secure out of the box; following the documentation maintains this property.
2. **Legacy functionality weakens security** -- enabling legacy options should only be done when absolutely necessary.
3. **Prefer TLS 1.3** -- if both server and client are under your control, disable TLS 1.2 in favor of TLS 1.3.
4. **cert_keys option** -- allows configuring more than one certificate/key pair for a client or server, providing "good security while allowing interoperability with legacy systems for a period of time."
5. **TLS Hardening Guide** -- the ssl application documentation includes a dedicated hardening guide (`ssl_hardening.html`).
6. **RSA PKCS-1 padding** -- same restrictions as for the crypto application; use `public_key:sign/4` and `public_key:verify/5` instead of legacy encrypt/decrypt functions.
7. **Debug functionality** -- the `keep_secrets` ssl option should not be used in production; it is explicitly marked as debug functionality (MSC-007).
8. **Potentially unsafe functions** -- `ssl:prf/5` is listed as potentially unsafe; use `ssl:export_key_materials/4` instead.
9. **Distribution security** -- for secure communication between Erlang nodes over untrusted networks, configure distribution to use TLS with client certificate verification.

# Construction / Recognition

## To Apply:
1. Follow the ssl application documentation and TLS Hardening Guide.
2. Do not enable legacy TLS options unless absolutely necessary.
3. If you control both ends, disable TLS 1.2 and use TLS 1.3 exclusively.
4. Use `cert_keys` when interoperability with legacy systems requires multiple certificate/key pairs.
5. Never use the `keep_secrets` option in production.
6. Replace `ssl:prf/5` with `ssl:export_key_materials/4`.
7. For Erlang distribution, configure TLS with client certificate verification per `ssl_distribution.html`.

## To Recognize:
1. Any ssl configuration that enables legacy protocol versions or cipher suites.
2. Use of `keep_secrets` option outside of debugging contexts.
3. Use of deprecated `ssl:prf/5` function.

# Context & Application

The ssl application is the primary mechanism for securing network communication in Erlang systems, including Erlang distribution (see DEP-001). Its "secure by default" design philosophy means that the most common mistake is weakening security by enabling legacy compatibility options. The document references the ssl application in the context of distribution security (DEP-001), OWASP A01:2025 (Broken Access Control), A02:2025 (Security Misconfiguration), and multiple API security risks. The ssh application has its own hardening chapter. The public_key application shares the RSA PKCS-1 padding restrictions with crypto.

# Examples

**Example 1** (secure_coding.md, "ssl Application"): "The cert_keys option can also be used to configure more than one possible certificate/key pair for a client or server, giving good security while allowing interoperability with legacy systems for a period of time."

**Example 2** (secure_coding.md, MSC-007): "Functionality that has been explicitly marked to be used only for debugging, such as erlang:list_to_pid/1 or the keep_secrets ssl option should not be used in production environments, except during interactive debugging."

# Relationships

## Builds Upon
- **Crypto Application Security** -- the ssl application uses the crypto application for cryptographic operations; "The ssl and public_key applications implement most things except for crypto functionality, which is provided by the crypto application"

## Enables
- **Distribution Security** -- TLS from the ssl application is the recommended mechanism for securing Erlang distribution over untrusted networks

## Related
- **Distribution Security** -- distribution should be configured to use TLS with client certificate verification

## Contrasts With
- No direct contrasts in source.

# Common Errors

- **Error**: Enabling legacy TLS versions or cipher suites for broad compatibility without assessing the security impact.
  **Correction**: Only enable legacy functionality when absolutely necessary. Use `cert_keys` for certificate interoperability rather than downgrading protocol versions.

- **Error**: Using the `keep_secrets` option in production code.
  **Correction**: This is debug-only functionality (MSC-007) with "no promises of API stability" that "may change without notice." It should be treated as unsafe in production (DSG-006).

# Common Confusions

- **Confusion**: Thinking that additional configuration is needed to make the ssl application secure.
  **Clarification**: The ssl application is "secure by default." The primary risk is weakening security through explicit configuration changes, not insufficiently hardening a weak default.

# Source Reference

OTP Design Principles, Secure Coding Guidelines, "ssl Application" section (secure_coding.md, lines 329-347), MSC-007 rule (lines 1338-1358), and "Potentially Unsafe Functionality" table entries for ssl:prf/5 (lines 1421-1423).

# Verification Notes

- Definition source: Directly quoted from the "ssl Application" section.
- Confidence rationale: High -- clear, explicit guidance with references to the TLS Hardening Guide for further detail.
- Uncertainties: None. The source is concise about ssl, deferring to the ssl application's own documentation for comprehensive guidance.
- Cross-reference status: References OWASP A01:2025, A02:2025, API2:2023, API6:2023, API8:2023 via DEP-001. Cross-references crypto-application-security, distribution-security.
