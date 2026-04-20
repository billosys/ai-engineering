---
# === CORE IDENTIFICATION ===
concept: Defer to Clean Up
slug: defer-to-clean-up

# === CLASSIFICATION ===
category: code-safety
subcategory: resource-management
tier: foundational

# === PROVENANCE ===
source: "Uber Go Style Guide"
source_slug: uber-style
authors: "Prashant Varanasi, Simon Newton"
chapter: "Guidelines"
chapter_number: 2
pdf_page: null
section: "Defer to Clean Up"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "defer for cleanup"
  - "defer unlock"
  - "defer close"

# === TYPED RELATIONSHIPS ===
prerequisites: []
extends: []
related:
  - zero-value-mutexes
  - copy-slices-and-maps-at-boundaries
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "When should I use defer in Go?"
  - "Is the overhead of defer significant?"
  - "How does defer improve code readability for resource cleanup?"
---

# Quick Definition

Use `defer` to clean up resources such as files and locks. The overhead is extremely small and the readability benefit is worth the minimal cost.

# Core Definition

The Uber Go Style Guide recommends using `defer` to clean up resources such as files and locks. Defer has an extremely small overhead and should be avoided only if you can prove that your function execution time is in the order of nanoseconds. The readability benefit of using defers is worth the minimal cost, especially for larger methods that have more than simple memory accesses, where other computations are more significant than the `defer` (Uber Go Style Guide, "Defer to Clean Up").

# Prerequisites

This is a foundational concept with no prerequisites within this source beyond basic Go knowledge.

# Key Properties

1. `defer` guarantees cleanup runs when the function returns, regardless of which return path is taken
2. The overhead of `defer` is extremely small (nanosecond-scale)
3. Defer should be avoided only in functions with nanosecond-scale execution time
4. Using defer with locks prevents missing `Unlock()` calls across multiple return paths
5. Code using defer is more readable because the cleanup is paired with the acquisition

# Construction / Recognition

## To Apply:
1. Immediately after acquiring a resource (lock, file, connection), add a `defer` to release it
2. Place `defer` on the line directly after the acquisition for maximum clarity
3. For locks: `mu.Lock()` followed by `defer mu.Unlock()`
4. For files: `f, err := os.Open(...)` followed by `defer f.Close()` (after error check)

## To Recognize:
1. Look for functions with multiple return paths that manually release resources at each path -- these should use defer
2. Look for paired Lock/Unlock calls without defer -- easy to miss an Unlock on one path
3. Look for file operations without `defer f.Close()` -- potential resource leak

# Context & Application

Defer is especially valuable in functions with multiple return paths, where manually releasing resources at each path is error-prone. The classic example is mutex lock/unlock: without defer, every return statement needs its own `Unlock()` call, and it's easy to miss one. With defer, the unlock is guaranteed to execute regardless of the return path, making the code both safer and more readable.

# Examples

**Example 1** (Guidelines, "Defer to Clean Up"):

Bad -- manual unlock at each return path:
```go
p.Lock()
if p.count < 10 {
  p.Unlock()
  return p.count
}

p.count++
newCount := p.count
p.Unlock()

return newCount

// easy to miss unlocks due to multiple returns
```

Good -- defer handles unlock automatically:
```go
p.Lock()
defer p.Unlock()

if p.count < 10 {
  return p.count
}

p.count++
return p.count

// more readable
```

# Relationships

## Builds Upon
- **Go defer mechanism** -- Understanding how deferred function calls work in Go

## Enables
- Reliable resource cleanup in complex functions
- Simpler, more readable code with multiple return paths

## Related
- **zero-value-mutexes** -- Mutexes are a primary use case for defer-based cleanup
- **copy-slices-and-maps-at-boundaries** -- Both patterns protect internal state integrity

## Contrasts With
- Manual resource cleanup at every return path (error-prone approach)

# Common Errors

- **Error**: Forgetting to unlock a mutex on one of several return paths when not using defer
  **Correction**: Use `defer mu.Unlock()` immediately after `mu.Lock()`

- **Error**: Avoiding defer due to performance concerns in normal application code
  **Correction**: Only avoid defer in functions with nanosecond-scale execution times; for all other code, the readability win outweighs the minimal cost

# Common Confusions

- **Confusion**: Believing that defer has significant performance overhead
  **Clarification**: Defer's overhead is extremely small and should only be a concern for functions running at nanosecond scale

- **Confusion**: Thinking defer executes immediately
  **Clarification**: Deferred functions execute when the surrounding function returns, in LIFO (last-in, first-out) order

# Source Reference

Chapter 2: Guidelines, Section "Defer to Clean Up".

# Verification Notes

- Definition source: Directly from the "Defer to Clean Up" section with Bad/Good code comparison
- Confidence rationale: HIGH -- explicit guideline with concrete example and clear rationale about overhead
- Uncertainties: None
- Cross-reference status: Related slugs verified against planned extractions
