---
# === CORE IDENTIFICATION ===
concept: Channel Size Is One or None
slug: channel-size-is-one-or-none

# === CLASSIFICATION ===
category: concurrency
subcategory: channels
tier: intermediate

# === PROVENANCE ===
source: "Uber Go Style Guide"
source_slug: uber-style
authors: "Prashant Varanasi, Simon Newton"
chapter: "Guidelines"
chapter_number: 2
pdf_page: null
section: "Channel Size is One or None"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "channel buffer size"
  - "unbuffered channels"
  - "buffered channel size one"

# === TYPED RELATIONSHIPS ===
prerequisites: []
extends: []
related:
  - zero-value-mutexes
  - defer-to-clean-up
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What size should Go channels be?"
  - "When is a buffered channel appropriate?"
  - "Why should channel buffers be limited to size 0 or 1?"
---

# Quick Definition

Channels should usually have a size of one or be unbuffered (size zero). Any other size must be subject to a high level of scrutiny.

# Core Definition

The Uber Go Style Guide states that channels should usually have a size of one or be unbuffered. By default, channels are unbuffered and have a size of zero. Any other size must be subject to a high level of scrutiny. The guide advises considering how the size is determined, what prevents the channel from filling up under load and blocking writers, and what happens when blocking occurs (Uber Go Style Guide, "Channel Size is One or None").

# Prerequisites

- **Go channels** -- Understanding how channels work, including buffered vs unbuffered semantics
- **Goroutines** -- Understanding concurrent execution and how goroutines communicate via channels

# Key Properties

1. By default, channels are unbuffered (size zero)
2. Unbuffered channels synchronize sender and receiver -- both block until the other is ready
3. A buffered channel of size one allows the sender to proceed once without a ready receiver
4. Any buffer size other than 0 or 1 requires careful justification
5. When choosing a larger buffer, you must answer: how is the size determined, what prevents filling, and what happens on fill

# Construction / Recognition

## To Apply:
1. Default to unbuffered channels: `c := make(chan T)`
2. Use size-one buffer when you need to decouple a single send from receive: `c := make(chan T, 1)`
3. If considering a larger buffer, document: why this specific size, what prevents overflow, what happens on overflow
4. Never use arbitrary large buffers (e.g., `make(chan int, 64)`) without rigorous justification

## To Recognize:
1. Look for `make(chan T, N)` where N > 1 -- this should be scrutinized
2. Comments like "ought to be enough" near channel declarations are a red flag
3. Arbitrary round-number buffer sizes (64, 100, 1024) without documentation are suspect

# Context & Application

This guideline prevents a common concurrency anti-pattern: using large channel buffers to mask synchronization problems. A large buffer can hide the fact that producers are outpacing consumers, delaying the problem rather than solving it. When the buffer eventually fills, the system exhibits the same blocking behavior but the bug is harder to reproduce and diagnose. By defaulting to unbuffered or size-one channels, concurrency issues surface immediately and are easier to reason about.

# Examples

**Example 1** (Guidelines, "Channel Size is One or None"):

Bad:
```go
// Ought to be enough for anybody!
c := make(chan int, 64)
```

Good:
```go
// Size of one
c := make(chan int, 1) // or
// Unbuffered channel, size of zero
c := make(chan int)
```

# Relationships

## Builds Upon
- **Go channel semantics** -- Understanding buffered vs unbuffered behavior is essential

## Enables
- Easier reasoning about concurrent code
- Early detection of producer/consumer imbalances

## Related
- **zero-value-mutexes** -- Another concurrency guideline from the same source
- **defer-to-clean-up** -- Defer is often used in goroutine cleanup patterns involving channels

## Contrasts With
- Using arbitrary large buffer sizes as a concurrency band-aid

# Common Errors

- **Error**: Using a large buffer size (e.g., 64 or 100) without analysis of overflow behavior
  **Correction**: Default to unbuffered or size 1; if a larger buffer is needed, document the justification

- **Error**: Using a buffered channel to avoid deadlocks rather than fixing the synchronization design
  **Correction**: Investigate why the deadlock occurs and fix the root cause; the buffer should not be a workaround

# Common Confusions

- **Confusion**: Believing larger buffers always improve performance
  **Clarification**: Larger buffers can mask problems and delay failures; they should only be used when there is a clear, documented reason

- **Confusion**: Thinking unbuffered channels are slow or inefficient
  **Clarification**: Unbuffered channels provide synchronization guarantees and are appropriate for most use cases; the "overhead" is the synchronization itself, which is usually desired

# Source Reference

Chapter 2: Guidelines, Section "Channel Size is One or None".

# Verification Notes

- Definition source: Directly from the "Channel Size is One or None" section with Bad/Good code comparison
- Confidence rationale: HIGH -- explicit guideline with clear rationale and example
- Uncertainties: None
- Cross-reference status: Related slugs verified against planned extractions
