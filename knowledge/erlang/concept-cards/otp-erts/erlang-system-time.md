---
concept: Erlang System Time
slug: erlang-system-time
category: performance
subcategory: time-management
tier: intermediate
source: "ERTS User's Guide"
source_slug: otp-erts
authors: "Ericsson AB"
chapter: "Time and Time Correction in Erlang"
chapter_number: null
pdf_page: null
section: "Erlang System Time"
extraction_confidence: high
aliases:
  - "system time"
  - "erlang:system_time/0"
prerequisites:
  - erlang-monotonic-time
  - time-offset
extends: []
related:
  - os-system-time
  - time-correction
  - time-warp
  - time-warp-modes
contrasts_with:
  - erlang-monotonic-time
  - os-system-time
answers_questions:
  - "What is Erlang system time?"
  - "How does Erlang system time relate to Erlang monotonic time?"
  - "How does OS system time relate to Erlang system time?"
---

# Quick Definition

Erlang system time is the Erlang runtime system's view of POSIX time. It is computed as Erlang monotonic time plus the current time offset, and the runtime works towards aligning it with OS system time -- possibly through time warps, depending on the time warp mode.

# Core Definition

The ERTS User's Guide defines Erlang system time as "the Erlang runtime systems view of POSIX time," retrieved via `erlang:system_time/0`. The guide states: "This time may or may not be an accurate view of POSIX time, and may or may not align with OS system time. The runtime system works towards aligning the two system times. Depending on the time warp mode used, this can be achieved by letting Erlang system time perform a time warp." (Time and Time Correction, "Erlang System Time" section).

The fundamental relationship, stated in the "Erlang Monotonic Time" section, is: current Erlang system time = current Erlang monotonic time + current time offset.

# Prerequisites

- **erlang-monotonic-time** -- Erlang system time is derived from Erlang monotonic time
- **time-offset** -- The additive component that transforms monotonic time into system time

# Key Properties

1. Represents the runtime system's view of POSIX time
2. Retrieved via `erlang:system_time/0` (native unit) or `erlang:system_time/1` (specified unit)
3. Computed as: Erlang monotonic time + time offset
4. May or may not accurately reflect actual POSIX time
5. May or may not align with OS system time at any given moment
6. The runtime works to align Erlang system time with OS system time
7. Alignment may involve time warps depending on the time warp mode
8. Should not be used for measuring elapsed time -- use Erlang monotonic time instead

# Construction / Recognition

## To Construct/Create:

1. Call `erlang:system_time/0` for the current value in native time unit
2. Call `erlang:system_time/1` with a time unit (e.g., `second`, `millisecond`)
3. Use `erlang:timestamp/0` for a format compatible with the old `erlang:now/0` return value
4. Equivalently, add `erlang:monotonic_time/0` and `erlang:time_offset/0`

## To Identify/Recognize:

1. Any time value intended to represent wall-clock / calendar time is Erlang system time
2. Values correspond to POSIX time (seconds since epoch, conceptually)
3. Unlike monotonic time, system time can warp (jump forward or backward)

# Context & Application

Erlang system time replaces the time-related use of `erlang:now/0`. The source explains the design decision: "The adjustment of system time could have been made smoother than using a time warp approach, but we think that would be a bad choice. As we can express and measure time that is not connected to calendar time by the use of Erlang monotonic time, it is better to expose the change in Erlang system time immediately. This as the Erlang applications executing on the system can react on the change in system time as soon as possible."

To detect changes in Erlang system time, you can monitor the time offset: `erlang:monitor(time_offset, clock_service)`. When the time offset changes, a message of the form `{'CHANGE', MonitorReference, time_offset, clock_service, NewTimeOffset}` is sent to the monitoring process.

# Examples

**Retrieving Erlang system time** (Time and Time Correction, "How to Work with the New API" section):

```erlang
%% Do - use erlang:system_time/1 to get current system time
SystemTimeSecs = erlang:system_time(second).

%% Do - use erlang:timestamp/0 for erlang:now/0-compatible format
{MegaSecs, Secs, MicroSecs} = erlang:timestamp().
```

**Don't** (same section): "Use `erlang:now/0` to retrieve the current Erlang system time."

**Monitoring for system time changes** (Time and Time Correction, "New Erlang Monotonic Time" section):

```erlang
%% Monitor the time offset to detect system time warps
MonRef = erlang:monitor(time_offset, clock_service).
%% When the offset changes, this message arrives:
%% {'CHANGE', MonRef, time_offset, clock_service, NewTimeOffset}
```

**Computing system time from components** (Time and Time Correction, "Erlang Monotonic Time" section):

```erlang
%% Erlang system time = Erlang monotonic time + time offset
MonoTime = erlang:monotonic_time(),
Offset = erlang:time_offset(),
SystemTime = MonoTime + Offset.
```

# Relationships

## Builds Upon

- **erlang-monotonic-time** -- System time is derived by adding monotonic time and time offset
- **time-offset** -- The bridge between monotonic time and system time

## Related

- **os-system-time** -- The OS-level view of POSIX time that Erlang system time works toward aligning with
- **time-correction** -- The mechanism that adjusts frequency and offset to align system times
- **time-warp** -- System time alignment may involve warps
- **time-warp-modes** -- Different modes control how alignment (and thus warps) occur

## Contrasts With

- **erlang-monotonic-time** -- Monotonic time never warps and has a local time scale; system time tracks POSIX time and can warp
- **os-system-time** -- OS system time is the OS's view of POSIX time; Erlang system time is the runtime's managed view, which may diverge

# Common Errors

- **Error**: Using `erlang:now/0` to get current system time
  **Correction**: Use `erlang:system_time/1` or `erlang:timestamp/0`. The source states emphatically: "Do not use `erlang:now/0`."

- **Error**: Using Erlang system time to measure elapsed time
  **Correction**: Use `erlang:monotonic_time/0` for elapsed time measurements. System time can warp, making elapsed-time calculations unreliable.

# Common Confusions

- **Confusion**: Assuming Erlang system time always equals OS system time
  **Clarification**: The source explicitly states it "may or may not align with OS system time." The runtime works toward alignment, but depending on the time warp mode, there may be periods of divergence.

- **Confusion**: Thinking system time changes are always smooth
  **Clarification**: The ERTS guide deliberately chose a time warp approach over smooth adjustment: "it is better to expose the change in Erlang system time immediately" so applications can react promptly.

# Source Reference

"Time and Time Correction in Erlang" chapter, sections "Erlang System Time," "New Erlang Monotonic Time," and "How to Work with the New API." The terminology section defines the concept; the new API section provides usage guidance.

# Verification Notes

- Definition: Direct quote from source ("the Erlang runtime systems view of POSIX time")
- Relationship formula: Explicit in source ("By adding current Erlang monotonic time with current time offset, you get current Erlang system time")
- Monitor message format: Verbatim from source
- Design rationale for warps over smooth adjustment: Paraphrased from source
- Confidence: HIGH -- explicitly defined with clear usage guidance in the ERTS User's Guide
