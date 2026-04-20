---
concept: Sending Values to Generators
slug: sending-values-to-generators
category: iterators-generators
subcategory: generators
tier: advanced
source: "JavaScript: The Definitive Guide, 7th Edition"
source_slug: js-definitive-guide
authors: "David Flanagan"
chapter: "Iterators and Generators"
chapter_number: 12
pdf_page: 354
section: "12.4.2 The Value of a yield Expression"
extraction_confidence: high
aliases:
  - "bidirectional generators"
  - "yield expression value"
prerequisites:
  - generator-functions
  - yield-keyword
extends: []
related:
  - generator-return-throw
contrasts_with: []
answers_questions: []
---

# Quick Definition

The ability to pass values into a running generator via `next(value)`, where the argument becomes the value of the `yield` expression that was previously paused, enabling bidirectional communication between generator and caller.

# Core Definition

"When the next() method of a generator is invoked, the generator function runs until it reaches a yield expression... The next time the next() method of the generator is called, the argument passed to next() becomes the value of the yield expression that was paused" (p. 354). The first `next()` argument is always discarded since there is no paused yield to receive it.

# Prerequisites

- **generator-functions** — Sending values requires a generator
- **yield-keyword** — yield as an expression receives the sent value

# Key Properties

1. `next(value)` makes `value` the result of the paused `yield` expression
2. The first `next()` call's argument is discarded (no yield is paused yet)
3. Enables two-way communication: generator yields out, caller sends in
4. The generator and caller are "two separate streams of execution passing values back and forth"

# Construction / Recognition

```js
function* smallNumbers() {
    let y1 = yield 1;    // y1 == "b"
    let y2 = yield 2;    // y2 == "c"
    return 4;
}
let g = smallNumbers();
let n1 = g.next("a");  // n1.value == 1, "a" is discarded
let n2 = g.next("b");  // n2.value == 2, y1 = "b"
let n3 = g.next("c");  // n3.value == 3, y2 = "c"
```

# Context & Application

Used for coroutine-like patterns where the generator and caller need to exchange data. Was previously used to manage async flows (before async/await).

# Examples

From the source text (p. 354-355): The `smallNumbers()` example demonstrates the asymmetry: `g.next("a")` starts the generator (argument discarded), yielding 1. `g.next("b")` resumes, making y1="b", yielding 2. `g.next("c")` resumes, making y2="c", yielding 3.

# Relationships

## Builds Upon
- **Generator Functions** — Values are sent into generators
- **Yield Keyword** — yield receives the sent value

## Related
- **Generator return/throw** — Other ways to send signals into generators

# Common Errors

- **Error**: Expecting the first `next()` argument to be received by the generator.
  **Correction**: The first `next()` call starts the generator; its argument is discarded because no yield is paused to receive it.

# Common Confusions

- **Confusion**: Thinking yield and next() are symmetric.
  **Clarification**: There is an inherent asymmetry: the first `next()` starts the generator without a receiving yield, and the last `next()` call receives the return value but cannot send anything useful.

# Source Reference

Chapter 12: Iterators and Generators, Section 12.4.2, pages 354-355.

# Verification Notes

- Definition source: Direct from source text
- Confidence rationale: High
- Uncertainties: None
- Cross-reference status: Verified
