---
# === CORE IDENTIFICATION ===
concept: Opaque Type
slug: opaque-type

# === CLASSIFICATION ===
category: data-types
subcategory: typespecs
tier: advanced

# === PROVENANCE ===
source: "Programming Erlang, Second Edition"
source_slug: programming-erlang
authors: Joe Armstrong
chapter: "Types"
chapter_number: 9
pdf_page: null
section: "Opaque Types"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "-opaque"
  - "-opaque attribute"
  - "abstract data type"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - type-declaration
  - exported-type
extends:
  - type-declaration
related:
  - dialyzer
contrasts_with:
  - type-declaration
  - exported-type

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is an opaque type?"
  - "How do I hide the internal structure of a data type?"
  - "What is an abstraction violation?"
---

# Quick Definition

An opaque type is a type declared with `-opaque` whose internal structure
is hidden from other modules: only the defining module may inspect its
representation. Other modules treat it as an abstract handle.

# Core Definition

An opaque type hides the internal details of a data structure so that
only the module that creates it knows the details of the type. It is
declared with `-opaque` instead of `-type` (chapter "Types," section
"Opaque Types"):

```erlang
-module(a).
-opaque rich_text() :: [{font(), char()}].
-export_type([rich_text/0]).
-export([make_text/1, bounding_box/1]).
-spec make_text(string()) -> rich_text().
-spec bounding_box(rich_text()) -> {Height::integer(), Width::integer()}.
```

A consuming module may pass an opaque value around and back into the
defining module without knowing its structure. Making use of the
internal structure of an opaque type from another module is called an
*abstraction violation* and can be detected by Dialyzer if the visibility
of the types in the functions involved is declared correctly.

# Prerequisites

- **Type declaration** — `-opaque` is a variant of the `-type` declaration form.
- **Exported type** — an opaque type is exported so other modules can name it.

# Key Properties

1. Declared with `-opaque Name() :: Definition.`
2. The defining module knows and may use the internal representation.
3. Other modules must treat values of the type as abstract.
4. Inspecting the structure from outside is an abstraction violation.
5. Dialyzer can detect abstraction violations when type visibility is declared.

# Construction / Recognition

## To Construct an Opaque Type:
1. Declare it with `-opaque Name() :: Definition.`
2. Export it with `-export_type`.
3. Provide exported functions to create and operate on values of the type.

## To Recognize an Abstraction Violation:
1. Look for code in a non-defining module that pattern-matches or comprehends over the type's internal structure.
2. Dialyzer reports it as an abstraction violation.

# Context & Application

- **Typical contexts**: Library modules exposing a handle whose layout may change.
- **Common applications**: Encapsulating data structures so callers depend only on the API.
- **Historical/stylistic notes**: The chapter contrasts module `b` (correctly treats `rich_text` as opaque) with module `c` (illegally comprehends over its internal 2-tuple structure).

# Examples

**Example 1** (section "Opaque Types"): `-opaque rich_text() :: [{font(), char()}].` declared in module `a`.

**Example 2** (section "Opaque Types"): module `c` writes `[F || {F,_} <- X]` over an opaque value, an abstraction violation, because it relies on `X` being a list of 2-tuples.

## Worked Example

From section "Opaque Types," module `b` uses the type correctly:

```erlang
do_this() ->
    X = a:make_text("hello world"),
    {W, H} = a:bounding_box(X).
```

`X` is created inside `a` and passed back into `a`; `b` never inspects
its structure.

# Relationships

## Builds Upon
- **Type declaration** — `-opaque` is the visibility-restricted form of `-type`.

## Enables
- **Dialyzer** — opaque declarations let Dialyzer flag abstraction violations.

## Related
- **Dialyzer** — the tool that enforces opacity at analysis time.

## Contrasts With
- **Type declaration** — a plain `-type` exposes its structure; `-opaque` hides it.
- **Exported type** — a plain exported `-type` lets consumers see and use the structure.

# Common Errors

- **Error**: Pattern-matching on an opaque value's internal shape from another module.
  **Correction**: Use only the defining module's exported functions to manipulate the value.

- **Error**: Declaring a type `-opaque` but not exporting it.
  **Correction**: Export the opaque type so other modules can name it as a handle.

# Common Confusions

- **Confusion**: Believing an opaque type is enforced by the runtime.
  **Clarification**: Opacity is a static contract; it is checked by Dialyzer, not the BEAM.

- **Confusion**: Thinking opacity prevents passing the value around.
  **Clarification**: The value can be freely passed; only inspecting its internal structure is forbidden.

# Source Reference

Chapter 9: "Types," section "Opaque Types." EPUB-origin source; no page
numbers.

# Verification Notes

- Definition source: Direct adaptation of the `-opaque rich_text()` example and the abstraction-violation discussion.
- Confidence rationale: HIGH — the source explicitly defines `-opaque` and abstraction violations.
- Uncertainties: None.
- Cross-reference status: Verified against planned cards.
- Re-extraction notes: Fresh extraction.
