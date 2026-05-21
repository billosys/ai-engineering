---
# === CORE IDENTIFICATION ===
concept: Erlang Threat Model
slug: erlang-threat-model

# === CLASSIFICATION ===
category: fault-tolerance
subcategory: security-model
tier: intermediate

# === PROVENANCE ===
source: "OTP Design Principles"
source_slug: otp-design-principles
authors: "Ericsson AB"
chapter: "Secure Coding Guidelines"
chapter_number: null
pdf_page: null
section: "Background"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "BEAM security model"
  - "Erlang security assumptions"

# === TYPED RELATIONSHIPS ===
prerequisites: []
extends: []
related:
  - erlang-memory-safety
  - native-code-safety
  - distribution-security
  - supervision-tree
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What does Erlang protect against from a security perspective?"
  - "What does Erlang NOT protect against?"
  - "What are the trust assumptions in an Erlang system?"
  - "How does the BEAM's threat model differ from sandboxed runtimes?"
---

# Quick Definition

The Erlang threat model defines what the BEAM runtime system protects against (memory safety, process isolation, well-defined behavior) and what it does not protect against (untrusted loaded code, excessive resource usage, connected nodes in distribution).

# Core Definition

As described in the Secure Coding Guidelines: all loaded code is assumed to be trusted, all nodes connected through Erlang distribution are assumed to be trusted, and inappropriate usage of functionality is not guaranteed to produce sensible results. Conversely, Erlang provides memory safety, process isolation, well-defined behavior for all possible inputs, and arbitrary precision arithmetic. The document uses the terms "trusted" and "untrusted" to mean "fully trusted" and "not fully trusted," respectively, stating that "anything that is not fully and completely trusted must be considered as untrusted as something given to you by a malicious actor."

# Prerequisites

This is a foundational security concept with no prerequisites within this source.

# Key Properties

1. **All loaded code is trusted** -- there is no built-in sandboxing mechanism for running untrusted Erlang code; a malicious BEAM module can do anything including crashing the VM.
2. **All connected nodes are trusted** -- nodes in an Erlang cluster have unrestricted access to all other connected systems; there is no authentication built into the default distribution protocol.
3. **Valid-appearing but nonsensical input** may produce valid-appearing garbage rather than crashing, because many function arguments are assumed to be trusted.
4. **Undocumented functionality** can result in almost anything happening.
5. **Memory safety is guaranteed** -- CWEs related to spatial and temporal memory safety cannot occur in pure Erlang.
6. **Process isolation** -- a crashing process has no impact on other processes beyond signals (messages, links, monitors) defined by the programmer.
7. **Well-defined behavior** -- the behavior of all Erlang programs is defined for all possible inputs; partial operations throw exceptions that leave the program in a well-defined state.
8. **Arbitrary precision arithmetic** -- integer overflow only occurs at several megabits in size and throws an exception rather than wrapping (CWE-190).

# Construction / Recognition

## To Apply:
1. Secure the host system so attackers cannot modify files relevant to the program (code, configuration, shared libraries).
2. Treat everything "not fully and completely trusted" as untrusted -- make no distinction between partially trusted and untrusted.
3. Put safeguards in place for resource usage (e.g., heap size limitations) since excessive consumption is not prevented by default.
4. Configure TLS with client certificate verification for distribution over untrusted networks.
5. Only use documented functionality.

## To Recognize:
1. A system that loads only trusted code modules.
2. An Erlang cluster where all nodes are under the same administrative domain.
3. Input validation boundaries drawn at the edges where untrusted data enters the system.

# Context & Application

Understanding the Erlang threat model is essential before writing any security-sensitive Erlang code. It defines the trust boundary: inside the BEAM, code has unrestricted access; security must therefore be enforced at the boundary where data and code enter the system. This model is fundamentally different from sandboxed environments (like browser JavaScript or Java applets) where untrusted code runs with restricted capabilities. In Erlang, the security strategy is to ensure only trusted code is loaded and to validate all data from untrusted sources at the system boundary.

# Examples

**Example 1** (secure_coding.md, "What is not protected against"): A malicious BEAM module can break the memory safety protections of the runtime system and crash the virtual machine. "This is no different from other languages, where for example modifying a Rust executable on disk could also break memory safety."

**Example 2** (secure_coding.md, "What is protected against"): "Erlang processes are isolated and can only affect other entities through the use of signals: messages, links, monitors, and so on. A process that crashes will do so without any impact on other processes other than that defined by the programmer."

# Relationships

## Builds Upon
- No prerequisites -- this is a foundational security concept.

## Enables
- **Erlang Memory Safety** -- the threat model defines the scope of memory safety guarantees
- **Secure Error Handling** -- the threat model justifies the let-it-crash approach to security
- **Distribution Security** -- understanding what distribution does not protect against motivates securing it

## Related
- **supervision-tree** -- the supervision tree is the mechanism through which crash recovery is structured
- **Native Code Safety** -- NIFs and drivers are one of the ways the threat model's guarantees can be violated

## Contrasts With
- No direct contrasts in source.

# Common Errors

- **Error**: Assuming Erlang provides sandboxing for untrusted code, similar to a browser's JavaScript sandbox.
  **Correction**: All loaded BEAM code is fully trusted and has unrestricted access. There is no built-in sandboxing.

- **Error**: Treating partially trusted data or code as safe.
  **Correction**: "Anything that is not fully and completely trusted must be considered as untrusted as something given to you by a malicious actor."

# Common Confusions

- **Confusion**: Believing that Erlang's process isolation provides security against malicious code within the same node.
  **Clarification**: Process isolation protects against accidental interference and bugs, not against malicious code. A loaded module has full access to the runtime system.

- **Confusion**: Thinking the Erlang distribution cookie provides authentication security.
  **Clarification**: The cookie mechanism only prevents unintentional mixing of clusters on the same network; it is not an authentication mechanism for untrusted networks.

# Source Reference

OTP Design Principles, Secure Coding Guidelines, "Background" section -- specifically "What is not protected against" and "What is protected against" subsections (secure_coding.md, lines 44-141).

# Verification Notes

- Definition source: Directly synthesized from the "Background" section of secure_coding.md.
- Confidence rationale: High -- the source explicitly enumerates what is and is not protected, with CWE references.
- Uncertainties: None.
- Cross-reference status: References CWE-416, CWE-465, CWE-1218, CWE-362, CWE-835, CWE-190.
