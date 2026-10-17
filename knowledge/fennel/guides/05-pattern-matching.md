# Pattern Matching

Prefer `case` when patterns should introduce fresh names. Use `match` when its
implicit comparison against existing locals is intentional. Pattern success is a
specific test, not a general data-schema guarantee.

Strengths describe this skill’s guidance: **MUST** marks a semantic requirement,
**SHOULD** a default with contextual exceptions, **CONSIDER** an optional technique,
and **AVOID** a recurrent trap. See [sources and licensing](./00-sources-and-license.md).

## PM-01: Choose case versus match intentionally

**Strength**: SHOULD

**Summary**: case binds fresh names; match pins names that already exist in scope.

```fennel
;; BAD: an outer binding changes what match accepts
(let [expected :old]
  (assert (= :miss (match :new expected :hit _ :miss))))
```

```fennel
;; GOOD: case makes fresh binding intent explicit
(let [expected :old]
  (assert (= :new (case :new expected expected))))
```

**Rationale**: A harmless-looking new local can change a `match` pattern’s meaning. With `case`,
explicit pinning uses `(= outer-name)` inside a `where` pattern. Guards and bodies
can use outer bindings normally unless the pattern rebinds the same name.

**Sources**: [Reference: Binding Pinning](https://git.sr.ht/~technomancy/fennel/tree/9af5e47fa7ddea806544d15507412ddc51bd046d/item/reference.md#L653); [Reference: match](https://git.sr.ht/~technomancy/fennel/tree/9af5e47fa7ddea806544d15507412ddc51bd046d/item/reference.md#L690).

## PM-02: Distinguish nil-admitting patterns from truth tests

**Strength**: MUST

**Summary**: Ordinary pattern bindings reject nil but accept false; ?name allows nil and _ ignores the value.

```fennel
;; BAD: a bound pattern does not mean truthy
(assert (= :bound (case false value :bound _ :absent)))
```

```fennel
;; GOOD: match nil or truth conditions explicitly
(fn classify [value]
  (case value
    nil :absent
    false :disabled
    _ :present))

(assert (= :disabled (classify false)))
(assert (= :absent (classify nil)))
```

**Rationale**: Do not use a plain binding pattern as an equivalent of `if value`. A `?name`
binding includes nil; `_` and underscore-prefixed ignored bindings also match nil.
Order clauses from specific cases to broad fallbacks.

**Sources**: [Reference: case binding patterns](https://git.sr.ht/~technomancy/fennel/tree/9af5e47fa7ddea806544d15507412ddc51bd046d/item/reference.md#L470).

## PM-03: A sequence pattern is not an exact-length check

**Strength**: MUST

**Summary**: [] matches any table; ordinary sequence patterns permit extra elements.

```fennel
;; BAD: an empty pattern does not establish emptiness
(assert (= :matched (case [1 2] [] :matched _ :other)))
```

```fennel
;; GOOD: test the intended shape explicitly
(fn empty-table? [value]
  (case value
    (where [] (= nil (next value))) true
    _ false))

(assert (empty-table? {}))
(assert (= false (empty-table? [1])))
(assert (= false (empty-table? :x)))
```

**Rationale**: Table patterns are partial shape matches. Guard a dense sequence with `length`
when exact sequence size is required, or test actual keys for map schemas. `length`
on a sparse table cannot establish that all expected entries exist.

**Sources**: [Reference: case table patterns and guards](https://git.sr.ht/~technomancy/fennel/tree/9af5e47fa7ddea806544d15507412ddc51bd046d/item/reference.md#L570).

## PM-04: Use guards with coherent bindings

**Strength**: MUST

**Summary**: Every alternative whose shared guard reads a binding must supply that binding.

```fennel
;; BAD: compile error: b is unavailable in one alternative
(case [1 2 3]
  (where (or [a 1 2] [a b 3]) (< b 4)) a)
```

```fennel
;; GOOD: both alternatives bind the same names
(assert (= 1 (case [1 2 3]
               (where (or [a b 2] [a b 3]) (< b 4)) a
               _ :miss)))
```

**Rationale**: `where` combines structural matching with conditions. A disjunction of patterns
is not permission to use names that only some branches bind. Repeated names within
a pattern also impose equality, so use distinct names when equality is not intended.

**Sources**: [Reference: Guard Clauses](https://git.sr.ht/~technomancy/fennel/tree/9af5e47fa7ddea806544d15507412ddc51bd046d/item/reference.md#L596).

## Summary Table

| Pattern | Strength | Rule |
|---|---|---|
| PM-01 | SHOULD | Choose case versus match intentionally |
| PM-02 | MUST | Distinguish nil-admitting patterns from truth tests |
| PM-03 | MUST | A sequence pattern is not an exact-length check |
| PM-04 | MUST | Use guards with coherent bindings |

## Related Guidelines

- [Tables and Data](./03-tables-and-data.md)
- [Errors and Resources](./07-errors-and-resources.md)
