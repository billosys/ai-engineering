---
concept: ETS Leak
slug: ets-leak
category: production-ops
subcategory: memory
tier: intermediate
source: "Stuff Goes Bad: Erlang in Anger"
source_slug: erlang-in-anger
authors: "Fred Hébert"
chapter: "Memory Leaks"
chapter_number: 7
pdf_page: null
section: "ETS"
extraction_confidence: high
aliases:
  - "ETS table leak"
prerequisites:
  - memory-leak-detection
related:
  - process-leak
contrasts_with: []
answers_questions:
  - "How can I find out if ETS tables are growing too fast?"
  - "Why is ETS memory not reclaimed automatically?"
---

# Quick Definition

An ETS leak is unbounded growth of memory held by ETS tables, which arises because ETS tables are never garbage collected — memory is reclaimed only by manually deleting records or dropping the table.

# Core Definition

From section "ETS": "ETS tables are never garbage collected, and will maintain their memory usage as long as records will be left undeleted in a table. Only removing records manually (or deleting the table) will reclaim memory." To diagnose, the chapter recommends the undocumented `ets:i()` function in the shell, which prints information on the number of entries (`size`) and the memory they take (`mem`).

# Prerequisites

- `memory-leak-detection` — recognizing that ETS memory is growing is the precondition for this investigation.

# Key Properties

1. ETS tables are never garbage collected.
2. Memory is held as long as records remain undeleted; only manual deletion or dropping the table reclaims it.
3. The undocumented `ets:i()` shell function prints per-table `size` (entries) and `mem` (memory).
4. Not all ETS growth is a leak — the data may be legitimate, indicating a need to shard across nodes.
5. The `compressed` option for `ets:new/2` can buy time by reducing table footprint.

# Construction / Recognition

1. Confirm ETS is the growing memory category.
2. Call `ets:i()` in the shell to list tables with their `size` and `mem`.
3. Identify any table whose entry count or memory looks abnormal.
4. If all data is legitimate, consider sharding the data set across nodes, or use the `compressed` table option as a stopgap.

# Context & Application

ETS leaks occur whenever a process inserts records into a table and never removes them — caches without eviction, session stores without timeouts, accumulators. Because ETS sits in its own un-collected memory area, the leak persists until explicit deletion.

# Examples

From section "ETS": "In the rare cases you're actually leaking ETS data, call the undocumented `ets:i()` function in the shell. It will print out information regarding number of entries (`size`) and how much memory they take (`mem`)."

# Relationships

## Builds Upon
- `memory-leak-detection` — one branch of the leak investigation.

## Enables
Nothing — terminal investigation card.

## Related
- `process-leak` — another category investigated when overall counts grow.

## Contrasts With
Nothing specific within this source.

# Common Errors

- Expecting ETS memory to be reclaimed by garbage collection; it is reclaimed only by explicit record/table deletion.
- Treating all ETS growth as a bug when the data set may legitimately need to be sharded.

# Common Confusions

- A growing ETS table is not always a leak — it can be a genuine capacity problem requiring sharding rather than a code defect.

# Source Reference

Chapter 7: Memory Leaks, Section "ETS". (No PDF pages — this source has none.)

# Verification Notes

- Definition source: quoted from section "ETS."
- Confidence rationale: high — the source explicitly states the mechanism and the diagnostic tool.
- Uncertainties: none.
- Cross-reference status: Verified
