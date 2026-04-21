# Coding conventions

This chapter covers [formatting](#formatting), [coding for correctness](#cc),
[using crates from crates.io](#cio), and some tips on [structuring your PR for easy review](#er).

<a id="formatting"></a>

## Formatting and the tidy script

rustc is moving towards the [Rust standard coding style][fmt].

However, for now we don't use stable `rustfmt`; we use a pinned version with a
special config, so this may result in different style from normal [`rustfmt`].
Therefore, formatting this repository using `cargo fmt` is not recommended.

Instead, formatting should be done using `./x fmt`.
It's a good habit to run `./x fmt` before every commit, as this reduces conflicts later.

Formatting is checked by the `tidy` script.
It runs automatically when you do `./x test` and can be run in isolation with `./x fmt --check`.

> **Note: Formatting and test suites**
>
> Most Rust source files under `tests/` directory are not formatted for reasons
> such as whitespace sensitivity, nature of snapshot tests, location-sensitive
> comments and more.
>
> Consult the `ignore` entries in
> <https://github.com/rust-lang/rust/blob/main/rustfmt.toml> for which test
> files are not formatted.

If you want to use format-on-save in your editor, the pinned version of
`rustfmt` is built under `build/<target>/stage0/bin/rustfmt`.

[fmt]: https://github.com/rust-dev-tools/fmt-rfcs
[`rustfmt`]:https://github.com/rust-lang/rustfmt

### Formatting C++ code

The compiler contains some C++ code for interfacing with parts of LLVM that
don't have a stable C API.
When modifying that code, use this command to format it:

```console
./x test tidy --extra-checks cpp:fmt --bless
```

This uses a pinned version of `clang-format`, to avoid relying on the local environment.

### Formatting and linting Python code

The Rust repository contains quite a lot of Python code.
We try to keep it both linted and formatted by the [ruff] tool.

When modifying Python code, use this command to format it:

```console
./x test tidy --extra-checks py:fmt --bless
```

And, the following command to run lints:

```console
./x test tidy --extra-checks py:lint
```

These use a pinned version of `ruff`, to avoid relying on the local environment.

[ruff]: https://github.com/astral-sh/ruff

<a id="copyright"></a>

<!-- REUSE-IgnoreStart -->
<!-- Prevent REUSE from interpreting the heading as a copyright notice -->
### Copyright notice
<!-- REUSE-IgnoreEnd -->

In the past, files began with a copyright and license notice.
Please **omit** this notice for new files licensed under the standard terms (MIT OR Apache-2.0).

All of the copyright notices should be gone by now, but if you come across one
in the rust-lang/rust repo, feel free to open a PR to remove it.

### Line length

Lines should be at most 100 characters.
It's even better if you can keep things to 80.

Sometimes, and particularly for tests, it can be necessary to exempt yourself from this limit.
In that case, you can add a comment towards the top of the file like so:

```rust
// ignore-tidy-linelength
```

### Tabs vs spaces

Prefer 4-space indents.

<a id="cc"></a>

## Coding for correctness

Beyond formatting, there are a few other tips that are worth following.

### Prefer exhaustive matches

Using `_` in a match is convenient, but it means that when new
variants are added to the enum, they may not get handled correctly.
Ask yourself: if a new variant were added to this enum, what's the
chance that it would want to use the `_` code, versus having some other treatment?
Unless the answer is "low", then prefer an exhaustive match.

The same advice applies to `if let` and `while let`,
which are effectively tests for a single variant.

### Use "TODO" comments for things you don't want to forget

As a useful tool to yourself, you can insert a `// TODO` comment
for something that you want to get back to before you land your PR:

```rust,ignore
fn do_something() {
    if something_else {
        unimplemented!(); // TODO write this
    }
}
```

The tidy script will report an error for a `// TODO` comment, so this
code would not be able to land until the TODO is fixed (or removed).

This can also be useful in a PR as a way to signal from one commit that you are
leaving a bug that a later commit will fix:

```rust,ignore
if foo {
    return true; // TODO wrong, but will be fixed in a later commit
}
```

If you want to leave a note in the codebase, use `// FIXME` instead.

<a id="cio"></a>

## Using crates from crates.io

See the [crates.io dependencies][crates] section.

<a id="er"></a>

## How to structure your PR

How you prepare the commits in your PR can make a big difference for the reviewer.
Here are some tips.

**Isolate "pure refactorings" into their own commit.** For example, if
you rename a method, then put that rename into its own commit, along
with the renames of all the uses.

**More commits is usually better.** If you are doing a large change,
it's almost always better to break it up into smaller steps that can be independently understood.
The one thing to be aware of is that if
you introduce some code following one strategy, then change it
dramatically (versus adding to it) in a later commit, that 'back-and-forth' can be confusing.

**Format liberally.** While only the final commit of a PR must be correctly
formatted, it is both easier to review and less noisy to format each commit
individually using `./x fmt`.

**No merges.** We do not allow merge commits into our history, other than those by bors.
If you get a merge conflict, rebase instead via a
command like `git rebase --interactive rust-lang/main` (presuming you use the
name `rust-lang` for your remote).

**Individual commits do not have to build (but it's nice).** We do not
require that every intermediate commit successfully builds – we only
expect to be able to bisect at a PR level.
However, if you *can* make individual commits build, that is always helpful.

## Naming conventions

Apart from normal Rust style/naming conventions, there are also some specific to the compiler.

- `cx` tends to be short for "context" and is often used as a suffix.
  For example, `tcx` is a common name for the [Typing Context][tcx].

- [`'tcx`][tcx] is used as the lifetime name for the Typing Context.

- Because `crate` is a keyword, if you need a variable to represent something
  crate-related, often the spelling is changed to `krate`.

[tcx]: ./ty.md

[crates]: ./crates-io.md


---

# Procedures for breaking changes

This page defines the best practices procedure for making bug fixes or soundness
corrections in the compiler that can cause existing code to stop compiling. This
text is based on
[RFC 1589](https://github.com/rust-lang/rfcs/blob/master/text/1589-rustc-bug-fix-procedure.md).

# Motivation

[motivation]: #motivation

From time to time, we encounter the need to make a bug fix, soundness
correction, or other change in the compiler which will cause existing code to
stop compiling. When this happens, it is important that we handle the change in
a way that gives users of Rust a smooth transition. What we want to avoid is
that existing programs suddenly stop compiling with opaque error messages: we
would prefer to have a gradual period of warnings, with clear guidance as to
what the problem is, how to fix it, and why the change was made. This RFC
describes the procedure that we have been developing for handling breaking
changes that aims to achieve that kind of smooth transition.

One of the key points of this policy is that (a) warnings should be issued
initially rather than hard errors if at all possible and (b) every change that
causes existing code to stop compiling will have an associated tracking issue.
This issue provides a point to collect feedback on the results of that change.
Sometimes changes have unexpectedly large consequences or there may be a way to
avoid the change that was not considered. In those cases, we may decide to
change course and roll back the change, or find another solution (if warnings
are being used, this is particularly easy to do).

### What qualifies as a bug fix?

Note that this RFC does not try to define when a breaking change is permitted.
That is already covered under [RFC 1122][]. This document assumes that the
change being made is in accordance with those policies. Here is a summary of the
conditions from RFC 1122:

- **Soundness changes:** Fixes to holes uncovered in the type system.
- **Compiler bugs:** Places where the compiler is not implementing the specified
  semantics found in an RFC or lang-team decision.
- **Underspecified language semantics:** Clarifications to grey areas where the
  compiler behaves inconsistently and no formal behavior had been previously
  decided.

Please see [the RFC][rfc 1122] for full details!

# Detailed design

[design]: #detailed-design

The procedure for making a breaking change is as follows (each of these steps is
described in more detail below):

1. Do a **crater run** to assess the impact of the change.
2. Make a **special tracking issue** dedicated to the change.
3. Do not report an error right away. Instead, **issue forwards-compatibility
   lint warnings**.
   - Sometimes this is not straightforward. See the text below for suggestions
     on different techniques we have employed in the past.
   - For cases where warnings are infeasible:
     - Report errors, but make every effort to give a targeted error message
       that directs users to the tracking issue
     - Submit PRs to all known affected crates that fix the issue
       - or, at minimum, alert the owners of those crates to the problem and
         direct them to the tracking issue
4. Once the change has been in the wild for at least one cycle, we can
   **stabilize the change**, converting those warnings into errors.

Finally, for changes to `rustc_ast` that will affect plugins, the general policy
is to batch these changes. That is discussed below in more detail.

### Tracking issue

Every breaking change should be accompanied by a **dedicated tracking issue**
for that change. The main text of this issue should describe the change being
made, with a focus on what users must do to fix their code. The issue should be
approachable and practical; it may make sense to direct users to an RFC or some
other issue for the full details. The issue also serves as a place where users
can comment with questions or other concerns.

A template for these breaking-change tracking issues can be found
[here][template]. An example of how such an issue should look can be [found
here][breaking-change-issue].

[template]: https://github.com/rust-lang/rust/issues/new?template=tracking_issue_future.md

### Issuing future compatibility warnings

The best way to handle a breaking change is to begin by issuing
future-compatibility warnings. These are a special category of lint warning.
Adding a new future-compatibility warning can be done as follows.

```rust
// 1. Define the lint in `compiler/rustc_lint/src/builtin.rs` and 
//    add the metadata for the future incompatibility:
declare_lint! {
    pub YOUR_LINT_HERE,
    Warn,
    "illegal use of foo bar baz"
    @future_incompatible = FutureIncompatibleInfo {
        reason: fcw!(FutureReleaseError #1234) // your tracking issue here!
    },
}

// 2. Add a decidacted lint pass for it.
//    This step can be skipped if you emit the lint as part of an existing pass.

#[derive(Default)]
pub struct MyLintPass {
    ...
}

impl {Early,Late}LintPass for MyLintPass { 
    ...
}

impl_lint_pass!(MyLintPass => [YOUR_LINT_HERE]);

// 3. emit the lint somewhere in your lint pass:
cx.emit_span_lint(
    YOUR_LINT_HERE,
    pat.span,
    // some diagnostic struct
    MyDiagnostic {
        ...
    },
);

```

Finally, register the lint in `compiler/rustc_lint/src/lib.rs`. 
There are many examples in that file that already show how to do so.

#### Helpful techniques

It can often be challenging to filter out new warnings from older, pre-existing
errors. One technique that has been used in the past is to run the older code
unchanged and collect the errors it would have reported. You can then issue
warnings for any errors you would give which do not appear in that original set.
Another option is to abort compilation after the original code completes if
errors are reported: then you know that your new code will only execute when
there were no errors before.

#### Crater and crates.io

[Crater] is a bot that will compile all crates.io crates and many
public github repos with the compiler with your changes. A report will then be
generated with crates that ceased to compile with or began to compile with your
changes. Crater runs can take a few days to complete.

[Crater]: ./tests/crater.md

We should always do a crater run to assess impact. It is polite and considerate
to at least notify the authors of affected crates the breaking change. If we can
submit PRs to fix the problem, so much the better.

#### Is it ever acceptable to go directly to issuing errors?

Changes that are believed to have negligible impact can go directly to issuing
an error. One rule of thumb would be to check against `crates.io`: if fewer than
10 **total** affected projects are found (**not** root errors), we can move
straight to an error. In such cases, we should still make the "breaking change"
page as before, and we should ensure that the error directs users to this page.
In other words, everything should be the same except that users are getting an
error, and not a warning. Moreover, we should submit PRs to the affected
projects (ideally before the PR implementing the change lands in rustc).

If the impact is not believed to be negligible (e.g., more than 10 crates are
affected), then warnings are required (unless the compiler team agrees to grant
a special exemption in some particular case). If implementing warnings is not
feasible, then we should make an aggressive strategy of migrating crates before
we land the change so as to lower the number of affected crates. Here are some
techniques for approaching this scenario:

1. Issue warnings for subparts of the problem, and reserve the new errors for
   the smallest set of cases you can.
2. Try to give a very precise error message that suggests how to fix the problem
   and directs users to the tracking issue.
3. It may also make sense to layer the fix:
   - First, add warnings where possible and let those land before proceeding to
     issue errors.
   - Work with authors of affected crates to ensure that corrected versions are
     available _before_ the fix lands, so that downstream users can use them.

### Stabilization

After a change is made, we will **stabilize** the change using the same process
that we use for unstable features:

- After a new release is made, we will go through the outstanding tracking
  issues corresponding to breaking changes and nominate some of them for **final
  comment period** (FCP).
- The FCP for such issues lasts for one cycle. In the final week or two of the
  cycle, we will review comments and make a final determination:

  - Convert to error: the change should be made into a hard error.
  - Revert: we should remove the warning and continue to allow the older code to
    compile.
  - Defer: can't decide yet, wait longer, or try other strategies.

Ideally, breaking changes should have landed on the **stable branch** of the
compiler before they are finalized.

<a id="guide"></a>

### Removing a lint

Once we have decided to make a "future warning" into a hard error, we need a PR
that removes the custom lint. As an example, here are the steps required to
remove the `overlapping_inherent_impls` compatibility lint. First, convert the
name of the lint to uppercase (`OVERLAPPING_INHERENT_IMPLS`) ripgrep through the
source for that string. We will basically by converting each place where this
lint name is mentioned (in the compiler, we use the upper-case name, and a macro
automatically generates the lower-case string; so searching for
`overlapping_inherent_impls` would not find much).

> NOTE: these exact files don't exist anymore, but the procedure is still the same.

#### Remove the lint.

The first reference you will likely find is the lint definition [in
`rustc_session/src/lint/builtin.rs` that resembles this][defsource]:

[defsource]: https://github.com/rust-lang/rust/blob/085d71c3efe453863739c1fb68fd9bd1beff214f/src/librustc/lint/builtin.rs#L171-L175

```rust
declare_lint! {
    pub OVERLAPPING_INHERENT_IMPLS,
    Deny, // this may also say Warning
    "two overlapping inherent impls define an item with the same name were erroneously allowed",
    @future_incompatible = FutureIncompatibleInfo {
        reason: fcw!(FutureReleaseError #1234), // your tracking issue here!
    },
}
```

This `declare_lint!` macro creates the relevant data structures. Remove it. You
will also find that there is a mention of `OVERLAPPING_INHERENT_IMPLS` later in
the file as [part of a `lint_array!`][lintarraysource]; remove it too.

[lintarraysource]: https://github.com/rust-lang/rust/blob/085d71c3efe453863739c1fb68fd9bd1beff214f/src/librustc/lint/builtin.rs#L252-L290

#### Add the lint to the list of removed lints.

In `compiler/rustc_lint/src/lib.rs` there is a list of "renamed and removed lints".
You can add this lint to the list:

```rust
store.register_removed("overlapping_inherent_impls", "converted into hard error, see #36889");
```

where `#36889` is the tracking issue for your lint.

#### Update the places that issue the lint

Finally, the last class of references you will see are the places that actually
**trigger** the lint itself (i.e., what causes the warnings to appear). These
you do not want to delete. Instead, you want to convert them into errors. In
this case, the [`add_lint` call][addlintsource] looks like this:

```rust
self.tcx.sess.add_lint(lint::builtin::OVERLAPPING_INHERENT_IMPLS,
                       node_id,
                       self.tcx.span_of_impl(item1).unwrap(),
                       msg);
```

You'll also often find `node_span_lint` used for this.

We want to convert this into an error. In some cases, there may be an
existing error for this scenario. In others, we will need to allocate a
fresh diagnostic code.  [Instructions for allocating a fresh diagnostic
code can be found here.](./diagnostics/error-codes.md) You may want
to mention in the extended description that the compiler behavior
changed on this point, and include a reference to the tracking issue for
the change.

Let's say that we've adopted `E0592` as our code. Then we can change the
`add_lint()` call above to something like:

```rust
struct_span_code_err!(self.dcx(), self.tcx.span_of_impl(item1).unwrap(), E0592, msg)
    .emit();
```

Or better: a structured diagnostic like this:

```rust
#[derive(Diagnostic)]
struct MyDiagnostic {
    #[label]
    span: Span,
    ...
}
```

#### Update tests

Finally, run the test suite. These should be some tests that used to reference
the `overlapping_inherent_impls` lint, those will need to be updated. In
general, if the test used to have `#[deny(overlapping_inherent_impls)]`, that
can just be removed.

```
./x test
```

#### All done!

Open a PR. =)

[addlintsource]: https://github.com/rust-lang/rust/blob/085d71c3efe453863739c1fb68fd9bd1beff214f/src/librustc_typeck/coherence/inherent.rs#L300-L303
[futuresource]: https://github.com/rust-lang/rust/blob/085d71c3efe453863739c1fb68fd9bd1beff214f/src/librustc_lint/lib.rs#L202-L205

<!-- -Links--------------------------------------------------------------------- -->

[rfc 1122]: https://github.com/rust-lang/rfcs/blob/master/text/1122-language-semver.md
[breaking-change-issue]: https://gist.github.com/nikomatsakis/631ec8b4af9a18b5d062d9d9b7d3d967


---

# Using external repositories

The `rust-lang/rust` git repository depends on several other repos in the `rust-lang` organization.
There are three main ways we use dependencies:
1. As a Cargo dependency through crates.io (e.g. `rustc-rayon`)
2. As a git (e.g. `clippy`) or a [josh] (e.g. `miri`) subtree
3. As a git submodule (e.g. `cargo`)

As a general rule:
- Use crates.io for libraries that could be useful for others in the ecosystem
- Use subtrees for tools that depend on compiler internals and need to be updated if there are breaking
  changes
- Use submodules for tools that are independent of the compiler

## External dependencies (subtrees)

The following external projects are managed using some form of a `subtree`:

* [clippy](https://github.com/rust-lang/rust-clippy)
* [miri](https://github.com/rust-lang/miri)
* [portable-simd](https://github.com/rust-lang/portable-simd)
* [rustfmt](https://github.com/rust-lang/rustfmt)
* [rust-analyzer](https://github.com/rust-lang/rust-analyzer)
* [rustc_codegen_cranelift](https://github.com/rust-lang/rustc_codegen_cranelift)
* [rustc_codegen_gcc](https://github.com/rust-lang/rustc_codegen_gcc)
* [rustc-dev-guide](https://github.com/rust-lang/rustc-dev-guide)
* [compiler-builtins](https://github.com/rust-lang/compiler-builtins)
* [stdarch](https://github.com/rust-lang/stdarch)

In contrast to `submodule` dependencies
(see below for those), the `subtree` dependencies are just regular files and directories which can
be updated in-tree. However, if possible, enhancements, bug fixes, etc. specific
to these tools should be filed against the tools directly in their respective upstream repositories.
The exception is that when rustc changes are required to
implement a new tool feature or test, that should happen in one collective rustc PR.

`subtree` dependencies are currently managed by two distinct approaches:

* Using `git subtree`
    * `clippy` ([sync guide](https://doc.rust-lang.org/nightly/clippy/development/infrastructure/sync.html#performing-the-sync-from-rust-langrust-to-clippy))
    * `portable-simd` ([sync script](https://github.com/rust-lang/portable-simd/blob/master/subtree-sync.sh))
    * `rustfmt`
    * `rustc_codegen_cranelift` ([sync script](https://github.com/rust-lang/rustc_codegen_cranelift/blob/113af154d459e41b3dc2c5d7d878e3d3a8f33c69/scripts/rustup.sh#L7))
    * `rustc_codegen_gcc` ([sync guide](https://github.com/rust-lang/rustc_codegen_gcc/blob/master/doc/subtree.md))
* Using the [josh](#synchronizing-a-josh-subtree) tool
    * `miri`
    * `rust-analyzer`
    * `rustc-dev-guide`
    * `compiler-builtins`
    * `stdarch`

### Josh subtrees

The [josh] tool is an alternative to git subtrees, which manages git history in a different way and scales better to larger repositories.
Specific tooling is required to work with josh.
We provide a helper [`rustc-josh-sync`][josh-sync] tool to help with the synchronization, described [below](#synchronizing-a-josh-subtree).

### Synchronizing a Josh subtree

We use a dedicated tool called [`rustc-josh-sync`][josh-sync] for performing Josh subtree updates.
The commands below can be used for all our Josh subtrees, although note that `miri`
requires you to perform some [additional steps](https://github.com/rust-lang/miri/blob/master/CONTRIBUTING.md#advanced-topic-syncing-with-the-rustc-repo) during pulls.

You can install the tool using the following command:
```
cargo install --locked --git https://github.com/rust-lang/josh-sync
```

Both pulls (synchronize changes from rust-lang/rust into the subtree) and pushes (synchronize
changes from the subtree to rust-lang/rust) are performed from the subtree repository (so first
switch to its repository checkout directory in your terminal).

#### Performing pull
1. Checkout a new branch that will be used to create a PR into the subtree
2. Run the pull command
    ```
    rustc-josh-sync pull
    ```
3. Push the branch to your fork and create a PR into the subtree repository
    - If you have `gh` CLI installed, `rustc-josh-sync` can create the PR for you.

#### Performing push

> NOTE:
> Before you proceed, look at some guidance related to Git [on josh-sync README].

1. Run the push command to create a branch named `<branch-name>` in a `rustc` fork under the `<gh-username>` account
    ```
    rustc-josh-sync push <branch-name> <gh-username>
    ```
2. Create a PR from `<branch-name>` into `rust-lang/rust`

### Creating a new Josh subtree dependency

If you want to migrate a repository dependency from `git subtree` or `git submodule` to josh, you can check out [this guide](https://hackmd.io/7pOuxnkdQDaL1Y1FQr65xg).

### Synchronizing a git subtree

Periodically the changes made to subtree based dependencies need to be synchronized between this
repository and the upstream tool repositories.

Subtree synchronizations are typically handled by the respective tool maintainers.
Other users
are welcome to submit synchronization PRs, however, in order to do so you will need to modify
your local git installation and follow a very precise set of instructions.
These instructions are documented, along with several useful tips and tricks, in the
[syncing subtree changes][clippy-sync-docs] section in Clippy's Contributing guide.
The instructions are applicable for use with any subtree based tool, just be sure to
use the correct corresponding subtree directory and remote repository.

The synchronization process goes in two directions: `subtree push` and `subtree pull`.

A `subtree push` takes all the changes that happened to the copy in this repo and creates commits
on the remote repo that match the local changes.
Every local commit that touched the subtree causes a commit on the remote repo, but
is modified to move the files from the specified directory to the tool repo root.

A `subtree pull` takes all changes since the last `subtree pull`
from the tool repo and adds these commits to the rustc repo along with a merge commit that moves
the tool changes into the specified directory in the Rust repository.

It is recommended that you always do a push first and get that merged to the default branch of the tool.
Then, when you do a pull, the merge works without conflicts.
While it's definitely possible to resolve conflicts during a pull, you may have to redo the conflict
resolution if your PR doesn't get merged fast enough and there are new conflicts.
Do not try to
rebase the result of a `git subtree pull`; rebasing merge commits is a bad idea in general.

You always need to specify the `-P` prefix to the subtree directory and the corresponding remote
repository.
If you specify the wrong directory or repository
you'll get very fun merges that try to push the wrong directory to the wrong remote repository.
Luckily you can just abort this without any consequences by throwing away either the pulled commits
in rustc or the pushed branch on the remote and try again.
It is usually fairly obvious
that this is happening because you suddenly get thousands of commits that want to be synchronized.

[clippy-sync-docs]: https://doc.rust-lang.org/nightly/clippy/development/infrastructure/sync.html

### Creating a new subtree dependency

If you want to create a new subtree dependency from an existing repository, call (from this
repository's root directory!)

```
git subtree add -P src/tools/clippy https://github.com/rust-lang/rust-clippy.git master
```

This will create a new commit, which you may not rebase under any circumstances!
Delete the commit and redo the operation if you need to rebase.

Now you're done, the `src/tools/clippy` directory behaves as if Clippy were
part of the rustc monorepo, so no one but you (or others that synchronize
subtrees) actually needs to use `git subtree`.

## External dependencies (submodules)

Building Rust will also use external git repositories tracked using [git submodules].
The complete list may be found in the [`.gitmodules`] file.
Some of these projects are required (like `stdarch` for the standard library) and
some of them are optional (like `src/doc/book`).

Usage of submodules is discussed more in the [Using Git chapter](git.md#git-submodules).

Some of the submodules are allowed to be in a "broken" state where they
either don't build or their tests don't pass, e.g. the documentation books
like [The Rust Reference].
Maintainers of these projects will be notified
when the project is in a broken state, and they should fix them as soon as possible.
The current status is tracked on the [toolstate website].
More information may be found on the Forge [Toolstate chapter].
In practice, it is very rare for documentation to have broken toolstate.

Breakage is not allowed in the beta and stable channels, and must be addressed
before the PR is merged.
They are also not allowed to be broken on `main` in the week leading up to the beta cut.

[git submodules]: https://git-scm.com/book/en/v2/Git-Tools-Submodules
[`.gitmodules`]: https://github.com/rust-lang/rust/blob/HEAD/.gitmodules
[The Rust Reference]: https://github.com/rust-lang/reference/
[toolstate website]: https://rust-lang-nursery.github.io/rust-toolstate/
[Toolstate chapter]: https://forge.rust-lang.org/infra/toolstate.html
[josh]: https://josh-project.github.io/josh/intro.html
[josh-sync]: https://github.com/rust-lang/josh-sync
[on josh-sync README]: https://github.com/rust-lang/josh-sync#git-peculiarities


---

# Fuzzing

<!-- date-check: Mar 2023 -->

For the purposes of this guide, *fuzzing* is any testing methodology that
involves compiling a wide variety of programs in an attempt to uncover bugs in rustc.
Fuzzing is often used to find internal compiler errors (ICEs).
Fuzzing can be beneficial, because it can find bugs before users run into them.
It also provides small, self-contained programs that make the bug easier to track down.
However, some common mistakes can reduce the helpfulness of fuzzing and end up
making contributors' lives harder.
To maximize your positive impact on the Rust
project, please read this guide before reporting fuzzer-generated bugs!

## Guidelines

### In a nutshell

*Please do:*

- Ensure the bug is still present on the latest nightly rustc
- Include a reasonably minimal, standalone example along with any bug report
- Include all of the information requested in the bug report template
- Search for existing reports with the same message and query stack
- Format the test case with `rustfmt`
- Indicate that the bug was found by fuzzing

*Please don't:*

- Don't report lots of bugs that use internal features, including but not
  limited to `custom_mir`, `lang_items`, `no_core`, and `rustc_attrs`.
- Don't seed your fuzzer with inputs that are known to crash rustc (details below).

### Discussion

If you're not sure whether or not an ICE is a duplicate of one that's already
been reported, please go ahead and report it and link to issues you think might be related.
In general, ICEs on the same line but with different *query stacks* are usually distinct bugs.
For example, [#109020] and [#109129] had similar error messages:

```
error: internal compiler error: compiler/rustc_middle/src/ty/normalize_erasing_regions.rs:195:90: Failed to normalize <[closure@src/main.rs:36:25: 36:28] as std::ops::FnOnce<(Emplacable<()>,)>>::Output, maybe try to call `try_normalize_erasing_regions` instead
```

```
error: internal compiler error: compiler/rustc_middle/src/ty/normalize_erasing_regions.rs:195:90: Failed to normalize <() as Project>::Assoc, maybe try to call `try_normalize_erasing_regions` instead
```

However, they have different query stacks:
```
query stack during panic:
#0 [fn_abi_of_instance] computing call ABI of `<[closure@src/main.rs:36:25: 36:28] as core::ops::function::FnOnce<(Emplacable<()>,)>>::call_once - shim(vtable)`
end of query stack
```
```
query stack during panic:
#0 [check_mod_attrs] checking attributes in top-level module
#1 [analysis] running analysis passes on this crate
end of query stack
```

[#109020]: https://github.com/rust-lang/rust/issues/109020
[#109129]: https://github.com/rust-lang/rust/issues/109129

## Building a corpus

When building a corpus, be sure to avoid collecting tests that are already known to crash rustc.
A fuzzer that is seeded with such tests is more likely to
generate bugs with the same root cause.
The simplest way to avoid this is to loop over each file in the corpus, see if it causes an
ICE, and remove it if so.

To build a corpus, you may want to use:

- The rustc/rust-analyzer/clippy test suites (or even source code) --- though avoid
  tests that are already known to cause failures, which often begin with comments
  like `//@ failure-status: 101` or `//@ known-bug: #NNN`.
- The already-fixed ICEs in the archived [Glacier] repository --- though
  avoid the unfixed ones in `ices/`!

[glacier]: https://github.com/rust-lang/glacier

## Extra credit

Here are a few things you can do to help the Rust project after filing an ICE:

- [Bisect][bisect] the bug to figure out when it was introduced.
  If you find the regressing PR / commit, you can mark the issue with the label `S-has-bisection`.
  If not, consider applying `E-needs-bisection` instead.
- Fix "distractions": problems with the test case that don't contribute to
  triggering the ICE, such as syntax errors or borrow-checking errors
- Minimize the test case (see below).
  If successful, you can label the issue with `S-has-mcve`.
  Otherwise, you can apply `E-needs-mcve`.
- Add the minimal test case to the rust-lang/rust repo as a [crash test].
  While you're at it, consider including other "untracked" crashes in your PR.
  Please don't forget to mark all relevant issues with `S-bug-has-test` once your PR is merged.

See also [applying and removing labels][labeling].

[bisect]: https://rust-lang.github.io/cargo-bisect-rustc/
[crash test]: tests/compiletest.html#crash-tests
[labeling]: https://forge.rust-lang.org/release/issue-triaging.html#applying-and-removing-labels

## Minimization

It is helpful to carefully *minimize* the fuzzer-generated input.
When minimizing, be careful to preserve the original error, and avoid introducing
distracting problems such as syntax, type-checking, or borrow-checking errors.

There are some tools that can help with minimization.
If you're not sure how to avoid introducing syntax, type-, and borrow-checking errors while using
these tools, post both the complete and minimized test cases.
Generally,
*syntax-aware* tools give the best results in the least amount of time.
[`treereduce-rust`][treereduce] and [picireny][picireny] are syntax-aware.
[`halfempty`][halfempty] is not, but is generally a high-quality tool.

[halfempty]: https://github.com/googleprojectzero/halfempty
[picireny]: https://github.com/renatahodovan/picireny
[treereduce]: https://github.com/langston-barrett/treereduce

## Effective fuzzing

When fuzzing rustc, you may want to avoid generating machine code, since this
is mostly done by LLVM.
Try `--emit=mir` instead.

A variety of compiler flags can uncover different issues.
`-Zmir-opt-level=4` will turn on MIR optimization passes that are not run by default, potentially
uncovering interesting bugs.
`-Zvalidate-mir` can help uncover such bugs.

If you're fuzzing a compiler you built, you may want to build it with `-C
target-cpu=native` or even PGO/BOLT to squeeze out a few more executions per second.
Of course, it's best to try multiple build configurations and see
what actually results in superior throughput.

You may want to build rustc from source with debug assertions to find
additional bugs, though this can slow down fuzzing by
requiring extra work for every execution.
To enable debug assertions, add this to `bootstrap.toml` when compiling rustc:

```toml
rust.debug-assertions = true
```

ICEs that require debug assertions to reproduce should be tagged
[`requires-debug-assertions`].

[`requires-debug-assertions`]: https://github.com/rust-lang/rust/labels/requires-debug-assertions

## Existing projects

- [fuzz-rustc][fuzz-rustc] demonstrates how to fuzz rustc with libfuzzer
- [icemaker][icemaker] runs rustc and other tools on a large number of source
  files with a variety of flags to catch ICEs
- [tree-splicer][tree-splicer] generates new source files by combining existing
  ones while maintaining correct syntax

[fuzz-rustc]: https://github.com/dwrensha/fuzz-rustc
[icemaker]: https://github.com/matthiaskrgr/icemaker/
[tree-splicer]: https://github.com/langston-barrett/tree-splicer/


---

# `rust-lang/rust` Licenses

The `rustc` compiler source and standard library are dual licensed under the [Apache License v2.0](https://github.com/rust-lang/rust/blob/HEAD/LICENSE-APACHE) and the [MIT License](https://github.com/rust-lang/rust/blob/HEAD/LICENSE-MIT) unless otherwise specified.

Detailed licensing information is available in the [COPYRIGHT document](https://github.com/rust-lang/rust/blob/HEAD/COPYRIGHT) of the `rust-lang/rust` repository.

## Guidelines for reviewers

In general, reviewers need to be looking not only for the code quality of contributions but also
that they are properly licensed.
We have some tips below for things to look out for when reviewing, but if you ever feel uncertain
as to whether some code might be properly licensed, err on the safe side — reach out to the Council
or Compiler Team Leads for feedback!

Things to watch out for:

- The PR author states that they copied, ported, or adapted the code from some other source.
- There is a comment in the code pointing to a webpage or describing where the algorithm was taken
from.
- The algorithm or code pattern seems like it was likely copied from somewhere else.
- When adding new dependencies, double check the dependency's license.

In all of these cases, we will want to check that source to make sure it is licensed in a way
that is compatible with Rust’s license.

Examples

- Porting C code from a GPL project, like GNU binutils, is not allowed. That would require Rust
itself to be licensed under the GPL.
- Copying code from an algorithms text book may be allowed, but some algorithms are patented.

## Porting

Contributions to rustc, especially around platform and compiler intrinsics, often include porting
over work from other projects, mainly LLVM and GCC.

Some general rules apply:

- Copying work needs to adhere to the original license
    - This applies to direct copy & paste
    - This also applies to code you looked at and ported

In general, taking inspiration from other codebases is fine, but please exercise caution when
porting code.

Ports of full libraries (e.g. C libraries shipped with LLVM) must keep the license of the original
library.


---

# Editions

This chapter gives an overview of how Edition support works in rustc.
This assumes that you are familiar with what Editions are (see the [Edition Guide]).

[Edition Guide]: https://doc.rust-lang.org/edition-guide/

## Edition definition

The `--edition` CLI flag specifies the edition to use for a crate.
This can be accessed from [`Session::edition`].
There are convenience functions like [`Session::at_least_rust_2021`] for checking the crate's
edition, though you should be careful about whether you check the global session or the span, see
[Edition hygiene] below.

As an alternative to the `at_least_rust_20xx` convenience methods, the [`Edition`] type also
supports comparisons for doing range checks, such as `span.edition() >= Edition::Edition2021`.

[`Session::edition`]: https://doc.rust-lang.org/nightly/nightly-rustc/rustc_session/struct.Session.html#method.edition
[`Session::at_least_rust_2021`]: https://doc.rust-lang.org/nightly/nightly-rustc/rustc_session/struct.Session.html#method.at_least_rust_2021
[`Edition`]: https://doc.rust-lang.org/nightly/nightly-rustc/rustc_span/edition/enum.Edition.html

### Adding a new edition

Adding a new edition mainly involves adding a variant to the [`Edition`] enum and then fixing
everything that is broken. See [#94461](https://github.com/rust-lang/rust/pull/94461) for an
example.

### Features and Edition stability

The [`Edition`] enum defines whether or not an edition is stable.
If it is not stable, then the `-Zunstable-options` CLI option must be passed to enable it.

When adding a new feature, there are two options you can choose for how to handle stability with a
future edition:

- Just check the edition of the span like `span.at_least_rust_20xx()` (see [Edition hygiene]) or the
  [`Session::edition`]. This will implicitly depend on the stability of the edition itself to
  indicate that your feature is available.
- Place your new behavior behind a [feature gate].

It may be sufficient to only check the current edition for relatively simple changes.
However, for larger language changes, you should consider creating a feature gate.
There are several benefits to using a feature gate:

- A feature gate makes it easier to work on and experiment with a new feature.
- It makes the intent clear when the `#![feature(…)]` attribute is used that your new feature is
  being enabled.
- It makes testing of editions easier so that features that are not yet complete do not interfere
  with testing of edition-specific features that are complete and ready.
- It decouples the feature from an edition, which makes it easier for the team to make a deliberate
  decision of whether or not a feature should be added to the next edition when the feature is
  ready.

When a feature is complete and ready, the feature gate can be removed (and the code should just
check the span or `Session` edition to determine if it is enabled).

There are a few different options for doing feature checks:

- For highly experimental features, that may or may not be involved in an edition, they can
  implement regular feature gates like `tcx.features().my_feature`, and ignore editions for the time
  being.

- For experimental features that *might* be involved in an edition, they should implement gates with
  `tcx.features().my_feature && span.at_least_rust_20xx()`.
  This requires the user to still specify `#![feature(my_feature)]`, to avoid disrupting testing of
  other edition features which are ready and have been accepted within the edition.

- For experimental features that have graduated to definitely be part of an edition,
  they should implement gates with `tcx.features().my_feature || span.at_least_rust_20xx()`,
  or just remove the feature check altogether and just check `span.at_least_rust_20xx()`.

If you need to do the feature gating in multiple places, consider placing the check in a single
function so that there will only be a single place to update. For example:

```rust,ignore
// An example from Edition 2021 disjoint closure captures.

fn enable_precise_capture(tcx: TyCtxt<'_>, span: Span) -> bool {
    tcx.features().capture_disjoint_fields || span.rust_2021()
}
```

See [Lints and stability](#lints-and-stability) below for more information about how lints handle
stability.

[feature gate]: ../feature-gates.md

## Edition parsing

For the most part, the lexer is edition-agnostic.
Within [`Lexer`], tokens can be modified based on edition-specific behavior.
For example, C-String literals like `c"foo"` are split into multiple tokens in editions before 2021.
This is also where things like reserved prefixes are handled for the 2021 edition.

Edition-specific parsing is relatively rare. One example is `async fn` which checks the span of the
token to determine if it is the 2015 edition, and emits an error in that case.
This can only be done if the syntax was already invalid.

If you need to do edition checking in the parser, you will normally want to look at the edition of
the token, see [Edition hygiene].
In some rare cases you may instead need to check the global edition from [`ParseSess::edition`].

Most edition-specific parsing behavior is handled with [migration lints] instead of in the parser.
This is appropriate when there is a *change* in syntax (as opposed to new syntax).
This allows the old syntax to continue to work on previous editions.
The lint then checks for the change in behavior.
On older editions, the lint pass should emit the migration lint to help with migrating to new
editions.
On newer editions, your code should emit a hard error with `emit_err` instead.
For example, the deprecated `start...end` pattern syntax emits the
[`ellipsis_inclusive_range_patterns`] lint on editions before 2021, and in 2021 is an hard error via
the `emit_err` method.

[`Lexer`]: https://doc.rust-lang.org/nightly/nightly-rustc/rustc_parse/lexer/struct.Lexer.html
[`ParseSess::edition`]: https://doc.rust-lang.org/nightly/nightly-rustc/rustc_session/parse/struct.ParseSess.html#structfield.edition
[`ellipsis_inclusive_range_patterns`]: https://doc.rust-lang.org/nightly/rustc/lints/listing/warn-by-default.html#ellipsis-inclusive-range-patterns

### Keywords

New keywords can be introduced across an edition boundary.
This is implemented by functions like [`Symbol::is_used_keyword_conditional`], which rely on the
ordering of how the keywords are defined.

When new keywords are introduced, the [`keyword_idents`] lint should be updated so that automatic
migrations can transition code that might be using the keyword as an identifier (see
[`KeywordIdents`]).
An alternative to consider is to implement the keyword as a weak keyword if the position it is used
is sufficient to distinguish it.

An additional option to consider is the `k#` prefix which was introduced in [RFC 3101].
This allows the use of a keyword in editions *before* the edition where the keyword is introduced.
This is currently not implemented.

[`Symbol::is_used_keyword_conditional`]: https://doc.rust-lang.org/nightly/nightly-rustc/rustc_span/symbol/struct.Symbol.html#method.is_used_keyword_conditional
[`keyword_idents`]: https://doc.rust-lang.org/nightly/rustc/lints/listing/allowed-by-default.html#keyword-idents
[`KeywordIdents`]: https://doc.rust-lang.org/nightly/nightly-rustc/rustc_lint/builtin/struct.KeywordIdents.html
[RFC 3101]: https://rust-lang.github.io/rfcs/3101-reserved_prefixes.html

### Edition hygiene
[edition hygiene]: #edition-hygiene

Spans are marked with the edition of the crate that the span came from.
See [Macro hygiene] in the Edition Guide for a user-centric description of what this means.

You should normally use the edition from the token span instead of looking at the global `Session`
edition.
For example, use `span.edition().at_least_rust_2021()` instead of `sess.at_least_rust_2021()`.
This helps ensure that macros behave correctly when used across crates.

[Macro hygiene]: https://doc.rust-lang.org/nightly/edition-guide/editions/advanced-migrations.html#macro-hygiene

## Lints

Lints support a few different options for interacting with editions.
Lints can be *future incompatible edition migration lints*, which are used to support
[migrations][migration lints] to newer editions.
Alternatively, lints can be [edition-specific](#edition-specific-lints), where they change their
default level starting in a specific edition.

### Migration lints
[migration lints]: #migration-lints
[migration lint]: #migration-lints

*Migration lints* are used to migrate projects from one edition to the next.
They are implemented with a `MachineApplicable` [suggestion](../diagnostics.md#suggestions) which
will rewrite code so that it will **successfully compile in both the previous and the next
edition**.
For example, the [`keyword_idents`] lint will take identifiers that conflict with a new keyword to
use the raw identifier syntax to avoid the conflict (for example changing `async` to `r#async`).

Migration lints must be declared with the [`FutureIncompatibilityReason::EditionError`] or
[`FutureIncompatibilityReason::EditionSemanticsChange`] [future-incompatible
option](../diagnostics.md#future-incompatible-lints) in the lint declaration:

```rust,ignore
declare_lint! {
    pub KEYWORD_IDENTS,
    Allow,
    "detects edition keywords being used as an identifier",
    @future_incompatible = FutureIncompatibleInfo {
        reason: fcw!(EditionError 2018 "slug-of-edition-guide-page")
    };
}
```

When declared like this, the lint is automatically added to the appropriate
`rust-20xx-compatibility` lint group.
When a user runs `cargo fix --edition`, cargo will pass the `--force-warn rust-20xx-compatibility`
flag to force all of these lints to appear during the edition migration.
Cargo also passes `--cap-lints=allow` so that no other lints interfere with the edition migration.

Make sure that the example code sets the correct edition. The example should illustrate the previous edition, and show what the migration warning would look like. For example, this lint for a 2024 migration shows an example in 2021:

```rust,ignore
declare_lint! {
    /// The `keyword_idents_2024` lint detects ...
    ///
    /// ### Example
    ///
    /// ```rust,edition2021
    /// #![warn(keyword_idents_2024)]
    /// fn gen() {}
    /// ```
    ///
    /// {{produces}}
}
```

Migration lints can be either `Allow` or `Warn` by default.
If it is `Allow`, users usually won't see this warning unless they are doing an edition migration
manually or there is a problem during the migration.
Most migration lints are `Allow`.

If it is `Warn` by default, users on all editions will see this warning.
Only use `Warn` if you think it is important for everyone to be aware of the change, and to
encourage people to update their code on all editions.
Beware that new warn-by-default lint that hit many projects can be very disruptive and frustrating
for users.
You may consider switching an `Allow` to `Warn` several years after the edition stabilizes.
This will only show up for the relatively small number of stragglers who have not updated to the new
edition.

[`keyword_idents`]: https://doc.rust-lang.org/nightly/rustc/lints/listing/allowed-by-default.html#keyword-idents
[`FutureIncompatibilityReason::EditionError`]: https://doc.rust-lang.org/nightly/nightly-rustc/rustc_lint_defs/enum.FutureIncompatibilityReason.html#variant.EditionError
[`FutureIncompatibilityReason::EditionSemanticsChange`]: https://doc.rust-lang.org/nightly/nightly-rustc/rustc_lint_defs/enum.FutureIncompatibilityReason.html#variant.EditionSemanticsChange

### Edition-specific lints

Lints can be marked so that they have a different level starting in a specific edition.
In the lint declaration, use the `@edition` marker:

```rust,ignore
declare_lint! {
    pub SOME_LINT_NAME,
    Allow,
    "my lint description",
    @edition Edition2024 => Warn;
}
```

Here, `SOME_LINT_NAME` defaults to `Allow` on all editions before 2024, and then becomes `Warn`
afterwards.

This should generally be used sparingly, as there are other options:

- Small impact stylistic changes unrelated to an edition can just make the lint `Warn` on all
  editions. If you want people to adopt a different way to write things, then go ahead and commit to
  having it show up for all projects.

  Beware that if a new warn-by-default lint hits many projects, it can be very disruptive and
  frustrating for users.

- Change the new style to be a hard error in the new edition, and use a [migration lint] to
  automatically convert projects to the new style. For example,
  [`ellipsis_inclusive_range_patterns`] is a hard error in 2021, and warns in all previous editions.

  Beware that these cannot be added after the edition stabilizes.

- Migration lints can also change over time.
  For example, the migration lint can start out as `Allow` by default.
  For people performing the migration, they will automatically get updated to the new code.
  Then, after some years, the lint can be made to `Warn` in previous editions.

  For example [`anonymous_parameters`] was a 2018 Edition migration lint (and a hard-error in 2018)
  that was `Allow` by default in previous editions.
  Then, three years later, it was changed to `Warn` for all previous editions, so that all users got
  a warning that the style was being phased out.
  If this was a warning from the start, it would have impacted many projects and be very disruptive.
  By making it part of the edition, most users eventually updated to the new edition and were
  handled by the migration.
  Switching to `Warn` only impacted a few stragglers who did not update.

[`ellipsis_inclusive_range_patterns`]: https://doc.rust-lang.org/nightly/rustc/lints/listing/warn-by-default.html#ellipsis-inclusive-range-patterns
[`anonymous_parameters`]: https://doc.rust-lang.org/nightly/rustc/lints/listing/warn-by-default.html#anonymous-parameters

### Lints and stability

Lints can be marked as being unstable, which can be helpful when developing a new edition feature,
and you want to test out a migration lint.
The feature gate can be specified in the lint's declaration like this:

```rust,ignore
declare_lint! {
    pub SOME_LINT_NAME,
    Allow,
    "my cool lint",
    @feature_gate = sym::my_feature_name;
}
```

Then, the lint will only fire if the user has the appropriate `#![feature(my_feature_name)]`.
Just beware that when it comes time to do crater runs testing the migration that the feature gate
will need to be removed.

Alternatively, you can implement an allow-by-default [migration lint] for an upcoming unstable
edition without a feature gate.
Although users may technically be able to enable the lint before the edition is stabilized, most
will not notice the new lint exists, and it should not disrupt anything or cause any breakage.

### Idiom lints

In the 2018 edition, there was a concept of "idiom lints" under the `rust-2018-idioms` lint group.
The concept was to have new idiomatic styles under a different lint group separate from the forced
migrations under the `rust-2018-compatibility` lint group, giving some flexibility as to how people
opt-in to certain edition changes.

Overall this approach did not seem to work very well,
and it is unlikely that we will use the idiom groups in the future.

## Standard library changes

### Preludes

Each edition comes with a specific prelude of the standard library.
These are implemented as regular modules in [`core::prelude`] and [`std::prelude`].
New items can be added to the prelude, just beware that this can conflict with user's pre-existing
code.
Usually a [migration lint] should be used to migrate existing code to avoid the conflict.
For example, [`rust_2021_prelude_collisions`] is used to handle the collisions with the new traits
in 2021.

[`core::prelude`]: https://doc.rust-lang.org/core/prelude/index.html
[`std::prelude`]: https://doc.rust-lang.org/std/prelude/index.html
[`rust_2021_prelude_collisions`]: https://doc.rust-lang.org/nightly/rustc/lints/listing/allowed-by-default.html#rust-2021-prelude-collisions

### Customized language behavior

Usually it is not possible to make breaking changes to the standard library.
In some rare cases, the teams may decide that the behavior change is important enough to break this
rule.
The downside is that this requires special handling in the compiler to be able to distinguish when
the old and new signatures or behaviors should be used.

One example is the change in method resolution for [`into_iter()` of arrays][into-iter].
This was implemented with the `#[rustc_skip_array_during_method_dispatch]` attribute on the
`IntoIterator` trait which then tells the compiler to consider an alternate trait resolution choice
based on the edition.

Another example is the [`panic!` macro changes][panic-macro].
This required defining multiple panic macros, and having the built-in panic macro implementation
determine the appropriate way to expand it.
This also included the [`non_fmt_panics`] [migration lint] to adjust old code to the new form, which
required the `rustc_diagnostic_item` attribute to detect the usage of the panic macro.

In general it is recommended to avoid these special cases except for very high value situations.

[into-iter]: https://doc.rust-lang.org/nightly/edition-guide/rust-2021/IntoIterator-for-arrays.html
[panic-macro]: https://doc.rust-lang.org/nightly/edition-guide/rust-2021/panic-macro-consistency.html
[`non_fmt_panics`]: https://doc.rust-lang.org/nightly/rustc/lints/listing/warn-by-default.html#non-fmt-panics

### Migrating the standard library edition

Updating the edition of the standard library itself roughly involves the following process:

- Wait until the newly stabilized edition has reached beta and the bootstrap compiler has been updated.
- Apply migration lints. This can be an involved process since some code is in external submodules[^std-submodules], and the standard library makes heavy use of conditional compilation. Also, running `cargo fix --edition` can be impractical on the standard library itself. One approach is to individually add `#![warn(...)]` at the top of each crate for each lint, run `./x check library`, apply the migrations, remove the `#![warn(...)]` and commit each migration separately. You'll likely need to run `./x check` with `--target` for many different targets to get full coverage (otherwise you'll likely spend days or weeks getting CI to pass)[^ed-docker]. See also the [advanced migration guide] for more tips.
    - Apply migrations to [`backtrace-rs`]. [Example for 2024](https://github.com/rust-lang/backtrace-rs/pull/700). Note that this doesn't update the edition of the crate itself because that is published independently on crates.io, and that would otherwise restrict the minimum Rust version. Consider adding some `#![deny()]` attributes to avoid regressions until its edition gets updated.
    - Apply migrations to [`stdarch`], and update its edition, and formatting. [Example for 2024](https://github.com/rust-lang/stdarch/pull/1710).
    - Post PRs to update the backtrace and stdarch submodules, and wait for those to land.
    - Apply migration lints to the standard library crates, and update their edition. I recommend working one crate at a time starting with `core`. [Example for 2024](https://github.com/rust-lang/rust/pull/138162).

[^std-submodules]: This will hopefully change in the future to pull these submodules into `rust-lang/rust`.
[^ed-docker]: You'll also likely need to do a lot of testing for different targets, and this is where [docker testing](../tests/docker.md) comes in handy.

[advanced migration guide]: https://doc.rust-lang.org/nightly/edition-guide/editions/advanced-migrations.html
[`backtrace-rs`]: https://github.com/rust-lang/backtrace-rs/
[`stdarch`]: https://github.com/rust-lang/stdarch/

## Stabilizing an edition

After the edition team has given the go-ahead, the process for stabilizing an edition is roughly:

- Update [`LATEST_STABLE_EDITION`].
- Update [`Edition::is_stable`].
- Hunt and find any document that refers to edition by number, and update it:
    - [`--edition` flag](https://github.com/rust-lang/rust/blob/HEAD/src/doc/rustc/src/command-line-arguments.md#--edition-specify-the-edition-to-use)
    - [Rustdoc attributes](https://github.com/rust-lang/rust/blob/HEAD/src/doc/rustdoc/src/write-documentation/documentation-tests.md#attributes)
- Clean up any tests that use the `//@ edition` header to remove the `-Zunstable-options` flag to ensure they are indeed stable. Note: Ideally this should be automated, see [#133582].
- Bless any tests that change.
- Update `lint-docs` to default to the new edition.

See [example for 2024](https://github.com/rust-lang/rust/pull/133349).

[`LATEST_STABLE_EDITION`]: https://doc.rust-lang.org/nightly/nightly-rustc/rustc_span/edition/constant.LATEST_STABLE_EDITION.html
[`Edition::is_stable`]: https://doc.rust-lang.org/nightly/nightly-rustc/rustc_span/edition/enum.Edition.html#method.is_stable
[#133582]: https://github.com/rust-lang/rust/issues/133582
