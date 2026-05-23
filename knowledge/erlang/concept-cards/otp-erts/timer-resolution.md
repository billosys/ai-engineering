---
concept: Timer Resolution
slug: timer-resolution
category: performance
subcategory: time-management
tier: intermediate
source: "ERTS User's Guide"
source_slug: otp-erts
authors: "Ericsson AB"
chapter: "Time and Time Correction in Erlang"
chapter_number: null
pdf_page: null
section: "Timers"
extraction_confidence: high
aliases:
  - "timer precision"
  - "timer accuracy"
  - "ERTS timers"
prerequisites:
  - erlang-monotonic-time
extends: []
related:
  - erlang-system-time
  - time-warp-modes
  - time-correction
contrasts_with: []
answers_questions:
  - "What is the resolution of timers in Erlang?"
  - "When exactly does a timer fire in Erlang?"
---

# Quick Definition

All Erlang timers -- `receive ... after`, BIF timers, and `timer` module timers -- are triggered relative to Erlang monotonic time with millisecond resolution. A timer with timeout T will typically trigger in the range [T, T+1) milliseconds under normal load, and never before T.

# Core Definition

The ERTS User's Guide states: "All timers are triggered relative Erlang monotonic time. All timers currently have millisecond resolution both in the API and internally in the runtime system. That is, resolution (as well as precision and accuracy) will not be higher than millisecond." The guide adds: "If Erlang monotonic time has a lower resolution than millisecond, the timer resolution will be lower than millisecond as well." (Time and Time Correction, "Timers" section).

The guide distinguishes three related but different time quality metrics: resolution is "the shortest time interval that can be distinguished when reading time values," precision is "the shortest time interval that can be distinguished repeatedly and reliably," and accuracy is "the correctness of time values."

# Prerequisites

- **erlang-monotonic-time** -- All timers trigger relative to Erlang monotonic time

# Key Properties

1. All timers trigger relative to Erlang monotonic time (not system time, not wall-clock time)
2. Millisecond resolution in both the API and internally
3. Resolution, precision, and accuracy are all bounded at millisecond (at most)
4. If Erlang monotonic time has lower resolution than millisecond, timer resolution is correspondingly lower
5. Timers can only trigger on whole milliseconds since runtime system start
6. A timer is never allowed to trigger before the user-specified timeout time T
7. Under normal load, a timer triggers in the range [T, T+1) milliseconds
8. Under heavy load, triggering may be delayed beyond T+1
9. Applies uniformly to `receive ... after`, BIF timers (`erlang:send_after/3`, `erlang:start_timer/3`), and `timer` module timers

# Construction / Recognition

## To Identify/Recognize:

1. Any `receive ... after Timeout` uses this timer mechanism
2. Any call to `erlang:send_after/3` or `erlang:start_timer/3` uses it
3. Any `timer` module function that involves time delay uses it
4. All share the same resolution and triggering semantics

## Key Distinctions:

1. **Resolution** -- the shortest distinguishable interval (hardware/OS limited)
2. **Precision** -- the shortest interval distinguishable repeatedly and reliably (limited by resolution but can be worse)
3. **Accuracy** -- correctness of the time value itself

# Context & Application

Understanding timer resolution is important for soft real-time applications. The guarantee that timers never fire early (before T) but may fire slightly late (typically within T+1) is a key property for reasoning about timing in concurrent systems. Under heavy system load, timer triggering may be further delayed.

Since all timers are relative to Erlang monotonic time rather than system time, they are unaffected by time warps in system time. A `receive ... after 5000` will wait approximately 5 seconds of elapsed time regardless of any system time adjustments that occur during the wait.

# Examples

**Timer triggering semantics** (Time and Time Correction, "Timers" section):

```erlang
%% A timer with timeout T=100ms:
%% - Will NOT trigger before 100ms have elapsed (monotonic time)
%% - Under normal load, triggers in [100, 101) ms
%% - Under heavy load, may trigger later than 101ms

receive
    Msg -> handle(Msg)
after 100 ->
    timeout_action()
end.
```

**Timers are immune to system time warps** (derived from source properties):

```erlang
%% Even if a system time warp occurs during the wait,
%% this timer still fires after ~5000ms of elapsed (monotonic) time
erlang:send_after(5000, self(), timeout_msg).
```

# Relationships

## Builds Upon

- **erlang-monotonic-time** -- Timers trigger relative to monotonic time, inheriting its resolution properties

## Related

- **erlang-system-time** -- Timers are independent of system time; system time warps do not affect them
- **time-warp-modes** -- Mode affects monotonic time accuracy, which indirectly affects timer accuracy
- **time-correction** -- Time correction improves monotonic time frequency accuracy, benefiting timers

# Common Errors

- **Error**: Expecting sub-millisecond timer precision
  **Correction**: Timer resolution is millisecond at best. For sub-millisecond needs, use busy-waiting or other OS-level mechanisms.

- **Error**: Expecting a timer to fire at exactly T milliseconds
  **Correction**: The guarantee is [T, T+1) under normal load; it can be later under heavy load. Timers never fire before T.

# Common Confusions

- **Confusion**: Thinking system time warps affect timer behavior
  **Clarification**: Timers are triggered relative to Erlang monotonic time, which never warps. System time changes do not cause timers to fire early or late.

- **Confusion**: Conflating resolution, precision, and accuracy
  **Clarification**: The source defines these as three distinct concepts. Resolution is the shortest distinguishable interval. Precision is reliable repeatability. Accuracy is correctness. Precision is limited by resolution, but they can differ significantly.

# Source Reference

"Time and Time Correction in Erlang" chapter, "Timers" section and terminology definitions for "Time Resolution," "Time Precision," and "Time Accuracy."

# Verification Notes

- Millisecond resolution: Direct from source ("All timers currently have millisecond resolution both in the API and internally")
- [T, T+1) range: Direct from source ("a timer will typically be triggered in the range [T, T+1) milliseconds")
- Never fires before T: Direct from source ("A timer is not allowed to trigger before the timeout time given by the user")
- Resolution/precision/accuracy definitions: Direct quotes from source terminology sections
- Confidence: HIGH -- explicit statements about timer behavior in the ERTS User's Guide
