---
concept: OS System Time and OS Monotonic Time
slug: os-system-time-and-os-monotonic-time
category: performance
subcategory: time-management
tier: intermediate
source: "ERTS User's Guide"
source_slug: otp-erts
authors: "Ericsson AB"
chapter: "Time and Time Correction in Erlang"
chapter_number: null
pdf_page: null
section: "OS System Time / OS Monotonic Time"
extraction_confidence: high
aliases:
  - os-system-time
  - os-monotonic-time
  - "os:system_time/0"
  - "operating system time"
prerequisites: []
extends: []
related:
  - erlang-monotonic-time
  - erlang-system-time
  - time-correction
contrasts_with: []
answers_questions:
  - "What is OS system time in Erlang?"
  - "What is OS monotonic time in Erlang?"
  - "How does OS system time relate to Erlang system time?"
---

# Quick Definition

OS system time is the operating system's view of POSIX time, which may be adjusted forwards or backwards without limitation. OS monotonic time is a monotonically increasing time provided by the OS that does not leap and has relatively steady frequency but may stop during system suspension. These two OS-level time sources are what the Erlang runtime uses to construct its own managed time values.

# Core Definition

The ERTS User's Guide defines OS system time as "the operating systems view of POSIX time," retrieved via `os:system_time/0`. The guide notes: "This may or may not be an accurate view of POSIX time. This time may typically be adjusted both backwards and forwards without limitation. That is, time warps may be observed." (Time and Time Correction, "OS System Time" section).

OS monotonic time is defined as "a monotonically increasing time provided by the OS. This time does not leap and has a relatively steady frequency although not completely correct. However, it is not uncommon that OS monotonic time stops if the system is suspended. This time typically increases since some unspecified point in time that is not connected to OS system time. This type of time is not necessarily provided by all OSs." (Time and Time Correction, "OS Monotonic Time" section).

# Prerequisites

None -- these are the lowest-level time sources, provided by the operating system.

# Key Properties

## OS System Time

1. Retrieved via `os:system_time/0` or `os:system_time/1`
2. Represents the OS's view of POSIX time
3. May not be accurate
4. Can be adjusted both backwards and forwards without limitation (time warps can occur)
5. Inspect the source with `erlang:system_info(os_system_time_source)`

## OS Monotonic Time

1. Monotonically increasing -- does not leap
2. Has relatively steady frequency, but not perfectly correct (has drift)
3. May stop if the system is suspended
4. Starts from an unspecified point not connected to OS system time
5. Not necessarily available on all operating systems
6. Inspect the source with `erlang:system_info(os_monotonic_time_source)`
7. Essential for time correction to function

# Construction / Recognition

## To Construct/Create:

1. Call `os:system_time/0` or `os:system_time/1` for OS system time
2. OS monotonic time is not directly exposed as an Erlang API; it is used internally by the runtime
3. Call `erlang:system_info(os_monotonic_time_source)` to inspect the OS monotonic time source
4. Call `erlang:system_info(os_system_time_source)` to inspect the OS system time source

## To Identify/Recognize:

1. OS system time is wall-clock time from the OS perspective
2. OS monotonic time is a low-level monotonic clock -- its availability and behavior vary by platform
3. If `erlang:system_info(os_monotonic_time_source)` returns information, OS monotonic time is available

# Context & Application

The Erlang runtime system uses both OS time sources together to provide its own managed time values. The source explains: "If time correction is enabled, the Erlang runtime system makes use of both OS system time and OS monotonic time, to adjust the frequency of the Erlang monotonic clock."

The availability of OS monotonic time is critical: time correction requires it. Without it, Erlang monotonic time can only guarantee monotonicity but not frequency accuracy. The source states: "By default time correction is enabled if support for it exists on the specific platform. Support for it includes both OS monotonic time, provided by the OS, and an implementation in the Erlang runtime system using OS monotonic time."

The introduction section provides context for why these OS-level sources are insufficient on their own: "A 'normal' modern computer cannot keep time, not on itself and not unless you have a chip-level atomic clock wired to it. Time, as perceived by your computer, must normally be corrected. Hence the Network Time Protocol (NTP) protocol, together with the `ntpd` process, does its best to keep your computer time in sync with the correct time."

# Examples

**Querying OS system time** (Time and Time Correction, "OS System Time" section):

```erlang
%% Retrieve current OS system time
OsSysTime = os:system_time().

%% Retrieve in a specific unit
OsSysTimeSecs = os:system_time(second).
```

**Inspecting time sources** (Time and Time Correction, "Time Correction" section):

```erlang
%% Check if OS monotonic time is available and its source
erlang:system_info(os_monotonic_time_source).

%% Check the OS system time source
erlang:system_info(os_system_time_source).

%% Check if time correction is enabled
erlang:system_info(time_correction).
```

# Relationships

## Enables

- **erlang-monotonic-time** -- Erlang monotonic time's accuracy depends on OS monotonic time
- **erlang-system-time** -- Erlang system time aims to align with OS system time
- **time-correction** -- Time correction uses both OS time sources to adjust the Erlang monotonic clock

## Related

- **time-correction** -- The mechanism that combines both OS time sources to produce reliable Erlang times

# Common Errors

- **Error**: Assuming OS system time is always accurate or monotonic
  **Correction**: The source states it "may or may not be an accurate view of POSIX time" and can warp in both directions

- **Error**: Assuming OS monotonic time is available on all platforms
  **Correction**: The source states "this type of time is not necessarily provided by all OSs." Check with `erlang:system_info(os_monotonic_time_source)`.

# Common Confusions

- **Confusion**: Conflating OS system time with Erlang system time
  **Clarification**: OS system time (`os:system_time/0`) is the raw OS value. Erlang system time (`erlang:system_time/0`) is the runtime's managed view, which may diverge from OS system time depending on the time warp mode.

- **Confusion**: Assuming OS monotonic time never stops
  **Clarification**: The source notes "it is not uncommon that OS monotonic time stops if the system is suspended"

# Source Reference

"Time and Time Correction in Erlang" chapter, terminology sections "OS System Time" and "OS Monotonic Time," plus the "Time Correction" and "Introduction" sections.

# Verification Notes

- OS system time definition: Direct quote from source
- OS monotonic time definition: Direct quote from source
- Suspension behavior: Explicit in source ("not uncommon that OS monotonic time stops if the system is suspended")
- Platform availability caveat: Explicit in source
- Confidence: HIGH -- terminology sections provide explicit definitions
