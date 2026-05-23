---
concept: Erlang Monotonic Time
slug: erlang-monotonic-time
category: performance
subcategory: time-management
tier: intermediate
source: "ERTS User's Guide"
source_slug: otp-erts
authors: "Ericsson AB"
chapter: "Time and Time Correction in Erlang"
chapter_number: null
pdf_page: null
section: "Erlang Monotonic Time"
extraction_confidence: high
aliases:
  - "monotonic time"
  - "erlang:monotonic_time/0"
prerequisites:
  - os-monotonic-time
  - os-system-time
extends: []
related:
  - erlang-system-time
  - time-offset
  - time-correction
  - time-warp-modes
  - timer-resolution
contrasts_with:
  - erlang-system-time
answers_questions:
  - "What is Erlang monotonic time?"
  - "How does Erlang monotonic time relate to Erlang system time?"
  - "What distinguishes monotonic time from system time?"
  - "How should I measure elapsed time in Erlang?"
---

# Quick Definition

Erlang monotonic time is a monotonically increasing time provided by the Erlang runtime system, starting from an unspecified point. It is the internal "time engine" used for all timers and time-related operations, and when added to the current time offset, yields Erlang system time.

# Core Definition

The ERTS User's Guide defines Erlang monotonic time as "a monotonically increasing time provided by the Erlang runtime system" that "increases since some unspecified point in time." It is retrieved via `erlang:monotonic_time/0`. The guide further states: "Internally in the runtime system, Erlang monotonic time is the 'time engine' that is used for more or less everything that has anything to do with time. All timers, regardless of it is a `receive ... after` timer, BIF timer, or a timer in the `timer` module, are triggered relative Erlang monotonic time." (Time and Time Correction, "Erlang Monotonic Time" section).

The fundamental relationship is: Erlang system time = Erlang monotonic time + time offset.

# Prerequisites

- **os-monotonic-time** -- Erlang monotonic time's accuracy depends on the underlying OS monotonic time source
- **os-system-time** -- Used alongside OS monotonic time for frequency adjustments

# Key Properties

1. Guaranteed to be monotonically increasing (never goes backwards)
2. Starts from an unspecified point in time (not connected to any calendar epoch)
3. Retrieved via `erlang:monotonic_time/0` (native time unit) or `erlang:monotonic_time/1` (specified unit)
4. Serves as the internal time engine for all timers and time operations in the runtime
5. When added to the current time offset, yields Erlang system time
6. Accuracy and precision depend on: OS monotonic time, OS system time, and the time warp mode used
7. On systems without OS monotonic time, monotonicity is still guaranteed but no other guarantees hold
8. Frequency adjustments depend on the time warp mode in use
9. May return negative values on a newly started runtime system (this is a memory optimization, not a bug)

# Construction / Recognition

## To Construct/Create:

1. Call `erlang:monotonic_time/0` to get the current value in native time unit
2. Call `erlang:monotonic_time/1` with a desired time unit (e.g., `millisecond`, `microsecond`)
3. Use `erlang:convert_time_unit/3` to convert between time units

## To Identify/Recognize:

1. Any time value used for measuring elapsed time should be Erlang monotonic time
2. Timer triggers are relative to Erlang monotonic time
3. Values from `erlang:monotonic_time/0` are in native time unit and may be negative

# Context & Application

Erlang monotonic time was introduced in ERTS 7.0 (OTP 18) specifically to detach time measurements (elapsed time) from calendar time. The source explains: "It is introduced to detach time measurements, such as elapsed time from calendar time. In many use cases there is a need to measure elapsed time or specify a time relative to another point in time without the need to know the involved times in UTC or any other globally defined time scale."

This separation allows the two Erlang times (monotonic and system) to be adjusted independently, so that "the accuracy of elapsed time does not have to suffer just because the system time happened to be wrong at some point in time." Full separation of adjustments occurs only in multi-time warp mode; other modes tie monotonic time adjustments to system time for backward compatibility.

# Examples

**Measuring elapsed time** (Time and Time Correction, "How to Work with the New API" section):

```erlang
%% Do - take timestamps with erlang:monotonic_time/0 and subtract
T1 = erlang:monotonic_time(),
%% ... operation ...
T2 = erlang:monotonic_time(),
ElapsedNative = T2 - T1,
ElapsedMs = erlang:convert_time_unit(ElapsedNative, native, millisecond).
```

**Determining order of events with time** (same section):

```erlang
%% Do - use monotonic time + unique integer for ordered event tags
Time = erlang:monotonic_time(),
UMI = erlang:unique_integer([monotonic]),
EventTag = {Time, UMI}.
%% These tuples are strictly monotonically ordered by creation time.
%% Monotonic time in the first element ensures correct tuple comparison.
```

**Don't** -- use `erlang:now/0` to measure elapsed time (same section): "Take time stamps with `erlang:now/0` and calculate the difference in time with `timer:now_diff/2`."

# Relationships

## Builds Upon

- **os-monotonic-time** -- Erlang monotonic time derives its accuracy from the OS monotonic time source
- **os-system-time** -- Used for frequency corrections

## Enables

- **erlang-system-time** -- Erlang system time is computed from monotonic time plus time offset
- **timer-resolution** -- All timers are triggered relative to Erlang monotonic time

## Related

- **time-offset** -- The additive bridge between monotonic time and system time
- **time-correction** -- The mechanism that adjusts monotonic time frequency
- **time-warp-modes** -- Different modes adjust monotonic time differently

## Contrasts With

- **erlang-system-time** -- System time tracks wall-clock (POSIX) time and can warp; monotonic time never warps and has a local (non-calendar) time scale

# Common Errors

- **Error**: Using `erlang:now/0` to measure elapsed time
  **Correction**: Use `erlang:monotonic_time/0` for elapsed time measurements. The source states: "Do not use `erlang:now/0`."

- **Error**: Assuming monotonic time values correspond to a specific wall-clock time
  **Correction**: Monotonic time uses a locally defined start point and has no connection to UTC or POSIX time. Add the time offset to get system time if needed.

# Common Confusions

- **Confusion**: Believing negative values from `erlang:monotonic_time/0` indicate a bug
  **Clarification**: The source notes: "Some of the new BIFs on some systems, perhaps surprisingly, return negative integer values on a newly started runtime system. This is not a bug, but a memory use optimization."

- **Confusion**: Thinking monotonic time has the same accuracy in all time warp modes
  **Clarification**: Accuracy is best in multi-time warp mode because monotonic time frequency is adjusted independently of system time alignment. In no-time-warp mode, frequency errors up to 1% can occur.

# Source Reference

"Time and Time Correction in Erlang" chapter, sections "Erlang Monotonic Time," "New Erlang Monotonic Time," and "How to Work with the New API." The terminology definitions and the new API section provide the core material.

# Verification Notes

- Definition: Direct quote from source ("a monotonically increasing time provided by the Erlang runtime system")
- Time engine quote: Direct from source
- Relationship formula (system time = monotonic time + offset): Explicit in source
- Negative values note: Direct from source
- Confidence: HIGH -- extensively defined with multiple explicit statements in the ERTS User's Guide
