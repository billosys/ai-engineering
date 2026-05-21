---
# === CORE IDENTIFICATION ===
concept: Crypto Application Security
slug: crypto-application-security

# === CLASSIFICATION ===
category: production-ops
subcategory: cryptography
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
  - "Erlang crypto module security"
  - "OTP cryptography guidelines"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - erlang-threat-model
extends: []
related:
  - ssl-tls-security
  - distribution-security
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How should the Erlang crypto application be initialized securely?"
  - "Why should crypto:start/0 not be called directly?"
  - "How do you generate cryptographically secure random numbers in Erlang?"
  - "What legacy crypto functions should be avoided?"
  - "Why is crypto:rand_uniform/2 unsafe?"
  - "How should FIPS mode be configured?"
---

# Quick Definition

The Erlang `crypto` application wraps OpenSSL's `libcrypto` library and requires careful initialization via `application:start(crypto)` (not `crypto:start/0`), use of the functional random number API with `crypto:rand_seed_s/0`, and avoidance of legacy RSA PKCS-1 padding functions. Incorrect usage can lead to insecure cryptographic operations.

# Core Definition

The Secure Coding Guidelines specify three critical areas for crypto application security. First, initialization: "In order to make sure that the libcrypto library is configured as expected, make sure not to load the crypto module by any other means than calling application:start(crypto). Any calls to the crypto library will load the module. Make sure not to call any functions in the crypto module, including crypto:start/0 prior to the call to application:start(crypto)." Second, random numbers: "Do not use crypto:rand_uniform/2 since it uses functionality from the OpenSSL libcrypto library that in old versions of the library does not produce cryptographically secure random numbers (CWE-338)." Third, legacy functions: "RSA with PKCS-1 padding is weak and should be avoided."

# Prerequisites

- **Erlang Threat Model** -- understanding trust boundaries and what constitutes unsafe functionality.

# Key Properties

1. **Initialization order** -- `application:start(crypto)` must be called before any use of the `crypto` module; `crypto:start/0` is listed as "Unsafe Functionality."
2. **FIPS mode** -- use the `fips_mode` application parameter instead of `crypto:enable_fips_mode/1` (listed as "Unsafe Functionality").
3. **Insecure random numbers** -- `crypto:rand_uniform/2` (CWE-338) is listed as "Unsafe Functionality"; use `rand:uniform_s/2` with a cryptographically strong generator.
4. **Functional random API preferred** -- `crypto:rand_seed_s/0`/`rand:uniform_s/2` (functional, state-passing) are preferred over `crypto:rand_seed/0`/`rand:uniform/1` (process dictionary-based) to avoid state modification by interleaved calls.
5. **Legacy RSA functions** -- `crypto:private_encrypt/4`, `crypto:private_decrypt/4`, `crypto:public_encrypt/4`, `crypto:public_decrypt/4` with `rsa_pkcs1_padding` option are all listed as "Unsafe Functionality."
6. **Signature alternatives** -- use `crypto:sign/4` and `crypto:verify/5` instead of legacy encrypt/decrypt functions for signatures.
7. **OpenSSL version matters** -- build Erlang/OTP against an up-to-date OpenSSL; only `libcrypto` from OpenSSL is used (not other OpenSSL components).
8. **Static linking option** -- `--disable-dynamic-ssl-lib` statically links `libcrypto` into the crypto NIF library, ensuring the intended version is used.

# Construction / Recognition

## Secure Initialization:
```erlang
%% DO -- proper initialization
application:start(crypto).

%% DO NOT -- bypasses application parameter configuration
crypto:start().

%% DO NOT -- any crypto call loads the module prematurely
crypto:hash(sha256, Data).  %% Before application:start(crypto)
```

## Secure Random Numbers:
```erlang
%% PREFER -- functional API, state not stored in process dictionary
{Seed, State0} = crypto:rand_seed_s(),
{Value, State1} = rand:uniform_s(100, State0).

%% ACCEPTABLE -- but process dictionary state can be modified by interleaved calls
crypto:rand_seed(),
Value = rand:uniform(100).

%% DO NOT -- uses potentially insecure OpenSSL functionality
crypto:rand_uniform(1, 100).
```

