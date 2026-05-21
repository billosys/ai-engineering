---
# === CORE IDENTIFICATION ===
concept: Documentation Metadata
slug: documentation-metadata

# === CLASSIFICATION ===
category: documentation
subcategory: metadata
tier: intermediate

# === PROVENANCE ===
source: "Erlang Reference Manual"
source_slug: otp-reference-manual
authors: "Ericsson AB"
chapter: "Documentation"
chapter_number: null
pdf_page: null
section: "Documentation metadata"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "doc metadata"
  - "moduledoc metadata"
  - "-doc metadata map"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - doc-attribute
  - moduledoc-attribute
extends: []
related:
  - doc-signatures
  - documentation-visibility
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do I add metadata to Erlang documentation?"
  - "What metadata keys are available for -moduledoc?"
  - "What metadata keys are available for -doc?"
  - "How do multiple metadata entries merge?"
---

# Quick Definition
Documentation metadata is added via map arguments to `-moduledoc` and `-doc` attributes. Reserved keys include `since`, `deprecated`, `format`, `group`, `equiv`, and `exported`. Multiple metadata maps merge, with the latest taking precedence for duplicate keys.

# Core Definition
The Erlang Reference Manual states: "It is possible to add metadata to the documentation entry. You do this by adding a `-moduledoc` or `-doc` attribute with a map as argument." (Documentation, "Documentation metadata"). "There can be multiple metadata documentation entries, in which case the maps will be merged with the latest taking precedence if there are duplicate keys." The metadata is used by documentation tools to provide extra information. "The keys and values in the metadata map can be any type, but it is recommended that only atoms are used for keys and strings for the values."

# Prerequisites
- **doc-attribute** -- Metadata is attached to `-doc` attributes
- **moduledoc-attribute** -- Metadata is attached to `-moduledoc` attributes

# Key Properties
1. Syntax: `-doc #{key => value}.` or `-moduledoc #{key => value}.`
2. Multiple metadata maps are merged; latest values win for duplicate keys
3. Recommended: atom keys, string values

### Reserved `-moduledoc` Keys:
4. `since` -- version when the module was added; propagates to functions/types/callbacks unless overridden
5. `deprecated` -- deprecation notice text
6. `format` -- documentation format (default: `text/markdown`), as MIME type

### Reserved `-doc` Keys:
7. `since` -- version when the function/type/callback was added
8. `deprecated` -- deprecation notice; auto-inserted if `-deprecated` attribute exists
9. `group` -- grouping for documentation tools and shell autocompletion
10. `equiv` -- equivalence notation (`F/A`, `F(Args)`, or string)
11. `exported` -- boolean set automatically by compiler (not user-settable)

# Construction / Recognition
## To Add Metadata:
1. Add a separate `-doc` or `-moduledoc` attribute with a map
2. Can be combined with or separate from the documentation text
3. Multiple metadata attributes merge

## Examples of Syntax:
```erlang
-doc "Description.".
-doc #{since => "1.0", author => "Joe"}.
-doc #{since => "2.0"}.
%% Result: #{since => "2.0", author => "Joe"}
```

# Context & Application
Documentation metadata enriches the generated documentation with version history, deprecation notices, grouping, and equivalence relationships. The `since` key on `-moduledoc` is particularly useful because it propagates to all functions, types, and callbacks in the module unless they override it with their own `since` value. The `equiv` key reduces duplication by linking convenience functions to their full-featured equivalents.

# Examples
**Example 1** (Documentation metadata -- merging):
```erlang
-doc "Adds two numbers.".
-doc #{since => "1.0", author => "Joe"}.
-doc #{since => "2.0"}.
add(One, Two) -> One + Two.
```
Result: metadata is `#{since => "2.0", author => "Joe"}`.

**Example 2** (Doc metadata -- equiv):
```erlang
-doc #{equiv => add/3}.
add(One, Two) -> add(One, Two, []).
add(One, Two, Options) -> ...
```

**Example 3** (Doc metadata -- equiv with args):
```erlang
-doc #{equiv => add(One, Two, [])}.
-spec add(One :: number(), Two :: number()) -> number().
add(One, Two) -> add(One, Two, []).
```

**Example 4** (Moduledoc metadata):
```erlang
-moduledoc {file, "../doc/arith.asciidoc"}.
-moduledoc #{since => "0.1", format => "text/asciidoc"}.
-moduledoc #{deprecated => "Use the Erlang arithmetic operators instead."}.
```

# Relationships
## Builds Upon
- **doc-attribute** -- Metadata extends `-doc` attributes
- **moduledoc-attribute** -- Metadata extends `-moduledoc` attributes

## Enables
Rich documentation output with version information, deprecation notices, and grouping.

## Related
- **doc-signatures** -- Signatures are derived separately from metadata
- **documentation-visibility** -- The `exported` metadata key relates to visibility

## Contrasts With
None.

# Common Errors
- **Error**: Setting the `exported` metadata key manually
  **Correction**: The `exported` key is automatically set by the compiler and should not be set by the user.

- **Error**: Using non-atom keys or non-string values in metadata
  **Correction**: While any type is technically allowed, atoms for keys and strings for values are recommended for consistency.

# Common Confusions
- **Confusion**: Thinking `-doc #{...}` replaces the documentation text
  **Clarification**: The metadata map is separate from the documentation text. Both can coexist: `-doc "text".` followed by `-doc #{since => "1.0"}.`

- **Confusion**: Expecting metadata to be ordered
  **Clarification**: Multiple metadata maps are merged. For duplicate keys, the latest value wins.

# Source Reference
"Documentation" chapter, "Documentation metadata," "Moduledoc metadata," and "Doc metadata" sections.

# Verification Notes
- Definition source: Direct from source text with all reserved keys listed
- Confidence rationale: High -- explicit metadata key definitions and merging rules
- Uncertainties: None
- Cross-reference status: All slugs verified
