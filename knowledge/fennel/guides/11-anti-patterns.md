# Anti-Patterns and Review Checks

Use these checks before writing code and while reviewing a change. Follow the
related chapter for the full rule, exceptions and source rationale. These examples
are deliberately small so each plausible mistake has an observable consequence.

Strengths describe this skill’s guidance: **MUST** marks a semantic requirement,
**SHOULD** a default with contextual exceptions, **CONSIDER** an optional technique,
and **AVOID** a recurrent trap. See [sources and licensing](./00-sources-and-license.md).

## AP-01: Importing another Lisp’s runtime model

**Strength**: AVOID

**Summary**: Do not treat colon strings as keywords, tables as persistent vectors, or operators as ordinary functions.

```fennel
;; BAD: a supposedly independent persistent value is an alias
(let [before {:n 1}
      after before]
  (set after.n 2)
  (assert (= 2 before.n)))
```

```fennel
;; GOOD: choose fresh data for an independent result
(let [before {:n 1}
      after {:n (+ before.n 1)}]
  (assert (= 1 before.n))
  (assert (= 2 after.n)))
```

**Rationale**: Check callers for shared mutation and identity equality, not just the local
function’s syntax. Core ID-02 and table DT-06 cover the related contracts.

**Sources**: [From Clojure: Tables](https://git.sr.ht/~technomancy/fennel/tree/9af5e47fa7ddea806544d15507412ddc51bd046d/item/from-clojure.md#L154).

## AP-02: Using truth as presence or size

**Strength**: AVOID

**Summary**: Check nil, false and empty explicitly rather than translating another language’s truth conventions.

```fennel
;; BAD: zero and empty text are both truthy
(assert (= :yes (if 0 :yes :no)))
(assert (= :yes (if "" :yes :no)))
```

```fennel
;; GOOD: state the domain test
(let [text ""]
  (assert (= :empty (if (= 0 (length text)) :empty :nonempty))))
```

**Rationale**: A successful happy-path test with a nonempty string does not exercise this
boundary. ID-04, DT-02 and PM-02 distinguish truth, absence and matching.

**Sources**: [Reference: if](https://git.sr.ht/~technomancy/fennel/tree/9af5e47fa7ddea806544d15507412ddc51bd046d/item/reference.md#L927).

## AP-03: Discarding or accidentally forwarding returns

**Strength**: AVOID

**Summary**: Review every variadic call and error boundary for the number and meaning of results.

```fennel
;; BAD: wrapping in a plain table loses trailing nil count
(fn payload [] (values :a nil nil))
(assert (= 1 (length [(payload)])))
```

```fennel
;; GOOD: count or explicitly select the promised results
(fn payload [] (values :a nil nil))
(assert (= 3 (select "#" (payload))))
(assert (= 1 (select "#" (pick-values 1 (payload)))))
```

**Rationale**: FN-02 and FN-03 cover expansion and storage. An expected `(nil, error)` result
is not equivalent to a raised error; ER-02 shows how pcall can mask that confusion.

**Sources**: [Reference: pick-values](https://git.sr.ht/~technomancy/fennel/tree/9af5e47fa7ddea806544d15507412ddc51bd046d/item/reference.md#L885); [Tutorial: varargs](https://git.sr.ht/~technomancy/fennel/tree/9af5e47fa7ddea806544d15507412ddc51bd046d/item/tutorial.md#L484).

## AP-04: Assuming an empty pattern tests an empty table

**Strength**: AVOID

**Summary**: Use actual shape conditions and make pinning intentional.

```fennel
;; BAD: partial shape match accepts additional fields
(assert (= :hit (case {:hidden 1} {} :hit _ :miss)))
```

```fennel
;; GOOD: guard verifies actual emptiness
(let [data {:hidden 1}]
  (assert (= :miss (case data
                     (where {} (= nil (next data))) :hit
                     _ :miss))))
```

**Rationale**: PM-01 through PM-04 explain case/match, nil-admitting bindings, partial shapes
and guards. Adding a local in outer scope deserves a regression test when match
implicitly pins its name.

**Sources**: [Reference: table patterns](https://git.sr.ht/~technomancy/fennel/tree/9af5e47fa7ddea806544d15507412ddc51bd046d/item/reference.md#L570).

## AP-05: Testing a macro only with literals

**Strength**: AVOID

**Summary**: Exercise effects, name collisions, error inputs and multi-form bodies.

```fennel
;; BAD: the literal hides duplicate evaluation
(macro square [x]
  `(* ,x ,x))
(assert (= 9 (square 3)))
```

```fennel
;; GOOD: an effect counter proves the required evaluation count
(macro square [x]
  `(let [x# ,x] (* x# x#)))
(var calls 0)
(fn next! [] (set calls (+ calls 1))
  3)
(assert (= 9 (square (next!))))
(assert (= 1 calls))
```

**Rationale**: MC-02 through MC-06 cover evaluation count, hygienic locals, phase separation,
self-contained expansion imports and AST diagnostics. Format an actual macrodebug
expansion and inspect it; a pretty macro definition is insufficient evidence.

**Sources**: [Reference: Macro gotchas](https://git.sr.ht/~technomancy/fennel/tree/9af5e47fa7ddea806544d15507412ddc51bd046d/item/reference.md#L1664).

## AP-06: Confusing compile success with a working distribution

**Strength**: AVOID

**Summary**: Run emitted Lua through its actual consumer with only the intended shipped dependencies.

```fennel
;; BAD: this runs in the launcher but requires fennel at runtime
(assert (= :table (type (require :fennel))))
```

```fennel
;; GOOD: this complete example needs only the host Lua standard library
(fn double [x] (* x 2))
(assert (= 12 (double 6)))
```

**Rationale**: TL-02 covers optional AOT global checks. LI-04 covers searcher installation,
AOT modules and dynamic requires. LI-03 covers runtime-specific syntax. Source files
left on the development machine can hide packaging defects; test a clean output
directory and the real embedded host before promising support there.

**Sources**: [Setup: Embedding and AOT](https://git.sr.ht/~technomancy/fennel/tree/9af5e47fa7ddea806544d15507412ddc51bd046d/item/setup.md#L69); [API: compile checks](https://git.sr.ht/~technomancy/fennel/tree/9af5e47fa7ddea806544d15507412ddc51bd046d/item/api.md#L234).

## Summary Table

| Pattern | Strength | Rule |
|---|---|---|
| AP-01 | AVOID | Importing another Lisp’s runtime model |
| AP-02 | AVOID | Using truth as presence or size |
| AP-03 | AVOID | Discarding or accidentally forwarding returns |
| AP-04 | AVOID | Assuming an empty pattern tests an empty table |
| AP-05 | AVOID | Testing a macro only with literals |
| AP-06 | AVOID | Confusing compile success with a working distribution |

## Related Guidelines

- [Values and Core Idioms](./01-values-and-core-idioms.md)
- [Tables and Data](./03-tables-and-data.md)
- [Macros](./08-macros.md)
- [Lua Interop and Distribution](./10-lua-interop-and-distribution.md)
