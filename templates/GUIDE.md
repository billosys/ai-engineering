# [Guide Topic Name]

[1-2 sentence overview of the guide's purpose and scope. Describes what the guide covers and who it's for. No heading for this paragraph.]

<!-- TEMPLATE NOTES
  File naming: NN-topic-slug.md (e.g., 01-core-idioms.md, 14-new-topic.md)
  The number NN determines ordering in the guide index.

  Card prefix: Derive a 2-3 letter ALL-CAPS prefix from the topic name.
  Examples: ID (idioms), API (api design), EH (error handling),
           TR (traits), AP (anti-patterns), PS (project structure),
           DC (documentation)

  Strength levels:
    MUST     - Required; violating this is always a bug or design flaw
    SHOULD   - Strongly recommended; deviations need explicit justification
    CONSIDER - Worth evaluating; may or may not apply depending on context
    AVOID    - Anti-pattern; actively harmful, use the recommended alternative

  Tone: Technical, instructive, direct. Use imperative/declarative voice.
  Second person ("you") is acceptable but not required.
  Keep prose concise; let code examples do the heavy lifting.
-->


## XX-01: [Card Title]

**Strength**: [MUST | SHOULD | CONSIDER | AVOID]

**Summary**: [One-line description of the pattern or guideline.]

```rust
// Bad - [brief explanation of what's wrong]
[anti-pattern code example]

// Good - [brief explanation of what's right]
[recommended code example]
```

<!-- TEMPLATE NOTES for code examples:
  - Use ```rust fenced code blocks
  - Show "Bad" examples first, then "Good" examples
  - Mark with comments: "// Bad -", "// Good -" for simple cases
  - Or use emoji markers for emphasis: "// ❌ BAD:", "// ✅ GOOD:", "// ⚠️ CAUTION:"
  - Pick one style and use it consistently within a guide
  - Include inline comments explaining the "why"
  - Typical length: 10-40 lines per code block
  - Multiple code blocks are fine for complex topics
  - Keep examples self-contained and compilable where possible
-->

**Rationale**: [1-3 sentences explaining *why* this pattern matters. Focus on consequences of violating the guideline.]

**See also**: [Optional. Comma-separated references to related guidelines, e.g., C-COMMON-TRAITS, M-PUBLIC-DEBUG, or cross-references like `03-error-handling.md`]

---

## XX-02: [Card Title]

**Strength**: [MUST | SHOULD | CONSIDER | AVOID]

**Summary**: [One-line description.]

```rust
[code example(s)]
```

**Rationale**: [Explanation.]

**See also**: [References]

---

<!-- TEMPLATE NOTES for the card sequence:
  - Continue with XX-03, XX-04, etc.
  - Each card is a self-contained unit covering one concept
  - Cards are separated by a single `---` horizontal rule
  - Order cards from most fundamental/common to more specialized
  - Group related cards together in the sequence
  - A guide typically has 15-40 cards, but can have more

  Required card fields:
    - ## XX-NN: Title (H2 heading with prefix-number and descriptive title)
    - **Strength**: (one of MUST/SHOULD/CONSIDER/AVOID)
    - **Summary**: (one-line description)
    - At least one code example (```rust block)

  Optional card fields (include when relevant):
    - **Rationale**: (why this matters; omit only if self-evident)
    - **See also**: (cross-references; omit if none apply)
    - **Clippy**: (relevant clippy lint name, e.g., clippy::ptr_arg)
    - Additional code blocks (for complex topics or separate good/bad examples)
-->


## Summary Table

| Pattern | Strength | Key Insight |
|---------|----------|-------------|
| [Card title or short name] | [MUST/SHOULD/CONSIDER/AVOID] | [One-phrase takeaway] |
| [Card title or short name] | [MUST/SHOULD/CONSIDER/AVOID] | [One-phrase takeaway] |

<!-- TEMPLATE NOTES for the summary table:
  - Include the most important cards (not necessarily all of them)
  - Columns: Pattern | Strength | Key Insight
  - For anti-pattern guides, alternative columns:
    Anti-Pattern | Instead Do | Why
  - Keep "Key Insight" to a short phrase (5-10 words)
  - This section is REQUIRED for all guides
-->


## Related Guidelines

- **[Topic]**: See `NN-filename.md` for [brief description of what's there]
- **[Topic]**: See `NN-filename.md` for [brief description of what's there]

<!-- TEMPLATE NOTES for Related Guidelines:
  - Cross-reference 2-4 other guides that complement this one
  - Format: **Bold topic name**: See `filename` for description
  - This section is REQUIRED for all guides
-->


## External References

- [Resource Name](https://url)
- [Resource Name](https://url)
- Pragmatic Rust Guidelines: M-GUIDELINE-ID, M-OTHER-ID

<!-- TEMPLATE NOTES for External References:
  - Link to official Rust documentation, API Guidelines, RFCs, etc.
  - Include relevant Pragmatic Rust Guideline IDs if applicable
  - Typically 2-5 references
  - This section is REQUIRED for all guides
-->
