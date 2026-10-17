# Setup, Tooling and Testing

Record the Fennel compiler version, formatter version and actual target Lua VM.
Formatting, compilation and runtime checks establish different properties; use
all that the project’s behavior requires.

Strengths describe this skill’s guidance: **MUST** marks a semantic requirement,
**SHOULD** a default with contextual exceptions, **CONSIDER** an optional technique,
and **AVOID** a recurrent trap. See [sources and licensing](./00-sources-and-license.md).

## TL-01: Pin the toolchain that produces deployable Lua

**Strength**: SHOULD

**Summary**: Keep compiler/runtime choices reproducible and test the actual host’s library surface.

```fennel
;; BAD: an assumed runtime helper need not exist on every Lua host
(assert (= :function (type table.unpack)))
```

```fennel
;; GOOD: choose the documented compatibility fallback when supporting older Lua
(let [unpack-values (or table.unpack _G.unpack)]
  (assert (= :function (type unpack-values)))
  (assert (= 3 (select "#" (unpack-values [1 2 3])))))
```

**Rationale**: Fennel release and Lua runtime versions are separate compatibility axes.
The setup guide recommends keeping the chosen compiler script with a project for
consistent builds. Do not silently upgrade a project’s compiler or assume the
workstation’s newer Lua proves compatibility with an embedded LuaJIT host.

**Sources**: [Setup: ahead-of-time compilation](https://git.sr.ht/~technomancy/fennel/tree/9af5e47fa7ddea806544d15507412ddc51bd046d/item/setup.md#L106); [Lua Primer: unpack differences](https://git.sr.ht/~technomancy/fennel/tree/9af5e47fa7ddea806544d15507412ddc51bd046d/item/lua-primer.md#L137).

## TL-02: Keep strict global checking in compilation checks

**Strength**: SHOULD

**Summary**: A successful bare AOT compile does not establish that global names are valid.

```fennel
;; BAD: compile-only counterexample: bare --compile can emit this unknown global
(misspelled-processor 1)
```

```fennel
;; GOOD: a lexical dependency is visible to strict checking
(fn process [value] (+ value 1))
(assert (= 2 (process 1)))
```

**Rationale**: The CLI help explicitly says AOT compilation defaults to no global checks.
Use `--globals` to add host-specific names while retaining standard globals, or
`--globals-only` with the complete intended set. The API compile functions also
need an `allowedGlobals` list to enable checking. Never call successful emission
of Lua a type check or a runtime behavior test.

**Sources**: [API: compile global checks](https://git.sr.ht/~technomancy/fennel/tree/9af5e47fa7ddea806544d15507412ddc51bd046d/item/api.md#L234); [Tutorial: Strict global checking](https://git.sr.ht/~technomancy/fennel/tree/9af5e47fa7ddea806544d15507412ddc51bd046d/item/tutorial.md#L529).

## TL-03: Test behavior at boundaries rather than only happy values

**Strength**: SHOULD

**Summary**: Include false, nil, extra returns, shadowed bindings and effects when those can change the contract.

```fennel
;; BAD: a literal-only macro test cannot detect repeated evaluation
(macro twice [x]
  `(+ ,x ,x))
(assert (= 6 (twice 3)))
```

```fennel
;; GOOD: an effectful input distinguishes a once-only expansion
(macro twice [x]
  `(let [x# ,x] (+ x# x#)))
(var calls 0)
(fn next! [] (set calls (+ calls 1)) calls)
(assert (= 2 (twice (next!))))
(assert (= 1 calls))
```

**Rationale**: Plain `assert` is sufficient for small executable examples. In a real project,
use its established test harness rather than inventing a testing framework here.
Keep compile-negative tests and runtime-error tests distinct. For emitted artifacts,
run Lua itself as well as the `fennel` launcher so loader dependencies cannot hide.

**Sources**: [Reference: repeated evaluation gotcha](https://git.sr.ht/~technomancy/fennel/tree/9af5e47fa7ddea806544d15507412ddc51bd046d/item/reference.md#L1664); [Setup: AOT compilation](https://git.sr.ht/~technomancy/fennel/tree/9af5e47fa7ddea806544d15507412ddc51bd046d/item/setup.md#L106).

## TL-04: Format without confusing formatting with correctness

**Strength**: SHOULD

**Summary**: Use fnlfmt on project-owned source and retain separate semantic checks.

```fennel
;; BAD: formatting cannot repair an incorrect default
(let [enabled? false]
  (assert (= true (or enabled? true))))
```

```fennel
;; GOOD: correct semantics remain a separate responsibility
(let [enabled? false]
  (assert (= false (if (= nil enabled?) true enabled?))))
```

**Rationale**: fnlfmt has `--check` and `--fix` modes; check should leave files untouched and
fix rewrites them. It does not establish correct macro expansion, nil handling or
resource lifetimes. Do not reformat retained upstream documents: their exact bytes
and attribution are part of the provenance contract.

**Sources**: [Style: defer formatting to fnlfmt](https://git.sr.ht/~technomancy/fennel/tree/9af5e47fa7ddea806544d15507412ddc51bd046d/item/style.md#L17); [fnlfmt usage](https://git.sr.ht/~technomancy/fnlfmt).

## Summary Table

| Pattern | Strength | Rule |
|---|---|---|
| TL-01 | SHOULD | Pin the toolchain that produces deployable Lua |
| TL-02 | SHOULD | Keep strict global checking in compilation checks |
| TL-03 | SHOULD | Test behavior at boundaries rather than only happy values |
| TL-04 | SHOULD | Format without confusing formatting with correctness |

## Related Guidelines

- [Macros](./08-macros.md)
- [Lua Interop and Distribution](./10-lua-interop-and-distribution.md)
- [Anti-Patterns](./11-anti-patterns.md)

## Concrete command sequence

Substitute the project’s source/test filenames and approved tool versions:

```sh
fennel --version
lua -v
fnlfmt --version
fnlfmt --check src/main.fnl
fennel test/main.fnl
# An empty addition still enables standard-global checking in the CLI:
fennel --globals '' --compile src/main.fnl > build/main.lua
lua build/main.lua
```

Create `build/` first. A module needs its consumer test rather than merely being
executed as a chunk. Run these through the project’s Make/task targets where they
exist. Check `fennel --help` for that compiler’s flags, and make host-global additions
explicit. The empty `--globals` example was exercised on Fennel 1.6.1.

On the authoring workstation, fnlfmt 0.3.2, Fennel 1.6.1 and PUC Lua 5.5 were
available. Other hosts need their own checks. If fnlfmt is missing, consult its
upstream README and the local package manager rather than assuming a formula name;
its documented source install is `make install PREFIX=...` in a checkout.
