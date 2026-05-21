# Data Modelling and Types

How to represent data in Erlang and how to describe it to Dialyzer: tagged tuples, records, maps, proplists, binaries and iolists for text, the right collection for the access pattern, and the type language (`-type`, `-opaque`, `-nominal`, `-spec`) with the success-typing model behind it. Representation choices that exist purely for speed live in `10-performance.md`; the tools that check these types (`dialyzer`, `xref`) live in `17-tooling.md`.

Target environment: **Erlang/OTP 27+** (one pattern, DT-19, is OTP 28+). Default toolchain: **rebar3** · **dialyzer + xref** · **elvis + erlfmt** · **eunit + common_test + PropEr** · **EDoc / -doc attributes**.

Grounded in: Erlang Programming Rules (§6.1, §6.2), Inaka guidelines (Records, Types), the Erlang Reference Manual (Data Types, Types and Function Specifications, Nominals), the Efficiency Guide (Maps), Programming Erlang, and Learn You Some Erlang.

---

## DT-01: Use Tagged Tuples for Structured Data and Results

**Strength**: SHOULD

**Summary**: Return and pass structured data as tagged tuples (`{ok, V}` / `{error, R}`, `{Tag, ...}`) so the shape is explicit and matchable, never as a bare in-band value.

```erlang
%% Bad - in-band value: the caller can't tell "missing" from a legitimate result
lookup(K, M) -> maps:get(K, M, undefined).

%% Good - a tagged tuple makes the contract explicit and pattern-matchable
-spec lookup(term(), map()) -> {ok, term()} | {error, not_found}.
lookup(K, M) ->
    case maps:find(K, M) of
        {ok, V} -> {ok, V};
        error   -> {error, not_found}
    end.
```

**Rationale**: A leading atom tag turns a value into a self-describing term that clauses and `case` can dispatch on, and that Dialyzer can reason about. In-band sentinels like `undefined` collide with real data and force callers to guess. Tagged tuples are the idiom behind `gen_server` replies and almost every well-behaved Erlang API.

**See also**: DT-02, DT-16, `02-api-design.md`, `03-error-handling.md`

---

## DT-02: Use Records via Selectors and Constructors, Not as Raw Tuples

**Strength**: SHOULD

**Summary**: Use records as the principal structured datatype, and access them only through the `#rec{}` constructor and `Var#rec.field` selector — never by positional tuple matching.

```erlang
%% Bad - match the record as a positional tuple; breaks the instant a field is added/reordered
{person, Name, _Age, _Phone} = P.

%% Good - constructor and selector syntax survives record changes
#person{name = Name} = P,        %% match form
Name2 = P#person.name.           %% selector form
```

**Rationale**: "A record is a tagged tuple… use records as the principal data structure" (Programming Rules §6.1), and "use selectors and constructors… don't use matching that explicitly assumes that the record is a tuple" (§6.2). Records are tuples at runtime, but treating them positionally couples your code to a layout that the record feature is meant to hide; one added field silently breaks every positional match.

**See also**: DT-03, DT-04, DT-07

---

## DT-03: Type Record Fields and Give Sensible Defaults

**Strength**: SHOULD

**Summary**: Annotate every record field with a type and a default; an untyped record teaches Dialyzer nothing and leaves fields defaulting to `undefined`.

```erlang
%% Bad - untyped record, no defaults; every unset field is silently 'undefined'
-record(user, {id, name, active}).

%% Good - typed fields with defaults dialyzer (and readers) can rely on
-record(user, {id           :: pos_integer(),
               name = <<>>   :: binary(),
               active = true :: boolean()}).
```

**Rationale**: Field types let Dialyzer flag misuse and document intent at the definition site; defaults make `#user{}` construct a valid value rather than one full of `undefined`. A field with no default and a non-`undefined` type is itself a subtle inconsistency Dialyzer will warn about.

**See also**: DT-02, DT-16, DT-17

---

