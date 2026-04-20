---
# === CORE IDENTIFICATION ===
concept: break and continue Statements
slug: break-continue-statements

# === CLASSIFICATION ===
category: language-fundamentals
subcategory: statements
tier: foundational

# === PROVENANCE ===
source: "JavaScript: The Definitive Guide, 7th Edition"
source_slug: js-definitive-guide
authors: "David Flanagan"
chapter: "Statements"
chapter_number: 5
pdf_page: 131
section: "5.5.2 break, 5.5.3 continue"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases: []

# === TYPED RELATIONSHIPS ===
prerequisites:
  - for-loop
  - while-loop
  - labeled-statements
extends: []
related:
  - switch-case-statement
  - return-statement
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What must I understand before learning about closures? (scope, statements)"
---

# Quick Definition

`break` exits the innermost enclosing loop or switch statement (or a labeled statement). `continue` skips the rest of the current loop iteration and begins the next one.

# Core Definition

"The break statement, used alone, causes the innermost enclosing loop or switch statement to exit immediately." "The continue statement is similar to the break statement. Instead of exiting a loop, however, continue restarts a loop at the next iteration." Both can be used with labels to target outer loops. (Ch. 5, §5.5.2-5.5.3)

# Prerequisites

- **for-loop** — `break` and `continue` are used within loops.
- **while-loop** — `break` and `continue` are used within loops.
- **labeled-statements** — Labels allow targeting outer loops.

# Key Properties

1. `break` without a label exits the innermost loop or switch.
2. `break labelname` exits the labeled statement (can be any statement, not just loops).
3. `continue` without a label restarts the innermost loop.
4. `continue labelname` restarts the labeled loop.
5. `continue` behavior differs by loop type: in `while`, it jumps to the condition; in `for`, it evaluates the increment first.
6. No line break allowed between `break`/`continue` and a label (ASI).
7. `break` cannot transfer control across function boundaries.

# Construction / Recognition

```js
break;
break labelname;
continue;
continue labelname;
```

# Context & Application

`break` is used to exit a loop early when a condition is met. `continue` is used to skip processing of certain items (e.g., invalid data). The labeled forms are used in nested loops.

# Examples

From the source text (§5.5.2-5.5.3, pp. 131-133):

```js
// break: exit loop when target is found
for(let i = 0; i < a.length; i++) {
    if (a[i] === target) break;
}

// Labeled break: exit nested structure
computeSum: if (matrix) {
    for(let x = 0; x < matrix.length; x++) {
        let row = matrix[x];
        if (!row) break computeSum;
        for(let y = 0; y < row.length; y++) {
            let cell = row[y];
            if (isNaN(cell)) break computeSum;
            sum += cell;
        }
    }
    success = true;
}

// continue: skip invalid data
for(let i = 0; i < data.length; i++) {
    if (!data[i]) continue;
    total += data[i];
}
```

# Relationships

## Builds Upon
- **for-loop** — Primary context for `break` and `continue`
- **while-loop** — Also uses `break` and `continue`
- **labeled-statements** — Labels enable targeting outer loops

## Enables
- Early termination and selective iteration patterns

## Related
- **switch-case-statement** — `break` is essential for preventing fall-through in switch
- **return-statement** — Another jump statement that exits a function

## Contrasts With
- No direct contrast (break vs. continue complement each other)

# Common Errors

- **Error**: Inserting a line break between `break`/`continue` and a label.
  **Correction**: ASI will insert a semicolon, turning it into an unlabeled `break`/`continue`. Keep the label on the same line.

# Common Confusions

- **Confusion**: Expecting `continue` in a `for` loop to skip the increment expression.
  **Clarification**: In a `for` loop, `continue` evaluates the increment expression before re-testing the condition. In a `while` loop, `continue` jumps directly to the condition.

# Source Reference

Chapter 5: Statements, Sections 5.5.2-5.5.3, pages 131-133.

# Verification Notes

- Definition source: Direct quotes from §5.5.2 and §5.5.3
- Confidence rationale: High — detailed per-loop-type behavior explained
- Uncertainties: None
- Cross-reference status: Verified
