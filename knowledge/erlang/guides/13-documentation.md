# Documentation

How to document Erlang on OTP 27+: the first-class `-moduledoc`/`-doc` attributes (which supersede EDoc `@`-tags), documenting types/callbacks/errors, doc signatures derived from `-spec`, testable examples, the three comment levels, and generating browsable output with ExDoc/EDoc. The `-spec`/`-type` mechanics these build on are in `04-data-and-types.md`; comment-level basics are in `01-core-idioms.md`.

Target environment: **Erlang/OTP 27+** (the `-doc`/`-moduledoc` attributes are OTP 27). Default toolchain: **rebar3** · **dialyzer + xref** · **elvis + erlfmt** · **eunit + common_test + PropEr** · **EDoc / -doc attributes**.

Grounded in: the Erlang Reference Manual (Documentation), Erlang and OTP in Action (EDoc), the Erlang Programming Rules (§8.3), and Inaka guidelines.

---

## DC-01: Document Modules and Functions with `-moduledoc`/`-doc`

**Strength**: SHOULD

**Summary**: Use the OTP 27 `-moduledoc` and `-doc` attributes (Markdown by default) for module and function documentation.

```erlang
%% Bad - no extractable documentation (a bare % comment isn't picked up by the doc tools)
-module(arith).
add(A, B) -> A + B.

%% Good - -moduledoc and -doc attributes
-module(arith).
-moduledoc "Basic arithmetic.".
-doc "Add two numbers.".
-spec add(number(), number()) -> number().
add(A, B) -> A + B.
```

**Rationale**: "Documentation in Erlang is done through the `-moduledoc` and `-doc` attributes" (Reference Manual), available since OTP 27. They are first-class attributes (not comments), default to Markdown, and feed both `h(arith)` in the shell and HTML generators. `-moduledoc` documents the module's overall purpose and must precede the first `-doc` or function.

**See also**: DC-02, DC-13, `04-data-and-types.md` (DT-16)

---

## DC-02: Document Exported Types and Callbacks Too

**Strength**: SHOULD

**Summary**: A `-doc` attribute can precede a `-type`/`-opaque` or a `-callback`; document the ones you export.

```erlang
%% Bad - exported type and behaviour callback with no documentation
-export_type([money/0]).
-type money() :: integer().
-callback handle(Event :: term(), State :: term()) -> {ok, term()}.

%% Good - -doc on the type and the callback
-doc "Monetary amount in minor units (cents).".
-type money() :: integer().
-export_type([money/0]).
-doc "Handle one event; return the new state.".
-callback handle(Event :: term(), State :: term()) -> {ok, NewState :: term()}.
```

**Rationale**: "The attributes that can be documented are user-defined types (`-type` and `-opaque`) and behaviour module attributes (`-callback`)" (Reference Manual). Exported types and callbacks are part of your public contract (API-06, BEH-17); documenting them explains what the type *means* and what an implementer's callback must do, beyond what the spec shows.

**See also**: DC-01, `02-api-design.md` (API-06), `07-otp-behaviours.md` (BEH-17)

---

## DC-03: Let Doc Signatures Derive from the `-spec`

**Strength**: CONSIDER

**Summary**: Don't restate a function's shape in prose; the doc signature is derived from the `-spec` (or arg names). Provide a custom signature only when the derived one is unhelpful.

```erlang
%% Bad - the prose duplicates the signature, and will drift from the real -spec
-doc "add(A, B) -> Sum. Adds A and B and returns the sum.".

%% Good - document behaviour; let the signature come from the -spec
-doc "Adds two numbers.".
-spec add(number(), number()) -> number().
%% (a custom signature, if needed, goes as the first line of -doc, up to the ->)
```

**Rationale**: "The doc signature… by default is determined by looking at the names of the arguments in the `-spec` or function" (Reference Manual). Restating the signature in prose duplicates information that the tools already render and that will fall out of sync. Spend the doc text on *what it does and why*, not on retyping the types.

**See also**: DC-01, `04-data-and-types.md` (DT-16)

---

## DC-04: Use the Three Comment Levels

**Strength**: SHOULD

**Summary**: `%%%` for module-level commentary, `%%` for function-level, `%` for inline — distinct from the `-doc` attributes, which are the *extracted* documentation.

```erlang
%% Bad - mismatched levels: %%% inline, % as a module header
% Accounting
total(L) -> %%% sum the items
    lists:sum(L).

%% Good - %%% module, %% function, % inline
%%% Accounting helpers.
%% Sum the line items.
total(L) -> lists:sum(L).   % delegates to lists:sum/1
```

**Rationale**: "Module comments go with `%%%`, function comments with `%%`, and code comments with `%`" (Inaka). The percent count encodes scope and lets readers and editors navigate. Comments explain *implementation* to maintainers; `-doc` attributes (DC-01) are the *interface* documentation extracted for users — use both for their purpose.

**See also**: DC-01, `01-core-idioms.md` (ID-02)

---

## DC-05: Give Every Module a Purpose Statement

**Strength**: SHOULD

