---
concept: NIF Efficiency
slug: nif-efficiency
category: common-pitfalls
subcategory: native-code
tier: advanced
source: "Erlang Efficiency Guide"
source_slug: otp-efficiency-guide
authors: "Ericsson/OTP Team"
chapter: "Common Caveats"
chapter_number: null
pdf_page: null
section: "Using NIFs"
extraction_confidence: high
aliases:
  - "NIF performance"
  - "native implemented functions"
  - "NIF work granularity"
prerequisites:
  - function-call-performance
extends: []
related:
  - erlang-system-limits
contrasts_with: []
answers_questions:
  - "When should Erlang code be rewritten as a NIF?"
  - "What are the risks of doing too much or too little work in a NIF call?"
---

# Quick Definition

Rewriting Erlang code to a NIF (Native Implemented Function) should be a last resort. NIFs must balance work granularity: too much work per call degrades VM responsiveness, while too little work means the NIF overhead negates the performance gain.

# Core Definition

Rewriting Erlang code to a NIF to make it faster should be seen as a last resort. Doing too much work in each NIF call will degrade responsiveness of the VM. Doing too little work can mean that the gain of the faster processing in the NIF is eaten up by the overhead of calling the NIF and checking the arguments (Ericsson/OTP Team, "Common Caveats," section "Using NIFs").

The source directs readers to the documentation on long-running NIFs before writing a NIF, emphasizing the importance of understanding scheduler impact.

# Prerequisites

- **function-call-performance** -- Understanding the relative costs of different call types provides context for when NIF overhead is justified

# Key Properties

1. NIFs should be a last resort for performance optimization
2. Too much work per NIF call degrades VM (scheduler) responsiveness
3. Too little work per NIF call wastes the potential gain on call overhead
4. NIFs execute on scheduler threads, blocking them from running other Erlang processes
5. Long-running NIFs require special techniques (yielding, dirty schedulers) to avoid blocking
6. The optimal NIF work granularity is a balance between these two extremes

# Construction / Recognition

## When to Consider a NIF

1. Profile the Erlang code and identify a genuine bottleneck
2. Verify that algorithmic improvements in Erlang have been exhausted
3. Confirm the bottleneck is CPU-bound computation (not I/O)
4. Estimate whether the NIF call overhead is small relative to the work done
5. Assess the scheduler impact of the expected NIF execution time

## Avoiding Long-Running NIF Problems

1. Keep NIF execution time under 1 millisecond per call on normal schedulers
2. For longer operations, use dirty schedulers or NIF yielding techniques
3. Read the ERTS documentation on long-running NIFs before implementation

# Context & Application

NIFs are written in C (or other native languages via bindings) and execute directly on BEAM scheduler threads. While they can offer significant speedups for CPU-intensive computation, they come with serious trade-offs:

- A NIF that runs too long blocks its scheduler thread, preventing other Erlang processes from executing
- NIFs can crash the entire VM if they contain bugs (no process isolation)
- NIF code is harder to debug, test, and maintain than Erlang code
- The call overhead (argument conversion, safety checks) means trivial operations are not worth implementing as NIFs

**Typical use cases where NIFs are justified:**
- Cryptographic operations (as in the `crypto` module)
- Compression/decompression
- Image processing or other computationally intensive transformations
- Interfacing with C libraries that have no Erlang equivalent

# Examples

**Decision framework** (derived from source: "Common Caveats," section "Using NIFs"):

```
Is the Erlang code a measured performance bottleneck?
  No  -> Do not write a NIF
  Yes -> Have algorithmic optimizations been exhausted in Erlang?
    No  -> Optimize the Erlang code first
    Yes -> Will each NIF call do enough work to justify the overhead?
      No  -> Do not write a NIF (overhead will eat the gain)
      Yes -> Will each NIF call complete in under ~1ms?
        Yes -> Write a normal NIF
        No  -> Use dirty schedulers or NIF yielding
```

# Relationships

## Related

- **erlang-system-limits** -- Scheduler count and process limits are relevant when considering NIF impact on system resources
- **function-call-performance** -- NIF calls have their own overhead profile compared to Erlang call types

# Common Errors

- **Error**: Rewriting simple utility functions as NIFs for marginal speedup
  **Correction**: Only consider NIFs for measured bottlenecks where the work per call is substantial

- **Error**: Writing a NIF that runs for seconds without yielding
  **Correction**: Use dirty schedulers or implement NIF yielding for long-running operations

# Common Confusions

- **Confusion**: Believing NIFs are always faster than Erlang code
  **Clarification**: NIF call overhead (argument checking, term conversion) can negate gains for small operations

- **Confusion**: Thinking NIFs are isolated like Erlang processes
  **Clarification**: A NIF bug (segfault, memory corruption) crashes the entire Erlang VM, not just the calling process

# Source Reference

"Common Caveats," section "Using NIFs." Brief section advising NIFs as a last resort and warning about the work granularity trade-off. References the ERTS erl_nif documentation for long-running NIF details.

# Verification Notes

- Definition: Direct from source -- "Rewriting Erlang code to a NIF to make it faster should be seen as a last resort"
- Work granularity trade-off: Both directions (too much, too little) explicitly stated in source
- Long-running NIF reference: Explicitly mentioned with link to ERTS docs
- Confidence: HIGH -- explicit documentation from official OTP guide, though the section is brief
