---
# === CORE IDENTIFICATION ===
concept: Dialyzer Opacity Enforcement
slug: dialyzer-opacity-enforcement

# === CLASSIFICATION ===
category: api-design
subcategory: static-analysis
tier: intermediate

# === PROVENANCE ===
source: "Erlang Reference Manual"
source_slug: otp-reference-manual
authors: "Ericsson AB"
chapter: "Opaques"
chapter_number: null
pdf_page: null
section: "Opaque Type Aliases"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "Dialyzer opaque checking"
  - "opacity enforcement"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - opaque-type
  - opacity-contract
extends: []
related:
  - dialyzer-nominal-checking
  - opaque-api-design-patterns
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How does Dialyzer enforce opacity rules?"
  - "What are the limitations of Dialyzer's opacity enforcement?"
  - "What is the opaque_union Dialyzer option?"
---

# Quick Definition
Dialyzer provides partial enforcement of opacity contracts by checking for opacity violations outside the defining module. Since OTP 28, Dialyzer checks opaques nominally within the defining module and adds the `opaque_union` option to warn on unions of opaque and non-opaque types.

# Core Definition
The Erlang Reference Manual states: "Dialyzer provides some opacity-checking, but the rest is up to convention." (Opaques, "Opaque Type Aliases"). Since Erlang/OTP 28, "Dialyzer checks opaques in their defining module in the same way as nominals. Outside of the defining module, Dialyzer checks opaques for opacity violations." Additionally, "a Dialyzer option `opaque_union` has been added, so that Dialyzer can raise a warning whenever a union of opaque and non-opaque types is produced outside the opaque's defining module." However, "opacity in Erlang is skin-deep" and "Dialyzer must make some approximations."

# Prerequisites
- **opaque-type** -- Must understand opaque type declarations
- **opacity-contract** -- Must understand what constitutes a violation

# Key Properties
1. Dialyzer checks for opacity violations outside the defining module
2. Since OTP 28, Dialyzer checks opaques nominally inside the defining module
3. The `opaque_union` option (OTP 28+) warns on unions of opaque and non-opaque types outside the defining module
4. Enforcement is not total -- Dialyzer must make approximations
5. The runtime does not enforce opacity at all
6. A determined consumer can circumvent opacity through printing, serializing, or using `term/0`-level functions

# Construction / Recognition
## How Enforcement Works:
1. In the defining module: Dialyzer treats the opaque like a nominal type (OTP 28+)
2. Outside the defining module: Dialyzer checks for opacity violations
3. Enable `opaque_union` to get warnings about opaque/non-opaque unions

## What Dialyzer Cannot Catch:
1. Runtime type inspection via printing or serialization
2. Using the value as `term()` and then inspecting with `is_map/1`, `maps:get/2`, etc.
3. Approximations in Dialyzer's analysis may miss some violations

# Context & Application
Dialyzer is the primary tool for enforcing opacity in Erlang, but developers must understand its limitations. The enforcement is a best-effort static analysis, not a guarantee. Running Dialyzer regularly as part of CI/CD catches most violations, but determined or accidental circumvention is possible at runtime. The `opaque_union` option in OTP 28 addresses a common source of opacity leaks.

# Examples
**Example 1** (Opaque Type Aliases -- runtime circumvention):
```erlang
%% This violates opacity but Dialyzer may not catch all cases
Set = sets:new(),
case is_map(Set) of
    true -> io:format("It's a map!~n");
    false -> io:format("Not a map~n")
end.
```
Since `is_map/1` reveals the underlying type, this violates the opacity contract. Dialyzer should warn about this, but the runtime will execute it.

**Example 2** (OTP 28 opaque_union option):
The `opaque_union` Dialyzer option raises warnings when code outside the defining module produces a union of opaque and non-opaque types, which can leak type information.

# Relationships
## Builds Upon
- **opaque-type** -- Dialyzer enforces the opacity rules for these types
- **opacity-contract** -- Dialyzer checks adherence to the contract

## Enables
Practical enforcement of opacity conventions in Erlang codebases.

## Related
- **dialyzer-nominal-checking** -- Since OTP 28, opaques are checked nominally within their defining module
- **opaque-api-design-patterns** -- Dialyzer validates that APIs using opaques are correct

## Contrasts With
None.

# Common Errors
- **Error**: Relying solely on Dialyzer for opacity enforcement
  **Correction**: Dialyzer's enforcement is not total. Also follow conventions, code reviews, and avoid type-revealing operations on opaques.

# Common Confusions
- **Confusion**: Thinking Dialyzer catches all opacity violations
  **Clarification**: Dialyzer "must make some approximations." A determined consumer can still circumvent opacity through printing, serialization, or using functions like `maps:get/2` on a value treated as `term()`.

- **Confusion**: Confusing Dialyzer's opacity checking with its nominal checking
  **Clarification**: Since OTP 28, inside the defining module, Dialyzer checks opaques the same way as nominals (name-based). Outside the defining module, Dialyzer checks for opacity violations (structure inspection).

# Source Reference
"Opaques" chapter, "Opaque Type Aliases" section.

# Verification Notes
- Definition source: Direct from source text with OTP 28 changes noted
- Confidence rationale: High -- explicit discussion of Dialyzer's role and limitations
- Uncertainties: Exact details of Dialyzer's approximations are not specified in the source
- Cross-reference status: All slugs verified
