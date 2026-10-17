# Macros

A macro transforms unevaluated syntax during compilation. Start with the ordinary
code you want to emit, then decide whether a new notation is worth its cost.
Keep lexical scope, evaluation count and runtime dependencies visible.

Strengths describe this skill’s guidance: **MUST** marks a semantic requirement,
**SHOULD** a default with contextual exceptions, **CONSIDER** an optional technique,
and **AVOID** a recurrent trap. See [sources and licensing](./00-sources-and-license.md).

## MC-01: Prefer a function when syntax transformation adds no value

**Strength**: SHOULD

**Summary**: Write the intended expansion first and keep the underlying capability callable without a macro.

```fennel
;; BAD: a macro adds no useful notation to simple arithmetic
(macro double-value [value]
  `(* 2 ,value))
(assert (= 8 (double-value 4)))
```

```fennel
;; GOOD: an ordinary function is reusable as a value
(fn double-value [value] (* 2 value))
(assert (= 8 (double-value 4)))
(assert (= :function (type double-value)))
```

**Rationale**: Macros are justified for evaluation control, bindings or a clear syntactic
abstraction, not merely to avoid function-call notation. A useful macro should
usually be convenient syntax over capabilities also available through functions.

**Sources**: [Style: Macros](https://git.sr.ht/~technomancy/fennel/tree/9af5e47fa7ddea806544d15507412ddc51bd046d/item/style.md#L557); [Macro Guide: Details](https://git.sr.ht/~technomancy/fennel/tree/9af5e47fa7ddea806544d15507412ddc51bd046d/item/macros.md#L75).

## MC-02: Evaluate caller expressions the intended number of times

**Strength**: MUST

**Summary**: Bind effectful arguments once unless repetition is explicitly the macro’s contract.

```fennel
;; BAD: the selected argument is evaluated a second time
(macro maximum [a b]
  `(if (< ,a ,b) ,b ,a))
(var calls 0)
(fn next! [] (set calls (+ calls 1)) calls)
(assert (= 2 (maximum (next!) 0)))
(assert (= 2 calls))
```

```fennel
;; GOOD: once-only evaluation is visible in the expansion
(macro maximum [a b]
  `(let [a# ,a
         b# ,b]
     (if (< a# b#) b# a#)))

(var calls 0)
(fn next! [] (set calls (+ calls 1)) calls)
(assert (= 1 (maximum (next!) 0)))
(assert (= 1 calls))
```

**Rationale**: Literal-only tests hide repeated evaluation. Test with changing return values
and an effect counter. Evaluate arguments in the intended order and preserve all
values required by the API; capturing in one binding intentionally selects one.

**Sources**: [Reference: Macro gotchas](https://git.sr.ht/~technomancy/fennel/tree/9af5e47fa7ddea806544d15507412ddc51bd046d/item/reference.md#L1664).

## MC-03: Use quoted templates and hygienic introduced locals

**Strength**: MUST

**Summary**: Suffix internal names with # in quotes; accept caller-visible binding names explicitly.

```fennel
;; BAD: compile error: a quoted macro may not introduce this unsafe binding
(macro twice [x] `(let [value ,x] (+ value value)))
(twice 3)
```

```fennel
;; GOOD: generated names cannot capture the caller’s value binding
(macro twice [x]
  `(let [value# ,x] (+ value# value#)))
(let [value 99]
  (assert (= 6 (twice 3)))
  (assert (= 99 value)))
```

**Rationale**: Prefer backtick and comma to manual `list`/`sym` construction; the compiler’s
accidental-binding safety check relies on quoted syntax. For intentionally exposed
locals, take a name as an argument, conventionally in a binding vector. Do not
bypass hygiene with `sym` just to silence a diagnostic.

**Sources**: [Macro Guide: Quoting](https://git.sr.ht/~technomancy/fennel/tree/9af5e47fa7ddea806544d15507412ddc51bd046d/item/macros.md#L179); [Macro Guide: Identifiers and Gensym](https://git.sr.ht/~technomancy/fennel/tree/9af5e47fa7ddea806544d15507412ddc51bd046d/item/macros.md#L250).

## MC-04: Keep compile-time and runtime environments distinct

**Strength**: MUST

**Summary**: Runtime locals are unavailable to the macro’s implementation; build emitted code from the input AST.

```fennel
;; BAD: compile error: runtime helper is unavailable in compiler scope
(fn helper [x] x)
(macro identity-form [x] (helper x))
(identity-form 3)
```

```fennel
;; GOOD: the macro returns syntax containing the caller’s expression
(macro identity-form [x]
  `(do
     ,x))
(let [runtime-value 3]
  (assert (= 3 (identity-form runtime-value))))
```

**Rationale**: A macro module defines ordinary functions and returns an export table, but
`import-macros` loads that module in compiler scope and binds those functions as
macros. Inline `macro` bindings cannot be returned as runtime values. Use
`import-macros` with explicit names rather than deprecated `require-macros`.

**Sources**: [Macro Guide: Macro Modules](https://git.sr.ht/~technomancy/fennel/tree/9af5e47fa7ddea806544d15507412ddc51bd046d/item/macros.md#L392); [Reference: import-macros](https://git.sr.ht/~technomancy/fennel/tree/9af5e47fa7ddea806544d15507412ddc51bd046d/item/reference.md#L1510).

## MC-05: Make expansion dependencies self-contained

**Strength**: SHOULD

**Summary**: Require a needed runtime module inside the emitted expression instead of assuming the caller imported it.

```fennel
;; BAD: compile error: caller is forced to provide an undeclared module alias
(macro absolute [x] `(numeric.abs ,x))
(absolute -4)
```

```fennel
;; GOOD: this expansion resolves its own runtime dependency
(macro absolute [x]
  `(let [math# (require :math)]
     (math#.abs ,x)))

(assert (= 4 (absolute -4)))
```

**Rationale**: `require` caches modules, so subsequent uses normally look up the existing value.
The macro’s own compile-time imports do not automatically create runtime imports
in generated Lua. Use a hygienic local for the emitted module reference.

**Sources**: [Macro Guide: Using functions from a module](https://git.sr.ht/~technomancy/fennel/tree/9af5e47fa7ddea806544d15507412ddc51bd046d/item/macros.md#L366).

## MC-06: Validate syntax and inspect real expansions

**Strength**: SHOULD

**Summary**: Use assert-compile with the input AST and use macrodebug before trusting a new macro.

```fennel
;; BAD: compile error: invalid macro input fails as an incidental table operation
(macro first-form [forms] (. forms 1))
(first-form 42)
```

```fennel
;; GOOD: domain-specific input checks pinpoint the bad form
(macro first-form [forms]
  (assert-compile (sequence? forms) "expected a sequential form" forms)
  (. forms 1))

(assert (= 8 (first-form [8 9])))
```

**Rationale**: Call `(macrodebug (your-macro ...))` in a development file/REPL to see expansion;
it prints during compilation and does not execute the expansion. Preserve source
metadata when constructing AST nodes. A nil literal in an AST is a symbol, not an
absent Lua table slot. Unquoting multiple forms in a non-final list position keeps
only the first; use a final splice inside a nested `do` when all forms are needed.

**Sources**: [Macro Guide: macrodebug](https://git.sr.ht/~technomancy/fennel/tree/9af5e47fa7ddea806544d15507412ddc51bd046d/item/macros.md#L231); [Macro Guide: AST quirks](https://git.sr.ht/~technomancy/fennel/tree/9af5e47fa7ddea806544d15507412ddc51bd046d/item/macros.md#L340); [Macro Guide: assert-compile](https://git.sr.ht/~technomancy/fennel/tree/9af5e47fa7ddea806544d15507412ddc51bd046d/item/macros.md#L431).

## Summary Table

| Pattern | Strength | Rule |
|---|---|---|
| MC-01 | SHOULD | Prefer a function when syntax transformation adds no value |
| MC-02 | MUST | Evaluate caller expressions the intended number of times |
| MC-03 | MUST | Use quoted templates and hygienic introduced locals |
| MC-04 | MUST | Keep compile-time and runtime environments distinct |
| MC-05 | SHOULD | Make expansion dependencies self-contained |
| MC-06 | SHOULD | Validate syntax and inspect real expansions |

## Related Guidelines

- [Values and Core Idioms](./01-values-and-core-idioms.md)
- [Setup, Tooling and Testing](./09-setup-tooling-and-testing.md)
- [Lua Interop and Distribution](./10-lua-interop-and-distribution.md)
