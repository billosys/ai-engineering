---
# === CORE IDENTIFICATION ===
concept: Dialyzer Nominal Checking
slug: dialyzer-nominal-checking

# === CLASSIFICATION ===
category: data-types
subcategory: static-analysis
tier: advanced

# === PROVENANCE ===
source: "Erlang Reference Manual"
source_slug: otp-reference-manual
authors: "Ericsson AB"
chapter: "Nominals"
chapter_number: null
pdf_page: null
section: "Nominal Type-Checking Rules"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "nominal type-checking in Dialyzer"
  - "Dialyzer nominal analysis"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - nominal-type
  - nominal-type-compatibility
  - function-specification
extends: []
related:
  - nominal-type-derivation
  - opaque-type
  - dialyzer-opacity-enforcement
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How does Dialyzer enforce nominal type rules?"
  - "What warnings does Dialyzer produce for nominal type violations?"
  - "Why is nominal type-checking not done by the compiler?"
---

# Quick Definition
Dialyzer is the tool that enforces nominal type-checking in Erlang. The Erlang compiler does not perform nominal type-checking; it is Dialyzer that raises warnings when incompatible nominal types are mixed.

# Core Definition
The Erlang Reference Manual states: "Within OTP, nominal type-checking is done in Dialyzer. The Erlang compiler does not perform nominal type-checking." (Nominals, "Rationale and Syntax"). Dialyzer's nominal type-checking "aligns with the examples' expected results" in the Nominals chapter. When a function spec declares a nominal return type but the implementation returns an incompatible nominal type, Dialyzer produces an "Invalid type specification" warning indicating that "The return types do not overlap."

# Prerequisites
- **nominal-type** -- Must understand nominal type declarations
- **nominal-type-compatibility** -- Must understand the compatibility rules Dialyzer enforces
- **function-specification** -- Dialyzer checks specs against implementations

# Key Properties
1. The Erlang compiler does not perform nominal type-checking
2. Dialyzer raises warnings for incompatible nominal type usage
3. Warning format: "Invalid type specification" with success typing information
4. Dialyzer respects derivation chains when checking nominal compatibility
5. Nominal types make Dialyzer's analysis faster compared to opaque types (when information hiding is not needed)

# Construction / Recognition
## Triggering Nominal Checking:
1. Declare nominal types using `-nominal`
2. Write function specs using those nominal types
3. Run Dialyzer on the codebase
4. Dialyzer will report warnings when incompatible nominals are mixed

## Warning Format:
```
Invalid type specification for function foo/0.
The success typing is foo() -> (meter() :: integer())
But the spec is foo() -> foot()
The return types do not overlap
```

# Context & Application
Dialyzer nominal checking is the enforcement mechanism that makes nominal types useful in practice. Without Dialyzer, nominal types would be indistinguishable from structural types at compile time. Running Dialyzer as part of CI/CD ensures that nominal type violations are caught before deployment. The source also notes that if an opaque type does not require information hiding, redefining it as a nominal type "makes Dialyzer's analysis faster."

# Examples
**Example 1** (Nominal Type-Checking Rules):
```erlang
-nominal meter() :: integer().
-nominal foot() :: integer().

-spec int_to_meter(integer()) -> meter().
int_to_meter(X) -> X.

-spec foo() -> foot().
foo() -> int_to_meter(24).
```
Dialyzer warning:
```
Invalid type specification for function foo/0.
The success typing is foo() -> (meter() :: integer())
But the spec is foo() -> foot()
The return types do not overlap
```

**Example 2** (Nominal Type-Checking Rules -- no warning):
```erlang
-spec qaz() -> integer().
qaz() -> int_to_meter(24).
```
No Dialyzer warning because `integer()` is a structural type compatible with `meter()`.

# Relationships
## Builds Upon
- **nominal-type** -- Dialyzer enforces the rules for this type system
- **nominal-type-compatibility** -- Dialyzer implements these compatibility rules
- **function-specification** -- Dialyzer checks specs against actual code behavior

## Enables
Practical use of nominal types by providing static analysis enforcement.

## Related
- **nominal-type-derivation** -- Dialyzer follows derivation chains
- **dialyzer-opacity-enforcement** -- Dialyzer also enforces opaque type rules

## Contrasts With
None.

# Common Errors
- **Error**: Expecting the compiler to reject code with nominal type mismatches
  **Correction**: Only Dialyzer checks nominal types. Code with nominal type violations will compile successfully but Dialyzer will report warnings.

# Common Confusions
- **Confusion**: Thinking Dialyzer warnings are compilation errors
  **Clarification**: Dialyzer warnings do not prevent compilation or execution. They are advisory static analysis results. Code with nominal type violations will still run.

# Source Reference
"Nominals" chapter, "Rationale and Syntax" and "Nominal Type-Checking Rules" sections.

# Verification Notes
- Definition source: Direct from source text including the exact warning format
- Confidence rationale: High -- explicit statement about Dialyzer's role and example warning
- Uncertainties: None
- Cross-reference status: All slugs verified
