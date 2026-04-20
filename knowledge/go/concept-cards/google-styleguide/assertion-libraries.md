---
# === CORE IDENTIFICATION ===
concept: Avoid Assertion Libraries
slug: assertion-libraries

# === CLASSIFICATION ===
category: testing
subcategory: test-design
tier: intermediate

# === PROVENANCE ===
source: "Google Go Style Guide"
source_slug: google-styleguide
authors: "Google Go Style Team"
chapter: "Style Decisions"
chapter_number: 3
pdf_page: null
section: "Assertion libraries"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "assert libraries"
  - "test assertions"
  - "assertion helpers"

# === TYPED RELATIONSHIPS ===
prerequisites: []
extends: []
related:
  - test-failure-messages
  - test-comparisons
  - use-package-testing
  - test-helpers-decisions
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "Should I use assertion libraries in Go tests?"
  - "Why does Google discourage Go assertion libraries?"
  - "What should I use instead of assert libraries in Go?"
  - "How do I compare structs in tests without assertions?"
---

# Quick Definition

Do not create or use assertion libraries for testing. Use standard Go comparisons with `cmp` and `fmt` instead. For domain-specific helpers, prefer returning values or errors rather than passing `*testing.T` and calling its error reporting methods.

# Core Definition

Assertion libraries attempt to combine validation and failure message production but tend to either stop tests early (via `t.Fatalf` or `panic`) or omit relevant information about what the test got right. Complex assertion functions often do not provide useful failure messages and the context that exists within the test function. Multiple assertion libraries fragment the developer experience, creating confusion about which library to use and what output format to expect. Instead, use Go itself: standard comparisons with `cmp.Equal`, `cmp.Diff`, and `fmt` formatting. For domain-specific comparison helpers, prefer returning a value or error that can be used in the test's failure message.

# Prerequisites

- **Go testing package** -- Familiarity with `t.Errorf`, `t.Fatalf`, `t.Error`, `t.Fatal`
- **cmp package** -- Understanding of `cmp.Equal` and `cmp.Diff` for structural comparison

# Key Properties

1. **No assertion libraries**: Do not create helpers that combine validation with failure message production
2. **Use cmp and fmt**: Standard libraries for comparison and formatting
3. **Return values, not test failures**: Domain-specific helpers should return values or errors, not call `t.Errorf`
4. **Full context**: Test failure messages should include context that only the test function knows
5. **No fragmentation**: Avoid multiple assertion styles that create inconsistent developer experiences

# Construction / Recognition

## To Apply:
1. Write comparisons directly in test functions using `if` statements
2. Use `cmp.Equal` for structural equality checks
3. Format failure messages with `t.Errorf` using the full context
4. Extract comparison logic into functions that return values, not into assertion helpers

## To Recognize:
1. Code importing `assert` or `require` packages from third-party libraries
2. Helper functions that take `*testing.T` and call `t.Fatalf` for comparisons
3. Custom `assert.Equal`, `assert.IsNotNil`, etc. patterns

# Context & Application

Go's testing philosophy favors explicit, readable test code over DSLs. Assertion libraries create a testing sub-language that obscures what the test actually checks. By keeping comparisons in plain Go, test failures are easier to understand, tests are easier to maintain, and large-scale refactorings are simpler because there is one consistent pattern.

# Examples

**Example 1 -- Anti-pattern with assertion library**:

```go
// Bad:
assert.IsNotNil(t, "obj", obj)
assert.StringEq(t, "obj.Type", obj.Type, "blogPost")
assert.IntEq(t, "obj.Comments", obj.Comments, 2)
```

**Example 2 -- Correct approach with cmp**:

```go
// Good:
want := BlogPost{Comments: 2, Body: "Hello, world!"}
if !cmp.Equal(got, want) {
    t.Errorf("Blog post = %v, want = %v", got, want)
}
```

**Example 3 -- Domain helper returning a value**:

```go
// Good:
func postLength(p BlogPost) int { return len(p.Body) }

func TestBlogPost_VeritableRant(t *testing.T) {
    post := BlogPost{Body: "I am Gunnery Sergeant Hartman..."}
    if got, want := postLength(post), 60; got != want {
        t.Errorf("Length of post = %v, want %v", got, want)
    }
}
```

# Relationships

## Related
- **test-failure-messages** -- Assertion libraries often produce poor failure messages
- **test-comparisons** -- The cmp package is the preferred alternative to assertion libraries
- **use-package-testing** -- The standard testing package is the only permitted framework
- **test-helpers-decisions** -- Test helpers differ from assertion libraries in purpose and design

# Common Errors

- **Error**: Creating assert helpers that call `t.Fatalf` on every comparison
  **Correction**: This stops the test early, hiding subsequent failures. Use `t.Errorf` in the test itself.

- **Error**: Building domain-specific assertion DSLs
  **Correction**: Use plain Go comparisons; they are clearer and more maintainable.

# Common Confusions

- **Confusion**: Thinking test helpers and assertion libraries are the same thing
  **Clarification**: Test helpers perform setup/cleanup and are marked with `t.Helper()`. Assertion libraries combine validation with failure reporting, which is the anti-pattern.

# Source Reference

Chapter 3: Style Decisions, Section "Assertion libraries" under "Useful test failures".

# Verification Notes

- Definition source: Directly from the "Assertion libraries" section
- Confidence rationale: HIGH -- the guidance is explicit with detailed examples and rationale
- Uncertainties: None
- Cross-reference status: References best practices on test functions and Go FAQ on testing frameworks
