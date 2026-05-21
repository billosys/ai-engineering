# API Design

How to design a module's public surface: keep the export list small and explicit, hide internal data behind opaque types and accessors, spec everything you export, return descriptive errors instead of assuming the caller's intent, and keep modules focused with a tree-shaped dependency graph. The type-language mechanics (`-type`/`-opaque`/`-spec`) live in `04-data-and-types.md`; the behaviour-call encapsulation rule lives in `07-otp-behaviours.md`.

Target environment: **Erlang/OTP 27+**. Default toolchain: **rebar3** · **dialyzer + xref** · **elvis + erlfmt** · **eunit + common_test + PropEr** · **EDoc / -doc attributes**.

Grounded in: the Erlang Programming Rules (§3.1, §3.2, §3.5, §3.11, §6.7), Inaka guidelines (API/Modules), the Erlang Reference Manual (Opaques), and Erlang and OTP in Action.

---

## API-01: Export Few Functions

**Strength**: SHOULD

**Summary**: A module's external complexity is the size of its export list; keep it small.

```erlang
%% Bad - export internals alongside the API; callers face the whole module
-export([start/0, loop/1, handle/2, parse/1, encode/1, helper/1]).

%% Good - export only the functions that form the documented interface
-export([start_link/0, put/2, get/1]).
```

**Rationale**: "Seen from the outside the complexity of a module depends upon the number of functions which are exported" (Programming Rules §3.1). A small export list means a user has less to learn and the maintainer is free to change everything else, as long as the interface holds. A low exported/total ratio is the goal.

**See also**: API-02, API-11, `01-core-idioms.md` (ID-10)

---

## API-02: Never `-compile(export_all)`

**Strength**: SHOULD

**Summary**: List the public functions explicitly in `-export`; never export everything.

```erlang
%% Bad - the public surface is undefined and uncontrollable
-compile(export_all).

%% Good - an explicit, reviewable export list
-export([open/1, close/1, read/2]).
```

**Rationale**: "Do not use the `-compile(export_all)` directive" (Inaka). `export_all` makes every function callable, so there is no documented boundary, xref can't find truly-dead code, and any function becomes an accidental part of the API that someone will depend on. An explicit list *is* the contract.

**See also**: API-01, API-03

---

## API-03: Group Exports by Purpose

**Strength**: CONSIDER

**Summary**: Separate and comment `-export` groups by *why* each function is exported — user interface, inter-module, or within-module-only.

```erlang
%% Bad - one undifferentiated export list
-export([help/0, start/0, make_pid/1, init/1]).

%% Good - grouped and commented by purpose
%% user interface
-export([help/0, start/0]).
%% intermodule exports
-export([make_pid/1]).
%% exported only for spawn/apply within this module
-export([init/1]).
```

**Rationale**: "Make a distinction of why a function is exported" (Programming Rules §6.7). A function may be exported as a user interface, as an interface for other modules, or only because `spawn`/`apply` needs it inside the module. Grouping makes the real public API obvious and signals which "exports" are not meant for general use.

**See also**: API-01, `13-documentation.md`

---

## API-04: Don't Leak Internal Data Structures

**Strength**: SHOULD

**Summary**: Hide a module's representation behind constructor and accessor functions, so the implementation can change without touching callers.

```erlang
%% Bad - the representation leaks: callers know the queue is a list and depend on it
NewQ = [],
N    = length(Queue).

%% Good - an abstract data type: callers use functions; the representation is free to change
NewQ = my_queue:new(),
N    = my_queue:len(Queue).
```

**Rationale**: "Abstracting out internal details of the implementation allows us to change the implementation without changing the code of the modules which call the functions" (Programming Rules §3.11). Exposing a list forces every caller to know it is a list and freezes that choice forever; accessor functions let you swap in a faster representation later with no caller changes.

**See also**: API-05, `04-data-and-types.md` (DT-04)

---

## API-05: Cross Boundaries with Opaque Types — and Honour the Contract

**Strength**: SHOULD

**Summary**: Expose shared data as an `-opaque` type and, as a consumer, never pattern-match or use type-revealing guards on another module's opaque value.

```erlang
%% Bad - a consumer reaches into another module's type with a type-revealing guard
case sets:new() of
    S when is_tuple(S) -> use(S)    %% broke when sets became map-backed in OTP 24
end.

%% Good - define the type opaque; consumers use only the module's functions
-opaque set() :: #{term() => []}.
-export_type([set/0]).
%% consumers call sets:is_element/2 etc., never inspecting the structure
```

**Rationale**: "When a module defines an `-opaque`, the contract is that only the defining module should rely on the definition" (Reference Manual). The runtime does not enforce opacity, but Dialyzer flags violations — and code that matched `sets` as a tuple genuinely broke when the internal representation changed. Respect the contract on both sides: define types opaque, and treat others' opaque values as black boxes.

**See also**: API-04, API-06, `04-data-and-types.md` (DT-17)

---

