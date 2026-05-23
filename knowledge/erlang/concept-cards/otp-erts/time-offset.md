---
concept: Time Offset
slug: time-offset
category: performance
subcategory: time-management
tier: intermediate
source: "ERTS User's Guide"
source_slug: otp-erts
authors: "Ericsson AB"
chapter: "Time and Time Correction in Erlang"
chapter_number: null
pdf_page: null
section: "Time Warp Modes"
extraction_confidence: high
aliases:
  - "erlang:time_offset/0"
  - "clock offset"
prerequisites:
  - erlang-monotonic-time
extends: []
related:
  - erlang-system-time
  - time-warp
  - time-warp-modes
  - time-correction
contrasts_with: []
answers_questions:
  - "How does Erlang monotonic time relate to Erlang system time?"
  - "What is the time offset in Erlang?"
---

# Quick Definition

The time offset is the value that, when added to Erlang monotonic time, yields Erlang system time. It is managed differently depending on the time warp mode: fixed at startup in no-time-warp mode, finalized once in single-time-warp mode, or freely adjustable at any time in multi-time-warp mode.

# Core Definition

The ERTS User's Guide states: "Current Erlang system time is determined by adding the current Erlang monotonic time with current time offset. The time offset is managed differently depending on which time warp mode you use." (Time and Time Correction, "Time Warp Modes" section). The time offset is retrieved via `erlang:time_offset/0` or `erlang:time_offset/1`.

The time offset is the bridge between the two Erlang time scales: monotonic time (which has a locally defined start and never warps) and system time (which tracks POSIX/wall-clock time). Changes to the time offset cause time warps in Erlang system time.

# Prerequisites

- **erlang-monotonic-time** -- The time offset is added to monotonic time to produce system time

# Key Properties

1. Erlang system time = Erlang monotonic time + time offset
2. Retrieved via `erlang:time_offset/0` (native unit) or `erlang:time_offset/1` (specified unit)
3. Changes to the time offset cause time warps in Erlang system time
4. The time offset can be monitored: `erlang:monitor(time_offset, clock_service)`
5. Management of the time offset depends on the time warp mode:
   - **No-time-warp mode**: Fixed at startup, never changes
   - **Single-time-warp mode**: Fixed during preliminary phase, adjusted once during finalization, then fixed forever
   - **Multi-time-warp mode**: Can change at any time without limitations
6. In single-time-warp mode, finalization is triggered by `erlang:system_flag(time_offset, finalize)`

# Construction / Recognition

## To Construct/Create:

1. The time offset is managed automatically by the runtime system
2. In single-time-warp mode, call `erlang:system_flag(time_offset, finalize)` to trigger finalization

## To Query:

1. Call `erlang:time_offset/0` for the current value in native time unit
2. Call `erlang:time_offset/1` with a desired time unit
3. Monitor with `erlang:monitor(time_offset, clock_service)` to be notified of changes

## To Identify/Recognize:

1. The time offset is the difference between Erlang system time and Erlang monotonic time
2. A change in the time offset means a time warp has occurred in Erlang system time

# Context & Application

The time offset is central to understanding how Erlang separates elapsed-time measurement from wall-clock tracking. The source explains that this separation was introduced in OTP 18 to allow "the two Erlang times (Erlang monotonic time and Erlang system time)" to be "adjusted separately," so that "the accuracy of elapsed time does not have to suffer just because the system time happened to be wrong at some point in time."

When recording events with both order and wall-clock context, the source recommends saving the time offset alongside monotonic time: "If you are executing in a mode where time offset can change, and you want to get the actual Erlang system time when the event occurred, you can save the time offset as a third element in the tuple."

# Examples

**Retrieving and using the time offset** (Time and Time Correction, "Erlang Monotonic Time" section):

```erlang
%% Erlang system time = Erlang monotonic time + time offset
MonoTime = erlang:monotonic_time(),
Offset = erlang:time_offset(),
SystemTime = MonoTime + Offset.
```

**Saving time offset with events** (Time and Time Correction, "How to Work with the New API" section):

```erlang
%% Save time offset as third element for wall-clock reconstruction
Time = erlang:monotonic_time(),
UMI = erlang:unique_integer([monotonic]),
Offset = erlang:time_offset(),
EventTag = {Time, UMI, Offset}.
%% Later: Time + Offset gives the Erlang system time at event creation
```

**Monitoring offset changes** (Time and Time Correction, "New Erlang Monotonic Time" section):

```erlang
MonRef = erlang:monitor(time_offset, clock_service),
receive
    {'CHANGE', MonRef, time_offset, clock_service, NewTimeOffset} ->
        io:format("Time offset changed to: ~p~n", [NewTimeOffset])
end.
```

**Finalizing in single-time-warp mode** (Time and Time Correction, "Single Time Warp Mode" section):

```erlang
%% After OS system time is confirmed correct, finalize the offset
erlang:system_flag(time_offset, finalize).
%% This can only be done once; triggers a single time warp
```

# Relationships

## Builds Upon

- **erlang-monotonic-time** -- The time offset is added to monotonic time to yield system time

## Enables

- **erlang-system-time** -- System time is computed from monotonic time plus time offset

## Related

- **time-warp** -- Changes in time offset cause time warps in system time
- **time-warp-modes** -- The three modes manage the time offset differently
- **time-correction** -- Time correction adjusts monotonic time frequency and (in some modes) the time offset

# Common Errors

- **Error**: Ignoring the time offset when reconstructing wall-clock time from monotonic time stamps
  **Correction**: Always add the time offset to monotonic time to get system time. In multi-time-warp mode, the offset can change, so save it alongside event timestamps if wall-clock precision matters.

# Common Confusions

- **Confusion**: Thinking the time offset is constant
  **Clarification**: Only in no-time-warp mode is the offset truly fixed. In multi-time-warp mode, it can change at any time. In single-time-warp mode, it changes exactly once during finalization.

- **Confusion**: Believing changes to the time offset affect Erlang monotonic time
  **Clarification**: The time offset only affects Erlang system time (monotonic time + offset). Monotonic time itself is independent of the offset.

# Source Reference

"Time and Time Correction in Erlang" chapter, "Time Warp Modes" section (where time offset management per mode is described), "Erlang Monotonic Time" section (where the relationship formula is given), and "How to Work with the New API" section (for usage patterns).

# Verification Notes

- Relationship formula: Direct from source ("adding the current Erlang monotonic time with current time offset")
- Per-mode behavior: Summarized from the detailed mode descriptions in source
- Event tagging with offset: Paraphrased from source
- Finalization BIF: Explicit in source
- Confidence: HIGH -- the relationship is stated explicitly and behavior per mode is clearly described
