---
concept: Time Warp Modes
slug: time-warp-modes
category: performance
subcategory: time-management
tier: advanced
source: "ERTS User's Guide"
source_slug: otp-erts
authors: "Ericsson AB"
chapter: "Time and Time Correction in Erlang"
chapter_number: null
pdf_page: null
section: "Time Warp Modes"
extraction_confidence: high
aliases:
  - "no time warp mode"
  - "single time warp mode"
  - "multi time warp mode"
  - "no_time_warp"
  - "single_time_warp"
  - "multi_time_warp"
prerequisites:
  - erlang-monotonic-time
  - erlang-system-time
  - time-offset
  - time-warp
extends: []
related:
  - time-correction
  - os-system-time-and-os-monotonic-time
  - timer-resolution
contrasts_with: []
answers_questions:
  - "What distinguishes the three time warp modes?"
  - "What must I know before using time warp modes?"
  - "What is a time warp in ERTS?"
---

# Quick Definition

Erlang provides three time warp modes that control how the time offset is managed and how Erlang system time aligns with OS system time. No-time-warp mode fixes the offset at startup (backward compatible); single-time-warp mode allows one offset adjustment after finalization; multi-time-warp mode (the default since OTP 26) allows the offset to change freely for best accuracy and performance.

# Core Definition

The ERTS User's Guide describes three time warp modes, set via the `+C` command-line flag: `+C no_time_warp`, `+C single_time_warp`, or `+C multi_time_warp`. The source states: "Current Erlang system time is determined by adding the current Erlang monotonic time with current time offset. The time offset is managed differently depending on which time warp mode you use." (Time and Time Correction, "Time Warp Modes" section).

**No Time Warp Mode**: "The time offset is determined at runtime system start and does not change later." To align system times, the runtime adjusts the Erlang monotonic clock frequency, which can introduce frequency errors "as large as 1%." Without time correction enabled, monotonic time freezes on backward OS time leaps and leaps forward on forward OS time leaps.

**Single Time Warp Mode**: Operates in two phases. During the preliminary phase, the time offset is fixed and monotonic clock frequency is kept correct (no alignment with OS system time). During the final phase, triggered by `erlang:system_flag(time_offset, finalize)`, the offset is adjusted once to align with OS system time, then fixed permanently. Requirements: OS time must be set earlier than actual POSIX time before startup, and must be correct at finalization time.

**Multi-Time Warp Mode**: "The time offset can change at any time without limitations." The source emphatically states: "Multi-time warp mode in combination with time correction is the preferred configuration. This as the Erlang runtime system have better performance, scale better, and behave better on almost all platforms. Also, the accuracy and precision of time measurements are better." This has been the default since OTP 26 (ERTS 14.0).

# Prerequisites

- **erlang-monotonic-time** -- Understanding how monotonic time is the time engine
- **erlang-system-time** -- Understanding that system time = monotonic time + offset
- **time-offset** -- The component managed differently by each mode
- **time-warp** -- Understanding what a time warp is and why it matters

# Key Properties

## No Time Warp Mode

1. Time offset fixed at startup, never changes
2. Frequency of Erlang monotonic clock is adjusted to align system times (can introduce up to 1% error)
3. No time warps in Erlang system time
4. Same behavior as pre-OTP 18 and was the default before OTP 26
5. Without time correction: monotonic time freezes on backward OS time leaps
6. All code is safe in this mode (no warps to handle)
7. Worst performance, scalability, and measurement accuracy of the three modes

## Single Time Warp Mode

1. Two phases: preliminary (offset fixed, no alignment) and final (offset adjusted once, then fixed)
2. Finalization triggered by `erlang:system_flag(time_offset, finalize)` (one-time only)
3. During preliminary phase, monotonic clock frequency stays correct but system time may diverge from OS
4. Forward time warp only at finalization -- OS time must be set early before startup
5. OS system time must be correct at finalization time
6. After finalization, behaves exactly as no-time-warp mode
7. Designed for embedded systems that boot without correct time

## Multi-Time Warp Mode

1. Time offset can change at any time without limitations
2. Enables best frequency accuracy for monotonic clock (adjusts independently of system time alignment)
3. Best performance, scalability, accuracy, and precision
4. Default since OTP 26 (ERTS 14.0)
5. Requires all code to be time warp safe
6. Without time correction: monotonic time briefly stops on backward OS time leaps (but does not freeze for extended periods)

# Construction / Recognition

## To Set the Mode:

```text
erl +C no_time_warp
erl +C single_time_warp
erl +C multi_time_warp
```

## To Query the Current Mode:

```erlang
erlang:system_info(time_warp_mode).
```

## To Choose the Right Mode:

1. **All code is time warp safe** -> Use multi-time-warp mode (best performance and accuracy)
2. **Some code is not time warp safe, system boots before correct time is available** -> Use single-time-warp mode
3. **Code is not time warp safe, need backward compatibility** -> Use no-time-warp mode
4. The source strongly encourages making all code time warp safe and using multi-time-warp mode

