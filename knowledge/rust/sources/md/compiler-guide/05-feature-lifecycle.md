<!-- date-check: Jul 2025 -->

# Implementing new language features

When you want to implement a new significant feature in the compiler,
you need to go through this process to make sure everything goes smoothly.

**NOTE: This section is for *language* features, not *library* features,
which use [a different process].**

See also [the Rust Language Design Team's procedures][lang-propose] for proposing changes to the language.

[a different process]: ./stability.md
[lang-propose]: https://lang-team.rust-lang.org/how_to/propose.html

## The @rfcbot FCP process

When the change is small, uncontroversial, non-breaking,
and does not affect the stable language in any user-observable ways or add any new unstable features,
then it can be done with just writing a PR and getting an r+ from someone who knows that part of the code.
However, if not, more must be done.
Even for compiler-internal work,
it would be a bad idea to push a controversial change without consensus from the rest of the team
(both in the "distributed system" sense to make sure you don't break anything you don't know about,
and in the social sense to avoid PR fights).

For changes that need the consensus of a team,
we use the process of proposing a final comment period (FCP).
If you're not on the relevant team (and thus don't have @rfcbot permissions),
ask someone who is to start one;
unless they have a concern themselves, they should.

The FCP process is only needed if you need consensus –
if no processes require consensus for your change
and you don't think anyone would have a problem with it, it's OK to rely on only an r+.
For example,
it is OK to add or modify unstable command-line flags
or attributes in the reserved compiler-internal `rustc_` namespace
without an FCP for compiler development or standard library use,
as long as you don't expect them to be in wide use in the nightly ecosystem.
Some teams have lighter weight processes that they use in scenarios like this;
for example,
the compiler team recommends filing a Major Change Proposal ([MCP])
as a lightweight way to garner support and feedback without requiring full consensus.

[MCP]: https://forge.rust-lang.org/compiler/proposals-and-stabilization.html#how-do-i-submit-an-mcp

You don't need to have the implementation fully ready for r+ to propose an FCP,
but it is generally a good idea to have at least a proof of concept
so that people can see what you are talking about.

When an FCP is proposed, it requires all members of the team to sign off on the FCP.
After they all do so,
there's a 10-day-long "final comment period" (hence the name) where everybody can comment,
and if no concerns are raised, the PR/issue gets FCP approval.

## The logistics of writing features

There are a few "logistical" hoops you might need to go through
in order to implement a feature in a working way.

### Warning Cycles

