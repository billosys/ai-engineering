# Sources, Scope and License

This skill derives practical authoring and review guidance from the official
Fennel documentation at language commit `9af5e47fa7ddea806544d15507412ddc51bd046d`
(release 1.6.1), linked by the website repository at
`253e9463c2d6a306feecb37237beee303f9714c1`. References below and in each rule
are pinned, not links to a moving branch. This is a snapshot, not a claim that
later compiler versions have been reviewed.

## How to read the rules

Semantic **MUST** statements describe requirements of the documented construct.
**SHOULD** means a default that can have explained contextual exceptions.
**CONSIDER** names a technique whose value depends on the task. **AVOID** marks
an error-prone habit. The upstream style guide explicitly asks for judgment;
its preferences are not newly invented compiler errors. Additional build/test
recommendations are identified as recommendations, not upstream guarantees.

Good/bad pairs are self-contained Fennel examples unless an accompanying section
explicitly describes a module or host fragment. BAD examples sometimes deliberately
fail compilation; others assert the observed undesirable behavior to demonstrate
the trap. GOOD examples assert the intended behavior. Formatting and successful
execution do not by themselves establish correctness of all surrounding prose.

## Source catalog

- [Style Guide](https://git.sr.ht/~technomancy/fennel/tree/9af5e47fa7ddea806544d15507412ddc51bd046d/item/style.md#L1)
- [Values of Fennel](https://git.sr.ht/~technomancy/fennel/tree/9af5e47fa7ddea806544d15507412ddc51bd046d/item/values.md#L1)
- [Setting up Fennel](https://git.sr.ht/~technomancy/fennel/tree/9af5e47fa7ddea806544d15507412ddc51bd046d/item/setup.md#L1)
- [Tutorial](https://git.sr.ht/~technomancy/fennel/tree/9af5e47fa7ddea806544d15507412ddc51bd046d/item/tutorial.md#L1)
- [Language Reference](https://git.sr.ht/~technomancy/fennel/tree/9af5e47fa7ddea806544d15507412ddc51bd046d/item/reference.md#L1)
- [Macro Guide](https://git.sr.ht/~technomancy/fennel/tree/9af5e47fa7ddea806544d15507412ddc51bd046d/item/macros.md#L1)
- [Lua API](https://git.sr.ht/~technomancy/fennel/tree/9af5e47fa7ddea806544d15507412ddc51bd046d/item/api.md#L1)
- [Lua Primer](https://git.sr.ht/~technomancy/fennel/tree/9af5e47fa7ddea806544d15507412ddc51bd046d/item/lua-primer.md#L1)
- [Rationale](https://git.sr.ht/~technomancy/fennel/tree/9af5e47fa7ddea806544d15507412ddc51bd046d/item/rationale.md#L1)
- [Learning Fennel from Clojure](https://git.sr.ht/~technomancy/fennel/tree/9af5e47fa7ddea806544d15507412ddc51bd046d/item/from-clojure.md#L1)
- [Security](https://git.sr.ht/~technomancy/fennel/tree/9af5e47fa7ddea806544d15507412ddc51bd046d/item/security.md#L1)
- [Changelog](https://git.sr.ht/~technomancy/fennel/tree/9af5e47fa7ddea806544d15507412ddc51bd046d/item/changelog.md#L1)
- [Language overview and source build](https://git.sr.ht/~technomancy/fennel/tree/9af5e47fa7ddea806544d15507412ddc51bd046d/item/README.md#L1)

The source repository retains those documents byte-for-byte under
`knowledge/fennel/sources/md/`. Its source provenance README, commit map and
verification manifest explain the non-squashed, history-preserving import.
Original sources are deliberately excluded from the installable zip: guide links
use pinned official URLs, so the installed guidance does not need a repository
checkout or an additional local path exception.

## Attribution and license

The adapted prose in this Fennel skill and its guides is distributed under
[Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported](https://creativecommons.org/licenses/by-nc-sa/3.0/).
It incorporates guidance from the Fennel Style Guide, copyright Taylor R. Campbell
2007–2011 and Phil Hagelberg and contributors 2021–2023, itself based on
[Taylor R. Campbell’s Lisp Style Guide](http://mumble.net/~campbell/scheme/style.txt).
This adaptation reorganizes, condenses and adds original examples and checks for
coding-assistant use; it is not endorsed by the upstream authors.

Other imported Fennel documentation is covered by the upstream MIT notice,
copyright 2016–2025 Calvin Rose and contributors, as stated in the
[pinned README license section](https://git.sr.ht/~technomancy/fennel/tree/9af5e47fa7ddea806544d15507412ddc51bd046d/item/README.md#L117),
subject to individual-file notices.
Those originals retain their licenses. The ai-engineering repository’s root MIT
license does not override this skill’s documentation license or style attribution.

## Guide map

| Guide | Patterns | Topic |
|---|---|---|
| [Values and Core Idioms](./01-values-and-core-idioms.md) | 5 | Lexical scope, effects, truth and runtime values |
| [Style and Naming](./02-style-and-naming.md) | 5 | Formatting, names, comments and docstrings |
| [Tables and Data](./03-tables-and-data.md) | 6 | Dense sequences, maps, iteration and identity |
| [Functions and Control Flow](./04-functions-and-control-flow.md) | 5 | Arguments, multiple returns, varargs and loops |
| [Pattern Matching](./05-pattern-matching.md) | 4 | Fresh bindings, pinning, guards and shapes |
| [Modules and API Design](./06-modules-and-api-design.md) | 5 | Exports, loading, relocation and reloading |
| [Errors and Resources](./07-errors-and-resources.md) | 5 | Failure values, raised errors and resource cleanup |
| [Macros](./08-macros.md) | 6 | Hygiene, phases, evaluation count and ASTs |
| [Setup, Tooling and Testing](./09-setup-tooling-and-testing.md) | 4 | Toolchain choices, format checks and behavior tests |
| [Lua Interop and Distribution](./10-lua-interop-and-distribution.md) | 5 | Host calls, VM features, loaders and emitted Lua |
| [Anti-Patterns and Review Checks](./11-anti-patterns.md) | 6 | Compact checks for recurring Fennel mistakes |
