# Values and Core Idioms

Fennel provides syntax and compile-time checks over Lua. Design small, transparent
programs whose bindings and effects can be followed locally. Do not import a second
language’s runtime model just because the surface resembles a Lisp.

Strengths describe this skill’s guidance: **MUST** marks a semantic requirement,
**SHOULD** a default with contextual exceptions, **CONSIDER** an optional technique,
and **AVOID** a recurrent trap. See [sources and licensing](./00-sources-and-license.md).

## ID-01: Keep bindings lexical and global access visible

**Strength**: SHOULD

**Summary**: Use explicit parameters and module dependencies; reserve `_G` for deliberate host integration.

```fennel
;; BAD: dependency hidden in global state
(set _G.fennel-guide-offset 3)
(fn adjust [x] (+ x _G.fennel-guide-offset))
(assert (= 7 (adjust 4)))
(set _G.fennel-guide-offset nil)
```

```fennel
;; GOOD: dependency visible at the call
(fn adjust [x offset] (+ x offset))
(assert (= 7 (adjust 4 3)))
```

**Rationale**: A global dependency can change outside the function’s lexical context. Strict global
checking catches many typos, but `_G` explicitly bypasses it; keep that escape visible.
For an embedded host’s legitimate globals, configure its allowlist rather than
turning checking off for the whole application.

**Sources**: [Values: Transparency](https://git.sr.ht/~technomancy/fennel/tree/9af5e47fa7ddea806544d15507412ddc51bd046d/item/values.md#L35); [Tutorial: Strict global checking](https://git.sr.ht/~technomancy/fennel/tree/9af5e47fa7ddea806544d15507412ddc51bd046d/item/tutorial.md#L529).

## ID-02: Distinguish rebinding from table mutation

**Strength**: MUST

**Summary**: `let` and `local` prevent rebinding; they do not freeze the table or its aliases.

```fennel
;; BAD: assuming an alias is an independent snapshot
(let [original {:count 1}
      snapshot original]
  (set original.count 2)
  (assert (= 2 snapshot.count)))
```

```fennel
;; GOOD: copy the required fields when independence is needed
(let [original {:count 1}
      snapshot {:count original.count}]
  (set original.count 2)
  (assert (= 1 snapshot.count)))
```

**Rationale**: Both names in the first example point at the same Lua table. The second makes a
shallow copy of the selected scalar field; nested tables would still need an explicit
copy policy. Use `var` only when the binding itself must change.

**Sources**: [Tutorial: Locals and variables](https://git.sr.ht/~technomancy/fennel/tree/9af5e47fa7ddea806544d15507412ddc51bd046d/item/tutorial.md#L86); [From Clojure: Tables](https://git.sr.ht/~technomancy/fennel/tree/9af5e47fa7ddea806544d15507412ddc51bd046d/item/from-clojure.md#L154).

## ID-03: Use if for value selection

**Strength**: SHOULD

**Summary**: Use `if` for alternatives, `when` for effects, and keep mutation’s scope small.

```fennel
;; BAD: an and/or pseudo-conditional loses a legitimate false result
(let [selected? true
      result (or (and selected? false) :fallback)]
  (assert (= :fallback result)))
```

```fennel
;; GOOD: if preserves either branch’s actual value
(let [selected? true
      result (if selected? false :fallback)]
  (assert (= false result)))
```

**Rationale**: Fennel is expression-oriented; the last expression supplies the value. Do not
simulate Lua early returns or Clojure `cond` with invented forms: `if` already accepts
multiple condition/result pairs and an optional final fallback.

**Sources**: [Tutorial: Conditionals](https://git.sr.ht/~technomancy/fennel/tree/9af5e47fa7ddea806544d15507412ddc51bd046d/item/tutorial.md#L307); [Style: Specific Forms](https://git.sr.ht/~technomancy/fennel/tree/9af5e47fa7ddea806544d15507412ddc51bd046d/item/style.md#L393).

## ID-04: Treat only nil and false as false

**Strength**: MUST

**Summary**: Zero, empty strings and empty tables are truthy; check the actual property you mean.

```fennel
;; BAD: truth does not mean nonempty
(assert (= :present (if [] :present :empty)))
(assert (= :present (if "" :present :empty)))
(assert (= :present (if 0 :present :empty)))
```

```fennel
;; GOOD: test emptiness explicitly
(let [items {}]
  (assert (= :empty (if (= nil (next items)) :empty :present))))
```

**Rationale**: A condition tests Lua truth, not collection size. For a general table use `next`
to test emptiness; `length` describes a sequence boundary rather than counting map keys.

**Sources**: [Reference: if](https://git.sr.ht/~technomancy/fennel/tree/9af5e47fa7ddea806544d15507412ddc51bd046d/item/reference.md#L927); [Style: table emptiness](https://git.sr.ht/~technomancy/fennel/tree/9af5e47fa7ddea806544d15507412ddc51bd046d/item/style.md#L455).

## ID-05: Use only runtime functions as first-class values

**Strength**: MUST

**Summary**: Operators and built-in macros are compile-time forms, so wrap an operation when passing it as a value.

```fennel
;; BAD: compile error: an operator is not a runtime function
(local add +)
(add 2 3)
```

```fennel
;; GOOD: an ordinary function can be passed around
(fn add [a b] (+ a b))
(fn combine [f] (f 2 3))
(assert (= 5 (combine add)))
```

**Rationale**: There is no built-in `apply`, `map` or persistent-sequence library. Use the Lua
runtime library, `table.unpack`/`unpack` for argument expansion, and Fennel’s
comprehensions and accumulators for common transformations. Choose a real library
only when it is an actual project dependency.

**Sources**: [Reference: operators](https://git.sr.ht/~technomancy/fennel/tree/9af5e47fa7ddea806544d15507412ddc51bd046d/item/reference.md#L1053); [Tutorial: Gotchas](https://git.sr.ht/~technomancy/fennel/tree/9af5e47fa7ddea806544d15507412ddc51bd046d/item/tutorial.md#L552).

## Summary Table

| Pattern | Strength | Rule |
|---|---|---|
| ID-01 | SHOULD | Keep bindings lexical and global access visible |
| ID-02 | MUST | Distinguish rebinding from table mutation |
| ID-03 | SHOULD | Use if for value selection |
| ID-04 | MUST | Treat only nil and false as false |
| ID-05 | MUST | Use only runtime functions as first-class values |

## Related Guidelines

- [Tables and Data](./03-tables-and-data.md)
- [Functions and Control Flow](./04-functions-and-control-flow.md)
- [Anti-Patterns](./11-anti-patterns.md)
