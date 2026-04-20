---
concept: Extracting Methods
slug: extracting-methods
category: objects
subcategory: methods
tier: intermediate
source: "Exploring JavaScript"
source_slug: exploring-js
authors: "Dr. Axel Rauschmayer"
chapter: "Objects"
chapter_number: 30
pdf_page: null
section: "30.6.5 `this` pitfall: extracting methods"
extraction_confidence: high
aliases:
  - "method extraction pitfall"
prerequisites:
  - this-keyword
  - function-bind-method
extends: []
related:
  - method-definition
contrasts_with: []
answers_questions:
  - "Why does my method lose `this` when passed as a callback?"
---

# Quick Definition

Extracting a method (storing it in a variable or passing it as a callback) disconnects it from its receiver, causing `this` to become `undefined` -- a pitfall that must be fixed with `.bind()` or an arrow wrapper.

# Core Definition

As described in "Exploring JavaScript" Ch. 30, function-calling a method extracted from an object fails because the extracted function has no receiver, so `this` is `undefined` (in strict mode). Fixes: use `.bind(obj)` to create a permanently bound copy, or use an arrow function wrapper `() => obj.method()`.

# Prerequisites

- The `this` keyword
- Function.prototype.bind()

# Key Properties

1. Extracting: `const func = obj.method;` disconnects from receiver.
2. `func()` has `this === undefined` in strict mode.
3. Fix with `.bind()`: `const func = obj.method.bind(obj)`.
4. Fix with arrow: `const func = (...args) => obj.method(...args)`.
5. Each `.bind()` creates a new function object.

# Construction / Recognition

```js
// Pitfall
const func = jane.says; // extracted
func('hello'); // TypeError: Cannot read 'first' of undefined

// Fix
const func = jane.says.bind(jane);
func('hello'); // works
```

# Context & Application

Common in event handlers, callbacks, and any place a method is passed as a value.

# Examples

From the source text (Ch. 30, section 30.6.5.1):

```js
class ClickHandler {
  constructor(id, elem) {
    this.id = id;
    // Wrong:
    elem.addEventListener('click', this.handleClick);
    // Right:
    const listener = this.handleClick.bind(this);
    elem.addEventListener('click', listener);
  }
  handleClick(event) { alert('Clicked ' + this.id); }
}
```

# Relationships

## Builds Upon
- **The this Keyword** -- understanding dynamic `this` is essential
- **Function.prototype.bind()** -- primary fix for the pitfall

# Common Errors

- **Error**: Passing `this.method` directly as a callback.
  **Correction**: Always bind or wrap methods before passing them as callbacks.

# Source Reference

Chapter 30: Objects, Section 30.6.5, lines 1305-1418.

# Verification Notes

- Definition source: direct
- Confidence rationale: Detailed pitfall with multiple solutions
- Cross-reference status: verified
