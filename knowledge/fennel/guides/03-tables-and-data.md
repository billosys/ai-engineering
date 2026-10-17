# Tables and Data

Square brackets and braces describe different uses of the same mutable Lua table.
Choose operations by the data’s contract: a dense sequence, an unordered mapping,
or a deliberately sparse indexed structure.

Strengths describe this skill’s guidance: **MUST** marks a semantic requirement,
**SHOULD** a default with contextual exceptions, **CONSIDER** an optional technique,
and **AVOID** a recurrent trap. See [sources and licensing](./00-sources-and-license.md).

## DT-01: Keep ordinary sequences dense and one-based

**Strength**: SHOULD

**Summary**: Use table.remove to delete a sequence element; assigning nil leaves a hole.

```fennel
;; BAD: nil deletion truncates ipairs traversal
(let [items [:a :b :c]]
  (set (. items 2) nil)
  (assert (= 1 (accumulate [n 0 _ _value (ipairs items)] (+ n 1)))))
```

```fennel
;; GOOD: sequence removal shifts later elements
(let [items [:a :b :c]]
  (table.remove items 2)
  (assert (= 2 (length items)))
  (assert (= :c (. items 2))))
```

**Rationale**: `ipairs` starts at 1 and stops at the first nil. A sequence with holes has no
reliable length for ordinary array algorithms. Sparse tables are valid when designed
as maps with an explicit iteration/count policy; do not accidentally treat them as
dense sequences.