## DT-04: Keep Records Private; Cross Module Boundaries with Opaque Types

**Strength**: SHOULD

**Summary**: Keep a record definition inside its owning module and expose shared objects as an `-opaque` exported type with accessor functions, rather than sharing the record through a header.

```erlang
%% Bad - share the record via a .hrl; every consumer couples to the field layout
%% user.hrl, included everywhere:
-record(user, {id, name}).
%% elsewhere: code matches #user{} and breaks when the record changes

%% Good - record stays internal; the boundary sees an opaque type + accessors
-opaque user() :: #user{}.
-export_type([user/0]).
-export([name/1]).
-spec name(user()) -> binary().
name(#user{name = N}) -> N.
```

**Rationale**: "Records should not be shared among multiple modules. If you need to share objects represented as records, use opaque exported types and provide adequate accessor functions" (Inaka). The classic approach of a shared `.hrl` (Programming Rules §6.1) is acceptable *within* one tightly-coupled, easily-recompiled unit, but across module/application boundaries it leaks representation and forces lock-step recompilation. Prefer encapsulation at the boundary.

**See also**: DT-05, DT-17, `02-api-design.md`

---

## DT-05: Reference Named Types in Specs; Declare Types at the Top of the Module

**Strength**: SHOULD

**Summary**: Write `-spec` against named types, not bare `#record{}`; put `-type`/`-record` declarations at the top of the module and keep types out of header files.

```erlang
%% Bad - a bare record in the spec; reader must hunt for the layout, no abstraction
-spec handle(#state{}) -> {reply, term(), #state{}}.

%% Good - a named type declared up top; the spec reads as intent, not layout
-opaque state() :: #state{}.
-export_type([state/0]).
-spec handle(state()) -> {reply, term(), state()}.
```

**Rationale**: "Avoid using records in your specs, use types" (Inaka). A named type documents intent, can be exported and made opaque, and decouples the contract from the field list. Declaring types and records at the top (not scattered, and not buried in `.hrl` files that invite sharing) keeps a module's data vocabulary in one obvious place.

**See also**: DT-04, DT-17

---

## DT-06: Use Maps for Dynamic, Extensible, or External Data

**Strength**: SHOULD

**Summary**: Represent open-ended, externally-shaped, or evolving data (config, JSON, protocol payloads) as a map, where new keys don't force recompilation.

```erlang
%% Bad - force externally-shaped data into a fixed record; a new key recompiles everyone
-record(event, {type, ts}).
parse(Json) -> #event{type = maps:get(<<"type">>, Json)}.

%% Good - keep open data as a map; match the keys you need, tolerate the rest
handle(#{<<"type">> := Type} = Event) ->
    Ts = maps:get(<<"ts">>, Event, erlang:system_time(second)),
    {Type, Ts}.
```

**Rationale**: Maps grow and shrink at runtime and survive added keys without recompiling consumers, which is exactly what you want for data crossing a system boundary (`json:decode/1` returns maps, OTP 27+). Pattern matching with `:=` lets you require the keys you depend on while ignoring the rest.

**See also**: DT-07, DT-08, `16-distribution.md`

---

## DT-07: Choose Records vs Maps on Properties, Not Performance

**Strength**: CONSIDER

**Summary**: Records and small maps perform similarly; decide by the properties you want — compile-time field safety (records) versus runtime flexibility (maps).

```erlang
%% Bad - reach for a map "because records are slow" (a myth for <=32 fields) and lose typo safety
new() -> #{cuont => 0}.          %% misspelled key compiles fine; fails later at runtime

%% Good - fixed, module-local fields where you want typo safety -> a record
-record(counter, {count = 0 :: non_neg_integer()}).
new() -> #counter{count = 0}.    %% a misspelled field name is a COMPILE error
```

**Rationale**: "The choice between records and maps should be based on the desired properties of the data structure and not performance" — they are expected to perform similarly for small maps (Efficiency Guide, "Maps or Records?"). Records catch misspelled fields at compile time and use slightly less memory but require recompiling all users when a field is added; maps are flexible but only fail on a bad key at runtime. Pick deliberately.

