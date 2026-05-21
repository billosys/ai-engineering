---
concept: Timer Module Overhead
slug: timer-module-overhead
category: performance
subcategory: process-bottlenecks
tier: intermediate
source: "Erlang Efficiency Guide"
source_slug: otp-efficiency-guide
authors: "Ericsson/OTP Team"
chapter: "Common Caveats"
chapter_number: null
pdf_page: null
section: "Timer Module"
extraction_confidence: high
aliases:
  - "timer server bottleneck"
  - "timer module vs erlang timers"
prerequisites: []
extends: []
related:
  - erlang-system-limits
contrasts_with: []
answers_questions:
  - "How does erlang:send_after/3 compare to the timer module?"
  - "Why can the timer module become a bottleneck?"
  - "Which timer functions are safe to use without performance concerns?"
---

# Quick Definition

The `timer` module in STDLIB uses a single server process to manage timers, making it a potential bottleneck. The BIFs `erlang:send_after/3` and `erlang:start_timer/3` are more efficient alternatives for creating timers.

# Core Definition

Creating timers using `erlang:send_after/3` and `erlang:start_timer/3` is more efficient than using the timers provided by the `timer` module in STDLIB. The `timer` module uses a separate process to manage the timers, and this single process can become a bottleneck of an application (Ericsson/OTP Team, "Common Caveats," section "Timer Module").

Before Erlang/OTP 25, the management overhead was substantial and increased with the number of timers, especially short-lived ones, causing the timer server process to easily become overloaded and unresponsive. In OTP 25, the timer module was improved by removing most of the management overhead, but the timer server remains a single process that may still become a bottleneck.

Functions in the `timer` module that do not manage timers (such as `timer:tc/3` or `timer:sleep/1`) do not call the timer-server process and are therefore harmless.

# Prerequisites

This is a foundational concept with no prerequisites within this source beyond general Erlang knowledge.

# Key Properties

1. The `timer` module delegates timer management to a single server process
2. `erlang:send_after/3` and `erlang:start_timer/3` are BIFs that bypass this server process
3. Before OTP 25, the timer server had substantial overhead that scaled with timer count
4. OTP 25 improved the timer module but the single-process bottleneck remains
5. Timer-unrelated functions in the `timer` module (e.g., `timer:tc/3`, `timer:sleep/1`) are safe -- they do not use the timer server process

# Construction / Recognition

## Recognizing the Anti-Pattern

1. Look for calls to `timer:send_after/2,3`, `timer:apply_after/4`, `timer:send_interval/2,3`, or `timer:apply_interval/4`
2. Assess whether the application creates many timers concurrently
3. If timer volume is high, the single timer server process may become a bottleneck

## Applying the Fix

1. Replace `timer:send_after/2` with `erlang:send_after/3`
2. Replace `timer:start_timer/3` patterns with `erlang:start_timer/3`
3. Keep using `timer:tc/3` and `timer:sleep/1` freely -- these are harmless

# Context & Application

This caveat is especially relevant in high-throughput systems that create many short-lived timers, such as:

- Protocol implementations with per-message timeouts
- Connection managers tracking idle timeouts
- Rate-limiting systems

The improvement in OTP 25 reduced the severity of this issue, but the architectural limitation (single process) means it can still surface under heavy load.

**Historical note:** The timer module's performance problems were severe enough before OTP 25 that experienced Erlang developers routinely avoided it entirely. Post OTP 25, casual use is less problematic, but high-volume timer creation should still use the BIFs directly.

# Examples

**Prefer BIFs for timer creation** (source: "Common Caveats," section "Timer Module"):

```erlang
%% Prefer this (BIF, no server process involvement):
erlang:send_after(5000, self(), timeout).

%% Over this (uses the timer server process):
timer:send_after(5000, timeout).
```

**Safe timer module functions** (source: same section):

```erlang
%% These do NOT call the timer-server process and are harmless:
timer:sleep(1000).
{Time, Value} = timer:tc(fun my_function/0).
```

# Relationships

## Related

- **erlang-system-limits** -- System limits on processes and ports are relevant when considering process-based bottlenecks like the timer server

# Common Errors

- **Error**: Using `timer:send_after/2` in a high-throughput loop creating thousands of timers
  **Correction**: Use `erlang:send_after/3` instead to avoid the single-process bottleneck

- **Error**: Avoiding all `timer` module functions, including `timer:tc/3` and `timer:sleep/1`
  **Correction**: These functions do not call the timer server and are safe to use freely

# Common Confusions

- **Confusion**: Believing the timer module was fully fixed in OTP 25 and is now always safe
  **Clarification**: OTP 25 removed most overhead, but the single-process architecture remains a potential bottleneck under heavy load

- **Confusion**: Thinking `timer:sleep/1` goes through the timer server process
  **Clarification**: `timer:sleep/1` and `timer:tc/3` do not use the timer server and have no overhead concern

# Source Reference

"Common Caveats," section "Timer Module." The source explicitly recommends `erlang:send_after/3` and `erlang:start_timer/3` over the `timer` module and explains the OTP 25 improvements.

# Verification Notes

- Definition: Direct from source -- "Creating timers using erlang:send_after/3 and erlang:start_timer/3, is more efficient than using the timers provided by the timer module"
- OTP 25 improvement details: Explicit in source
- Harmless functions list: Explicitly named in source (timer:tc/3, timer:sleep/1)
- Confidence: HIGH -- explicit documentation from official OTP guide with clear recommendations
