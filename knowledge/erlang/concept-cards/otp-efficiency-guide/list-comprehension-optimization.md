---
concept: List Comprehension Optimization
slug: list-comprehension-optimization
category: performance
subcategory: list-optimization
tier: intermediate
source: "Erlang Efficiency Guide"
source_slug: otp-efficiency-guide
authors: "Ericsson/OTP Team"
chapter: "List Handling"
chapter_number: null
pdf_page: null
section: "List Comprehensions"
extraction_confidence: high
aliases:
  - "list comprehension compilation"
  - "unused list comprehension optimization"
prerequisites:
  - list-construction-efficiency
extends: []
related:
  - body-vs-tail-recursive-list-functions
contrasts_with: []
answers_questions:
  - "How are list comprehensions compiled in Erlang?"
  - "When does the compiler optimize away list construction in comprehensions?"
---

# Quick Definition

List comprehensions are compiled into local recursive functions equivalent to body-recursive list construction. When the compiler determines the result list will not be used, it optimizes away the list construction entirely, executing only the side effects.

# Core Definition

A list comprehension `[Expr(E) || E <- List]` is basically translated to a local function that constructs the result list using body recursion: `[Expr(E)|'lc^0'(Tail, Expr)]`. If the result of the list comprehension will obviously not be used -- not assigned to a variable, not passed to another function, and not returned -- a list will not be constructed. The compiler also understands that assigning to `_` means the value will not be used, and the comprehension will also be optimized in that case (Ericsson/OTP Team, "List Handling," section "List Comprehensions").

# Prerequisites

- **list-construction-efficiency** -- Understanding how lists are built is needed to appreciate how comprehensions are compiled

# Key Properties

1. List comprehensions compile to local recursive functions
2. The compiled form uses body recursion (not tail recursion with accumulator)
3. When the result is obviously unused, the compiler eliminates list construction
4. "Obviously unused" means: not assigned to a variable, not passed to a function, not returned
5. Assigning to `_` also counts as "unused" -- the optimization still applies
6. When optimized for side effects only, the compiled form calls `Expr(E)` without consing

# Construction / Recognition

## Recognizing When the Optimization Applies

1. The comprehension result is not assigned: `[io:put_chars(E) || E <- List], ok.`
2. The comprehension result is assigned to `_`: `_ = [io:put_chars(E) || E <- List], ok.`
3. The comprehension result is in a position where it is discarded (e.g., non-final expression in a case clause followed by other expressions)

## Recognizing When the Optimization Does NOT Apply

1. The result is assigned to a named variable: `Result = [f(E) || E <- List]`
2. The result is returned from the function
3. The result is passed to another function: `g([f(E) || E <- List])`

# Context & Application

This optimization matters for list comprehensions used purely for side effects (logging, I/O, sending messages). Without the optimization, the runtime would allocate cons cells for a result list that is immediately discarded.

**Typical contexts:**
- Logging each element: `[logger:info("~p", [E]) || E <- List]`
- Sending messages: `[Pid ! Msg || Pid <- Pids]`
- Any "for-each" usage of list comprehensions

**Caveat:** Using list comprehensions for side effects is idiomatic in Erlang but can be surprising to developers from other functional languages where comprehensions are always expected to produce a value.

# Examples

**Side-effect comprehension with implicit discard** (source: "List Comprehensions" section):

```erlang
[io:put_chars(E) || E <- List],
ok.
```

The result is not assigned or returned. The compiler generates code equivalent to:

```erlang
'lc^0'([E|Tail], Expr) ->
    Expr(E),
    'lc^0'(Tail, Expr);
'lc^0'([], _Expr) -> [].
```

No list is constructed.

**Side-effect comprehension in a case clause** (source: same section):

```erlang
case Var of
    ... ->
        [io:put_chars(E) || E <- List];
    ... ->
end,
some_function(...),
```

The value is not used after the case expression, so the optimization applies.

**Explicit underscore assignment** (source: same section):

```erlang
_ = [io:put_chars(E) || E <- List],
ok.
```

The compiler recognizes `_` as "unused" and applies the same optimization.

**Normal (non-optimized) compilation** (source: same section):

A list comprehension `[Expr(E) || E <- List]` compiles to:

```erlang
'lc^0'([E|Tail], Expr) ->
    [Expr(E)|'lc^0'(Tail, Expr)];
'lc^0'([], _Expr) -> [].
```

This is body-recursive, constructing the result list as it recurses.

# Relationships

## Related

- **body-vs-tail-recursive-list-functions** -- List comprehensions compile to body-recursive style, which is discussed in the recursion comparison

# Common Errors

- **Error**: Using a list comprehension for side effects and accidentally capturing the result, preventing optimization
  **Correction**: Ensure the result is not assigned to a named variable if you only want side effects

# Common Confusions

- **Confusion**: Thinking list comprehensions are always less efficient than explicit recursion
  **Clarification**: List comprehensions compile to the same recursive pattern that hand-written code would use. The compiler may even optimize away the list construction when the result is unused.

- **Confusion**: Believing `_ = [f(E) || E <- List]` prevents the optimization
  **Clarification**: The compiler specifically recognizes `_` as an unused binding and still applies the optimization.

# Source Reference

"List Handling," section "List Comprehensions." The source shows the compiled form of a list comprehension (both normal and side-effect-optimized), provides three examples of when the optimization applies (implicit discard, case clause, underscore assignment), and explicitly states that `_` assignment triggers the optimization.

# Verification Notes

- Definition: Directly from source -- "A list comprehension ... is basically translated to a local function"
- Compiled form: Directly from source showing the `'lc^0'` function
- Optimization trigger: Explicitly stated -- "If the result of the list comprehension will obviously not be used, a list will not be constructed"
- Underscore handling: Explicitly stated -- "The compiler also understands that assigning to _ means that the value will not be used"
- All three optimization examples from source
- Confidence: HIGH -- explicit compiled forms and optimization rules in official OTP documentation
