# Style and Naming

These defaults adapt the upstream style guide. Its opening explicitly asks for
judgment and context; stylistic preferences are not compiler requirements. Let
fnlfmt settle routine layout and spend review attention on meaning.

Strengths describe this skill’s guidance: **MUST** marks a semantic requirement,
**SHOULD** a default with contextual exceptions, **CONSIDER** an optional technique,
and **AVOID** a recurrent trap. See [sources and licensing](./00-sources-and-license.md).

## ST-01: Let structure determine indentation

**Strength**: SHOULD

**Summary**: Use spaces, body indentation, grouped closing delimiters and short lines; run fnlfmt.

```fennel
;; BAD: valid code with distracting layout
(fn total [a b]
        (+ a b
        )
)
(assert (= 5 (total 2 3)))
```

```fennel
;; GOOD: ordinary layout makes nesting visible
(fn total [a b]
  (+ a b))

(assert (= 5 (total 2 3)))
```

**Rationale**: Body-taking forms generally indent by two spaces. Regular calls align continued
arguments. Prefer roughly 80 columns. The upstream exceptions for commented-out
forms and large data tables are contextual, not a reason to place every closing
parenthesis on a separate line. `fnlfmt --check file.fnl` reports drift.

**Sources**: [Style: Parentheses and indentation](https://git.sr.ht/~technomancy/fennel/tree/9af5e47fa7ddea806544d15507412ddc51bd046d/item/style.md#L20).

## ST-02: Name intent and effects

**Strength**: SHOULD

**Summary**: Use lower-case hyphenated names; `?` for predicates, `!` for principally destructive operations, `->` for conversions.

```fennel
;; BAD: names obscure the distinction between inspection and mutation
(fn isReady [x] (= x.status :ready))
(fn change [x] (set x.status :ready))
(let [x {}] (change x) (assert (isReady x)))
```

```fennel
;; GOOD: names expose the API’s intent
(fn ready? [x] (= x.status :ready))
(fn mark-ready! [x] (set x.status :ready))
(let [x {}] (mark-ready! x) (assert (ready? x)))
```

**Rationale**: Do not attach `!` indiscriminately to every function that happens to have an
effect. Use descriptive local names, `_unused` for deliberately ignored values,
`?optional` for potentially nil values, and `self` for an explicit method receiver.
Export underscore names when that improves a Lua caller’s experience.

**Sources**: [Style: Names](https://git.sr.ht/~technomancy/fennel/tree/9af5e47fa7ddea806544d15507412ddc51bd046d/item/style.md#L234).

## ST-03: Use string notation to communicate role

**Strength**: SHOULD

**Summary**: Use colon strings for opaque names and quoted strings when their text matters.

```fennel
;; BAD: notation suggests a keyword type that does not exist
(let [keyword :ready]
  (assert (= :string (type keyword))))
```

```fennel
;; GOOD: literal and name conventions share the same string type
(let [status :ready
      message "Ready to receive input"]
  (assert (= :ready status))
  (assert (= :string (type message))))
```

**Rationale**: `:ready` is exactly the Lua string `"ready"`, not a distinct keyword object.
Use ordinary quoted text for messages, paths and contents; use colon notation for
keys and labels where that improves readability. Source formatting may normalize
some representations without changing the string.

**Sources**: [Style: colon-style strings](https://git.sr.ht/~technomancy/fennel/tree/9af5e47fa7ddea806544d15507412ddc51bd046d/item/style.md#L382); [Reference: string syntax](https://git.sr.ht/~technomancy/fennel/tree/9af5e47fa7ddea806544d15507412ddc51bd046d/item/reference.md#L92).

## ST-04: Prefer named intermediates when the subject changes

**Strength**: SHOULD

**Summary**: Use arrows for a clear pipeline; use let when names explain distinct steps.

```fennel
;; BAD: opaque pipeline mixes different conceptual subjects
(assert (= :3 (-> [1 2 3] (length) (tostring))))
```

```fennel
;; GOOD: name the derived quantity when it matters to the reader
(let [items [1 2 3]
      item-count (length items)]
  (assert (= :3 (tostring item-count))))
```

**Rationale**: Both examples compute the same result. The second is preferable when count is a
domain concept, not because arrows are intrinsically wrong. `->` inserts first,
`->>` inserts last; nil/false-short-circuiting arrows have separate semantics and
only carry one value.

**Sources**: [Style: arrow forms](https://git.sr.ht/~technomancy/fennel/tree/9af5e47fa7ddea806544d15507412ddc51bd046d/item/style.md#L397); [Reference: threading macros](https://git.sr.ht/~technomancy/fennel/tree/9af5e47fa7ddea806544d15507412ddc51bd046d/item/reference.md#L1339).

## ST-05: Document contracts rather than narrating syntax

**Strength**: SHOULD

**Summary**: Give public functions useful docstrings and use comments for constraints and reasons.

```fennel
;; BAD: comment repeats the expression and leaves its unit unexplained
(fn window [x]
  ;; Multiply x by two.
  (* x 2))

(assert (= 8 (window 4)))
```

```fennel
;; GOOD: documentation explains the caller-visible contract
(fn window-width [radius]
  "Return the full window width in samples for a radius in samples."
  (* radius 2))

(assert (= 8 (window-width 4)))
```

**Rationale**: Start a docstring with a short purpose sentence; document argument/return shapes
and failure conventions where relevant. Docstrings support editor/REPL discovery,
while explanatory user documentation still needs prose and use cases. Metadata is
normally omitted outside the REPL unless enabled; it has runtime costs.

**Sources**: [Style: Comments and Docstrings](https://git.sr.ht/~technomancy/fennel/tree/9af5e47fa7ddea806544d15507412ddc51bd046d/item/style.md#L314); [API: docstrings and metadata](https://git.sr.ht/~technomancy/fennel/tree/9af5e47fa7ddea806544d15507412ddc51bd046d/item/api.md#L556).

## Summary Table

| Pattern | Strength | Rule |
|---|---|---|
| ST-01 | SHOULD | Let structure determine indentation |
| ST-02 | SHOULD | Name intent and effects |
| ST-03 | SHOULD | Use string notation to communicate role |
| ST-04 | SHOULD | Prefer named intermediates when the subject changes |
| ST-05 | SHOULD | Document contracts rather than narrating syntax |

## Related Guidelines

- [Modules and API Design](./06-modules-and-api-design.md)
- [Setup, Tooling and Testing](./09-setup-tooling-and-testing.md)
