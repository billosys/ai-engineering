# Guide Structure Analysis

Reverse-engineered from the 7 exemplar guides:
`01-core-idioms.md`, `02-api-design.md`, `03-error-handling.md`,
`06-traits.md`, `11-anti-patterns.md`, `12-project-structure.md`,
`13-documentation.md`


## 1. Common Structure (All Guides)

Every guide follows the same high-level skeleton:

```
# Title                           ← H1, descriptive noun phrase
[1-2 sentence intro paragraph]    ← No heading, immediately after title
                                  ← Optional --- separator (inconsistent)

## XX-01: Card Title              ← Concept cards (the body)
**Strength**: ...
**Summary**: ...
[code examples]
**Rationale**: ...
**See also**: ...
---

## XX-02: Card Title              ← More cards, separated by ---
...

## Summary Table                  ← Markdown table of key patterns
## Related Guidelines             ← Cross-references to other guides
## External References            ← Links to official docs, Pragmatic Rust IDs
```


## 2. Detailed Element Analysis

### 2.1 File Naming

- Pattern: `NN-topic-slug.md` (e.g., `01-core-idioms.md`)
- Numbers determine ordering; they are NOT in the guide title itself
- Slug uses lowercase-hyphenated words

### 2.2 Title (H1)

- Always `# Descriptive Topic Name`
- Never includes the file number
- Examples: `# Core Rust Idioms`, `# API Design Guidelines`, `# Trait Design and Implementation`
- Tone: professional, direct

### 2.3 Introduction Paragraph

- 1-2 sentences, no heading
- Immediately follows the H1 title
- Describes purpose and scope of the guide
- **No frontmatter** (no YAML, no TOML metadata in any guide)

### 2.4 Concept Cards (The Main Body)

Each card is an H2 section representing one guideline/pattern:

| Field | Format | Required? |
|-------|--------|-----------|
| Heading | `## PREFIX-NN: Title` | Yes |
| Strength | `**Strength**: MUST/SHOULD/CONSIDER/AVOID` | Yes |
| Summary | `**Summary**: One-line description` | Yes |
| Code example(s) | `` ```rust `` fenced blocks | Yes |
| Rationale | `**Rationale**: 1-3 sentences` | Common but optional |
| See also | `**See also**: references` | Optional |
| Clippy | `**Clippy**: lint_name` | Rare (anti-patterns only) |

**Card prefix conventions observed:**

| Guide | Prefix | Example |
|-------|--------|---------|
| Core Idioms | ID | ID-01 |
| API Design | API | API-01 |
| Error Handling | EH | EH-01 |
| Traits | TR | TR-01 |
| Anti-Patterns | AP | AP-01 |
| Project Structure | PS | PS-01 |
| Documentation | DC | DC-01 |

**Card counts by guide:**
- 01-core-idioms: 42 cards
- 02-api-design: 59 cards
- 03-error-handling: 32 cards
- 06-traits: 26 cards
- 11-anti-patterns: 80 cards
- 12-project-structure: 31 cards
- 13-documentation: 35 cards

**Strength level distribution:**
- `MUST` — required, violation is always wrong
- `SHOULD` — strongly recommended, needs justification to deviate
- `CONSIDER` — contextual, may or may not apply
- `AVOID` — anti-pattern (predominant in guide 11, but appears across all guides)

### 2.5 Code Example Conventions

- Always use `` ```rust `` fenced blocks
- Two labeling conventions used (both acceptable, pick one per guide):
  - Text comments: `// Good - explanation`, `// Bad - explanation`
  - Emoji markers: `// ✅ GOOD: explanation`, `// ❌ BAD: explanation`, `// ⚠️ CAUTION:`
- Show the bad pattern first, then the good pattern
- Inline comments explain the "why", not just the "what"
- Typical length: 10-40 lines per block
- Multiple code blocks per card are common for complex topics
- Some cards show separate "Bad" and "Good" blocks; others combine them

### 2.6 Summary Table

- Always present as the last major content section before cross-references
- Standard columns: `| Pattern | Strength | Key Insight |`
- Anti-patterns variant: `| Anti-Pattern | Instead Do | Why |`
- Covers the most important cards (not necessarily all)

### 2.7 Related Guidelines

- Always present
- Format: `- **Topic Name**: See \`NN-filename.md\` for brief description`
- Typically references 2-4 other guides

### 2.8 External References

- Always present
- Markdown links to official docs
- Often ends with: `Pragmatic Rust Guidelines: M-ID-1, M-ID-2`
- Common references: Rust API Guidelines, Rust Book, Rustdoc Book

### 2.9 Tone and Voice

- Technical and instructive
- Predominantly imperative/declarative: "Use X", "Prefer Y", "Don't do Z"
- Second person ("you") appears but is not dominant
- Professional but not stiff; avoids marketing language
- Concise prose; code examples carry the primary teaching load
- No humor, no emojis outside of code examples