**See also**: DT-06, DT-03, `10-performance.md`

---

## DT-08: Update Maps with `:=` vs `=>` Deliberately

**Strength**: MUST

**Summary**: `=>` adds or replaces a key (upsert); `:=` updates only an existing key and raises `badkey` if it is missing. Use `:=` when you intend to modify, so typos fail loudly.

```erlang
%% Bad - => silently inserts a misspelled key instead of updating the intended one
bump(M) -> M#{conut => maps:get(count, M) + 1}.   %% 'count' unchanged; 'conut' added

%% Good - := updates only an existing key; a typo raises badkey immediately
bump(M) -> M#{count := maps:get(count, M) + 1}.
```

**Rationale**: "`M#{K => V}` adds a new association or replaces an existing one; `M#{K := V}` updates only an existing key… if it does not match, a `badkey` exception is raised" (Reference Manual, "Updating Maps"). Using `:=` for genuine updates turns a silent key typo — one of the few ways maps lose you compile-time safety — into an immediate, located crash.

**See also**: DT-06, DT-07

---

## DT-09: Read Options by Key; Prefer Maps for Rich Config

**Strength**: CONSIDER

**Summary**: Read an options/proplist by key with a default, never by assuming its order or shape; for anything beyond a simple flag list, prefer a map.

```erlang
%% Bad - assume positional structure of an options list
[{timeout, T}, {retries, R}] = Opts.   %% breaks if order differs or a key is absent

%% Good - read by key with a default; order- and presence-independent
T = proplists:get_value(timeout, Opts, 5000),
R = proplists:get_value(retries, Opts, 3).
%% for richer/validated config, prefer a map: maps:get(timeout, Opts, 5000)
```

**Rationale**: Proplists remain idiomatic for simple options lists (and `proplists:get_value/3` tolerates absence with a default), but positional matching is brittle and re-implements lookup badly. As configuration grows, a map gives you `:=` matching, guards, and clearer intent.

**See also**: DT-06, DT-14

---

## DT-10: Represent Sizeable Text as Binaries, Not Char Lists

**Strength**: SHOULD

**Summary**: Use binaries (`<<"...">>`) for strings of any size; reserve char lists for small, locally-manipulated text.

```erlang
%% Bad - large text as a char list: a list of integers, ~8 bytes per character to carry around
Body = "long message " ++ more_text().

%% Good - represent text as a binary; convert mixed input with the unicode module
Body  = <<"long message ">>,
Body2 = unicode:characters_to_binary(Parts).
```

**Rationale**: A char list stores each code point as a full list cell, which is costly to build, copy, and send between processes; binaries are compact and shareable (large ones are reference-counted). Most I/O, parsing, and networking in modern Erlang is binary-first.

**See also**: DT-11, DT-12, `10-performance.md`

---

## DT-11: Build Output with Iolists, Not String Concatenation

**Strength**: SHOULD

**Summary**: Assemble output as an iolist — a nested list of binaries and integers — instead of concatenating with `++`.

```erlang
%% Bad - ++ copies its left operand on every concatenation, and forces list conversions
Msg = "Hello " ++ binary_to_list(Name) ++ "! Have a nice day!".

%% Good - assemble an iolist; IO functions accept it directly, no flattening, no copying
Msg = ["Hello ", Name, "! Have a nice day!"],
file:write(Fd, Msg).
```

**Rationale**: "Use iolists instead of string concatenation whenever possible" (Inaka). An iolist defers concatenation: nothing is copied, and `file`/`gen_tcp`/`io` functions consume the nested structure as-is. `++` copies its whole left side each time and tends to drag in `binary_to_list` conversions that can fail.

**See also**: DT-10, DT-12

---

## DT-12: Construct and Parse Binaries with the Bit Syntax

**Strength**: SHOULD

