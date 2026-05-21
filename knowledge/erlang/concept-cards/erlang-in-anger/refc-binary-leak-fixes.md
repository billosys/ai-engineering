---
concept: Refc Binary Leak Fixes
slug: refc-binary-leak-fixes
category: production-ops
subcategory: binaries
tier: advanced
source: "Stuff Goes Bad: Erlang in Anger"
source_slug: erlang-in-anger
authors: "Fred Hébert"
chapter: "Memory Leaks"
chapter_number: 7
pdf_page: null
section: "Fixing Leaks"
extraction_confidence: high
aliases:
  - "Fixing binary memory leaks"
prerequisites:
  - refc-binary-leak-detection
related:
  - routing-binaries-pattern
  - refc-binary
contrasts_with: []
answers_questions:
  - "How do I fix a refc binary leak?"
  - "What should I do to minimize binary memory usage on a node?"
---

# Quick Definition

Refc binary leaks are fixed by making the leaking process garbage collect more often or hold binaries more briefly — via hibernation, `binary:copy/1-2` on small fragments, moving work to one-off processes, or (as a last resort) manual GC.

# Core Definition

From section "Fixing Leaks": once a binary memory leak is established with `recon:bin_leak(Max)`, the leaking processes are inspected, and the leak "can be solved in a few different ways, depending on the source":

1. Call garbage collection manually at given intervals ("icky, but somewhat efficient").
2. Stop using binaries ("often not desirable").
3. Use `binary:copy/1-2` if keeping only a small fragment (usually less than 64 bytes) of a larger binary.
4. Move work involving larger binaries to temporary one-off processes that die when done (a lesser form of manual GC).
5. Add hibernation calls when appropriate (possibly the cleanest solution for inactive processes).

The first two options are "frankly not agreeable" and should be tried last; the last three are usually the best.

# Prerequisites

- `refc-binary-leak-detection` — you must have confirmed and localized the leak before applying a fix.

# Key Properties

1. Five options exist; the last three (copy, one-off processes, hibernation) are preferred.
2. `binary:copy/1-2` breaks the reference to a large binary by copying the small fragment you actually keep, letting the large binary be collected.
3. Copying is worthwhile even for a fairly large fragment — e.g. copying 10 MB off a 2 GB binary frees the 2 GB binary.
4. One-off processes die when finished, releasing all their binary references at once.
5. Hibernation forces a process to shrink and garbage collect — ideal for inactive processes.
6. Manual periodic GC works but is considered ugly; abandoning binaries entirely is usually undesirable.

# Construction / Recognition

1. Identify the leaking process and what work it does.
2. If it idles between bursts, add `hibernate` calls.
3. If it keeps a small slice of a large binary, apply `binary:copy/1-2` to that slice.
4. If it does heavy one-shot binary work, spawn a temporary process to do it and let that process die.
5. Only if none of those fit, fall back to periodic manual `garbage_collect`.

# Context & Application

This is the remediation step after `recon:bin_leak/1` localizes the leak. The choice depends on the process's behaviour: idle processes get hibernation; fragment-keepers get `binary:copy`; heavy one-shot work gets one-off processes. (Open-ended question 2 of the chapter — a process opening a 150 MB log file and storing an extract in ETS — is solved by `binary:copy/1` on the extracted fragment.)

# Examples

From section "Fixing Leaks," footnote: "It might be worth copying even a larger fragment of a refc binary. For example, copying 10 megabytes off a 2 gigabytes binary should be worth the short-term overhead if it allows the 2 gigabytes binary to be garbage-collected while keeping the smaller fragment longer."

# Relationships

## Builds Upon
- `refc-binary-leak-detection` — fixes are applied after detection localizes the leak.

## Enables
Nothing — terminal remediation card.

## Related
- `routing-binaries-pattern` — a fix for the specific router-process variant of the leak.
- `refc-binary` — the data type whose lifecycle these fixes manage.

## Contrasts With
Nothing specific within this source.

# Common Errors

- Reaching for manual periodic GC or abandoning binaries first; these are last-resort options.
- Keeping a small fragment of a huge binary without `binary:copy`, which pins the entire huge binary in memory.

# Common Confusions

- `binary:copy` *increases* short-term memory (the fragment is duplicated) but *reduces* long-term memory by letting the large source binary be collected — a deliberate trade-off.

# Source Reference

Chapter 7: Memory Leaks, Section "Fixing Leaks". (No PDF pages — this source has none.)

# Verification Notes

- Definition source: quoted from section "Fixing Leaks."
- Confidence rationale: high — the source explicitly enumerates the five fixes.
- Uncertainties: none.
- Cross-reference status: Verified