## Secure Signatures:
```erlang
%% DO -- use dedicated signature functions
Signature = crypto:sign(rsa, sha256, Data, PrivateKey).
true = crypto:verify(rsa, sha256, Data, Signature, PublicKey).

%% DO NOT -- legacy encrypt with PKCS-1 padding
crypto:private_encrypt(rsa, Data, PrivateKey, rsa_pkcs1_padding).
```

# Context & Application

The crypto application is security-critical infrastructure underlying TLS, SSH, and any application-level cryptographic operations. The Secure Coding Guidelines list six crypto-related entries in the "Unsafe Functionality" table: `crypto:start/0`, `crypto:enable_fips_mode/1`, `crypto:rand_uniform/2`, and four `crypto:*_encrypt/4`/`crypto:*_decrypt/4` functions with `rsa_pkcs1_padding`. The `public_key` application has analogous unsafe functions. The build recommendation (DEP-002) to use `--with-ssl=PATH` and `--disable-dynamic-ssl-lib` ensures the correct OpenSSL version is used, with the note that "only the libcrypto library from OpenSSL will be used and that vulnerabilities in other parts of OpenSSL do not affect Erlang/OTP."

# Examples

**Example 1** (secure_coding.md, "Initializing crypto"): "The libcrypto library from OpenSSL will be loaded and configured when the crypto module is loaded. During loading of the crypto module some crypto application parameters will be read in order to configure the libcrypto library. Such application parameters are only available after the application has been started using the application:start/1 functionality."

**Example 2** (secure_coding.md, "Cryptographically Secure Random Numbers"): "The above mentioned functionality will store a state in the process dictionary of the currently executing process. This state could be modified to select another generator by other functionality called interleaved with calls retrieving random numbers."

# Relationships

## Builds Upon
- **Erlang Threat Model** -- crypto misuse falls under the category of functionality that produces valid-appearing but insecure results

## Enables
- **SSL/TLS Security** -- the ssl application depends on crypto for its cryptographic operations
- **Distribution Security** -- TLS-secured distribution depends on properly configured crypto

## Related
- **SSL/TLS Security** -- the ssl and crypto applications work together; the ssl application implements TLS while crypto provides the primitives

## Contrasts With
- No direct contrasts in source.

# Common Errors

- **Error**: Calling `crypto:start/0` or any crypto function before `application:start(crypto)`.
  **Correction**: Always use `application:start(crypto)` as the first interaction with the crypto application, ensuring application parameters (including FIPS mode) are properly loaded.

- **Error**: Using `crypto:rand_uniform/2` for security-sensitive random number generation.
  **Correction**: Use `crypto:rand_seed_s/0` with `rand:uniform_s/2` for the functional API, or `crypto:rand_seed/0` with `rand:uniform/1` for the process dictionary API.

- **Error**: Using RSA with PKCS-1 padding for signatures.
  **Correction**: Use `crypto:sign/4` and `crypto:verify/5` instead of the legacy encrypt/decrypt functions with `rsa_pkcs1_padding`.

# Common Confusions

- **Confusion**: Thinking `crypto:rand_seed/0` only produces a seed.
  **Clarification**: "Note that crypto:rand_seed/0 not only produces a seed but also selects a generator that will be used by rand:uniform/1."

- **Confusion**: Assuming all of OpenSSL's attack surface applies to Erlang.
  **Clarification**: "Only the libcrypto library from OpenSSL will be used and that vulnerabilities in other parts of OpenSSL do not affect Erlang/OTP. The ssl and public_key applications implement most things except for crypto functionality."

# Source Reference

OTP Design Principles, Secure Coding Guidelines, "crypto Application" section (secure_coding.md, lines 268-327), "Unsafe Functionality" table (lines 1360-1384), and DEP-002 rule (lines 603-656).

# Verification Notes

- Definition source: Directly quoted from the "crypto Application" section and the Unsafe Functionality table.
- Confidence rationale: High -- specific, detailed guidelines with explicit unsafe function listings and CWE references (CWE-338).
- Uncertainties: None.
- Cross-reference status: References CWE-338, OWASP A04:2025. Cross-references ssl-tls-security, distribution-security.
