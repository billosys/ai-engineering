# Modules and API Design

A module is the value returned by a loaded chunk, conventionally a table. Keep
its exports, dependencies, state and failure conventions explicit.

Strengths describe this skill’s guidance: **MUST** marks a semantic requirement,
**SHOULD** a default with contextual exceptions, **CONSIDER** an optional technique,
and **AVOID** a recurrent trap. See [sources and licensing](./00-sources-and-license.md).

## MD-01: Return a small export table

**Strength**: SHOULD

**Summary**: Keep implementation bindings local and gather public exports at the bottom.

```fennel
;; BAD: returning a bare function makes extension awkward
(fn make-module [] (fn [x] (+ x 1)))
(assert (= 4 ((make-module) 3)))
```

```fennel
;; GOOD: a named export table can grow without changing its shape
(fn make-module []
  (fn increment [x] (+ x 1))

  {: increment})

(let [api (make-module)]
  (assert (= 4 (api.increment 3))))
```

**Rationale**: For a real module, put the final table at file scope rather than inside this
demonstration factory. Group requires at the top, use `local` for file-level
bindings and `let` for small inner scopes. Export only stable public operations;
an `internal`/`private` module name should be a deliberate boundary.

**Sources**: [Style: Modules](https://git.sr.ht/~technomancy/fennel/tree/9af5e47fa7ddea806544d15507412ddc51bd046d/item/style.md#L470).

## MD-02: Keep import-time behavior quiet

**Strength**: SHOULD

**Summary**: Expose explicit initialization and effects instead of doing work merely because a module was required.

```fennel
;; BAD: loading this factory immediately performs initialization
(var starts 0)
(fn load-module []
  (set starts (+ starts 1))
  {})

(load-module)
(assert (= 1 starts))
```

```fennel
;; GOOD: initialization has an explicit owner
(var starts 0)
(fn load-module []
  (fn start! [] (set starts (+ starts 1)))

  {: start!})

(let [api (load-module)]
  (assert (= 0 starts))
  (api.start!)
  (assert (= 1 starts)))
```

**Rationale**: Lua caches required modules. Hidden initialization makes import order, tests and
reloads harder to reason about. Document state ownership and shutdown for resources
that an explicit initializer creates; a module cache is not a lifecycle manager.

**Sources**: [Style: module effects](https://git.sr.ht/~technomancy/fennel/tree/9af5e47fa7ddea806544d15507412ddc51bd046d/item/style.md#L507); [API: require caching](https://git.sr.ht/~technomancy/fennel/tree/9af5e47fa7ddea806544d15507412ddc51bd046d/item/api.md#L148).

## MD-03: Use relative requires for relocatable libraries

**Strength**: SHOULD

**Summary**: Resolve child modules from the module name supplied by require, not the shell’s working directory.

```fennel
;; BAD: hard-coded root name cannot follow relocation
(fn child-name [_module-name]
  :example.worker)
(assert (not= :libs.example.worker (child-name :libs.example)))
```

```fennel
;; GOOD: mirror an init.fnl chunk’s module argument
(fn child-name [...] (.. ... :.worker))
(assert (= :libs.example.worker (child-name :libs.example)))
```

**Rationale**: In an actual `init.fnl`, `(require (.. ... :.worker))` resolves a child relative
to the module name. A non-init module must strip its last name segment first.
This is Lua’s module-loader vararg behavior, not a generic filesystem-relative
require. A file run directly as a script has different arguments. Keep compile-time
relative paths self-contained when using `--require-as-include`.

**Sources**: [Tutorial: Relative require](https://git.sr.ht/~technomancy/fennel/tree/9af5e47fa7ddea806544d15507412ddc51bd046d/item/tutorial.md#L632).

## MD-04: Account for references retained across reloads

**Strength**: CONSIDER

**Summary**: Keep a module reference when you need field replacement to be observed; copied function bindings remain old references.

```fennel
;; BAD: destructured function is a snapshot of the field
(let [api {:value (fn [] 1)}
      {: value} api]
  (set api.value (fn [] 2))
  (assert (= 1 (value))))
```

```fennel
;; GOOD: field lookup observes replacement in this same table
(let [api {:value (fn [] 1)}]
  (set api.value (fn [] 2))
  (assert (= 2 (api.value))))
```

**Rationale**: This demonstrates field replacement, not a universal reload algorithm. A reload
that replaces the whole module table also leaves older table references stale;
update dependents or use a designed indirection strategy. Avoid mutating module
exports during normal operation merely because tables allow it.

**Sources**: [Style: reloading and destructured requires](https://git.sr.ht/~technomancy/fennel/tree/9af5e47fa7ddea806544d15507412ddc51bd046d/item/style.md#L510); [API: require and reload](https://git.sr.ht/~technomancy/fennel/tree/9af5e47fa7ddea806544d15507412ddc51bd046d/item/api.md#L148).

## MD-05: Make the Lua-facing surface comfortable

**Strength**: SHOULD

**Summary**: Keep idiomatic internal names and map export keys when Lua identifiers require it.

```fennel
;; BAD: hyphenated export requires bracket access in Lua
(fn make-api []
  (fn parse-value [x] (tonumber x))

  {: parse-value})

(assert (= 12 ((. (make-api) :parse-value) :12)))
```

```fennel
;; GOOD: underscore alias supports Lua api.parse_value calls
(fn make-api []
  (fn parse-value [x] (tonumber x))

  {:parse_value parse-value})

(assert (= 12 ((. (make-api) :parse_value) :12)))
```

**Rationale**: Fennel function values work directly in Lua. Document receiver conventions,
mutated tables, nil/error returns and argument types as part of the public API.
Do not pretend the exported alias requires camelCase or underscores in all internal
Fennel bindings.

**Sources**: [Style: Names for Lua consumers](https://git.sr.ht/~technomancy/fennel/tree/9af5e47fa7ddea806544d15507412ddc51bd046d/item/style.md#L249); [From Clojure: Runtime](https://git.sr.ht/~technomancy/fennel/tree/9af5e47fa7ddea806544d15507412ddc51bd046d/item/from-clojure.md#L16).

## Summary Table

| Pattern | Strength | Rule |
|---|---|---|
| MD-01 | SHOULD | Return a small export table |
| MD-02 | SHOULD | Keep import-time behavior quiet |
| MD-03 | SHOULD | Use relative requires for relocatable libraries |
| MD-04 | CONSIDER | Account for references retained across reloads |
| MD-05 | SHOULD | Make the Lua-facing surface comfortable |

## Related Guidelines

- [Errors and Resources](./07-errors-and-resources.md)
- [Lua Interop and Distribution](./10-lua-interop-and-distribution.md)
