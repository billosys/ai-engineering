---
# === CORE IDENTIFICATION ===
concept: Dot Character
slug: dot-character

# === CLASSIFICATION ===
category: text-processing
subcategory: pattern-syntax
tier: intermediate

# === PROVENANCE ===
source: "Eloquent JavaScript, 4th Edition"
source_slug: eloquent-js
authors: "Marijn Haverbeke"
chapter: "Regular Expressions"
chapter_number: 9
pdf_page: null
section: "Sets of characters"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - wildcard character
  - period in regex

# === TYPED RELATIONSHIPS ===
prerequisites:
  - regular-expression
extends: []
related:
  - character-class
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What does the dot match in a regular expression?"
---

# Quick Definition
In a regular expression, the dot (`.`) matches any single character except a newline character.

# Core Definition
From the chapter's character class table: "`.` Any character except for newline" (Ch 9, "Sets of characters"). To match ANY character including newlines, use `[^]` (any character not in the empty set).

# Prerequisites
- **Regular expressions**: The dot is a regex metacharacter

# Key Properties
1. Matches any single character except `\n`
2. Inside square brackets `[...]`, the dot loses its special meaning
3. `[^]` can be used to match any character INCLUDING newlines
4. With the `u` flag, `.` correctly handles characters that take two code units

# Construction / Recognition
```javascript
/./ // matches any single non-newline character
```

# Context & Application
The dot is commonly used in patterns where the specific character doesn't matter, often combined with repetition operators.

# Examples
From the comment-stripping example, `[^]` is used instead of `.` to match any character including newlines:
```javascript
// [^] matches ANY character (including newline)
/\/\*[^]*?\*\//g  // matches block comments that span lines
```
"We use `[^]` (any character that is not in the empty set of characters) as a way to match any character. We cannot just use a period here because block comments can continue on a new line, and the period character does not match newline characters." (Ch 9, "Greed", lines 793-797)

# Relationships
## Builds Upon
- regular-expression
## Enables
- Wildcard matching in patterns
## Related
- character-class
## Contrasts With
- N/A

# Common Errors
- **Error**: Using `.` to match newlines
  **Correction**: Use `[^]` or enable the `s` (dotAll) flag to match any character including newlines

# Common Confusions
- **Confusion**: `.` matches literally everything
  **Clarification**: `.` does NOT match newline characters by default

# Source Reference
Chapter 9: Regular Expressions, Section "Sets of characters", line 155, and "Greed", lines 793-797.

# Verification Notes
- Definition source: direct
- Confidence rationale: Listed in character class table and discussed in examples
- Cross-reference status: verified
