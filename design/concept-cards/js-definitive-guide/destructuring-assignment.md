---
# === CORE IDENTIFICATION ===
concept: Destructuring Assignment
slug: destructuring-assignment

# === CLASSIFICATION ===
category: language-fundamentals
subcategory: variables
tier: intermediate

# === PROVENANCE ===
source: "JavaScript: The Definitive Guide, 7th Edition"
source_slug: js-definitive-guide
authors: "David Flanagan"
chapter: "Types, Values, and Variables"
chapter_number: 3
pdf_page: 75
section: "3.10.3 Destructuring Assignment"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - array destructuring
  - object destructuring
  - destructured declaration

# === TYPED RELATIONSHIPS ===
prerequisites:
  - let-and-const-declarations
  - object-type-overview
extends: []
related:
  - nested-destructuring
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is destructuring assignment?"
  - "How do I destructure nested objects and arrays?"
---

# Quick Definition

Destructuring assignment is an ES6 syntax that extracts values from arrays or properties from objects into distinct variables using a syntax that mirrors array and object literal notation on the left side of an assignment.

# Core Definition

"ES6 implements a kind of compound declaration and assignment syntax known as destructuring assignment. In a destructuring assignment, the value on the righthand side of the equals sign is an array or object (a 'structured' value), and the lefthand side specifies one or more variable names using a syntax that mimics array and object literal syntax. When a destructuring assignment occurs, one or more values are extracted ('destructured') from the value on the right and stored into the variables named on the left." (p. 75)

# Prerequisites

- **let-and-const-declarations** — Destructuring works with let, const, and var
- **object-type-overview** — Must understand objects and arrays

# Key Properties

**Array destructuring:**
1. Variables on left in `[]` match positions on right
2. Extra variables get `undefined`; extra values are ignored
3. Commas skip positions: `[,x,,y] = [1,2,3,4]`
4. Rest syntax: `[x, ...y] = [1,2,3,4]` gives `y == [2,3,4]`
5. Works with any iterable, not just arrays
6. Supports nesting: `[a, [b, c]] = [1, [2,2.5], 3]`
7. Enables variable swapping: `[x,y] = [y,x]`

**Object destructuring:**
8. Variable names match property names: `{r, g, b} = color`
9. Rename syntax: `{cos: cosine} = Math`
10. Can destructure nested structures
11. Useful in for/of loops with `Object.entries()`

# Construction / Recognition

```javascript
// Array destructuring
let [x, y] = [1, 2];              // x=1, y=2
[x, y] = [y, x];                  // Swap values

// Object destructuring
let {r, g, b} = transparent;       // Extract named properties
const {sin, cos, tan} = Math;      // Extract Math functions

// With renaming
const {cos: cosine, tan: tangent} = Math;

// In loops
for (const [name, value] of Object.entries(o)) { ... }
```

# Context & Application

Destructuring is widely used in modern JavaScript for function return values, module imports, configuration objects, and React props. It makes code more concise and readable when working with structured data.

# Examples

From the source text (pp. 75-77):

Array destructuring:
```javascript
let [x,y] = [1,2];          // Same as let x=1, y=2
[x,y] = [x+1,y+1];         // Same as x = x+1, y = y+1
[x,y] = [y,x];              // Swap the value of the two variables

// With functions that return arrays
function toPolar(x, y) {
    return [Math.sqrt(x*x+y*y), Math.atan2(y,x)];
}
let [r,theta] = toPolar(1.0, 1.0);

// Skip values, rest syntax
let [x,y] = [1];             // x == 1; y == undefined
[,x,,y] = [1,2,3,4];         // x == 2; y == 4
let [x, ...y] = [1,2,3,4];   // y == [2,3,4]

// Destructuring strings
let [first, ...rest] = "Hello";  // first == "H"; rest == ["e","l","l","o"]
```

Object destructuring:
```javascript
let transparent = {r: 0.0, g: 0.0, b: 0.0, a: 1.0};
let {r, g, b} = transparent;     // r == 0.0; g == 0.0; b == 0.0

const {sin, cos, tan} = Math;    // Extract Math functions
const {cos: cosine, tan: tangent} = Math;  // With renaming

// In loops
let o = { x: 1, y: 2 };
for(const [name, value] of Object.entries(o)) {
    console.log(name, value);  // Prints "x 1" and "y 2"
}
```

# Relationships

## Builds Upon
- **let-and-const-declarations** — Used with let, const, and var
- **object-type-overview** — Destructures objects and arrays

## Enables
- **nested-destructuring** — Complex nested destructuring patterns
- Function parameter destructuring (covered in §8.3.5)

## Related
- **nested-destructuring** — Advanced destructuring of nested data

## Contrasts With
- Traditional property access: `let x = obj.x; let y = obj.y;`

# Common Errors

- **Error**: Confusing property names and variable names in object destructuring with renaming.
  **Correction**: In `{cos: cosine} = Math`, `cos` is the property name and `cosine` is the variable. "Property names are always on the left of the colon" (p. 77).

# Common Confusions

- **Confusion**: Object destructuring requires variable names to match property names.
  **Clarification**: You can rename with colon syntax: `{propertyName: variableName} = obj`.

# Source Reference

Chapter 3: Types, Values, and Variables, Section 3.10.3, pages 75-77.

# Verification Notes

- Definition source: Direct quote from p. 75
- Confidence rationale: High — comprehensive treatment with many examples
- Uncertainties: None
- Cross-reference status: Verified
