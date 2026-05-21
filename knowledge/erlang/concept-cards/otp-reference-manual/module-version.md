---
# === CORE IDENTIFICATION ===
concept: Module Version
slug: module-version

# === CLASSIFICATION ===
category: core-idioms
subcategory: module-structure
tier: intermediate

# === PROVENANCE ===
source: "Erlang Reference Manual"
source_slug: otp-reference-manual
authors: "Ericsson AB"
chapter: "Modules"
chapter_number: null
pdf_page: null
section: "Pre-Defined Module Attributes"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "-vsn"
  - "vsn attribute"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - erlang-module
extends: []
related:
  - module-declaration
  - module-info
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do I set a version for an Erlang module?"
  - "What is the -vsn attribute?"
  - "What happens if I don't set a module version?"
---

# Quick Definition
The `-vsn(Vsn)` attribute assigns a version identifier to a module. If omitted, the version defaults to the MD5 checksum of the module.

# Core Definition
The Erlang Reference Manual states: "`-vsn(Vsn).` -- Module version. `Vsn` is any literal term and can be retrieved using `beam_lib:version/1`. If this attribute is not specified, the version defaults to the MD5 checksum of the module." (Modules, "Pre-Defined Module Attributes" section).

# Prerequisites
- **erlang-module** -- The vsn attribute is a module attribute

# Key Properties
1. Syntax: `-vsn(Vsn).` where `Vsn` is any literal term
2. Can be any literal term: an integer, string, tuple, list, etc.
3. Retrieved at runtime using `beam_lib:version/1`
4. Defaults to the MD5 checksum of the module if not specified
5. Also accessible via `Module:module_info(attributes)` where it appears in the attributes list

# Construction / Recognition
## To Construct/Create:
1. Add `-vsn("1.0.0").` or `-vsn(1).` or `-vsn({1, 0, 0}).` to the module attributes

## To Identify/Recognize:
1. The `-vsn(...)` attribute in a module's source code
2. Retrieved via `beam_lib:version/1` or `Module:module_info(attributes)`

# Context & Application
The module version attribute is useful for tracking which version of a module is loaded in a running system, especially during hot code upgrades. The OTP release handler uses module versions to manage code upgrades and downgrades. In `appup` files, version information helps determine which upgrade instructions to apply.

# Examples
**Example 1** (setting a version):
```erlang
-module(my_module).
-vsn("2.1.0").
```

**Example 2** (retrieving the version):
```erlang
1> beam_lib:version("my_module.beam").
{ok, {my_module, "2.1.0"}}
```

# Relationships
## Builds Upon
- **erlang-module** -- Version is a module attribute

## Enables
None directly, but supports release management and hot code upgrades.

## Related
- **module-info** -- Version is accessible through `module_info(attributes)`
- **module-declaration** -- Another pre-defined module attribute

## Contrasts With
None.

# Common Errors
- **Error**: Expecting the version to auto-increment
  **Correction**: The version is a static literal; you must update it manually

# Common Confusions
- **Confusion**: Thinking the MD5-based default version changes between compilations of identical source
  **Clarification**: The MD5 checksum is computed from the module's abstract code, so identical source code produces the same default version

# Source Reference
"Modules" chapter, "Pre-Defined Module Attributes" section.

# Verification Notes
- Definition source: Direct quote from source
- Confidence rationale: High -- explicit definition with default behavior specified
- Uncertainties: None
- Cross-reference status: All slugs correspond to planned or existing cards
