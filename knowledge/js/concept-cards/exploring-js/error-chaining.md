---
concept: Error Chaining
slug: error-chaining
category: error-handling
subcategory: error-types
tier: intermediate
source: "Exploring JavaScript"
source_slug: exploring-js
authors: "Dr. Axel Rauschmayer"
chapter: "Exception handling"
chapter_number: 26
pdf_page: null
section: "26.5 Chaining errors: the instance property `.cause`"
extraction_confidence: high
aliases:
  - "error cause"
  - ".cause property"
prerequisites:
  - error-class
  - try-catch-finally
extends:
  - error-class
related:
  - error-subclasses
contrasts_with: []
answers_questions:
  - "How do I attach context to a caught error before re-throwing?"
---

# Quick Definition

Error chaining (ES2022) links a new error to the original error that caused it via the `.cause` property, preserving the full error context.

# Core Definition

As described in "Exploring JavaScript" Ch. 26, the `.cause` property is created via the options object in `new Error('msg', {cause: originalError})`. It specifies which other error caused the current one. This enables catching errors from deeply nested calls and attaching additional context before re-throwing. The cause is displayed properly by `util.inspect()` and console output.

# Prerequisites

- Error class
- Try-catch-finally

# Key Properties

1. Introduced in ES2022.
2. Set via `new Error(message, {cause: error})`.
3. `.cause` can hold any value, not just `Error` instances.
4. Displayed alongside the error in console output and `util.inspect()`.
5. Not visible when converting an error to a string or via `.stack`.

# Construction / Recognition

```js
try {
  riskyOperation();
} catch (error) {
  throw new Error('Context message', {cause: error});
}
```

# Context & Application

Used when catching errors at intermediate levels to add context (like which file was being processed) while preserving the original error and its stack trace.

# Examples

From the source text (Ch. 26, section 26.5.1):

```js
function readFiles(filePaths) {
  return filePaths.map((filePath) => {
    try {
      const text = readText(filePath);
      const json = JSON.parse(text);
      return processJson(json);
    } catch (error) {
      throw new Error(
        `While processing ${filePath}`,
        {cause: error}
      );
    }
  });
}
```

# Relationships

## Builds Upon
- **Error Class** -- uses the `options` parameter of the `Error` constructor

## Related
- **Error Subclasses** -- all subclasses support `{cause}` in their constructors

# Common Errors

- **Error**: Using `.cause` for non-error context data when error chaining is also needed.
  **Correction**: If you use `.cause` for context data, you can no longer chain exceptions. Consider adding custom properties instead.

# Common Confusions

- **Confusion**: Expecting `.cause` to appear in `error.stack` or `String(error)`.
  **Clarification**: `.cause` is only visible via `console.log()` or `util.inspect()`, not via `.stack` or string conversion.

# Source Reference

Chapter 26: Exception handling, Section 26.5, lines 460-568.

# Verification Notes

- Definition source: direct
- Confidence rationale: Explicit definition with practical examples
- Cross-reference status: verified