## 3. Optional Sections (Topic-Specific)

Some guides include additional sections between the last card and the Summary Table.
These are topic-specific and should only be included when they serve the content:

| Section | Appears In | Purpose |
|---------|-----------|---------|
| Common Patterns | 03-error-handling | Reusable template (full error struct) |
| Project Checklist | 12-project-structure | Cargo.toml template + directory layouts |
| Common Project Structures | 12-project-structure | ASCII directory trees for reference |
| Documentation Checklist | 13-documentation | Quick-reference doc comment template |
| Module Template | 13-documentation | Reusable module doc template |
| Critical Reminders for AI | 11-anti-patterns | List of patterns AI models get wrong |

These are **optional** — only add them if the topic genuinely benefits from a
quick-reference template or checklist.


## 4. Deviations from Common Pattern

### 4.1 Intentional Deviations (Topic-Specific)

These deviations seem purposeful and appropriate for their topic:

- **Anti-patterns (11)**: Uses blockquote `>` after title and a `**Purpose**:`
  annotation in the intro. This is warranted because anti-patterns benefit from
  stronger framing ("here's why this guide exists"). Also uses `AVOID` as the
  predominant strength level and has a "Critical Reminders for AI" section.
  Later cards (AP-63+) use `❌` emoji prefix in the card title itself — this is
  a style choice for emphasis.

- **Error handling (03)**: Includes a "Common Patterns" section with the full
  error template code. Warranted because error types have a canonical structure
  worth showing in full.

- **Project structure (12)**: Includes project layout ASCII trees and a
  Cargo.toml template. Warranted because project structure is inherently visual.

- **Documentation (13)**: Includes both a "Documentation Checklist" and "Module
  Template" section. Warranted because documentation has canonical templates.

### 4.2 Incidental Deviations (Inconsistencies)

These appear to be inconsistencies rather than intentional choices:

- **Initial `---` separator after intro**: Present in guides 01 and 02, absent
  in 03, 06, 11, 12, 13. **Recommendation**: Omit it (majority omits it).

- **Double `---` between cards**: Appears sporadically in guides 01, 06, 11
  (e.g., two `---` in a row). Appears to be copy-paste artifacts.
  **Recommendation**: Use single `---` between cards consistently.

- **Stub/empty cards**: Several guides have cards with heading and strength but
  no summary, code, or rationale:
  - Guide 12 (project structure): PS-03, PS-07, PS-11, PS-13, PS-18, PS-22, PS-31
  - Guide 13 (documentation): DC-01, DC-04, DC-06, DC-22, DC-32, DC-34
  These appear to be placeholder/WIP cards.
  **Recommendation**: Either complete or remove stubs before treating a guide as
  stable.

- **Duplicate content across cards**: Some guides have cards covering the same
  topic with slight variations:
  - Guide 01: ID-34 and ID-37 both cover `format!` for string concatenation
  - Guide 01: ID-39 and ID-40 both cover borrowed types for arguments
  - Guide 02: API-42 and API-49 both cover smart pointer methods
  - Guide 02: API-48 and API-49 both cover smart pointers not adding methods
  **Recommendation**: Deduplicate before finalizing guides.

- **Inconsistent Summary Table heading**:
  - Most: `## Summary Table`
  - Guide 11: `## Summary of Anti-Patterns`
  - Guide 01: `## Best Practices Summary` > `### Quick Reference Table`
  **Recommendation**: Standardize on `## Summary Table`.


## 5. Recommendations for New Guides (e.g., Cobalt)

Based on this analysis, a new guide should:

1. **Follow the template strictly** for all required elements (title, intro,
   cards, summary table, related guidelines, external references).

2. **Choose a 2-3 letter prefix** that's distinct from existing ones. For a
   Cobalt guide, `CB-` or `CO-` would work.

3. **Use single `---`** between cards (not double).

4. **Omit the `---`** after the intro paragraph (follow the majority pattern).

5. **Don't create stub cards** — only add cards that have complete content.

6. **Pick one code labeling style** and use it consistently throughout:
   either `// Good -`/`// Bad -` or `// ✅ GOOD:`/`// ❌ BAD:`.

7. **Include topic-specific extra sections** only if they genuinely add value
   (e.g., a quick-start template, a checklist, or a canonical code template).

8. **Cross-reference existing guides** in the Related Guidelines section —
   the Cobalt guide would likely reference core idioms (01), API design (02),
   error handling (03), and project structure (12).

9. **Include Pragmatic Rust guideline IDs** in External References where they
   apply (most existing guides do this).

10. **Target 15-40 cards** for a well-scoped guide. Larger guides (like
    API design at 59 or anti-patterns at 80) risk becoming unwieldy unless
    the topic genuinely demands it.