# Context & Application

As of OTP 26, multi-time-warp mode is the default. The source warns: "If you have old code in the system that is not time warp safe, you now explicitly need to start the system in no time warp mode (or single time warp mode if it is partially time warp safe) in order to avoid problems."

The source is emphatic about the preferred configuration: "Multi-time warp mode in combination with time correction is the preferred configuration." It also states: "If you have code that is not time warp safe, you are strongly encouraged to change this so that you can use multi time warp mode. Compared to no time warp mode, multi time warp mode improves scalability and performance as well as accuracy and precision of time measurements."

The single-time-warp mode exists for embedded systems: "On an embedded system it is not uncommon that the system has no power supply, not even a battery, when it is shut off. The system clock on such a system is typically way off when the system boots."

# Examples

**Starting with a specific time warp mode** (Time and Time Correction, "Time Warp Modes" section):

```text
%% Start with the preferred configuration (default since OTP 26)
erl +C multi_time_warp

%% Start with backward-compatible mode (no warps, reduced accuracy)
erl +C no_time_warp

%% Start with single-time-warp mode for embedded systems
erl +C single_time_warp
```

**Single-time-warp finalization workflow** (Time and Time Correction, "Single Time Warp Mode" section):

```erlang
%% 1. System boots with incorrect OS time (embedded scenario)
%% 2. Preliminary phase: time offset is fixed, system time may diverge
%% 3. OS time is corrected (e.g., via NTP)
%% 4. Finalize the time offset (can only be done once):
erlang:system_flag(time_offset, finalize).
%% 5. A single time warp occurs in Erlang system time
%% 6. System now behaves as no-time-warp mode
```

**Checking the current mode** (derived from source API):

```erlang
Mode = erlang:system_info(time_warp_mode).
%% Returns: no_time_warp | single_time_warp | multi_time_warp
```

# Relationships

## Builds Upon

- **erlang-monotonic-time** -- Each mode adjusts monotonic time frequency differently
- **erlang-system-time** -- Each mode achieves system time alignment differently
- **time-offset** -- The modes define how the time offset is managed
- **time-warp** -- The modes control when warps are permitted

## Related

- **time-correction** -- Time correction interacts with the warp mode to determine frequency adjustments
- **os-system-time-and-os-monotonic-time** -- The OS time sources that the modes align against
- **timer-resolution** -- Timers are triggered relative to monotonic time, which is affected by mode-dependent accuracy

# Common Errors

- **Error**: Running time warp unsafe code (e.g., using `erlang:now/0`) in multi-time-warp mode
  **Correction**: Replace `erlang:now/0` with the new time API. Or, if changing the code is not immediately possible, start with `+C no_time_warp`.

- **Error**: In single-time-warp mode, finalizing when OS system time is incorrect
  **Correction**: The source requires that "OS system time must be correct when the user finalizes the time offset." Ensure NTP has synchronized before calling `erlang:system_flag(time_offset, finalize)`.

- **Error**: In single-time-warp mode, starting with OS time later than actual POSIX time
  **Correction**: The source requires the time warp at finalization to go forward. "Set it to a time that is guaranteed to be earlier than actual POSIX time before starting the Erlang runtime system."

# Common Confusions

- **Confusion**: Thinking no-time-warp mode provides better time accuracy
  **Clarification**: The opposite is true. No-time-warp mode introduces up to 1% frequency error in the monotonic clock to prevent warps. Multi-time-warp mode provides the best accuracy and precision.

- **Confusion**: Believing the time warp mode only affects system time
  **Clarification**: The mode also affects how the Erlang monotonic clock frequency is adjusted. In no-time-warp mode, frequency is intentionally skewed to align system times; in multi-time-warp mode, frequency stays as accurate as possible.

- **Confusion**: Assuming single-time-warp mode is better than multi-time-warp for general use
  **Clarification**: Single-time-warp mode exists specifically for embedded systems booting without correct time. For general use, the source states multi-time-warp mode is "the preferred configuration."

# Source Reference

"Time and Time Correction in Erlang" chapter, "Time Warp Modes" section (including "No Time Warp Mode," "Single Time Warp Mode," and "Multi-Time Warp Mode" subsections), and the "Extended Time Functionality" note at the chapter start.

# Verification Notes

- All three mode descriptions: Paraphrased closely from their respective subsections
- 1% frequency error in no-time-warp mode: Explicit in source ("This error can be as large as 1%")
- Multi-time-warp as preferred: Direct quote from source
- OTP 26 default change: Explicit in source
- Single-time-warp requirements: Direct from source (forward warp only, correct OS time at finalization)
- Confidence: HIGH -- each mode is described in detail with explicit behavioral specifications
