---
# === CORE IDENTIFICATION ===
concept: Use Time to Handle Time
slug: use-time-to-handle-time

# === CLASSIFICATION ===
category: data-structures
subcategory: time-handling
tier: intermediate

# === PROVENANCE ===
source: "Uber Go Style Guide"
source_slug: uber-style
authors: "Prashant Varanasi, Simon Newton"
chapter: "Guidelines"
chapter_number: 2
pdf_page: null
section: "Use `\"time\"` to handle time"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "time.Time best practices"
  - "time.Duration best practices"
  - "Go time handling"

# === TYPED RELATIONSHIPS ===
prerequisites: []
extends: []
related:
  - start-enums-at-one
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How does `time.Time` differ from `time.Duration` in external system interactions?"
  - "What distinguishes `time.Add` from `time.AddDate`?"
  - "How should I represent time in Go APIs?"
  - "How do I handle time durations in JSON when time.Duration is not supported?"
---

# Quick Definition

Always use the `time` package (`time.Time` for instants, `time.Duration` for periods) when dealing with time. Avoid representing time as raw integers or floats, which introduce ambiguity and errors.

# Core Definition

The Uber Go Style Guide states that time is complicated and that many common assumptions about time are incorrect (e.g., a day does not always have 24 hours due to daylight saving time). Therefore, always use the `time` package when dealing with time. Use `time.Time` for instants of time and the methods on `time.Time` for comparing, adding, or subtracting time. Use `time.Duration` for periods of time. When interacting with external systems, prefer `time.Time` and `time.Duration` where possible; when not possible, include the unit in the field name (e.g., `IntervalMillis`). For timestamps in serialization, use RFC 3339 format (Uber Go Style Guide, "Use `\"time\"` to handle time").

# Prerequisites

- **Go standard library** -- Familiarity with the `time` package basics
- **JSON/YAML serialization** -- Understanding of how Go structs are marshaled to external formats

# Key Properties

1. Use `time.Time` for instants of time, not `int` or `int64`
2. Use `time.Duration` for periods of time, not raw integers
3. `Time.Add` adds a fixed duration (e.g., exactly 24 hours); `Time.AddDate` adds calendar units (e.g., 1 day, accounting for DST)
4. When `time.Duration` is not available in external formats (e.g., JSON), include the unit in the field name (e.g., `IntervalMillis`)
5. When `time.Time` is not available, use RFC 3339 formatted strings
6. Many external systems support time types natively: `flag` supports `time.Duration`, `encoding/json` supports `time.Time` as RFC 3339, `database/sql` supports `time.Time` for DATETIME/TIMESTAMP columns
7. The `time` package does not support leap seconds in parsing or calculations

# Construction / Recognition

## To Apply:
1. Replace `int` or `float64` time parameters with `time.Time` or `time.Duration`
2. Use `time.Time` methods (`Before`, `After`, `Equal`, `Add`, `Sub`) for comparisons and arithmetic
3. Use `Time.AddDate(0, 0, 1)` for "next calendar day" and `Time.Add(24 * time.Hour)` for "exactly 24 hours later"
4. For JSON fields without `time.Duration` support, name fields with units: `IntervalMillis`, `TimeoutSecs`
5. For JSON timestamps, use RFC 3339 format via `time.RFC3339`

## To Recognize:
1. Look for `int` or `float64` parameters named `delay`, `timeout`, `interval`, `timestamp` -- these should be `time.Duration` or `time.Time`
2. Look for ambiguous calls like `poll(10)` where the unit is unclear -- should be `poll(10 * time.Second)`
3. Look for `t.Add(24 * time.Hour)` used for "next day" -- may need `t.AddDate(0, 0, 1)` instead

# Context & Application

Time handling is a pervasive source of bugs. Common incorrect assumptions include: a day always has 24 hours (false due to DST), an hour always has 60 minutes, a year always has 365 days. The `time` package accounts for many of these edge cases. The distinction between `Time.Add` and `Time.AddDate` is critical: `Add` works with absolute durations while `AddDate` works with calendar units that respect daylight saving transitions and varying month lengths.