## API-06: Export the Types Your Public Functions Use

**Strength**: SHOULD

**Summary**: Any type that appears in an exported function's `-spec` should itself be exported with `-export_type`.

```erlang
%% Bad - a public spec mentions types callers cannot name
-spec connect(config()) -> {ok, conn()}.   %% config()/conn() are private

%% Good - export the types used in the public surface
-export_type([config/0, conn/0]).
-spec connect(config()) -> {ok, conn()} | {error, term()}.
```

**Rationale**: A spec that references unexported types can't be used by callers writing their own specs, and Dialyzer's cross-module analysis is weaker for it. Exporting the types your API mentions makes the contract fully expressible at the call site — the type-level counterpart to exporting the functions themselves.

**See also**: API-05, API-07, `04-data-and-types.md` (DT-17)

---

## API-07: Write a `-spec` for Every Exported Function

**Strength**: SHOULD

**Summary**: Give every exported function a `-spec` (and define the types it needs); spec unexported functions too when it documents real intent.

```erlang
%% Bad - an exported function with no contract
-export([run/2]).
run(N, Cmds) -> apply_all(N, Cmds).

%% Good - a -spec plus the types it references
-type command() :: inc | dec.
-spec run(pos_integer(), [command()]) -> pos_integer().
run(N, Cmds) -> apply_all(N, Cmds).
```

**Rationale**: "Write the `-spec`s for your exported funs… define as many types as needed" (Inaka). Specs document the contract precisely for humans, feed EDoc/`-doc` signatures, and give Dialyzer the information it propagates across callers (DT-16). The export list says *what* is public; the specs say what each public function *promises*.

**See also**: API-06, `04-data-and-types.md` (DT-16), `13-documentation.md`

---

## API-08: Return Errors; Don't Assume the Caller's Intent

**Strength**: SHOULD

**Summary**: When input may be invalid, return an `{error, Reason}` descriptor and let the caller decide — don't print, log, or pick a recovery on the caller's behalf.

```erlang
%% Bad - the function decides what to do on bad input and prints to stdout
do_something(Arg) ->
    case check(Arg) of
        ok    -> work(Arg);
        Error -> io:format("* error: ~p~n", [Error])   %% assumes the caller wants this printed
    end.

%% Good - return a descriptor; the caller decides (and formats separately)
-spec do_something(arg()) -> ok | {error, term()}.
do_something(Arg) ->
    case check(Arg) of
        ok    -> work(Arg);
        Error -> {error, Error}
    end.
```

**Rationale**: "Don't make assumptions about why a function has been called or about what the caller wishes to do with the results" (Programming Rules §3.5). A library that prints or exits on bad input is unusable in a context that wanted to handle the error differently. Return structured errors (EH-12) and leave presentation and policy to the caller.

**See also**: API-09, `03-error-handling.md` (EH-01, EH-12)

---

## API-09: Avoid Boolean Parameters

**Strength**: SHOULD

**Summary**: Don't use `true`/`false` to select behaviour; use descriptive atoms that read at the call site.

```erlang
%% Bad - a bare boolean; the call site is unreadable without checking the definition
draw_square(Len, true),
draw_square(Len, false).

%% Good - descriptive atoms state intent where the function is called
draw_square(Len, filled),
draw_square(Len, outline).
```

**Rationale**: "Don't use boolean parameters to control clause selection" (Inaka). `f(X, true)` forces the reader to open the definition to learn what `true` means; `f(X, filled)` says it outright and lets the function clause-match on the meaningful atom. It also extends cleanly to a third option later without reversing a boolean.

**See also**: API-08, API-14, `05-functions-and-pattern-matching.md`

---

## API-10: Hide the Message Protocol Behind Interface Functions

**Strength**: SHOULD

**Summary**: A module's API is functions, not messages; never make callers send raw messages to a process.

```erlang
%% Bad - the API exposes the wire protocol
db ! {self(), {lookup, Key}},
receive {db, Reply} -> Reply end.

%% Good - the protocol is private; callers call a function
lookup(Key) -> db:lookup(Key).   %% db wraps gen_server:call / its own send-receive
```

**Rationale**: Exposing messages couples every caller to the format, so it can never change, and scatters the protocol across the codebase. An interface function gives the interaction a name and a spec and keeps the messaging private — the API-level statement of PC-05/BEH-03.

**See also**: API-04, `06-processes-and-concurrency.md` (PC-05), `07-otp-behaviours.md` (BEH-03)

---

## API-11: No God Modules

**Strength**: SHOULD

**Summary**: Don't accumulate every operation for every entity into one module; keep each module focused on one responsibility.

```erlang
%% Bad - a god module: every operation for every entity in one place
-module(db).
-export([create_user/1, delete_user/1, create_post/1, delete_post/1, create_comment/1]).

%% Good - one module per concern, each with a small surface
-module(users). -export([create/1, delete/1]).
-module(posts). -export([create/1, delete/1]).
```

