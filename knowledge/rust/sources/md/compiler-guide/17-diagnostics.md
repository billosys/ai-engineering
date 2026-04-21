# Errors and lints

A lot of effort has been put into making `rustc` have great error messages.
This chapter is about how to emit compile errors and lints from the compiler.

## Diagnostic structure

The main parts of a diagnostic error are the following:

```
error[E0000]: main error message
  --> file.rs:LL:CC
   |
LL | <code>
   | -^^^^- secondary label
   |  |
   |  primary label
   |
   = note: note without a `Span`, created with `.note`
note: sub-diagnostic message for `.span_note`
  --> file.rs:LL:CC
   |
LL | more code
   |      ^^^^
```

- Level (`error`, `warning`, etc.). It indicates the severity of the message.
  (See [diagnostic levels](#diagnostic-levels))
- Code (for example, for "mismatched types", it is `E0308`).
  It helps users get more information about the current error through an extended
  description of the problem in the error code index.
  Not all diagnostic have a code.
  For example, diagnostics created by lints don't have one.
- Message.
  It is the main description of the problem.
  It should be general and able to stand on its own, so that it can make sense even in isolation.
- Diagnostic window.
  This contains several things:
  - The path, line number and column of the beginning of the primary span.
  - The users' affected code and its surroundings.
  - Primary and secondary spans underlying the users' code.
    These spans can optionally contain one or more labels.
    - Primary spans should have enough text to describe the problem in such a
      way that if it were the only thing being displayed (for example, in an
      IDE) it would still make sense.
      Because it is "spatially aware" (it
      points at the code), it can generally be more succinct than the error message.
    - If cluttered output can be foreseen in cases when multiple span labels
      overlap, it is a good idea to tweak the output appropriately.
      For example, the `if/else arms have incompatible types` error uses different
      spans depending on whether the arms are all in the same line, if one of
      the arms is empty and if none of those cases applies.
- Sub-diagnostics.
  Any error can have multiple sub-diagnostics that look similar to the main part of the error.
  These are used for cases where the
  order of the explanation might not correspond with the order of the code.
  If the order of the explanation can be "order free", leveraging secondary labels
  in the main diagnostic is preferred, as it is typically less verbose.

The text should be matter of fact and avoid capitalization and periods, unless
multiple sentences are _needed_:

```txt
error: the fobrulator needs to be krontrificated
```

When code or an identifier must appear in a message or label, it should be
surrounded with backticks:

```txt
error: the identifier `foo.bar` is invalid
```

### Error codes and explanations

Most errors have an associated error code.
Error codes are linked to long-form
explanations which contains an example of how to trigger the error and in-depth
details about the error.
They may be viewed with the `--explain` flag, or via the [error index].

As a general rule, give an error a code (with an associated explanation) if the
explanation would give more information than the error itself.
A lot of the time it's better to put all the information in the emitted error itself.
However,
sometimes that would make the error verbose or there are too many possible
triggers to include useful information for all cases in the error, in which case
it's a good idea to add an explanation.[^estebank]
As always, if you are not sure, just ask your reviewer!

If you decide to add a new error with an associated error code, please read
[this section][error-codes] for a guide and important details about the process.

[^estebank]: This rule of thumb was suggested by **@estebank** [here][estebank-comment].

[error index]: https://doc.rust-lang.org/error-index.html
[estebank-comment]: https://github.com/rust-lang/rustc-dev-guide/pull/967#issuecomment-733218283
[error-codes]: ./diagnostics/error-codes.md

### Lints versus fixed diagnostics

Some messages are emitted via [lints](#lints), where the user can control the level.
Most diagnostics are hard-coded such that the user cannot control the level.

Usually it is obvious whether a diagnostic should be "fixed" or a lint, but
there are some grey areas.

Here are a few examples:

- Borrow checker errors: these are fixed errors.
  The user cannot adjust the level of these diagnostics to silence the borrow checker.
- Dead code: this is a lint.
  While the user probably doesn't want dead code in
  their crate, making this a hard error would make refactoring and development very painful.
- [future-incompatible lints]: these are silenceable lints.
  It was decided that making them fixed errors would cause too much breakage,
  so warnings are instead emitted,
  and will eventually be turned into fixed (hard) errors.

Hard-coded warnings (those using methods like `span_warn`) should be avoided
for normal code, preferring to use lints instead.
Some cases, such as warnings with CLI flags, will require the use of hard-coded warnings.

See the `deny` [lint level](#diagnostic-levels) below for guidelines when to
use an error-level lint instead of a fixed error.

[future-incompatible lints]: #future-incompatible-lints

## Diagnostic output style guide

- Write in plain simple English.
  If your message, when shown on a – possibly
  small – screen (which hasn't been cleaned for a while), cannot be understood
  by a normal programmer, who just came out of bed after a night partying,
  it's too complex.
- `Error`, `Warning`, `Note`, and `Help` messages start with a lowercase
  letter and do not end with punctuation.
- Error messages should be succinct.
  Users will see these error messages many
  times, and more verbose descriptions can be viewed with the `--explain` flag.
  That said, don't make it so terse that it's hard to understand.
- The word "illegal" is illegal.
  Prefer "invalid" or a more specific word instead.
- Errors should document the span of code where they occur (use
  [`rustc_errors::DiagCtxt`][DiagCtxt]'s
  `span_*` methods or a diagnostic struct's `#[primary_span]` to easily do this).
  Also `note` other spans that have contributed to the error if the span isn't too large.
- When emitting a message with span, try to reduce the span to the smallest
  amount possible that still signifies the issue
- Try not to emit multiple error messages for the same error.
  This may require detecting duplicates.
- When the compiler has too little information for a specific error message,
  consult with the compiler team to add new attributes for library code that
  allow adding more information.
  For example, see [`#[rustc_on_unimplemented]`](#rustc_on_unimplemented).
  Use these annotations when available!
- Keep in mind that Rust's learning curve is rather steep, and that the
  compiler messages are an important learning tool.
- When talking about the compiler, call it `the compiler`, not `Rust` or `rustc`.
- Use the [Oxford comma](https://en.wikipedia.org/wiki/Serial_comma) when writing lists of items.

### Lint naming

From [RFC 0344], lint names should be consistent, with the following guidelines:

The basic rule is: the lint name should make sense when read as "allow
*lint-name*" or "allow *lint-name* items".
For example, "allow `deprecated` items" and "allow `dead_code`" makes sense, while "allow
`unsafe_block`" is ungrammatical (should be plural).

- Lint names should state the bad thing being checked for, e.g. `deprecated`,
  so that `#[allow(deprecated)]` (items) reads correctly.
  Thus, `ctypes` is not an appropriate name; `improper_ctypes` is.

- Lints that apply to arbitrary items (like the stability lints) should just
  mention what they check for: use `deprecated` rather than `deprecated_items`.
  This keeps lint names short.
  (Again, think "allow *lint-name* items".)

- If a lint applies to a specific grammatical class, mention that class and
  use the plural form: use `unused_variables` rather than `unused_variable`.
  This makes `#[allow(unused_variables)]` read correctly.

- Lints that catch unnecessary, unused, or useless aspects of code should use
  the term `unused`, e.g. `unused_imports`, `unused_typecasts`.

- Use snake case in the same way you would for function names.

[RFC 0344]: https://github.com/rust-lang/rfcs/blob/master/text/0344-conventions-galore.md#lints

### Diagnostic levels

Guidelines for different diagnostic levels:

- `error`: emitted when the compiler detects a problem that makes it unable to
  compile the program, either because the program is invalid or the programmer
  has decided to make a specific `warning` into an error.

- `warning`: emitted when the compiler detects something odd about a program.
  Care should be taken when adding warnings to avoid warning fatigue, and
  avoid false-positives where there really isn't a problem with the code.
  Some examples of when it is appropriate to issue a warning:

  - A situation where the user *should* take action, such as swap out a
    deprecated item, or use a `Result`, but otherwise doesn't prevent compilation.
  - Unnecessary syntax that can be removed without affecting the semantics of the code.
    For example, unused code, or unnecessary `unsafe`.
  - Code that is very likely to be incorrect, dangerous, or confusing, but the
    language technically allows, and is not ready or confident enough to make an error.
    Examples are `unused_comparisons` (out of bounds comparisons) or
    `bindings_with_variant_name` (the user likely did not intend to create a
    binding in a pattern).
  - [Future-incompatible lints](#future-incompatible), where something was
    accidentally or erroneously accepted in the past, but rejecting would
    cause excessive breakage in the ecosystem.
  - Stylistic choices.
    For example, camel or snake case, or the `dyn` trait warning in the 2018 edition.
    These have a high bar to be added, and should only be used in exceptional circumstances.
    Other stylistic choices should
    either be allow-by-default lints, or part of other tools like Clippy or rustfmt.

- `help`: emitted following an `error` or `warning` to give additional
  information to the user about how to solve their problem.
  These messages often include a suggestion string and [`rustc_errors::Applicability`]
  confidence level to guide automated source fixes by tools.
  See the [Suggestions](#suggestions) section for more details.

  The error or warning portion should *not* suggest how to fix the problem,
  only the "help" sub-diagnostic should.

- `note`: emitted to give more context and identify additional circumstances
  and parts of the code that caused the warning or error.
  For example, the borrow checker will note any previous conflicting borrows.

  `help` vs `note`: `help` should be used to show changes the user can
  possibly make to fix the problem.
  `note` should be used for everything else,
  such as other context, information and facts, online resources to read, etc.

Not to be confused with *lint levels*, whose guidelines are:

- `forbid`: Lints should never default to `forbid`.
- `deny`: Equivalent to `error` diagnostic level.
  Some examples:

  - A future-incompatible or edition-based lint that has graduated from the warning level.
  - Something that has an extremely high confidence that is incorrect, but
    still want an escape hatch to allow it to pass.

- `warn`: Equivalent to the `warning` diagnostic level.
  See `warning` above for guidelines.
- `allow`: Examples of the kinds of lints that should default to `allow`:

  - The lint has a too high false positive rate.
  - The lint is too opinionated.
  - The lint is experimental.
  - The lint is used for enforcing something that is not normally enforced.
    For example, the `unsafe_code` lint can be used to prevent usage of unsafe code.

More information about lint levels can be found in the [rustc
book][rustc-lint-levels] and the [reference][reference-diagnostics].

[`rustc_errors::Applicability`]: https://doc.rust-lang.org/nightly/nightly-rustc/rustc_errors/enum.Applicability.html
[reference-diagnostics]: https://doc.rust-lang.org/nightly/reference/attributes/diagnostics.html#lint-check-attributes
[rustc-lint-levels]: https://doc.rust-lang.org/nightly/rustc/lints/levels.html

## Helpful tips and options

### Finding the source of errors

There are three main ways to find where a given error is emitted:

- `grep` for either a sub-part of the error message/label or error code.
  This usually works well and is straightforward, but there are some cases where
  the code emitting the error is removed from the code where the error is
  constructed behind a relatively deep call-stack.
  Even then, it is a good way to get your bearings.
- Invoking `rustc` with the nightly-only flag `-Z treat-err-as-bug=1`
  will treat the first error being emitted as an Internal Compiler Error, which
  allows you to get a stack trace at the point the error has been emitted.
  Change the `1` to something else if you wish to trigger on a later error.

  There are limitations with this approach:
  - Some calls get elided from the stack trace because they get inlined in the compiled `rustc`.
  - The _construction_ of the error is far away from where it is _emitted_,
    a problem similar to the one we faced with the `grep` approach.
    In some cases, we buffer multiple errors in order to emit them in order.
- Invoking `rustc` with `-Z track-diagnostics` will print error creation
  locations alongside the error.

The regular development practices apply: judicious use of `debug!()` statements
and use of a debugger to trigger break points in order to figure out in what
order things are happening.

## `Span`

[`Span`][span] is the primary data structure in `rustc` used to represent a
location in the code being compiled.
`Span`s are attached to most constructs in
HIR and MIR, allowing for more informative error reporting.

[span]: https://doc.rust-lang.org/nightly/nightly-rustc/rustc_span/struct.Span.html

A `Span` can be looked up in a [`SourceMap`][sourcemap] to get a "snippet"
useful for displaying errors with [`span_to_snippet`][sptosnip] and other
similar methods on the `SourceMap`.

[sourcemap]: https://doc.rust-lang.org/nightly/nightly-rustc/rustc_span/source_map/struct.SourceMap.html
[sptosnip]: https://doc.rust-lang.org/nightly/nightly-rustc/rustc_span/source_map/struct.SourceMap.html#method.span_to_snippet

## Error messages

The [`rustc_errors`][errors] crate defines most of the utilities used for reporting errors.

[errors]: https://doc.rust-lang.org/nightly/nightly-rustc/rustc_errors/index.html

Diagnostics can be implemented as types which implement the `Diagnostic` trait.
This is preferred for new diagnostics as it enforces a separation
between diagnostic emitting logic and the main code paths.
For less-complex diagnostics, the `Diagnostic` trait can be derived -- see [Diagnostic
structs][diagnostic-structs].
Within the trait implementation, the APIs described below can be used as normal.

[diagnostic-structs]: ./diagnostics/diagnostic-structs.md

[`DiagCtxt`][DiagCtxt] has methods that create and emit errors.
These methods
usually have names like `span_err` or `struct_span_err` or `span_warn`, etc...
There are lots of them; they emit different types of "errors", such as
warnings, errors, fatal errors, suggestions, etc.

[DiagCtxt]: https://doc.rust-lang.org/nightly/nightly-rustc/rustc_errors/struct.DiagCtxt.html

In general, there are two classes of such methods: ones that emit an error
directly and ones that allow finer control over what to emit.
For example,
[`span_err`][spanerr] emits the given error message at the given `Span`, but
[`struct_span_err`][strspanerr] instead returns a [`Diag`][diag].

Most of these methods will accept strings, but it is recommended that typed
identifiers for translatable diagnostics be used for new diagnostics (see
[Translation][translation]).

[translation]: ./diagnostics/translation.md

`Diag` allows you to add related notes and suggestions to an error
before emitting it by calling the [`emit`][emit] method.
(Failing to either emit or [cancel] a `Diag` will result in an ICE.) See the
[docs][diag] for more info on what you can do.

[spanerr]: https://doc.rust-lang.org/nightly/nightly-rustc/rustc_errors/struct.DiagCtxt.html#method.span_err
[strspanerr]: https://doc.rust-lang.org/nightly/nightly-rustc/rustc_errors/struct.DiagCtxt.html#method.struct_span_err
[diag]: https://doc.rust-lang.org/nightly/nightly-rustc/rustc_errors/struct.Diag.html
[emit]: https://doc.rust-lang.org/nightly/nightly-rustc/rustc_errors/struct.Diag.html#method.emit
[cancel]: https://doc.rust-lang.org/nightly/nightly-rustc/rustc_errors/struct.Diag.html#method.cancel

```rust,ignore
// Get a `Diag`. This does _not_ emit an error yet.
let mut err = sess.dcx.struct_span_err(sp, fluent::example::example_error);

// In some cases, you might need to check if `sp` is generated by a macro to
// avoid printing weird errors about macro-generated code.

if let Ok(snippet) = sess.source_map().span_to_snippet(sp) {
    // Use the snippet to generate a suggested fix
    err.span_suggestion(suggestion_sp, fluent::example::try_qux_suggestion, format!("qux {}", snippet));
} else {
    // If we weren't able to generate a snippet, then emit a "help" message
    // instead of a concrete "suggestion". In practice this is unlikely to be
    // reached.
    err.span_help(suggestion_sp, fluent::example::qux_suggestion);
}

// emit the error
err.emit();
```

```fluent
example-example-error = oh no! this is an error!
  .try-qux-suggestion = try using a qux here
  .qux-suggestion = you could use a qux here instead
```

## Suggestions

In addition to telling the user exactly _why_ their code is wrong, it's
oftentimes furthermore possible to tell them how to fix it.
To this end,
[`Diag`][diag] offers a structured suggestions API, which formats code
suggestions pleasingly in the terminal, or (when the `--error-format json` flag
is passed) as JSON for consumption by tools like [`rustfix`][rustfix].

[diag]: https://doc.rust-lang.org/nightly/nightly-rustc/rustc_errors/struct.Diag.html
[rustfix]: https://github.com/rust-lang/rustfix

Not all suggestions should be applied mechanically, they have a degree of
confidence in the suggested code, from high
(`Applicability::MachineApplicable`) to low (`Applicability::MaybeIncorrect`).
Be conservative when choosing the level.
Use the [`span_suggestion`][span_suggestion] method of `Diag` to
make a suggestion.
The last argument provides a hint to tools whether the suggestion is mechanically applicable or not.

Suggestions point to one or more spans with corresponding code that will
replace their current content.

The message that accompanies them should be understandable in the following contexts:

- shown as an independent sub-diagnostic (this is the default output)
- shown as a label pointing at the affected span (this is done automatically if
some heuristics for verbosity are met)
- shown as a `help` sub-diagnostic with no content (used for cases where the
suggestion is obvious from the text, but we still want to let tools to apply them)
- not shown (used for _very_ obvious cases, but we still want to allow tools to apply them)

[span_suggestion]: https://doc.rust-lang.org/nightly/nightly-rustc/rustc_errors/struct.Diag.html#method.span_suggestion

For example, to make our `qux` suggestion machine-applicable, we would do:

```rust,ignore
let mut err = sess.dcx.struct_span_err(sp, fluent::example::message);

if let Ok(snippet) = sess.source_map().span_to_snippet(sp) {
    err.span_suggestion(
        suggestion_sp,
        fluent::example::try_qux_suggestion,
        format!("qux {}", snippet),
        Applicability::MachineApplicable,
    );
} else {
    err.span_help(suggestion_sp, fluent::example::qux_suggestion);
}

err.emit();
```

This might emit an error like

```console
$ rustc mycode.rs
error[E0999]: oh no! this is an error!
 --> mycode.rs:3:5
  |
3 |     sad()
  |     ^ help: try using a qux here: `qux sad()`

error: aborting due to previous error

For more information about this error, try `rustc --explain E0999`.
```

In some cases, like when the suggestion spans multiple lines or when there are
multiple suggestions, the suggestions are displayed on their own:

```console
error[E0999]: oh no! this is an error!
 --> mycode.rs:3:5
  |
3 |     sad()
  |     ^
help: try using a qux here:
  |
3 |     qux sad()
  |     ^^^

error: aborting due to previous error

For more information about this error, try `rustc --explain E0999`.
```

The possible values of [`Applicability`][appl] are:

- `MachineApplicable`: Can be applied mechanically.
- `HasPlaceholders`: Cannot be applied mechanically because it has placeholder
  text in the suggestions.
  For example: ```try adding a type: `let x: <type>` ```.
- `MaybeIncorrect`: Cannot be applied mechanically because the suggestion may
  or may not be a good one.
- `Unspecified`: Cannot be applied mechanically because we don't know which
  of the above cases it falls into.

[appl]: https://doc.rust-lang.org/nightly/nightly-rustc/rustc_errors/enum.Applicability.html

### Suggestion Style Guide

- Suggestions should not be a question.
  In particular, language like "did you mean" should be avoided.
  Sometimes, it's unclear why a particular suggestion is being made.
  In these cases, it's better to be upfront about what the suggestion is.

  Compare "did you mean: `Foo`" vs.
  "there is a struct with a similar name: `Foo`".

- The message should not contain any phrases like "the following", "as shown",
  etc. Use the span to convey what is being talked about.
- The message may contain further instruction such as "to do xyz, use" or "to do xyz, use abc".
- The message may contain a name of a function, variable, or type, but avoid whole expressions.

## Lints

The compiler linting infrastructure is defined in the [`rustc_middle::lint`][rlint] module.

[rlint]: https://doc.rust-lang.org/nightly/nightly-rustc/rustc_middle/lint/index.html

### When do lints run?

Different lints will run at different times based on what information the lint needs to do its job.
Some lints get grouped into *passes* where the lints
within a pass are processed together via a single visitor.
Some of the passes are:

- Pre-expansion pass: Works on [AST nodes] before [macro expansion].
  This should generally be avoided.
  - Example: [`keyword_idents`] checks for identifiers that will become
    keywords in future editions, but is sensitive to identifiers used in macros.

- Early lint pass: Works on [AST nodes] after [macro expansion] and name
  resolution, just before [AST lowering].
  These lints are for purely syntactical lints.
  - Example: The [`unused_parens`] lint checks for parenthesized-expressions
    in situations where they are not needed, like an `if` condition.

- Late lint pass: Works on [HIR nodes], towards the end of [analysis] (after
  borrow checking, etc.). These lints have full type information available.
  Most lints are late.
  - Example: The [`invalid_value`] lint (which checks for obviously invalid
    uninitialized values) is a late lint because it needs type information to
    figure out whether a type allows being left uninitialized.

- MIR pass: Works on [MIR nodes].
  This isn't quite the same as other passes;
  lints that work on MIR nodes have their own methods for running.
  - Example: The [`arithmetic_overflow`] lint is emitted when it detects a
    constant value that may overflow.

Most lints work well via the pass systems, and they have a fairly
straightforward interface and easy way to integrate (mostly just implementing
a specific `check` function).
However, some lints are easier to write when
they live on a specific code path anywhere in the compiler.
For example, the [`unused_mut`] lint is implemented in the borrow checker as it requires some
information and state in the borrow checker.

Some of these inline lints fire before the linting system is ready.
Those lints will be *buffered* where they are held until later phases of the
compiler when the linting system is ready.
See [Linting early in the compiler](#linting-early-in-the-compiler).


[AST nodes]: the-parser.md
[AST lowering]: ./hir/lowering.md
[HIR nodes]: hir.md
[MIR nodes]: mir/index.md
[macro expansion]: macro-expansion.md
[analysis]: part-4-intro.md
[`keyword_idents`]: https://doc.rust-lang.org/rustc/lints/listing/allowed-by-default.html#keyword-idents
[`unused_parens`]: https://doc.rust-lang.org/rustc/lints/listing/warn-by-default.html#unused-parens
[`invalid_value`]: https://doc.rust-lang.org/rustc/lints/listing/warn-by-default.html#invalid-value
[`arithmetic_overflow`]: https://doc.rust-lang.org/rustc/lints/listing/deny-by-default.html#arithmetic-overflow
[`unused_mut`]: https://doc.rust-lang.org/rustc/lints/listing/warn-by-default.html#unused-mut

### Lint definition terms

Lints are managed via the [`LintStore`][LintStore] and get registered in various ways.
The following terms refer to the different classes of lints
generally based on how they are registered.

- *Built-in* lints are defined inside the compiler source.
- *Driver-registered* lints are registered when the compiler driver is created
  by an external driver.
  This is the mechanism used by Clippy, for example.
- *Tool* lints are lints with a path prefix like `clippy::` or `rustdoc::`.
- *Internal* lints are the `rustc::` scoped tool lints that only run on the
  rustc source tree itself and are defined in the compiler source like a regular built-in lint.

More information about lint registration can be found in the [LintStore] chapter.

[LintStore]: diagnostics/lintstore.md

### Declaring a lint

The built-in compiler lints are defined in the [`rustc_lint`][builtin] crate.
Lints that need to be implemented in other crates are defined in [`rustc_lint_defs`].
You should prefer to place lints in `rustc_lint` if possible.
One benefit is that it is close to the dependency root, so it can be much faster to work on.

[builtin]: https://doc.rust-lang.org/nightly/nightly-rustc/rustc_lint/index.html
[`rustc_lint_defs`]: https://doc.rust-lang.org/nightly/nightly-rustc/rustc_lint_defs/index.html

Every lint is implemented via a `struct` that implements the `LintPass` `trait`
(you can also implement one of the more specific lint pass traits, either
`EarlyLintPass` or `LateLintPass` depending on when is best for your lint to run).
The trait implementation allows you to check certain syntactic constructs
as the linter walks the AST.
You can then choose to emit lints in a very similar way to compile errors.

You also declare the metadata of a particular lint via the [`declare_lint!`] macro.
This macro includes the name, the default level, a short description, and some more details.

Note that the lint and the lint pass must be registered with the compiler.

For example, the following lint checks for uses
of `while true { ... }` and suggests using `loop { ... }` instead.

```rust,ignore
// Declare a lint called `WHILE_TRUE`
declare_lint! {
    WHILE_TRUE,

    // warn-by-default
    Warn,

    // This string is the lint description
    "suggest using `loop { }` instead of `while true { }`"
}

// This declares a struct and a lint pass, providing a list of associated lints. The
// compiler currently doesn't use the associated lints directly (e.g., to not
// run the pass or otherwise check that the pass emits the appropriate set of
// lints). However, it's good to be accurate here as it's possible that we're
// going to register the lints via the get_lints method on our lint pass (that
// this macro generates).
declare_lint_pass!(WhileTrue => [WHILE_TRUE]);

// Helper function for `WhileTrue` lint.
// Traverse through any amount of parenthesis and return the first non-parens expression.
fn pierce_parens(mut expr: &ast::Expr) -> &ast::Expr {
    while let ast::ExprKind::Paren(sub) = &expr.kind {
        expr = sub;
    }
    expr
}

// `EarlyLintPass` has lots of methods. We only override the definition of
// `check_expr` for this lint because that's all we need, but you could
// override other methods for your own lint. See the rustc docs for a full
// list of methods.
impl EarlyLintPass for WhileTrue {
    fn check_expr(&mut self, cx: &EarlyContext<'_>, e: &ast::Expr) {
        if let ast::ExprKind::While(cond, ..) = &e.kind
            && let ast::ExprKind::Lit(ref lit) = pierce_parens(cond).kind
            && let ast::LitKind::Bool(true) = lit.kind
            && !lit.span.from_expansion()
        {
            let condition_span = cx.sess.source_map().guess_head_span(e.span);
            cx.struct_span_lint(WHILE_TRUE, condition_span, |lint| {
                lint.build(fluent::example::use_loop)
                    .span_suggestion_short(
                        condition_span,
                        fluent::example::suggestion,
                        "loop".to_owned(),
                        Applicability::MachineApplicable,
                    )
                    .emit();
            })
        }
    }
}
```

```fluent
example-use-loop = denote infinite loops with `loop {"{"} ... {"}"}`
  .suggestion = use `loop`
```

[`declare_lint!`]: https://doc.rust-lang.org/nightly/nightly-rustc/rustc_lint_defs/macro.declare_lint.html

### Edition-gated lints

Sometimes we want to change the behavior of a lint in a new edition.
To do this,
we just add the transition to our invocation of `declare_lint!`:

```rust,ignore
declare_lint! {
    pub ANONYMOUS_PARAMETERS,
    Allow,
    "detects anonymous parameters",
    Edition::Edition2018 => Warn,
}
```

This makes the `ANONYMOUS_PARAMETERS` lint allow-by-default in the 2015 edition
but warn-by-default in the 2018 edition.

See [Edition-specific lints](./guides/editions.md#edition-specific-lints) for more information.

### Feature-gated lints

Lints belonging to a feature should only be usable if the feature is enabled in the crate.
To support this, lint declarations can contain a feature gate like so:

```rust,ignore
declare_lint! {
    pub SOME_LINT_NAME,
    Warn,
    "a new and useful, but feature gated lint",
    @feature_gate = sym::feature_name;
}
```

### Future-incompatible lints

The use of the term `future-incompatible` within the compiler has a slightly
broader meaning than what rustc exposes to users of the compiler.

Inside rustc, future-incompatible lints are for signalling to the user that code they have
written may not compile in the future.
In general, future-incompatible code exists for two reasons:
* The user has written unsound code that the compiler mistakenly accepted.
  While it is within Rust's backwards compatibility guarantees to fix the soundness hole
(breaking the user's code), the lint is there to warn the user that this will happen
in some upcoming version of rustc *regardless of which edition the code uses*. This is the
meaning that rustc exclusively exposes to users as "future incompatible".
* The user has written code that will either no longer compiler *or* will change
meaning in an upcoming *edition*. These are often called "edition lints" and can be
typically seen in the various "edition compatibility" lint groups (e.g., `rust_2021_compatibility`)
that are used to lint against code that will break if the user updates the crate's edition.
See [migration lints](guides/editions.md#migration-lints) for more details.

A future-incompatible lint should be declared with the `@future_incompatible` additional "field":

```rust,ignore
declare_lint! {
    pub ANONYMOUS_PARAMETERS,
    Allow,
    "detects anonymous parameters",
    @future_incompatible = FutureIncompatibleInfo {
        reason: fcw!(EditionError 2018 "slug-of-edition-guide-page")
    };
}
```

Notice the `reason` field which describes why the future incompatible change is happening.
This will change the diagnostic message the user receives as well as determine which
lint groups the lint is added to.
In the example above, the lint is an "edition lint"
(since its "reason" is `EditionError`), signifying to the user that the use of anonymous
parameters will no longer compile in Rust 2018 and beyond.

Inside [LintStore::register_lints][fi-lint-groupings], lints with `future_incompatible`
fields get placed into either edition-based lint groups (if their `reason` is tied to
an edition) or into the `future_incompatibility` lint group.

[fi-lint-groupings]: https://github.com/rust-lang/rust/blob/51fd129ac12d5bfeca7d216c47b0e337bf13e0c2/compiler/rustc_lint/src/context.rs#L212-L237

If you need a combination of options that's not supported by the
`declare_lint!` macro, you can always change the `declare_lint!` macro to support this.

### Renaming or removing a lint

If it is determined that a lint is either improperly named or no longer needed,
the lint must be registered for renaming or removal, which will trigger a warning if a user tries
to use the old lint name.
To declare a rename/remove, add a line with
[`store.register_renamed`] or [`store.register_removed`] to the code of the
[`rustc_lint::register_builtins`] function.

```rust,ignore
store.register_renamed("single_use_lifetime", "single_use_lifetimes");
```

[`store.register_renamed`]: https://doc.rust-lang.org/nightly/nightly-rustc/rustc_lint/struct.LintStore.html#method.register_renamed
[`store.register_removed`]: https://doc.rust-lang.org/nightly/nightly-rustc/rustc_lint/struct.LintStore.html#method.register_removed
[`rustc_lint::register_builtins`]: https://doc.rust-lang.org/nightly/nightly-rustc/rustc_lint/fn.register_builtins.html

### Lint groups

Lints can be turned on in groups.
These groups are declared in the
[`register_builtins`][rbuiltins] function in [`rustc_lint::lib`][builtin].
The `add_lint_group!` macro is used to declare a new group.

[rbuiltins]: https://doc.rust-lang.org/nightly/nightly-rustc/rustc_lint/fn.register_builtins.html

For example,

```rust,ignore
add_lint_group!(sess,
    "nonstandard_style",
    NON_CAMEL_CASE_TYPES,
    NON_SNAKE_CASE,
    NON_UPPER_CASE_GLOBALS);
```

This defines the `nonstandard_style` group which turns on the listed lints.
A user can turn on these lints with a `#![warn(nonstandard_style)]` attribute in
the source code, or by passing `-W nonstandard-style` on the command line.

Some lint groups are created automatically in `LintStore::register_lints`.
For instance,
any lint declared with `FutureIncompatibleInfo` where the reason is
`FutureIncompatibilityReason::FutureReleaseError` (the default when
`@future_incompatible` is used in `declare_lint!`), will be added to
the `future_incompatible` lint group.
Editions also have their own lint groups
(e.g., `rust_2021_compatibility`) automatically generated for any lints signaling
future-incompatible code that will break in the specified edition.

### Linting early in the compiler

On occasion, you may need to define a lint that runs before the linting system
has been initialized (e.g. during parsing or macro expansion). This is
problematic because we need to have computed lint levels to know whether we
should emit a warning or an error or nothing at all.

To solve this problem, we buffer the lints until the linting system is processed.
[`Session`][sessbl] and [`ParseSess`][parsebl] both have
`buffer_lint` methods that allow you to buffer a lint for later.
The linting system automatically takes care of handling buffered lints later.

[sessbl]: https://doc.rust-lang.org/nightly/nightly-rustc/rustc_session/struct.Session.html#method.buffer_lint
[parsebl]: https://doc.rust-lang.org/nightly/nightly-rustc/rustc_session/parse/struct.ParseSess.html#method.buffer_lint

Thus, to define a lint that runs early in the compilation, one defines a lint
like normal but invokes the lint with `buffer_lint`.

#### Linting even earlier in the compiler

The parser (`rustc_ast`) is interesting in that it cannot have dependencies on
any of the other `rustc*` crates.
In particular, it cannot depend on
`rustc_middle::lint` or `rustc_lint`, where all of the compiler linting infrastructure is defined.
That's troublesome!

To solve this, `rustc_ast` defines its own buffered lint type, which `ParseSess::buffer_lint` uses.
After macro expansion, these buffered lints are
then dumped into the `Session::buffered_lints` used by the rest of the compiler.

## JSON diagnostic output

The compiler accepts an `--error-format json` flag to output
diagnostics as JSON objects (for the benefit of tools such as `cargo fix`).
It looks like this:

```console
$ rustc json_error_demo.rs --error-format json
{"message":"cannot add `&str` to `{integer}`","code":{"code":"E0277","explanation":"\nYou tried to use a type which doesn't implement some trait in a place which\nexpected that trait. Erroneous code example:\n\n```compile_fail,E0277\n// here we declare the Foo trait with a bar method\ntrait Foo {\n    fn bar(&self);\n}\n\n// we now declare a function which takes an object implementing the Foo trait\nfn some_func<T: Foo>(foo: T) {\n    foo.bar();\n}\n\nfn main() {\n    // we now call the method with the i32 type, which doesn't implement\n    // the Foo trait\n    some_func(5i32); // error: the trait bound `i32 : Foo` is not satisfied\n}\n```\n\nIn order to fix this error, verify that the type you're using does implement\nthe trait. Example:\n\n```\ntrait Foo {\n    fn bar(&self);\n}\n\nfn some_func<T: Foo>(foo: T) {\n    foo.bar(); // we can now use this method since i32 implements the\n               // Foo trait\n}\n\n// we implement the trait on the i32 type\nimpl Foo for i32 {\n    fn bar(&self) {}\n}\n\nfn main() {\n    some_func(5i32); // ok!\n}\n```\n\nOr in a generic context, an erroneous code example would look like:\n\n```compile_fail,E0277\nfn some_func<T>(foo: T) {\n    println!(\"{:?}\", foo); // error: the trait `core::fmt::Debug` is not\n                           //        implemented for the type `T`\n}\n\nfn main() {\n    // We now call the method with the i32 type,\n    // which *does* implement the Debug trait.\n    some_func(5i32);\n}\n```\n\nNote that the error here is in the definition of the generic function: Although\nwe only call it with a parameter that does implement `Debug`, the compiler\nstill rejects the function: It must work with all possible input types. In\norder to make this example compile, we need to restrict the generic type we're\naccepting:\n\n```\nuse std::fmt;\n\n// Restrict the input type to types that implement Debug.\nfn some_func<T: fmt::Debug>(foo: T) {\n    println!(\"{:?}\", foo);\n}\n\nfn main() {\n    // Calling the method is still fine, as i32 implements Debug.\n    some_func(5i32);\n\n    // This would fail to compile now:\n    // struct WithoutDebug;\n    // some_func(WithoutDebug);\n}\n```\n\nRust only looks at the signature of the called function, as such it must\nalready specify all requirements that will be used for every type parameter.\n"},"level":"error","spans":[{"file_name":"json_error_demo.rs","byte_start":50,"byte_end":51,"line_start":4,"line_end":4,"column_start":7,"column_end":8,"is_primary":true,"text":[{"text":"    a + b","highlight_start":7,"highlight_end":8}],"label":"no implementation for `{integer} + &str`","suggested_replacement":null,"suggestion_applicability":null,"expansion":null}],"children":[{"message":"the trait `std::ops::Add<&str>` is not implemented for `{integer}`","code":null,"level":"help","spans":[],"children":[],"rendered":null}],"rendered":"error[E0277]: cannot add `&str` to `{integer}`\n --> json_error_demo.rs:4:7\n  |\n4 |     a + b\n  |       ^ no implementation for `{integer} + &str`\n  |\n  = help: the trait `std::ops::Add<&str>` is not implemented for `{integer}`\n\n"}
{"message":"aborting due to previous error","code":null,"level":"error","spans":[],"children":[],"rendered":"error: aborting due to previous error\n\n"}
{"message":"For more information about this error, try `rustc --explain E0277`.","code":null,"level":"","spans":[],"children":[],"rendered":"For more information about this error, try `rustc --explain E0277`.\n"}
```

Note that the output is a series of lines, each of which is a JSON
object, but the series of lines taken together is, unfortunately, not
valid JSON, thwarting tools and tricks (such as [piping to `python3 -m
json.tool`](https://docs.python.org/3/library/json.html#module-json.tool)) that require such.
(One speculates that this was intentional for LSP
performance purposes, so that each line/object can be sent as it is flushed?)

Also note the "rendered" field, which contains the "human" output as a
string; this was introduced so that UI tests could both make use of
the structured JSON and see the "human" output (well, _sans_ colors)
without having to compile everything twice.

The "human" readable and the json format emitter can be found under
`rustc_errors`, both were moved from the `rustc_ast` crate to the
[rustc_errors crate](https://doc.rust-lang.org/nightly/nightly-rustc/rustc_errors/index.html).

The JSON emitter defines [its own `Diagnostic`
struct](https://doc.rust-lang.org/nightly/nightly-rustc/rustc_errors/json/struct.Diagnostic.html)
(and sub-structs) for the JSON serialization.
Don't confuse this with
[`errors::Diag`](https://doc.rust-lang.org/nightly/nightly-rustc/rustc_errors/struct.Diag.html)!

## `#[rustc_on_unimplemented]`

This attribute allows trait definitions to modify error messages when an implementation was
expected but not found.
The string literals in the attribute are format strings and can be formatted with named parameters.
See the Formatting section below for what parameters are permitted.

```rust,ignore
#[rustc_on_unimplemented(message = "an iterator over \
    elements of type `{A}` cannot be built from a \
    collection of type `{Self}`")]
trait MyIterator<A> {
    fn next(&mut self) -> A;
}

fn iterate_chars<I: MyIterator<char>>(i: I) {
    // ...
}

fn main() {
    iterate_chars(&[1, 2, 3][..]);
}
```

When the user compiles this, they will see the following;

```txt
error[E0277]: an iterator over elements of type `char` cannot be built from a collection of type `&[{integer}]`
  --> src/main.rs:13:19
   |
13 |     iterate_chars(&[1, 2, 3][..]);
   |     ------------- ^^^^^^^^^^^^^^ the trait `MyIterator<char>` is not implemented for `&[{integer}]`
   |     |
   |     required by a bound introduced by this call
   |
note: required by a bound in `iterate_chars`
```

You can modify the contents of:
 - the main error message (`message`)
 - the label (`label`)
 - the note(s) (`note`)

For example, the following attribute

```rust,ignore
#[rustc_on_unimplemented(message = "message", label = "label", note = "note")]
trait MyIterator<A> {
    fn next(&mut self) -> A;
}
```

Would generate the following output:

```text
error[E0277]: message
  --> <file>:10:19
   |
10 |     iterate_chars(&[1, 2, 3][..]);
   |     ------------- ^^^^^^^^^^^^^^ label
   |     |
   |     required by a bound introduced by this call
   |
   = help: the trait `MyIterator<char>` is not implemented for `&[{integer}]`
   = note: note
note: required by a bound in `iterate_chars`
```

The functionality discussed so far is also available with
[`#[diagnostic::on_unimplemented]`](https://doc.rust-lang.org/nightly/reference/attributes/diagnostics.html#the-diagnosticon_unimplemented-attribute).
If you can, you should use that instead.

### Filtering

To allow more targeted error messages, it is possible to filter the
application of these fields with `on`.

You can filter on the following boolean flags:
 - `crate_local`: whether the code causing the trait bound to not be
   fulfilled is part of the user's crate.
   This is used to avoid suggesting code changes that would require modifying a dependency.
 - `direct`: whether this is a user-specified rather than derived obligation.
 - `from_desugaring`: whether we are in some kind of desugaring, like `?`
   or a `try` block for example.
   This flag can also be matched on, see below.

You can match on the following names and values, using `name = "value"`:
 - `cause`: Match against one variant of the `ObligationCauseCode` enum.
   Only `"MainFunctionType"` is supported.
 - `from_desugaring`: Match against a particular variant of the `DesugaringKind` enum.
   The desugaring is identified by its variant name, for example
   `"QuestionMark"` for `?` desugaring, or `"TryBlock"` for `try` blocks.
 - `Self` and any generic arguments of the trait, like `Self = "alloc::string::String"`
   or `Rhs="i32"`.

The compiler can provide several values to match on, for example:
  - the self_ty, pretty printed with and without type arguments resolved.
  - `"{integral}"`, if self_ty is an integral of which the type is known.
  - `"[]"`, `"[{ty}]"`, `"[{ty}; _]"`, `"[{ty}; $N]"` when applicable.
  - references to said slices and arrays.
  - `"fn"`, `"unsafe fn"` or `"#[target_feature] fn"` when self is a function.
  - `"{integer}"` and `"{float}"` if the type is a number but we haven't inferred it yet.
  - `"{struct}"`, `"{enum}"` and `"{union}"` to match self as an ADT
  - combinations of the above, like `"[{integral}; _]"`.

For example, the `Iterator` trait can be filtered in the following way:

```rust,ignore
#[rustc_on_unimplemented(
    on(Self = "&str", note = "call `.chars()` or `.as_bytes()` on `{Self}`"),
    message = "`{Self}` is not an iterator",
    label = "`{Self}` is not an iterator",
    note = "maybe try calling `.iter()` or a similar method"
)]
pub trait Iterator {}
```

Which would produce the following outputs:

```text
error[E0277]: `Foo` is not an iterator
 --> src/main.rs:4:16
  |
4 |     for foo in Foo {}
  |                ^^^ `Foo` is not an iterator
  |
  = note: maybe try calling `.iter()` or a similar method
  = help: the trait `std::iter::Iterator` is not implemented for `Foo`
  = note: required by `std::iter::IntoIterator::into_iter`

error[E0277]: `&str` is not an iterator
 --> src/main.rs:5:16
  |
5 |     for foo in "" {}
  |                ^^ `&str` is not an iterator
  |
  = note: call `.chars()` or `.bytes() on `&str`
  = help: the trait `std::iter::Iterator` is not implemented for `&str`
  = note: required by `std::iter::IntoIterator::into_iter`
```

The `on` filter accepts `all`, `any` and `not` predicates similar to the `cfg` attribute:

```rust,ignore
#[rustc_on_unimplemented(on(
    all(Self = "&str", T = "alloc::string::String"),
    note = "you can coerce a `{T}` into a `{Self}` by writing `&*variable`"
))]
pub trait From<T>: Sized {
    /* ... */
}
```

### Formatting

The string literals are format strings that accept parameters wrapped in braces
but positional and listed parameters and format specifiers are not accepted.
The following parameter names are valid:
- `Self` and all generic parameters of the trait.
- `This`: the name of the trait the attribute is on, without generics.
- `Trait`: the name of the "sugared" trait.
  See `TraitRefPrintSugared`.
- `ItemContext`: the kind of `hir::Node` we're in, things like `"an async block"`,
   `"a function"`, `"an async function"`, etc.

Something like:

```rust,ignore
#![feature(rustc_attrs)]

#[rustc_on_unimplemented(message = "Self = `{Self}`, \
    T = `{T}`, this = `{This}`, trait = `{Trait}`, \
    context = `{ItemContext}`")]
pub trait From<T>: Sized {
    fn from(x: T) -> Self;
}

fn main() {
    let x: i8 = From::from(42_i32);
}
```

Will format the message into
```text
"Self = `i8`, T = `i32`, this = `From`, trait = `From<i32>`, context = `a function`"
```


---

# Diagnostic and subdiagnostic structs
rustc has two diagnostic traits that can be used to create diagnostics:
`Diagnostic` and `Subdiagnostic`.

For simple diagnostics,
derived impls can be used, e.g. `#[derive(Diagnostic)]`. They are only suitable for simple diagnostics that
don't require much logic in deciding whether or not to add additional subdiagnostics.

In cases where diagnostics require more complex or dynamic behavior, such as conditionally adding subdiagnostics,
customizing the rendering logic, or selecting messages at runtime, you will need to manually implement
the corresponding trait (`Diagnostic` or `Subdiagnostic`).
This approach provides greater flexibility and is recommended for diagnostics that go beyond simple, static structures.

Diagnostic can be translated into different languages.

## `#[derive(Diagnostic)]`

Consider the [definition][defn] of the "field already declared" diagnostic shown below:

```rust,ignore
#[derive(Diagnostic)]
#[diag("field `{$field_name}` is already declared", code = E0124)]
pub struct FieldAlreadyDeclared {
    pub field_name: Ident,
    #[primary_span]
    #[label("field already declared")]
    pub span: Span,
    #[label("`{$field_name}` first declared here")]
    pub prev_span: Span,
}
```

`Diagnostic` can only be derived on structs and enums.
Attributes that are placed on the type for structs are placed on each 
variants for enums (or vice versa).
Each `Diagnostic` has to have one
attribute, `#[diag(...)]`, applied to the struct or each enum variant.

If an error has an error code (e.g. "E0624"), then that can be specified using
the `code` sub-attribute.
Specifying a `code` isn't mandatory, but if you are
porting a diagnostic that uses `Diag` to use `Diagnostic`
then you should keep the code if there was one.

`#[diag(..)]` must provide a message as the first positional argument.
The message is written in English, but might be translated to the locale requested by the user.
See [translation documentation](./translation.md) to learn more about how
translatable error messages are written and how they are generated.

Every field of the `Diagnostic` which does not have an annotation is
available in Fluent messages as a variable, like `field_name` in the example above.
Fields can be annotated `#[skip_arg]` if this is undesired.

Using the `#[primary_span]` attribute on a field (that has type `Span`)
indicates the primary span of the diagnostic which will have the main message of the diagnostic.

Diagnostics are more than just their primary message, they often include
labels, notes, help messages and suggestions, all of which can also be specified on a `Diagnostic`.

`#[label]`, `#[help]`, `#[warning]` and `#[note]` can all be applied to fields which have the
type `Span`.
Applying any of these attributes will create the corresponding subdiagnostic with that `Span`.
These attributes take a diagnostic message as an argument.

Other types have special behavior when used in a `Diagnostic` derive:

- Any attribute applied to an `Option<T>` will only emit a
  subdiagnostic if the option is `Some(..)`.
- Any attribute applied to a `Vec<T>` will be repeated for each element of the vector.

`#[help]`, `#[warning]` and `#[note]` can also be applied to the struct itself, in which case
they work exactly like when applied to fields except the subdiagnostic won't have a `Span`.
These attributes can also be applied to fields of type `()` for
the same effect, which when combined with the `Option` type can be used to
represent optional `#[note]`/`#[help]`/`#[warning]` subdiagnostics.

Suggestions can be emitted using one of four field attributes:

- `#[suggestion("message", code = "...", applicability = "...")]`
- `#[suggestion_hidden("message", code = "...", applicability = "...")]`
- `#[suggestion_short("message", code = "...", applicability = "...")]`
- `#[suggestion_verbose("message", code = "...", applicability = "...")]`

Suggestions must be applied on either a `Span` field or a `(Span,
MachineApplicability)` field.
Similarly to other field attributes, a message needs to be provided which will be shown to the user.
`code` specifies the code that should be suggested as a
replacement and is a format string (e.g. `{field_name}` would be replaced by
the value of the `field_name` field of the struct).
`applicability` can be used to specify the applicability in the attribute, it
cannot be used when the field's type contains an `Applicability`.

In the end, the `Diagnostic` derive will generate an implementation of
`Diagnostic` that looks like the following:

```rust,ignore
impl<'a, G: EmissionGuarantee> Diagnostic<'a> for FieldAlreadyDeclared {
    fn into_diag(self, dcx: &'a DiagCtxt, level: Level) -> Diag<'a, G> {
        let mut diag = Diag::new(dcx, level, "field `{$field_name}` is already declared");
        diag.set_span(self.span);
        diag.span_label(
            self.span,
            "field already declared"
        );
        diag.span_label(
            self.prev_span,
            "`{$field_name}` first declared here"
        );
        diag
    }
}
```

Now that we've defined our diagnostic, how do we [use it][use]?
It's quite straightforward, just create an instance of the struct and pass it to
`emit_err` (or `emit_warning`):

```rust,ignore
tcx.dcx().emit_err(FieldAlreadyDeclared {
    field_name: f.ident,
    span: f.span,
    prev_span,
});
```

### Reference for `#[derive(Diagnostic)]`
`#[derive(Diagnostic)]` supports the following attributes:

- `#[diag("message", code = "...")]`
  - _Applied to struct or enum variant._
  - _Mandatory_
  - Defines the text and error code to be associated with the diagnostic.
  - Message (_Mandatory_)
    - The diagnostic message which will be shown to the user.
    - See [translation documentation](./translation.md).
  - `code = "..."` (_Optional_)
    - Specifies the error code.
- `#[note("message")]` (_Optional_)
  - _Applied to struct or struct fields of type `Span`, `Option<()>` or `()`._
  - Adds a note subdiagnostic.
  - Value is the note's message.
  - If applied to a `Span` field, creates a spanned note.
- `#[help("message")]` (_Optional_)
  - _Applied to struct or struct fields of type `Span`, `Option<()>` or `()`._
  - Adds a help subdiagnostic.
  - Value is the help message.
  - If applied to a `Span` field, creates a spanned help.
- `#[label("message")]` (_Optional_)
  - _Applied to `Span` fields._
  - Adds a label subdiagnostic.
  - Value is the label's message.
- `#[warning("message")]` (_Optional_)
  - _Applied to struct or struct fields of type `Span`, `Option<()>` or `()`._
  - Adds a warning subdiagnostic.
  - Value is the warning's message.
- `#[suggestion{,_hidden,_short,_verbose}("message", code = "...", applicability = "...")]`
  (_Optional_)
  - _Applied to `(Span, MachineApplicability)` or `Span` fields._
  - Adds a suggestion subdiagnostic.
  - Message (_Mandatory_)
    - Value is the suggestion message that will be shown to the user.
    - See [translation documentation](./translation.md).
  - `code = "..."`/`code("...", ...)` (_Mandatory_)
    - One or multiple format strings indicating the code to be suggested as a replacement.
      Multiple values signify multiple possible replacements.
  - `applicability = "..."` (_Optional_)
    - String which must be one of `machine-applicable`, `maybe-incorrect`,
      `has-placeholders` or `unspecified`.
- `#[subdiagnostic]`
  - _Applied to a type that implements `Subdiagnostic` (from `#[derive(Subdiagnostic)]`)._
  - Adds the subdiagnostic represented by the subdiagnostic struct.
- `#[primary_span]` (_Optional_)
  - _Applied to `Span` fields on `Subdiagnostic`s.
  - Indicates the primary span of the diagnostic.
- `#[skip_arg]` (_Optional_)
  - _Applied to any field._
  - Prevents the field from being provided as a diagnostic argument.

## `#[derive(Subdiagnostic)]`
It is common in the compiler to write a function that conditionally adds a
specific subdiagnostic to an error if it is applicable.
Oftentimes these subdiagnostics could be represented using a diagnostic struct even if the
overall diagnostic could not.
In this circumstance, the `Subdiagnostic`
derive can be used to represent a partial diagnostic (e.g a note, label, help or
suggestion) as a struct.

Consider the [definition][subdiag_defn] of the "expected return type" label shown below:

```rust
#[derive(Subdiagnostic)]
pub enum ExpectedReturnTypeLabel<'tcx> {
    #[label("expected `()` because of default return type")]
    Unit {
        #[primary_span]
        span: Span,
    },
    #[label("expected `{$expected}` because of return type")]
    Other {
        #[primary_span]
        span: Span,
        expected: Ty<'tcx>,
    },
}
```

Like `Diagnostic`, `Subdiagnostic` can be derived for structs or enums.
Attributes that are placed on the type for structs are placed on each
variants for enums (or vice versa).
Each `Subdiagnostic` should have one attribute applied to the struct or each variant, one of:

- `#[label(..)]` for defining a label
- `#[note(..)]` for defining a note
- `#[help(..)]` for defining a help
- `#[warning(..)]` for defining a warning
- `#[suggestion{,_hidden,_short,_verbose}(..)]` for defining a suggestion

All of the above must provide a diagnostic message as the first positional argument.
See [translation documentation](./translation.md) to learn more about how
translatable error messages are generated.

Using the `#[primary_span]` attribute on a field (with type `Span`) will denote
the primary span of the subdiagnostic.
A primary span is only necessary for a label or suggestion, which can not be spanless.

Every field of the type/variant which does not have an annotation is available
in Fluent messages as a variable.
Fields can be annotated `#[skip_arg]` if this is undesired.

Like `Diagnostic`, `Subdiagnostic` supports `Option<T>` and `Vec<T>` fields.

Suggestions can be emitted using one of four attributes on the type/variant:

- `#[suggestion("...", code = "...", applicability = "...")]`
- `#[suggestion_hidden("...", code = "...", applicability = "...")]`
- `#[suggestion_short("...", code = "...", applicability = "...")]`
- `#[suggestion_verbose("...", code = "...", applicability = "...")]`

Suggestions require `#[primary_span]` be set on a field and can have the following sub-attributes:

- The first positional argument specifies the message which will be shown to the user.
- `code` specifies the code that should be suggested as a replacement and is a
  format string (e.g. `{field_name}` would be replaced by the value of the
  `field_name` field of the struct), not a Fluent identifier.
- `applicability` can be used to specify the applicability in the attribute, it
  cannot be used when the field's type contains an `Applicability`.

Applicabilities can also be specified as a field (of type `Applicability`)
using the `#[applicability]` attribute.

In the end, the `Subdiagnostic` derive will generate an implementation
of `Subdiagnostic` that looks like the following:

```rust
impl<'tcx> Subdiagnostic for ExpectedReturnTypeLabel<'tcx> {
    fn add_to_diag(self, diag: &mut rustc_errors::Diagnostic) {
        use rustc_errors::{Applicability, IntoDiagArg};
        match self {
            ExpectedReturnTypeLabel::Unit { span } => {
                diag.span_label(span, "expected `()` because of default return type")
            }
            ExpectedReturnTypeLabel::Other { span, expected } => {
                diag.set_arg("expected", expected);
                diag.span_label(span, "expected `{$expected}` because of return type")
            }
        }
    }
}
```

Once defined, a subdiagnostic can be used by passing it to the `subdiagnostic`
function ([example][subdiag_use_1] and [example][subdiag_use_2]) on a
diagnostic or by assigning it to a `#[subdiagnostic]`-annotated field of a diagnostic struct.

### Argument sharing and isolation

Subdiagnostics add their own arguments (i.e., certain fields in their structure) to the `Diag` structure before rendering the information.
`Diag` structure also stores the arguments from the main diagnostic, so the subdiagnostic can also use the arguments from the main diagnostic.

However, when a subdiagnostic is added to a main diagnostic by implementing `#[derive(Subdiagnostic)]`,
the following rules, introduced in [rust-lang/rust#142724](https://github.com/rust-lang/rust/pull/142724)
apply to the handling of arguments (i.e., variables used in Fluent messages):

**Argument isolation between sub diagnostics**:
Arguments set by a subdiagnostic are only available during the rendering of that subdiagnostic.
After the subdiagnostic is rendered, all arguments it introduced are restored from the main diagnostic.
This ensures that multiple subdiagnostics do not pollute each other's argument scope.
For example, when using a `Vec<Subdiag>`, it iteratively adds the same argument over and over again.

**Same argument override between sub and main diagnostics**:
If a subdiagnostic sets a argument with the same name as a arguments already in the main diagnostic,
it will report an error at runtime unless both have exactly the same value.
It has two benefits:
- preserves the flexibility that arguments in the main diagnostic are allowed to appear in the attributes of the subdiagnostic.
For example, There is an attribute `#[suggestion("...", code = "{new_vis}")]` in the subdiagnostic, but `new_vis` is the field in the main diagnostic struct.
- prevents accidental overwriting or deletion of arguments required by the main diagnostic or other subdiagnostics.

These rules guarantee that arguments injected by subdiagnostics are strictly scoped to their own rendering.
The main diagnostic's arguments remain unaffected by subdiagnostic logic, even in the presence of name collisions.
Additionally, subdiagnostics can access arguments from the main diagnostic with the same name when needed.

### Reference for `#[derive(Subdiagnostic)]`
`#[derive(Subdiagnostic)]` supports the following attributes:

- `#[label("message")]`, `#[help("message")]`, `#[warning("message")]` or `#[note("message")]`
  - _Applied to struct or enum variant.
    Mutually exclusive with struct/enum variant attributes._
  - _Mandatory_
  - Defines the type to be representing a label, help or note.
  - Message (_Mandatory_)
    - The diagnostic message that will be shown to the user.
    - See [translation documentation](./translation.md).
- `#[suggestion{,_hidden,_short,_verbose}("message", code = "...", applicability = "...")]`
  - _Applied to struct or enum variant.
    Mutually exclusive with struct/enum variant attributes._
  - _Mandatory_
  - Defines the type to be representing a suggestion.
  - Message (_Mandatory_)
    - The diagnostic message that will be shown to the user.
    - See [translation documentation](./translation.md).
  - `code = "..."`/`code("...", ...)` (_Mandatory_)
    - One or multiple format strings indicating the code to be suggested as a replacement.
      Multiple values signify multiple possible replacements.
  - `applicability = "..."` (_Optional_)
    - _Mutually exclusive with `#[applicability]` on a field._
    - Value is the applicability of the suggestion.
    - String which must be one of:
      - `machine-applicable`
      - `maybe-incorrect`
      - `has-placeholders`
      - `unspecified`
- `#[multipart_suggestion{,_hidden,_short,_verbose}("message", applicability = "...")]`
  - _Applied to struct or enum variant.
    Mutually exclusive with struct/enum variant attributes._
  - _Mandatory_
  - Defines the type to be representing a multipart suggestion.
  - Message (_Mandatory_): see `#[suggestion]`
  - `applicability = "..."` (_Optional_): see `#[suggestion]`
- `#[primary_span]` (_Mandatory_ for labels and suggestions; _optional_ otherwise; not applicable
to multipart suggestions)
  - _Applied to `Span` fields._
  - Indicates the primary span of the subdiagnostic.
- `#[suggestion_part(code = "...")]` (_Mandatory_; only applicable to multipart suggestions)
  - _Applied to `Span` fields._
  - Indicates the span to be one part of the multipart suggestion.
  - `code = "..."` (_Mandatory_)
    - Value is a format string indicating the code to be suggested as a replacement.
- `#[applicability]` (_Optional_; only applicable to (simple and multipart) suggestions)
  - _Applied to `Applicability` fields._
  - Indicates the applicability of the suggestion.
- `#[skip_arg]` (_Optional_)
  - _Applied to any field._
  - Prevents the field from being provided as a diagnostic argument.

[defn]: https://github.com/rust-lang/rust/blob/6201eabde85db854c1ebb57624be5ec699246b50/compiler/rustc_hir_analysis/src/errors.rs#L68-L77
[use]: https://github.com/rust-lang/rust/blob/f1112099eba41abadb6f921df7edba70affe92c5/compiler/rustc_hir_analysis/src/collect.rs#L823-L827

[subdiag_defn]: https://github.com/rust-lang/rust/blob/f1112099eba41abadb6f921df7edba70affe92c5/compiler/rustc_hir_analysis/src/errors.rs#L221-L234
[subdiag_use_1]: https://github.com/rust-lang/rust/blob/f1112099eba41abadb6f921df7edba70affe92c5/compiler/rustc_hir_analysis/src/check/fn_ctxt/suggestions.rs#L670-L674
[subdiag_use_2]: https://github.com/rust-lang/rust/blob/f1112099eba41abadb6f921df7edba70affe92c5/compiler/rustc_hir_analysis/src/check/fn_ctxt/suggestions.rs#L704-L707


---

# Translation

<div class="warning">
rustc's current diagnostics translation infrastructure (as of
<!-- date-check --> October 2024
) unfortunately causes some friction for compiler contributors, and the current
infrastructure is mostly pending a redesign that better addresses needs of both
compiler contributors and translation teams.
Note that there is no current
active redesign proposals (as of
<!-- date-check --> October 2024
)!

Please see the tracking issue <https://github.com/rust-lang/rust/issues/132181>
for status updates.

The translation infra is waiting for a yet-to-be-proposed redesign and thus rework, we are not
mandating usage of current translation infra.
Use the infra if you *want to* or
otherwise makes the code cleaner, but otherwise sidestep the translation infra
if you need more flexibility.
</div>

rustc's diagnostic infrastructure supports translatable diagnostics using [Fluent].

## Writing translatable diagnostics

There are two ways of writing translatable diagnostics:

1. For simple diagnostics, using a diagnostic (or subdiagnostic) derive.
   ("Simple" diagnostics being those that don't require a lot of logic in
   deciding to emit subdiagnostics and can therefore be represented as diagnostic structs).
   See [the diagnostic and subdiagnostic structs documentation](./diagnostic-structs.md).
2. Using typed identifiers with `Diag` APIs (in `Diagnostic` or `Subdiagnostic` implementations).

When adding or changing a translatable diagnostic,
you don't need to worry about the translations.
Only updating the original English message is required.

## Fluent

Fluent is built around the idea of "asymmetric localization", which aims to
decouple the expressiveness of translations from the grammar of the source
language (English in rustc's case).
Prior to translation, rustc's diagnostics
relied heavily on interpolation to build the messages shown to the users.
Interpolated strings are hard to translate because writing a natural-sounding
translation might require more, less, or just different interpolation than the
English string, all of which would require changes to the compiler's source code to support.

Diagnostic messages are defined in Fluent resources.
A combined set of Fluent
resources for a given locale (e.g. `en-US`) is known as Fluent bundle.

```fluent
typeck_address_of_temporary_taken = cannot take address of a temporary
```

In the above example, `typeck_address_of_temporary_taken` is the identifier for
a Fluent message and corresponds to the diagnostic message in English.
Other Fluent resources can be written which would correspond to a message in another language.
Each diagnostic therefore has at least one Fluent message.

```fluent
typeck_address_of_temporary_taken = cannot take address of a temporary
    .label = temporary value
```

By convention, diagnostic messages for subdiagnostics are specified as
"attributes" on Fluent messages (additional related messages, denoted by the
`.<attribute-name>` syntax).
In the above example, `label` is an attribute of
`typeck_address_of_temporary_taken` which corresponds to the message for the
label added to this diagnostic.

Diagnostic messages often interpolate additional context into the message shown
to the user, such as the name of a type or of a variable.
Additional context to Fluent messages is provided as an "argument" to the diagnostic.

```fluent
typeck_struct_expr_non_exhaustive =
    cannot create non-exhaustive {$what} using struct expression
```

In the above example, the Fluent message refers to an argument named `what`
which is expected to exist (how arguments are provided to diagnostics is discussed in detail later).

You can consult the [Fluent] documentation for other usage examples of Fluent and its syntax.

### Guideline for message naming

Usually, fluent uses `-` for separating words inside a message name.
However,
`_` is accepted by fluent as well.
As `_` fits Rust's use cases better, due to
the identifiers on the Rust side using `_` as well, inside rustc, `-` is not
allowed for separating words, and instead `_` is recommended.
The only exception is for leading `-`s, for message names like `-passes_see_issue`.

### Guidelines for writing translatable messages

For a message to be translatable into different languages, all of the
information required by any language must be provided to the diagnostic as an
argument (not just the information required in the English message).

As the compiler team gain more experience writing diagnostics that have all of
the information necessary to be translated into different languages, this page
will be updated with more guidance.
For now, the [Fluent] documentation has
excellent examples of translating messages into different locales and the
information that needs to be provided by the code to do so.

### Compile-time validation and typed identifiers

rustc's `#[derive(Diagnostic)]` macro performs compile-time validation of Fluent messages.
Compile-time validation of Fluent resources will emit any parsing errors
from Fluent resources while building the compiler, preventing invalid Fluent
resources from causing panics in the compiler.
Compile-time validation also emits an error if multiple Fluent messages have the same identifier.

## Internals

Various parts of rustc's diagnostic internals are modified in order to support translation.

### Messages

All of rustc's traditional diagnostic APIs (e.g. `struct_span_err` or `note`)
take any message that can be converted into a `DiagMessage`.

[`rustc_error_messages::DiagMessage`] can represent legacy non-translatable
diagnostic messages and translatable messages.
Non-translatable messages are just `String`s.
Translatable messages are just a `&'static str` with the
identifier of the Fluent message (sometimes with an additional `&'static str` with an attribute).

`DiagMessage` never needs to be interacted with directly:
`DiagMessage` constants are created for each diagnostic message in a
Fluent resource (described in more detail below), or `DiagMessage`s will
either be created in the macro-generated code of a diagnostic derive.

`DiagMessage`  implements `Into` for any
type that can be converted into a string, and converts these into
non-translatable diagnostics - this keeps all existing diagnostic calls working.

### Arguments

Additional context for Fluent messages which are interpolated into message
contents needs to be provided to translatable diagnostics.

Diagnostics have a `set_arg` function that can be used to provide this
additional context to a diagnostic.

Arguments have both a name (e.g. "what" in the earlier example) and a value.
Argument values are represented using the `DiagArgValue` type, which is just a string or a number.
rustc types can implement `IntoDiagArg` with
conversion into a string or a number, and common types like `Ty<'tcx>` already
have such implementations.

`set_arg` calls are handled transparently by diagnostic derives but need to be
added manually when using diagnostic builder APIs.

[Fluent]: https://projectfluent.org
[`compiler/rustc_borrowck/messages.ftl`]: https://github.com/rust-lang/rust/blob/HEAD/compiler/rustc_borrowck/messages.ftl
[`compiler/rustc_parse/messages.ftl`]: https://github.com/rust-lang/rust/blob/HEAD/compiler/rustc_parse/messages.ftl
[`rustc_error_messages::DiagMessage`]: https://doc.rust-lang.org/nightly/nightly-rustc/rustc_error_messages/enum.DiagMessage.html


---

# Lints

This page documents some of the machinery around lint registration and how we
run lints in the compiler.

The [`LintStore`] is the central piece of infrastructure, around which everything rotates.
The `LintStore` is held as part of the [`Session`], and it
gets populated with the list of lints shortly after the `Session` is created.

## Lints vs. lint passes

There are two parts to the linting mechanism within the compiler: lints and lint passes.
Unfortunately, a lot of the documentation we have refers to both of these as just "lints."

First, we have the lint declarations themselves,
and this is where the name and default lint level and other metadata come from.
These are normally defined by way of the [`declare_lint!`] macro,
which boils down to a static with type [`&rustc_lint_defs::Lint`]
(although this may change in the future,
as the macro is somewhat unwieldy to add new fields to,
like all macros).

We lint against direct declarations without the use of the macro.

Lint declarations don't carry any "state" - they are merely global identifiers
and descriptions of lints.
We assert at runtime that they are not registered twice (by lint name).

Lint passes are the meat of any lint.
Notably, there is not a one-to-one
relationship between lints and lint passes; a lint might not have any lint pass
that emits it, it could have many, or just one -- the compiler doesn't track
whether a pass is in any way associated with a particular lint, and frequently
lints are emitted as part of other work (e.g., type checking, etc.).

## Registration

### High-level overview

In [`rustc_interface::run_compiler`],
the [`LintStore`] is created,
and all lints are registered.

There are three 'sources' of lints:

* internal lints: lints only used by the rustc codebase
* builtin lints: lints built into the compiler and not provided by some outside source
* `rustc_interface::Config`[`register_lints`]: lints passed into the compiler during construction

Lints are registered via the [`LintStore::register_lint`] function.
This should happen just once for any lint, or an ICE will occur.

Once the registration is complete, we "freeze" the lint store by placing it in an `Arc`.

Lint passes are registered separately into one of the categories
(pre-expansion, early, late, late module).
Passes are registered as a closure
-- i.e., `impl Fn() -> Box<dyn X>`, where `dyn X` is either an early or late
lint pass trait object.
When we run the lint passes, we run the closure and then invoke the lint pass methods.
The lint pass methods take `&mut self` so they can keep track of state internally.

#### Internal lints

These are lints used just by the compiler or drivers like `clippy`.
They can be found in [`rustc_lint::internal`].

An example of such a lint is the check that lint passes are implemented using
the `declare_lint_pass!` macro and not by hand.
This is accomplished with the `LINT_PASS_IMPL_WITHOUT_MACRO` lint.

Registration of these lints happens in the [`rustc_lint::register_internals`]
function which is called when constructing a new lint store inside [`rustc_lint::new_lint_store`].

#### Builtin Lints

These are primarily described in two places,
`rustc_lint_defs::builtin` and `rustc_lint::builtin`.
Often the first provides the definitions for the lints themselves,
and the latter provides the lint pass definitions (and implementations),
but this is not always true.

The builtin lint registration happens in the [`rustc_lint::register_builtins`] function.
Just like with internal lints,
this happens inside of [`rustc_lint::new_lint_store`].

#### Driver lints

These are the lints provided by drivers via the `rustc_interface::Config`
[`register_lints`] field, which is a callback.
Drivers should, if finding it
already set, call the function currently set within the callback they add.
The best way for drivers to get access to this is by overriding the
`Callbacks::config` function which gives them direct access to the `Config` structure.

## Compiler lint passes are combined into one pass

Within the compiler, for performance reasons, we usually do not register dozens
of lint passes. Instead, we have a single lint pass of each variety (e.g.,
`BuiltinCombinedModuleLateLintPass`) which will internally call all of the
individual lint passes; this is because then we get the benefits of static over
dynamic dispatch for each of the (often empty) trait methods.

Ideally, we'd not have to do this, since it adds to the complexity of understanding the code.
However, with the current type-erased lint store
approach, it is beneficial to do so for performance reasons.

[`LintStore`]: https://doc.rust-lang.org/nightly/nightly-rustc/rustc_lint/struct.LintStore.html
[`LintStore::register_lint`]: https://doc.rust-lang.org/nightly/nightly-rustc/rustc_lint/struct.LintStore.html#method.register_lints
[`rustc_lint::register_builtins`]: https://doc.rust-lang.org/nightly/nightly-rustc/rustc_lint/fn.register_builtins.html
[`rustc_lint::register_internals`]: https://doc.rust-lang.org/nightly/nightly-rustc/rustc_lint/fn.register_internals.html
[`rustc_lint::new_lint_store`]: https://doc.rust-lang.org/nightly/nightly-rustc/rustc_lint/fn.new_lint_store.html
[`declare_lint!`]: https://doc.rust-lang.org/nightly/nightly-rustc/rustc_session/macro.declare_lint.html
[`declare_tool_lint!`]: https://doc.rust-lang.org/nightly/nightly-rustc/rustc_session/macro.declare_tool_lint.html
[`register_lints`]: https://doc.rust-lang.org/nightly/nightly-rustc/rustc_interface/interface/struct.Config.html#structfield.register_lints
[`&rustc_lint_defs::Lint`]: https://doc.rust-lang.org/nightly/nightly-rustc/rustc_lint_defs/struct.Lint.html
[`Session`]: https://doc.rust-lang.org/nightly/nightly-rustc/rustc_session/struct.Session.html
[`rustc_interface::run_compiler`]: https://doc.rust-lang.org/nightly/nightly-rustc/rustc_interface/index.html#reexport.run_compiler
[`rustc_lint::internal`]: https://doc.rust-lang.org/nightly/nightly-rustc/rustc_lint/internal/index.html


---

# Error codes
We generally try to assign each error message a unique code like `E0123`.
These codes are defined in the compiler in the `diagnostics.rs` files found in each
crate, which basically consist of macros.
All error codes have an associated explanation: new error codes must include them.
Note that not all _historical_ (no longer emitted) error codes have explanations.

## Error explanations

The explanations are written in Markdown (see the [CommonMark Spec] for
specifics around syntax), and all of them are linked in the [`rustc_error_codes`] crate.
Please read [RFC 1567] for details on how to format and write long error codes.
As of <!-- date-check --> March 2026, there is an
effort[^new-explanations] to replace this largely outdated RFC with a new more flexible standard.

Error explanations should expand on the error message and provide details about
_why_ the error occurs.
It is not helpful for users to copy-paste a quick fix;
explanations should help users understand why their code cannot be accepted by the compiler.
Rust prides itself on helpful error messages and long-form explanations are no exception.
However, before error explanations are
overhauled[^new-explanations] it is a bit open as to how exactly they should be
written, as always: ask your reviewer or ask around on the Rust Zulip.

[^new-explanations]: See the draft RFC [here][new-explanations-rfc].

[`rustc_error_codes`]: https://doc.rust-lang.org/nightly/nightly-rustc/rustc_error_codes/index.html
[CommonMark Spec]: https://spec.commonmark.org/current/
[RFC 1567]: https://github.com/rust-lang/rfcs/blob/master/text/1567-long-error-codes-explanation-normalization.md
[new-explanations-rfc]: https://github.com/rust-lang/rfcs/pull/3370

## Allocating a fresh code

Error codes are stored in `compiler/rustc_error_codes`.

To create a new error, you first need to find the next available code.
You can find it by opening `rustc_error_codes/src/lib.rs` and scrolling down 
to the end of the `error_codes!` macro declaration.

Here we might see the highest error code in use is `E0805`, so we _probably_ want `E0806`.
To be sure, run `rg E0806` and check, you should see no references.

You will have to write an extended description for your error,
which will go in `rustc_error_codes/src/error_codes/E0806.md`.
To register the error, add the code (in its proper numerical order) to 
the `error_codes!` macro, like this:

```rust
macro_rules! error_codes {
...
0806,
}
```

To actually issue the error, you can use the `struct_span_code_err!` macro:

```rust
struct_span_code_err!(self.dcx(), // some path to the `DiagCtxt` here
                 span, // whatever span in the source you want
                 E0806, // your new error code
                 fluent::example::an_error_message)
    .emit() // actually issue the error
```

If you want to add notes or other snippets, you can invoke methods before you call `.emit()`:

```rust
struct_span_code_err!(...)
    .span_label(another_span, fluent::example::example_label)
    .span_note(another_span, fluent::example::separate_note)
    .emit()
```

For an example of a PR adding an error code, see [#76143].

[#76143]: https://github.com/rust-lang/rust/pull/76143

## Running error code doctests

To test the examples added in `rustc_error_codes/src/error_codes`, run the
error index generator using:

```
./x test ./src/tools/error_index_generator
```


---

# Diagnostic Items

While writing lints it's common to check for specific types, traits and
functions. This raises the question on how to check for these. Types can be
checked by their complete type path. However, this requires hard coding paths
and can lead to misclassifications in some edge cases. To counteract this,
rustc has introduced diagnostic items that are used to identify types via
[`Symbol`]s.

## Finding diagnostic items

Diagnostic items are added to items inside `rustc`/`std`/`core`/`alloc` with the
`rustc_diagnostic_item` attribute. The item for a specific type can be found by
opening the source code in the documentation and looking for this attribute.
Note that it's often added with the `cfg_attr` attribute to avoid compilation
errors during tests. A definition often looks like this:

```rs
// This is the diagnostic item for this type   vvvvvvv
#[cfg_attr(not(test), rustc_diagnostic_item = "Penguin")]
struct Penguin;
```

Diagnostic items are usually only added to traits,
types,
and standalone functions.
If the goal is to check for an associated type or method,
please use the diagnostic item of the item and reference
[*Using Diagnostic Items*](#using-diagnostic-items).

## Adding diagnostic items

A new diagnostic item can be added with these two steps:

1. Find the target item inside the Rust repo. Now add the diagnostic item as a
   string via the `rustc_diagnostic_item` attribute. This can sometimes cause
   compilation errors while running tests. These errors can be avoided by using
   the `cfg_attr` attribute with the `not(test)` condition (it's fine adding
   then for all `rustc_diagnostic_item` attributes as a preventive manner). At
   the end, it should look like this:

    ```rs
    // This will be the new diagnostic item        vvv
    #[cfg_attr(not(test), rustc_diagnostic_item = "Cat")]
    struct Cat;
    ```

    For the naming conventions of diagnostic items, please refer to
    [*Naming Conventions*](#naming-conventions).

2. <!-- date-check: Feb 2023 -->
   Diagnostic items in code are accessed via symbols in
   [`rustc_span::symbol::sym`].
   To add your newly-created diagnostic item,
   simply open the module file,
   and add the name (In this case `Cat`) at the correct point in the list.

Now you can create a pull request with your changes. :tada:

> NOTE:
> When using diagnostic items in other projects like Clippy,
> it might take some time until the repos get synchronized.

## Naming conventions

Diagnostic items don't have a naming convention yet.
Following are some guidelines that should be used in future,
but might differ from existing names:

* Types, traits, and enums are named using UpperCamelCase
  (Examples: `Iterator` and `HashMap`)
* For type names that are used multiple times,
  like `Writer`,
  it's good to choose a more precise name,
  maybe by adding the module to it
  (Example: `IoWriter`)
* Associated items should not get their own diagnostic items,
  but instead be accessed indirectly by the diagnostic item
  of the type they're originating from.
* Freestanding functions like `std::mem::swap()` should be named using
  `snake_case` with one important (export) module as a prefix
  (Examples: `mem_swap` and `cmp_max`)
* Modules should usually not have a diagnostic item attached to them.
  Diagnostic items were added to avoid the usage of paths,
  and using them on modules would therefore most likely be counterproductive.

## Using diagnostic items

In rustc, diagnostic items are looked up via [`Symbol`]s from inside the
[`rustc_span::symbol::sym`] module. These can then be mapped to [`DefId`]s
using [`TyCtxt::get_diagnostic_item()`] or checked if they match a [`DefId`]
using [`TyCtxt::is_diagnostic_item()`]. When mapping from a diagnostic item to
a [`DefId`], the method will return a `Option<DefId>`. This can be `None` if
either the symbol isn't a diagnostic item or the type is not registered, for
instance when compiling with `#[no_std]`.
All the following examples are based on [`DefId`]s and their usage.

### Example: Checking for a type

```rust
use rustc_span::symbol::sym;

/// This example checks if the given type (`ty`) has the type `HashMap` using
/// `TyCtxt::is_diagnostic_item()`
fn example_1(cx: &LateContext<'_>, ty: Ty<'_>) -> bool {
    match ty.kind() {
        ty::Adt(adt, _) => cx.tcx.is_diagnostic_item(sym::HashMap, adt.did()),
        _ => false,
    }
}
```

### Example: Checking for a trait implementation

```rust
/// This example checks if a given [`DefId`] from a method is part of a trait
/// implementation defined by a diagnostic item.
fn is_diag_trait_item(
    cx: &LateContext<'_>,
    def_id: DefId,
    diag_item: Symbol
) -> bool {
    if let Some(trait_did) = cx.tcx.trait_of_item(def_id) {
        return cx.tcx.is_diagnostic_item(diag_item, trait_did);
    }
    false
}
```

### Associated Types

Associated types of diagnostic items can be accessed indirectly by first
getting the [`DefId`] of the trait and then calling
[`TyCtxt::associated_items()`]. This returns an [`AssocItems`] object which can
be used for further checks. Checkout
[`clippy_utils::ty::get_iterator_item_ty()`] for an example usage of this.

### Usage in Clippy

Clippy tries to use diagnostic items where possible and has developed some
wrapper and utility functions. Please also refer to its documentation when
using diagnostic items in Clippy. (See [*Common tools for writing
lints*][clippy-Common-tools-for-writing-lints].)

## Related issues

These are probably only interesting to people
who really want to take a deep dive into the topic :)

* [rust#60966]: The Rust PR that introduced diagnostic items
* [rust-clippy#5393]: Clippy's tracking issue for moving away from hard coded paths to
  diagnostic item

<!-- Links -->

[`rustc_span::symbol::sym`]: https://doc.rust-lang.org/nightly/nightly-rustc/rustc_span/symbol/sym/index.html
[`Symbol`]: https://doc.rust-lang.org/nightly/nightly-rustc/rustc_span/symbol/struct.Symbol.html
[`DefId`]: https://doc.rust-lang.org/nightly/nightly-rustc/rustc_hir/def_id/struct.DefId.html
[`TyCtxt::get_diagnostic_item()`]: https://doc.rust-lang.org/nightly/nightly-rustc/rustc_middle/ty/context/struct.TyCtxt.html#method.get_diagnostic_item
[`TyCtxt::is_diagnostic_item()`]: https://doc.rust-lang.org/nightly/nightly-rustc/rustc_middle/ty/context/struct.TyCtxt.html#method.is_diagnostic_item
[`TyCtxt::associated_items()`]: https://doc.rust-lang.org/nightly/nightly-rustc/rustc_middle/ty/context/struct.TyCtxt.html#method.associated_items
[`AssocItems`]: https://doc.rust-lang.org/nightly/nightly-rustc/rustc_middle/ty/assoc/struct.AssocItems.html
[`clippy_utils::ty::get_iterator_item_ty()`]: https://github.com/rust-lang/rust-clippy/blob/305177342fbc622c0b3cb148467bab4b9524c934/clippy_utils/src/ty.rs#L55-L72
[clippy-Common-tools-for-writing-lints]: https://doc.rust-lang.org/nightly/clippy/development/common_tools_writing_lints.html
[rust#60966]: https://github.com/rust-lang/rust/pull/60966
[rust-clippy#5393]: https://github.com/rust-lang/rust-clippy/issues/5393


---

# `ErrorGuaranteed`
The previous sections have been about the error message that a user of the
compiler sees. But emitting an error can also have a second important side
effect within the compiler source code: it generates an
[`ErrorGuaranteed`][errorguar].

`ErrorGuaranteed` is a zero-sized type that is unconstructable outside of the
[`rustc_errors`][rerrors] crate. It is generated whenever an error is reported
to the user, so that if your compiler code ever encounters a value of type
`ErrorGuaranteed`, the compilation is _statically guaranteed to fail_. This is
useful for avoiding unsoundness bugs because you can statically check that an
error code path leads to a failure.

There are some important considerations about the usage of `ErrorGuaranteed`:

* It does _not_ convey information about the _kind_ of error. For example, the
  error may be due (indirectly) to a delayed bug or other compiler error.
  Thus, you should not rely on
  `ErrorGuaranteed` when deciding whether to emit an error, or what kind of error
  to emit.
* `ErrorGuaranteed` should not be used to indicate that a compilation _will
  emit_ an error in the future. It should be used to indicate that an error
  _has already been_ emitted -- that is, the [`emit()`][emit] function has
  already been called.  For example, if we detect that a future part of the
  compiler will error, we _cannot_ use `ErrorGuaranteed` unless we first emit
  an error or delayed bug ourselves.

Thankfully, in most cases, it should be statically impossible to abuse
`ErrorGuaranteed`.

[errorguar]: https://doc.rust-lang.org/nightly/nightly-rustc/rustc_errors/struct.ErrorGuaranteed.html
[rerrors]: https://doc.rust-lang.org/nightly/nightly-rustc/rustc_errors/index.html
[emit]: https://doc.rust-lang.org/nightly/nightly-rustc/rustc_errors/diagnostic/struct.Diag.html#method.emit
