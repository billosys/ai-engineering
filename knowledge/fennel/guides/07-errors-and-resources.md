# Errors and Resources

Lua-style expected failures and raised errors are distinct protocols. Decide which
one each boundary uses, preserve the details, and close resources deterministically.

Strengths describe this skill’s guidance: **MUST** marks a semantic requirement,
**SHOULD** a default with contextual exceptions, **CONSIDER** an optional technique,
and **AVOID** a recurrent trap. See [sources and licensing](./00-sources-and-license.md).

## ER-01: Handle expected failures as multiple values

**Strength**: SHOULD

**Summary**: Return nil plus an error value for routine failure; use case to keep success and failure adjacent.

```fennel
;; BAD: taking only the first result discards the explanation
(fn fetch [] (values nil "not available"))
(let [value (fetch)] (assert (= nil value)))
```

```fennel
;; GOOD: preserve both values and handle both branches
(fn fetch [] (values nil "not available"))
(let [message (case (fetch)
                (nil reason) reason
                value (tostring value))]
  (assert (= "not available" message)))
```

**Rationale**: Document whether success may be false or nil. A plain binding pattern accepts
false, and a success-as-nil API needs a different discriminator. Do not silently
convert expected failure into a successful-looking empty table or a vague message.

**Sources**: [Style: Error handling](https://git.sr.ht/~technomancy/fennel/tree/9af5e47fa7ddea806544d15507412ddc51bd046d/item/style.md#L539); [Tutorial: Error handling](https://git.sr.ht/~technomancy/fennel/tree/9af5e47fa7ddea806544d15507412ddc51bd046d/item/tutorial.md#L415).

## ER-02: Do not confuse pcall success with operation success

**Strength**: MUST

**Summary**: pcall adds a boolean for whether an error was raised; it does not reinterpret nil/error returns.

```fennel
;; BAD: pcall succeeds even when the operation returns failure values
(fn missing [] (values nil :missing))
(let [[ok? value reason] [(pcall missing)]]
  (assert ok?)
  (assert (= nil value))
  (assert (= :missing reason)))
```

```fennel
;; GOOD: convert value failure explicitly when the boundary requires a raised error
(fn missing [] (values nil :missing))
(let [[ok? reason] [(pcall (fn [] (assert (missing))))]]
  (assert (= false ok?))
  (assert (string.find reason :missing 1 true)))
```

**Rationale**: `assert` rejects nil and false and raises an error; use it where aborting that
operation is the intended policy. `pcall` returns true followed by normal results,
or false followed by the raised error object. `case-try` sequences value failures;
its `catch` does not catch a raised error without an explicit protected call.

**Sources**: [Tutorial: protected calls](https://git.sr.ht/~technomancy/fennel/tree/9af5e47fa7ddea806544d15507412ddc51bd046d/item/tutorial.md#L442); [Reference: case-try](https://git.sr.ht/~technomancy/fennel/tree/9af5e47fa7ddea806544d15507412ddc51bd046d/item/reference.md#L734).

## ER-03: Sequence fallible values without losing the first failure

**Strength**: CONSIDER

**Summary**: Use case-try for staged nil/error operations and make its catch policy explicit.

```fennel
;; BAD: a second step erases the earlier failure
(fn lookup [] (values nil "lookup failed"))
(let [value (lookup)]
  (assert (= :default (or value :default))))
```

```fennel
;; GOOD: the failed stage short-circuits later work
(fn lookup [] (values nil "lookup failed"))
(var called? false)
(let [result (case-try (lookup)
               value (do
                       (set called? true) value)
               (catch (nil reason) reason))]
  (assert (= "lookup failed" result))
  (assert (= false called?)))
```

**Rationale**: Patterns decide whether each step advances. With a catch, unmatched values are
matched against its clauses; no matching catch yields nil. Without catch, mismatched
values are returned. Test early failure, later failure and successful completion
rather than assuming a name ending in `try` catches exceptions.

**Sources**: [Reference: case-try](https://git.sr.ht/~technomancy/fennel/tree/9af5e47fa7ddea806544d15507412ddc51bd046d/item/reference.md#L734).

## ER-04: Use deterministic resource cleanup

**Strength**: SHOULD

**Summary**: Handle open failure first, then use with-open with the cleanup protocol of the selected mode.

```fennel
;; BAD: forgetting cleanup leaks the resource until another mechanism acts
(let [closed? {:value false}
      handle {:close (fn [_self] (set closed?.value true))}]
  (assert (= false closed?.value)))
```

```fennel
;; GOOD: with-open closes even if the body raises
(let [state {:closed? false}
      handle {:close (fn [_self] (set state.closed? true))}
      [ok?] [(pcall (fn []
                      (with-open [resource handle]
                        (error "read failed"))))]]
  (assert (= false ok?))
  (assert state.closed?))
```

**Rationale**: A file open can fail: `(case (io.open path) (nil reason) ... file ...)` keeps that
failure explicit before the `with-open`. If open failure should abort, use
`(with-open [file (assert (io.open path))] ...)`. Normally cleanup uses a protected
call and invokes the handle’s `:close` method. `--to-be-closed` instead selects
Lua 5.4+ native closing: a non-nil/non-false resource must support Lua’s `__close`
metamethod, as actual file handles do. A plain table with only `:close` does not
satisfy that native protocol. The fake handle above tests the default protected
cleanup path, not the native mode. Test custom resources in the mode you ship.

**Sources**: [Upstream native-closing test](https://git.sr.ht/~technomancy/fennel/tree/9af5e47fa7ddea806544d15507412ddc51bd046d/item/test/core.fnl#L378); [Reference: with-open](https://git.sr.ht/~technomancy/fennel/tree/9af5e47fa7ddea806544d15507412ddc51bd046d/item/reference.md#L848); [Lua Primer: io module](https://git.sr.ht/~technomancy/fennel/tree/9af5e47fa7ddea806544d15507412ddc51bd046d/item/lua-primer.md#L102).

## ER-05: Make diagnostics inspect data without changing the contract

**Strength**: SHOULD

**Summary**: Use fennel.view for development inspection and preserve useful error context.

```fennel
;; BAD: tostring does not describe ordinary table contents
(let [text (tostring {:count 3})]
  (assert (not= "{:count 3}" text)))
```

```fennel
;; GOOD: view shows the data during development
(let [fennel (require :fennel)
      text (fennel.view {:count 3})]
  (assert (string.find text :count 1 true))
  (assert (string.find text :3 1 true)))
```

**Rationale**: Using `fennel.view` at runtime is an explicit dependency on a function in the
compiler library. If you ship only ahead-of-time Lua, either include that library
or keep this development-only. It prints placeholders for functions/userdata and
is not a general persistence format for arbitrary application objects.

**Sources**: [API: view serialization](https://git.sr.ht/~technomancy/fennel/tree/9af5e47fa7ddea806544d15507412ddc51bd046d/item/api.md#L403); [Tutorial: Gotchas](https://git.sr.ht/~technomancy/fennel/tree/9af5e47fa7ddea806544d15507412ddc51bd046d/item/tutorial.md#L552).

## Summary Table

| Pattern | Strength | Rule |
|---|---|---|
| ER-01 | SHOULD | Handle expected failures as multiple values |
| ER-02 | MUST | Do not confuse pcall success with operation success |
| ER-03 | CONSIDER | Sequence fallible values without losing the first failure |
| ER-04 | SHOULD | Use deterministic resource cleanup |
| ER-05 | SHOULD | Make diagnostics inspect data without changing the contract |

## Related Guidelines

- [Functions and Control Flow](./04-functions-and-control-flow.md)
- [Pattern Matching](./05-pattern-matching.md)
- [Lua Interop and Distribution](./10-lua-interop-and-distribution.md)
