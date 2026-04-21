# Contribution procedures

## Bug reports

While bugs are unfortunate, they're a reality in software.
We can't fix what we don't know about, so please report liberally.
If you're not sure if something is a bug, feel free to open an issue anyway.

**If you believe reporting your bug publicly represents a security risk to Rust users,
please follow our [instructions for reporting security vulnerabilities][vuln]**.

[vuln]: https://www.rust-lang.org/policies/security

If you're using the nightly channel, please check if the bug exists in the
latest toolchain before filing your bug.
It might be fixed already.

If you have the chance, before reporting a bug, please [search existing issues],
as it's possible that someone else has already reported your error.
This doesn't always work, and sometimes it's hard to know what to search for, so consider this
extra credit.
We won't mind if you accidentally file a duplicate report.

Similarly, to help others who encountered the bug find your issue, consider
filing an issue with a descriptive title, which contains information that might be unique to it.
This can be the language or compiler feature used, the
conditions that trigger the bug, or part of the error message if there is any.
An example could be: **"impossible case reached" on lifetime inference for impl
Trait in return position**.

Opening an issue is as easy as following [this link][create an issue] and filling out the fields
in the appropriate provided template.

## Bug fixes or "normal" code changes

For most PRs, no special procedures are needed.
You can just [open a PR], and it will be reviewed, approved, and merged.
This includes most bug fixes, refactorings, and other user-invisible changes.
The next few sections talk about exceptions to this rule.

Also, note that it is perfectly acceptable to open WIP PRs or GitHub [Draft PRs].
Some people prefer to do this so they can get feedback along the
way or share their code with a collaborator.
Others do this so they can utilize
the CI to build and test their PR (e.g. when developing on a slow machine).

[open a PR]: #pull-requests
[Draft PRs]: https://github.blog/2019-02-14-introducing-draft-pull-requests/

## New features

Rust has strong backwards-compatibility guarantees.
Thus, new features can't just be implemented directly in stable Rust.
Instead, we have 3 release channels: stable, beta, and nightly.
See [The Rust Book] for more details on Rust’s train release model.

- **Stable**: this is the latest stable release for general usage.
- **Beta**: this is the next release (will be stable within 6 weeks).
- **Nightly**: follows the `main` branch of the repo.
  This is the only channel where unstable features are intended to be used,
  which happens via opt-in feature gates.

See [this chapter on implementing new features](./implementing-new-features.md) for more
information.

[The Rust Book]: https://doc.rust-lang.org/book/appendix-07-nightly-rust.html

### Breaking changes

Breaking changes have a [dedicated section][Breaking Changes] in the dev-guide.

### Major changes

The compiler team has a special process for large changes, whether or not they cause breakage.
This process is called a Major Change Proposal (MCP).
MCP is a relatively lightweight mechanism for getting feedback on large changes to the
compiler (as opposed to a full RFC or a design meeting with the team).

Example of things that might require MCPs include major refactorings, changes
to important types, or important changes to how the compiler does something, or
smaller user-facing changes.

**When in doubt, ask [on Zulip].
It would be a shame to put a lot of work
into a PR that ends up not getting merged!** [See this document][mcpinfo] for more info on MCPs.

[mcpinfo]: https://forge.rust-lang.org/compiler/proposals-and-stabilization.html#how-do-i-submit-an-mcp
[on Zulip]: https://rust-lang.zulipchat.com/#narrow/stream/131828-t-compiler

### Performance

Compiler performance is important.
We have put a lot of effort over the last few years into [gradually improving it][perfdash].

[perfdash]: https://perf.rust-lang.org/dashboard.html

If you suspect that your change may cause a performance regression (or
improvement), you can request a "perf run" (and your reviewer may also request one
before approving).
This is yet another bot that will compile a collection of
benchmarks on a compiler with your changes.
The numbers are reported
[here][perf], and you can see a comparison of your changes against the latest `main`.

> For an introduction to the performance of Rust code in general
> which would also be useful in rustc development, see [The Rust Performance Book].

[perf]: https://perf.rust-lang.org
[The Rust Performance Book]: https://nnethercote.github.io/perf-book/

## Pull requests

Pull requests (or PRs for short) are the primary mechanism we use to change Rust.
GitHub itself has some [great documentation][about-pull-requests] on using the Pull Request feature.
We use the ["fork and pull" model][development-models],
where contributors push changes to their personal fork and create pull requests to
bring those changes into the source repository.
We have [a chapter](git.md) on how to use Git when contributing to Rust.

