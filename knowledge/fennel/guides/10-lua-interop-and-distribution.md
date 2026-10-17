# Lua Interop and Distribution

Pick either runtime compilation with an installed Fennel searcher or ahead-of-time
Lua delivery. Both use the host VM’s semantics, libraries and resource constraints.

Strengths describe this skill’s guidance: **MUST** marks a semantic requirement,
**SHOULD** a default with contextual exceptions, **CONSIDER** an optional technique,
and **AVOID** a recurrent trap. See [sources and licensing](./00-sources-and-license.md).

## LI-01: Distinguish functions from methods at Lua boundaries

**Strength**: MUST

**Summary**: A colon call passes the receiver first; a dot call does not.

```fennel
;; BAD: compile/run error avoided here by observing the missing receiver
(let [object {:value 7 :read (fn [self] (if self self.value :missing))}]
  (assert (= :missing (object.read))))
```

```fennel
;; GOOD: method notation supplies self
(let [object {:value 7 :read (fn [self] self.value)}]
  (assert (= 7 (object:read)))
  (assert (= 7 (object.read object))))
```

**Rationale**: Use `(object:method arg)` for a static method name, or `(: object method arg)`
when the receiver/name is computed. Functions created in Fennel need an explicit
receiver parameter when used as methods; defining a function with a dotted name
does not insert that parameter.

