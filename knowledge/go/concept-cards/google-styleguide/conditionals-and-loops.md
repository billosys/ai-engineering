---
concept: Conditionals and Loops
slug: conditionals-and-loops
category: language
subcategory: code-formatting
tier: intermediate
source: "Google Go Style Guide"
source_slug: google-styleguide
authors: "Google Go Style Team"
chapter: "Style Decisions"
chapter_number: 3
pdf_page: null
section: "Conditionals and loops"
extraction_confidence: high
aliases:
  - if statement formatting
  - switch formatting
  - loop formatting
prerequisites:
  - go-control-flow-basics
related:
  - indent-error-flow
  - function-formatting
  - switch-and-break
contrasts_with: []
answers_questions:
  - "Should Go if statements be broken across multiple lines?"
  - "How should long switch cases be formatted in Go?"
  - "Should variables be on the left or right of comparisons in Go?"
  - "How should long for loop conditions be handled?"
---

# Quick Definition

Do not break `if` statements across multiple lines; extract boolean operands into local variables instead. Keep `switch`/`case` statements on single lines. Let long `for` loops be long, or refactor conditions into the body. Place variables on the left side of comparisons (no "Yoda conditions").

# Core Definition

> "An `if` statement should not be line broken; multi-line `if` clauses can lead to indentation confusion." -- Google Go Style Guide, "Conditionals and loops"

> "`switch` and `case` statements should also remain on a single line." -- Google Go Style Guide, "Conditionals and loops"

> "In conditionals comparing a variable to a constant, place the variable value on the left hand side of the equality operator." -- Google Go Style Guide, "Conditionals and loops"

# Prerequisites

- Understanding of Go `if`, `switch`, and `for` statements
- Familiarity with indentation confusion risks

# Key Properties

1. **No multi-line if**: Do not break `if` conditions across lines; extract complex conditions into local variables.
2. **Extract boolean operands**: Factor repeated sub-expressions into named locals for clarity.
3. **Single-line switch/case**: Keep case clauses on one line; if too long, indent all cases and separate with blank lines.
4. **No Yoda conditions**: Write `result == "foo"`, not `"foo" == result`.
5. **Long for loops are okay**: Let long `for` lines stay long, or move conditions into the loop body.
6. **Closures in if**: When `if` contains closures or multi-line struct literals, ensure braces match properly.

# Construction / Recognition

**Bad -- multi-line if causes indentation confusion:**

```go
if db.CurrentStatusIs(db.InTransaction) &&
    db.ValuesEqual(db.TransactionKey(), row.Key()) {
    return db.Errorf(db.TransactionError, "query failed: row (%v): key does not match transaction key", row)
}
```

**Good -- extract into local variables:**

```go
inTransaction := db.CurrentStatusIs(db.InTransaction)
keysMatch := db.ValuesEqual(db.TransactionKey(), row.Key())
if inTransaction && keysMatch {
    return db.Error(db.TransactionError, "query failed: row (%v): key does not match transaction key", row)
}
```

**Good -- extract repeated sub-expression:**

```go
uid := user.GetUniqueUserID()
if db.UserIsAdmin(uid) || db.UserHasPermission(uid, perms.ViewServerConfig) || db.UserHasPermission(uid, perms.CreateGroup) {
    // ...
}
```

**Good -- switch/case on single lines:**

```go
switch good := db.TransactionStatus(); good {
case db.TransactionStarting, db.TransactionActive, db.TransactionWaiting:
    // ...
case db.TransactionCommitted, db.NoTransaction:
    // ...
default:
    // ...
}
```

**Good -- excessively long cases indented with blank line separator:**

```go
switch db.TransactionStatus() {
case
    db.TransactionStarting,
    db.TransactionActive,
    db.TransactionWaiting,
    db.TransactionCommitted:

    // ...
case db.NoTransaction:
    // ...
default:
    // ...
}
```

**Good -- no Yoda conditions:**

```go
if result == "foo" {
    // ...
}
```

**Bad -- Yoda condition:**

```go
if "foo" == result {
    // ...
}
```

**Good -- closure in if with matching braces:**

```go
if err := db.RunInTransaction(func(tx *db.TX) error {
    return tx.Execute(userUpdate, x, y, z)
}); err != nil {
    return fmt.Errorf("user update failed: %s", err)
}
```

# Context & Application

Multi-line `if` conditions create indentation confusion because the wrapped condition aligns with the body of the `if` block, making it hard to see where the condition ends and the body begins. Extracting conditions into named variables simultaneously fixes the formatting problem and improves readability by giving names to the concepts being tested.

# Examples

See Construction / Recognition above for the complete set of source examples.

# Relationships

- **indent-error-flow**: The complementary pattern for structuring error-first conditionals.
- **function-formatting**: Shares the same indentation-confusion concern.
- **switch-and-break**: Related guidance on break behavior in switch statements.

# Common Errors

1. Breaking `if` conditions across multiple lines.
2. Splitting `case` clauses across lines when they could stay on one.
3. Using Yoda conditions (`"foo" == result`).
4. Repeating complex sub-expressions instead of extracting them.

# Common Confusions

- **Long lines are acceptable**: A long single-line `if` or `for` is better than a multi-line one that causes indentation confusion.
- **When to break case clauses**: Only when they are excessively long, and then all cases should be indented with blank-line separators.

# Source Reference

Google Go Style Guide, "Style Decisions" chapter, "Conditionals and loops" section.

# Verification Notes

Confidence: high. All guidance and code examples are directly from the source text.
