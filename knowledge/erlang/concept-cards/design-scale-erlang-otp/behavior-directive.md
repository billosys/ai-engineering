---
# === CORE IDENTIFICATION ===
concept: Behavior Directive
slug: behavior-directive

# === CLASSIFICATION ===
category: otp-behaviours
subcategory: gen-server
tier: intermediate

# === PROVENANCE ===
source: "Designing for Scalability with Erlang/OTP"
source_slug: design-scale-erlang-otp
authors: "Francesco Cesarini & Steve Vinoski"
chapter: "Generic Servers"
chapter_number: 3
pdf_page: 96
section: "Behavior Directives"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "-behavior"
  - "-behaviour"
  - behaviour directive
  - "-vsn"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - gen-server
extends: []
related:
  - callback-module
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What does the -behavior directive do?"
  - "Why declare a behavior in a callback module?"
---

# Quick Definition

The `-behavior` directive declares that a module implements an OTP behavior. The compiler uses it to warn about missing, unexported, or wrong-arity callback functions.

# Core Definition

"When we are implementing an OTP behavior, we need to include behavior directives in our module declarations" (Cesarini & Vinoski, p. 77). "The behavior directive is used by the compiler to issue warnings about callback functions that are not defined, not exported, or defined with the wrong arity. The dialyzer tool also uses these declarations for checking type discrepancies" (p. 77). It also documents intent: a maintainer "will see these directives and immediately know you have been using the generic server patterns." Both spellings are accepted: "both the American 'behavior' and British 'behaviour' spellings are honored" (p. 77). An optional companion directive, `-vsn(Version)`, tracks module versions during code upgrade and downgrade.

# Prerequisites

- **Gen_server** — The behavior directive declares which behavior (e.g., `gen_server`) a callback module implements.

# Key Properties

1. Declared as `-behavior(BehaviorName).` in the callback module.
2. The compiler warns about callbacks that are missing, unexported, or of wrong arity.
3. `dialyzer` uses the declaration to check type discrepancies.
4. It documents to maintainers which OTP pattern the module follows.
5. Both `-behavior` and `-behaviour` spellings are accepted.
6. The optional `-vsn(Version)` directive tracks versions across upgrades.

# Construction / Recognition

## To Construct:
1. Add `-behavior(gen_server).` (or `-behaviour(...)`) near the top of the callback module.
2. Optionally add `-vsn(Version).` to track the module version.

## To Recognize:
1. Look for a `-behavior`/`-behaviour` attribute in a module's declarations.

# Context & Application

- **Typical contexts**: The header of every OTP callback module.
- **Common applications**: `-behavior(gen_server).` in the frequency callback module.
- **Historical/stylistic notes**: Historically, omitting the British spelling could cause an "unknown behavior" warning; both spellings are now honored.

# Examples

**Example 1** (p. 77): The directive in a callback module:

```erlang
-module(frequency).
-behavior(gen_server).
-export([start_link/1, init/1, ...]).
```

**Example 2** (p. 77): Both spellings are valid:

```erlang
-behavior(tcp_wrapper).
-behaviour(tcp_wrapper).
```

# Relationships

## Builds Upon
- **Gen_server** — The directive names the behavior the module implements.

## Enables
- *(none specific in scope)*

## Related
- **Callback module** — The directive belongs in the callback module and declares its contract.

## Contrasts With
- *(none)*

# Common Errors

- **Error**: Omitting a required callback (e.g., `code_change/3`) and ignoring the resulting compiler warning.
  **Correction**: Implement the callbacks the behavior expects, or knowingly accept the warning for callbacks covered later.

# Common Confusions

- **Confusion**: Believing the British spelling `-behaviour` is required.
  **Clarification**: Both `-behavior` and `-behaviour` are honored by the compiler.

# Source Reference

Chapter 3: Generic Servers, Section "Behavior Directives," pages 77-78. See the "Behavior Versus Behaviour" sidebar.

# Verification Notes

- Definition source: Direct quotes from p. 77.
- Confidence rationale: HIGH — explicit treatment with a dedicated sidebar.
- Uncertainties: None.
- Cross-reference status: Verified against planned cards.
- Re-extraction notes: Fresh extraction — no pre-existing card for this source.
</content>
</invoke>