**Summary**: State what the module is for in its `-moduledoc` (and follow the project's header conventions for copyright/author).

```erlang
%% Bad - no indication of the module's purpose or ownership
-module(billing).
-export([charge/1]).

%% Good - a module doc that states the purpose
-module(billing).
-moduledoc """
Customer billing: charging cards, issuing refunds, and generating invoices.
""".
-export([charge/1]).
```

**Rationale**: A reader landing in a module should learn its responsibility in one sentence without reverse-engineering the functions. The `-moduledoc` is where that lives; project-wide header conventions (copyright, author, revision history) belong there too where required. A focused purpose statement also reinforces "one responsibility per module" (ID-10/API-11).

**See also**: DC-01, `01-core-idioms.md` (ID-10)

---

## DC-06: Hide Internal Entities with `-doc false`

**Strength**: CONSIDER

**Summary**: Mark functions/types that are exported only for internal reasons with `-doc false` so they don't clutter the public documentation.

```erlang
%% Bad - an internal helper (exported only for spawn/apply) shows up in the public docs
-doc "Normalise the cents value.".
normalise(X) -> X.

%% Good - hide it from the generated documentation
-doc false.
normalise(X) -> X.
```

**Rationale**: The `-doc` attribute "accepts… `false` to hide the entity" (Reference Manual). Some functions are exported for `spawn`/`apply` or behaviour callbacks rather than for users (API-03); `-doc false` keeps them out of the rendered docs so the public surface reads as the actual API.

**See also**: DC-01, `02-api-design.md` (API-03)

---

## DC-07: Make Examples Testable (Doctests)

**Strength**: CONSIDER

**Summary**: Put runnable examples in `-doc` and verify them with `ct_doctest`, so documentation can't silently drift from behaviour.

```erlang
%% Bad - a prose example that has drifted from reality and is never checked
-doc "Example: add(2, 2) returns 5.".

%% Good - a runnable shell example that ct_doctest executes as a test
-doc """
Adds two numbers.

```erlang
1> arith:add(2, 2).
4
```
""".
```

**Rationale**: "Documentation can include examples that are testable using `ct_doctest`" (Reference Manual). An example that runs as part of the test suite stays correct as the code changes — turning documentation from a liability that rots into an asset that's verified. This is the documentation analogue of the runnable GOOD/BAD examples this skill itself uses.

**See also**: DC-01, `15-testing.md`

---

## DC-08: Document the Errors a Function Can Produce

**Strength**: SHOULD

**Summary**: State the exceptions/error returns a function can raise and the conditions that trigger them.

```erlang
%% Bad - the doc omits what the function raises; callers discover it at runtime
-doc "Fetch the user.".
-spec fetch(id()) -> user().

%% Good - document the failure modes and their causes
-doc """
Fetch the user by id.

Raises `error:not_found` if no user exists for `Id`.
""".
-spec fetch(id()) -> user() | no_return().
```

**Rationale**: "All errors should be listed together with… what they mean" (Programming Rules §8.3). A caller can only handle (or deliberately not handle, per let-it-crash) a failure they know about; documenting the error returns and exceptions makes the function's full contract visible. Pair with structured reasons (EH-12) so the documented term is also matchable.

**See also**: DC-02, `03-error-handling.md` (EH-12)

---

## DC-09: Document Message and Data Protocols

**Strength**: SHOULD

**Summary**: For a process or behaviour, document the messages it accepts and the data structures it exchanges — not just the function API.

```erlang
%% Bad - the message protocol lives only in scattered handle_* clauses; callers reverse-engineer it

%% Good - the module doc describes the accepted messages and their replies
-moduledoc """
Cache server.

API messages:
- `{put, Key, Value}` (cast)        — store a value
- `{get, Key}` (call) -> `{ok, Value} | error`
""".
```

**Rationale**: A process's real interface is its message protocol (PC-05/API-10); if that protocol is only implicit in the `handle_*` clauses, callers must read the implementation to use it. Documenting the accepted messages and the shape of replies makes the protocol a contract. Likewise document the public data structures and records callers will encounter.

**See also**: DC-08, `06-processes-and-concurrency.md` (PC-05), `02-api-design.md` (API-10)

---

## DC-10: Write Docs in Markdown, with Structured Metadata

**Strength**: CONSIDER

**Summary**: Use Markdown in `-doc` bodies and the metadata map for structured fields like `deprecated`/`since`.

```erlang
%% Bad - raw HTML and no structured metadata
-doc "<b>Deprecated.</b> use add/2".

%% Good - Markdown body, plus a metadata map for structured fields
-doc #{deprecated => "Use add/2 instead.", since => <<"2.0">>}.
-doc "Adds two numbers. **Note:** integers and floats both work.".
add(A, B) -> A + B.
```

**Rationale**: The default `-doc` format is Markdown (changeable via the `format` metadata key), and a metadata map carries structured fields (`since`, `deprecated`, `equiv`) that tools render specially — e.g. surfacing deprecation in IDEs and generated docs. Markdown keeps source-readable docs that also render well; metadata makes lifecycle facts machine-usable.

**See also**: DC-01, DC-12

---

## DC-11: Delete Dead Code — Don't Comment It Out

**Strength**: SHOULD

**Summary**: Remove unused/old code rather than leaving it commented out "for reference"; version control is the archive.

```erlang
%% Bad - commented-out code kept "just in case"
charge(I) ->
    %% old_charge(I),
    %% case legacy_mode of true -> ...; _ -> ... end,
    new_charge(I).

%% Good - delete it; git remembers
charge(I) -> new_charge(I).
```

**Rationale**: Commented-out code rots — it isn't compiled, tested, or refactored with the rest, so it misleads readers and hides the live path. Version control already preserves history with context (the commit message). Keeping the source lean is itself a form of documentation: what's there is what runs.

**See also**: DC-04, `01-core-idioms.md`

---

## DC-12: Generate and Ship Browsable Documentation

**Strength**: CONSIDER

**Summary**: Generate HTML docs from the attributes (ExDoc or EDoc) and publish them, rather than expecting readers to open source files.

```erlang
%% Bad - rely on users reading .erl files to understand the library

%% Good - generate docs from -moduledoc/-doc and ship them
%% rebar3 ex_doc            %% ExDoc HTML (renders -doc attributes, OTP 27+)
%% or, from the shell:  edoc:application(my_app).
```

**Rationale**: The `-doc` attributes exist to be extracted; ExDoc (the modern generator, also used by OTP itself) and EDoc turn them into searchable HTML with cross-links between functions, types, and callbacks. Publishing generated docs (e.g. to HexDocs) is what makes a library usable without reading its source.

**See also**: DC-01, DC-10, `12-project-structure.md`

---

## DC-13: Prefer `-doc` Attributes over EDoc `@`-Tags on OTP 27+

**Strength**: CONSIDER

**Summary**: For new code on OTP 27+, write `-doc`/`-moduledoc` attributes rather than EDoc `@doc`/`@spec` comment tags.

```erlang
%% Bad - EDoc @-tags in comments for new OTP 27+ code
%% @doc Adds two numbers.
%% @spec add(A::number(), B::number()) -> number()
add(A, B) -> A + B.

%% Good - first-class attributes (Markdown) plus a real -spec
-doc "Adds two numbers.".
-spec add(number(), number()) -> number().
add(A, B) -> A + B.
```

**Rationale**: EDoc `@`-tags live in comments and were the pre-27 standard; the `-doc` attributes are first-class, Markdown-based, integrate with the shell's `h/1`, support testable examples and metadata, and are what OTP and ExDoc now consume. On OTP 27+, prefer attributes for new code; existing `@`-tag docs still work, so migrate as you touch modules.

**See also**: DC-01, DC-03

---

## Summary Table

| Pattern | Strength | Key Insight |
|---------|----------|-------------|
| DC-01 `-moduledoc`/`-doc` | SHOULD | First-class, Markdown docs (OTP 27) |
| DC-02 Document types/callbacks | SHOULD | They're part of the public contract |
| DC-03 Derive doc signatures | CONSIDER | Don't restate the `-spec` in prose |
| DC-04 Comment levels | SHOULD | `%%%`/`%%`/`%`; comments ≠ `-doc` |
| DC-05 Module purpose | SHOULD | One-sentence `-moduledoc` of responsibility |
| DC-06 `-doc false` | CONSIDER | Hide internal-only exports from docs |
| DC-07 Testable examples | CONSIDER | `ct_doctest` keeps examples honest |
| DC-08 Document errors | SHOULD | State what a function raises and when |
| DC-09 Document protocols | SHOULD | Messages/data structures, not just functions |
| DC-10 Markdown + metadata | CONSIDER | Markdown body; `since`/`deprecated` map |
| DC-11 Delete dead code | SHOULD | Don't comment it out; git remembers |
| DC-12 Generate docs | CONSIDER | ExDoc/EDoc HTML, published |
| DC-13 `-doc` over `@`-tags | CONSIDER | Attributes for new OTP 27+ code |

## Related Guidelines

- **Data & types**: See `04-data-and-types.md` — `-spec`/`-type` (DT-16/DT-17) drive doc signatures (DC-03) and the documented contract.
- **Core idioms**: See `01-core-idioms.md` — comment levels (ID-02) underlie DC-04.
- **API design**: See `02-api-design.md` — DC-02/DC-06/DC-09 document the surface defined by API-06/API-03/API-10.
- **OTP behaviours**: See `07-otp-behaviours.md` (BEH-17) for documenting custom-behaviour callbacks.
- **Error handling**: See `03-error-handling.md` (EH-12) for the structured reasons DC-08 documents.

## External References

- [Erlang Reference Manual — Documentation (`-moduledoc`/`-doc`)](https://www.erlang.org/doc/system/documentation.html)
- [EDoc User's Guide](https://www.erlang.org/doc/apps/edoc/chapter.html)
- [ExDoc](https://hexdocs.pm/ex_doc/)
- Erlang Programming Rules and Conventions — §8.3 (document all errors)
- *Erlang and OTP in Action* — §3.2.2 (EDoc)
- Inaka Erlang Guidelines — comment levels; don't comment out code
