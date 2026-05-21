---
# === CORE IDENTIFICATION ===
concept: Priority Messages
slug: priority-messages

# === CLASSIFICATION ===
category: processes-concurrency
subcategory: null
tier: advanced

# === PROVENANCE ===
source: "Erlang Reference Manual"
source_slug: otp-reference-manual
authors: "Ericsson AB"
chapter: "Processes"
chapter_number: null
pdf_page: null
section: "Enabling Priority Message Reception"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - priority message reception
  - priority alias

# === TYPED RELATIONSHIPS ===
prerequisites:
  - erlang-process
  - message-queue
  - process-aliases
extends:
  - message-queue
  - process-aliases
related:
  - message-receiving
  - links
  - monitors
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What are priority messages in Erlang?"
  - "How do I enable priority message reception?"
---

# Quick Definition
Priority messages (introduced in OTP 28.0) allow certain messages to be inserted ahead of ordinary messages in a process's message queue. A process enables this by creating a priority process alias, and senders must use both the priority alias and the `priority` option via `erlang:send/3` to send priority messages.

# Core Definition
The Erlang Reference Manual explains: "A process can enable priority message reception by creating a _priority process alias_ or shorter _priority alias_. Such an alias is created by calling the `erlang:alias/1` BIF with the `priority` option." To send a priority message, "the priority alias should be passed to the `erlang:send/3` BIF at the same time as the option `priority` is passed in the option list. Note that both the priority alias and the `priority` option need to be passed in order for the message to be accepted as a priority message." When priority messages exist in the queue, they are placed "after the last accepted priority message in the queue," while ordinary messages remain at the end. (Processes chapter, "Enabling Priority Message Reception" subsection).

# Prerequisites
- **erlang-process** -- Priority messages are received by processes
- **message-queue** -- Must understand how the message queue works before understanding priority ordering
- **process-aliases** -- Priority aliases are a special kind of process alias

# Key Properties
1. Introduced in OTP 28.0
2. Enabled by creating a priority alias via `erlang:alias/1` with the `priority` option
3. Both the priority alias AND the `priority` option must be passed to `erlang:send/3`
4. Priority messages are inserted after the last priority message, before ordinary messages
5. The queue has two logical regions: priority messages (P) followed by ordinary messages (M)
6. Total queue length = P + M; the individual lengths are not visible
7. Priority messages do NOT violate the signal ordering guarantee
8. There is no way to distinguish a priority message from an ordinary message when fetching
9. Processes are not optimized for large amounts of priority messages
10. Priority can also be enabled for exit signals (via `erlang:exit/3` with priority alias and option) and for monitor/link signals

# Construction / Recognition
## To Construct/Create:
1. Create a priority alias: `Alias = erlang:alias([priority])`
2. Distribute the alias to potential senders
3. Senders use `erlang:send(Alias, Message, [priority])` to send priority messages

## To Identify/Recognize:
1. There is no way to distinguish a priority message from an ordinary message when fetching from the queue
2. Knowledge of the message protocol is required to know which messages are priority

# Context & Application
The source includes an explicit warning: "Priority messages are intended to solve very specific problems where it previously was very hard to solve such problems efficiently using ordinary signaling. You *very seldom* need to resort to usage of priority messages." They are not a general-purpose mechanism and the receiving process is not optimized for large amounts of priority messages. This feature is for cases where certain control messages need to be processed before a backlog of data messages.

# Examples
**Example 1** (Processes, "Enabling Priority Message Reception" section): The source describes the queue structure: when priority messages exist, they form a region at the front of the queue (after any earlier priority messages), with ordinary messages following. A `receive` expression "will select the first message, from the start, in the message queue that matches, just as if only ordinary messages exist."

**Example 2** (Processes, "Enabling Priority Message Reception" section): Priority can also be applied to monitor and link signals: "In order to enable priority message reception of messages triggered by a monitor, the process that creates the monitor needs to create it using the `erlang:monitor/3` BIF and pass the option `priority`."

# Relationships
## Builds Upon
- **message-queue** -- Priority messages modify the default queue ordering
- **process-aliases** -- Priority aliases extend the alias mechanism

## Enables
No concepts depend on priority messages specifically.

## Related
- **message-receiving** -- Priority messages are fetched the same way as ordinary messages
- **links** -- Priority can be applied to exit signals from links via `erlang:link/2` with `priority` option
- **monitors** -- Priority can be applied to DOWN messages via `erlang:monitor/3` with `priority` option

## Contrasts With
No direct contrasts.

# Common Errors
- **Error**: Using only the priority alias without the `priority` option (or vice versa) when sending
  **Correction**: Both the priority alias AND the `priority` option must be provided to `erlang:send/3` for the message to be treated as priority.

# Common Confusions
- **Confusion**: Thinking priority messages give the exit signal itself higher priority
  **Clarification**: For exit signals with priority, "this *only* affects how a potential exit message is handled if the receiver is trapping exits. The exit signal as such will not get a higher priority."

# Source Reference
Processes chapter, "Enabling Priority Message Reception" subsection.

# Verification Notes
- Definition source: Direct from source with extensive quoting
- Confidence rationale: High -- detailed section with explicit warning and usage instructions
- Uncertainties: None
- Cross-reference status: All slugs verified against planned extraction