> **Advice for potentially large, complex, cross-cutting and/or very domain-specific changes**
>
> The compiler reviewers on rotation usually each have areas of the compiler that they know well,
> but also have areas that they are not very familiar with. If your PR contains changes that are
> large, complex, cross-cutting and/or highly domain-specific, it becomes very difficult to find a
> suitable reviewer who is comfortable in reviewing all of the changes in such a PR. This is also
> true if the changes are not only compiler-specific but also contains changes which fall under the
> purview of reviewers from other teams, like the standard library team. [There's a bot][triagebot]
> which notifies the relevant teams and pings people who have setup specific alerts based on the
> files modified.
>
> Before making such changes, you are strongly encouraged to **discuss your proposed changes with
> the compiler team beforehand** (and with other teams that the changes would require approval
> from), and work with the compiler team to see if we can help you **break down a large potentially
> unreviewable PR into a series of smaller more individually reviewable PRs**.
>
> You can communicate with the compiler team by creating a [#t-compiler thread on Zulip][t-compiler]
> to discuss your proposed changes.
>
> Communicating with the compiler team beforehand helps in several ways:
>
> 1. It increases the likelihood of your PRs being reviewed in a timely manner.
>     - We can help you identify suitable reviewers *before* you open actual PRs, or help find
>       advisors and liaisons to help you navigate the change procedures, or help with running
>       try-jobs, perf runs and crater runs as suitable.
> 2. It helps the compiler team track your changes.
> 3. The compiler team can perform vibe checks on your changes early and often, to see if the
>    direction of the changes align with what the compiler team prefers to see.
> 4. Helps to avoid situations where you may have invested significant time and effort into large
>   changes that the compiler team might not be willing to accept, or finding out very late that the
>   changes are in a direction that the compiler team disagrees with.

[about-pull-requests]: https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/about-pull-requests
[development-models]: https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/getting-started/about-collaborative-development-models#fork-and-pull-model
[t-compiler]: https://rust-lang.zulipchat.com/#narrow/stream/131828-t-compiler
[triagebot]: https://github.com/rust-lang/rust/blob/HEAD/triagebot.toml

### Keeping your branch up-to-date

The CI in rust-lang/rust applies your patches directly against current `main`,
not against the commit your branch is based on.
This can lead to unexpected failures
if your branch is outdated, even when there are no explicit merge conflicts.

Update your branch only when needed: when you have merge conflicts, upstream CI is broken and blocking your green PR, or a maintainer requests it.
Avoid updating an already-green PR under review unless necessary.
During review, make incremental commits to address feedback.
Prefer to squash or rebase only at the end, or when a reviewer requests it.

When updating, use `git push --force-with-lease` and leave a brief comment explaining what changed.
Some repos prefer merging from `upstream/main` instead of rebasing;
follow the project's conventions.
See [keeping things up to date](git.md#keeping-things-up-to-date) for detailed instructions.

After rebasing, it's recommended to [run the relevant tests locally](tests/intro.md) to catch any issues before CI runs.

### r?

All pull requests are reviewed by another person.
We have a bot, [@rustbot], that will automatically assign a random person
to review your request based on which files you changed.

If you want to request that a specific person reviews your pull request, you
can add an `r?` to the pull request description or in a comment.
For example, if you want to ask a review by @awesome-reviewer,
add the following to the end of the pull request description:

    r? @awesome-reviewer

[@rustbot] will then assign the PR to that reviewer instead of a random person.
This is entirely optional.

You can also assign a random reviewer from a specific team by writing `r? rust-lang/groupname`.
As an example, if you were making a diagnostics change,
you could get a reviewer from the diagnostics team by adding:

    r? rust-lang/diagnostics

For a full list of possible `groupname`s,
check the `adhoc_groups` section at the [triagebot.toml config file],
or the list of teams in the [rust-lang teams database].

### Waiting for reviews

> NOTE
>
> Pull request reviewers are often working at capacity,
> and many of them are contributing on a volunteer basis.
> In order to minimize review delays,
> pull request authors and assigned reviewers should ensure that the review label
> (`S-waiting-on-review` and `S-waiting-on-author`) stays updated,
> invoking these commands when appropriate:
>
> - `@rustbot author`:
>   the review is finished,
>   and PR author should check the comments and take action accordingly.
>
> - `@rustbot review`:
>   the author is ready for a review,
>   and this PR will be queued again in the reviewer's queue.

Please note that the reviewers are humans, who for the most part work on `rustc` in their free time.
This means that they can take some time to respond and review your PR.
It also means that reviewers can miss some PRs that are assigned to them.

To try to move PRs forward, the Triage WG regularly goes through all PRs that
are waiting for review and haven't been discussed for at least 2 weeks.
If you don't get a review within 2 weeks, feel free to ask the Triage WG on
Zulip ([#t-release/triage]).
They have knowledge of when to ping, who might be on vacation, etc.

The reviewer may request some changes using the GitHub code review interface.
They may also request special procedures for some PRs.
See [Crater] and [Breaking Changes] chapters for some examples of such procedures.

[r?]: https://github.com/rust-lang/rust/pull/78133#issuecomment-712692371
[#t-release/triage]: https://rust-lang.zulipchat.com/#narrow/stream/242269-t-release.2Ftriage
[Crater]: tests/crater.md

### CI

In addition to being reviewed by a human, pull requests are automatically tested,
thanks to continuous integration (CI).
Basically, every time you open and update
a pull request, CI builds the compiler and tests it against the
[compiler test suite], and also performs other tests such as checking that
your pull request is in compliance with Rust's style guidelines.

Running continuous integration tests allows PR authors to catch mistakes early
without going through a first review cycle, and also helps reviewers stay aware
of the status of a particular pull request.

Rust has plenty of CI capacity, and you should never have to worry about wasting
computational resources each time you push a change.
It is also perfectly fine
(and even encouraged!) to use the CI to test your changes if it can help your productivity.
In particular, we don't recommend running the full `./x test` suite locally,
since it takes a very long time to execute.

### r+

After someone has reviewed your pull request, they will leave an annotation
on the pull request with an `r+`.
It will look something like this:

    @bors r+

This tells [@bors], our lovable integration bot, that your pull request has been approved.
The PR then enters the [merge queue], where [@bors]
will run *all* the tests on *every* platform we support.
If it all works out, [@bors] will merge your code into `main` and close the pull request.

Depending on the scale of the change, you may see a slightly different form of `r+`:

    @bors r+ rollup

The additional `rollup` tells [@bors] that this change should always be "rolled up".
Changes that are rolled up are tested and merged alongside other PRs, to speed the process up.
Typically, only small changes that are expected not to conflict
with one another are marked as "always roll up".

Be patient;
this can take a while and the queue can sometimes be long.
Also, note that PRs are never merged by hand.

[@rustbot]: https://github.com/rustbot
[@bors]: https://github.com/rust-lang/bors

### Opening a PR

You are now ready to file a pull request (PR)?
Great!
Here are a few points you should be aware of.

All pull requests should be filed against the `main` branch,
unless you know for sure that you should target a different branch.

Run some style checks before you submit the PR:

    ./x test tidy --bless

We recommend to make this check before every pull request (and every new commit in a pull request);
you can add [git hooks] before every push to make sure you never forget to make this check.
The CI will also run tidy and will fail if tidy fails.

Rust follows a _no merge-commit policy_,
meaning that when you encounter merge conflicts,
you are expected to always rebase instead of merging.
For example,
always use rebase when bringing the latest changes from the `main` branch to your feature branch.
If your PR contains merge commits, it will get marked as `has-merge-commits`.
Once you have removed the merge commits, e.g., through an interactive rebase, you
should remove the label again:

    @rustbot label -has-merge-commits

See [this chapter][labeling] for more details.

If you encounter merge conflicts or when a reviewer asks you to perform some
changes, your PR will get marked as `S-waiting-on-author`.
When you resolve them, you should use `@rustbot` to mark it as `S-waiting-on-review`:

    @rustbot ready

GitHub allows [closing issues using keywords][closing-keywords].
This feature should be used to keep the issue tracker tidy.
However, it is generally preferred
to put the "closes #123" text in the PR description rather than the commit message;
particularly during rebasing, citing the issue number in the commit can "spam"
the issue in question.

However, if your PR fixes a stable-to-beta or stable-to-stable regression and has
been accepted for a beta and/or stable backport (i.e., it is marked `beta-accepted`
and/or `stable-accepted`), please do *not* use any such keywords since we don't
want the corresponding issue to get auto-closed once the fix lands on `main`.
Please update the PR description while still mentioning the issue somewhere.
For example, you could write `Fixes (after beta backport) #NNN.`.

As for further actions, please keep a sharp look-out for a PR whose title begins with
`[beta]` or `[stable]` and which backports the PR in question.
When that one gets merged, the relevant issue can be closed.
The closing comment should mention all PRs that were involved.
If you don't have the permissions to close the issue, please
leave a comment on the original PR asking the reviewer to close it for you.

[labeling]: ./rustbot.md#issue-relabeling
[closing-keywords]: https://docs.github.com/en/issues/tracking-your-work-with-issues/linking-a-pull-request-to-an-issue

### Reverting a PR

When a PR leads to miscompile, significant performance regressions, or other critical issues, we may
want to revert that PR with a regression test case.
You can also check out the [revert policy] on
Forge docs (which is mainly targeted for reviewers, but contains useful info for PR authors too).

If the PR contains huge changes, it can be challenging to revert, making it harder to review
incremental fixes in subsequent updates.
Or if certain code in that PR is heavily depended upon by
subsequent PRs, reverting it can become difficult.

In such cases, we can identify the problematic code and disable it for some input, as shown in [#128271][#128271].

For MIR optimizations, we can also use the `-Zunsound-mir-opt` option to gate the mir-opt, as shown
in [#132356][#132356].

[revert policy]: https://forge.rust-lang.org/compiler/reviews.html?highlight=revert#reverts
[#128271]: https://github.com/rust-lang/rust/pull/128271
[#132356]: https://github.com/rust-lang/rust/pull/132356

## External dependencies

This section has moved to ["Using External Repositories"](./external-repos.md).

## Writing documentation

Documentation improvements are very welcome.
The source of `doc.rust-lang.org`
is located in [`src/doc`] in the tree, and standard API documentation is generated
from the source code itself (e.g. [`library/std/src/lib.rs`][std-root]). Documentation pull requests
function in the same way as other pull requests.

[`src/doc`]: https://github.com/rust-lang/rust/tree/HEAD/src/doc
[std-root]: https://github.com/rust-lang/rust/blob/HEAD/library/std/src/lib.rs#L1

To find documentation-related issues, use the [A-docs label].

You can find documentation style guidelines in [RFC 1574].

To build the standard library documentation, use `x doc --stage 1 library --open`.
To build the documentation for a book (e.g. the unstable book), use `x doc src/doc/unstable-book.`
Results should appear in `build/host/doc`, as well as automatically open in your default browser.
See [Building Documentation](./building/compiler-documenting.md#building-documentation) for more
information.

You can also use `rustdoc` directly to check small fixes.
For example, `rustdoc src/doc/reference.md` will render reference to `doc/reference.html`.
The CSS might be messed up, but you can verify that the HTML is right.

Please notice that we don't accept typography/spellcheck fixes to **internal documentation**
as it's usually not worth the churn or the review time.
Examples of internal documentation is code comments and rustc api docs.
However, feel free to fix those if accompanied by other improvements in the same PR.

### Contributing to rustc-dev-guide

Contributions to the [rustc-dev-guide] are always welcome, and can be made directly at
[the rust-lang/rustc-dev-guide repo][rdgrepo].
The issue tracker in that repo is also a great way to find things that need doing.
There are issues for beginners and advanced compiler devs alike!

Just a few things to keep in mind:

- Please try to avoid overly long lines and use semantic line breaks (where you break the line after each sentence).
  There is no strict limit on line lengths;
  let the sentence or part of the sentence flow to its proper end on the same line.

  You can use a tool in ci/sembr to help with this.
  Its help output can be seen with this command:

  ```console
  cargo run --manifest-path ci/sembr/Cargo.toml -- --help
  ```

- When contributing text to the guide, please contextualize the information with some time period
  and/or a reason so that the reader knows how much to trust the information.
  Aim to provide a reasonable amount of context, possibly including but not limited to:

  - A reason for why the text may be out of date other than "change",
    as change is a constant across the project.

  - The date the comment was added, e.g. instead of writing _"Currently, ..."_
    or _"As of now, ..."_, consider adding the date, in one of the following formats:
    - Jan 2021
    - January 2021
    - jan 2021
    - january 2021

    There is a CI action (in `.github/workflows/date-check.yml`)
    that generates a monthly report showing those that are over 6 months old
    ([example](https://github.com/rust-lang/rustc-dev-guide/issues/2052)).

    For the action to pick the date, add a special annotation before specifying the date:

    ```md
    <!-- date-check --> Nov 2025
    ```

    Example:

    ```md
    As of <!-- date-check --> Nov 2025, the foo did the bar.
    ```

    For cases where the date should not be part of the visible rendered output,
    use the following instead:

    ```md
    <!-- date-check: Nov 2025 -->
    ```

  - A link to a relevant WG, tracking issue, `rustc` rustdoc page, or similar, that may provide
    further explanation for the change process or a way to verify that the information is not
    outdated.

- If a text grows rather long (more than a few page scrolls) or complicated (more than four
  subsections), it might benefit from having a Table of Contents at the beginning,
  which you can auto-generate by including the `<!-- toc -->` marker at the top.

#### ⚠️ Note: Where to contribute `rustc-dev-guide` changes

For detailed information about where to contribute rustc-dev-guide changes and the benefits of doing so,
see [the rustc-dev-guide team documentation].

## Issue triage

Please see <https://forge.rust-lang.org/release/issue-triaging.html>.

[stable-]: https://github.com/rust-lang/rust/labels?q=stable
[beta-]: https://github.com/rust-lang/rust/labels?q=beta
[I-\*-nominated]: https://github.com/rust-lang/rust/labels?q=nominated
[I-prioritize]: https://github.com/rust-lang/rust/labels/I-prioritize
[tracking issues]: https://github.com/rust-lang/rust/labels/C-tracking-issue
[beta-backport]: https://forge.rust-lang.org/release/backporting.html#beta-backporting-in-rust-langrust
[stable-backport]: https://forge.rust-lang.org/release/backporting.html#stable-backporting-in-rust-langrust
[metabug]: https://github.com/rust-lang/rust/labels/metabug
[regression-]: https://github.com/rust-lang/rust/labels?q=regression
[relnotes]: https://github.com/rust-lang/rust/labels/relnotes
[S-tracking-]: https://github.com/rust-lang/rust/labels?q=s-tracking
[the rustc-dev-guide team documentation]: https://forge.rust-lang.org/rustc-dev-guide/index.html#where-to-contribute-rustc-dev-guide-changes

### rfcbot labels

[rfcbot] uses its own labels for tracking the process of coordinating
asynchronous decisions, such as approving or rejecting a change.
This is used for [RFCs], issues, and pull requests.

| Labels | Color | Description |
|--------|-------|-------------|
| [proposed-final-comment-period] | <span class="label-color" style="background-color:#ededed;">&#x2003;</span>&nbsp;Gray | Currently awaiting signoff of all team members in order to enter the final comment period. |
| [disposition-merge] | <span class="label-color" style="background-color:#008800;">&#x2003;</span>&nbsp;Green | Indicates the intent is to merge the change. |
| [disposition-close] | <span class="label-color" style="background-color:#dd0000;">&#x2003;</span>&nbsp;Red | Indicates the intent is to not accept the change and close it. |
| [disposition-postpone] | <span class="label-color" style="background-color:#ededed;">&#x2003;</span>&nbsp;Gray | Indicates the intent is to not accept the change at this time and postpone it to a later date. |
| [final-comment-period] | <span class="label-color" style="background-color:#1e76d9;">&#x2003;</span>&nbsp;Blue | Currently soliciting final comments before merging or closing. |
| [finished-final-comment-period] | <span class="label-color" style="background-color:#f9e189;">&#x2003;</span>&nbsp;Light Yellow | The final comment period has concluded, and the issue will be merged or closed. |
| [postponed] | <span class="label-color" style="background-color:#fbca04;">&#x2003;</span>&nbsp;Yellow | The issue has been postponed. |
| [closed] | <span class="label-color" style="background-color:#dd0000;">&#x2003;</span>&nbsp;Red | The issue has been rejected. |
| [to-announce] | <span class="label-color" style="background-color:#ededed;">&#x2003;</span>&nbsp;Gray | Issues that have finished their final-comment-period and should be publicly announced. Note: the rust-lang/rust repository uses this label differently, to announce issues at the triage meetings. |

[disposition-merge]: https://github.com/rust-lang/rust/labels/disposition-merge
[disposition-close]: https://github.com/rust-lang/rust/labels/disposition-close
[disposition-postpone]: https://github.com/rust-lang/rust/labels/disposition-postpone
[proposed-final-comment-period]: https://github.com/rust-lang/rust/labels/proposed-final-comment-period
[final-comment-period]: https://github.com/rust-lang/rust/labels/final-comment-period
[finished-final-comment-period]: https://github.com/rust-lang/rust/labels/finished-final-comment-period
[postponed]: https://github.com/rust-lang/rfcs/labels/postponed
[closed]: https://github.com/rust-lang/rfcs/labels/closed
[to-announce]: https://github.com/rust-lang/rfcs/labels/to-announce
[rfcbot]: https://github.com/anp/rfcbot-rs/
[RFCs]: https://github.com/rust-lang/rfcs

## Helpful links and information

This section has moved to the ["About this guide"] chapter.

["About this guide"]: about-this-guide.md#other-places-to-find-information
[search existing issues]: https://github.com/rust-lang/rust/issues?q=is%3Aissue
[Breaking Changes]: bug-fix-procedure.md
[triagebot.toml config file]: https://github.com/rust-lang/rust/blob/HEAD/triagebot.toml
[rust-lang teams database]: https://github.com/rust-lang/team/tree/HEAD/teams
[compiler test suite]: tests/intro.md
[merge queue]: https://bors.rust-lang.org/queue/rust
[git hooks]: https://git-scm.com/book/en/v2/Customizing-Git-Git-Hooks
[A-docs label]: https://github.com/rust-lang/rust/issues?q=is%3Aopen%20is%3Aissue%20label%3AA-docs
[RFC 1574]: https://github.com/rust-lang/rfcs/blob/master/text/1574-more-api-documentation-conventions.md#appendix-a-full-conventions-text
[rustc-dev-guide]: https://rustc-dev-guide.rust-lang.org/
[rdgrepo]: https://github.com/rust-lang/rustc-dev-guide
[create an issue]: https://github.com/rust-lang/rust/issues/new/choose


---

# About the compiler team

> NOTE:
> There exists much detail about the team [on Forge], making most of the following obsolete.

rustc is maintained by the [Rust compiler team][team].
The people who belong to
this team collectively work to track regressions and implement new features.
Members of the Rust compiler team are people who have made significant
contributions to rustc and its design.

[on Forge]: https://forge.rust-lang.org/compiler
[team]: https://www.rust-lang.org/governance/teams/compiler

## Discussion

Currently the compiler team chats in Zulip:

- Team chat occurs in the [`t-compiler`][zulip-t-compiler] stream on the Zulip instance
- There are also a number of other associated Zulip channels,
  such as [`t-compiler/help`][zulip-help], where people can ask for help
  with rustc development, or [`t-compiler/meetings`][zulip-meetings],
  where the team holds their weekly triage and steering meetings.

## Reviewers

If you're interested in figuring out who can answer questions about a
particular part of the compiler, or you'd just like to know who works on what,
check out [triagebot.toml's assign section][map].
It contains a listing of the various parts of the compiler and a list of people
who are reviewers of each part.

[map]: https://github.com/rust-lang/rust/blob/HEAD/triagebot.toml

## Rust compiler meeting

The compiler team has a weekly meeting where we do triage and try to
generally stay on top of new bugs, regressions, and discuss important things in general.
They are held on [Zulip][zulip-meetings].
It works roughly as follows:

- **Announcements, MCPs/FCPs, and WG-check-ins:** We share some
  announcements with the rest of the team about important things we want everyone to be aware of.
  We also share the status of MCPs and FCPs and we
  use the opportunity to have a couple of WGs giving us an update about their work.
- **Check for beta and stable nominations:** These are nominations of things to
  backport to beta and stable respectively.
  We then look for new cases where the compiler broke previously working code in the wild.
  Regressions are important issues to fix, so it's
  likely that they are tagged as P-critical or P-high; the major
  exception would be bug fixes (though even there we often [aim to give
  warnings first][procedure]).
- **Review P-critical and P-high bugs:** P-critical and P-high bugs are
  those that are sufficiently important for us to actively track progress.
  P-critical and P-high bugs should ideally always have an assignee.
- **Check `S-waiting-on-t-compiler` and `I-compiler-nominated` issues:** These are issues where
  feedback from the team is desired.
- **Look over the performance triage report:** We check for PRs that made the
    performance worse and try to decide if it's worth reverting the performance regression or if
    the regression can be addressed in a future PR.

The meeting currently takes place on Thursdays at 10am Boston time
(UTC-4 typically, but daylight savings time sometimes makes things complicated).

[procedure]: ./bug-fix-procedure.md
[zulip-t-compiler]: https://rust-lang.zulipchat.com/#narrow/stream/131828-t-compiler
[zulip-help]: https://rust-lang.zulipchat.com/#narrow/stream/182449-t-compiler.2Fhelp
[zulip-meetings]: https://rust-lang.zulipchat.com/#narrow/stream/238009-t-compiler.2Fmeetings

## Team membership

Membership in the Rust team is typically offered when someone has been
making significant contributions to the compiler for some time.
Membership is both a recognition but also an obligation:
compiler team members are generally expected to help with upkeep as
well as doing reviews and other work.

If you are interested in becoming a compiler team member, the first
thing to do is to start fixing some bugs, or get involved in a working group.
One good way to find bugs is to look for
[open issues tagged with E-easy](https://github.com/rust-lang/rust/issues?q=is%3Aopen+is%3Aissue+label%3AE-easy)
or [E-mentor](https://github.com/rust-lang/rust/issues?q=is%3Aopen+is%3Aissue+label%3AE-mentor).

You can also dig through the graveyard of PRs that were
[closed due to inactivity](https://github.com/rust-lang/rust/pulls?q=is%3Apr+label%3AS-inactive),
some of them may contain work that is still useful - refer to the
associated issues, if any - and only needs some finishing touches
for which the original author didn't have time.

### r+ rights

Once you have made a number of individual PRs to rustc, we will often offer r+ privileges.
This means that you have the right to instruct
"bors" (the robot that manages which PRs get landed into rustc) to merge a PR
([here are some instructions for how to talk to bors][bors-guide]).

[bors-guide]: https://bors.rust-lang.org/

The guidelines for reviewers are as follows:

- You are always welcome to review any PR, regardless of who it is assigned to.
  However, do not r+ PRs unless:
  - You are confident in that part of the code.
  - You are confident that nobody else wants to review it first.
    - For example, sometimes people will express a desire to review a
      PR before it lands, perhaps because it touches a particularly
      sensitive part of the code.
- Always be polite when reviewing: you are a representative of the
  Rust project, so it is expected that you will go above and beyond
  when it comes to the [Code of Conduct].

[Code of Conduct]: https://www.rust-lang.org/policies/code-of-conduct

### Reviewer rotation

Once you have r+ rights, you can also be added to the [reviewer rotation].
[triagebot] is the bot that [automatically assigns] incoming PRs to reviewers.
If you are added, you will be randomly selected to review PRs.
If you find you are assigned a PR that you don't feel comfortable
reviewing, you can also leave a comment like `r? @so-and-so` to assign
to someone else — if you don't know who to request, just write `r?
@nikomatsakis for reassignment` and @nikomatsakis will pick someone for you.

[reviewer rotation]: https://github.com/rust-lang/rust/blob/36285c5de8915ecc00d91ae0baa79a87ed5858d5/triagebot.toml#L528-L577
[triagebot]: https://github.com/rust-lang/triagebot/
[automatically assigns]: https://forge.rust-lang.org/triagebot/pr-assignment.html

Getting on the reviewer rotation is much appreciated as it lowers the review burden for all of us!
However, if you don't have time to give
people timely feedback on their PRs, it may be better that you don't get on the list.


---

# Using Git

The Rust project uses [Git] to manage its source code.
In order to contribute, you'll need some familiarity with its features so that your changes
can be incorporated into the compiler.

[Git]: https://git-scm.com

The goal of this page is to cover some of the more common questions and
problems new contributors face.
Although some Git basics will be covered here,
if you find that this is still a little too fast for you, it might make sense
to first read some introductions to Git, such as the Beginner and Getting
started sections of [this tutorial from Atlassian][atlassian-git].
GitHub also provides [documentation] and [guides] for beginners, or you can consult the
more in depth [book from Git].

This guide is incomplete.
If you run into trouble with git that this page doesn't help with,
please [open an issue] so we can document how to fix it.

[open an issue]: https://github.com/rust-lang/rustc-dev-guide/issues/new
[book from Git]: https://git-scm.com/book/en/v2/
[atlassian-git]: https://www.atlassian.com/git/tutorials/what-is-version-control
[documentation]: https://docs.github.com/en/get-started/quickstart/set-up-git
[guides]: https://guides.github.com/introduction/git-handbook/

## Prerequisites

We'll assume that you've installed Git, forked [rust-lang/rust], and cloned the
forked repo to your PC.
We'll use the command line interface to interact
with Git; there are also a number of GUIs and IDE integrations that can
generally do the same things.

[rust-lang/rust]: https://github.com/rust-lang/rust

If you've cloned your fork, then you will be able to reference it with `origin` in your local repo.
It may be helpful to also set up a remote for the official rust-lang/rust repo via

```console
git remote add upstream https://github.com/rust-lang/rust.git
```

if you're using HTTPS, or

```console
git remote add upstream git@github.com:rust-lang/rust.git
```

if you're using SSH.

**NOTE:** This page is dedicated to workflows for `rust-lang/rust`, but will likely be
useful when contributing to other repositories in the Rust project.


## Standard Process

Below is the normal procedure that you're likely to use for most minor changes and PRs:

 1. Ensure that you're making your changes on top of `main`: `git checkout main`.
 2. Get the latest changes from the Rust repo: `git pull upstream main --ff-only`.
 (see [No-Merge Policy][no-merge-policy] for more info about this).
 3. Make a new branch for your change: `git checkout -b issue-12345-fix`.
 4. Make some changes to the repo and test them.
 5. Stage your changes via `git add src/changed/file.rs src/another/change.rs`
 and then commit them with `git commit`.
 Of course, making intermediate commits may be a good idea as well.
 Avoid `git add .`, as it makes it too easy to
 unintentionally commit changes that should not be committed, such as submodule updates.
 You can use `git status` to check if there are any files you forgot to stage.
 6. Push your changes to your fork: `git push --set-upstream origin issue-12345-fix`
 (After adding commits, you can use `git push` and after rebasing or
pulling-and-rebasing, you can use `git push --force-with-lease`).
 7. [Open a PR][ghpullrequest] from your fork to `rust-lang/rust`'s `main` branch.

[ghpullrequest]: https://guides.github.com/activities/forking/#making-a-pull-request

If you end up needing to rebase and are hitting conflicts, see [Rebasing](#rebasing).
If you want to track upstream while working on long-running feature/issue, see
[Keeping things up to date][no-merge-policy].

If your reviewer requests changes, the procedure for those changes looks much
the same, with some steps skipped:

 1. Ensure that you're making changes to the most recent version of your code:
 `git checkout issue-12345-fix`.
 2. Make, stage, and commit your additional changes just like before.
 3. Push those changes to your fork: `git push`.

 [no-merge-policy]: #keeping-things-up-to-date

## Troubleshooting git issues

You don't need to clone `rust-lang/rust` from scratch if it's out of date!
Even if you think you've messed it up beyond repair, there are ways to fix
the git state that don't require downloading the whole repository again.
Here are some common issues you might run into:

### I made a merge commit by accident.

Git has two ways to update your branch with the newest changes: merging and rebasing.
Rust [uses rebasing][no-merge-policy].
If you make a merge commit, it's not too hard to fix: `git rebase -i upstream/main`.

See [Rebasing](#rebasing) for more about rebasing.

### I deleted my fork on GitHub!

This is not a problem from git's perspective.
If you run `git remote -v`,
it will say something like this:

```console
$ git remote -v
origin  git@github.com:jyn514/rust.git (fetch)
origin  git@github.com:jyn514/rust.git (push)
upstream        https://github.com/rust-lang/rust (fetch)
upstream        https://github.com/rust-lang/rust (fetch)
```

If you renamed your fork, you can change the URL like this:

```console
git remote set-url origin <URL>
```

where the `<URL>` is your new fork.

### I changed a submodule by accident

Usually people notice this when rustbot posts a comment on github that `cargo` has been modified:

![rustbot submodule comment](./img/rustbot-submodules.png)

You might also notice conflicts in the web UI:

![conflict in src/tools/cargo](./img/submodule-conflicts.png)

The most common cause is that you rebased after a change and ran `git add .` without first running
`x` to update the submodules.
 Alternatively, you might have run `cargo fmt` instead of `x fmt`
and modified files in a submodule, then committed the changes.

To fix it, do the following things (if you changed a submodule other than cargo,
replace `src/tools/cargo` with the path to that submodule):

1. See which commit has the accidental changes: `git log --stat -n1 src/tools/cargo`
2. Revert the changes to that commit: `git checkout <my-commit>~ src/tools/cargo`.
   Type `~` literally but replace `<my-commit>` with the output from step 1.
3. Tell git to commit the changes: `git commit --fixup <my-commit>`
4. Repeat steps 1-3 for all the submodules you modified.
    - If you modified the submodule in several different commits, you will need to repeat steps 1-3
    for each commit you modified.
    You'll know when to stop when the `git log` command shows a commit
    that's not authored by you.
5. Squash your changes into the existing commits: `git rebase --autosquash -i upstream/main`
6. [Push your changes](#standard-process).

### I see "error: cannot rebase" when I try to rebase

These are two common errors to see when rebasing:
```console
error: cannot rebase: Your index contains uncommitted changes.
error: Please commit or stash them.
```
```console
error: cannot rebase: You have unstaged changes.
error: Please commit or stash them.
```

(See <https://git-scm.com/book/en/v2/Getting-Started-What-is-Git%3F#_the_three_states> for the difference between the two.)

This means you have made changes since the last time you made a commit.
To be able to rebase, either
commit your changes, or make a temporary commit called a "stash" to have them still not be committed
when you finish rebasing.
You may want to configure git to make this "stash" automatically, which
will prevent the "cannot rebase" error in nearly all cases:

```console
git config --global rebase.autostash true
```

See <https://git-scm.com/book/en/v2/Git-Tools-Stashing-and-Cleaning> for more info about stashing.

### I see 'Untracked Files: src/stdarch'?

This is left over from the move to the `library/` directory.
Unfortunately, `git rebase` does not follow renames for submodules, so you
have to delete the directory yourself:

```console
rm -r src/stdarch
```

### I see `<<< HEAD`?

You were probably in the middle of a rebase or merge conflict.
See [Conflicts](#rebasing-and-conflicts) for how to fix the conflict.
If you don't care about the changes
and just want to get a clean copy of the repository back, you can use `git reset`:

```console
# WARNING: this throws out any local changes you've made! Consider resolving the conflicts instead.
git reset --hard main
```

### failed to push some refs

`git push` will not work properly and say something like this:

```console
 ! [rejected]        issue-xxxxx -> issue-xxxxx (non-fast-forward)
error: failed to push some refs to 'https://github.com/username/rust.git'
hint: Updates were rejected because the tip of your current branch is behind
hint: its remote counterpart. Integrate the remote changes (e.g.
hint: 'git pull ...') before pushing again.
hint: See the 'Note about fast-forwards' in 'git push --help' for details.
```

The advice this gives is incorrect!
Because of Rust's ["no-merge" policy](#no-merge-policy), the merge commit created by `git pull`
will not be allowed in the final PR, in addition to defeating the point of the rebase!
Use `git push --force-with-lease` instead.

### Git is trying to rebase commits I didn't write?

If you see many commits in your rebase list, or merge commits, or commits by other people that you
didn't write, it likely means you're trying to rebase over the wrong branch.
For example, you may
have a `rust-lang/rust` remote `upstream`, but ran `git rebase origin/main` instead of `git rebase
upstream/main`.
The fix is to abort the rebase and use the correct branch instead:

```console
git rebase --abort
git rebase --interactive upstream/main
```

<details><summary>Click here to see an example of rebasing over the wrong branch</summary>

![Interactive rebase over the wrong branch](img/other-peoples-commits.png)

</details>

### Quick note about submodules

When updating your local repository with `git pull`, you may notice that sometimes
Git says you have modified some files that you have never edited.
For example,
running `git status` gives you something like (note the `new commits` mention):

```console
On branch main
Your branch is up to date with 'origin/main'.

Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
	modified:   src/llvm-project (new commits)
	modified:   src/tools/cargo (new commits)

no changes added to commit (use "git add" and/or "git commit -a")
```

These changes are not changes to files: they are changes to submodules (more on this [later](#git-submodules)).
To get rid of those:

```console
git submodule update
```

Some submodules are not actually needed; for example, `src/llvm-project` doesn't need to be checked
out if you're using `download-ci-llvm`.
 To avoid having to keep fetching its history, you can use
`git submodule deinit -f src/llvm-project`, which will also avoid it showing as modified again.

## Rebasing and Conflicts

When you edit your code locally, you are making changes to the version of
rust-lang/rust that existed when you created your feature branch.
As such, when you submit your PR, it is possible that some of the changes that have been made
to rust-lang/rust since then are in conflict with the changes you've made.
When this happens, you need to resolve the conflicts before your changes can be merged.
To do that, you need to rebase your work on top of rust-lang/rust.

### Rebasing

To rebase your feature branch on top of the newest version of the `main` branch
of rust-lang/rust, checkout your branch, and then run this command:

```console
git pull --rebase https://github.com/rust-lang/rust.git main
```

> If you are met with the following error:
> ```console
> error: cannot pull with rebase: Your index contains uncommitted changes.
> error: please commit or stash them.
> ```
> it means that you have some uncommitted work in your working tree. In that
> case, run `git stash` before rebasing, and then `git stash pop` after you
> have rebased and fixed all conflicts.

When you rebase a branch on main, all the changes on your branch are
reapplied to the most recent version of `main`.
In other words, Git tries to
pretend that the changes you made to the old version of `main` were instead
made to the new version of `main`.
During this process, you should expect to encounter at least one "rebase conflict".
This happens when Git's attempt to
reapply the changes fails because your changes conflicted with other changes that have been made.
You can tell that this happened because you'll see lines in the output that look like

```console
CONFLICT (content): Merge conflict in file.rs
```

When you open these files, you'll see sections of the form

```console
<<<<<<< HEAD
Original code
=======
Your code
>>>>>>> 8fbf656... Commit fixes 12345
```

This represents the lines in the file that Git could not figure out how to rebase.
The section between `<<<<<<< HEAD` and `=======` has the code from
`main`, while the other side has your version of the code.
You'll need to decide how to deal with the conflict.
You may want to keep your changes,
keep the changes on `main`, or combine the two.

Generally, resolving the conflict consists of two steps: First, fix the particular conflict.
Edit the file to make the changes you want and remove the
`<<<<<<<`, `=======` and `>>>>>>>` lines in the process.
Second, check the surrounding code.
If there was a conflict, its likely there are some logical errors lying around too!
It's a good idea to run `x check` here to make sure there are no glaring errors.

Once you're all done fixing the conflicts, you need to stage the files that had
conflicts in them via `git add`.
Afterwards, run `git rebase --continue` to let
Git know that you've resolved the conflicts and it should finish the rebase.

Once the rebase has succeeded, you'll want to update the associated branch on
your fork with `git push --force-with-lease`.

### Keeping things up to date

The [above section](#rebasing) is a specific
guide on rebasing work and dealing with merge conflicts.
Here is some general advice about how to keep your local repo up-to-date with upstream changes:

Using `git pull upstream main` while on your local `main` branch regularly will keep it up-to-date.
You will also want to keep your feature branches up-to-date as well.
After pulling, you can checkout the feature branches and rebase them:

```console
git checkout main
git pull upstream main --ff-only # to make certain there are no merge commits
git rebase main feature_branch
git push --force-with-lease # (set origin to be the same as local)
```

To avoid merges as per the [No-Merge Policy](#no-merge-policy), you may want to use
`git config pull.ff only` (this will apply the config only to the local repo)
to ensure that Git doesn't create merge commits when `git pull`ing, without
needing to pass `--ff-only` or `--rebase` every time.

You can also `git push --force-with-lease` from main to double-check that your
feature branches are in sync with their state on the GitHub side.

## Advanced Rebasing

### Squash your commits

"Squashing" commits into each other causes them to be merged into a single commit.
Both the upside and downside of this is that it simplifies the history.
On the one hand, you lose track of the steps in which changes were made, but
the history becomes easier to work with.

The easiest way to squash your commits in a PR on the `rust-lang/rust` repository is to use the `@bors squash` command in a comment on the PR.
By default, [bors] combines all commit messages of the PR into the squashed commit message.
To customize the commit message, use `@bors squash msg="<commit message>"`.
For example, `@bors squash msg="Improve diagnostics for missing lifetime parameter"`.

If you want to squash commits using local git operations, read on below.

If there are no conflicts and you are just squashing to clean up the history,
use `git rebase --interactive --keep-base main`.
This keeps the fork point of your PR the same, making it easier to review the diff of what happened
across your rebases.

Squashing can also be useful as part of conflict resolution.
If your branch contains multiple consecutive rewrites of the same code, or if
the rebase conflicts are extremely severe, you can use
`git rebase --interactive main` to gain more control over the process.
This allows you to choose to skip commits, edit the commits that you do not skip,
change the order in which they are applied, or "squash" them into each other.

Alternatively, you can sacrifice the commit history like this:

```console
# squash all the changes into one commit so you only have to worry about conflicts once
git rebase --interactive --keep-base main  # and squash all changes along the way
git rebase main
# fix all merge conflicts
git rebase --continue
```

You also may want to squash just the last few commits together, possibly
because they only represent "fixups" and not real changes.
For example,
`git rebase --interactive HEAD~2` will allow you to edit the two commits only.

[bors]: https://github.com/rust-lang/bors

### `git range-diff`

After completing a rebase, and before pushing up your changes, you may want to
review the changes between your old branch and your new one.
You can do that with `git range-diff main @{upstream} HEAD`.

The first argument to `range-diff`, `main` in this case, is the base revision
that you're comparing your old and new branch against.
The second argument is
the old version of your branch; in this case, `@upstream` means the version that
you've pushed to GitHub, which is the same as what people will see in your pull request.
Finally, the third argument to `range-diff` is the *new* version of
your branch; in this case, it is `HEAD`, which is the commit that is currently
checked-out in your local repo.

Note that you can also use the equivalent, abbreviated form `git range-diff main @{u} HEAD`.

Unlike in regular Git diffs, you'll see a `-` or `+` next to another `-` or `+`
in the range-diff output.
The marker on the left indicates a change between the
old branch and the new branch, and the marker on the right indicates a change you've committed.
So, you can think of a range-diff as a "diff of diffs" since
it shows you the differences between your old diff and your new diff.

Here's an example of `git range-diff` output (taken from [Git's docs][range-diff-example-docs]):

```console
-:  ------- > 1:  0ddba11 Prepare for the inevitable!
1:  c0debee = 2:  cab005e Add a helpful message at the start
2:  f00dbal ! 3:  decafe1 Describe a bug
    @@ -1,3 +1,3 @@
     Author: A U Thor <author@example.com>

    -TODO: Describe a bug
    +Describe a bug
    @@ -324,5 +324,6
      This is expected.

    -+What is unexpected is that it will also crash.
    ++Unexpectedly, it also crashes. This is a bug, and the jury is
    ++still out there how to fix it best. See ticket #314 for details.

      Contact
3:  bedead < -:  ------- TO-UNDO
```

(Note that `git range-diff` output in your terminal will probably be easier to
read than in this example because it will have colors.)

Another feature of `git range-diff` is that, unlike `git diff`, it will also diff commit messages.
This feature can be useful when amending several commit
messages so you can make sure you changed the right parts.

`git range-diff` is a very useful command, but note that it can take some time
to get used to its output format.
You may also find Git's documentation on the
command useful, especially their ["Examples" section][range-diff-example-docs].

[range-diff-example-docs]: https://git-scm.com/docs/git-range-diff#_examples

## No-Merge Policy

The rust-lang/rust repo uses what is known as a "rebase workflow".
This means that merge commits in PRs are not accepted.
As a result, if you are running
`git merge` locally, chances are good that you should be rebasing instead.
Of course, this is not always true; if your merge will just be a fast-forward,
like the merges that `git pull` usually performs, then no merge commit is
created and you have nothing to worry about.
Running `git config merge.ff only` (this will apply the config to the local repo)
once will ensure that all the merges you perform are of this type, so that you
cannot make a mistake.

There are a number of reasons for this decision, and like all others, it is a tradeoff.
The main advantage is the generally linear commit history.
This greatly simplifies bisecting and makes the history and commit log much easier
to follow and understand.

## Tips for reviewing

**NOTE**: This section is for *reviewing* PRs, not authoring them.

### Hiding whitespace

GitHub has a button for disabling whitespace changes that may be useful.
You can also use `git diff -w origin/main` to view changes locally.

![hide whitespace](./img/github-whitespace-changes.png)

### Fetching PRs

To checkout PRs locally, you can use `git fetch upstream pull/NNNNN/head && git checkout
FETCH_HEAD`.

You can also use github's cli tool.
GitHub shows a button on PRs where you can copy-paste the command to check it out locally.
See <https://cli.github.com/> for more info.

![`gh` suggestion](./img/github-cli.png)

### Using GitHub dev

As an alternative to the GitHub web UI, GitHub Dev provides a web-based editor for browsing
repository and PRs.
It can be opened by replacing `github.com` with `github.dev` in the URL
or by pressing `.` on a GitHub page.
See [the docs for github.dev editor](https://docs.github.com/en/codespaces/the-githubdev-web-based-editor)
for more details.

### Moving large sections of code

Git and GitHub's default diff view for large moves *within* a file is quite poor; it will show each
line as deleted and each line as added, forcing you to compare each line yourself.
Git has an option to show moved lines in a different color:

```console
git log -p --color-moved=dimmed-zebra --color-moved-ws=allow-indentation-change
```

See [the docs for `--color-moved`](https://git-scm.com/docs/git-diff#Documentation/git-diff.txt---color-movedltmodegt) for more info.

### range-diff

See [the relevant section for PR authors](#git-range-diff).
This can be useful for comparing code
that was force-pushed to make sure there are no unexpected changes.

### Ignoring changes to specific files

Many large files in the repo are autogenerated.
To view a diff that ignores changes to those files,
you can use the following syntax (e.g. Cargo.lock):

```console
git log -p ':!Cargo.lock'
```

Arbitrary patterns are supported (e.g. `:!compiler/*`). Patterns use the same syntax as
`.gitignore`, with `:` prepended to indicate a pattern.

## Git submodules

**NOTE**: submodules are a nice thing to know about, but it *isn't* an absolute
prerequisite to contribute to `rustc`.
If you are using Git for the first time,
you might want to get used to the main concepts of Git before reading this section.

The `rust-lang/rust` repository uses [Git submodules] as a way to use other
Rust projects from within the `rust` repo.
Examples include Rust's fork of
`llvm-project`, `cargo`, and libraries like `stdarch` and `backtrace`.

Those projects are developed and maintained in a separate Git (and GitHub)
repository, and they have their own Git history/commits, issue tracker and PRs.
Submodules allow us to create some sort of embedded sub-repository inside the
`rust` repository and use them like they were directories in the `rust` repository.

Take `llvm-project` for example.
`llvm-project` is maintained in the [`rust-lang/llvm-project`]
repository, but it is used in `rust-lang/rust` by the compiler for code generation and optimization.
We bring it in `rust` as a submodule, in the `src/llvm-project` folder.

The contents of submodules are ignored by Git: submodules are in some sense isolated
from the rest of the repository.
However, if you try to `cd src/llvm-project` and then run `git status`:

```console
HEAD detached at 9567f08afc943
nothing to commit, working tree clean
```

As far as git is concerned, you are no longer in the `rust` repo, but in the `llvm-project` repo.
You will notice that we are in "detached HEAD" state, i.e. not on a branch but on a
particular commit.

This is because, like any dependency, we want to be able to control which version to use.
Submodules allow us to do just that: every submodule is "pinned" to a certain
commit, which doesn't change unless modified manually.
If you use `git checkout <commit>`
in the `llvm-project` directory and go back to the `rust` directory, you can stage this
change like any other, e.g. by running `git add src/llvm-project`. (Note that if
you *don't* stage the change to commit, then you run the risk that running
`x` will just undo your change by switching back to the previous commit when
it automatically "updates" the submodules.)

This version selection is usually done by the maintainers of the project, and
looks like [this][llvm-update].

Git submodules take some time to get used to, so don't worry if it isn't perfectly clear yet.
You will rarely have to use them directly and, again, you don't need
to know everything about submodules to contribute to Rust.
Just know that they exist and that they correspond to some sort of embedded subrepository dependency
that Git can nicely and fairly conveniently handle for us.

### Hard-resetting submodules

Sometimes you might run into (when you run `git status`)

```console
Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
  (commit or discard the untracked or modified content in submodules)
        modified:   src/llvm-project (new commits, modified content)
```

and when you try to run `git submodule update` it breaks horribly with errors like

```console
error: RPC failed; curl 92 HTTP/2 stream 7 was not closed cleanly: CANCEL (err 8)
error: 2782 bytes of body are still expected
fetch-pack: unexpected disconnect while reading sideband packet
fatal: early EOF
fatal: fetch-pack: invalid index-pack output
fatal: Fetched in submodule path 'src/llvm-project', but it did not contain 5a5152f653959d14d68613a3a8a033fb65eec021. Direct fetching of that commit failed.
```

If you see `(new commits, modified content)` you can run

```console
git submodule foreach git reset --hard
```

and then try `git submodule update` again.

### Deinit git submodules

If that doesn't work, you can try to deinit all git submodules...

```console
git submodule deinit -f --all
```

Unfortunately sometimes your local git submodules configuration can become
completely messed up for some reason.

### Overcoming `fatal: not a git repository: <submodule>/../../.git/modules/<submodule>`

Sometimes, for some forsaken reason, you might run into

```console
fatal: not a git repository: src/gcc/../../.git/modules/src/gcc
```

In this situation, for the given submodule path, i.e. `<submodule_path> =
src/gcc` in this example, you need to:

1. `rm -rf <submodule_path>/.git`
2. `rm -rf .git/modules/<submodule_path>/config`
3. `rm -rf .gitconfig.lock` if somehow the `.gitconfig` lock is orphaned.

Then do something like `./x fmt` to have bootstrap manage the submodule checkouts for you.

## Ignoring commits during `git blame`

Some commits contain large reformatting changes that don't otherwise change functionality.
They can be instructed to be ignored by `git blame` through
[`.git-blame-ignore-revs`](https://github.com/rust-lang/rust/blob/HEAD/.git-blame-ignore-revs):

1. Configure `git blame` to use `.git-blame-ignore-revs` as the list of commits to ignore: `git
   config blame.ignorerevsfile .git-blame-ignore-revs`
2. Add suitable commits that you wish to be ignored by `git blame`.

Please include a comment for the commit that you add to `.git-blame-ignore-revs` so people can
easily figure out *why* a commit is ignored.

[Git submodules]: https://git-scm.com/book/en/v2/Git-Tools-Submodules
[`rust-lang/llvm-project`]: https://github.com/rust-lang/llvm-project
[llvm-update]: https://github.com/rust-lang/rust/pull/99464/files


---

# Mastering @rustbot

`@rustbot` (also known as `triagebot`) is a utility robot that is mostly used to
allow any contributor to achieve certain tasks that would normally require GitHub
membership to the `rust-lang` organization. Its most interesting features for
contributors to `rustc` are issue claiming and relabeling.

## Issue claiming

`@rustbot` exposes a command that allows anyone to assign an issue to themselves.
If you see an issue you want to work on, you can send the following message as a
comment on the issue at hand:

    @rustbot claim

This will tell `@rustbot` to assign the issue to you if it has no assignee yet.
Note that because of some GitHub restrictions, you may be assigned indirectly,
i.e. `@rustbot` will assign itself as a placeholder and edit the top comment to
reflect the fact that the issue is now assigned to you.

If you want to unassign from an issue, `@rustbot` has a different command:

    @rustbot release-assignment

## Issue relabeling

Changing labels for an issue or PR is also normally reserved for members of the
organization. However, `@rustbot` allows you to relabel an issue yourself, only
with a few restrictions. This is mostly useful in two cases:

**Helping with issue triage**: Rust's issue tracker has more than 5,000 open
issues at the time of this writing, so labels are the most powerful tool that we
have to keep it as tidy as possible. You don't need to spend hours in the issue tracker
to triage issues, but if you open an issue, you should feel free to label it if
you are comfortable with doing it yourself.

**Updating the status of a PR**: We use "status labels" to reflect the status of
PRs. For example, if your PR has merge conflicts, it will automatically be assigned
the `S-waiting-on-author`, and reviewers might not review it until you rebase your
PR. Once you do rebase your branch, you should change the labels yourself to remove
the `S-waiting-on-author` label and add back `S-waiting-on-review`. In this case,
the `@rustbot` command will look like this:

    @rustbot label -S-waiting-on-author +S-waiting-on-review

The syntax for this command is pretty loose, so there are other variants of this
command invocation. There are also some shortcuts to update labels,
for instance `@rustbot ready` will do the same thing with above command.
For more details, see [the docs page about labeling][labeling] and [shortcuts][shortcuts].

[labeling]: https://forge.rust-lang.org/triagebot/labeling.html
[shortcuts]: https://forge.rust-lang.org/triagebot/shortcuts.html

## Other commands

If you are interested in seeing what `@rustbot` is capable of, check out its [documentation],
which is meant as a reference for the bot and should be kept up to date every time the
bot gets an upgrade.

`@rustbot` is maintained by the Release team. If you have any feedback regarding
existing commands or suggestions for new commands, feel free to reach out
[on Zulip][zulip] or file an issue in [the triagebot repository][repo]

[documentation]: https://forge.rust-lang.org/triagebot/index.html
[zulip]: https://rust-lang.zulipchat.com/#narrow/stream/224082-t-release.2Ftriagebot
[repo]: https://github.com/rust-lang/triagebot/


---

# Walkthrough: a typical contribution

There are _a lot_ of ways to contribute to the Rust compiler, including fixing
bugs, improving performance, helping design features, providing feedback on existing features, etc.
This chapter does not claim to scratch the surface.
Instead, it walks through the design and implementation of a new feature.
Not all of the steps and processes described here are needed for every
contribution, and I will try to point those out as they arise.

In general, if you are interested in making a contribution and aren't sure
where to start, please feel free to ask!

## Overview

The feature I will discuss in this chapter is the `?` Kleene operator for macros.
Basically, we want to be able to write something like this:

```rust,ignore
macro_rules! foo {
    ($arg:ident $(, $optional_arg:ident)?) => {
        println!("{}", $arg);

        $(
            println!("{}", $optional_arg);
        )?
    }
}

fn main() {
    let x = 0;
    foo!(x); // ok! prints "0"
    foo!(x, x); // ok! prints "0 0"
}
```

So basically, the `$(pat)?` matcher in the macro means "this pattern can occur
0 or 1 times", similar to other regex syntaxes.

There were a number of steps to go from an idea to stable Rust feature.
Here is a quick list.
We will go through each of these in order below.
As I mentioned before, not all of these are needed for every type of contribution.

- **Idea discussion/Pre-RFC**  A Pre-RFC is an early draft or design discussion of a feature.
  This stage is intended to flesh out the design space a bit and
  get a grasp on the different merits and problems with an idea.
  It's a great way to get early feedback on your idea before presenting it to the wider audience.
  You can find the original discussion [here][prerfc].
- **RFC**  This is when you formally present your idea to the community for consideration.
  You can find the RFC [here][rfc].
- **Implementation** Implement your idea unstably in the compiler.
  You can find the original implementation [here][impl1].
- **Possibly iterate/refine** As the community gets experience with your
  feature on the nightly compiler and in `std`, there may be additional
  feedback about design choice that might be adjusted.
  This particular feature went [through][impl2] a [number][impl3] of [iterations][impl4].
- **Stabilization** When your feature has baked enough, a Rust team member may
  [propose to stabilize it][merge].
  If there is consensus, this is done.
- **Relax** Your feature is now a stable Rust feature!

[prerfc]: https://internals.rust-lang.org/t/pre-rfc-at-most-one-repetition-macro-patterns/6557
[rfc]: https://github.com/rust-lang/rfcs/pull/2298
[impl1]: https://github.com/rust-lang/rust/pull/47752
[impl2]: https://github.com/rust-lang/rust/pull/49719
[impl3]: https://github.com/rust-lang/rust/pull/51336
[impl4]: https://github.com/rust-lang/rust/pull/51587
[merge]: https://github.com/rust-lang/rust/issues/48075#issuecomment-433177613

## Pre-RFC and RFC

> NOTE: In general, if you are not proposing a _new_ feature or substantial
> change to Rust or the ecosystem, you don't need to follow the RFC process.
> Instead, you can just jump to [implementation](#impl).
>
> You can find the official guidelines for when to open an RFC [here][rfcwhen].

[rfcwhen]: https://github.com/rust-lang/rfcs#when-you-need-to-follow-this-process

An RFC is a document that describes the feature or change you are proposing in detail.
Anyone can write an RFC;
the process is the same for everyone, including Rust team members.

To open an RFC, open a PR on the [rust-lang/rfcs](https://github.com/rust-lang/rfcs) repo on GitHub.
You can find detailed instructions in the
[README](https://github.com/rust-lang/rfcs#what-the-process-is).

Before opening an RFC, you should do the research to "flesh out" your idea.
Hastily-proposed RFCs tend not to be accepted.
You should generally have a good description of the motivation, impact, disadvantages, and potential
interactions with other features.

If that sounds like a lot of work, it's because it is.
But no fear!
Even if you're not a compiler hacker, you can get great feedback by doing a _pre-RFC_.
This is an _informal_ discussion of the idea.
The best place to do this is [internals.rust-lang.org](https://internals.rust-lang.org).
Your post doesn't have to follow any particular structure.
It doesn't even need to be a cohesive idea.
Generally, you will get tons of feedback that you can integrate back to produce a good RFC.

(Another pro-tip: try searching the RFCs repo and internals for prior related ideas.
A lot of times an idea has already been considered and was either
rejected or postponed to be tried again later.
This can save you and everybody else some time)

In the case of our example, a participant in the pre-RFC thread pointed out a
syntax ambiguity and a potential resolution.
Also, the overall feedback seemed positive.
In this case, the discussion converged pretty quickly, but for some
ideas, a lot more discussion can happen (e.g. see [this RFC][nonascii] which
received a whopping 684 comments!).
If that happens, don't be discouraged;
it means the community is interested in your idea, but it perhaps needs some adjustments.

[nonascii]: https://github.com/rust-lang/rfcs/pull/2457

The RFC for our `?` macro feature did receive some discussion on the RFC thread too.
As with most RFCs, there were a few questions that we couldn't answer by
discussion: we needed experience using the feature to decide.
Such questions are listed in the "Unresolved Questions" section of the RFC.
Also, over the course of the RFC discussion, you will probably want to update the RFC document
itself to reflect the course of the discussion (e.g. new alternatives or prior
work may be added or you may decide to change parts of the proposal itself).

In the end, when the discussion seems to reach a consensus and die down a bit,
a Rust team member may propose to move to "final comment period" (FCP) with one
of three possible dispositions.
This means that they want the other members of
the appropriate teams to review and comment on the RFC.
More discussion may ensue, which may result in more changes or unresolved questions being added.
At some point, when everyone is satisfied, the RFC enters the FCP, which is the
last chance for people to bring up objections.
When the FCP is over, the disposition is adopted.
Here are the three possible dispositions:

- _Merge_: accept the feature.
  Here is the proposal to merge for our [`?` macro feature][rfcmerge].
- _Close_: this feature in its current form is not a good fit for rust.
  Don't be discouraged if this happens to your RFC, and don't take it personally.
  This is not a reflection on you, but rather a community decision that rust
  will go a different direction.
- _Postpone_: there is interest in going this direction but not at the moment.
  This happens most often because the appropriate Rust team doesn't have the
  bandwidth to shepherd the feature through the process to stabilization.
  Often this is the case when the feature doesn't fit into the team's roadmap.
  Postponed ideas may be revisited later.

[rfcmerge]: https://github.com/rust-lang/rfcs/pull/2298#issuecomment-360582667

When an RFC is merged, the PR is merged into the RFCs repo.
A new _tracking issue_ is created in the [rust-lang/rust] repo to track progress on the feature
and discuss unresolved questions, implementation progress and blockers, etc.
Here is the tracking issue on for our [`?` macro feature][tracking].

[tracking]: https://github.com/rust-lang/rust/issues/48075

## Experimental RFC (eRFC)

An eRFC is a variant of the RFC process used for complex features where the high-level need
is clear, but the design space is too large to settle on a detailed specification upfront.
Instead of providing a final design, an eRFC outlines a high-level strategy to authorize
a period of active experimentation.
This allows the team to implement the feature behind
a feature gate and gather practical data, which then informs a subsequent formal RFC for stabilization.
While this process was used for major features like coroutines ([see RFC 2033][rfc2033]),
the explicit "eRFC" label is rarely used today.
The project now generally prefers approving a standard
RFC for an initial version and iterating on it through the nightly channel before final stabilization.

[rfc2033]: https://github.com/rust-lang/rfcs/pull/2033#issuecomment-309057591

<a id="impl"></a>

## Implementation

To make a change to the compiler, open a PR against the [rust-lang/rust] repo.

[rust-lang/rust]: https://github.com/rust-lang/rust

Depending on the feature/change/bug fix/improvement, implementation may be
relatively-straightforward or it may be a major undertaking.
You can always ask for help or mentorship from more experienced compiler devs.
Also, you don't have to be the one to implement your feature;
but keep in mind that if you don't, it might be a while before someone else does.

For the `?` macro feature, I needed to go understand the relevant parts of
macro expansion in the compiler.
Personally, I find that [improving the
comments][comments] in the code is a helpful way of making sure I understand
it, but you don't have to do that if you don't want to.

[comments]: https://github.com/rust-lang/rust/pull/47732

I then [implemented][impl1] the original feature, as described in the RFC.
When a new feature is implemented, it goes behind a _feature gate_, which means that
you have to use `#![feature(my_feature_name)]` to use the feature.
The feature gate is removed when the feature is stabilized.

**Most bug fixes and improvements** don't require a feature gate.
You can just make your changes/improvements.

When you open a PR on the [rust-lang/rust], a bot will assign your PR to a reviewer.
If there is a particular Rust team member you are working with, you can
request that reviewer by leaving a comment on the thread with `r?
@reviewer-github-id` (e.g. `r? @eddyb`). If you don't know who to request,
don't request anyone;
the bot will assign someone automatically based on which files you changed.

The reviewer may request changes before they approve your PR, they may mark the PR with label 
"S-waiting-on-author" after leaving comments, this means that the PR is blocked on you to make 
some requested changes.
When you finished iterating on the changes, you can mark the PR as
`S-waiting-on-review` again by leaving a comment with `@rustbot ready`, this will remove the 
`S-waiting-on-author` label and add the `S-waiting-on-review` label.

Feel free to ask questions or discuss things you don't understand or disagree with.
However, recognize that the PR won't be merged unless someone on the Rust team approves it.
If a reviewer leave a comment like `r=me after fixing ...`, that means they approve the PR and
you can merge it with comment with `@bors r=reviewer-github-id`(e.g. `@bors r=eddyb`) to merge it 
after fixing trivial issues.
Note that `r=someone` requires permission and bors could say
something like "🔑 Insufficient privileges..." when commenting `r=someone`.
In that case, you have to ask the reviewer to revisit your PR.

When your reviewer approves the PR, it will go into a queue for yet another bot called `@bors`.
`@bors` manages the CI build/merge queue.
When your PR reaches the head of the `@bors` queue, `@bors` will test out the merge by running all
tests against your PR on GitHub Actions.
This takes a lot of time to finish.
If all tests pass, the PR is merged and becomes part of the next nightly compiler!

There are a couple of things that may happen for some PRs during the review process

- If the change is substantial enough, the reviewer may request an FCP on the PR.
  This gives all members of the appropriate team a chance to review the changes.
- If the change may cause breakage, the reviewer may request a [crater] run.
  This compiles the compiler with your changes and then attempts to compile all
  crates on crates.io with your modified compiler.
  This is a great smoke test
  to check if you introduced a change to compiler behavior that affects a large
  portion of the ecosystem.
- If the diff of your PR is large or the reviewer is busy, your PR may have
  some merge conflicts with other PRs that happen to get merged first.
  You should fix these merge conflicts using the normal git procedures.

[crater]: ./tests/crater.html

If you are not doing a new feature or something like that (e.g. if you are
fixing a bug), then that's it!
Thanks for your contribution :)

## Refining your implementation

As people get experience with your new feature on nightly, slight changes may
be proposed and unresolved questions may become resolved.
Updates/changes go through the same process for implementing any other changes, as described
above (i.e. submit a PR, go through review, wait for `@bors`, etc).

Some changes may be major enough to require an FCP and some review by Rust team members.

For the `?` macro feature, we went through a few different iterations after the
original implementation: [1][impl2], [2][impl3], [3][impl4].

Along the way, we decided that `?` should not take a separator, which was
previously an unresolved question listed in the RFC.
We also changed the disambiguation strategy: we decided to remove the ability to use `?` as a
separator token for other repetition operators (e.g. `+` or `*`). However,
since this was a breaking change, we decided to do it over an edition boundary.
Thus, the new feature can be enabled only in edition 2018. These deviations
from the original RFC required [another FCP](https://github.com/rust-lang/rust/issues/51934).

## Stabilization

Finally, after the feature had baked for a while on nightly, a language team member
[moved to stabilize it][stabilizefcp].

[stabilizefcp]: https://github.com/rust-lang/rust/issues/48075#issuecomment-433177613

A _stabilization report_ needs to be written that includes

- brief description of the behavior and any deviations from the RFC
- which edition(s) are affected and how
- links to a few tests to show the interesting aspects

The stabilization report for our feature is [here][stabrep].

[stabrep]: https://github.com/rust-lang/rust/issues/48075#issuecomment-433243048

After this, [a PR is made][stab] to remove the feature gate, enabling the feature by
default (on the 2018 edition).
A note is added to the [Release notes][relnotes] about the feature.

[stab]: https://github.com/rust-lang/rust/pull/56245

Steps to stabilize the feature can be found at [Stabilizing Features](./stabilization-guide.md).

[relnotes]: https://github.com/rust-lang/rust/blob/HEAD/RELEASES.md
