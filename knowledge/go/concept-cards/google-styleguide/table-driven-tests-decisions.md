---
# === CORE IDENTIFICATION ===
concept: Table-Driven Tests
slug: table-driven-tests-decisions

# === CLASSIFICATION ===
category: testing
subcategory: test-patterns
tier: intermediate

# === PROVENANCE ===
source: "Google Go Style Guide"
source_slug: google-styleguide
authors: "Google Go Style Team"
chapter: "Style Decisions"
chapter_number: 3
pdf_page: null
section: "Table-driven tests"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "table tests"
  - "data-driven tests"
  - "parameterized tests in Go"

# === TYPED RELATIONSHIPS ===
prerequisites: []
extends: []
related:
  - subtests
  - test-failure-messages
  - test-helpers-decisions
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "When should I use table-driven tests in Go?"
  - "When should I use separate test functions instead of tables?"
  - "How do I handle different test logic in table-driven tests?"
  - "How should I identify rows in table-driven tests?"
  - "What makes a table test too complex?"
---

# Quick Definition

Use table-driven tests when many cases share similar testing logic. Avoid complexity in the loop body -- when cases need different logic, split into separate test functions or use disjoint tables. Never use row index as identification; always name rows descriptively.

# Core Definition

Table-driven tests use a slice of test case structs iterated in a loop, suitable when testing whether output matches expectations or outputs conform to invariants. The minimal structure is a struct with inputs, expected outputs, and a loop that calls the function under test and compares results. When test cases require different logic (conditional branches in the loop body), split them into separate test functions or use disjoint tables (GoTip #50). Avoid complexity that makes the loop body hard to understand. Data-driven test cases should keep conditional behavior out of the loop; if different setups are needed, write separate test functions with shared test case types. Always name test rows descriptively -- never identify them by index number.

# Prerequisites

- **Go testing basics** -- `t.Errorf`, `t.Fatalf`, struct literals
- **subtests** -- `t.Run` for naming individual table entries

# Key Properties

1. **When to use**: Many cases sharing similar testing logic (output equality or invariant checking)
2. **When to split**: Cases requiring different logic should use separate test functions
3. **No conditional complexity**: Avoid branches in the loop body based on test input parameters
4. **Named rows**: Always include a name or description field; never identify by index
5. **Disjoint tables**: Use GoTip #50 pattern when some cases need different checking logic
6. **Combine tables and functions**: You can have multiple table-driven test functions, e.g., one for valid outputs, one for error cases
7. **Simple error cases**: Basic error checking can stay in the same table if it does not add conditional flow

# Construction / Recognition

## To Apply:
1. Define a struct with input fields, expected output fields, and a `name` field
2. Create a slice of test cases
3. Iterate with `for _, test := range tests`
4. Use `t.Run(test.name, ...)` for subtest naming
5. Keep the loop body simple and uniform
6. Split into multiple functions when logic diverges

## To Recognize:
1. Loop bodies with `switch` or `if` on test case fields to change validation logic
2. Tests identified by `case #%d` index
3. Table entries with many conditional fields that control test flow

# Context & Application

Table-driven tests are a Go idiom that reduces boilerplate when testing many similar cases. However, they should not be forced onto tests with divergent logic. The key trade-off is between reducing duplication (good) and making the loop body complex and hard to understand (bad). When complexity creeps in, splitting into separate functions preserves readability while maintaining the table-driven pattern where it fits.

# Examples

**Example 1 -- Minimal table-driven test**:

```go
func TestCompare(t *testing.T) {
    tests := []struct {
        a, b string
        want int
    }{
        {"", "", 0},
        {"a", "", 1},
        {"", "a", -1},
        {"abc", "abc", 0},
    }
    for _, test := range tests {
        got := Compare(test.a, test.b)
        if got != test.want {
            t.Errorf("Compare(%q, %q) = %v, want %v", test.a, test.b, got, test.want)
        }
    }
}
```

**Example 2 -- Table with simple error checking**:

```go
func TestDivide(t *testing.T) {
    tests := []struct {
        dividend, divisor, want int
        wantErr                 bool
    }{
        {dividend: 4, divisor: 2, want: 2},
        {dividend: 1, divisor: 0, wantErr: true},
    }
    for _, test := range tests {
        got, err := Divide(test.dividend, test.divisor)
        if (err != nil) != test.wantErr {
            t.Errorf("Divide(%d, %d) error = %v, want error presence = %t",
                test.dividend, test.divisor, err, test.wantErr)
        }
        if err != nil {
            continue
        }
        if got != test.want {
            t.Errorf("Divide(%d, %d) = %d, want %d",
                test.dividend, test.divisor, got, test.want)
        }
    }
}
```

**Example 3 -- Anti-pattern: row identified by index**:

```go
// Bad:
for i, d := range tests {
    if strings.ToUpper(d.input) != d.want {
        t.Errorf("Failed on case #%d", i)
    }
}
```

# Relationships

## Related
- **subtests** -- `t.Run` provides naming and scoping for each table row
- **test-failure-messages** -- Each table row failure must identify the function, inputs, got, and want
- **test-helpers-decisions** -- Helpers can simplify setup to keep table test bodies readable

# Common Errors

- **Error**: Using index numbers to identify test rows
  **Correction**: Add a `name` field to the struct and use `t.Run(test.name, ...)`.

- **Error**: Adding complex conditional logic in the table test loop
  **Correction**: Split into separate test functions or use disjoint table tests (GoTip #50).

# Common Confusions

- **Confusion**: Thinking all related test cases must go in one table
  **Clarification**: It is perfectly fine to have multiple table-driven test functions. Split by the type of checking needed (e.g., normal output vs error cases).

- **Confusion**: Thinking table-driven tests are always better than individual tests
  **Clarification**: When cases have substantially different logic, separate test functions are clearer.

# Source Reference

Chapter 3: Style Decisions, Sections "Table-driven tests", "Data-driven test cases", and "Identifying the row" under "Test structure".

# Verification Notes

- Definition source: Directly from the "Table-driven tests" section and its subsections
- Confidence rationale: HIGH -- detailed guidance with multiple examples and anti-patterns
- Uncertainties: None
- Cross-reference status: References GoTip #50 on disjoint table tests
