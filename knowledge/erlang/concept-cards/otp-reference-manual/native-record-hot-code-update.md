---
# === CORE IDENTIFICATION ===
concept: Native Record Hot Code Update
slug: native-record-hot-code-update

# === CLASSIFICATION ===
category: data-types
subcategory: native-records
tier: advanced

# === PROVENANCE ===
source: "Erlang Reference Manual"
source_slug: otp-reference-manual
authors: "Ericsson AB"
chapter: "Native Records"
chapter_number: null
pdf_page: null
section: "Advanced: Hot Code Updating"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "native record migration"
  - "native record upgrade"
  - "record field addition"
  - "record field deletion"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - native-record-construction
  - native-record-patterns
  - native-record-update
extends: []
related:
  - native-record-definition
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do I add a field to a native record during hot code update?"
  - "How do I remove a field from a native record during hot code update?"
  - "How does the captured definition help with hot code update?"
  - "What is the nowarn_undefined_field option?"
---

# Quick Definition
Native records support hot code updating by leveraging the captured definition mechanism. An `update/1` function can match old record versions (using the captured definition) and construct new versions, enabling field addition and removal during live upgrades.

# Core Definition
The Erlang Reference Manual explains hot code updating for native records through two scenarios: adding and removing fields. The key insight is: "Remember that the captured definition is used when matching a record. That makes it possible to access all fields in a record constructed by a previous version of a module." For adding a field, the `update/1` function pattern-matches old records and constructs new ones with the additional field. For removing a field, the function matches on the old field (generating a compile warning) and produces a new record without it. The `nowarn_undefined_field` compile option suppresses the warning for referencing removed fields (Native Records, "Advanced: Hot Code Updating" section).

# Prerequisites
- **native-record-construction** -- Understanding how definitions are captured at construction
- **native-record-patterns** -- Pattern matching old record versions
- **native-record-update** -- Understanding that update uses the captured definition

# Key Properties
1. The captured definition enables matching fields from old record versions
2. An `update/1` function pattern-matches old records and constructs new ones
3. The first clause should detect already-updated records (idempotency)
4. Adding a field: match old fields, construct with new field added
5. Removing a field: match the removed field (generates warning), construct without it
6. `nowarn_undefined_field` compile option suppresses warnings for removed fields
7. The `update/1` function should be idempotent -- calling it twice returns the same result

# Construction / Recognition
## To Add a Field:
1. Add the new field to the record definition
2. Write an `update/1` function with two clauses:
   - First: match records that already have the new field (idempotent guard)
   - Second: match old records, extract all fields, construct new record with added field

## To Remove a Field:
1. Remove the field from the record definition
2. Write an `update/1` function with two clauses:
   - First: match old records with the removed field, construct new record incorporating the value elsewhere
   - Second: match already-updated records (idempotent)
3. Optionally add `-compile(nowarn_undefined_field).` to suppress warnings

# Context & Application
Hot code updating is a critical Erlang/OTP capability for zero-downtime deployments. Native records' captured definition mechanism makes this more robust than with tuple-based records, because matching against old record versions works naturally -- the captured definition contains the old field layout. This is particularly important in long-running systems where state records accumulate across module versions.

# Examples
**Example 1** (How to add a field section): Adding the `new` field:
```erlang
-module(add_one_field).
-record #rec{a, b, c, d, new}.
-export([update/1]).

update(#rec{new=_}=AlreadyUpdated) ->
    AlreadyUpdated;
update(#rec{a=A, b=B, c=C, d=D}) ->
    #rec{a=A, b=B, c=C, d=D, new=new_value}.
```

Session demonstrating the update:
```erlang
1> c(add_one_field).   %% Compile original version (without 'new' field)
2> R = make_rec(1, 2, 3, 4).
#add_one_field:rec{a = 1,b = 2,c = 3,d = 4}
3> c(add_one_field).   %% Compile modified version (with 'new' field)
4> NewR = add_one_field:update(R).
#add_one_field:rec{a = 1,b = 2,c = 3,d = 4,new = new_value}
5> NewR = add_one_field:update(NewR).  %% Idempotent
#add_one_field:rec{a = 1,b = 2,c = 3,d = 4,new = new_value}
```

**Example 2** (How to delete one field section): Removing the `d` field:
```erlang
-module(delete_one_field).
-compile(nowarn_undefined_field).
-record #rec{a, b, c, opts=[]}.
-export([update/1]).

update(#rec{a=A, b=B, c=C, d=D, opts=Opts}) ->
    #rec{a=A, b=B, c=C, opts=[{d,D} | Opts]};
update(#rec{}=AlreadyUpdated) ->
    AlreadyUpdated.
```

Session demonstrating the update:
```erlang
1> c(delete_one_field).   %% Compile original version (with 'd' field)
2> R = make_rec(1, 2, 3, 4).
#delete_one_field:rec{a = 1,b = 2,c = 3,d = 4,opts = []}
3> c(delete_one_field).   %% Compile modified version (without 'd' field)
4> NewR = delete_one_field:update(R).
#delete_one_field:rec{a = 1,b = 2,c = 3,opts = [{d,4}]}
5> NewR = delete_one_field:update(NewR).  %% Idempotent
#delete_one_field:rec{a = 1,b = 2,c = 3,opts = [{d,4}]}
```

# Relationships
## Builds Upon
- **native-record-construction** -- Captured definitions enable cross-version matching
- **native-record-patterns** -- Pattern matching extracts fields from old versions
- **native-record-update** -- Understanding that update uses captured definitions

## Enables
No direct dependents within this extraction scope.

## Related
- **native-record-definition** -- The definition changes are what trigger the need for update functions

## Contrasts With
No direct contrasts within this extraction scope.

# Common Errors
- **Error**: Forgetting the idempotency clause in the `update/1` function
  **Correction**: Always include a clause that detects already-updated records to prevent double-conversion.

- **Error**: Not using `-compile(nowarn_undefined_field)` when matching removed fields
  **Correction**: Add this option or accept the compile warning. The warning is intentional -- matching a removed field is unusual but valid for hot code update.

# Common Confusions
- **Confusion**: Thinking old record values are automatically updated when the module is reloaded
  **Clarification**: Record values retain their captured definition. An explicit `update/1` function must be called on each old value to convert it to the new format.

- **Confusion**: Wondering how the `update/1` function can match a field not in the current definition
  **Clarification**: The captured definition from the old record value contains the old field layout. Pattern matching uses this captured definition, not the new module definition.

# Source Reference
Native Records chapter, "Advanced: Hot Code Updating" section.

# Verification Notes
- Definition source: Direct examples and quotes from source text
- Confidence rationale: High -- complete worked examples with shell sessions
- Uncertainties: None
- Cross-reference status: All referenced slugs correspond to cards in this extraction
