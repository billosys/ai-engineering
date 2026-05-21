---
# === CORE IDENTIFICATION ===
concept: Be Restrictive Rule
slug: be-restrictive-rule

# === CLASSIFICATION ===
category: error-handling
subcategory: coding-style
tier: intermediate

# === PROVENANCE ===
source: "OTP Design Principles"
source_slug: otp-design-principles
authors: "Ericsson AB"
chapter: "Secure Coding Guidelines"
chapter_number: null
pdf_page: null
section: "Rules / Secure Coding Standard"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "STL-001"
  - "restrictive pattern matching"
  - "deny by default coding"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - secure-error-handling
extends: []
related:
  - supervision-tree
  - atom-exhaustion
  - input-validation
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What does the Be Restrictive rule (STL-001) mean?"
  - "Why should Erlang code avoid catch-all patterns?"
  - "How does restrictive pattern matching improve security?"
  - "What are the DO and DO NOT patterns for restrictive Erlang code?"
  - "Why should you match on specific values rather than using wildcards?"
---

# Quick Definition

The Be Restrictive rule (STL-001, priority: High) states that Erlang code should be written as restrictively as possible, provoking errors whenever anything unexpected happens rather than silently continuing. This makes program bugs (the third error category) visible as crashes instead of allowing silent continuation in an invalid state.

# Core Definition

As stated in the Secure Coding Guidelines under STL-001: "Erlang code should be written as restrictively as possible, to provoke errors whenever anything unexpected happens. The idea is to make the third error category, program bugs, visible as a crash instead of silently continuing." The rule is directly tied to the Error Handling section's principle that "encountering something unexpected means that we have left the known and tested path, and continuing greatly increases the risk for bugs and security issues."

Rule priority: High. Related CWEs: CWE-252 (Unchecked Return Value), CWE-253 (Incorrect Check of Function Return Value), CWE-391 (Unchecked Error Condition), CWE-392 (Missing Report of Error Condition), CWE-394 (Unexpected Status Code or Return Value), CWE-396 (Declaration of Catch for Generic Exception). Related OWASP risks: A10:2025.

# Prerequisites

- **Secure Error Handling** -- the Be Restrictive rule is an application of the deny-by-default error handling philosophy.

# Key Properties

1. **Match specific values, not wildcards** -- use exact atoms (`true`, `false`) instead of catch-all `_` patterns.
2. **Assert return values** -- use `ok = file:write(Fd, Data)` instead of `_ = file:write(Fd, Data)`.
3. **Match specific list structures** -- use `foo([]) -> []` instead of `foo(_) -> []`.
4. **Prefer explicit atom conversion** -- map known input values explicitly rather than using `binary_to_existing_atom`.
5. **Catch specific exceptions** -- use `catch error:specific_error` instead of `catch error:_`.
6. **Use tagged return values** -- prefer `{changed, List}` over untagged `List` to prevent misspelled-atom confusion.
7. **Use strict generators in comprehensions** -- prefer `<:-` (strict) over `<-` (filtering) to avoid silently dropping non-matching entries.

# Construction / Recognition

## DO Patterns:

```erlang
%% Match specific boolean results
case operation(A, B) of
    true -> C;
    false -> D
end.

%% Assert success
ok = file:write(Fd, Data)

%% Match specific list structure
foo([First | Rest]) ->
    [bar(First) | foo(Rest)];
foo([]) ->
    [].

%% Explicit atom conversion for known sets
input_to_atom(<<"foo">>) -> foo;
input_to_atom(<<"bar">>) -> bar;
input_to_atom(<<"quux">>) -> quux.

%% Catch specific exceptions
try operation(A, B) of
    {ok, X} -> something(X)
catch
    error:specific_error -> error
end.

%% Use tagged return values
case my_filter(List0, unchanged) of
    unchanged -> List0;
    {changed, List} -> List
end

%% Use strict generators
[op(L) || #my_record{}=L <:- ListOfMyRecord]
```

## DO NOT Patterns:

