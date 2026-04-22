---
# === CORE IDENTIFICATION ===
concept: Easy Doc Initialization
slug: easy-doc-initialization

# === CLASSIFICATION ===
category: idiom
subcategory: documentation
tier: intermediate

# === PROVENANCE ===
source: "Rust Design Patterns"
source_slug: design-patterns
authors: "The Rust Community"
chapter: "01-idioms"
chapter_number: 1
pdf_page: null
section: "Easy doc initialization"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "doc example helper"
  - "rustdoc boilerplate reduction"
  - "doc test initialization"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - rustdoc-basics
extends: []
related:
  - doc-hidden
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do I reduce boilerplate in rustdoc examples for types with complex initialization?"
  - "How can I avoid repeating setup code in every doc example for a struct?"
  - "What is the trade-off of using helper functions in doc tests?"
---

# Quick Definition

When a struct requires complex initialization, wrap doc examples in a helper function that takes the struct as an argument. This eliminates repeated boilerplate across examples. The trade-off is that code inside the helper function is only compiled, not executed, during `cargo test` -- so assertions inside it will not be checked.

# Core Definition

> "If a struct takes significant effort to initialize when writing docs, it can be quicker to wrap your example with a helper function which takes the struct as an argument." -- Rust Design Patterns, "Easy doc initialization"

The pattern uses `# fn call_example(connection: Connection, request: Request) {` (with the `#` prefix to hide it in rendered docs) to wrap the example body. This means each method's doc example only shows the interesting code, not the setup. The cost is that the inner code is never invoked at test time -- it only compiles.

# Prerequisites

- Understanding of rustdoc conventions and doc tests
- Familiarity with the `#` prefix in doc examples (hides lines from rendered output)

# Key Properties

1. **Eliminates repeated boilerplate**: Setup code appears once in the hidden helper, not in every example.
2. **Compile-checked only**: The helper function is never called, so assertions inside do not execute.
3. **Removes need for no_run**: Since the function is never called, the example does not need `no_run`.
4. **Hidden with # prefix**: The `# fn ...` line is hidden in rendered docs but present in the test.
5. **Alternative with #[doc(hidden)]**: For examples needing assertions, create a public `#[doc(hidden)]` helper method that can be called from doc tests.

# Construction / Recognition

## To Apply:
1. Identify a struct with complex initialization used across multiple doc examples
2. In each doc example, wrap the interesting code in a hidden helper function: `# fn helper(val: MyStruct) {`
3. The helper takes the complex-to-initialize types as parameters
4. Close the helper at the end of the example: `# }`

## To Recognize:
- Doc examples with `# fn` wrapper functions
- Parameters that would otherwise require multi-line setup
- Doc examples that compile but whose assertions are not exercised

# Context & Application

When a type like a network `Connection` requires establishing a TCP stream and filling in multiple fields just to demonstrate a method call, repeating that setup in every doc example is verbose and error-prone. This pattern moves the ceremony out of sight. However, if you need assertions to actually run, consider the `#[doc(hidden)]` alternative where a public-but-hidden helper method creates test instances.

# Examples

**Bad -- repeated boilerplate in every doc example:**

```rust,ignore
impl Connection {
    /// Sends a request over the connection.
    ///
    /// # Example
    /// ```no_run
    /// # let stream = TcpStream::connect("127.0.0.1:34254");
    /// # let connection = Connection { name: "foo".to_owned(), stream };
    /// # let request = Request::new("RequestId", RequestType::Get, "payload");
    /// let response = connection.send_request(request);
    /// assert!(response.is_ok());
    /// ```
    fn send_request(&self, request: Request) -> Result<Status, SendErr> {
        // ...
    }
}
```

**Good -- helper function eliminates boilerplate:**

```rust,ignore
impl Connection {
    /// Sends a request over the connection.
    ///
    /// # Example
    /// ```
    /// # fn call_send(connection: Connection, request: Request) {
    /// let response = connection.send_request(request);
    /// assert!(response.is_ok());
    /// # }
    /// ```
    fn send_request(&self, request: Request) -> Result<Status, SendErr> {
        // ...
    }
}
```

# Relationships

## Related
- **doc-hidden** -- `#[doc(hidden)]` helper methods can provide testable initialization when assertions must execute

# Common Errors

- **Error**: Expecting assertions inside the helper function to execute during `cargo test`
  **Correction**: The helper function is never called; assertions are only compiled, not run

- **Error**: Adding `no_run` when using the helper function pattern
  **Correction**: `no_run` is unnecessary since the function is never invoked

# Common Confusions

- **Confusion**: Thinking the example code is fully tested
  **Clarification**: Only compilation is verified; to test assertions, use a `#[doc(hidden)]` helper method instead

- **Confusion**: Not realizing lines prefixed with `#` are hidden in rendered docs
  **Clarification**: The `#` prefix is a rustdoc convention that hides lines from the reader while keeping them for compilation

# Source Reference

Chapter 1: Idioms, Section "Easy doc initialization".

# Verification Notes

- Definition source: Directly from "Easy doc initialization" section
- Confidence rationale: HIGH -- clear motivation, good/bad examples, and documented trade-offs
- Uncertainties: None
- Cross-reference status: Mentions #[doc(hidden)] alternative
