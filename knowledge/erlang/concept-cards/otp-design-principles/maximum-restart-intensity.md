---
# === CORE IDENTIFICATION ===
concept: Maximum Restart Intensity
slug: maximum-restart-intensity

# === CLASSIFICATION ===
category: fault-tolerance
subcategory: restart-limiting
tier: intermediate

# === PROVENANCE ===
source: "OTP Design Principles"
source_slug: otp-design-principles
authors: "Ericsson AB"
chapter: "Supervisor Behaviour"
chapter_number: null
pdf_page: null
section: "Maximum Restart Intensity"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "MaxR/MaxT"
  - "intensity and period"
  - "restart intensity"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - supervisor-behaviour
  - supervisor-flags
extends: []
related:
  - restart-strategy
  - child-restart-type
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do restart strategies affect child processes?"
  - "What must I know before designing a supervision tree?"
---

# Quick Definition

Maximum restart intensity is a built-in supervisor mechanism that limits the number of child restarts allowed within a given time period, causing the supervisor to terminate itself if the limit is exceeded.

# Core Definition

Supervisors have a built-in mechanism to limit the number of restarts which can occur in a given time interval. This is specified by the two keys `intensity` and `period` in the supervisor flags map. If more than `MaxR` (intensity) number of restarts occur in the last `MaxT` (period) seconds, the supervisor terminates all the child processes and then itself with reason `shutdown`. When the supervisor terminates, the next higher-level supervisor takes action -- it either restarts the terminated supervisor or terminates itself. The intention is to prevent a situation where a process repeatedly dies for the same reason, only to be restarted again. The default values are `intensity => 1` and `period => 5`. (Source: sup_princ.md, "Maximum Restart Intensity")

# Prerequisites

- **[Supervisor Behaviour](/concept-cards/otp-design-principles/supervisor-behaviour.md)** -- Restart intensity is a supervisor property.
- **[Supervisor Flags](/concept-cards/otp-design-principles/supervisor-flags.md)** -- Configured via `intensity` and `period` keys.

# Key Properties

1. **Two parameters**: `intensity` (MaxR, default 1) and `period` (MaxT, default 5 seconds).
2. **Sliding window**: Counts restarts in the last `MaxT` seconds (not a fixed window).
3. **Escalation on breach**: Supervisor terminates all children and itself with reason `shutdown`.
4. **Cascading to parent**: The parent supervisor then decides whether to restart or escalate further.
5. **Multiplicative across levels**: Total restarts before top-level gives up is the product of intensities at all levels.

# Construction / Recognition

## To Construct/Create:
1. Set `intensity` and `period` in supervisor flags:

```erlang
SupFlags = #{intensity => MaxR, period => MaxT, ...}
```

## To Identify/Recognize:
1. Look for `intensity` and `period` keys in the supervisor flags map.

# Context & Application

Tuning restart intensity is critical for production systems. The source provides detailed guidance:

- **Burst tolerance**: Set `intensity` to allow short bursts (5-10 restarts) even within the same second for quick recovery.
- **Sustained failure rate**: Set `period` long enough to limit the sustained restart rate. For example, intensity 5 / period 30 gives at most one restart per 6 seconds sustained.
- **Multi-level hierarchies**: Do not set the same intensity at all levels. The product of intensities determines total restarts. For example, 10 at top level and 10 at next level means 100 restarts of the bottom child -- probably excessive.

# Examples

**Example 1** (sup_princ.md, "Maximum Restart Intensity"): Default intensity:

```erlang
SupFlags = #{intensity => 1, period => 5, ...}
```

If more than 1 restart occurs within 5 seconds, the supervisor terminates.

**Example 2** (sup_princ.md, "Tuning the intensity and period"): Recommended tuning -- intensity 5, period 30 gives at most one restart per 6 seconds for any longer period, keeping logs manageable.

**Example 3** (sup_princ.md, "Tuning the intensity and period"): Multi-level consideration -- if the top level allows 10 restarts and the next level also allows 10, a crashing child below that level will be restarted 100 times. Allowing at most 3 restarts for the top level is a better choice.

# Relationships

## Builds Upon
- **[Supervisor Flags](/concept-cards/otp-design-principles/supervisor-flags.md)** -- Intensity and period are supervisor flag keys.
- **[Supervisor Behaviour](/concept-cards/otp-design-principles/supervisor-behaviour.md)** -- This is an intrinsic supervisor mechanism.

## Enables
- Escalation of persistent failures up the supervision tree.
- Prevention of infinite restart loops.

## Related
- **[Restart Strategy](/concept-cards/otp-design-principles/restart-strategy.md)** -- Works in conjunction with the restart strategy.
- **[Child Restart Type](/concept-cards/otp-design-principles/child-restart-type.md)** -- Only restartable children count toward the intensity limit.

## Contrasts With
- None directly.

# Common Errors

- **Error**: Setting intensity to 1 and period to 6 for a "safe" rate, which prevents even two quick restart attempts.
  **Correction**: Consider burst tolerance. Use higher intensity with appropriate period (e.g., 5/30 or 10/60) to allow quick bursts while limiting sustained rate.

- **Error**: Setting period to a very high value (e.g., 3600) with a low intensity (e.g., 5), causing the supervisor to give up after a burst even if a later single restart is hours later.
  **Correction**: Keep period to 5-10 minutes so that temporally separated crashes are treated as separate incidents.

- **Error**: Setting the same restart intensities at all levels of a deep supervision hierarchy.
  **Correction**: The total restarts is the product of all levels' intensities. Use lower values at higher levels (e.g., 3 at top, 10 at bottom).

# Common Confusions

- **Confusion**: The supervisor only counts restarts within fixed time windows.
  **Clarification**: It counts restarts within the *last* `MaxT` seconds as a sliding window, not in fixed time slots.

# Source Reference

sup_princ.md, "Maximum Restart Intensity" and "Tuning the intensity and period" sections.

# Verification Notes

- Definition source: Directly from sup_princ.md, "Maximum Restart Intensity" section.
- Confidence rationale: High -- explicitly defined with detailed tuning guidance.
- Uncertainties: None.
- Cross-reference status: References supervisor-flags, restart-strategy, child-restart-type.