**Sources**: [Reference: method calls](https://git.sr.ht/~technomancy/fennel/tree/9af5e47fa7ddea806544d15507412ddc51bd046d/item/reference.md#L1286).

## LI-02: Do not infer Unicode or regex semantics from strings

**Strength**: MUST

**Summary**: Lua strings are bytes; Lua string patterns are not regular expressions.

```fennel
;; BAD: byte length is not Unicode codepoint count
(assert (= 2 (length "é")))
```

```fennel
;; GOOD: choose codepoint-aware operations when the runtime provides utf8
(assert (= 1 (utf8.len "é")))
(assert (= :42 (string.match :value=42 "value=(%d+)")))
```

**Rationale**: The good example needs Lua 5.3+ `utf8` or a compatible supplied module. Codepoint
counts still are not grapheme counts. `string.gmatch` and `string.match` use Lua’s
pattern syntax (`%d`, not an assumed regex engine). Binary data is valid string
content and may need a different validation contract.

**Sources**: [Tutorial: Numbers and strings](https://git.sr.ht/~technomancy/fennel/tree/9af5e47fa7ddea806544d15507412ddc51bd046d/item/tutorial.md#L135); [Lua Primer: missing regex/split](https://git.sr.ht/~technomancy/fennel/tree/9af5e47fa7ddea806544d15507412ddc51bd046d/item/lua-primer.md#L192).

## LI-03: Respect target VM feature boundaries

**Strength**: MUST

**Summary**: Gate integer division, bitwise operations and native closing against the chosen runtime.

```fennel
;; BAD: a host-specific operation cannot prove older-host compatibility
(assert (= 2 (// 5 2)))
```

```fennel
;; GOOD: use a portable operation only when its semantics match the domain
(assert (= 2 (math.floor (/ 5 2))))
```

**Rationale**: `//` needs Lua 5.3+. Bitwise operators also target 5.3+ syntax unless configured
for LuaJIT’s bit library. `--to-be-closed` needs 5.4+ and resources with the native `__close` protocol;
a custom `:close` method alone is insufficient (see
[resource cleanup](./07-errors-and-resources.md)). Floor division through floating
arithmetic is suitable only within a range where precision matches the application;
it is not a universal replacement for integer division. Test on each promised VM.

**Sources**: [Reference: operators](https://git.sr.ht/~technomancy/fennel/tree/9af5e47fa7ddea806544d15507412ddc51bd046d/item/reference.md#L1053); [Reference: native with-open closing](https://git.sr.ht/~technomancy/fennel/tree/9af5e47fa7ddea806544d15507412ddc51bd046d/item/reference.md#L848).

## LI-04: Keep runtime compiler dependencies explicit

**Strength**: MUST

**Summary**: Pure emitted Lua has no automatic Fennel loader or compiler library; development helpers are still dependencies.

```fennel
;; BAD: view introduces a runtime compiler-library dependency
(let [fennel (require :fennel)]
  (assert (= :string (type (fennel.view {:value 7})))))
```

```fennel
;; GOOD: ordinary application logic can ship as Lua without fennel
(fn describe [value] (.. :value= (tostring value)))
(assert (= :value=7 (describe 7)))
```

**Rationale**: For runtime compilation, load `fennel.lua` (the library, not the executable) and
call `require("fennel").install()` before requiring `.fnl` modules. For AOT delivery,
compile all runtime modules or bundle resolvable requires with `--require-as-include`.
Dynamic requires still need files/loaders at runtime. Test the distribution in a
clean directory so source files cannot accidentally satisfy missing dependencies.

**Sources**: [Setup: Embedding Fennel](https://git.sr.ht/~technomancy/fennel/tree/9af5e47fa7ddea806544d15507412ddc51bd046d/item/setup.md#L69); [API: searcher installation](https://git.sr.ht/~technomancy/fennel/tree/9af5e47fa7ddea806544d15507412ddc51bd046d/item/api.md#L148); [Reference: include](https://git.sr.ht/~technomancy/fennel/tree/9af5e47fa7ddea806544d15507412ddc51bd046d/item/reference.md#L1427).

## LI-05: Do not use the compiler sandbox as a security boundary

**Strength**: MUST

**Summary**: Compilation runs macros; do not compile untrusted code in a trusted process merely because default compiler restrictions exist.

```fennel
;; BAD: evaluation executes code; it is not parsing
(let [fennel (require :fennel)]
  (assert (= 3 (fennel.eval "(+ 1 2)"))))
```

```fennel
;; GOOD: keep the host’s authority explicit in the API boundary
(let [fennel (require :fennel)
      env {:supplied (fn [x] (+ x 1))}]
  (assert (= 3 (fennel.eval "(supplied 2)" {: env}))))
```

**Rationale**: The restricted environment example controls the supplied runtime names; it is
not a safe evaluator for adversarial input. `compilerEnv` and runtime `env` are
different options. The reference explicitly disclaims a robust security boundary
for its compiler sandbox. Preserve restrictions unless a trusted, justified build
needs more authority; disabling the sandbox globally is not a routine fix.

**Sources**: [Reference: Sandboxing](https://git.sr.ht/~technomancy/fennel/tree/9af5e47fa7ddea806544d15507412ddc51bd046d/item/reference.md#L1780); [API: env and compilerEnv](https://git.sr.ht/~technomancy/fennel/tree/9af5e47fa7ddea806544d15507412ddc51bd046d/item/api.md#L11); [Security: Historical Issues](https://git.sr.ht/~technomancy/fennel/tree/9af5e47fa7ddea806544d15507412ddc51bd046d/item/security.md#L29).

## Summary Table

| Pattern | Strength | Rule |
|---|---|---|
| LI-01 | MUST | Distinguish functions from methods at Lua boundaries |
| LI-02 | MUST | Do not infer Unicode or regex semantics from strings |
| LI-03 | MUST | Respect target VM feature boundaries |
| LI-04 | MUST | Keep runtime compiler dependencies explicit |
| LI-05 | MUST | Do not use the compiler sandbox as a security boundary |

## Related Guidelines

- [Functions and Control Flow](./04-functions-and-control-flow.md)
- [Modules and API Design](./06-modules-and-api-design.md)
- [Macros](./08-macros.md)

## Embedding and AOT shapes

Minimal Lua host for trusted application code, with `fennel.lua` and `main.fnl`
available on the configured paths:

```lua
local fennel = require("fennel")
fennel.install()
fennel.dofile("main.fnl")
```

For compilation through the API, enable global checks explicitly:

```lua
local fennel = require("fennel")
local code = fennel.compileString("(print (+ 1 2))", {
  filename = "example.fnl",
  allowedGlobals = {"print"}
})
assert(type(code) == "string")
```

`fennel.eval` and `fennel.dofile` execute; `compileString` returns Lua text. Adding a
searcher affects the Lua state’s loader list, while `dofile` bypasses the require
cache. Configure `fennel.path` for `.fnl`, `package.path` for `.lua`, and
`fennel.macro-path` for macro modules; they serve separate phases.

An AOT build can compile into a temporary output and rename it only after success,
so a failed build does not leave a truncated deployable file. Include macro files
as build dependencies even though they do not ship as runtime modules. These build
practices are this skill’s recommendations derived from the compile-time model.
