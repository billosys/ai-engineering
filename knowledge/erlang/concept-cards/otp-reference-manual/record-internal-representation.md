---
# === CORE IDENTIFICATION ===
concept: Record Internal Representation
slug: record-internal-representation

# === CLASSIFICATION ===
category: data-types
subcategory: records
tier: foundational

# === PROVENANCE ===
source: "Erlang Reference Manual"
source_slug: otp-reference-manual
authors: "Ericsson AB"
chapter: "Records"
chapter_number: null
pdf_page: null
section: "Internal Representation of Records"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "record as tuple"
  - "tagged tuple record"
  - "record tuple representation"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - record-definition
  - tuple
extends: []
related:
  - record-field-position
  - record-creation
contrasts_with:
  - native-record-definition

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How are records represented internally in Erlang?"
  - "What is record_info and how is it used?"
  - "What is the relationship between records and tuples?"
  - "What is the size of a record's tuple representation?"
---

# Quick Definition
Records are internally represented as tagged tuples where the first element is the record name atom and the remaining elements are the field values in definition order. A record `-record(Name, {Field1, ..., FieldN})` becomes `{Name, Value1, ..., ValueN}`.

# Core Definition
The Erlang Reference Manual states: "Record expressions are translated to tuple expressions during compilation. A record defined as `-record(Name, {Field1, ..., FieldN}).` is internally represented by the tuple `{Name, Value1, ..., ValueN}` where each `ValueI` is the default value for `FieldI`." Additionally, "To each module using records, a pseudo function is added during compilation to obtain information about records: `record_info(fields, Record) -> [Field]` and `record_info(size, Record) -> Size`." The size "is the size of the tuple representation, that is, one more than the number of fields" (Records, "Internal Representation of Records" section).

# Prerequisites
- **record-definition** -- Understanding what a record defines
- **tuple** -- Records are compiled to tuples

# Key Properties
1. Records compile to tuples: `-record(Name, {F1, ..., FN})` becomes `{Name, V1, ..., VN}`
2. The first tuple element is the record name atom (the "tag")
3. The tuple size is one more than the number of fields (tag + fields)
4. `record_info(fields, Record)` returns a list of field name atoms
5. `record_info(size, Record)` returns the tuple size (N + 1)
6. `record_info` is a pseudo function added at compile time, not a regular function
7. All record operations are compile-time transformations to tuple operations

# Construction / Recognition
## To Inspect the Representation:
1. Use `record_info(fields, RecordName)` to get field names
2. Use `record_info(size, RecordName)` to get the tuple size
3. Use `tuple_to_list/1` in the shell to see the underlying tuple

## To Recognize:
1. Any tagged tuple `{atom, ...}` could be a record
2. The `is_record/2` BIF checks both the tag and size

# Context & Application
Understanding the tuple representation is important for debugging, interoperability with tuple-based code, ETS/Mnesia (which store tuples), and performance reasoning. Since records are just tuples, they can be processed by any function that operates on tuples. However, relying on the tuple representation directly (instead of using record syntax) makes code fragile when fields are added or reordered.

# Examples
**Example 1** (Internal Representation section): A record and its tuple form:
```erlang
-record(person, {name, phone, address}).

%% The following record creation:
#person{name="Joe", phone="555-1234", address="Stockholm"}

%% is internally represented as:
{person, "Joe", "555-1234", "Stockholm"}
```

**Example 2** (Internal Representation section): Using record_info:
```erlang
record_info(fields, person).   %% Returns [name, phone, address]
record_info(size, person).     %% Returns 4 (1 tag + 3 fields)
```

# Relationships
## Builds Upon
- **record-definition** -- The definition determines the tuple structure
- **tuple** -- Records are tuples at runtime

## Enables
- **record-field-position** -- Position access relies on the tuple layout

## Related
- **record-creation** -- Creation expressions compile to tuple creation

## Contrasts With
- **native-record-definition** -- Native records are a distinct type, not tuples. `is_record/1` returns `false` for tuple-based records.

# Common Errors
- **Error**: Using `record_info` as a regular function (e.g., passing it as a fun or applying it dynamically)
  **Correction**: `record_info` is a pseudo function resolved at compile time. It cannot be called dynamically or passed as a function reference.

# Common Confusions
- **Confusion**: Thinking records have a distinct runtime type
  **Clarification**: Records are ordinary tuples at runtime. There is no runtime type tag beyond the conventional first-element atom.

- **Confusion**: Expecting `record_info(size, Rec)` to return the number of fields
  **Clarification**: It returns the tuple size, which is the number of fields plus one (for the record tag).

# Source Reference
Records chapter, "Internal Representation of Records" section.

# Verification Notes
- Definition source: Direct quotes from source text
- Confidence rationale: High -- explicit definition and pseudo-function documentation
- Uncertainties: None
- Cross-reference status: All referenced slugs correspond to cards in this extraction
