---
concept: Code Memory Leak
slug: code-memory-leak
category: production-ops
subcategory: memory
tier: intermediate
source: "Stuff Goes Bad: Erlang in Anger"
source_slug: erlang-in-anger
authors: "Fred Hébert"
chapter: "Memory Leaks"
chapter_number: 7
pdf_page: null
section: "Code"
extraction_confidence: high
aliases:
  - "HiPE code leak"
  - "Native code memory leak"
prerequisites:
  - memory-leak-detection
related:
  - atom-leak
contrasts_with: []
answers_questions:
  - "How could code itself cause a memory leak?"
  - "Why can HiPE native code not be garbage collected?"
---

# Quick Definition

A code memory leak is growth in the code memory area of a node, most commonly caused by HiPE native-compiled modules, which — unlike regular BEAM bytecode — cannot be garbage collected when new versions are loaded.

# Core Definition

From section "Code": the code on an Erlang node is loaded into its own memory area and sits there until garbage collected. Only two copies of a module can coexist at one time, so very large modules are easy-ish to spot. If no large module stands out, the culprit is often HiPE-compiled code: "HiPE code, unlike regular BEAM code, is native code and cannot be garbage collected from the VM when new versions are loaded. Memory can accumulate, usually very slowly, if many or large modules are native-compiled and loaded at run time."

# Prerequisites

- `memory-leak-detection` — recognizing that the code memory category is growing is the precondition for this investigation.

# Key Properties

1. Code lives in its own memory area and stays there until garbage collected.
2. At most two copies of a module can coexist (current and old) — so very large modules are easy to find.
3. Regular BEAM bytecode is garbage-collectable when superseded; HiPE native code is not.
4. HiPE code accumulates slowly when many or large modules are native-compiled and loaded at run time.
5. Unexpected, unfamiliar modules on a node may indicate a security compromise rather than a benign leak.

# Construction / Recognition

1. Confirm that code memory is the growing category.
2. Look for very large modules — only two copies can exist, so they are conspicuous.
3. If none stand out, look for HiPE native-compiled modules loaded at run time.
4. Also scan for weird modules you did not load yourself — and treat their presence as a possible intrusion.

# Context & Application

This applies to long-lived nodes that hot-load code repeatedly, especially systems using HiPE for performance-critical modules. Because HiPE native code is never reclaimed, repeated reloads of native modules cause slow, steady code-memory growth.

# Examples

From section "Code": "Alternatively, you may look for weird modules you didn't load yourself on the node and panic if someone got access to your system!"

# Relationships

## Builds Upon
- `memory-leak-detection` — this is one branch of the leak investigation.

## Enables
Nothing — terminal investigation card.

## Related
- `atom-leak` — another category of memory that is not reclaimed by ordinary garbage collection.

## Contrasts With
Nothing specific within this source.

# Common Errors

- Assuming all code is garbage-collectable; HiPE native code is the exception.
- Overlooking that repeated run-time loading of native modules is what causes accumulation, not a single load.

# Common Confusions

- Regular BEAM bytecode and HiPE native code differ fundamentally: the former is reclaimed when a third version would be needed, the latter is not.

# Source Reference

Chapter 7: Memory Leaks, Section "Code". (No PDF pages — this source has none.)

# Verification Notes

- Definition source: quoted from section "Code."
- Confidence rationale: high — the source explicitly describes the HiPE leak mechanism.
- Uncertainties: none.
- Cross-reference status: Verified