When integrating with external systems (command-line flags, JSON, SQL, YAML), prefer the native `time.Time` and `time.Duration` support where available. When not available, always include the unit in the field or variable name to prevent ambiguity.

# Examples

**Example 1** (Guidelines, "Use `time.Time` for instants of time"):

Bad:
```go
func isActive(now, start, stop int) bool {
  return start <= now && now < stop
}
```

Good:
```go
func isActive(now, start, stop time.Time) bool {
  return (start.Before(now) || start.Equal(now)) && now.Before(stop)
}
```

**Example 2** (Guidelines, "Use `time.Duration` for periods of time"):

Bad:
```go
func poll(delay int) {
  for {
    // ...
    time.Sleep(time.Duration(delay) * time.Millisecond)
  }
}

poll(10) // was it seconds or milliseconds?
```

Good:
```go
func poll(delay time.Duration) {
  for {
    // ...
    time.Sleep(delay)
  }
}

poll(10*time.Second)
```

**Example 3** (Guidelines, "Use `time.Time` and `time.Duration` with external systems"):

The difference between `Time.Add` and `Time.AddDate`:
```go
newDay := t.AddDate(0 /* years */, 0 /* months */, 1 /* days */)
maybeNewDay := t.Add(24 * time.Hour)
```

**Example 4** (Guidelines, "Use `time.Time` and `time.Duration` with external systems"):

When `time.Duration` is not supported in serialization, include the unit in the name:

Bad:
```go
// {"interval": 2}
type Config struct {
  Interval int `json:"interval"`
}
```

Good:
```go
// {"intervalMillis": 2000}
type Config struct {
  IntervalMillis int `json:"intervalMillis"`
}
```

# Relationships

## Builds Upon
- **Go `time` package** -- This guideline codifies best practices for using the standard library's time package

## Enables
- Correct handling of time zones, DST transitions, and calendar arithmetic
- Unambiguous APIs where time parameters are self-documenting

## Related
- **start-enums-at-one** -- Both are Guidelines section recommendations about using Go's type system to prevent ambiguity

## Contrasts With
- Using raw `int` or `float64` for time values (ambiguous, error-prone)

# Common Errors

- **Error**: Using `t.Add(24 * time.Hour)` to get "tomorrow" (next calendar day)
  **Correction**: Use `t.AddDate(0, 0, 1)` for calendar-day semantics; `Add` with 24 hours may not cross a calendar day boundary during DST transitions

- **Error**: Accepting `int` delay parameters where the unit is ambiguous
  **Correction**: Use `time.Duration` so the caller specifies the unit explicitly: `poll(10 * time.Second)`

- **Error**: Using `int` for JSON interval fields without indicating the unit
  **Correction**: Include the unit in the field name: `IntervalMillis`, `TimeoutSecs`

# Common Confusions

- **Confusion**: Believing `time.Add(24 * time.Hour)` and `time.AddDate(0, 0, 1)` are equivalent
  **Clarification**: `Add` adds an exact duration; `AddDate` adds calendar units. On a DST transition day, adding 24 hours may not yield the same time on the next day, while `AddDate(0, 0, 1)` will give the same clock time the next day.

- **Confusion**: Thinking the `time` package handles leap seconds
  **Clarification**: Go's `time` package does not support parsing timestamps with leap seconds and does not account for them in calculations

# Source Reference

Chapter 2: Guidelines, Section "Use `\"time\"` to handle time", subsections "Use `time.Time` for instants of time", "Use `time.Duration` for periods of time", and "Use `time.Time` and `time.Duration` with external systems".

# Verification Notes

- Definition source: Directly from the comprehensive "Use `\"time\"` to handle time" section with multiple subsections and examples
- Confidence rationale: HIGH -- extensive source material with multiple Bad/Good examples, detailed subsections, and explicit rationale
- Uncertainties: None
- Cross-reference status: Related slugs verified against planned extractions
