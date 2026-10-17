# Functions and Control Flow

Functions are Lua functions; Fennel adds expression syntax and optional nil checking.
Multiple return values need special attention at every call boundary.

Strengths describe this skill’s guidance: **MUST** marks a semantic requirement,
**SHOULD** a default with contextual exceptions, **CONSIDER** an optional technique,
and **AVOID** a recurrent trap. See [sources and licensing](./00-sources-and-license.md).

## FN-01: Choose fn or lambda by the argument contract

**Strength**: SHOULD

**Summary**: fn accepts missing/extra arguments; lambda checks required arguments for nil, not full types or exact arity.

```fennel
;; BAD: missing input silently becomes nil with fn
(fn identity [value] value)
(assert (= nil (identity)))
(assert (= 1 (identity 1 2)))
```

```fennel
;; GOOD: lambda expresses a non-nil boundary and optional parameter
(lambda label [name ?suffix]
  (.. name (or ?suffix "")))

(assert (= :A! (label :A "!")))
(let [[ok?] [(pcall label nil)]]
  (assert (= false ok?)))
```

**Rationale**: Use `fn` where Lua’s permissiveness is intended or checks are already performed.
`lambda`/`λ` rejects nil for required bindings; false remains valid, extra arguments
are still ignored, and types/ranges need their own validation. `--lambda-as-fn`
removes this check and changes the contract.

**Sources**: [Reference: fn and lambda](https://git.sr.ht/~technomancy/fennel/tree/9af5e47fa7ddea806544d15507412ddc51bd046d/item/reference.md#L111).

## FN-02: Control expansion of multiple return values

**Strength**: MUST

**Summary**: A final function call in an argument list can expand; use pick-values when the consumer needs exactly one value.

```fennel
;; BAD: an incidental second return changes the call arity
(fn item [] (values :widget :metadata))
(assert (= 2 (select "#" (item))))
```

```fennel
;; GOOD: explicitly select one value at a variadic boundary
(fn item [] (values :widget :metadata))
(let [items []]
  (table.insert items (pick-values 1 (item)))
  (assert (= :widget (. items 1)))
  (assert (= 1 (length items))))
```

**Rationale**: Lua adjusts multiple values according to expression position. A final call in an
argument list or sequence literal may expand; non-final calls are adjusted to one
value. Operators still have a compile-time number of operands, so they are not a
runtime variadic reduction. For example, `table.insert` has both two- and three-
argument forms, and leaking a second return can select the wrong one.

**Sources**: [Reference: pick-values](https://git.sr.ht/~technomancy/fennel/tree/9af5e47fa7ddea806544d15507412ddc51bd046d/item/reference.md#L885); [Style: multiple-value return hazard](https://git.sr.ht/~technomancy/fennel/tree/9af5e47fa7ddea806544d15507412ddc51bd046d/item/style.md#L417).

## FN-03: Preserve nil-containing varargs with an explicit count

**Strength**: MUST

**Summary**: Do not close over ... or treat a plain table’s length as the original vararg count.

```fennel
;; BAD: a plain table loses trailing nil cardinality
(fn argument-count [...] (length [...]))
(assert (= 1 (argument-count :a nil nil)))
```

```fennel
;; GOOD: capture count and values before making a closure
(fn capture [...]
  (let [n (select "#" ...)
        args [...]
        unpack-values (or table.unpack _G.unpack)]
    (fn [] (unpack-values args 1 n))))

(let [restore (capture :a nil nil)]
  (assert (= 3 (select "#" (restore))))
  (assert (= :a (restore))))
```

**Rationale**: Varargs belong to the immediately enclosing variadic function and are not a
first-class sequence. Explicit bounds preserve trailing nils during unpacking.
The runtime fallback above supports Lua 5.1’s global `unpack`; the compiler macro
environment separately supplies normalized `pack` and `unpack` helpers.

**Sources**: [Tutorial: Variadic Functions](https://git.sr.ht/~technomancy/fennel/tree/9af5e47fa7ddea806544d15507412ddc51bd046d/item/tutorial.md#L484); [Reference: Compiler Environment](https://git.sr.ht/~technomancy/fennel/tree/9af5e47fa7ddea806544d15507412ddc51bd046d/item/reference.md#L1731).

## FN-04: Separate numeric loops from iterators

**Strength**: SHOULD

**Summary**: Use for for inclusive numeric ranges, each for iterators, and &until for visible early termination.

```fennel
;; BAD: an unguarded numeric loop always visits the full range
(var visited 0)
(for [_i 1 5] (set visited (+ visited 1)))
(assert (= 5 visited))
```

```fennel
;; GOOD: the guard is checked before the body
(var visited 0)
(for [_i 1 5 &until (<= 2 visited)]
  (set visited (+ visited 1)))

(assert (= 2 visited))
(assert (= nil (for [_i 1 0] :unused)))
```

**Rationale**: `for`, `each` and `while` return nil, not the last iteration’s value. Use an
accumulator or comprehension for results. Put the stopping condition in the binding
clause where readers can see it; a true initial `&until` means zero body executions.

**Sources**: [Reference: each, for and while](https://git.sr.ht/~technomancy/fennel/tree/9af5e47fa7ddea806544d15507412ddc51bd046d/item/reference.md#L962).

## FN-05: Keep recursion in a real tail position

**Strength**: CONSIDER

**Summary**: Use tail! when bounded stack use is a correctness requirement, and test a large input.

```fennel
;; BAD: compile error: work follows the asserted tail call
(fn walk [n]
  (when (< 0 n)
    (tail! (walk (- n 1)))
    (print n)))
```

```fennel
;; GOOD: the recursive result is returned directly
(fn total [n acc]
  (if (= n 0)
      acc
      (tail! (total (- n 1) (+ acc n)))))

(assert (= 50005000 (total 10000 0)))
```

**Rationale**: Lua optimizes actual tail calls. Naming a function recursive does not guarantee
bounded stack use, and wrapping its result in arithmetic destroys tail position.
Fennel’s `tail!` gives a compile-time check against later refactors that add work.

**Sources**: [Reference: tail!](https://git.sr.ht/~technomancy/fennel/tree/9af5e47fa7ddea806544d15507412ddc51bd046d/item/reference.md#L1408).

## Summary Table

| Pattern | Strength | Rule |
|---|---|---|
| FN-01 | SHOULD | Choose fn or lambda by the argument contract |
| FN-02 | MUST | Control expansion of multiple return values |
| FN-03 | MUST | Preserve nil-containing varargs with an explicit count |
| FN-04 | SHOULD | Separate numeric loops from iterators |
| FN-05 | CONSIDER | Keep recursion in a real tail position |

## Related Guidelines

- [Pattern Matching](./05-pattern-matching.md)
- [Errors and Resources](./07-errors-and-resources.md)
- [Lua Interop and Distribution](./10-lua-interop-and-distribution.md)