**Rationale**: "Don't design your system using god modules — modules that have a huge number of functions and/or deal with very unrelated things" (Inaka). A god module accretes until it is a multi-thousand-line monolith no one fully understands and every change risks. Splitting by responsibility keeps each surface small (API-01) and ownership clear.

**See also**: API-01, API-12, `01-core-idioms.md` (ID-10)

---

## API-12: Reduce Inter-Module Dependencies; Keep the Graph a Tree

**Strength**: CONSIDER

**Summary**: Minimise how many modules a module calls, and keep the inter-module call graph acyclic (a tree), not a web of cycles.

```erlang
%% Bad - a module reaches into many others, and dependencies form cycles (a -> b -> a)
%% a.erl calls b, c, d, e, f; e.erl calls back into a

%% Good - depend on a few modules; layers call only downward (a -> b -> c), no back edges
%% the call graph forms a tree, so an interface change touches few callers
```

**Rationale**: "A module which calls functions in many different modules will be more difficult to maintain" (Programming Rules §3.2), because every interface change forces a check of every caller, and cycles make modules impossible to understand or test in isolation. A tree-shaped dependency graph localises the impact of change.

**See also**: API-11, `12-project-structure.md`

---

## API-13: Give a Library a Facade

**Strength**: CONSIDER

**Summary**: Present a library through a single facade module rather than making users wire together its internal modules.

```erlang
%% Bad - users must orchestrate several internal modules to do anything
mylib_conn:open(Cfg),
mylib_proto:frame(Req),
mylib_codec:encode(Framed).

%% Good - one facade module is the library's surface; it delegates internally
-module(mylib).
-export([connect/1, request/2, close/1]).
```

**Rationale**: A facade gives the library one obvious entry point, one place to document, and the freedom to reorganise internal modules without breaking users. It is API-01 and API-04 applied at the package level: a small, stable surface over a changeable interior.

**See also**: API-01, API-11, `12-project-structure.md`

---

## API-14: Name Functions for Intent

**Strength**: CONSIDER

**Summary**: A public function's name should say what it does, so callers needn't read the body to use it correctly.

```erlang
%% Bad - a vague name forces the caller to open the definition
handle(Invoice).

%% Good - the name states intent (intentional programming)
charge_customer(Invoice).
```

**Rationale**: The name is the most-read part of an API. A function that does what its name implies, with a name that reveals its purpose, follows the principle of least astonishment (ID-19) and lets callers reason about code they haven't read. Pair intention-revealing names with descriptive atom arguments (API-09).

**See also**: API-09, `01-core-idioms.md` (ID-19)

---

## Summary Table

| Pattern | Strength | Key Insight |
|---------|----------|-------------|
| API-01 Export few functions | SHOULD | External complexity = export-list size |
| API-02 No `export_all` | SHOULD | The export list is the contract |
| API-03 Group exports by purpose | CONSIDER | Separate UI / inter-module / internal exports |
| API-04 Don't leak data structures | SHOULD | ADTs via constructors/accessors |
| API-05 Opaque + honour the contract | SHOULD | Don't inspect another module's opaque value |
| API-06 Export public types | SHOULD | Types in public specs must be exported |
| API-07 `-spec` every export | SHOULD | The promise behind each public function |
| API-08 Return errors | SHOULD | Don't assume caller intent; don't print |
| API-09 No boolean parameters | SHOULD | Descriptive atoms read at the call site |
| API-10 Hide the protocol | SHOULD | API is functions, not messages |
| API-11 No god modules | SHOULD | One responsibility per module |
| API-12 Tree-shaped deps | CONSIDER | Few dependencies, no cycles |
| API-13 Library facade | CONSIDER | One entry point over a changeable interior |
| API-14 Intentional names | CONSIDER | The name reveals the purpose |

## Related Guidelines

- **Data & types**: See `04-data-and-types.md` — opaque types (DT-17), exported types, and `-spec` discipline (DT-16) are the mechanics behind API-04…API-07.
- **Error handling**: See `03-error-handling.md` — API-08 is EH-01/EH-12 at the interface.
- **Processes & behaviours**: See `06-processes-and-concurrency.md` (PC-05) and `07-otp-behaviours.md` (BEH-03) for hiding the message protocol (API-10).
- **Core idioms**: See `01-core-idioms.md` — focused modules (ID-10) and intention-revealing, consistent names (ID-19).
- **Project structure**: See `12-project-structure.md` for how facades and tree-shaped dependencies map onto applications.

## External References

- Erlang Programming Rules and Conventions — §3.1 (export few), §3.2 (reduce dependencies), §3.5 (don't assume caller intent), §3.11 (hide data structures), §6.7 (group exports)
- [Erlang Reference Manual — Opaques](https://www.erlang.org/doc/system/opaques.html)
- Inaka Erlang Guidelines — Modules/API (no `export_all`, no god modules, avoid boolean parameters, write function specs)
- *Erlang and OTP in Action* — module interface design
