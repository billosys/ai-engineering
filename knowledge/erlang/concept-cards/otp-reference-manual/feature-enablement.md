---
# === CORE IDENTIFICATION ===
concept: Feature Enablement
slug: feature-enablement

# === CLASSIFICATION ===
category: core-idioms
subcategory: language-evolution
tier: intermediate

# === PROVENANCE ===
source: "Erlang Reference Manual"
source_slug: otp-reference-manual
authors: "Ericsson AB"
chapter: "Features"
chapter_number: null
pdf_page: null
section: "Enabling and Disabling Features"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "feature directive"
  - "feature configuration"
  - "enabling features"
  - "disabling features"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - erlang-feature-concept
  - feature-lifecycle
extends: []
related:
  - maybe-expression-feature
  - feature-preprocessor-macros
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do I enable an experimental feature in Erlang?"
  - "What is the -feature directive?"
  - "What are the different ways to enable or disable features?"
  - "Do I need to enable features in the runtime to load modules using them?"
---

# Quick Definition
Features can be enabled or disabled through three mechanisms: `erlc` command-line options, compiler options, and the `-feature` module directive. The `-feature` directive within a module is the preferred method.

# Core Definition
The Erlang Reference Manual describes three ways to enable/disable features (Features, "Enabling and Disabling Features"): (1) "Options to `erlc`" using `-enable-feature` and `-disable-feature`; (2) "Compiler options" using `{feature, <feature>, enable|disable}` as a `+<term>` option to `erlc` or in arguments to `compile` module functions; (3) "The feature directive" using `-feature(<feature>, enable|disable)` inside a module prefix, which "is the preferred method of enabling and disabling features." Since OTP 26, it is no longer necessary to enable features in the runtime to load modules that use them (this was required in OTP 25), though using features directly in the shell still requires runtime enablement.

# Prerequisites
- **erlang-feature-concept** -- Must understand what features are
- **feature-lifecycle** -- Must understand which features can be configured

# Key Properties
1. Three methods: `erlc` options, compiler options, `-feature` directive
2. The `-feature` directive is the preferred method
3. Directive syntax: `-feature(<feature>, enable|disable).`
4. The directive must be in the module prefix (before functions)
5. Since OTP 26, runtime enablement is not needed to load feature-using modules
6. Shell usage still requires runtime enablement via `-enable-feature` to `erl`
7. Only configurable features (experimental and approved) can be enabled/disabled

# Construction / Recognition
## Using the -feature Directive (Preferred):
```erlang
-feature(maybe_expr, enable).
```

## Using erlc Options:
```
erlc -enable-feature maybe_expr my_module.erl
erlc -disable-feature maybe_expr my_module.erl
```

## Using Compiler Options:
```erlang
compile:file("my_module.erl", [{feature, maybe_expr, enable}]).
```
Or with `erlc`:
```
erlc +'{feature, maybe_expr, enable}' my_module.erl
```

# Context & Application
Feature enablement is the mechanism that allows gradual adoption. A team can enable an experimental feature in specific modules using the `-feature` directive while leaving the rest of the codebase unchanged. This is particularly useful during OTP upgrades, where approved features that change existing behavior can be disabled until the codebase is ready. The `-feature` directive is preferred because it makes the feature requirement explicit in the source file itself, rather than depending on build system configuration.

# Examples
**Example 1** (Enabling and Disabling Features -- directive):
```erlang
-module(my_module).
-feature(maybe_expr, enable).

%% Now the maybe expression is available in this module
```

**Example 2** (Enabling and Disabling Features -- erlc):
```
erlc -enable-feature maybe_expr my_module.erl
```

**Example 3** (Preprocessor Additions -- conditional compilation):
```erlang
-ifdef(FEATURE_AVAILABLE(maybe_expr)).
  %% Code using maybe expression
-else.
  %% Fallback code
-endif.
```

# Relationships
## Builds Upon
- **erlang-feature-concept** -- Enablement is how features are activated
- **feature-lifecycle** -- Only configurable features can be enabled/disabled

## Enables
- **maybe-expression-feature** -- Enabling `maybe_expr` makes the maybe expression available

## Related
- **feature-preprocessor-macros** -- Macros for conditional compilation based on feature state

## Contrasts With
None.

# Common Errors
- **Error**: Trying to enable a rejected or permanent feature
  **Correction**: Rejected features cannot be enabled (they are not available). Permanent features are always enabled and cannot be configured.

- **Error**: Placing the `-feature` directive after function declarations
  **Correction**: The directive must be in the module prefix, before the first function declaration.

# Common Confusions
- **Confusion**: Thinking the runtime must be configured to load feature-using modules (post OTP 25)
  **Clarification**: Since OTP 26, runtime enablement is not needed to load modules. However, using features directly in the shell still requires the `-enable-feature` option to `erl`.

- **Confusion**: Thinking `erlc` options and the `-feature` directive have different effects
  **Clarification**: All three methods achieve the same result. The `-feature` directive is preferred because it is self-documenting in the source code.

# Source Reference
"Features" chapter, "Enabling and Disabling Features" and "Preprocessor Additions" sections.

# Verification Notes
- Definition source: Direct from source text
- Confidence rationale: High -- explicit methods and syntax described
- Uncertainties: None
- Cross-reference status: All slugs verified
