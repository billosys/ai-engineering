---
concept: Compiler Binary Optimization
slug: compiler-binary-optimization
category: compiler-optimization
subcategory: binary-optimization
tier: advanced
source: "Erlang Efficiency Guide"
source_slug: otp-efficiency-guide
authors: "Ericsson/OTP Team"
chapter: "Constructing and Matching Binaries"
chapter_number: null
pdf_page: null
section: "Compiler Support For Constructing Binaries"
extraction_confidence: high
aliases:
  - "compiler support for binary construction"
  - "compiler binary append hints"
prerequisites:
  - binary-append-optimization
  - refc-binary
extends:
  - binary-append-optimization
related:
  - forced-copying
  - bin-opt-info
  - binary-construction-efficiency
contrasts_with: []
answers_questions:
  - "How does the compiler optimize binary construction?"
---

# Quick Definition

The Erlang compiler (since OTP 26) can generate more efficient code for binary append operations when it determines that no branching, failure handling, or heap binary promotion is needed. In such cases, the compiler rewrites the initial empty binary creation to directly allocate a refc binary with pre-reserved space.

# Core Definition

The basic binary append optimization requires the runtime to handle several edge cases: appending to a heap binary (requiring promotion to refc), appending to an older version of the binary (requiring a copy to preserve referential transparency), and handling append failures. This handling is not free -- for example, the runtime must create a sub binary for every append operation to track which binary version supports cheap appends.

When the compiler can determine that none of those situations need to be handled and that the append operation cannot possibly fail, it generates code that causes the runtime system to apply a more efficient variant of the optimization. Specifically, the compiler rewrites the creation of the empty binary to instead create a refc binary with 256 bytes already reserved, so the append operation never needs to handle a binary not prepared for appending (Ericsson/OTP Team, "Constructing and Matching Binaries," section "Compiler Support For Constructing Binaries").

# Prerequisites

- **binary-append-optimization** -- The compiler optimization enhances the basic runtime append optimization; understanding the base mechanism is essential
- **refc-binary** -- The compiler optimization pre-creates refc binaries; understanding their structure is needed

# Key Properties

1. Added in Erlang/OTP 26
2. Applies when the compiler can prove no branching over binary versions occurs
3. Applies when the compiler can prove the append cannot fail
4. Eliminates the need to create a sub binary on every append (which the basic optimization requires)
5. Rewrites `<<>>` creation to pre-allocate a refc binary with 256 bytes reserved
6. The append operation never encounters an unprepared (heap) binary
7. Only applies to single-version, linear binary construction patterns

# Construction / Recognition

## When the Compiler Optimization Applies

1. The function maintains only a single version of the binary (no branching)
2. The binary is not shared or stored in multiple variables that are later used for appending
3. The append operation cannot fail (e.g., size calculations are guaranteed to succeed)
4. The pattern is a straightforward accumulation loop

## When the Compiler Optimization Does NOT Apply

1. When the binary is used in multiple append branches (like line 5 in the basic optimization example)
2. When the binary might be a heap binary at the point of append
3. When the append might fail (e.g., variable-length fields with unchecked sizes)

# Context & Application

This is a "second-level" optimization on top of the basic runtime append optimization. Most well-written binary construction code benefits from it automatically. The compiler does the analysis transparently, and no special coding is required beyond following the standard efficient binary construction patterns.

**Typical contexts:**
- Binary repacking functions (converting between binary formats)
- Accumulator-based binary construction in tail-recursive loops
- Any linear, single-version binary accumulation

**Historical note:** This compiler support was added in Erlang/OTP 26. Before that release, only the basic runtime optimization was available.

# Examples

**Compiler-optimized binary repacking** (source: "Compiler Support For Constructing Binaries" section):

```erlang
-module(repack).
-export([repack/1]).

repack(Bin) when is_binary(Bin) ->
    repack(Bin, <<>>).

repack(<<C:8,T/binary>>, Result) ->
    repack(T, <<Result/binary,C:16>>);
repack(<<>>, Result) ->
    Result.
```

The `repack/2` function only keeps a single version of the binary (`Result`), so there is never any need to copy the binary. The compiler rewrites the `<<>>` in `repack/1` to instead create a refc binary with 256 bytes already reserved. The append in `repack/2` never needs to handle a binary not prepared for appending, and no sub binary is created for tracking purposes.

# Relationships

## Builds Upon

- **binary-append-optimization** -- This is an enhanced form of the basic runtime append optimization

## Related

- **forced-copying** -- The compiler optimization avoids the conditions that force copying
- **bin-opt-info** -- Can reveal whether the compiler optimization is being applied
- **binary-construction-efficiency** -- The high-level pattern that this optimization makes efficient at the implementation level

# Common Errors

- **Error**: Assuming all binary append code benefits from the compiler optimization
  **Correction**: The compiler optimization only applies when the compiler can prove single-version, non-failing appends. Code with branching binary versions falls back to the basic runtime optimization.

# Common Confusions

- **Confusion**: Thinking the compiler optimization replaces the runtime optimization
  **Clarification**: The compiler optimization is an enhancement of the runtime optimization, not a replacement. The runtime still does the actual appending; the compiler just ensures the binary is always pre-prepared for appending.

- **Confusion**: Believing you need to write code differently to benefit from the compiler optimization
  **Clarification**: Standard efficient binary construction patterns (accumulator as first segment, single version) automatically benefit. The compiler does the analysis transparently.

# Source Reference

"Constructing and Matching Binaries," section "Compiler Support For Constructing Binaries." The source provides the `repack/1` example and explains how the compiler rewrites empty binary creation to pre-allocate a refc binary with 256 bytes reserved. Notes that this support was added in Erlang/OTP 26.

# Verification Notes

- Definition: Directly from source -- "the compiler generates code that causes the runtime system to apply a more efficient variant of the optimization"
- OTP 26 introduction: Explicitly stated in a Change info box
- Sub binary elimination: Explicitly stated -- "the runtime system must create a sub binary" for basic optimization; the compiler variant avoids this
- Rewrite behavior: Explicitly stated -- "The compiler rewrites the creation of the empty binary in repack/1 to instead create a refc binary with 256 bytes already reserved"
- Single-version requirement: Derived from "The repack/2 function only keeps a single version of the binary"
- Confidence: HIGH -- explicit section with worked example in official OTP documentation