```erlang
%% Catch-all hides extension bugs and misspellings
case operation(A, B) of
    true -> C;
    _ -> D    %% What if operation/2 returns 'maybe'?
end.

%% Discarding return value hides write failures
_ = file:write(Fd, Data)

%% Catch-all hides non-list input
foo([First | Rest]) ->
    [bar(First) | foo(Rest)];
foo(_) ->
    [].

%% Dynamic conversion allows unexpected atoms
input_to_atom(Text) -> binary_to_existing_atom(Text).

%% Generic exception catch hides unexpected errors
try operation(A, B) of
    {ok, X} -> something(X)
catch
    error:_ -> error
end.

%% Untagged value can match misspelled atoms
case my_filter(List0, unchanged) of
    unchanged -> List0;
    List -> List    %% What if 'uchanged' is returned?
end

%% Filtering generator silently drops non-matching entries
[op(L) || #my_record{}=L <- ListOfMyRecord]
```

# Context & Application

STL-001 is the most fundamental coding rule in the Secure Coding Guidelines, rated High priority. It operationalizes the error handling philosophy into concrete coding patterns. Every other secure coding rule in the document builds upon or complements this principle. The rule directly addresses six CWEs related to unchecked or improperly checked return values and error conditions. It is especially important when processing untrusted input, as overly permissive patterns can allow unexpected data to flow through the system unchecked.

# Examples

**Example 1** (secure_coding.md, STL-001): Case expression with boolean result:
```erlang
%% DO
case operation(A, B) of
    true -> C;
    false -> D
end.

%% DO NOT -- What if operation/2 is extended to also return
%% 'maybe', or someone misspells 'true' as 'tru'?
case operation(A, B) of
    true -> C;
    _ -> D
end.
```

**Example 2** (secure_coding.md, STL-001): Asserting success of side-effecting operations:
```erlang
%% DO
ok = file:write(Fd, Data)

%% DO NOT
_ = file:write(Fd, Data)
```

**Example 3** (secure_coding.md, STL-001): Strict vs filtering comprehension generators:
```erlang
%% PREFER -- crashes if entry does not match
[op(L) || #my_record{}=L <:- ListOfMyRecord]

%% AVOID -- silently filters out non-matching entries
[op(L) || #my_record{}=L <- ListOfMyRecord]
```

# Relationships

## Builds Upon
- **Secure Error Handling** -- STL-001 is the concrete coding practice that implements the deny-by-default execution philosophy

## Enables
- **Atom Exhaustion** prevention -- explicit atom mapping (the preferred approach) is also the best defense against atom exhaustion
- **Input Validation** -- restrictive patterns are the first line of defense for input validation

## Related
- **supervision-tree** -- supervision trees handle the crashes that restrictive patterns provoke on unexpected input

## Contrasts With
- No direct contrasts in source, though the rule implicitly contrasts with defensive programming that uses catch-all patterns to prevent crashes.

# Common Errors

- **Error**: Using `_` as a catch-all in case expressions to handle "the other case."
  **Correction**: Match every expected value explicitly. If only `true` and `false` are expected, match both. A catch-all hides bugs where the function is extended to return new values or where values are misspelled.

- **Error**: Ignoring return values with `_ = some_function()`.
  **Correction**: Match on the expected return value (e.g., `ok = file:write(Fd, Data)`) so failures are immediately visible as crashes.

- **Error**: Using `catch error:_` to catch all errors of a given class.
  **Correction**: Catch only the specific error reasons you expect and know how to handle. Generic exception catching masks unexpected errors.

# Common Confusions

- **Confusion**: Thinking restrictive patterns make code fragile or crash-prone.
  **Clarification**: The crashes are desirable -- they surface bugs immediately rather than allowing silent continuation in an invalid state. The supervision tree handles recovery. "Continuing greatly increases the risk for bugs and security issues."

- **Confusion**: Thinking `binary_to_existing_atom` is the preferred solution for atom conversion.
  **Clarification**: While safer than `binary_to_atom`, the source states that explicit conversion (pattern matching on known values) is "AND PREFER" -- `binary_to_existing_atom` can return any atom in the system, not just those valid in context.

# Source Reference

OTP Design Principles, Secure Coding Guidelines, STL-001 rule (secure_coding.md, lines 402-501). Also references the Error Handling section (lines 142-202).

# Verification Notes

- Definition source: Directly quoted from the STL-001 rule section with all code examples reproduced from the source.
- Confidence rationale: High -- the most extensively documented rule in the chapter with seven distinct DO/DO NOT code examples and six CWE references.
- Uncertainties: None.
- Cross-reference status: References CWE-252, CWE-253, CWE-391, CWE-392, CWE-394, CWE-396, OWASP A10:2025. Cross-references secure-error-handling, supervision-tree, atom-exhaustion.
