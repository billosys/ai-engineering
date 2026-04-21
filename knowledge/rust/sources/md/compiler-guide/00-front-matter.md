# Getting Started

Thank you for your interest in contributing to Rust!
There are many ways to contribute, and we appreciate all of them.

If this is your first time contributing, the [walkthrough] chapter can give you a good example of
how a typical contribution would go.

This documentation is _not_ intended to be comprehensive;
it is meant to be a quick guide for the most useful things.
For more information,
see [How to build and run the compiler](building/how-to-build-and-run.md).

[internals]: https://internals.rust-lang.org
[rust-zulip]: https://rust-lang.zulipchat.com
[coc]: https://www.rust-lang.org/policies/code-of-conduct
[walkthrough]: ./walkthrough.md
[Getting Started]: ./getting-started.md

## Asking Questions

If you have questions, please make a post on the [Rust Zulip server][rust-zulip] or
[internals.rust-lang.org][internals].
See the [list of teams and working groups][governance] and [the Community page][community] on the
official website for more resources.

[governance]: https://www.rust-lang.org/governance
[community]: https://www.rust-lang.org/community

As a reminder, all contributors are expected to follow our [Code of Conduct][coc].

The compiler team (or `t-compiler`) usually hangs out in Zulip in
[the #t-compiler channel][z-t-compiler];
questions about how the compiler works can go in [#t-compiler/help][z-help].

[z-t-compiler]: https://rust-lang.zulipchat.com/#narrow/channel/131828-t-compiler
[z-help]: https://rust-lang.zulipchat.com/#narrow/channel/182449-t-compiler.2Fhelp

**Please ask questions!** A lot of people report feeling that they are "wasting
expert's time", but nobody on `t-compiler` feels this way.
Contributors are important to us.

Also, if you feel comfortable, prefer public topics, as this means others can
see the questions and answers, and perhaps even integrate them back into this guide :)

**Tip**: If you're not a native English speaker and feel unsure about writing, try using a translator to help.
But avoid using LLM tools that generate long, complex words.
In daily teamwork, **simple and clear words** are best for easy understanding.
Even small typos or grammar mistakes can make you seem more human, and people connect better with humans.

### Experts

Not all `t-compiler` members are experts on all parts of `rustc`;
it's a pretty large project.
To find out who could have some expertise on
different parts of the compiler, [consult triagebot assign groups][map].
The sections that start with `[assign*` in `triagebot.toml` file.
But also, feel free to ask questions even if you can't figure out who to ping.

Another way to find experts for a given part of the compiler is to see who has made recent commits.
For example, to find people who have recently worked on name resolution since the 1.68.2 release,
you could run `git shortlog -n 1.68.2.. compiler/rustc_resolve/`.
Ignore any commits starting with
"Rollup merge" or commits by `@bors` (see [CI contribution procedures](./contributing.md#ci) for
more information about these commits).

[map]: https://github.com/rust-lang/rust/blob/HEAD/triagebot.toml

### Etiquette

We do ask that you be mindful to include as much useful information as you can
in your question, but we recognize this can be hard if you are unfamiliar with contributing to Rust.

Just pinging someone without providing any context can be a bit annoying and
just create noise, so we ask that you be mindful of the fact that the
`t-compiler` folks get a lot of pings in a day.

## What should I work on?

The Rust project is quite large and it can be difficult to know which parts of the project need
help, or are a good starting place for beginners.
Here are some suggested starting places.

### Easy or mentored issues

If you're looking for somewhere to start, check out the following [issue
search][help-wanted-search].
See the [Triage] for an explanation of these labels.
You can also try filtering the search to areas you're interested in.
For example:

- `repo:rust-lang/rust-clippy` will only show clippy issues
- `label:T-compiler` will only show issues related to the compiler
- `label:A-diagnostics` will only show diagnostic issues

Not all important or beginner work has issue labels.
See below for how to find work that isn't labelled.

[help-wanted-search]: https://github.com/rust-lang/rust/issues?q=is%3Aopen%20is%3Aissue%20org%3Arust-lang%20no%3Aassignee%20label%3AE-easy%2CE-medium%2CE-help-wanted%2CE-mentor%20-label%3AS-blocked%20-linked%3Apr
[Triage]: ./contributing.md#issue-triage

### Recurring work

Some work is too large to be done by a single person.
In this case, it's common to have "Tracking issues" to co-ordinate the work between contributors.
Here are some example tracking issues where
it's easy to pick up work without a large time commitment:

- *Add recurring work items here.*

If you find more recurring work, please feel free to add it here!

### Clippy issues

The [Clippy] project has spent a long time making its contribution process as friendly to newcomers
as possible.
Consider working on it first to get familiar with the process and the compiler internals.

See [the Clippy contribution guide][clippy-contributing] for instructions on getting started.

[Clippy]: https://doc.rust-lang.org/clippy/
[clippy-contributing]: https://github.com/rust-lang/rust-clippy/blob/master/CONTRIBUTING.md

### Diagnostic issues

Many diagnostic issues are self-contained and don't need detailed background knowledge of the
compiler.
You can see a list of diagnostic issues [here][diagnostic-issues].

[diagnostic-issues]: https://github.com/rust-lang/rust/issues?q=is%3Aissue+is%3Aopen+label%3AA-diagnostics+no%3Aassignee

### Picking up abandoned pull requests

Sometimes, contributors send a pull request, but later find out that they don't have enough
time to work on it, or they simply are not interested in it anymore.
Such PRs are often eventually closed and they receive the `S-inactive` label.
You could try to examine some of these PRs and pick up the work.
You can find the list of such PRs [here][abandoned-prs].

If the PR has been implemented in some other way in the meantime, the `S-inactive` label
should be removed from it.
If not, and it seems that there is still interest in the change,
you can try to rebase the pull request on top of the latest `main` branch and send a new
pull request, continuing the work on the feature.

[abandoned-prs]: https://github.com/rust-lang/rust/pulls?q=is%3Apr+label%3AS-inactive+is%3Aclosed

### Writing tests

Issues that have been resolved but do not have a regression test are marked with the `E-needs-test` label.
Writing unit tests is a low-risk,
lower-priority task that offers new contributors a great opportunity to familiarize themselves
with the testing infrastructure and contribution workflow.
You can see a list of needs test issues [here][needs-test-issues].

[needs-test-issues]: https://github.com/rust-lang/rust/issues?q=is%3Aissue%20is%3Aopen%20label%3AE-needs-test%20no%3Aassignee

### Contributing to std (standard library)

See [std-dev-guide](https://std-dev-guide.rust-lang.org/).

### Contributing code to other Rust projects

There are a bunch of other projects that you can contribute to outside of the
`rust-lang/rust` repo, including `cargo`, `miri`, `rustup`, and many others.

These repos might have their own contributing guidelines and procedures.
Many of them are owned by working groups.
For more info, see the documentation in those repos' READMEs.

### Other ways to contribute

There are a bunch of other ways you can contribute, especially if you don't
feel comfortable jumping straight into the large `rust-lang/rust` codebase.

The following tasks are doable without much background knowledge but are incredibly helpful:

- [Writing documentation][wd]: if you are feeling a bit more intrepid, you could try
  to read a part of the code and write doc comments for it.
  This will help you to learn some part of the compiler while also producing a useful artifact!
- [Triaging issues][triage]: categorizing, replicating, and minimizing issues is very helpful to the Rust maintainers.
- [Working areas][wa]: there are a bunch of working areas on a wide variety
  of rust-related things.
- Answer questions on [users.rust-lang.org][users], or on [Stack Overflow][so].
- Participate in the [RFC process](https://github.com/rust-lang/rfcs).
- Find a [requested community library][community-library], build it, and publish
  it to [Crates.io](http://crates.io).
  Easier said than done, but very, very valuable!

[users]: https://users.rust-lang.org/
[so]: http://stackoverflow.com/questions/tagged/rust
[community-library]: https://github.com/rust-lang/rfcs/labels/A-community-library
[wd]: ./contributing.md#writing-documentation
[wa]: https://forge.rust-lang.org/compiler/working-areas.html
[triage]: ./contributing.md#issue-triage

## Cloning and Building

See ["How to build and run the compiler"](./building/how-to-build-and-run.md).

## Contributor Procedures

This section has moved to the ["Contribution Procedures"](./contributing.md) chapter.

## Other Resources

This section has moved to the ["About this guide"][more-links] chapter.

[more-links]: ./about-this-guide.md#other-places-to-find-information


---

# About this guide

This guide is meant to help document how rustc – the Rust compiler – works,
as well as to help new contributors get involved in rustc development.

There are several parts to this guide:

1. [Building and debugging `rustc`][p1]:
   Contains information that should be useful no matter how you are contributing,
   about building, debugging, profiling, etc.
1. [Contributing to Rust][p2]:
   Contains information that should be useful no matter how you are contributing,
   about procedures for contribution, using git and GitHub, stabilizing features, etc.
1. [Bootstrapping][p3]:
   Describes how the Rust compiler builds itself using previous versions, including
   an introduction to the bootstrap process and debugging methods.
1. [High-level Compiler Architecture][p4]:
   Discusses the high-level architecture of the compiler and stages of the compile process.
1. [Source Code Representation][p5]:
   Describes the process of taking raw source code from the user
   and transforming it into various forms that the compiler can work with easily.
1. [Supporting Infrastructure][p6]:
   Covers command-line argument conventions, compiler entry points like rustc_driver and
   rustc_interface, and the design and implementation of errors and lints.
1. [Analysis][p7]:
   Discusses the analyses that the compiler uses to check various properties of the code
   and inform later stages of the compile process (e.g., type checking).
1. [MIR to Binaries][p8]: How linked executable machine code is generated.
1. [Appendices][p9] at the end with useful reference information.
   There are a few of these with different information, including a glossary.

[p1]: ./building/how-to-build-and-run.html
[p2]: ./contributing.md
[p3]: ./building/bootstrapping/intro.md
[p4]: ./part-2-intro.md
[p5]: ./part-3-intro.md
[p6]: ./cli.md
[p7]: ./part-4-intro.md
[p8]: ./part-5-intro.md
[p9]: ./appendix/background.md

### Constant change

Keep in mind that `rustc` is a real production-quality product,
being worked upon continuously by a sizeable set of contributors.
As such, it has its fair share of codebase churn and technical debt.
In addition, many of the ideas discussed throughout this guide are idealized designs
that are not fully realized yet.
All this makes keeping this guide completely up to date on everything very hard!

The guide itself is of course open source as well,
and the sources are hosted on [a GitHub repository].
If you find any mistakes in the guide, please file an issue.
Even better, open a PR with a correction!

If you do contribute to the guide,
please see the corresponding [subsection on writing documentation in this guide].

[subsection on writing documentation in this guide]: contributing.md#contributing-to-rustc-dev-guide

> “‘All conditioned things are impermanent’ —
> when one sees this with wisdom, one turns away from suffering.”
> _The Dhammapada, verse 277_

## Other places to find information

This guide, the one you are currently reading,
contains information about how various parts of the compiler work,
and how to contribute to the compiler.

You might also find the following sites useful:

- [rustc API docs] -- rustdoc documentation for the compiler, devtools, and internal tools
- [Forge] -- contains documentation about Rust infrastructure, team procedures, and more
- [compiler-team] -- the home-base for the Rust compiler team, with description
  of the team procedures, active working groups, and the team calendar.
- [std-dev-guide] -- a similar guide for developing the standard library.
- [rust-analyzer book] -- documentation for the rust-analyzer.
- [The t-compiler Zulip][z]
- The [Rust Internals forum][rif], a place to ask questions and discuss Rust's internals
- The [Rust reference][rr], even though it doesn't specifically talk about
  Rust's internals, is a great resource nonetheless
- Although out of date, [Tom Lee's great blog article][tlgba] is very helpful
- The [Rust Compiler Testing Docs][rctd]
- For [@bors], [this cheat sheet][cheatsheet] is helpful
- Google is always helpful when programming.
  You can [search all Rust documentation][gsearchdocs] (the standard library,
  the compiler, the books, the references, and the guides) to quickly find
  information about the language and compiler.
- You can also use Rustdoc's built-in search feature to find documentation on
  types and functions within the crates you're looking at.
  You can also search by type signature!
  For example, searching for `* -> vec` should find all functions that return a `Vec<T>`.
  _Hint:_ Find more tips and keyboard shortcuts by typing `?` on any Rustdoc page!


[rustc dev guide]: about-this-guide.md
[gsearchdocs]: https://www.google.com/search?q=site:doc.rust-lang.org+your+query+here
[stddocs]: https://doc.rust-lang.org/std
[rif]: http://internals.rust-lang.org
[rr]: https://doc.rust-lang.org/reference/
[rustforge]: https://forge.rust-lang.org/
[tlgba]: https://tomlee.co/2014/04/a-more-detailed-tour-of-the-rust-compiler/
[ro]: https://www.rustaceans.org/
[rctd]: tests/intro.md
[cheatsheet]: https://bors.rust-lang.org/help
[Miri]: https://github.com/rust-lang/miri
[@bors]: https://github.com/rust-lang/bors
[a GitHub repository]: https://github.com/rust-lang/rustc-dev-guide/
[rustc API docs]: https://doc.rust-lang.org/nightly/nightly-rustc/rustc_middle
[Forge]: https://forge.rust-lang.org/
[compiler-team]: https://github.com/rust-lang/compiler-team/
[std-dev-guide]: https://std-dev-guide.rust-lang.org/
[rust-analyzer book]: https://rust-analyzer.github.io/book/
[z]: https://rust-lang.zulipchat.com/#narrow/stream/131828-t-compiler