**Sources**: [Tutorial: Sequential Tables](https://git.sr.ht/~technomancy/fennel/tree/9af5e47fa7ddea806544d15507412ddc51bd046d/item/tutorial.md#L192); [Reference: length](https://git.sr.ht/~technomancy/fennel/tree/9af5e47fa7ddea806544d15507412ddc51bd046d/item/reference.md#L1087).

## DT-02: Distinguish absent from false

**Strength**: MUST

**Summary**: A nil field is absent; false is present data. Default only on nil when false is valid.

```fennel
;; BAD: or replaces an explicitly disabled option
(let [options {:enabled false}]
  (assert (= true (or options.enabled true))))
```

```fennel
;; GOOD: a nil check preserves false
(let [options {:enabled false}
      enabled? (if (= nil options.enabled) true options.enabled)]
  (assert (= false enabled?)))
```

**Rationale**: Assigning nil removes a key, and nil cannot be a key. A map cannot represent a
separate “present with nil value” state without an additional tag or sentinel.
For configuration booleans, `(or value default)` is often the wrong policy.

**Sources**: [Tutorial: table absence](https://git.sr.ht/~technomancy/fennel/tree/9af5e47fa7ddea806544d15507412ddc51bd046d/item/tutorial.md#L405); [Reference: truth in if](https://git.sr.ht/~technomancy/fennel/tree/9af5e47fa7ddea806544d15507412ddc51bd046d/item/reference.md#L927).

## DT-03: Do not depend on pairs ordering

**Strength**: MUST

**Summary**: Use ipairs for dense sequences and impose ordering explicitly when map output must be deterministic.

```fennel
;; BAD: a sequence does not make pairs ordered
(let [items [:a :b :c]
      seen (icollect [_ value (pairs items)] value)]
  ;; Its length is known; its iteration order is not promised.
  (assert (= 3 (length seen))))
```

```fennel
;; GOOD: sort map keys before producing ordered output
(let [counts {:z 2 :a 1}
      keys (icollect [key _value (pairs counts)] key)]
  (table.sort keys)
  (assert (= "a,z" (table.concat keys ","))))
```

**Rationale**: Use `pairs` when order is irrelevant. Sorting keys also requires a defined
comparator if key types differ or a domain-specific ordering is needed. Neither the
literal order of braces nor an observed stable run establishes an ordering contract.

**Sources**: [Lua Primer: Iteration](https://git.sr.ht/~technomancy/fennel/tree/9af5e47fa7ddea806544d15507412ddc51bd046d/item/lua-primer.md#L63).

## DT-04: Use destructuring and static field access deliberately

**Strength**: SHOULD

**Summary**: Destructure a group of fields; use dotted access for static keys and . for computed keys.

```fennel
;; BAD: repeated dynamic lookup obscures a known shape
(let [point {:x 3 :y 4}]
  (assert (= 25 (+ (* (. point :x) (. point :x)) (* (. point :y) (. point :y))))))
```

```fennel
;; GOOD: destructuring names the fields once
(let [{: x : y} {:x 3 :y 4}]
  (assert (= 25 (+ (* x x) (* y y)))))
```

**Rationale**: Destructuring is convenient but is not validation: missing fields become nil.
Use pattern matching or explicit checks for untrusted shapes. `{: x}` is shorthand
for the string key `"x"` mapped to the binding `x`; `&as` retains the original table.

**Sources**: [Reference: let destructuring](https://git.sr.ht/~technomancy/fennel/tree/9af5e47fa7ddea806544d15507412ddc51bd046d/item/reference.md#L378); [Style: field access](https://git.sr.ht/~technomancy/fennel/tree/9af5e47fa7ddea806544d15507412ddc51bd046d/item/style.md#L407).

## DT-05: Use comprehensions with their actual result contracts

**Strength**: SHOULD

**Summary**: icollect builds a dense sequence, collect emits key/value pairs, and nil results are omitted.

```fennel
;; BAD: using false as a filtering sentinel keeps it
(let [items (icollect [_ x (ipairs [1 2 3])]
              (if (< 1 x) x false))]
  (assert (= false (. items 1)))
  (assert (= 3 (length items))))
```

```fennel
;; GOOD: nil is the omit signal
(let [items (icollect [_ x (ipairs [1 2 3])]
              (if (< 1 x) (* x x)))
      labels (collect [_ x (ipairs items)] (tostring x) x)]
  (assert (= "4,9" (table.concat items ",")))
  (assert (= 9 (. labels :9))))
```

**Rationale**: `collect` does not return pairs as nested vectors: its body emits a key and value,
either directly or via `values`. `&into` mutates an existing destination. Use
`accumulate`/`faccumulate` for reduction rather than inventing a built-in `reduce`.

**Sources**: [Reference: comprehensions and accumulation](https://git.sr.ht/~technomancy/fennel/tree/9af5e47fa7ddea806544d15507412ddc51bd046d/item/reference.md#L1146).

## DT-06: Know identity equality and map emptiness

**Strength**: MUST

**Summary**: Ordinary table equality compares identity; length is not a map-entry count.

```fennel
;; BAD: equal contents do not make separate tables equal
(assert (not= {:x 1} {:x 1}))
(assert (= 0 (length {:x 1})))
```

```fennel
;; GOOD: compare the actual fields required by the contract
(let [left {:x 1}
      right {:x 1}]
  (assert (= left.x right.x))
  (assert (not= nil (next left)))
  (assert (= left left)))
```

**Rationale**: For ordinary tables without an equality metamethod, `=` compares object identity.
Use explicit field assertions or a chosen deep-equality routine when that is the
contract. Metatables can customize behavior; do not infer general structural equality
from a special type’s `__eq`. `next` tests actual emptiness.

**Sources**: [Tutorial: Gotchas](https://git.sr.ht/~technomancy/fennel/tree/9af5e47fa7ddea806544d15507412ddc51bd046d/item/tutorial.md#L552); [Lua Primer: table module](https://git.sr.ht/~technomancy/fennel/tree/9af5e47fa7ddea806544d15507412ddc51bd046d/item/lua-primer.md#L137).

## Summary Table

| Pattern | Strength | Rule |
|---|---|---|
| DT-01 | SHOULD | Keep ordinary sequences dense and one-based |
| DT-02 | MUST | Distinguish absent from false |
| DT-03 | MUST | Do not depend on pairs ordering |
| DT-04 | SHOULD | Use destructuring and static field access deliberately |
| DT-05 | SHOULD | Use comprehensions with their actual result contracts |
| DT-06 | MUST | Know identity equality and map emptiness |

## Related Guidelines

- [Functions and Control Flow](./04-functions-and-control-flow.md)
- [Pattern Matching](./05-pattern-matching.md)
- [Anti-Patterns](./11-anti-patterns.md)
