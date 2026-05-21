---
# === CORE IDENTIFICATION ===
concept: Hibernation
slug: hibernation

# === CLASSIFICATION ===
category: otp-behaviours
subcategory: state-machine
tier: advanced

# === PROVENANCE ===
source: "OTP Design Principles"
source_slug: otp-design-principles
authors: "Ericsson AB"
chapter: "gen_statem Behaviour"
chapter_number: null
pdf_page: null
section: "Hibernation"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "hibernate"
  - "process hibernation"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - gen-statem
  - transition-actions
extends: []
related:
  - event-timeout
  - gen-server
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What must I know before using gen_statem?"
---

# Quick Definition

Hibernation in `gen_statem` minimizes the memory footprint of a server process by garbage collecting its heap via `proc_lib:hibernate/3`, activated through the `hibernate` transition action and best used during idle states.

# Core Definition

As described in the OTP Design Principles: "If you have many servers in one node and they have some state(s) in their lifetime in which the servers can be expected to idle for a while, and the amount of heap memory all these servers need is a problem, then the memory footprint of a server can be minimized by hibernating it through proc_lib:hibernate/3." The source cautions: "It is rather costly to hibernate a process; see erlang:hibernate/3. It is not something you want to do after every event."

# Prerequisites

- **gen_statem** -- The behaviour that supports hibernation via transition actions.
- **Transition actions** -- Hibernate is ordered as a transition action.

# Key Properties

1. Activated by the `hibernate` atom or `{hibernate, true}` in the transition actions list.
2. Triggers garbage collection of the process heap, reducing memory footprint.
3. Costly operation -- should not be done after every event.
4. Best applied in states where the server is expected to idle for a while.
5. The server automatically "wakes up" when the next event arrives.
6. Can also be triggered automatically using the `{hibernate_after, Timeout}` start option.
7. An event timeout can be used to trigger hibernation after a period of inactivity.

# Construction / Recognition

## To Construct/Create:
1. Include `hibernate` in the transition actions list when entering an idle state.
2. Alternatively, use `{hibernate_after, Timeout}` as a start option for automatic hibernation.

## To Identify/Recognize:
1. The `hibernate` atom or `{hibernate, true}` in a transition actions list.
2. Typically placed in state enter calls or transitions to idle states.
3. `{hibernate_after, Timeout}` in start options.

# Context & Application

Hibernation is a memory optimization for systems with many gen_statem processes that spend significant time idle. The source demonstrates hibernating in the `open` state of the code_lock example, since the door normally just waits for the state timeout. The source notes that the server should produce "non-insignificant garbage during callback execution" for hibernation to be worthwhile.

# Examples

**Example 1** (statem.md, "Hibernation"): Hibernating when entering the open state:

```erlang
handle_event(enter, _OldState, {open,_}, _Data) ->
    do_unlock(),
    {keep_state_and_data,
     [{state_timeout,10_000,lock},
      hibernate]};
```

**Example 2** (statem.md, "Hibernation"): The source describes alternative approaches: "Another not uncommon scenario is to use the event time-out to trigger hibernation after a certain time of inactivity. There is also a server start option `{hibernate_after, Timeout}` for `start/3,4`, `start_link/3,4`, or `enter_loop/4,5,6` that may be used to automatically hibernate the server."

# Relationships

## Builds Upon
- **Transition actions** -- Hibernate is a transition action.
- **gen_statem** -- The engine that manages process hibernation.

## Enables
- Memory optimization for systems with many idle state machine processes.

## Related
- **Event timeout** -- Can be used to trigger hibernation after inactivity.
- **gen_server** -- Also supports hibernation with similar semantics.

## Contrasts With
- None directly.

# Common Errors

- **Error**: Hibernating after every event.
  **Correction**: "It is rather costly to hibernate a process...It is not something you want to do after every event." Only hibernate in states where the server is expected to idle.

- **Error**: Hibernating a process that does not accumulate significant heap garbage.
  **Correction**: "To gain anything from hibernation, your server would have to produce non-insignificant garbage during callback execution." If the server's heap is already small, hibernation adds cost without benefit.

# Common Confusions

- **Confusion**: Hibernation stops the process.
  **Clarification**: Hibernation only garbage collects the heap and reduces memory. The process remains alive and will automatically resume normal execution when the next message/event arrives.

- **Confusion**: The server must be manually woken from hibernation.
  **Clarification**: The gen_statem engine handles waking automatically. Any incoming event (including timeouts) will cause the process to resume.

# Source Reference

Described in the "Hibernation" section of the gen_statem Behaviour chapter, near the end of the document.

# Verification Notes

- Definition source: Directly from the "Hibernation" section of statem.md.
- Confidence rationale: High -- explicitly defined with clear guidelines on when to use and when to avoid.
- Uncertainties: None.
- Cross-reference status: References gen-statem, transition-actions, event-timeout, gen-server.
