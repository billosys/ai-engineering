---
# === CORE IDENTIFICATION ===
concept: Large-System Profiling
slug: large-system-profiling

# === CLASSIFICATION ===
category: performance
subcategory: null
tier: advanced

# === PROVENANCE ===
source: "Erlang Efficiency Guide"
source_slug: otp-efficiency-guide
authors: "Ericsson/OTP Team"
chapter: "Profiling"
chapter_number: null
pdf_page: null
section: "Large Systems"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "system-level profiling"
  - "production profiling"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - profiling-strategy
  - profiling-analysis
extends:
  - profiling-strategy
related:
  - fprof
  - eprof
  - dbg-profiling
  - lcnt
  - memory-profiling
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What must I understand before profiling a large system?"
  - "How do I profile an Erlang application to find performance bottlenecks?"
  - "What tools give a system-wide view with low overhead?"
---

# Quick Definition

Large-system profiling involves strategies and tools for profiling production-scale Erlang systems, where bottlenecks may only appear under real load with many concurrent processes and nodes. It uses low-overhead tools like `observer`, `etop`, and `msacc` for system-wide views before drilling down with targeted profilers.

# Core Definition

The Erlang Efficiency Guide dedicates a section to large-system profiling: "For a large system, it can be interesting to run profiling on a simulated and limited scenario to start with. But bottlenecks have a tendency to appear or cause problems only when many things are going on at the same time, and when many nodes are involved. Therefore, it is also desirable to run profiling in a system test plant on a real target system."

The guide continues: "For a large system, you do not want to run the profiling tools on the whole system. Instead you want to concentrate on central processes and modules, which account for a big part of the execution."

Three system-wide monitoring tools are recommended: `observer` (GUI tool for remote node monitoring), `etop` (command-line top-like tool), and `msacc` (microstate accounting with very low overhead).

# Prerequisites

- **Profiling Strategy** -- Understanding the fundamental principle that bottlenecks must be measured, not guessed.
- **Profiling Analysis** -- Knowing what to look for in profiling results before tackling a large system.

# Key Properties

1. Bottlenecks may only appear when many things happen simultaneously and many nodes are involved.
2. Start with simulated/limited scenarios, then move to real target systems.
3. Do not profile the whole system -- concentrate on central processes and modules.
4. Use low-overhead tools for system-wide views before targeted profiling.
5. `observer` provides a GUI for remote node monitoring.
6. `etop` provides command-line top-like views of remote nodes.
7. `msacc` shows what the Erlang Run-Time System spends its time doing, with very low overhead.
8. Real system test plants on real target systems are desirable for finding production-only bottlenecks.

# Construction / Recognition

## To Profile a Large System:
1. Start with a simulated/limited scenario to establish baseline behavior.
2. Use `msacc` (very low overhead) to get a broad view of where the runtime spends time.
3. Use `observer` or `etop` to identify which processes consume the most resources.
4. Narrow focus to central processes and modules that account for most execution.
5. Apply targeted profiling tools (fprof, eprof, tprof, dbg) to the identified hotspots.
6. Run profiling on a real target system to catch bottlenecks that only appear under real load.

## To Recognize When Large-System Profiling Is Needed:
1. Bottlenecks that appear in production but not in unit tests.
2. Performance that degrades non-linearly with system load or number of nodes.
3. Profiling individual modules in isolation fails to reproduce the performance issue.

# Context & Application

This section addresses a practical reality of Erlang/OTP systems: they are often distributed, multi-node applications with many concurrent processes. Performance bottlenecks in such systems are qualitatively different from those in small programs -- they emerge from interactions between components, contention on shared resources, and communication patterns that only manifest at scale.

The guide's advice to "concentrate on central processes and modules" is pragmatic: in a large system, most execution time is typically spent in a small number of hot paths. System-wide monitoring tools help identify those paths before applying heavyweight profilers.

**System-wide tools:**
- `observer` -- GUI tool that connects to remote nodes and displays a variety of information about the running system.
- `etop` -- Command-line tool that connects to remote nodes and displays information similar to what the UNIX tool `top` shows.
- `msacc` -- Allows the user to get a view of what the Erlang Run-Time System is spending its time doing. Has very low overhead, making it useful in heavily loaded systems to identify where to start more granular profiling.

# Examples

**Example 1** (profiling.md, "Large Systems"): The source describes the progression from simulated profiling to real-system profiling: "bottlenecks have a tendency to appear or cause problems only when many things are going on at the same time, and when many nodes are involved."

**Example 2** (profiling.md, "Large Systems"): The source recommends `msacc` specifically for heavily loaded systems due to its "very low overhead, which makes it useful to run in heavily loaded systems to get some idea of where to start doing more granular profiling."

# Relationships

## Builds Upon
- **profiling-strategy** -- large-system profiling extends the basic profiling strategy to production-scale systems
- **profiling-analysis** -- you need to know what to look for before profiling large systems

## Enables
- Identification of production-only bottlenecks
- Targeted application of profiling tools to central processes

## Related
- **lcnt** -- lock contention is a particularly relevant concern in large multi-scheduler systems
- **dbg-profiling** -- dbg's precision targeting is valuable for narrowing down issues in large systems
- **memory-profiling** -- memory issues often manifest in large systems under load

## Contrasts With
- No direct contrasts in source, though the approach implicitly contrasts with naive whole-system profiling.

# Common Errors

- **Error**: Running fprof or eprof on an entire large system.
  **Correction**: Concentrate on central processes and modules. Use low-overhead tools (observer, etop, msacc) first to identify where to focus.

- **Error**: Profiling only in simulated environments and assuming results apply to production.
  **Correction**: Bottlenecks often appear only when many things happen simultaneously and many nodes are involved. Profile in real target systems as well.

# Common Confusions

- **Confusion**: Thinking observer, etop, and msacc are full profilers.
  **Clarification**: These are system-wide monitoring tools that help identify where to focus more detailed profiling. They do not replace fprof, eprof, or tprof for function-level analysis.

- **Confusion**: Believing that profiling a simulated scenario is sufficient.
  **Clarification**: The source explicitly states that bottlenecks "have a tendency to appear or cause problems only when many things are going on at the same time, and when many nodes are involved."

# Source Reference

Erlang Efficiency Guide, "Profiling" chapter, "Large Systems" section. References `observer`, `etop`, and `msacc` modules with their manual pages.

# Verification Notes

- Definition: Directly quoted from the "Large Systems" section.
- Key Properties: All points derived from source text.
- Tool descriptions: Quoted from source's tool listings.
- Confidence: HIGH -- the source dedicates a named section to this topic with explicit methodology and tool recommendations.
- Cross-references: All tool slugs correspond to cards in this extraction.
- Uncertainties: None.