**Summary**: Use the bit syntax (`<<...>>`) to build and destructure binary data declaratively, rather than slicing with manual offsets.

```erlang
%% Bad - manual slicing with magic offsets is opaque and easy to get wrong
Version = binary:at(Pkt, 0),
Len     = binary:decode_unsigned(binary:part(Pkt, 1, 2)),
Payload = binary:part(Pkt, 3, Len).

%% Good - destructure with the bit syntax: declarative, total, and compiler-optimised
<<Version:8, Len:16, Payload:Len/binary, Rest/binary>> = Pkt.
```

**Rationale**: The bit syntax expresses binary layout directly, binds fields and the remainder in one match, and the compiler optimises matching (and reuses match contexts) far better than ad-hoc `binary:part/3` arithmetic. It is the idiomatic way to handle protocols, file formats, and framing.

**See also**: DT-10, DT-11, `05-functions-and-pattern-matching.md`

---

## DT-13: Never Build Atoms from Untrusted Input

**Strength**: SHOULD

**Summary**: Do not call `list_to_atom/1` (or `binary_to_atom/2`) on external input; the atom table is bounded and never garbage-collected. Use the `existing_atom` variants.

```erlang
%% Bad - external input becomes new atoms forever; the atom table fills and the node crashes (DoS)
route(Name) -> handler(list_to_atom(Name)).

%% Good - only resolve to atoms that already exist
route(Name) -> handler(binary_to_existing_atom(Name, utf8)).
```

**Rationale**: Atoms are not reclaimed and the table has a hard limit (default ~1M); letting untrusted data mint atoms is a classic denial-of-service that takes down the whole node. `binary_to_existing_atom/2` (and `list_to_existing_atom/1`) only succeed for atoms already known to the system, which is what you want at a boundary. **AVOID** the non-`existing` forms on any externally-influenced value.

**See also**: DT-01, `11-anti-patterns.md`

---

## DT-14: Pick the Collection That Fits the Access Pattern

**Strength**: CONSIDER

**Summary**: Match the data structure to how you read and write it — a linear scan of a list in a hot path is the usual mistake.

```erlang
%% Bad - O(n) linear scan of a proplist on every lookup in a hot path
get(K, KVList) -> proplists:get_value(K, KVList).

%% Good - choose the structure for the access pattern
%%   in-process key/value          -> map      (maps:get/2)
%%   ordered / range queries        -> gb_trees
%%   FIFO queue                     -> queue
%%   shared across processes / large -> ets
Val = maps:get(K, Map).
```

**Rationale**: Erlang's stdlib offers `maps`, `gb_trees`, `gb_sets`, `sets`, `ordsets`, `queue`, `array`, `dict`/`orddict`, and `ets`, each with different cost and sharing characteristics. The common performance bug is scanning a list where a map or ETS table belongs. Choose by access pattern and sharing needs, not familiarity.

**See also**: DT-06, DT-09, `10-performance.md`

---

## DT-15: Use Exact Equality `=:=`; Know the Term Order

**Strength**: SHOULD

**Summary**: Prefer `=:=`/`=/=` (exact) over `==`/`/=` (arithmetic coercion), and know that all terms have a single total order.

```erlang
%% Bad - == coerces: 2 == 2.0 is true; this masks type errors and hinders Dialyzer
is_two(X) -> X == 2.

%% Good - =:= is exact: 2 =:= 2.0 is false; reserve == for deliberate numeric coercion
is_two(X) -> X =:= 2.
%% total term order: number < atom < reference < fun < port < pid < tuple < map < list < bitstring
```

**Rationale**: "The book recommends exact equality for general comparison and warns that `==` masks type errors and hinders tools like Dialyzer" (Erlang and OTP in Action, §2.2.9). `=:=` distinguishes `2` from `2.0`; `==` does not. Because every pair of terms is comparable in one total order, `lists:sort/1` works on mixed terms — useful, but a trap if you assumed type-homogeneous data.

**See also**: DT-18, `05-functions-and-pattern-matching.md`