In some cases, a feature or bugfix might break some existing programs in some edge cases.
In that case,
you'll want to do a crater run to assess the impact and possibly add a future-compatibility lint,
similar to those used for [edition-gated lints](diagnostics.md#edition-gated-lints).

### Stability

We [value the stability of Rust].
Code that works and runs on stable should (mostly) not break.
Because of that,
we don't want to release a feature to the world with only team consensus and code review -
we want to gain real-world experience on using that feature on nightly,
and we might want to change the feature based on that experience.

To allow for that,
we must make sure users don't accidentally depend on that new feature -
otherwise,
especially if experimentation takes time or is delayed and the feature takes the trains to stable,
it would end up de facto stable
and we'll not be able to make changes in it without breaking people's code.

The way we do that is that we make sure all new features are feature gated -
they can't be used without enabling a feature gate (`#[feature(foo)]`),
which can't be done in a stable/beta compiler.
See the [stability in code] section for the technical details.

Eventually, after we gain enough experience using the feature, make the necessary changes,
and are satisfied, we expose it to the world using the stabilization process described [here].
Until then, the feature is not set in stone:
every part of the feature can be changed, or the feature might be completely rewritten or removed.
Features do not gain tenure by being unstable and unchanged for long periods of time.

###  Tracking Issues

To keep track of the status of an unstable feature,
the experience we get while using it on nightly,
and of the concerns that block its stabilization,
every feature-gate needs a tracking issue.
When creating issues and PRs related to the feature, reference this tracking issue,
and when there are updates about the feature's progress, post those to the tracking issue.

For features that are part of an accept RFC or approved lang experiment,
use the tracking issue for that.

For other features, create a tracking issue for that feature.
The issue title should be "Tracking issue for YOUR FEATURE".
Use the ["Tracking Issue" issue template][template].

[template]: https://github.com/rust-lang/rust/issues/new?template=tracking_issue.md

### Lang experiments

To land in the compiler,
features that have user-visible effects on the language (even unstable ones)
must either be part of an accepted RFC or an approved [lang experiment].

To propose a new lang experiment,
open an issue in `rust-lang/rust` that describes the motivation and the intended solution.
If it's accepted, this issue will become the tracking issue for the experiment,
so use the tracking issue [template] while also including these other details.
Nominate the issue for the lang team and CC `@rust-lang/lang` and `@rust-lang/lang-advisors`.
When the experiment is approved, the tracking issue will be marked as `B-experimental`.

Feature flags related to a lang experiment must be marked as `incomplete`
until an RFC is accepted for the feature.

[lang experiment]: https://lang-team.rust-lang.org/how_to/experiment.html

##  Stability in code

The below steps needs to be followed in order to implement a new unstable feature:

1. Open or identify the [tracking issue].
   For features that are part of an accept RFC or approved lang experiment,
   use the tracking issue for that.

   Label the tracking issue with `C-tracking-issue` and the relevant `F-feature_name` label
   (adding that label if needed).

1. Pick a name for the feature gate (for RFCs, use the name in the RFC).

1. Add the feature name to `rustc_span/src/symbol.rs` in the `Symbols {...}` block.

   Note that this block must be in alphabetical order.

1. Add a feature gate declaration to `rustc_feature/src/unstable.rs`
   in the unstable `declare_features` block.

   ```rust ignore
   /// description of feature
   (unstable, $feature_name, "CURRENT_RUSTC_VERSION", Some($tracking_issue_number))
   ```

   If you haven't yet opened a tracking issue
   (e.g. because you want initial feedback on whether the feature is likely to be accepted),
   you can temporarily use `None` - but make sure to update it before the PR is merged!

   For example:

   ```rust ignore
   /// Allows defining identifiers beyond ASCII.
   (unstable, non_ascii_idents, "CURRENT_RUSTC_VERSION", Some(55467)),
   ```

   Features can be marked as incomplete,
   and trigger the warn-by-default [`incomplete_features` lint]
   by setting their type to `incomplete`:

   [`incomplete_features` lint]: https://doc.rust-lang.org/rustc/lints/listing/warn-by-default.html#incomplete-features

   ```rust ignore
   /// Allows deref patterns.
   (incomplete, deref_patterns, "CURRENT_RUSTC_VERSION", Some(87121)),
   ```

   Feature flags related to a lang experiment must be marked as `incomplete`
   until an RFC is accepted for the feature.

   To avoid [semantic merge conflicts],
   use `CURRENT_RUSTC_VERSION` instead of `1.70` or another explicit version number.

   [semantic merge conflicts]: https://bors.tech/essay/2017/02/02/pitch/

1. Prevent usage of the new feature unless the feature gate is set.
   You can check it in most places in the compiler
   using the expression `tcx.features().$feature_name()`.

    If the feature gate is not set,
    you should either maintain the pre-feature behavior or raise an error,
    depending on what makes sense.
    Errors should generally use [`rustc_session::parse::feature_err`].
    For an example of adding an error, see [#81015].

   For features introducing new syntax, pre-expansion gating should be used instead.
   During parsing, when the new syntax is parsed,
   the symbol must be inserted to the current crate's [`GatedSpans`]
   via `self.sess.gated_span.gate(sym::my_feature, span)`.

   After being inserted to the gated spans,
   the span must be checked in the [`rustc_ast_passes::feature_gate::check_crate`] function,
   which actually denies features.
   Exactly how it is gated depends on the exact type of feature,
   but most likely will use the `gate_all!()` macro.

1. Add a test to ensure the feature cannot be used without a feature gate,
   by creating `tests/ui/feature-gates/feature-gate-$feature_name.rs`.
   You can generate the corresponding `.stderr` file
   by running `./x test tests/ui/feature-gates/ --bless`.

1. Add a section to the unstable book,
   in `src/doc/unstable-book/src/language-features/$feature_name.md`.

1. Write a lot of tests for the new feature, preferably in `tests/ui/$feature_name/`.
   PRs without tests will not be accepted!

1. Get your PR reviewed and land it.
   You have now successfully implemented a feature in Rust!

[`GatedSpans`]: https://doc.rust-lang.org/nightly/nightly-rustc/rustc_session/parse/struct.GatedSpans.html
[#81015]: https://github.com/rust-lang/rust/pull/81015
[`rustc_session::parse::feature_err`]: https://doc.rust-lang.org/nightly/nightly-rustc/rustc_session/parse/fn.feature_err.html
[`rustc_ast_passes::feature_gate::check_crate`]: https://doc.rust-lang.org/nightly/nightly-rustc/rustc_ast_passes/feature_gate/fn.check_crate.html
[value the stability of Rust]: https://github.com/rust-lang/rfcs/blob/master/text/1122-language-semver.md
[stability in code]: #stability-in-code
[here]: ./stabilization-guide.md
[tracking issue]: #tracking-issues
[add-feature-gate]: ./feature-gates.md#adding-a-feature-gate

## Call for testing

Once the implementation is complete,
the feature will be available to nightly users but not yet part of stable Rust.
This is a good time to write a blog post on [the main Rust blog][rust-blog]
and issue a "call for testing".

Some earlier such blog posts include:

1. [The push for GATs stabilization](https://blog.rust-lang.org/2021/08/03/GATs-stabilization-push/)
2. [Changes to `impl Trait` in Rust 2024](https://blog.rust-lang.org/2024/09/05/impl-trait-capture-rules.html)
3. [Async Closures MVP: Call for Testing!](https://blog.rust-lang.org/inside-rust/2024/08/09/async-closures-call-for-testing/)

Alternatively, [*This Week in Rust*][twir] has a [section][twir-cft] for this.
One example of this having been used is:

- [Call for testing on boolean literals as cfg predicates](https://github.com/rust-lang/rust/issues/131204#issuecomment-2569314526)

Which option to choose might depend on how significant the language change is,
though note that the [*This Week in Rust*][twir] section might be less visible
than a dedicated post on the main Rust blog.

## Polishing

Giving users a polished experience means more than just implementing the feature in rustc.
We need to think about all of the tools and resources that we ship.
This work includes:

- Documenting the language feature in the [Rust Reference][reference].
- Extending [`rustfmt`] to format any new syntax (if applicable).
- Extending [`rust-analyzer`] (if applicable).
  The extent of this work can depend on the nature of the language feature,
  as some features don't need to be blocked on *full* support.
   - When a language feature degrades the user experience
     simply by existing before support is implemented in [`rust-analyzer`],
     that may lead the lang team to raise a blocking concern.
   - Examples of such might include new syntax that [`rust-analyzer`] can't parse
     or type inference changes it doesn't understand when those lead to bogus diagnostics.

## Stabilization

The final step in the feature lifecycle is [stabilization][stab],
which is when the feature becomes available to all Rust users.
At this point,
backward incompatible changes are generally no longer permitted
(see the lang team's [defined semver policies](https://rust-lang.github.io/rfcs/1122-language-semver.html) for details).
To learn more about stabilization, see the [stabilization guide][stab].


[stab]: ./stabilization-guide.md
[rust-blog]: https://github.com/rust-lang/blog.rust-lang.org/
[twir]: https://github.com/rust-lang/this-week-in-rust
[twir-cft]: https://this-week-in-rust.org/blog/2025/01/22/this-week-in-rust-583/#calls-for-testing
[`rustfmt`]: https://github.com/rust-lang/rustfmt
[`rust-analyzer`]: https://github.com/rust-lang/rust-analyzer
[reference]: https://github.com/rust-lang/reference


---

# Stability guarantees

This page gives an overview of our stability guarantees.

## RFCs

* [RFC 1105 api evolution](https://github.com/rust-lang/rfcs/blob/master/text/1105-api-evolution.md)
* [RFC 1122 language semver](https://github.com/rust-lang/rfcs/blob/master/text/1122-language-semver.md)

## Blog posts

* [Stability as a Deliverable](https://blog.rust-lang.org/2014/10/30/Stability/)

## rustc-dev-guide links

* [Stabilizing library features](./stability.md)
* [Stabilizing language features](./stabilization-guide.md)
* [What qualifies as a bug fix?](./bug-fix-procedure.md#what-qualifies-as-a-bug-fix)

## Exemptions

Even if some of our infrastructure can be used by others, it is still considered
internal and comes without stability guarantees. This is a non-exhaustive list
of components without stability guarantees:

* The CLIs and environment variables used by `remote-test-client` / `remote-test-server`


---

# Stability attributes

This section is about the stability attributes and schemes that allow stable
APIs to use unstable APIs internally in the rustc standard library.

**NOTE**: this section is for *library* features, not *language* features. For instructions on
stabilizing a language feature see [Stabilizing Features](./stabilization-guide.md).

## unstable

The `#[unstable(feature = "foo", issue = "1234", reason = "lorem ipsum")]`
attribute explicitly marks an item as unstable. Items that are marked as
"unstable" cannot be used without a corresponding `#![feature]` attribute on
the crate, even on a nightly compiler. This restriction only applies across
crate boundaries, unstable items may be used within the crate that defines
them.

The `issue` field specifies the associated GitHub [issue number]. This field is
required and all unstable features should have an associated tracking issue. In
rare cases where there is no sensible value `issue = "none"` is used.

The `unstable` attribute infects all sub-items, where the attribute doesn't
have to be reapplied. So if you apply this to a module, all items in the module
will be unstable.

If you rename a feature, you can add `old_name = "old_name"` to produce a 
useful error message.

You can make specific sub-items stable by using the `#[stable]` attribute on
them. The stability scheme works similarly to how `pub` works. You can have
public functions of nonpublic modules and you can have stable functions in
unstable modules or vice versa.

Previously, due to a [rustc bug], stable items inside unstable modules were
available to stable code in that location.
As of <!-- date-check --> September 2024, items with [accidentally stabilized
paths] are marked with the `#[rustc_allowed_through_unstable_modules]` attribute
to prevent code dependent on those paths from breaking. Do *not* add this attribute
to any more items unless that is needed to avoid breaking changes.

The `unstable` attribute may also have the `soft` value, which makes it a
future-incompatible deny-by-default lint instead of a hard error. This is used
by the `bench` attribute which was accidentally accepted in the past. This
prevents breaking dependencies by leveraging Cargo's lint capping.

[issue number]: https://github.com/rust-lang/rust/issues
[rustc bug]: https://github.com/rust-lang/rust/issues/15702
[accidentally stabilized paths]: https://github.com/rust-lang/rust/issues/113387

## stable
The `#[stable(feature = "foo", since = "1.420.69")]` attribute explicitly
marks an item as stabilized. Note that stable functions may use unstable things in their body.

## rustc_const_unstable

The `#[rustc_const_unstable(feature = "foo", issue = "1234", reason = "lorem
ipsum")]` has the same interface as the `unstable` attribute. It is used to mark
`const fn` as having their constness be unstable. This is only needed in rare cases:
- If a `const fn` makes use of unstable language features or intrinsics.
  (The compiler will tell you to add the attribute if you run into this.)
- If a `const fn` is `#[stable]` but not yet intended to be const-stable.
- To change the feature gate that is required to call a const-unstable intrinsic.

Const-stability differs from regular stability in that it is *recursive*: a
`#[rustc_const_unstable(...)]` function cannot even be indirectly called from stable code. This is
to avoid accidentally leaking unstable compiler implementation artifacts to stable code or locking
us into the accidental quirks of an incomplete implementation. See the rustc_const_stable_indirect
and rustc_allow_const_fn_unstable attributes below for how to fine-tune this check.

## rustc_const_stable

The `#[rustc_const_stable(feature = "foo", since = "1.420.69")]` attribute explicitly marks
a `const fn` as having its constness be `stable`.

## rustc_const_stable_indirect

The `#[rustc_const_stable_indirect]` attribute can be added to a `#[rustc_const_unstable(...)]`
function to make it callable from `#[rustc_const_stable(...)]` functions. This indicates that the
function is ready for stable in terms of its implementation (i.e., it doesn't use any unstable
compiler features); the only reason it is not const-stable yet are API concerns.

This should also be added to lang items for which const-calls are synthesized in the compiler, to
ensure those calls do not bypass recursive const stability rules.

## rustc_intrinsic_const_stable_indirect

On an intrinsic, this attribute marks the intrinsic as "ready to be used by public stable functions".
If the intrinsic has a `rustc_const_unstable` attribute, it should be removed.
**Adding this attribute to an intrinsic requires t-lang and wg-const-eval approval!**

## rustc_default_body_unstable

The `#[rustc_default_body_unstable(feature = "foo", issue = "1234", reason =
"lorem ipsum")]` attribute has the same interface as the `unstable` attribute.
It is used to mark the default implementation for an item within a trait as
unstable.
A trait with a default-body-unstable item can be implemented stably by providing
an explicit body for any such item, or the default body can be used by enabling
its corresponding `#![feature]`.

## Stabilizing a library feature

To stabilize a feature, follow these steps:

1. Ask a **@T-libs-api** member to start an FCP on the tracking issue and wait for
   the FCP to complete (with `disposition-merge`).
2. Change `#[unstable(...)]` to `#[stable(since = "CURRENT_RUSTC_VERSION")]`.
3. Remove `#![feature(...)]` from any test or doc-test for this API. If the feature is used in the
   compiler or tools, remove it from there as well.
4. If this is a `const fn`, add `#[rustc_const_stable(since = "CURRENT_RUSTC_VERSION")]`.
   Alternatively, if this is not supposed to be const-stabilized yet,
   add `#[rustc_const_unstable(...)]` for some new feature gate (with a new tracking issue).
5. Open a PR against `rust-lang/rust`.
   - Add the appropriate labels: `@rustbot modify labels: +T-libs-api`.
   - Link to the tracking issue and say "Closes #XXXXX".

You can see an example of stabilizing a feature with
[tracking issue #81656 with FCP](https://github.com/rust-lang/rust/issues/81656)
and the associated
[implementation PR #84642](https://github.com/rust-lang/rust/pull/84642).

## allow_internal_unstable

Macros and compiler desugarings expose their bodies to the call
site. To work around not being able to use unstable things in the standard
library's macros, there's the `#[allow_internal_unstable(feature1, feature2)]`
attribute that allows the given features to be used in stable macros.

Note that if a macro is used in const context and generates a call to a
`#[rustc_const_unstable(...)]` function, that will *still* be rejected even with
`allow_internal_unstable`. Add `#[rustc_const_stable_indirect]` to the function to ensure the macro
cannot accidentally bypass the recursive const stability checks.

## rustc_allow_const_fn_unstable

As explained above, no unstable const features are allowed inside stable `const fn`, not even
indirectly.

However, sometimes we do know that a feature will get stabilized, just not when, or there is a
stable (but e.g. runtime-slow) workaround, so we could always fall back to some stable version if we
scrapped the unstable feature. In those cases, the `[rustc_allow_const_fn_unstable(feature1,
feature2)]` attribute can be used to allow some unstable features in the body of a stable (or
indirectly stable) `const fn`.

You also need to take care to uphold the `const fn` invariant that calling it at runtime and
compile-time needs to behave the same (see also [this blog post][blog]). This means that you
may not create a `const fn` that e.g. transmutes a memory address to an integer,
because the addresses of things are nondeterministic and often unknown at
compile-time.

**Always ping @rust-lang/wg-const-eval if you are adding more
`rustc_allow_const_fn_unstable` attributes to any `const fn`.**

## staged_api

Any crate that uses the `stable` or `unstable` attributes must include the
`#![feature(staged_api)]` attribute on the crate.

## deprecated

Deprecations in the standard library are nearly identical to deprecations in
user code. When `#[deprecated]` is used on an item, it must also have a `stable`
or `unstable `attribute.

`deprecated` has the following form:

```rust,ignore
#[deprecated(
    since = "1.38.0",
    note = "explanation for deprecation",
    suggestion = "other_function"
)]
```

The `suggestion` field is optional. If given, it should be a string that can be
used as a machine-applicable suggestion to correct the warning. This is
typically used when the identifier is renamed, but no other significant changes
are necessary. When the `suggestion` field is used, you need to have
`#![feature(deprecated_suggestion)]` at the crate root.

Another difference from user code is that the `since` field is actually checked
against the current version of `rustc`. If `since` is in a future version, then
the `deprecated_in_future` lint is triggered which is default `allow`, but most
of the standard library raises it to a warning with
`#![warn(deprecated_in_future)]`.

## unstable_feature_bound
The `#[unstable_feature_bound(foo)]` attribute can be used together with `#[unstable]` attribute to mark an `impl` of stable type and stable trait as unstable. In std/core, an item annotated with `#[unstable_feature_bound(foo)]` can only be used by another item that is also annotated with `#[unstable_feature_bound(foo)]`. Outside of std/core, using an item with `#[unstable_feature_bound(foo)]` requires the feature to be enabled with `#![feature(foo)]` attribute on the crate.

Currently, the items that can be annotated with `#[unstable_feature_bound]` are:
- `impl`
- free function
- trait

## renamed and removed features
Unstable features can get renamed and removed. If you rename a feature, you can add `old_name = "old_name"` to the `#[unstable]` attribute.
If you remove a feature, the `#!unstable_removed(feature = "foo", reason = "brief description", link = "link", since = "1.90.0")`
attribute should be used to produce a good error message for users of the removed feature.

The `link` field can be used to link to the most relevant information on the removal of the feature such as a GitHub issue, comment or PR.

[blog]: https://www.ralfj.de/blog/2018/07/19/const.html


---

# Request for stabilization

**NOTE**: This page is about stabilizing *language* features.
For stabilizing *library* features, see [Stabilizing a library feature].

[Stabilizing a library feature]: ./stability.md#stabilizing-a-library-feature

Once an unstable feature has been well-tested with no outstanding concerns, anyone may push for its stabilization, though involving the people who have worked on it is prudent.
Follow these steps:

## Write an RFC, if needed

If the feature was part of a [lang experiment], the lang team generally will want to first accept an RFC before stabilization.

[lang experiment]: https://lang-team.rust-lang.org/how_to/experiment.html

## Documentation PRs

<a id="updating-documentation"></a>

The feature might be documented in the [`Unstable Book`], located at [`src/doc/unstable-book`].
Remove the page for the feature gate if it exists.
Integrate any useful parts of that documentation in other places.

Places that may need updated documentation include:

- [The Reference]: This must be updated, in full detail, and a member of the lang-docs team must review and approve the PR before the stabilization can be merged.
- [The Book]: This is updated as needed.
  If you're not sure, please open an issue on this repository and it can be discussed.
- Standard library documentation: This is updated as needed.
  Language features often don't need this, but if it's a feature that changes how idiomatic examples are written, such as when `?` was added to the language, updating these in the library documentation is important.
  Review also the keyword documentation and ABI documentation in the standard library, as these sometimes need updates for language changes.
- [Rust by Example]: This is updated as needed.

Prepare PRs to update documentation involving this new feature for the repositories mentioned above.
Maintainers of these repositories will keep these PRs open until the whole stabilization process has completed.
Meanwhile, we can proceed to the next step.

## Write a stabilization report

Author a stabilization report using the [template found in this repository][srt].

The stabilization reports summarizes:

- The main design decisions and deviations since the RFC was accepted, including both decisions that were FCP'd or otherwise accepted by the language team as well as those being presented to the lang team for the first time.
    - Often, the final stabilized language feature has significant design deviations from the original RFC.
      That's OK, but these deviations must be highlighted and explained carefully.
- The work that has been done since the RFC was accepted, acknowledging the main contributors that helped drive the language feature forward.

The [*Stabilization Template*][srt] includes a series of questions that aim to surface connections between this feature and lang's subteams (e.g. types, opsem, lang-docs, etc.) and to identify items that are commonly overlooked.

[srt]: ./stabilization-report-template.md

The stabilization report is typically posted as the main comment on the stabilization PR (see the next section).

## Stabilization PR

Every feature is different, and some may require steps beyond what this guide discusses.

Before the stabilization will be considered by the lang team, there must be a complete PR to the Reference describing the feature, and before the stabilization PR will be merged, this PR must have been reviewed and approved by the lang-docs team.

### Updating the feature-gate listing

There is a central listing of unstable feature-gates in [`compiler/rustc_feature/src/unstable.rs`].
Search for the `declare_features!`  macro.
There should be an entry for the feature you are aiming to stabilize,
something like the following (taken from [rust-lang/rust#32409]):

```rust,ignore
// pub(restricted) visibilities (RFC 1422)
(unstable, pub_restricted, "CURRENT_RUSTC_VERSION", Some(32409)),
```

The above line should be moved to [`compiler/rustc_feature/src/accepted.rs`].
Entries in the `declare_features!` call are sorted, so find the correct place.
When it is done, it should look like:

```rust,ignore
// pub(restricted) visibilities (RFC 1422)
(accepted, pub_restricted, "CURRENT_RUSTC_VERSION", Some(32409)),
// note that we changed this
```

(Even though you will encounter version numbers in the file of past changes, you should not put the rustc version you expect your stabilization to happen in, but instead use `CURRENT_RUSTC_VERSION`.)

### Removing existing uses of the feature-gate

Next, search for the feature string (in this case, `pub_restricted`) in the codebase to find where it appears.
Change uses of `#![feature(XXX)]` from the `std` and any rustc crates
(which includes test folders under `library/` and `compiler/` but not the toplevel `tests/` one)
to be `#![cfg_attr(bootstrap, feature(XXX))]`.
This includes the feature-gate only for stage0, which is built using the current beta (this is needed because the feature is still unstable in the current beta).

Also, remove those strings from any tests (e.g. under `tests/`). If there are tests specifically targeting the feature-gate (i.e., testing that the feature-gate is required to use the feature, but nothing else), simply remove the test.

### Do not require the feature-gate to use the feature

Most importantly, remove the code which flags an error if the feature-gate is not present (since the feature is now considered stable).
If the feature can be detected because it employs some new syntax, then a common place for that code to be is in `compiler/rustc_ast_passes/src/feature_gate.rs`.
For example, you might see code like this:

```rust,ignore
gate_all!(pub_restricted, "`pub(restricted)` syntax is experimental");
```

The `gate_all!` macro reports an error if the `pub_restricted` feature is not enabled.
It is not needed now that `pub(restricted)` is stable.

For more subtle features, you may find code like this:

```rust,ignore
if self.tcx.features().async_fn_in_dyn_trait() { /* XXX */ }
```

This `pub_restricted` field (named after the feature) would ordinarily be false if the feature flag is not present and true if it is.
So, transform the code to assume that the field is true.
In this case, that would mean removing the `if` and leaving just the `/* XXX */`.

```rust,ignore
if self.tcx.sess.features.borrow().pub_restricted { /* XXX */ }
becomes
/* XXX */

if self.tcx.sess.features.borrow().pub_restricted && something { /* XXX */ }
 becomes
if something { /* XXX */ }
```

[rust-lang/rust#32409]: https://github.com/rust-lang/rust/issues/32409
[std-guide-stabilization]: https://std-dev-guide.rust-lang.org/feature-lifecycle/stabilization.html
[src-version]: https://github.com/rust-lang/rust/blob/HEAD/src/version
[forge-versions]: https://forge.rust-lang.org/#current-release-versions
[forge-release-process]: https://forge.rust-lang.org/release/process.html
[`compiler/rustc_feature`]: https://doc.rust-lang.org/nightly/nightly-rustc/rustc_feature/index.html
[`compiler/rustc_feature/src/accepted.rs`]: https://github.com/rust-lang/rust/tree/HEAD/compiler/rustc_feature/src/accepted.rs
[`compiler/rustc_feature/src/unstable.rs`]: https://github.com/rust-lang/rust/tree/HEAD/compiler/rustc_feature/src/unstable.rs
[The Reference]: https://github.com/rust-lang/reference
[The Book]: https://github.com/rust-lang/book
[Rust by Example]: https://github.com/rust-lang/rust-by-example
[`Unstable Book`]: https://doc.rust-lang.org/unstable-book/index.html
[`src/doc/unstable-book`]: https://github.com/rust-lang/rust/tree/HEAD/src/doc/unstable-book

## Team nominations

When opening the stabilization PR, CC the lang team and its advisors (`@rust-lang/lang @rust-lang/lang-advisors`) and any other teams to whom the feature is relevant, e.g.:

- `@rust-lang/types`, for type system interactions.
- `@rust-lang/opsem`, for interactions with unsafe code.
- `@rust-lang/compiler`, for implementation robustness.
- `@rust-lang/libs-api`, for changes to the standard library API or its guarantees.
- `@rust-lang/lang-docs`, for questions about how this should be documented in the Reference.

After the stabilization PR is opened with the stabilization report, wait a bit for any immediate comments.
When such comments "simmer down" and you feel the PR is ready for consideration by the lang team, [nominate the PR](https://lang-team.rust-lang.org/how_to/nominate.html) to get it on the agenda for consideration in an upcoming lang meeting.

If you are not a `rust-lang` organization member, you can ask your assigned reviewer to CC the relevant teams on your behalf.

## Propose FCP on the PR

After the lang team and other relevant teams review the stabilization, and after you have answered any questions they may have had, a member of one of the teams may propose to accept the stabilization by commenting:

```text
@rfcbot fcp merge
```

Once enough team members have reviewed, the PR will move into a "final comment period" (FCP).
If no new concerns are raised, this period will complete and the PR can be merged after implementation review in the usual way.

## Reviewing and merging stabilizations

On a stabilization, before giving it the `r+`, ensure that the PR:

- Matches what the team proposed for stabilization and what is documented in the Reference PR.
- Includes any changes the team decided to request along the way in order to resolve or avoid concerns.
- Is otherwise exactly what is described in the stabilization report and in any relevant RFCs or prior lang FCPs.
- Does not expose on stable behaviors other than those specified, accepted for stabilization, and documented in the Reference.
- Has sufficient tests to convincingly demonstrate these things.
- Is accompanied by a PR to the Reference than has been reviewed and approved by a member of lang-docs.

In particular, when reviewing the PR, keep an eye out for any user-visible details that the lang team failed to consider and specify.
If you find one, describe it and nominate the PR for the lang team.


---

# Stabilization report template

## What is this?

This is a template for [stabilization reports](./stabilization-guide.md) of **language features**. The questions aim to solicit the details most often needed. These details help reviewers to identify potential problems upfront. Not all parts of the template will apply to every stabilization. If a question doesn't apply, explain briefly why.

Copy everything after the separator and edit it as Markdown. Replace each *TODO* with your answer.

---

# Stabilization report

## Summary

> Remind us what this feature is and what value it provides. Tell the story of what led up to this stabilization.
>
> E.g., see:
>
> - [Stabilize AFIT/RPITIT](https://web.archive.org/web/20250329190642/https://github.com/rust-lang/rust/pull/115822)
> - [Stabilize RTN](https://web.archive.org/web/20250321214601/https://github.com/rust-lang/rust/pull/138424)
> - [Stabilize ATPIT](https://web.archive.org/web/20250124214256/https://github.com/rust-lang/rust/pull/120700)
> - [Stabilize opaque type precise capturing](https://web.archive.org/web/20250312173538/https://github.com/rust-lang/rust/pull/127672)

*TODO*

Tracking:

- *TODO* (Link to tracking issue.)

Reference PRs:

- *TODO* (Link to Reference PRs.)

cc @rust-lang/lang @rust-lang/lang-advisors

### What is stabilized

> Describe each behavior being stabilized and give a short example of code that will now be accepted.

```rust
todo!()
```

### What isn't stabilized

> Describe any parts of the feature not being stabilized. Talk about what we might want to do later and what doors are being left open for that. If what we're not stabilizing might lead to surprises for users, talk about that in particular.

## Design

### Reference

> What updates are needed to the Reference? Link to each PR. If the Reference is missing content needed for describing this feature, discuss that.

- *TODO*

### RFC history

> What RFCs have been accepted for this feature?

- *TODO*

### Answers to unresolved questions

> What questions were left unresolved by the RFC? How have they been answered? Link to any relevant lang decisions.

*TODO*

### Post-RFC changes

> What other user-visible changes have occurred since the RFC was accepted? Describe both changes that the lang team accepted (and link to those decisions) as well as changes that are being presented to the team for the first time in this stabilization report.

*TODO*

### Key points

> What decisions have been most difficult and what behaviors to be stabilized have proved most contentious? Summarize the major arguments on all sides and link to earlier documents and discussions.

*TODO*

### Nightly extensions

> Are there extensions to this feature that remain unstable? How do we know that we are not accidentally committing to those?

*TODO*

### Doors closed

> What doors does this stabilization close for later changes to the language? E.g., does this stabilization make any other RFCs, lang experiments, or known in-flight proposals more difficult or impossible to do later?

## Feedback

### Call for testing

> Has a "call for testing" been done? If so, what feedback was received?

*TODO*

### Nightly use

> Do any known nightly users use this feature? Counting instances of `#![feature(FEATURE_NAME)]` on GitHub with grep might be informative.

*TODO*

## Implementation

### Major parts

> Summarize the major parts of the implementation and provide links into the code and to relevant PRs.
>
> See, e.g., this breakdown of the major parts of async closures:
>
> - <https://rustc-dev-guide.rust-lang.org/coroutine-closures.html>

*TODO*

### Coverage

> Summarize the test coverage of this feature.
>
> Consider what the "edges" of this feature are. We're particularly interested in seeing tests that assure us about exactly what nearby things we're not stabilizing. Tests should of course comprehensively demonstrate that the feature works. Think too about demonstrating the diagnostics seen when common mistakes are made and the feature is used incorrectly.
>
> Within each test, include a comment at the top describing the purpose of the test and what set of invariants it intends to demonstrate. This is a great help to our review.
>
> Describe any known or intentional gaps in test coverage.
>
> Contextualize and link to test folders and individual tests.

*TODO*

### Outstanding bugs

> What outstanding bugs involve this feature? List them. Should any block the stabilization? Discuss why or why not.

*TODO*

- *TODO*
- *TODO*
- *TODO*

### Outstanding FIXMEs

> What FIXMEs are still in the code for that feature and why is it OK to leave them there?

*TODO*

### Tool changes

> What changes must be made to our other tools to support this feature. Has this work been done? Link to any relevant PRs and issues.

- [ ] rustfmt
  - *TODO*
- [ ] rust-analyzer
  - *TODO*
- [ ] rustdoc (both JSON and HTML)
  - *TODO*
- [ ] cargo
  - *TODO*
- [ ] clippy
  - *TODO*
- [ ] rustup
  - *TODO*
- [ ] docs.rs
  - *TODO*

*TODO*

### Breaking changes

> If this stabilization represents a known breaking change, link to the crater report, the analysis of the crater report, and to all PRs we've made to ecosystem projects affected by this breakage. Discuss any limitations of what we're able to know about or to fix.

*TODO*

Crater report:

- *TODO*

Crater analysis:

- *TODO*

PRs to affected crates:

- *TODO*
- *TODO*
- *TODO*

## Type system, opsem

### Compile-time checks

> What compilation-time checks are done that are needed to prevent undefined behavior?
>
> Link to tests demonstrating that these checks are being done.

*TODO*

- *TODO*
- *TODO*
- *TODO*

### Type system rules

> What type system rules are enforced for this feature and what is the purpose of each?

*TODO*

### Sound by default?

> Does the feature's implementation need specific checks to prevent UB, or is it sound by default and need specific opt-in to perform the dangerous/unsafe operations? If it is not sound by default, what is the rationale?

*TODO*

### Breaks the AM?

> Can users use this feature to introduce undefined behavior, or use this feature to break the abstraction of Rust and expose the underlying assembly-level implementation? Describe this if so.

*TODO*

## Common interactions

### Temporaries

> Does this feature introduce new expressions that can produce temporaries? What are the scopes of those temporaries?

*TODO*

### Drop order

> Does this feature raise questions about the order in which we should drop values? Talk about the decisions made here and how they're consistent with our earlier decisions.

*TODO*

### Pre-expansion / post-expansion

> Does this feature raise questions about what should be accepted pre-expansion (e.g. in code covered by `#[cfg(false)]`) versus what should be accepted post-expansion? What decisions were made about this?

*TODO*

### Edition hygiene

> If this feature is gated on an edition, how do we decide, in the context of the edition hygiene of tokens, whether to accept or reject code. E.g., what token do we use to decide?

*TODO*

### SemVer implications

> Does this feature create any new ways in which library authors must take care to prevent breaking downstreams when making minor-version releases? Describe these. Are these new hazards "major" or "minor" according to [RFC 1105](https://rust-lang.github.io/rfcs/1105-api-evolution.html)?

*TODO*

### Exposing other features

> Are there any other unstable features whose behavior may be exposed by this feature in any way? What features present the highest risk of that?

*TODO*

## History

> List issues and PRs that are important for understanding how we got here.

- *TODO*
- *TODO*
- *TODO*

## Acknowledgments

> Summarize contributors to the feature by name for recognition and so that those people are notified about the stabilization. Does anyone who worked on this *not* think it should be stabilized right now? We'd like to hear about that if so.

*TODO*

## Open items

> List any known items that have not yet been completed and that should be before this is stabilized.

- [ ] *TODO*
- [ ] *TODO*
- [ ] *TODO*


---

# Feature gates

This chapter is intended to provide basic help for adding, removing, and modifying feature gates.

For how rustc enforces and checks feature gates in the compiler pipeline,
see [Feature Gate Checking][feature-gate-check].

Note that this is specific to *language* feature gates; *library* feature gates use [a different
mechanism][libs-gate].

[feature-gate-check]: ./feature-gate-check.md
[libs-gate]: ./stability.md

## Adding a feature gate

See ["Stability in code"][adding] in the "Implementing new features" section for instructions.

[adding]: ./implementing-new-features.md#stability-in-code

## Removing a feature gate

[removing]: #removing-a-feature-gate

To remove a feature gate, follow these steps:

1. Remove the feature gate declaration in `rustc_feature/src/unstable.rs`.
   It will look like this:

   ```rust,ignore
   /// description of feature
   (unstable, $feature_name, "$version", Some($tracking_issue_number))
   ```

2. Add a modified version of the feature gate declaration that you just
   removed to `rustc_feature/src/removed.rs`:

   ```rust,ignore
   /// description of feature
   (removed, $old_feature_name, "$version", Some($tracking_issue_number),
    Some("$why_it_was_removed"))
   ```


## Renaming a feature gate

[renaming]: #renaming-a-feature-gate

To rename a feature gate, follow these steps (the first two are the same steps
to follow when [removing a feature gate][removing]):

1. Remove the old feature gate declaration in `rustc_feature/src/unstable.rs`.
   It will look like this:

   ```rust,ignore
   /// description of feature
   (unstable, $old_feature_name, "$version", Some($tracking_issue_number))
   ```

2. Add a modified version of the old feature gate declaration that you just
   removed to `rustc_feature/src/removed.rs`:

   ```rust,ignore
   /// description of feature
   /// Renamed to `$new_feature_name`
   (removed, $old_feature_name, "$version", Some($tracking_issue_number),
    Some("renamed to `$new_feature_name`"))
   ```

3. Add a feature gate declaration with the new name to `rustc_feature/src/unstable.rs`.
   It should look very similar to the old declaration:

   ```rust,ignore
   /// description of feature
   (unstable, $new_feature_name, "$version", Some($tracking_issue_number))
   ```


## Stabilizing a feature

See ["Updating the feature-gate listing"] in the "Stabilizing Features" chapter for instructions.
There are additional steps you will need to take beyond just updating the declaration!


["Stability in code"]: ./implementing-new-features.md#stability-in-code
["Updating the feature-gate listing"]: ./stabilization-guide.md#updating-the-feature-gate-listing
