---
concept: Full Mailbox Diagnosis
slug: full-mailbox-diagnosis
category: production-ops
subcategory: crash-analysis
tier: intermediate
source: "Stuff Goes Bad: Erlang in Anger"
source_slug: erlang-in-anger
authors: "Fred Hébert"
chapter: "Reading Crash Dumps"
chapter_number: 6
pdf_page: null
section: "Full Mailboxes"
extraction_confidence: high
aliases:
  - queue_fun.awk
  - loaded mailboxes
prerequisites:
  - crash-dump-analysis
extends: []
related:
  - process-inspection
  - out-of-memory-crash
contrasts_with: []
answers_questions:
  - "How do I read a crash dump?"
  - "How do I diagnose overflowing mailboxes from a crash dump?"
---

# Quick Definition

Full mailbox diagnosis is the crash-dump technique of finding processes with very long message queues and identifying what function they were running, typically using recon's `queue_fun.awk` script.

# Core Definition

"For loaded mailboxes, looking at large counters is the best way to do it. If there is one large mailbox, go investigate the process in the crash dump... If you find out many mailboxes are loaded, you may want to use recon's `queue_fun.awk` to figure out what function they're running at the time of the crash" (Chapter 6, "Full Mailboxes").

# Prerequisites

- `crash-dump-analysis`: full mailbox diagnosis is one branch of the broader crash-dump workflow.

# Key Properties

1. Start from the "largest message queue lengths" counters in the dump summary.
2. One large mailbox → investigate that single process: is it failing to match on some message, or is it overloaded?
3. Many large mailboxes → use `queue_fun.awk` to see what function the loaded processes were running.
4. `queue_fun.awk` takes a `threshold` variable and the dump path; it outputs the current function of every process with at least `threshold` messages queued.
5. A common revealing result: many processes blocked on the same function (e.g. `io:wait_io_mon_reply/2`), indicating node-wide lock-up — in the book's example, the node was locked waiting on IO for `io:format/2` calls.
6. If a similar node is still running live, you can log onto it and inspect the equivalent process directly.

# Construction / Recognition

1. Read the largest mailbox counters from the analyzer summary.
2. For one offender, locate that process in the dump.
3. For many offenders, run `awk -v threshold=10000 -f queue_fun.awk /path/to/erl_crash.dump`.
4. Look for a function shared across many loaded mailboxes — it points at the bottleneck.

# Context & Application

Used when a crash dump shows abnormally long message queues — a symptom of overload or of a process failing to selectively receive certain messages.

# Examples

From Chapter 6, "Full Mailboxes":

```text
$ awk -v threshold=10000 -f queue_fun.awk /path/to/erl_crash.dump
MESSAGE QUEUE LENGTH: CURRENT FUNCTION
======================================
10641: io:wait_io_mon_reply/2
12646: io:wait_io_mon_reply/2
...
2183837: io:wait_io_mon_reply/2
```

"In the case of this run, the script showed that the entire node was locking up waiting on IO for `io:format/2` calls."

# Relationships

## Builds Upon
- crash-dump-analysis

## Enables

## Related
- process-inspection
- out-of-memory-crash

## Contrasts With

# Common Errors

- Setting the `queue_fun.awk` threshold too low and drowning in noise — pick a threshold meaningful for the node.
- Treating one huge mailbox and many medium mailboxes the same — the former is an individual process bug, the latter suggests systemic overload/contention.

# Common Confusions

- A loaded mailbox can mean two distinct things — selective-receive mismatch vs. raw overload — and the dump alone may not disambiguate; a live similar node helps.

# Source Reference

Chapter 6: Reading Crash Dumps, Section "Full Mailboxes". (No PDF pages — this source has none.)

# Verification Notes

- Definition source: quoted from the chapter.
- Confidence rationale: high — explicitly described with the `queue_fun.awk` example.
- Uncertainties: none.
- Cross-reference status: Verified
