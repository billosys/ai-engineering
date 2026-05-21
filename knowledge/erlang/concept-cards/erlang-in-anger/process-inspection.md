---
concept: Process Inspection
slug: process-inspection
category: production-ops
subcategory: live-debugging
tier: intermediate
source: "Stuff Goes Bad: Erlang in Anger"
source_slug: erlang-in-anger
authors: "Fred Hébert"
chapter: "Runtime Metrics"
chapter_number: 5
pdf_page: null
section: "Digging In > Processes"
extraction_confidence: high
aliases:
  - "process_info/2"
  - "recon:info/1"
prerequisites:
  - runtime-introspection
  - reduction
extends: []
related:
  - recon-proc-count
  - recon-proc-window
  - sys-module-introspection
contrasts_with: []
answers_questions:
  - "How do I safely inspect a process?"
  - "How can I find what code a process is running?"
  - "Which process inspection values are dangerous in production?"
---

# Quick Definition

Process inspection is the act of querying a single process's metadata, signals, location, memory, and work via `process_info(Pid, Key)` or recon's safer `recon:info/1` wrapper — distinguishing keys that are safe in production from those that can crash the node.

# Core Definition

"All the values can be obtained by calling `process_info(Pid, Key)` or `process_info(Pid, [Keys])`" (Chapter 5, "Digging In > Processes").

The VM "makes a lot of information available, some of which is safe to use, and some of which is unsafe to use in production (because they can return data sets large enough that the amount of memory copied to the shell process and used to print it can kill the node)."

# Prerequisites

- `runtime-introspection`: process inspection is the core "in the small" tool.
- `reduction`: the `reductions` key is a key inspection value.

# Key Properties

1. Common *safe* keys: `dictionary`, `group_leader`, `registered_name`, `status`, `links`, `monitored_by`, `monitors`, `trap_exit`, `current_function`, `current_location`, `current_stacktrace`, `initial_call`, `garbage_collection`, `heap_size`, `memory`, `message_queue_len`, `total_heap_size`, `reductions`.
2. Dangerous keys: `messages` (a mailbox can hold millions of messages) and `binary` (a process may have many refc binaries). Always check `message_queue_len` before requesting `messages`.
3. `links` is generally safe but can return thousands of entries on large supervisors — use with care.
4. `heap_size` and `total_heap_size` are reported in *words*; `memory` is reported in *bytes*.
5. `recon:info/1` regroups the common, safe keys into categories: `meta`, `signals`, `location`, `memory_used`, `work`.
6. `recon:info/1` accepts any pid-like argument: literal pids, strings (`"<0.12.0>"`), registered atoms, global names (`{global, Atom}`), third-party registry names (`{via, gproc, Name}`), or tuples (`{0,12,0}`).
7. `recon:info(Pid, [Keys])` works like `process_info/2` and *can* fetch unsafe information.
8. `process_flag(sensitive, true)` lets a process keep its information private.

# Construction / Recognition

Use `recon:info(Pid)` for a safe categorized dump, `recon:info(Pid, Category)` for one category (e.g. `work`), or `recon:info(Pid, [Keys])` for specific keys. Before calling `messages`, always call `message_queue_len` first.

# Context & Application

Used to diagnose a specific suspect process: what code it runs (`current_function`, `initial_call`, `current_stacktrace`), how much memory it holds, how loaded its mailbox is, and how much work it does.

# Examples

From Chapter 5, "Digging In > Processes":

```erlang-repl
1> recon:info("<0.12.0>").
[{meta,[{registered_name,rex}, ...]},
 {signals,[{links,[<0.11.0>]}, {monitors,[]}, {monitored_by,[]}, {trap_exit,true}]},
 {location,[{initial_call,{proc_lib,init_p,5}}, ...]},
 {memory_used,[{memory,2808},{message_queue_len,0},{heap_size,233}, ...]},
 {work,[{reductions,35}]}]
```

```erlang-repl
3> recon:info(self(), [memory, status]).
[{memory,10600},{status,running}]
```

# Relationships

## Builds Upon
- runtime-introspection
- reduction

## Enables
- recon-proc-count
- recon-proc-window

## Related
- sys-module-introspection

## Contrasts With

# Common Errors

- Calling `process_info(Pid, messages)` on a process with a huge mailbox — copying millions of messages to the shell can kill the node. Always check `message_queue_len` first.
- Fetching `binary` on a process with many refc binaries — same danger.
- Confusing units: `heap_size`/`total_heap_size` are in words, `memory` is in bytes.

# Common Confusions

- `recon:info/1` is safe by default, but `recon:info(Pid, [Keys])` can still fetch unsafe keys — the safety is in *which keys* you ask for.
- `current_function` shows what is running now; `initial_call` shows what the process was spawned as — they are different questions.

# Source Reference

Chapter 5: Runtime Metrics, Section "Digging In > Processes". (No PDF pages — this source has none.)

# Verification Notes

- Definition source: quoted from the chapter.
- Confidence rationale: high — keys and safety notes explicitly documented.
- Uncertainties: none.
- Cross-reference status: Verified
