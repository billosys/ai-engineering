---
# === CORE IDENTIFICATION ===
concept: Records
slug: records

# === CLASSIFICATION ===
category: data-types
subcategory: records
tier: foundational

# === PROVENANCE ===
source: "Designing for Scalability with Erlang/OTP"
source_slug: design-scale-erlang-otp
authors: "Francesco Cesarini & Steve Vinoski"
chapter: "Introducing Erlang"
chapter_number: 1
pdf_page: 40
section: "Records"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - record
  - "-record directive"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - pattern-matching
extends: []
related: []
contrasts_with:
  - maps

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is a record in Erlang?"
  - "When should I use a record instead of a map?"
---

# Quick Definition

A record provides named access to the fields of a tuple-like collection. It is defined with the `-record` directive and is, under the covers, implemented as a tuple.

# Core Definition

"Records address the shortcomings of tuples by providing a way to access fields of a tuple-like collection by name" (Cesarini & Vinoski, p. 40). "The `-record` directive is used to define a record, with the record name specified as the directive's first argument. The second argument, which resembles a tuple of atoms, defines the fields of the record. Fields can have specific default values ... Fields without specified defaults have the atom `undefined` as their default values" (p. 40). "Records are just syntactic sugar; under the covers, they are implemented as tuples" (p. 42). Records are "fast, so use them when you have a fixed number of fields known at compile time" (p. 43).

# Prerequisites

- **Pattern matching** — Records are commonly used in pattern matching, especially in function heads to extract fields.

# Key Properties

1. Defined with the `-record(Name, {Fields})` directive.
2. Fields are accessed by name, e.g., `HostEnt#hostent.h_addrtype`.
3. Fields may declare default values; undeclared fields default to the atom `undefined`.
4. The number of fields is fixed at compile time.
5. Field names are atoms only.
6. Records are syntactic sugar over tuples; field names are not part of the runtime instance.
7. To use a record you must have access to its definition (often via `-include_lib`).

# Construction / Recognition

## To Construct:
1. Define the record with `-record(Name, {field1, field2 = Default, ...})`.
2. Create an instance with `#Name{field1 = Value, ...}`; unset fields take their defaults.
3. Access a field via `Var#Name.field` or extract it in a pattern `#Name{field = Var}`.

## To Recognize:
1. Look for `-record` directives and `#Name{...}` / `Var#Name.field` syntax.

# Context & Application

- **Typical contexts**: Grouping a fixed set of related fields known at compile time.
- **Common applications**: Process state, configuration structures; the OTP `inet` module's `hostent` record.
- **Historical/stylistic notes**: The shell command `rr` reads record definitions so the shell can display tuples as records.

# Examples

**Example 1** (p. 40): The `hostent` record with default values:

```erlang
-record(hostent,
    {
        h_name,           % offical name of host
        h_aliases = [],   % alias list
        h_addrtype,       % host address type
        h_length,         % length of address
        h_addr_list = []  % list of addresses from name server
    }).
```

**Example 2** (p. 41): Extracting a field by pattern matching in a function:

```erlang
type(Addr) ->
    {ok, #hostent{h_addrtype=AddrType}} = inet:gethostbyaddr(Addr),
    AddrType.
```

# Relationships

## Builds Upon
- *(none — foundational)*

## Enables
- *(none specific in scope)*

## Related
- *(none additional)*

## Contrasts With
- **Maps** — Maps are a built-in type with runtime-variable fields and any-term keys; records are compile-time-fixed, atom-keyed, and faster.

# Common Errors

- **Error**: Using a record without including its definition in the module.
  **Correction**: `-include` or `-include_lib` the file defining the record before use.
- **Error**: Changing a record definition but not recompiling every module that uses it.
  **Correction**: Recompile all dependents; mismatched versions throw exceptions or silently access wrong fields.

# Common Confusions

- **Confusion**: Believing maps make records obsolete.
  **Clarification**: "In practice they each fulfill different needs and both are useful" — records for fixed compile-time fields, maps for runtime-variable fields (p. 43).

# Source Reference

Chapter 1: Introducing Erlang, Section "Records," pages 40-42. See the "Correct Record Versions" sidebar on p. 42.

# Verification Notes

- Definition source: Direct quotes from pp. 40-43.
- Confidence rationale: HIGH — explicit definition with the `hostent` example.
- Uncertainties: None.
- Cross-reference status: Verified against planned cards.
- Re-extraction notes: Fresh extraction — no pre-existing card for this source.
</content>
</invoke>