---

## DT-16: Write a `-spec` for Every Exported Function

**Strength**: SHOULD

**Summary**: Give every exported function a `-spec`; it documents the contract and lets Dialyzer check callers.

```erlang
%% Bad - exported function with no contract; Dialyzer has nothing to check callers against
-export([connect/2]).
connect(Host, Port) -> gen_tcp:connect(Host, Port, []).

%% Good - a spec on every exported function
-export([connect/2]).
-spec connect(inet:hostname(), inet:port_number()) ->
          {ok, gen_tcp:socket()} | {error, inet:posix()}.
connect(Host, Port) -> gen_tcp:connect(Host, Port, []).
```

**Rationale**: Specs are the contract Dialyzer propagates across call sites; without them it can only infer success types locally and misses many mismatches. A spec also documents the public API far more precisely than prose, and pairs naturally with EDoc/`-doc`.

**See also**: DT-17, DT-18, `13-documentation.md`

---

## DT-17: Define `-type` Aliases; Hide Representation with `-opaque`; Export Exposed Types

**Strength**: SHOULD

**Summary**: Name domain types with `-type`, hide internals with `-opaque`, and `-export_type` any type that appears in your public specs.

```erlang
%% Bad - leak the representation; callers start matching your internals and couple to them
-export([new/0]).
new() -> {cache, #{}}.            %% callers begin matching {cache, _}

%% Good - name a type, hide representation with -opaque, export it
-opaque cache() :: #{term() => term()}.
-export_type([cache/0]).
-spec new() -> cache().
new() -> #{}.
```

