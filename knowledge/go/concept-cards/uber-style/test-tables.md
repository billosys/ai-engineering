---
concept: Test Tables
slug: test-tables
category: patterns
subcategory: testing
tier: foundational
source: "Uber Go Style Guide"
source_slug: uber-style
authors: "Prashant Varanasi, Simon Newton"
chapter: "Patterns"
chapter_number: 5
pdf_page: null
section: "Test Tables"
extraction_confidence: high
aliases:
  - table-driven tests
  - table tests
prerequisites: []
extends: []
related:
  - initializing-structs
contrasts_with: []
answers_questions:
  - "What is a table-driven test?"
  - "How do I write a table-driven test with subtests?"
  - "When should I avoid table-driven tests?"
---

# Quick Definition

Table-driven tests use a slice of test case structs iterated with subtests (`t.Run`) to avoid duplicating test logic. Use them when testing multiple conditions with the same core logic, but avoid them when subtests require complex branching or conditional assertions.

# Core Definition

The Uber Go Style Guide recommends table-driven tests with subtests as a pattern for testing a system against multiple conditions where inputs and outputs vary but the core test logic remains the same. The pattern uses a slice of anonymous structs (conventionally named `tests`) iterated with `range`, running each case as a subtest via `t.Run`.

The guide also warns against unnecessary complexity: table tests should not be used when subtests require conditional assertions, complex mock setup, or multiple branching pathways. In those cases, separate test functions are preferred.

# Prerequisites

- Understanding of Go's `testing` package and `t.Run` for subtests
- Familiarity with anonymous struct slices

# Key Properties

1. **Convention**: The slice is named `tests`, each case is `tt`, inputs use `give` prefix, outputs use `want` prefix.
2. **Subtests with `t.Run`**: Each test case runs as a named subtest for clear failure reporting.
3. **Avoid complexity**: Do not use table tests when subtests need conditional logic, complex mock setup, or branching paths like `shouldCallX`.
4. **Shallow test depth**: Aim for minimal successive assertions that depend on previous assertions holding.
5. **All fields used in all tests**: Every table field should be used by every test case.
6. **Parallel tests**: When using `t.Parallel()`, loop variables must be explicitly captured to avoid race conditions.

# Construction / Recognition

**Good -- table-driven test with subtests:**

```go
// func TestSplitHostPort(t *testing.T)

tests := []struct{
  give     string
  wantHost string
  wantPort string
}{
  {
    give:     "192.0.2.0:8000",
    wantHost: "192.0.2.0",
    wantPort: "8000",
  },
  {
    give:     "192.0.2.0:http",
    wantHost: "192.0.2.0",
    wantPort: "http",
  },
  {
    give:     ":8000",
    wantHost: "",
    wantPort: "8000",
  },
  {
    give:     "1:8",
    wantHost: "1",
    wantPort: "8",
  },
}

for _, tt := range tests {
  t.Run(tt.give, func(t *testing.T) {
    host, port, err := net.SplitHostPort(tt.give)
    require.NoError(t, err)
    assert.Equal(t, tt.wantHost, host)
    assert.Equal(t, tt.wantPort, port)
  })
}
```

**Bad -- duplicated test logic without table:**

```go
host, port, err := net.SplitHostPort("192.0.2.0:8000")
require.NoError(t, err)
assert.Equal(t, "192.0.2.0", host)
assert.Equal(t, "8000", port)

host, port, err = net.SplitHostPort("192.0.2.0:http")
require.NoError(t, err)
assert.Equal(t, "192.0.2.0", host)
assert.Equal(t, "http", port)
// ... repeated for each case
```

**Bad -- overly complex table test (use separate functions instead):**

```go
func TestComplicatedTable(t *testing.T) {
  tests := []struct {
    give          string
    want          string
    wantErr       error
    shouldCallX   bool
    shouldCallY   bool
    giveXResponse string
    giveXErr      error
    giveYResponse string
    giveYErr      error
  }{
    // ...
  }

  for _, tt := range tests {
    t.Run(tt.give, func(t *testing.T) {
      // complex conditional mock setup
      ctrl := gomock.NewController(t)
      xMock := xmock.NewMockX(ctrl)
      if tt.shouldCallX {
        xMock.EXPECT().Call().Return(
          tt.giveXResponse, tt.giveXErr,
        )
      }
      // ... more branching
    })
  }
}
```

**Good -- separate functions for complex cases:**

```go
func TestShouldCallX(t *testing.T) {
  ctrl := gomock.NewController(t)
  xMock := xmock.NewMockX(ctrl)
  xMock.EXPECT().Call().Return("XResponse", nil)

  yMock := ymock.NewMockY(ctrl)

  got, err := DoComplexThing("inputX", xMock, yMock)

  require.NoError(t, err)
  assert.Equal(t, "want", got)
}

func TestShouldCallYAndFail(t *testing.T) {
  ctrl := gomock.NewController(t)
  xMock := xmock.NewMockX(ctrl)

  yMock := ymock.NewMockY(ctrl)
  yMock.EXPECT().Call().Return("YResponse", nil)

  _, err := DoComplexThing("inputY", xMock, yMock)
  assert.EqualError(t, err, "Y failed")
}
```

# Context & Application

Table-driven tests are one of Go's most recognizable patterns. They work best when the test logic is uniform across cases and differs only in inputs and expected outputs. The guide emphasizes that readability and maintainability should always be the deciding factor when choosing between table tests and separate test functions.

A simple `shouldErr` branching pathway is acceptable when the test body is short and straightforward.

# Examples

**Parallel table test:**

```go
tests := []struct{
  give string
  // ...
}{
  // ...
}

for _, tt := range tests {
  t.Run(tt.give, func(t *testing.T) {
    t.Parallel()
    // ...
  })
}
```

# Relationships

- **initializing-structs**: Test table structs follow the same initialization conventions (field names, zero-value handling).

# Common Errors

1. Adding complex conditional logic inside the `for` loop -- split into separate test functions instead.
2. Having table fields that are only used by some test cases -- every field should be used by every case.
3. Not using `t.Run` for subtests -- losing the ability to run individual cases and see clear failure output.
4. Forgetting to capture loop variables when using `t.Parallel()`.

# Common Confusions

- **When to use table tests vs separate functions**: Use table tests when core logic is the same across cases. Use separate functions when cases require different setup, mock configurations, or assertion paths.
- **`give` / `want` vs `input` / `expected`**: The Uber convention uses `give` and `want` prefixes. Other codebases may use different conventions; consistency within a codebase matters most.

# Source Reference

Uber Go Style Guide, "Patterns" chapter, "Test Tables" section (including sub-sections: "Avoid Unnecessary Complexity in Table Tests," "Parallel Tests").

# Verification Notes

Confidence: high. The pattern definition, conventions, complexity warnings, and all code examples are directly from the source text.
