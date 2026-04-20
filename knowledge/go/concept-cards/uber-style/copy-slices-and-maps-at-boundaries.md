---
# === CORE IDENTIFICATION ===
concept: Copy Slices and Maps at Boundaries
slug: copy-slices-and-maps-at-boundaries

# === CLASSIFICATION ===
category: data-structures
subcategory: defensive-copying
tier: intermediate

# === PROVENANCE ===
source: "Uber Go Style Guide"
source_slug: uber-style
authors: "Prashant Varanasi, Simon Newton"
chapter: "Guidelines"
chapter_number: 2
pdf_page: null
section: "Copy Slices and Maps at Boundaries"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "defensive copying"
  - "slice and map copying"
  - "copy at API boundaries"

# === TYPED RELATIONSHIPS ===
prerequisites: []
extends: []
related:
  - zero-value-mutexes
  - defer-to-clean-up
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do I safely copy slices and maps at API boundaries?"
  - "Why should I copy slices and maps when receiving or returning them?"
  - "How can returning a map from a mutex-protected method cause data races?"
---

# Quick Definition

Slices and maps contain pointers to underlying data, so when receiving them as arguments or returning them from functions, copy them to prevent callers from unexpectedly mutating internal state.

# Core Definition

The Uber Go Style Guide warns that slices and maps contain pointers to the underlying data, so you must be wary of scenarios when they need to be copied. When receiving a slice or map as a function argument, callers can modify the data through their reference if you store it directly. When returning a slice or map, callers can modify your internal state through the returned reference. Both scenarios are solved by making defensive copies at API boundaries (Uber Go Style Guide, "Copy Slices and Maps at Boundaries").

# Prerequisites

- **Slices in Go** -- Understanding that slices are backed by an underlying array and multiple slices can share the same backing array
- **Maps in Go** -- Understanding that maps are reference types and assignments share the same underlying data
- **sync.Mutex** -- Understanding mutual exclusion, since a key example involves mutex-protected maps

# Key Properties

1. Slices and maps are reference types -- assigning them does not copy the underlying data
2. Storing a received slice or map directly allows the caller to mutate your internal state
3. Returning an internal slice or map directly allows the caller to mutate your internal state
4. For slices: use `make` + `copy` to create a defensive copy
5. For maps: iterate and copy key-value pairs into a new map
6. Returning a mutex-protected map without copying exposes the data to races once the lock is released

# Construction / Recognition

## To Apply:
1. When receiving a slice as a parameter and storing it, create a copy:
   - `d.items = make([]T, len(items))` then `copy(d.items, items)`
2. When receiving a map as a parameter and storing it, create a copy:
   - Iterate over the input map and copy each key-value pair into a new map
3. When returning an internal slice, return a copy instead
4. When returning an internal map, create and return a copy with the same entries
5. Pre-allocate the copy with the correct capacity using `len()` for efficiency

## To Recognize:
1. Look for methods that directly assign a received slice/map to a struct field -- this is the anti-pattern
2. Look for methods that return an internal slice/map field directly -- this is the anti-pattern
3. Look for mutex-protected fields being returned without copying -- this creates race conditions

# Context & Application

This guideline is critical for any Go code that stores or exposes slices and maps at API boundaries -- especially in concurrent programs. The classic example is a mutex-protected map: if you return the map reference directly, callers can read and write to it without acquiring the lock, leading to data races. Defensive copying ensures internal state remains encapsulated.

# Examples

**Example 1** (Guidelines, "Receiving Slices and Maps"):

Bad -- storing the received slice directly:
```go
func (d *Driver) SetTrips(trips []Trip) {
  d.trips = trips
}

trips := ...
d1.SetTrips(trips)

// Did you mean to modify d1.trips?
trips[0] = ...
```

Good -- copying the received slice:
```go
func (d *Driver) SetTrips(trips []Trip) {
  d.trips = make([]Trip, len(trips))
  copy(d.trips, trips)
}

trips := ...
d1.SetTrips(trips)

// We can now modify trips[0] without affecting d1.trips.
trips[0] = ...
```

**Example 2** (Guidelines, "Returning Slices and Maps"):

Bad -- returning the internal map directly (race condition):
```go
type Stats struct {
  mu sync.Mutex
  counters map[string]int
}

func (s *Stats) Snapshot() map[string]int {
  s.mu.Lock()
  defer s.mu.Unlock()

  return s.counters
}

// snapshot is no longer protected by the mutex, so any
// access to the snapshot is subject to data races.
snapshot := stats.Snapshot()
```

Good -- returning a copy of the map:
```go
func (s *Stats) Snapshot() map[string]int {
  s.mu.Lock()
  defer s.mu.Unlock()

  result := make(map[string]int, len(s.counters))
  for k, v := range s.counters {
    result[k] = v
  }
  return result
}

// Snapshot is now a copy.
snapshot := stats.Snapshot()
```

# Relationships

## Builds Upon
- **Go reference types** -- Understanding that slices and maps are reference types is the foundation for this guideline

## Enables
- Thread-safe APIs by preventing accidental shared-state mutation
- Clean encapsulation of internal data structures

## Related
- **zero-value-mutexes** -- Mutex-protected data often needs defensive copying when returned
- **defer-to-clean-up** -- Defer is used with mutex unlock in the examples

## Contrasts With
- Directly storing or returning slices/maps without copying (the anti-pattern)

# Common Errors

- **Error**: Directly assigning a received slice to a struct field (`d.trips = trips`)
  **Correction**: Create a copy with `make` and `copy` before storing

- **Error**: Returning a mutex-protected map reference directly
  **Correction**: Copy the map contents into a new map before returning, while still holding the lock

# Common Confusions

- **Confusion**: Believing that assigning a slice to a new variable creates a copy of the data
  **Clarification**: Slice assignment copies only the slice header (pointer, length, capacity), not the underlying array data

- **Confusion**: Thinking the mutex protects the map after Snapshot() returns
  **Clarification**: Once the lock is released, the returned map reference is unprotected; only a copy provides safety

# Source Reference

Chapter 2: Guidelines, Section "Copy Slices and Maps at Boundaries", subsections "Receiving Slices and Maps" and "Returning Slices and Maps".

# Verification Notes

- Definition source: Directly from the "Copy Slices and Maps at Boundaries" section with detailed Bad/Good examples
- Confidence rationale: HIGH -- the source provides explicit examples for both receiving and returning, with clear rationale
- Uncertainties: None
- Cross-reference status: Related slugs verified against planned extractions
