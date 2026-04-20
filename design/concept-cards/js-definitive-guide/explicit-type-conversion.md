---
# === CORE IDENTIFICATION ===
concept: Explicit Type Conversion
slug: explicit-type-conversion

# === CLASSIFICATION ===
category: type-system
subcategory: type-conversion
tier: intermediate

# === PROVENANCE ===
source: "JavaScript: The Definitive Guide, 7th Edition"
source_slug: js-definitive-guide
authors: "David Flanagan"
chapter: "Types, Values, and Variables"
chapter_number: 3
pdf_page: 64
section: "3.9.2 Explicit Conversions"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - type casting
  - manual type conversion

# === TYPED RELATIONSHIPS ===
prerequisites:
  - type-coercion
extends: []
related:
  - number-type
  - string-type
  - boolean-type
contrasts_with:
  - type-coercion

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is type coercion in JavaScript?"
---

# Quick Definition

Explicit type conversion uses functions like `Number()`, `String()`, `Boolean()`, `parseInt()`, and `parseFloat()` to deliberately convert values between types, along with methods like `toString()`, `toFixed()`, and `toPrecision()` for formatted output.

# Core Definition

"The simplest way to perform an explicit type conversion is to use the Boolean(), Number(), and String() functions." (p. 64) Operator-based idioms include: `x + ""` for String conversion, `+x` for Number conversion, `!!x` for Boolean conversion. For number-to-string formatting: `toString(radix)`, `toFixed()`, `toExponential()`, `toPrecision()`. For string-to-number: `parseInt()` and `parseFloat()` are "more flexible" than `Number()` — they "skip leading whitespace, parse as many numeric characters as they can, and ignore anything that follows." (pp. 64-66)

# Prerequisites

- **type-coercion** — Must understand implicit conversion to appreciate explicit conversion

# Key Properties

1. `Boolean(x)`, `Number(x)`, `String(x)` — basic conversion functions
2. `x + ""` — convert to string via concatenation
3. `+x` or `x - 0` — convert to number via unary operator
4. `!!x` — convert to boolean via double negation
5. `n.toString(radix)` — convert number to string in base 2-36
6. `n.toFixed(digits)` — fixed decimal places, no exponential notation
7. `n.toExponential(digits)` — exponential notation
8. `n.toPrecision(digits)` — specified significant digits
9. `parseInt(str, radix)` — parse integers, supports radix 2-36
10. `parseFloat(str)` — parse floating-point numbers
11. Both `parseInt` and `parseFloat` skip leading whitespace and ignore trailing non-numeric characters

# Construction / Recognition

```javascript
Number("3")            // => 3
String(false)          // => "false"
Boolean([])            // => true

+x                     // => Number(x)
x + ""                 // => String(x)
!!x                    // => Boolean(x)

parseInt("3 blind mice")    // => 3
parseFloat(" 3.14 meters")  // => 3.14
parseInt("0xff")            // => 255
parseInt("11", 2)           // => 3
```

# Context & Application

Explicit conversion is preferred over implicit coercion for code clarity. Use `Number()` for strict numeric parsing; use `parseInt()`/`parseFloat()` when you need to extract numbers from strings with trailing text.

# Examples

From the source text (pp. 64-66):
```javascript
Number("3")               // => 3
String(false)              // => "false": Or use false.toString()
Boolean([])                // => true

let n = 17;
let binary = "0b" + n.toString(2);     // binary == "0b10001"
let octal = "0o" + n.toString(8);      // octal == "0o21"
let hex = "0x" + n.toString(16);       // hex == "0x11"

let n = 123456.789;
n.toFixed(0)               // => "123457"
n.toFixed(2)               // => "123456.79"
n.toExponential(1)         // => "1.2e+5"
n.toPrecision(4)           // => "1.235e+5"

parseInt("3 blind mice")   // => 3
parseFloat(" 3.14 meters") // => 3.14
parseInt("-12.34")          // => -12
parseInt("0xFF")            // => 255
parseInt(".1")              // => NaN: integers can't start with "."
parseFloat("$72.47")       // => NaN: numbers can't start with "$"
parseInt("11", 2)           // => 3: (1*2 + 1)
parseInt("ff", 16)          // => 255: (15*16 + 15)
parseInt("077", 8)          // => 63: (7*8 + 7)
```

# Relationships

## Builds Upon
- **type-coercion** — Explicit conversion provides deliberate control over coercion

## Enables
- Formatted numeric output
- Robust string-to-number parsing

## Related
- **number-type** — Number conversion methods
- **string-type** — String conversion functions
- **boolean-type** — Boolean conversion

## Contrasts With
- **type-coercion** — Explicit conversion is deliberate; coercion is automatic

# Common Errors

- **Error**: Using `Number()` to parse strings like "3 blind mice".
  **Correction**: `Number("3 blind mice")` returns `NaN`. Use `parseInt("3 blind mice")` which returns `3`.

- **Error**: Forgetting the radix argument in `parseInt("077")`.
  **Correction**: Without a radix, leading `0` could be ambiguous. Always specify: `parseInt("077", 10)` for decimal.

# Common Confusions

- **Confusion**: `Boolean()`, `Number()`, `String()` and their `new` constructor forms are the same.
  **Clarification**: Without `new`, they are conversion functions. With `new`, they create wrapper objects — "a historical leftover" that should be avoided (p. 64).

# Source Reference

Chapter 3: Types, Values, and Variables, Section 3.9.2, pages 64-66.

# Verification Notes

- Definition source: Direct quotes from pp. 64-66
- Confidence rationale: High — thorough treatment with examples
- Uncertainties: None
- Cross-reference status: Verified
