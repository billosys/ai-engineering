# Competency Questions for Inaka's Erlang Coding Guidelines

> Source: "Erlang Coding Standards & Guidelines" — Inaka
> Canonical extraction input: `knowledge/erlang/sources/md/inaka-guidelines/README.md`
> Phase 0 deliverable (per `docs/dev/concept-cards/0010-...-v3.2.md`, Step 0.1).

The source is a single-file mini-book: a catalog of 64 named guidelines split
into **Conventions & Rules** (51 PR-rejection rules) and **Suggestions & Great
Ideas** (13 non-blocking recommendations). CQs below are framed around the
concepts those guidelines define.

## Definitional (What is X?)

1. What is a God module, and why is it an anti-pattern?
2. What is spaghetti code in Erlang?
3. What does the DRY principle mean for Erlang code?
4. What is a dynamic (`Mod:Fun(...)`) function call?
5. What is a non-local return in Erlang?
6. What is an iolist, and why is it preferred over string concatenation?
7. What is the module-state record convention (`#mod_state{}` / `-type state()`)?
8. What are the three Erlang comment levels (`%`, `%%`, `%%%`)?
9. What is the facade pattern for an Erlang library?
10. What is an opaque exported type?
11. What is a `-callback` attribute, and what does it replace?
12. What is a tagged-tuple message?
13. What does "lock your dependencies" mean?
14. What is a behaviour, and what is it used for?
15. What does "encapsulate OTP server APIs" mean?

## Relational (How does X relate to Y?)

1. How does "avoid deep nesting" relate to "more, smaller functions over case expressions"?
2. How does "keep functions small" relate to "avoid deep nesting"?
3. How do records relate to opaque types for encapsulation?
4. How does "don't share your records" relate to the rules for header files?
5. How does "avoid if expressions" relate to pattern matching and `case`?
6. How does "encapsulate OTP server APIs" relate to `xref` and "avoid dynamic calls"?
7. How do function specs relate to Dialyzer?
8. How does "get your types together" relate to "records go first"?
9. How does "CamelCase over Under_Score" relate to the variable/atom naming rules?
10. How does "favor higher-order functions" relate to "prefer pattern-matching over equality"?

## Procedural (How do I do X?)

1. How do I name and type the state record in an OTP behaviour module?
2. How do I lay out exported vs. unexported functions within a module?
3. How do I replace a top-level `case` expression with function clauses?
4. How should I format messages sent between processes?
5. How do I avoid nested header-inclusion conflicts?
6. How do I write `-spec`s for exported functions?
7. How should I name modules, atoms, functions, and variables?
8. How do I replace `case catch` with proper error handling?
9. How do I lock a dependency to a fixed version in `rebar.config`/`erlang.mk`?
10. How should I choose a `lager` logging level?
11. How do I avoid an unnecessary call to `length/1`?
12. How do I provide an accessor-based API instead of sharing a record?

## Prerequisite (What before X?)

1. What must I understand before applying the module-state record convention?
2. What must I know before using `-callback` attributes for a behaviour?
3. What concepts underlie "encapsulate OTP server APIs"?
4. What must I know before using opaque types to stop sharing records?
5. What do I need to know before writing useful function specs?
6. What must I understand before favoring higher-order functions over manual recursion?

## Diagnostic (What distinguishes X from Y?)

1. What distinguishes a "convention/rule" from a "suggestion" in these guidelines?
2. What distinguishes `try...of...catch` from `case catch`?
3. What distinguishes an `if` expression from a `case` expression in idiomatic Erlang?
4. What distinguishes an acceptable macro use from one that should be avoided?
5. What distinguishes when defensive validation belongs on the client vs. the server side?
6. What distinguishes `%`, `%%`, and `%%%` comments?
7. What distinguishes a boolean parameter from a descriptive-atom parameter?
8. What distinguishes a "God module" from a well-scoped module?
