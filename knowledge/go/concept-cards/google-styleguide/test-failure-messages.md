---
# === CORE IDENTIFICATION ===
concept: Test Failure Message Conventions
slug: test-failure-messages

# === CLASSIFICATION ===
category: testing
subcategory: failure-reporting
tier: foundational

# === PROVENANCE ===
source: "Google Go Style Guide"
source_slug: google-styleguide
authors: "Google Go Style Team"
chapter: "Style Decisions"
chapter_number: 3
pdf_page: null
section: "Useful test failures"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "test output format"
  - "got before want"
  - "identify the function"
  - "identify the input"
  - "test failure detail level"

# === TYPED RELATIONSHIPS ===
prerequisites: []
extends: []
related:
  - test-comparisons
  - assertion-libraries
  - use-percent-q
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What format should Go test failure messages follow?"
  - "Should got or want come first in test output?"
  - "Should I include the function name in test failure messages?"
  - "When should I use t.Error vs t.Fatal?"
  - "How much detail should test failure messages include?"
---

# Quick Definition

Test failure messages should follow the format `YourFunc(%v) = %v, want %v` -- include the function name, its inputs, the actual result ("got") before the expected result ("want"), and use `t.Error` over `t.Fatal` to keep tests running through multiple failures.

# Core Definition

This concept combines five closely related sub-guidelines for writing useful test failure messages. **Identify the function**: always include the function name in the failure message, even when it seems obvious from the test name. **Identify the input**: include the function inputs if they are short; for large or opaque inputs, name the test case and print the description. **Got before want**: print the actual value before the expected value using `YourFunc(%v) = %v, want %v`; use "got" and "want" (not "actual" and "expected"). **Keep going**: prefer `t.Error` over `t.Fatal` so the test continues reporting subsequent failures; use `t.Fatal` only when subsequent checks would be meaningless. **Level of detail**: the standard format suffices for most tests, but include more context for complex interactions, and less for setup failures.

# Prerequisites

- **Go testing package** -- Familiarity with `t.Errorf`, `t.Fatalf`, `t.Error`, `t.Fatal`
- **Test design basics** -- Understanding of what makes a test failure diagnosable

# Key Properties

1. **Function name in message**: `YourFunc(%v) = %v, want %v` not just `got %v, want %v`
2. **Input identification**: Include inputs in the message when they are short; use descriptive names otherwise
3. **Got before want**: Actual result first, then expected
4. **"got" and "want" terminology**: Not "actual" and "expected"
5. **Keep going with t.Error**: Use `t.Error` for most comparisons so the test reports all failures
6. **t.Fatal for dependencies**: Use `t.Fatal` only when subsequent checks depend on the failed one (e.g., decoding depends on encoding succeeding)
7. **Diff direction labeling**: For diffs, always include a key like `(-want +got)` to clarify direction
8. **Appropriate detail level**: More detail for complex interactions; less for setup failures

# Construction / Recognition

## To Apply:
1. Start failure messages with the function name: `YourFunc(%v) = %v, want %v`
2. Include inputs or a descriptive test case name
3. Put "got" before "want" in the message
4. Use `t.Errorf` for individual comparison failures
5. Use `t.Fatalf` only for errors that make subsequent checks meaningless
6. For diffs, label the direction: `(-want +got)`

## To Recognize:
1. Messages missing the function name: `got %v, want %v`
2. Messages with want before got: `want %v, got %v`
3. Using "expected" and "actual" instead of "want" and "got"
4. Tests that use `t.Fatal` for every comparison, hiding subsequent failures

# Context & Application

It should be possible to diagnose a test failure without reading the test source code. The failure message alone should tell you what function failed, what inputs it received, what it returned, and what was expected. Keeping tests running through multiple failures (via `t.Error`) lets developers see all broken checks in a single test run rather than fixing them one at a time.

# Examples

**Example 1 -- Standard failure message format**:

```go
if got != want {
    t.Errorf("YourFunc(%v) = %v, want %v", input, got, want)
}
```

**Example 2 -- Keep going with multiple checks**:

```go
// Good:
if diff := cmp.Diff(wantMean, gotMean); diff != "" {
    t.Errorf("MyDistribution(%v) mean (-want +got):\n%s", input, diff)
}
if diff := cmp.Diff(wantVariance, gotVariance); diff != "" {
    t.Errorf("MyDistribution(%v) variance (-want +got):\n%s", input, diff)
}
```

**Example 3 -- When t.Fatal is appropriate**:

```go
// Good:
gotEncoded := Encode(input)
if gotEncoded != wantEncoded {
    t.Fatalf("Encode(%q) = %q, want %q", input, gotEncoded, wantEncoded)
    // Decoding from unexpected encoded input would be meaningless.
}
gotDecoded, err := Decode(gotEncoded)
if err != nil {
    t.Fatalf("Decode(%q) returned unexpected error: %v", gotEncoded, err)
}
```

**Example 4 -- Setup failure (less detail is fine)**:

```go
t.Fatalf("Setup: Failed to set up test database: %s", err)
```

# Relationships

## Related
- **test-comparisons** -- How to perform the actual comparisons that feed into failure messages
- **assertion-libraries** -- Assertion libraries often produce poor failure messages, motivating these conventions
- **use-percent-q** -- Use `%q` for string values in failure messages to show boundaries

# Common Errors

- **Error**: Omitting the function name from the failure message
  **Correction**: Always include it: `YourFunc(%v) = %v, want %v`.

- **Error**: Using `t.Fatal` for every comparison
  **Correction**: Use `t.Error` so the test keeps running and reports all failures. Reserve `t.Fatal` for errors that make subsequent checks meaningless.

- **Error**: Printing want before got
  **Correction**: Convention is got first, then want: `= %v, want %v`.

# Common Confusions

- **Confusion**: Thinking `t.Fatal` is always better because it stops at the first failure
  **Clarification**: Stopping early means developers fix one issue, re-run, find the next. `t.Error` reveals all issues at once.

- **Confusion**: Thinking diff direction does not need labeling
  **Clarification**: Existing code is inconsistent about diff order, so always include a key like `(-want +got)`.

# Source Reference

Chapter 3: Style Decisions, Sections "Identify the function", "Identify the input", "Got before want", "Keep going", and "Level of detail" under "Useful test failures".

# Verification Notes

- Definition source: Synthesized from five subsections under "Useful test failures"
- Confidence rationale: HIGH -- all five subsections are explicit with clear examples
- Uncertainties: None
- Cross-reference status: Related slugs verified against planned extractions
