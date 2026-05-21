---
# === CORE IDENTIFICATION ===
concept: Secure Error Handling
slug: secure-error-handling

# === CLASSIFICATION ===
category: error-handling
subcategory: security
tier: intermediate

# === PROVENANCE ===
source: "OTP Design Principles"
source_slug: otp-design-principles
authors: "Ericsson AB"
chapter: "Secure Coding Guidelines"
chapter_number: null
pdf_page: null
section: "Error Handling"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "let-it-crash security"
  - "deny-by-default execution"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - supervision-tree
  - erlang-threat-model
extends: []
related:
  - be-restrictive-rule
  - behaviour
  - gen-server
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How does the let-it-crash philosophy improve security?"
  - "Why should unexpected conditions be treated as errors?"
  - "What are the three categories of errors in Erlang's security model?"
  - "How does process isolation make crash-based error handling safe?"
  - "What does 'deny by default' mean for program execution?"
---

# Quick Definition

Erlang's error handling philosophy -- abandoning execution on unexpected conditions and delegating recovery to supervision trees -- is a security mechanism. By restricting program behavior to only that which is expected, it greatly reduces the surface area for bugs and security issues, functioning as a "deny by default" execution model.

# Core Definition

The Secure Coding Guidelines define three error categories: (1) errors not expected to be handled gracefully (e.g., local disk suddenly unavailable), (2) errors expected to be handled gracefully (e.g., web server 404), and (3) program bugs (e.g., writing to a closed file). The document states: "a cornerstone of idiomatic error handling in Erlang is to abandon execution once something unexpected occurs, leaving the consequences to the program's supervision structure instead of ignoring or trying to handle the condition and continuing execution." This is described as making "program execution 'deny by default' and that it may only continue as explicitly defined."

# Prerequisites

- **Supervision Tree** -- a well-designed supervision structure is a prerequisite for crash-based error handling to be effective.
- **Erlang Threat Model** -- understanding process isolation is necessary to understand why crashing is safe.

# Key Properties

1. **Three error categories** -- (1) unexpected unrecoverable errors, (2) expected recoverable errors, (3) program bugs. Classical error handling mixes all three, causing issues.
2. **Crash on the unexpected** -- encountering something unexpected means leaving the "known and tested" path; continuing greatly increases risk of bugs and security issues.
3. **Supervision-based recovery** -- the supervision tree provides generalized recovery from program bugs without the programmer defining each case.
4. **Limited blast radius** -- whatever the crashing process worked on is lost, but the program as a whole is spared due to process isolation.
5. **Deny by default** -- program execution may only continue as explicitly defined; anything else causes a crash.
6. **Security implication** -- "Security issues are almost by definition a result of unexpected program behavior, and restricting program behavior to only that which is expected greatly reduces the surface area for bugs and security issues."
7. **Expected errors should still be handled** -- components that can meaningfully handle all consequences of an error locally should do so; those that cannot should delegate to supervision.
8. **Well-designed supervision required** -- must adequately model the problem domain so local failures are contained locally (e.g., a single failed request should not tear down the entire program).

# Construction / Recognition

## To Apply:
1. Design the supervision tree to reflect the problem domain (see DSG-001), ensuring isolated concerns are separate processes.
2. For expected errors (category 2), handle them locally where meaningful -- e.g., respond with an error message rather than crashing (to avoid spamming error logs).
3. For unexpected errors (categories 1 and 3), let the process crash and allow the supervision structure to handle recovery.
4. Write restrictive pattern matches so that unexpected values cause immediate crashes rather than silent continuation (see STL-001).
5. Use the `{ok, Result} | {error, Reason}` convention (see DSG-002) to let callers decide whether an error is exceptional.

## To Recognize:
1. Code that pattern-matches on specific expected values rather than using catch-all clauses.
2. Supervision trees that model the problem domain's isolation boundaries.
3. Absence of defensive try/catch blocks around operations whose failure should propagate.

# Context & Application

This concept is central to writing secure Erlang code. The source ties it directly to OWASP A10:2025 (Mishandling of Exceptional Conditions), stating: "program execution should be restricted to that which is expected, and unexpected situations should be left to the supervision structure." The document emphasizes that "blindly continuing execution may not only result in unexpected behavior, but can also become a security issue as assumptions that are made may no longer be valid." This is also referenced by multiple coding rules including STL-001 (Be Restrictive) and DSG-001 (Encode the Problem Domain in the Supervision Tree).

# Examples

**Example 1** (secure_coding.md, "Error Handling"): The third error category -- program bugs -- "is especially sinister because of the difficulty in ensuring that the offending code has not left parts of the program in an invalid state, but it is nevertheless necessary for a language to be able to handle it since a broken invariant in an insignificant part of the program would otherwise tear the entire program down."

**Example 2** (secure_coding.md, "Error Handling"): "If a program encounters an error of the first or second categories, it can either handle them explicitly, or leave it to the supervision structure by either pattern-matching on the return value or leaving exceptions uncaught."

**Example 3** (secure_coding.md, DSG-002): The `{ok, Result} | {error, Reason}` convention:
```erlang
%% PREFER
case some_function(A, B) of
    {ok, C} ->
        %% Happy path
        ...;
    {error, Error} ->
        %% Handle it
end
```

# Relationships

## Builds Upon
- **supervision-tree** -- supervision trees are the mechanism that makes crash-based error handling safe and practical
- **Erlang Threat Model** -- process isolation is what limits the blast radius of a crash

## Enables
- **Be Restrictive Rule** -- the security rationale for restrictive pattern matching stems from this error handling philosophy

## Related
- **gen-server** -- gen_server and other behaviours provide the framework for structured error handling within supervision trees
- **behaviour** -- OTP behaviours implement the patterns needed for supervised crash recovery

## Contrasts With
- No direct contrasts in source, though the document implicitly contrasts with defensive programming styles that attempt to handle all errors locally.

# Common Errors

- **Error**: Catching all exceptions broadly to prevent crashes, using overly general `catch` clauses.
  **Correction**: Only catch specific, expected exceptions. Let unexpected errors propagate to the supervision structure. "Blindly continuing execution may not only result in unexpected behavior, but can also become a security issue."

- **Error**: Designing a flat supervision tree where a single failed request tears down the entire application.
  **Correction**: The supervision structure must reflect the problem domain. Isolated flows should be separate processes so that "a single failed request should not tear down the entire program, but only the subtree started through said request."

# Common Confusions

- **Confusion**: Thinking "let it crash" means errors should never be handled.
  **Clarification**: Expected errors (category 2) should be handled locally where the component can meaningfully deal with all consequences. Only unexpected errors should be left to supervision. "Care should also be taken to handle the errors that are expected and can be handled locally to avoid spamming the error logs."

- **Confusion**: Believing that crashing a process is inherently risky or dangerous.
  **Clarification**: Because processes are isolated and supervision trees handle recovery, crashing is the safest response to unexpected conditions -- it prevents the program from continuing in a potentially invalid state.

# Source Reference

OTP Design Principles, Secure Coding Guidelines, "Error Handling" section (secure_coding.md, lines 142-202). Also referenced by DSG-001, DSG-002, STL-001, and the OWASP A10:2025 commentary.

# Verification Notes

- Definition source: Directly quoted from the "Error Handling" section of secure_coding.md.
- Confidence rationale: High -- this section is extensively developed with clear security rationale and multiple cross-references throughout the document.
- Uncertainties: None.
- Cross-reference status: References supervision-tree, behaviour, gen-server. Linked to by STL-001 (be-restrictive-rule), DSG-001, DSG-002, and OWASP A10:2025.
