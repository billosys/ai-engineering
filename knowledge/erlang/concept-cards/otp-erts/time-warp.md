---
concept: Time Warp
slug: time-warp
category: performance
subcategory: time-management
tier: intermediate
source: "ERTS User's Guide"
source_slug: otp-erts
authors: "Ericsson AB"
chapter: "Time and Time Correction in Erlang"
chapter_number: null
pdf_page: null
section: "Time Warp"
extraction_confidence: high
aliases:
  - "time leap"
prerequisites: []
extends: []
related:
  - erlang-system-time
  - time-warp-modes
  - time-correction
  - erlang-monotonic-time
contrasts_with: []
answers_questions:
  - "What is a time warp in ERTS?"
  - "What must I know before using time warp modes?"
---

# Quick Definition

A time warp is a leap forwards or backwards in time where the difference between time values taken before and after the warp does not correspond to the actual elapsed time. In Erlang, time warps affect Erlang system time (which tracks wall-clock time) but never affect Erlang monotonic time (which is guaranteed to increase monotonically).

# Core Definition

The ERTS User's Guide defines a time warp precisely: "A time warp is a leap forwards or backwards in time. That is, the difference of time values taken before and after the time warp does not correspond to the actual elapsed time." (Time and Time Correction, "Time Warp" terminology section).

Time warps occur in Erlang system time when the time offset is adjusted to align Erlang system time with OS system time. Whether and how such warps can occur depends on the time warp mode in use. Code that can correctly handle time warps of Erlang system time is called "time warp safe."

# Prerequisites

None -- this is a terminology definition that other time concepts build upon.

# Key Properties

1. A time warp is a discontinuity in time values -- a jump forward or backward
2. After a warp, the difference between pre-warp and post-warp values does not reflect actual elapsed time
3. Time warps affect Erlang system time, not Erlang monotonic time
4. Time warps occur when the time offset changes
5. The time warp mode determines whether and when warps are permitted
6. Code must be "time warp safe" to run correctly in modes that allow warps
7. `erlang:now/0` is explicitly time warp unsafe -- it freezes when system time warps backwards

# Construction / Recognition

## To Identify/Recognize:

1. A time warp has occurred if successive `erlang:system_time/0` calls show a backwards jump
2. Monitor the time offset with `erlang:monitor(time_offset, clock_service)` to be notified of offset changes that cause warps
3. The time warp mode determines if warps are possible: no-time-warp mode prevents them (at the cost of monotonic clock accuracy)

## To Handle:

1. Use `erlang:monotonic_time/0` for elapsed time measurements -- it is immune to warps
2. Monitor time offset changes to react to system time warps
3. Avoid `erlang:now/0` -- it behaves badly on backwards warps (freezes for potentially years)

# Context & Application

The concept of time warps is central to understanding the ERTS time system redesign in OTP 18. The ERTS guide explains why time warps were chosen over smooth adjustment: "The adjustment of system time could have been made smoother than using a time warp approach, but we think that would be a bad choice. As we can express and measure time that is not connected to calendar time by the use of Erlang monotonic time, it is better to expose the change in Erlang system time immediately."

The dangers of time warp unsafe code are illustrated by `erlang:now/0`: "When Erlang system time does a time warp backwards, the values returned from `erlang:now/0` freeze (if you disregard the microsecond increments made because of the actual call) until OS system time reaches the point of the last value returned by `erlang:now/0`. This freeze can continue for a long time. It can take years, decades, and even longer until the freeze stops." This is why `erlang:now/0` is strongly discouraged.

# Examples

**Time warp unsafe code** (Time and Time Correction, "Time Warp Safe Code" section):

```erlang
%% Bad - erlang:now/0 freezes on backward time warps
%% The values freeze "for years, decades, and even longer"
Before = erlang:now(),
%% ... if a backward time warp occurs here ...
After = erlang:now().
%% timer:now_diff(After, Before) gives meaningless results
```

**Time warp safe code** (Time and Time Correction, "How to Work with the New API" section):

```erlang
%% Good - monotonic time is immune to time warps
T1 = erlang:monotonic_time(),
%% ... operation (even if system time warps) ...
T2 = erlang:monotonic_time(),
Elapsed = T2 - T1.  %% Always correct elapsed time
```

**Detecting time warps** (Time and Time Correction, "New Erlang Monotonic Time" section):

```erlang
%% Monitor for time offset changes (which cause system time warps)
MonRef = erlang:monitor(time_offset, clock_service),
receive
    {'CHANGE', MonRef, time_offset, clock_service, NewOffset} ->
        %% A time warp just occurred in Erlang system time
        handle_time_warp(NewOffset)
end.
```

# Relationships

## Enables

- **time-warp-modes** -- The three modes control when and how time warps are permitted
- **time-correction** -- Time correction and time warps work together to align system times

## Related

- **erlang-system-time** -- Time warps affect Erlang system time
- **erlang-monotonic-time** -- Monotonic time is immune to time warps
- **time-offset** -- Time warps occur when the time offset changes

# Common Errors

- **Error**: Using `erlang:now/0` in code that may experience time warps
  **Correction**: The source warns that `erlang:now/0` can freeze for "years, decades, and even longer" on backward warps. Use the new time API instead.

- **Error**: Computing elapsed time from `erlang:system_time/0` differences
  **Correction**: System time can warp, making elapsed-time calculations unreliable. Use `erlang:monotonic_time/0`.

# Common Confusions

- **Confusion**: Thinking time warps affect Erlang monotonic time
  **Clarification**: Time warps only affect Erlang system time (via time offset changes). Erlang monotonic time is guaranteed to be monotonically increasing and never warps.

- **Confusion**: Believing time warps are bugs or errors
  **Clarification**: Time warps are a deliberate design choice. The ERTS guide chose them over smooth adjustment because exposing system time changes immediately lets applications react promptly.

# Source Reference

"Time and Time Correction in Erlang" chapter, terminology section "Time Warp" and section "Time Warp Safe Code." Additional context from "New Erlang Monotonic Time" and "How to Work with the New API."

# Verification Notes

- Definition: Direct quote from source ("A time warp is a leap forwards or backwards in time...")
- erlang:now/0 freeze behavior: Direct quote from source ("years, decades, and even longer")
- Design rationale: Paraphrased from source
- Confidence: HIGH -- explicitly defined in terminology section with detailed behavioral description
