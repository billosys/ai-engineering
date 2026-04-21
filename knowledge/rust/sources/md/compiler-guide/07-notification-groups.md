# Notification groups

The **notification groups** are an easy way to help out with rustc in a
"piece-meal" fashion, without committing to a larger project.
Notification groups are **[easy to join](#join)** (just submit a PR!)
and joining does not entail any particular commitment.

Once you [join a notification group](#join), you will be added to
a list that receives pings on github whenever a new issue is found
that fits the notification group's criteria.
If you are interested, you can then [claim the issue] and start working on it.

Of course, you don't have to wait for new issues to be tagged!
If you prefer, you can use the GitHub label for a notification group to
search for existing issues that haven't been claimed yet.

[claim the issue]: https://forge.rust-lang.org/triagebot/issue-assignment.html

## List of notification groups

Here's the list of the notification groups:
- [Apple](./apple.md)
- [ARM](./arm.md)
- [Emscripten](./emscripten.md)
- [LoongArch](./loongarch.md)
- [RISC-V](./risc-v.md)
- [WASI](./wasi.md)
- [WebAssembly](./wasm.md)
- [Windows](./windows.md)
- [Rust for Linux](./rust-for-linux.md)
- [GPU target](./gpu-target.md)

## What issues are a good fit for notification groups?

Notification groups tend to get pinged on **isolated** bugs,
particularly those of **middle priority**:

- By **isolated**, we mean that we do not expect large-scale refactoring
  to be required to fix the bug.
- By **middle priority**, we mean that we'd like to see the bug fixed,
  but it's not such a burning problem that we are dropping everything else to fix it.
  The danger with such bugs, of course, is that they
  can accumulate over time, and the role of the notification group is
  to try and stop that from happening!

<a id="join"></a>

## Joining a notification group

To join a notification group, you just have to open a PR adding your
GitHub username to the appropriate file in the Rust team repository.
See the "example PRs" below to get a precise idea and to identify the file to edit.

Also, if you are not already a member of a Rust team then -- in addition
to adding your name to the file -- you have to checkout the repository and
run the following command:

```bash
cargo run add-person $your_user_name
```

Example PRs:

* [Example of adding yourself to the Apple group.](https://github.com/rust-lang/team/pull/1434)
* [Example of adding yourself to the ARM group.](https://github.com/rust-lang/team/pull/358)
* [Example of adding yourself to the Emscripten group.](https://github.com/rust-lang/team/pull/1579)
* [Example of adding yourself to the LoongArch group.](https://github.com/rust-lang/team/pull/2176)
* [Example of adding yourself to the RISC-V group.](https://github.com/rust-lang/team/pull/394)
* [Example of adding yourself to the WASI group.](https://github.com/rust-lang/team/pull/1580)
* [Example of adding yourself to the WebAssembly group.](https://github.com/rust-lang/team/pull/1581)
* [Example of adding yourself to the Windows group.](https://github.com/rust-lang/team/pull/348)

## Tagging an issue for a notification group

To tag an issue as appropriate for a notification group, you give
[rustbot] a [`ping`] command with the name of the notification group.
For example:

```text
@rustbot ping apple
@rustbot ping arm
@rustbot ping emscripten
@rustbot ping risc-v
@rustbot ping wasi
@rustbot ping wasm
@rustbot ping windows
```

To make some commands shorter and easier to remember, there are aliases,
defined in the [`triagebot.toml`] file.
For example, all of these commands are equivalent and will ping the Apple group:

```text
@rustbot ping apple
@rustbot ping macos
@rustbot ping ios
```

Keep in mind that these aliases are meant to make humans' life easier.
They might be subject to change.
If you need to ensure that a command
will always be valid, prefer the full invocations over the aliases.

**Note though that this should only be done by compiler team members
or contributors, and is typically done as part of compiler team triage.**

[rustbot]: https://github.com/rust-lang/triagebot/
[`ping`]: https://forge.rust-lang.org/triagebot/pinging.html
[`triagebot.toml`]: https://github.com/rust-lang/rust/blob/HEAD/triagebot.toml


---

# Apple notification group

**GitHub Labels:** [O-macos], [O-ios], [O-tvos], [O-watchos] and [O-visionos] <br>
**Ping command:** `@rustbot ping apple`

This list will be used to ask for help both in diagnosing and testing
Apple-related issues as well as suggestions on how to resolve interesting
questions regarding our macOS/iOS/tvOS/watchOS/visionOS support.

To get a better idea for what the group will do, here are some examples of the
kinds of questions where we would have reached out to the group for advice in
determining the best course of action:

* Raising the minimum supported versions (e.g. [#104385])
* Additional Apple targets (e.g. [#121419])
* Obscure Xcode linker details (e.g. [#121430])

[O-macos]: https://github.com/rust-lang/rust/labels/O-macos
[O-ios]: https://github.com/rust-lang/rust/labels/O-ios
[O-tvos]: https://github.com/rust-lang/rust/labels/O-tvos
[O-watchos]: https://github.com/rust-lang/rust/labels/O-watchos
[O-visionos]: https://github.com/rust-lang/rust/labels/O-visionos
[#104385]: https://github.com/rust-lang/rust/pull/104385
[#121419]: https://github.com/rust-lang/rust/pull/121419
[#121430]: https://github.com/rust-lang/rust/pull/121430

## Deployment targets

Apple platforms have a concept of "deployment target", controlled with the
`*_DEPLOYMENT_TARGET` environment variables, and specifies the minimum OS
version that a binary runs on.

Using an API from a newer OS version in the standard library than the default
that `rustc` uses will result in either a static or a dynamic linker error.
For this reason, try to suggest that people document on `extern "C"` APIs
which OS version they were introduced with, and if that's newer than the
current default used by `rustc`, suggest to use weak linking.

## The App Store and private APIs

Apple are very protective about using undocumented APIs, so it's important
that whenever a change uses a new function, that they are verified to actually
be public API, as even just mentioning undocumented APIs in the binary
(without calling it) can lead to rejections from the App Store.

For example, Darwin / the XNU kernel actually has futex syscalls, but we can't
use them in `std` because they are not public API.

In general, for an API to be considered public by Apple, it has to:
- Appear in a public header (i.e. one distributed with Xcode, and found for
  the specific platform under `xcrun --show-sdk-path --sdk $SDK`).
- Have an availability attribute on it (like `__API_AVAILABLE`,
  `API_AVAILABLE` or similar).


---

# ARM notification group

**GitHub Label:** [O-ARM] <br>
**Ping command:** `@rustbot ping arm`

[O-ARM]: https://github.com/rust-lang/rust/labels/O-ARM

This list will be used to ask for help both in diagnosing and testing
ARM-related issues as well as suggestions on how to resolve
interesting questions regarding our ARM support.

The group also has an associated Zulip channel ([`#t-compiler/arm`])
where people can go to pose questions and discuss ARM-specific topics.

So, if you are interested in participating, please sign up for the ARM group!
To do so, open a PR against the [rust-lang/team] repository.
Just [follow this example][eg], but change the username to your own!

[`#t-compiler/arm`]: https://rust-lang.zulipchat.com/#narrow/stream/242906-t-compiler.2Farm
[rust-lang/team]: https://github.com/rust-lang/team
[eg]: https://github.com/rust-lang/team/pull/358


---

# Emscripten notification group

**GitHub Label:** [O-emscripten] <br>
**Ping command:** `@rustbot ping emscripten`

[O-emscripten]: https://github.com/rust-lang/rust/labels/O-emscripten

This list will be used to ask for help both in diagnosing and testing
Emscripten-related issues as well as suggestions on how to resolve
interesting questions regarding our Emscripten support.

The group also has an associated Zulip channel ([`#t-compiler/wasm`])
where people can go to pose questions and discuss Emscripten-specific topics.

So, if you are interested in participating, please sign up for the Emscripten group!
To do so, open a PR against the [rust-lang/team] repository.
Just [follow this example][eg], but change the username to your own!

[`#t-compiler/wasm`]: https://rust-lang.zulipchat.com/#narrow/stream/463513-t-compiler.2Fwasm
[rust-lang/team]: https://github.com/rust-lang/team
[eg]: https://github.com/rust-lang/team/pull/1579


---

# Fuchsia notification group

**GitHub Label:** [O-fuchsia] <br>
**Ping command:** `@rustbot ping fuchsia`

[O-fuchsia]: https://github.com/rust-lang/rust/labels/O-fuchsia

This list will be used to notify [Fuchsia][fuchsia] maintainers
when the compiler or the standard library changes in a way that would break the Fuchsia integration.

[fuchsia]: ../tests/ecosystem-test-jobs/fuchsia.md


---

# LoongArch notification group

**GitHub Label:** [O-loongarch] <br>
**Ping command:** `@rustbot ping loongarch`

[O-loongarch]: https://github.com/rust-lang/rust/labels/O-loongarch

This list will be used to ask for help both in diagnosing and testing
LoongArch-related issues as well as suggestions on how to resolve
interesting questions regarding our LoongArch support.

The group also has an associated Zulip channel ([`#t-compiler/loong-arch`])
where people can go to pose questions and discuss LoongArch-specific topics.

So, if you are interested in participating, please sign up for the LoongArch group!
To do so, open a PR against the [rust-lang/team] repository.
Just [follow this example][eg], but change the username to your own!

[`#t-compiler/loong-arch`]: https://rust-lang.zulipchat.com/#narrow/channel/551512-t-compiler.2Floong-arch
[rust-lang/team]: https://github.com/rust-lang/team
[eg]: https://github.com/rust-lang/team/pull/2176


---

# RISC-V notification group

**GitHub Label:** [O-riscv] <br>
**Ping command:** `@rustbot ping risc-v`

[O-riscv]: https://github.com/rust-lang/rust/labels/O-riscv

This list will be used to ask for help both in diagnosing and testing
RISC-V-related issues as well as suggestions on how to resolve
interesting questions regarding our RISC-V support.

The group also has an associated Zulip channel ([`#t-compiler/risc-v`])
where people can go to pose questions and discuss RISC-V-specific topics.

So, if you are interested in participating, please sign up for the RISC-V group!
To do so, open a PR against the [rust-lang/team] repository.
Just [follow this example][eg], but change the username to your own!

[`#t-compiler/risc-v`]: https://rust-lang.zulipchat.com/#narrow/stream/250483-t-compiler.2Frisc-v
[rust-lang/team]: https://github.com/rust-lang/team
[eg]: https://github.com/rust-lang/team/pull/394


---

# Rust for Linux notification group

**GitHub Label:** [A-rust-for-linux] <br>
**Ping command:** `@rustbot ping rfl`

[A-rust-for-linux]: https://github.com/rust-lang/rust/labels/A-rust-for-linux

This list will be used to notify [Rust for Linux (RfL)][rfl] maintainers
when the compiler or the standard library changes in a way that would
break Rust for Linux, since it depends on several unstable flags and features.
The RfL maintainers should then ideally provide support
for resolving the breakage or decide to temporarily accept the breakage
and unblock CI by temporarily removing the RfL CI jobs.

The group also has an associated Zulip channel ([`#rust-for-linux`])
where people can go to ask questions and discuss topics related to Rust for Linux.

If you are interested in participating, please sign up for the
Rust for Linux group on [Zulip][`#rust-for-linux`]!

[rfl]: https://rust-for-linux.com/
[`#rust-for-linux`]: https://rust-lang.zulipchat.com/#narrow/stream/425075-rust-for-linux


---

# WASI notification group

**GitHub Label:** [O-wasi] <br>
**Ping command:** `@rustbot ping wasi`

[O-wasi]: https://github.com/rust-lang/rust/labels/O-wasi

This list will be used to ask for help both in diagnosing and testing
WASI-related issues as well as suggestions on how to resolve
interesting questions regarding our WASI support.

The group also has an associated Zulip channel ([`#t-compiler/wasm`])
where people can go to pose questions and discuss WASI-specific topics.

So, if you are interested in participating, please sign up for the WASI group!
To do so, open a PR against the [rust-lang/team] repository.
Just [follow this example][eg], but change the username to your own!

[`#t-compiler/wasm`]: https://rust-lang.zulipchat.com/#narrow/stream/463513-t-compiler.2Fwasm
[rust-lang/team]: https://github.com/rust-lang/team
[eg]: https://github.com/rust-lang/team/pull/1580


---

# WebAssembly (WASM) notification group

**GitHub Label:** [O-wasm] <br>
**Ping command:** `@rustbot ping wasm`

[O-wasm]: https://github.com/rust-lang/rust/labels/O-wasm

This list will be used to ask for help both in diagnosing and testing
WebAssembly-related issues as well as suggestions on how to resolve
interesting questions regarding our WASM support.

The group also has an associated Zulip channel ([`#t-compiler/wasm`])
where people can go to pose questions and discuss WASM-specific
topics.

So, if you are interested in participating, please sign up for the
WASM group! To do so, open a PR against the [rust-lang/team]
repository. Just [follow this example][eg], but change the username to
your own!

[`#t-compiler/wasm`]: https://rust-lang.zulipchat.com/#narrow/stream/463513-t-compiler.2Fwasm
[rust-lang/team]: https://github.com/rust-lang/team
[eg]: https://github.com/rust-lang/team/pull/1581


---

# Windows notification group

**GitHub Label:** [O-Windows] <br>
**Ping command:** `@rustbot ping windows`

[O-Windows]: https://github.com/rust-lang/rust/labels/O-Windows

This list will be used to ask for help both in diagnosing and testing
Windows-related issues as well as suggestions on how to resolve
interesting questions regarding our Windows support.

The group also has an associated Zulip channel ([`#t-compiler/windows`])
where people can go to pose questions and discuss Windows-specific topics.

To get a better idea for what the group will do, here are some
examples of the kinds of questions where we would have reached out to
the group for advice in determining the best course of action:

* Which versions of MinGW should we support?
* Should we remove the legacy InnoSetup GUI installer? [#72569]
* What names should we use for static libraries on Windows?
  [#29520]

So, if you are interested in participating, please sign up for the Windows group!
To do so, open a PR against the [rust-lang/team] repository.
Just [follow this example][eg], but change the username to your own!

[`#t-compiler/windows`]: https://rust-lang.zulipchat.com/#streams/242869/t-compiler.2Fwindows
[rust-lang/team]: https://github.com/rust-lang/team
[eg]: https://github.com/rust-lang/team/pull/348/
[#72569]: https://github.com/rust-lang/rust/pull/72569
[#29520]: https://github.com/rust-lang/rust/pull/29520


---

# GPU target notification group

**Github Label:** None <br>
**Ping command:** `@rustbot ping gpu-target`

This notification group deals with linker related issues and their integration
within the compiler.

The group also has an associated Zulip stream ([`#t-compiler/gpgpu-backend`])
where people can go to ask questions and discuss GPU-related topics and issues.

if you're interested in participating, feel free to sign up for this group! To
do so, open a PR against the [rust-lang/team] repository and add your GitHub
user to [this file][gpu-target-team].

[`#t-compiler/gpgpu-backend`]: https://rust-lang.zulipchat.com/#narrow/channel/422870-t-compiler.2Fgpgpu-backend
[rust-lang/team]: https://github.com/rust-lang/team
[gpu-target-team]: https://github.com/rust-lang/team/blob/main/teams/gpu-target.toml