**Rationale**: An `-opaque` type lets callers hold and pass a value without depending on its shape; inspecting it from another module is an *abstraction violation* Dialyzer can detect (Programming Erlang, "Opaque Types"). Exporting types you mention in public specs keeps cross-module Dialyzer analysis honest. (When you don't actually need to hide structure, see DT-19.)

**See also**: DT-04, DT-05, DT-19

---

## DT-18: Treat Dialyzer as Success Typing — Presence of Errors, Not Absence

**Strength**: CONSIDER

**Summary**: Dialyzer never produces false positives but does miss real errors; a clean run is evidence, not proof. Add specs to narrow it, run it in CI, and still test.

```erlang
%% Bad - assume a clean Dialyzer run means the code is type-correct (it is not a sound checker)
-spec area(integer()) -> integer().
area(R) -> 3 * R * R.            %% a float caller may not be flagged at all

%% Good - narrow types with specs, run dialyzer in CI, AND keep tests for behaviour
-spec area(number()) -> number().
area(R) -> 3 * R * R.
```

**Rationale**: Dialyzer uses *success typing*: it only reports a problem when code *cannot* succeed, so it is conservative — "it is never wrong, but it does not find every error." That makes it a high-signal, zero-false-positive gate worth enforcing, but not a substitute for tests (chapter 15) or for writing specs (DT-16) that give it more to work with.

**See also**: DT-16, DT-17, `15-testing.md`, `17-tooling.md`

---

## DT-19: Consider `-nominal` Types to Prevent Mixing Same-Shaped Data (OTP 28+)

**Strength**: CONSIDER

**Summary**: When two types share a structure but must never be interchanged (units, ids), declare them `-nominal` so Dialyzer treats them as incompatible.

```erlang
%% Bad - structural -type: same shape means interchangeable; meters and feet silently mix
-type meter() :: integer().
-type foot()  :: integer().
-spec walk(meter()) -> ok.
walk(_) -> ok.
%% walk(SomeFoot) passes Dialyzer with no warning

%% Good - OTP 28+: -nominal makes same-shaped types incompatible; mixing is flagged
-nominal meter() :: integer().
-nominal foot()  :: integer().
%% passing a foot() where meter() is expected now triggers a Dialyzer warning
```

**Rationale**: By default the compiler uses *structural* typing — `-type` names are ignored, so two equally-shaped types are equivalent (Reference Manual, "Nominals"). `-nominal` (OTP 28+) makes equivalence depend on the declared name. The Reference Manual suggests it for same-structured-but-distinct types, for units (meter/second/byte), and as a faster alternative to `-opaque` when you don't actually need to hide the representation. On OTP 27 or earlier, reach for `-opaque` (DT-17) instead.

**See also**: DT-17, DT-05, `17-tooling.md`

---

## Summary Table

| Pattern | Strength | Key Insight |
|---------|----------|-------------|
| DT-01 Tagged tuples | SHOULD | Self-describing, matchable terms; no in-band sentinels |
| DT-02 Records via selectors | SHOULD | Never match a record as a positional tuple |
| DT-03 Type record fields | SHOULD | Typed fields + defaults; no silent `undefined` |
| DT-04 Keep records private | SHOULD | Cross boundaries with opaque types + accessors |
| DT-05 Named types in specs | SHOULD | `-spec` against types, not bare `#record{}` |
| DT-06 Maps for open data | SHOULD | Dynamic/external/JSON data tolerates new keys |
| DT-07 Records vs maps | CONSIDER | Choose on properties (typo safety vs flexibility), not speed |
| DT-08 `:=` vs `=>` | MUST | `:=` updates existing keys; a typo crashes loudly |
| DT-09 Read options by key | CONSIDER | Never positional; prefer maps for rich config |
| DT-10 Binaries for text | SHOULD | Char lists are heavy; binaries are compact/shareable |
| DT-11 Iolists, not `++` | SHOULD | Defer concatenation; IO accepts nested iolists |
| DT-12 Bit syntax | SHOULD | Declarative binary construction and parsing |
| DT-13 No atoms from input | SHOULD | Atom table is bounded/uncollected; use `existing_atom` |
| DT-14 Right collection | CONSIDER | Match structure to access pattern; avoid list scans |
| DT-15 Exact equality `=:=` | SHOULD | `==` coerces and masks type errors; know term order |
| DT-16 `-spec` everything exported | SHOULD | Contracts Dialyzer can propagate across callers |
| DT-17 `-type`/`-opaque`/export | SHOULD | Name and hide representation; export public types |
| DT-18 Dialyzer = success typing | CONSIDER | No false positives, but misses errors; still test |
| DT-19 `-nominal` types | CONSIDER | OTP 28+: stop same-shaped types from mixing |

## Related Guidelines

- **API design**: See `02-api-design.md` for return conventions and opaque interfaces that DT-01/DT-04/DT-17 support.
- **Functions & pattern matching**: See `05-functions-and-pattern-matching.md` for matching maps, binaries, and records in clause heads.
- **Performance**: See `10-performance.md` for the memory/representation trade-offs behind DT-07, DT-10, and DT-14 (binaries, ETS, maps internals).
- **Anti-patterns**: See `11-anti-patterns.md` for the atom-table-exhaustion trap (DT-13) among others.
- **Documentation & tooling**: See `13-documentation.md` and `17-tooling.md` for how `-spec`/`-type` feed EDoc and Dialyzer.

## External References

- Erlang Programming Rules and Conventions — §6.1 (records as principal data structure), §6.2 (record selectors/constructors)
- [Erlang Reference Manual — Data Types](https://www.erlang.org/doc/system/data_types.html)
- [Erlang Reference Manual — Types and Function Specifications](https://www.erlang.org/doc/system/typespec.html)
- [Erlang Reference Manual — Nominals (`-nominal`, OTP 28+)](https://www.erlang.org/doc/system/nominals.html)
- [Erlang Efficiency Guide — Maps ("Maps or Records?")](https://www.erlang.org/doc/system/maps.html)
- Inaka Erlang Guidelines — Records (don't share records, type record fields), Types (avoid records in specs)
- *Programming Erlang* (Joe Armstrong) — Types, Opaque Types
- *Erlang and OTP in Action* — §2.2.9 (comparing and ordering terms)
