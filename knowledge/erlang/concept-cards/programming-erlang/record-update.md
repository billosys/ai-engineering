---
# === CORE IDENTIFICATION ===
concept: Record Update
slug: record-update

# === CLASSIFICATION ===
category: data-types
subcategory: compound-data
tier: intermediate

# === PROVENANCE ===
source: Programming Erlang, Second Edition
source_slug: programming-erlang
authors: Joe Armstrong
chapter: "Records and Maps"
chapter_number: 5
pdf_page: null
section: "Creating and Updating Records"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - record copy
  - record field update
  - dot syntax

# === TYPED RELATIONSHIPS ===
prerequisites:
  - record
  - pattern-matching
extends:
  - record
related:
  - map-update
contrasts_with:
  - map-update

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do I update a field in a record?"
  - "How do I extract a single field from a record?"
---

# Quick Definition

Record update creates a copy of an existing record with one or more field values changed, using the syntax `OldRecord#Name{field=NewValue}`. The original record is never modified.

# Core Definition

To update a record, the syntax `X1#todo{status=done}` says "create a copy of `X1` (which must be of type `todo`), changing the field value `status` to `done`." This makes a *copy* of the original record; the original record is not changed. To extract a single field, the "dot syntax" `X2#todo.text` returns the value of one named field. Multiple fields can be extracted at once by pattern matching with a record pattern such as `#todo{who=W, text=Txt} = X2` ("Records and Maps," *Creating and Updating Records*; *Extracting the Fields of a Record*).

# Prerequisites

- **Record** — Record update operates on values created from a `-record` declaration.
- **Pattern matching** — Multi-field extraction uses record patterns on the left side of `=`.

# Key Properties

1. `OldRec#Name{f=V}` produces a new record; the original is unchanged (immutability preserved).
2. The updated value must already be of the named record type.
3. Any subset of fields may be updated in a single expression.
4. The "dot syntax" `Rec#Name.field` extracts a single field's value.
5. Pattern matching with a record pattern extracts several fields in one operation.

# Construction / Recognition

## To Construct/Create (update):
1. Start with an existing record value, e.g. `X1`.
2. Write `X1#todo{status=done}` to copy it with `status` set to `done`.
3. Bind the result to a new variable, e.g. `X2 = X1#todo{status=done}`.

## To Identify/Recognize (extract):
1. For one field, write `X2#todo.text`.
2. For several fields, write `#todo{who=W, text=Txt} = X2`; on a successful match `W` and `Txt` bind to the field values.

# Context & Application

- **Typical contexts**: Producing modified records in functional, side-effect-free code.
- **Common applications**: A function that takes a record, changes a status, and returns the new record (e.g. `clear_status/1`).
- **Historical/stylistic notes**: Because Erlang data is immutable, "update" always means copy-with-change.

# Examples

**Example 1** (*Creating and Updating Records*): Copying a record with a changed field.

```erlang
X2 = X1#todo{status=done}.
%% => #todo{status = done, who = joe, text = "Fix errata in book"}
```

**Example 2** (*Extracting the Fields of a Record*): Single-field extraction with dot syntax.

```erlang
X2#todo.text.
%% => "Fix errata in book"
```

**Example 3** (*Extracting the Fields of a Record*): Multi-field extraction by pattern matching.

```erlang
#todo{who=W, text=Txt} = X2.
%% W bound to joe, Txt bound to "Fix errata in book"
```

# Relationships

## Builds Upon
- **Record** — Update and extraction operate on record values.

## Enables
- **Record** — Functions that transform records depend on the copy-update operation.

## Related
- **Map update** — The analogous operation for maps.

## Contrasts With
- **Map update** — Map update can add new keys with `=>`; record update cannot add fields, only change declared ones.

# Common Errors

- **Error**: Expecting `X1#todo{status=done}` to mutate `X1`.
  **Correction**: It returns a new copy; capture the result in a new variable.

- **Error**: Trying to update a field name that is not in the record declaration.
  **Correction**: Only fields declared in the `-record` declaration may be updated.

# Common Confusions

- **Confusion**: Thinking record update is expensive because it "copies" the record.
  **Clarification**: It produces a new tuple but the operation is lightweight; only the structure needed to represent the change is created.

# Source Reference

Chapter 5: Records and Maps, sections "Creating and Updating Records" and "Extracting the Fields of a Record." EPUB-origin source — no page numbers.

# Verification Notes

- Definition source: Direct adaptation of the update and extraction descriptions in the source.
- Confidence rationale: HIGH — explicit syntax and worked shell examples in the source.
- Uncertainties: None.
- Cross-reference status: Verified against planned cards.
- Re-extraction notes: Fresh extraction — no pre-existing card for this source.
