---
concept: Time Correction
slug: time-correction
category: performance
subcategory: time-management
tier: advanced
source: "ERTS User's Guide"
source_slug: otp-erts
authors: "Ericsson AB"
chapter: "Time and Time Correction in Erlang"
chapter_number: null
pdf_page: null
section: "Time Correction"
extraction_confidence: high
aliases:
  - "corrected estimate of time"
  - "time frequency adjustment"
prerequisites:
  - erlang-monotonic-time
  - os-system-time-and-os-monotonic-time
  - time-warp-modes
extends: []
related:
  - erlang-system-time
  - time-offset
  - time-warp
contrasts_with: []
answers_questions:
  - "What is time correction in Erlang?"
  - "How does the Erlang runtime keep time accurate?"
---

# Quick Definition

Time correction is the ERTS mechanism that uses both OS system time and OS monotonic time to adjust the frequency of the Erlang monotonic clock. It ensures Erlang monotonic time does not warp and maintains relatively accurate frequency. The type of frequency adjustment depends on the time warp mode.

# Core Definition

The ERTS User's Guide states: "If time correction is enabled, the Erlang runtime system makes use of both OS system time and OS monotonic time, to adjust the frequency of the Erlang monotonic clock. Time correction ensures that Erlang monotonic time does not warp and that the frequency is relatively accurate. The type of frequency adjustments depends on the time warp mode used." (Time and Time Correction, "Time Correction" section).

The source provides critical historical context: "Erlang therefore introduced the 'corrected estimate of time', or the 'time correction', many years ago. The time correction relies on the fact that most operating systems have some kind of monotonic clock, either a real-time extension or some built-in 'tick counter' that is independent of the wall clock settings."

# Prerequisites

- **erlang-monotonic-time** -- Time correction adjusts the Erlang monotonic clock
- **os-system-time-and-os-monotonic-time** -- Both OS time sources are inputs to time correction
- **time-warp-modes** -- The type of frequency adjustment depends on the mode

# Key Properties

1. Enabled by default if the platform supports OS monotonic time
2. Uses both OS system time and OS monotonic time as inputs
3. Adjusts the frequency of the Erlang monotonic clock
4. Ensures Erlang monotonic time never warps (no backwards leaps)
5. Ensures relatively accurate monotonic clock frequency
6. The type of frequency adjustment depends on the time warp mode
7. Controlled via the `+c [true|false]` command-line flag
8. Platform support requires both OS monotonic time and a runtime system implementation
9. Check support: `erlang:system_info(os_monotonic_time_source)`
10. Check if enabled: `erlang:system_info(time_correction)`

# Construction / Recognition

## To Enable/Disable:

```text
erl +c true    %% Enable time correction (default if supported)
erl +c false   %% Disable time correction (strongly discouraged)
```

## To Query:

```erlang
%% Check if time correction is enabled
erlang:system_info(time_correction).

%% Check OS monotonic time source (needed for time correction)
erlang:system_info(os_monotonic_time_source).
```

## Interaction with Time Warp Modes:

1. **No-time-warp mode + time correction**: Frequency adjusted to align both system times (can introduce up to 1% error)
2. **Single-time-warp mode + time correction**: During preliminary phase, frequency kept correct (no alignment); after finalization, behaves as no-time-warp mode
3. **Multi-time-warp mode + time correction**: Frequency adjusted for maximum accuracy (alignment done via offset changes instead)

# Context & Application

The source is emphatic that time correction should almost never be disabled: "You typically never want to disable time correction. Previously a performance penalty was associated with time correction, but nowadays it is usually the other way around. If time correction is disabled, you probably get bad scalability, bad performance, and bad time measurements."

Without time correction, the consequences are severe: "If time correction is disabled, Erlang monotonic time can warp forwards or stop, or even freeze for extended periods of time. There are then no guarantees that the frequency of the Erlang monotonic clock is accurate or stable."

The source explains why computers need time correction at all: "A 'normal' modern computer cannot keep time, not on itself and not unless you have a chip-level atomic clock wired to it. Time, as perceived by your computer, must normally be corrected. Hence the Network Time Protocol (NTP) protocol, together with the `ntpd` process, does its best to keep your computer time in sync with the correct time."

The preferred overall configuration is multi-time-warp mode with time correction enabled: "Multi-time warp mode in combination with time correction is the preferred configuration."

# Examples

**Checking time correction status** (Time and Time Correction, "Time Correction" section):

```erlang
%% Check if time correction is enabled on this system
true = erlang:system_info(time_correction).

%% Check the OS monotonic time source (required for time correction)
erlang:system_info(os_monotonic_time_source).
%% Returns a list of tuples describing the source
```

**Behavior without time correction** (Time and Time Correction, "Time Correction" and mode subsections):

```text
%% With time correction DISABLED:
%% - In no-time-warp mode: monotonic time FREEZES on backward OS time leaps
%%   and LEAPS FORWARD on forward OS time leaps
%% - In multi-time-warp mode: monotonic time briefly stops on backward OS
%%   time leaps but does not freeze for extended periods
%% - In all modes: no frequency accuracy or stability guarantees
```

# Relationships

## Builds Upon

- **erlang-monotonic-time** -- Time correction adjusts the monotonic clock
- **os-system-time-and-os-monotonic-time** -- Both OS sources feed the correction mechanism
- **time-warp-modes** -- The mode determines what type of frequency adjustment is made

## Enables

- **erlang-system-time** -- Accurate system time depends on accurate monotonic time and proper offset management
- **timer-resolution** -- Timer accuracy benefits from correct monotonic clock frequency

## Related

- **time-offset** -- In some modes, time correction also influences offset management
- **time-warp** -- Time correction prevents monotonic time warps; system time warps are mode-dependent

# Common Errors

- **Error**: Disabling time correction for perceived performance benefits
  **Correction**: The source states: "Previously a performance penalty was associated with time correction, but nowadays it is usually the other way around." Disabling it leads to worse performance, scalability, and measurements.

- **Error**: Assuming time correction works without OS monotonic time
  **Correction**: Time correction requires OS monotonic time. Check availability with `erlang:system_info(os_monotonic_time_source)`.

# Common Confusions

- **Confusion**: Thinking time correction prevents all time warps
  **Clarification**: Time correction prevents Erlang monotonic time from warping. It does not prevent Erlang system time warps -- those are controlled by the time warp mode.

- **Confusion**: Believing time correction makes Erlang time perfectly accurate
  **Clarification**: Time correction makes the monotonic clock "relatively accurate." The accuracy still depends on the underlying OS monotonic time source, which itself has drift that "cannot be ignored."

# Source Reference

"Time and Time Correction in Erlang" chapter, "Time Correction" section and "Introduction" section. The mode-specific behavior of time correction is described in the "No Time Warp Mode," "Single Time Warp Mode," and "Multi-Time Warp Mode" subsections.

# Verification Notes

- Core definition: Direct quote from source
- "Corrected estimate of time" terminology: Direct from source
- Warning against disabling: Direct quotes from source
- Behavior without time correction: Direct from source ("can warp forwards or stop, or even freeze")
- Performance inversion: Direct from source ("nowadays it is usually the other way around")
- NTP context: Paraphrased from source introduction
- Confidence: HIGH -- the section provides explicit definitions, behavioral guarantees, and strong recommendations
