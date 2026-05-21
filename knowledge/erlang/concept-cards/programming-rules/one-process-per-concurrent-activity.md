---
concept: One Parallel Process Per True Concurrent Activity
slug: one-process-per-concurrent-activity
category: processes-concurrency
subcategory: processes-servers-messages
tier: intermediate
source: "Program Development Using Erlang — Programming Rules and Conventions"
source_slug: programming-rules
authors: "Klas Eriksson, Mike Williams, Joe Armstrong"
chapter: "Processes, Servers and Messages"
chapter_number: 5
pdf_page: null
section: "5.4 Assign exactly one parallel process to each true concurrent activity in the system"
extraction_confidence: high
aliases:
  - "one process per concurrent activity"
  - "model concurrency with processes"
prerequisites: []
extends: []
related:
  - use-processes-for-structuring
  - one-role-per-process
contrasts_with: []
answers_questions:
  - "How many processes should model a given concurrent activity?"
  - "How do I decide between sequential and parallel processes?"
---

# Quick Definition

Use exactly one parallel process to model each truly concurrent activity in the real world.

# Core Definition

"Use one parallel process to model each truly concurrent activity in the real world" (Programming Rules, 5.4). When deciding between sequential and parallel processes, follow the intrinsic structure of the problem. If there is a one-to-one mapping between the number of parallel processes and the number of truly parallel real-world activities, the program will be easy to understand.

# Prerequisites

This is a foundational concept with no prerequisites within this source.

# Key Properties

1. Each truly concurrent real-world activity is modeled by exactly one process.
2. The process structure follows the intrinsic structure of the problem.
3. A one-to-one process/activity mapping makes the program easy to understand.

# Construction / Recognition

## To Apply

1. Identify the genuinely concurrent activities in the problem domain.
2. Create one process per such activity — no more, no fewer.

## To Recognize a Violation

1. The process count does not match the number of real concurrent activities (too many or too few).

# Context & Application

A core process-design principle (section 5).

- **Typical contexts**: modeling concurrent real-world entities (calls, sessions, connections).
- **Common applications**: one process per active call in a telecom system.

# Examples

The source gives the rule as a quoted maxim; no code listing is given.

# Relationships

## Related

- **Use processes for structuring the system** — this rule is the criterion for when a process is warranted.
- **Each process should only have one "role"** — companion process-design rule.

# Common Errors

- **Error**: Using one process for several concurrent activities, or many processes for one.
  **Correction**: Map exactly one process to each truly concurrent activity.

# Common Confusions

- **Confusion**: Adding processes for parallelism that the problem does not actually have.
  **Clarification**: The mapping is to *truly* concurrent activities; invented parallelism only adds complexity.

# Source Reference

"Program Development Using Erlang — Programming Rules and Conventions", section 5.4 "Assign exactly one parallel process to each true concurrent activity in the system".

# Verification Notes

- Definition source: Direct adaptation of section 5.4.
- Confidence rationale: HIGH — the rule is stated explicitly as a quoted maxim.
- Uncertainties: None.
- Cross-reference status: all referenced slugs are planned cards in this extraction.
