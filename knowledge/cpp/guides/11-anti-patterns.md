# Anti-Patterns

The cheap safety net for C++ work. Load this first on any C++ task, then load the home guide for each relevant rule.

This file is an index of negative C++ Core Guidelines rules: `Avoid`, `Don't`, `Do not`, `Never`, `must not`, and close variants.
It intentionally points back to the topic guides so the detailed upstream rationale, examples, and enforcement text stay in one place.

## Anti-Pattern Index

| Rule | Avoid | Home Guide | Source Anchor |
|------|-------|------------|---------------|
| `In.0` | Don't panic! | `01-core-idioms.md` | `r0` |
| `P.8` | Don't leak any resources | `01-core-idioms.md` | `rp-leak` |
| `P.9` | Don't waste time or space | `01-core-idioms.md` | `rp-waste` |
| `I.2` | Avoid non-`const` global variables | `02-api-design.md` | `ri-global` |
| `I.3` | Avoid singletons | `02-api-design.md` | `ri-singleton` |
| `I.11` | Never transfer ownership by a raw pointer (`T*`) or reference (`T&`) | `02-api-design.md` | `ri-raw` |
| `I.12` | Declare a pointer that must not be null as `not_null` | `02-api-design.md` | `ri-nullptr` |
| `I.13` | Do not pass an array as a single pointer | `02-api-design.md` | `ri-array` |
| `I.22` | Avoid complex initialization of global objects | `02-api-design.md` | `ri-global-init` |
| `I.24` | Avoid adjacent parameters that can be invoked by the same arguments in either order with different meaning | `02-api-design.md` | `ri-unrelated` |
| `F.6` | If your function must not throw, declare it `noexcept` | `03-functions.md` | `rf-noexcept` |
| `F.43` | Never (directly or indirectly) return a pointer or a reference to a local object | `03-functions.md` | `rf-dangle` |
| `F.45` | Don't return a `T&&` | `03-functions.md` | `rf-return-ref-ref` |
| `F.48` | Don't `return std::move(local)` | `03-functions.md` | `rf-return-move-local` |
| `F.49` | Don't return `const T` | `03-functions.md` | `rf-return-const` |
| `F.53` | Avoid capturing by reference in lambdas that will be used non-locally, including returned, stored on the heap, or passed to another thread | `03-functions.md` | `rf-value-capture` |
| `F.54` | When writing a lambda that captures `this` or any class data member, don't use `[=]` default capture | `03-functions.md` | `rf-this-capture` |
| `F.55` | Don't use `va_arg` arguments | `03-functions.md` | `f-varargs` |
| `F.56` | Avoid unnecessary condition nesting | `03-functions.md` | `f-nesting` |
| `C.7` | Don't define a class or enum and declare a variable of its type in the same statement | `04-classes-and-value-types.md` | `rc-standalone` |
| `C.12` | Don't make data members `const` or references in a copyable or movable type | `04-classes-and-value-types.md` | `rc-constref` |
| `C.20` | If you can avoid defining default operations, do | `04-classes-and-value-types.md` | `rc-zero` |
| `C.36` | A destructor must not fail | `04-classes-and-value-types.md` | `rc-dtor-fail` |
| `C.45` | Don't define a default constructor that only initializes data members; use default member initializers instead | `04-classes-and-value-types.md` | `rc-default` |
| `C.82` | Don't call virtual functions in constructors and destructors | `04-classes-and-value-types.md` | `rc-ctor-virtual` |
| `C.84` | A `swap` function must not fail | `04-classes-and-value-types.md` | `rc-swap-fail` |
| `C.131` | Avoid trivial getters and setters | `04-classes-and-value-types.md` | `rh-get` |
| `C.132` | Don't make a function `virtual` without reason | `04-classes-and-value-types.md` | `rh-virtual` |
| `C.133` | Avoid `protected` data | `04-classes-and-value-types.md` | `rh-protected` |
| `C.137` | Use `virtual` bases to avoid overly general base classes | `04-classes-and-value-types.md` | `rh-vbase` |
| `C.140` | Do not provide different default arguments for a virtual function and an overrider | `04-classes-and-value-types.md` | `rh-virtual-default-arg` |
| `C.146` | Use `dynamic_cast` where class hierarchy navigation is unavoidable | `04-classes-and-value-types.md` | `rh-dynamic_cast` |
| `C.149` | Use `unique_ptr` or `shared_ptr` to avoid forgetting to `delete` objects created using `new` | `04-classes-and-value-types.md` | `rh-smart` |
| `C.152` | Never assign a pointer to an array of derived class objects to a pointer to its base | `04-classes-and-value-types.md` | `rh-array` |
| `C.164` | Avoid implicit conversion operators | `04-classes-and-value-types.md` | `ro-conversion` |
| `C.181` | Avoid "naked" `union`s | `04-classes-and-value-types.md` | `ru-naked` |
| `C.183` | Don't use a `union` for type punning | `04-classes-and-value-types.md` | `ru-pun` |
| `Enum.5` | Don't use `ALL_CAPS` for enumerators | `04-classes-and-value-types.md` | `renum-caps` |
| `Enum.6` | Avoid unnamed enumerations | `04-classes-and-value-types.md` | `renum-unnamed` |
| `R.5` | Prefer scoped objects, don't heap-allocate unnecessarily | `05-resource-management.md` | `rr-scoped` |
| `R.6` | Avoid non-`const` global variables | `05-resource-management.md` | `rr-global` |
| `R.10` | Avoid `malloc()` and `free()` | `05-resource-management.md` | `rr-mallocfree` |
| `R.11` | Avoid calling `new` and `delete` explicitly | `05-resource-management.md` | `rr-newdelete` |
| `R.14` | Avoid `[]` parameters, prefer `span` | `05-resource-management.md` | `rr-ap` |
| `R.37` | Do not pass a pointer or reference obtained from an aliased smart pointer | `05-resource-management.md` | `rr-smartptrget` |
| `ES.3` | Don't repeat yourself, avoid redundant code | `10-expressions-and-statements.md` | `res-dry` |
| `ES.8` | Avoid similar-looking names | `10-expressions-and-statements.md` | `res-name-similar` |
| `ES.9` | Avoid `ALL_CAPS` names | `10-expressions-and-statements.md` | `res-not-caps` |
| `ES.11` | Use `auto` to avoid redundant repetition of type names | `10-expressions-and-statements.md` | `res-auto` |
| `ES.12` | Do not reuse names in nested scopes | `10-expressions-and-statements.md` | `res-reuse` |
| `ES.21` | Don't introduce a variable (or constant) before you need to use it | `10-expressions-and-statements.md` | `res-introduce` |
| `ES.22` | Don't declare a variable until you have a value to initialize it with | `10-expressions-and-statements.md` | `res-init` |
| `ES.26` | Don't use a variable for two unrelated purposes | `10-expressions-and-statements.md` | `res-recycle` |
| `ES.30` | Don't use macros for program text manipulation | `10-expressions-and-statements.md` | `res-macros` |
| `ES.31` | Don't use macros for constants or "functions" | `10-expressions-and-statements.md` | `res-macros2` |
| `ES.40` | Avoid complicated expressions | `10-expressions-and-statements.md` | `res-complicated` |
| `ES.43` | Avoid expressions with undefined order of evaluation | `10-expressions-and-statements.md` | `res-order` |
| `ES.44` | Don't depend on order of evaluation of function arguments | `10-expressions-and-statements.md` | `res-order-fct` |
| `ES.45` | Avoid "magic constants"; use symbolic constants | `10-expressions-and-statements.md` | `res-magic` |
| `ES.46` | Avoid lossy (narrowing, truncating) arithmetic conversions | `10-expressions-and-statements.md` | `res-narrowing` |
| `ES.48` | Avoid casts | `10-expressions-and-statements.md` | `res-casts` |
| `ES.50` | Don't cast away `const` | `10-expressions-and-statements.md` | `res-casts-const` |
| `ES.55` | Avoid the need for range checking | `10-expressions-and-statements.md` | `res-range-checking` |
| `ES.60` | Avoid `new` and `delete` outside resource management functions | `10-expressions-and-statements.md` | `res-new` |
| `ES.62` | Don't compare pointers into different arrays | `10-expressions-and-statements.md` | `res-arr2` |
| `ES.63` | Don't slice | `10-expressions-and-statements.md` | `res-slice` |
| `ES.65` | Don't dereference an invalid pointer | `10-expressions-and-statements.md` | `res-deref` |
| `ES.75` | Avoid `do`-statements | `10-expressions-and-statements.md` | `res-do` |
| `ES.76` | Avoid `goto` | `10-expressions-and-statements.md` | `res-goto` |
| `ES.78` | Don't rely on implicit fallthrough in `switch` statements | `10-expressions-and-statements.md` | `res-break` |
| `ES.84` | Don't try to declare a local variable with no name | `10-expressions-and-statements.md` | `res-noname` |
| `ES.86` | Avoid modifying loop control variables inside the body of raw for-loops | `10-expressions-and-statements.md` | `res-loop-counter` |
| `ES.87` | Don't add redundant `==` or `!=` to conditions | `10-expressions-and-statements.md` | `res-if` |
| `ES.100` | Don't mix signed and unsigned arithmetic | `10-expressions-and-statements.md` | `res-mix` |
| `ES.103` | Don't overflow | `10-expressions-and-statements.md` | `res-overflow` |
| `ES.104` | Don't underflow | `10-expressions-and-statements.md` | `res-underflow` |
| `ES.105` | Don't divide by integer zero | `10-expressions-and-statements.md` | `res-zero` |
| `ES.106` | Don't try to avoid negative values by using `unsigned` | `10-expressions-and-statements.md` | `res-nonnegative` |
| `ES.107` | Don't use `unsigned` for subscripts, prefer `gsl::index` | `10-expressions-and-statements.md` | `res-subscripts` |
| `Per.1` | Don't optimize without reason | `09-performance.md` | `rper-reason` |
| `Per.2` | Don't optimize prematurely | `09-performance.md` | `rper-knuth` |
| `Per.3` | Don't optimize something that's not performance critical | `09-performance.md` | `rper-critical` |
| `Per.4` | Don't assume that complicated code is necessarily faster than simple code | `09-performance.md` | `rper-simple` |
| `Per.5` | Don't assume that low-level code is necessarily faster than high-level code | `09-performance.md` | `rper-low` |
| `Per.6` | Don't make claims about performance without measurements | `09-performance.md` | `rper-measure` |
| `Per.15` | Do not allocate on a critical branch | `09-performance.md` | `rper-alloc0` |
| `Per.30` | Avoid context switches on the critical path | `09-performance.md` | `rper-context` |
| `CP.2` | Avoid data races | `08-concurrency.md` | `rconc-races` |
| `CP.8` | Don't try to use `volatile` for synchronization | `08-concurrency.md` | `rconc-volatile` |
| `CP.9` | Whenever feasible use tools to validate your concurrent code | `08-concurrency.md` | `rconc-tools` |
| `CP.20` | Use RAII, never plain `lock()`/`unlock()` | `08-concurrency.md` | `rconc-raii` |
| `CP.22` | Never call unknown code while holding a lock (e.g., a callback) | `08-concurrency.md` | `rconc-unknown` |
| `CP.26` | Don't `detach()` a thread | `08-concurrency.md` | `rconc-detached_thread` |
| `CP.42` | Don't `wait` without a condition | `08-concurrency.md` | `rconc-wait` |
| `CP.51` | Do not use capturing lambdas that are coroutines | `08-concurrency.md` | `rcoro-capture` |
| `CP.52` | Do not hold locks or other synchronization primitives across suspension points | `08-concurrency.md` | `rcoro-locks` |
| `CP.53` | Parameters to coroutines should not be passed by reference | `08-concurrency.md` | `rcoro-reference-parameters` |
| `CP.100` | Don't use lock-free programming unless you absolutely have to | `08-concurrency.md` | `rconc-lockfree` |
| `CP.110` | Do not write your own double-checked locking for initialization | `08-concurrency.md` | `rconc-double` |
| `E.13` | Never throw while being the direct owner of an object | `06-error-handling.md` | `re-never-throw` |
| `E.16` | Destructors, deallocation, `swap`, and exception type copy/move construction must never fail | `06-error-handling.md` | `re-never-fail` |
| `E.17` | Don't try to catch every exception in every function | `06-error-handling.md` | `re-not-always` |
| `E.28` | Avoid error handling based on global state (e.g. `errno`) | `06-error-handling.md` | `re-no-throw` |
| `E.30` | Don't use exception specifications | `06-error-handling.md` | `re-specifications` |
| `Con.4` | Use `const` to define objects with values that do not change after construction | `10-expressions-and-statements.md` | `rconst-const` |
| `T.11` | Whenever possible use standard concepts | `07-templates-and-generics.md` | `rt-std-concepts` |
| `T.20` | Avoid "concepts" without meaningful semantics | `07-templates-and-generics.md` | `rt-low` |
| `T.25` | Avoid complementary constraints | `07-templates-and-generics.md` | `rt-not` |
| `T.47` | Avoid highly visible unconstrained templates with common names | `07-templates-and-generics.md` | `rt-visible` |
| `T.49` | Where possible, avoid type-erasure | `07-templates-and-generics.md` | `rt-erasure` |
| `T.61` | Do not over-parameterize members (SCARY) | `07-templates-and-generics.md` | `rt-scary` |
| `T.68` | Use `{}` rather than `()` within templates to avoid ambiguities | `07-templates-and-generics.md` | `rt-cast` |
| `T.69` | Inside a template, don't make an unqualified non-member function call unless you intend it to be a customization point | `07-templates-and-generics.md` | `rt-customization` |
| `T.80` | Do not naively templatize a class hierarchy | `07-templates-and-generics.md` | `rt-hier` |
| `T.81` | Do not mix hierarchies and arrays | `07-templates-and-generics.md` | `rt-array` |
| `T.83` | Do not declare a member function template virtual | `07-templates-and-generics.md` | `rt-virtual` |
| `T.103` | Don't use variadic templates for homogeneous argument lists | `07-templates-and-generics.md` | `rt-variadic-not` |
| `T.143` | Don't write unintentionally non-generic code | `07-templates-and-generics.md` | `rt-non-generic` |
| `T.144` | Don't specialize function templates | `07-templates-and-generics.md` | `rt-specialize-function` |
| `SF.2` | A header file must not contain object definitions or non-inline function definitions | `12-project-structure-and-tooling.md` | `rs-inline` |
| `SF.7` | Don't write `using namespace` at global scope in a header file | `12-project-structure-and-tooling.md` | `rs-using-directive` |
| `SF.9` | Avoid cyclic dependencies among source files | `12-project-structure-and-tooling.md` | `rs-cycles` |
| `SF.10` | Avoid dependencies on implicitly `#include`d names | `12-project-structure-and-tooling.md` | `rs-implicit` |
| `SF.21` | Don't use an unnamed (anonymous) namespace in a header | `12-project-structure-and-tooling.md` | `rs-unnamed` |
| `SL.3` | Do not add non-standard entities to namespace `std` | `13-standard-library.md` | `sl-std` |
| `SL.con.3` | Avoid bounds errors | `13-standard-library.md` | `rsl-bounds` |
| `SL.con.4` | don't use `memset` or `memcpy` for arguments that are not trivially-copyable | `13-standard-library.md` | `rsl-copy` |
| `SL.str.5` | Use `std::byte` to refer to byte values that do not necessarily represent characters | `13-standard-library.md` | `rstr-byte` |
| `SL.io.50` | Avoid `endl` | `13-standard-library.md` | `rio-endl` |
| `SL.C.1` | Don't use setjmp/longjmp | `13-standard-library.md` | `rclib-jmp` |
| `NR.1` | Don't insist that all declarations should be at the top of a function | `15-reference-and-glossary.md` | `rnr-top` |
| `NR.2` | Don't insist on having only a single `return`-statement in a function | `15-reference-and-glossary.md` | `rnr-single-return` |
| `NR.3` | Don't avoid exceptions | `15-reference-and-glossary.md` | `rnr-no-exceptions` |
| `NR.4` | Don't insist on placing each class definition in its own source file | `15-reference-and-glossary.md` | `rnr-lots-of-files` |
| `NR.5` | Don't use two-phase initialization | `15-reference-and-glossary.md` | `rnr-two-phase-init` |
| `NR.6` | Don't place all cleanup actions at the end of a function and `goto exit` | `15-reference-and-glossary.md` | `rnr-goto-exit` |
| `NR.7` | Don't make data members `protected` | `15-reference-and-glossary.md` | `rnr-protected-data` |
| `NL.1` | Don't say in comments what can be clearly stated in code | `01-core-idioms.md` | `rl-comments` |
| `NL.5` | Avoid encoding type information in names | `01-core-idioms.md` | `rl-name-type` |
| `NL.19` | Avoid names that are easily misread | `01-core-idioms.md` | `rl-misread` |
| `NL.20` | Don't place two statements on the same line | `01-core-idioms.md` | `rl-stmt` |
| `NL.25` | Don't use `void` as an argument type | `01-core-idioms.md` | `rl-void` |

## Review Routine

1. Scan this table before writing or reviewing C++.
2. Open the home guide for any rule family touched by the code.
3. Prefer repairs that preserve C++ Core Guideline intent: type safety, resource safety, RAII, clear ownership, scoped lifetime, and simple interfaces.
4. When project constraints force a violation, isolate it behind the smallest interface and document the reason, matching `I.30`.

## Recurring Generated-Code Risks

- Raw ownership transfer through `T*` or `T&` instead of RAII handles.
- Uninitialized objects, reused variables, and hidden lifetime extension assumptions.
- `new`/`delete`, `malloc`/`free`, `reinterpret_cast`, macros, and naked unions where safer standard-library or type-system alternatives exist.
- Lambda reference captures that outlive their scope or cross threads.
- Polymorphic base classes without virtual/protected destructors, missing `override`, or public copy/move.
- Detached threads, data races, mutable shared state, or blocking work without lifecycle ownership.
- Exception-safety drift: throwing destructors, broad catch-all handling, or missing `noexcept` on functions that must not throw.
