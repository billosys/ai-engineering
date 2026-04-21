# Clap Source Documentation

> Extracted from clap repository
> Date: 2026-01-09
> Purpose: Comprehensive inline documentation for creating CLI guidelines

## Table of Contents

- [1. Core Concepts - Command](#command)
- [2. Arguments (Arg)](#arguments)
- [3. Argument Matching (ArgMatches)](#arg-matches)
- [4. Value Parsers](#value-parsers)
- [5. Derive API - Overview](#derive-general)
- [6. Derive API - Parser](#derive-parser)
- [8. Validation](#validation)
- [9. Error Handling](#error-handling)
- [10. Help and Usage Output](#help-output)
- [11. Styling and Formatting](#styling)
- [12. Shell Completions](#completions)
- [14. Other Topics](#other)
- [Appendix: All Documented Items](#appendix)


---


## 1. Core Concepts - Command {#command}


### From `repos/clap/clap_builder/src/builder/command.rs`


#### Struct: `Command` (line 36)

<!-- Source: repos/clap/clap_builder/src/builder/command.rs:36 -->

<!-- Type: struct -->


Build a command-line interface.

This includes defining arguments, subcommands, parser behavior, and help output.
Once all configuration is complete,
the [`Command::get_matches`] family of methods starts the runtime-parsing
process. These methods then return information about the user supplied
arguments (or lack thereof).

When deriving a [`Parser`][crate::Parser], you can use
[`CommandFactory::command`][crate::CommandFactory::command] to access the
`Command`.

- [Basic API][crate::Command#basic-api]
- [Application-wide Settings][crate::Command#application-wide-settings]
- [Command-specific Settings][crate::Command#command-specific-settings]
- [Subcommand-specific Settings][crate::Command#subcommand-specific-settings]
- [Reflection][crate::Command#reflection]

# Examples

```no_run
# use clap_builder as clap;
# use clap::{Command, Arg};
let m = Command::new("My Program")
.author("Me, me@mail.com")
.version("1.0.2")
.about("Explains in brief what the program does")
.arg(
Arg::new("in_file")
)
.after_help("Longer explanation to appear after the options when \
displaying the help information from --help or -h")
.get_matches();

// Your program logic starts here...
```
[`Command::get_matches`]: Command::get_matches()


**Code Examples:**


```rust
# use clap_builder as clap;
# use clap::{Command, Arg};
let m = Command::new("My Program")
.author("Me, me@mail.com")
.version("1.0.2")
.about("Explains in brief what the program does")
.arg(
Arg::new("in_file")
)
.after_help("Longer explanation to appear after the options when \
displaying the help information from --help or -h")
.get_matches();

// Your program logic starts here...
```


#### Impl: `Command` (line 115)

<!-- Source: repos/clap/clap_builder/src/builder/command.rs:115 -->

<!-- Type: impl -->


# Basic API


#### Fn: `new` (line 117)

<!-- Source: repos/clap/clap_builder/src/builder/command.rs:117 -->

<!-- Type: fn -->


Creates a new instance of an `Command`.

It is common, but not required, to use binary name as the `name`. This
name will only be displayed to the user when they request to print
version or help and usage information.

See also [`command!`](crate::command!) and [`crate_name!`](crate::crate_name!).

# Examples

```rust
# use clap_builder as clap;
# use clap::Command;
Command::new("My Program")
# ;
```


**Code Examples:**


```rust
# use clap_builder as clap;
# use clap::Command;
Command::new("My Program")
# ;
```


#### Fn: `new_inner` (line 134)

<!-- Source: repos/clap/clap_builder/src/builder/command.rs:134 -->

<!-- Type: fn -->


The actual implementation of `new`, non-generic to save code size.

If we don't do this rustc will unnecessarily generate multiple versions
of this code.


#### Fn: `arg` (line 148)

<!-- Source: repos/clap/clap_builder/src/builder/command.rs:148 -->

<!-- Type: fn -->


Adds an [argument] to the list of valid possibilities.

# Examples

```rust
# use clap_builder as clap;
# use clap::{Command, arg, Arg};
Command::new("myprog")
// Adding a single "flag" argument with a short and help text, using Arg::new()
.arg(
Arg::new("debug")
.short('d')
.help("turns on debugging mode")
)
// Adding a single "option" argument with a short, a long, and help text using the less
// verbose Arg::from()
.arg(
arg!(-c --config <CONFIG> "Optionally sets a config file to use")
)
# ;
```
[argument]: Arg


**Code Examples:**


```rust
# use clap_builder as clap;
# use clap::{Command, arg, Arg};
Command::new("myprog")
// Adding a single "flag" argument with a short and help text, using Arg::new()
.arg(
Arg::new("debug")
.short('d')
.help("turns on debugging mode")
)
// Adding a single "option" argument with a short, a long, and help text using the less
// verbose Arg::from()
.arg(
arg!(-c --config <CONFIG> "Optionally sets a config file to use")
)
# ;
```


#### Fn: `args` (line 191)

<!-- Source: repos/clap/clap_builder/src/builder/command.rs:191 -->

<!-- Type: fn -->


Adds multiple [arguments] to the list of valid possibilities.

# Examples

```rust
# use clap_builder as clap;
# use clap::{Command, arg, Arg};
Command::new("myprog")
.args([
arg!(-d --debug "turns on debugging info"),
Arg::new("input").help("the input file to use")
])
# ;
```
[arguments]: Arg


**Code Examples:**


```rust
# use clap_builder as clap;
# use clap::{Command, arg, Arg};
Command::new("myprog")
.args([
arg!(-d --debug "turns on debugging info"),
Arg::new("input").help("the input file to use")
])
# ;
```


#### Fn: `mut_arg` (line 214)

<!-- Source: repos/clap/clap_builder/src/builder/command.rs:214 -->

<!-- Type: fn -->


Allows one to mutate an [`Arg`] after it's been added to a [`Command`].

# Panics

If the argument is undefined

# Examples

```rust
# use clap_builder as clap;
# use clap::{Command, Arg, ArgAction};

let mut cmd = Command::new("foo")
.arg(Arg::new("bar")
.short('b')
.action(ArgAction::SetTrue))
.mut_arg("bar", |a| a.short('B'));

let res = cmd.try_get_matches_from_mut(vec!["foo", "-b"]);

// Since we changed `bar`'s short to "B" this should err as there
// is no `-b` anymore, only `-B`

assert!(res.is_err());

let res = cmd.try_get_matches_from_mut(vec!["foo", "-B"]);
assert!(res.is_ok());
```


**Code Examples:**


```rust
# use clap_builder as clap;
# use clap::{Command, Arg, ArgAction};

let mut cmd = Command::new("foo")
.arg(Arg::new("bar")
.short('b')
.action(ArgAction::SetTrue))
.mut_arg("bar", |a| a.short('B'));

let res = cmd.try_get_matches_from_mut(vec!["foo", "-b"]);

// Since we changed `bar`'s short to "B" this should err as there
// is no `-b` anymore, only `-B`

assert!(res.is_err());

let res = cmd.try_get_matches_from_mut(vec!["foo", "-B"]);
assert!(res.is_ok());
```


#### Fn: `mut_args` (line 267)

<!-- Source: repos/clap/clap_builder/src/builder/command.rs:267 -->

<!-- Type: fn -->


# use clap::{Command, Arg, ArgAction};

let mut cmd = Command::new("foo")
.arg(Arg::new("bar")
.long("bar")
.action(ArgAction::SetTrue))
.arg(Arg::new("baz")
.long("baz")
.action(ArgAction::SetTrue))
.mut_args(|a| {
if let Some(l) = a.get_long().map(|l| format!("prefix-{l}")) {
a.long(l)
} else {
a
}
});

let res = cmd.try_get_matches_from_mut(vec!["foo", "--bar"]);

// Since we changed `bar`'s long to "prefix-bar" this should err as there
// is no `--bar` anymore, only `--prefix-bar`.

assert!(res.is_err());

let res = cmd.try_get_matches_from_mut(vec!["foo", "--prefix-bar"]);
assert!(res.is_ok());
```


#### Fn: `mut_group` (line 304)

<!-- Source: repos/clap/clap_builder/src/builder/command.rs:304 -->

<!-- Type: fn -->


Allows one to mutate an [`ArgGroup`] after it's been added to a [`Command`].

# Panics

If the argument is undefined

# Examples

```rust
# use clap_builder as clap;
# use clap::{Command, arg, ArgGroup};

Command::new("foo")
.arg(arg!(--"set-ver" <ver> "set the version manually").required(false))
.arg(arg!(--major "auto increase major"))
.arg(arg!(--minor "auto increase minor"))
.arg(arg!(--patch "auto increase patch"))
.group(ArgGroup::new("vers")
.args(["set-ver", "major", "minor","patch"])
.required(true))
.mut_group("vers", |a| a.required(false));
```


**Code Examples:**


```rust
# use clap_builder as clap;
# use clap::{Command, arg, ArgGroup};

Command::new("foo")
.arg(arg!(--"set-ver" <ver> "set the version manually").required(false))
.arg(arg!(--major "auto increase major"))
.arg(arg!(--minor "auto increase minor"))
.arg(arg!(--patch "auto increase patch"))
.group(ArgGroup::new("vers")
.args(["set-ver", "major", "minor","patch"])
.required(true))
.mut_group("vers", |a| a.required(false));
```


#### Fn: `mut_subcommand` (line 343)

<!-- Source: repos/clap/clap_builder/src/builder/command.rs:343 -->

<!-- Type: fn -->


Allows one to mutate a [`Command`] after it's been added as a subcommand.

This can be useful for modifying auto-generated arguments of nested subcommands with
[`Command::mut_arg`].

# Panics

If the subcommand is undefined

# Examples

```rust
# use clap_builder as clap;
# use clap::Command;

let mut cmd = Command::new("foo")
.subcommand(Command::new("bar"))
.mut_subcommand("bar", |subcmd| subcmd.disable_help_flag(true));

let res = cmd.try_get_matches_from_mut(vec!["foo", "bar", "--help"]);

// Since we disabled the help flag on the "bar" subcommand, this should err.

assert!(res.is_err());

let res = cmd.try_get_matches_from_mut(vec!["foo", "bar"]);
assert!(res.is_ok());
```


**Code Examples:**


```rust
# use clap_builder as clap;
# use clap::Command;

let mut cmd = Command::new("foo")
.subcommand(Command::new("bar"))
.mut_subcommand("bar", |subcmd| subcmd.disable_help_flag(true));

let res = cmd.try_get_matches_from_mut(vec!["foo", "bar", "--help"]);

// Since we disabled the help flag on the "bar" subcommand, this should err.

assert!(res.is_err());

let res = cmd.try_get_matches_from_mut(vec!["foo", "bar"]);
assert!(res.is_ok());
```


#### Fn: `mut_subcommands` (line 398)

<!-- Source: repos/clap/clap_builder/src/builder/command.rs:398 -->

<!-- Type: fn -->


# use clap::{Command, Arg, ArgAction};

let mut cmd = Command::new("foo")
.subcommands([
Command::new("fetch"),
Command::new("push"),
])
// Allow title-case subcommands
.mut_subcommands(|sub| {
let name = sub.get_name();
let alias = name.chars().enumerate().map(|(i, c)| {
if i == 0 {
c.to_ascii_uppercase()
} else {
c
}
}).collect::<String>();
sub.alias(alias)
});

let res = cmd.try_get_matches_from_mut(vec!["foo", "fetch"]);
assert!(res.is_ok());

let res = cmd.try_get_matches_from_mut(vec!["foo", "Fetch"]);
assert!(res.is_ok());
```


#### Fn: `group` (line 434)

<!-- Source: repos/clap/clap_builder/src/builder/command.rs:434 -->

<!-- Type: fn -->


Adds an [`ArgGroup`] to the application.

[`ArgGroup`]s are a family of related arguments.
By placing them in a logical group, you can build easier requirement and exclusion rules.

Example use cases:
- Make an entire [`ArgGroup`] required, meaning that one (and *only*
one) argument from that group must be present at runtime.
- Name an [`ArgGroup`] as a conflict to another argument.
Meaning any of the arguments that belong to that group will cause a failure if present with
the conflicting argument.
- Ensure exclusion between arguments.
- Extract a value from a group instead of determining exactly which argument was used.

# Examples

The following example demonstrates using an [`ArgGroup`] to ensure that one, and only one,
of the arguments from the specified group is present at runtime.

```rust
# use clap_builder as clap;
# use clap::{Command, arg, ArgGroup};
Command::new("cmd")
.arg(arg!(--"set-ver" <ver> "set the version manually").required(false))
.arg(arg!(--major "auto increase major"))
.arg(arg!(--minor "auto increase minor"))
.arg(arg!(--patch "auto increase patch"))
.group(ArgGroup::new("vers")
.args(["set-ver", "major", "minor","patch"])
.required(true))
# ;
```


**Code Examples:**


```rust
# use clap_builder as clap;
# use clap::{Command, arg, ArgGroup};
Command::new("cmd")
.arg(arg!(--"set-ver" <ver> "set the version manually").required(false))
.arg(arg!(--major "auto increase major"))
.arg(arg!(--minor "auto increase minor"))
.arg(arg!(--patch "auto increase patch"))
.group(ArgGroup::new("vers")
.args(["set-ver", "major", "minor","patch"])
.required(true))
# ;
```


#### Fn: `groups` (line 473)

<!-- Source: repos/clap/clap_builder/src/builder/command.rs:473 -->

<!-- Type: fn -->


Adds multiple [`ArgGroup`]s to the [`Command`] at once.

# Examples

```rust
# use clap_builder as clap;
# use clap::{Command, arg, ArgGroup};
Command::new("cmd")
.arg(arg!(--"set-ver" <ver> "set the version manually").required(false))
.arg(arg!(--major         "auto increase major"))
.arg(arg!(--minor         "auto increase minor"))
.arg(arg!(--patch         "auto increase patch"))
.arg(arg!(-c <FILE>       "a config file").required(false))
.arg(arg!(-i <IFACE>      "an interface").required(false))
.groups([
ArgGroup::new("vers")
.args(["set-ver", "major", "minor","patch"])
.required(true),
ArgGroup::new("input")
.args(["c", "i"])
])
# ;
```


**Code Examples:**


```rust
# use clap_builder as clap;
# use clap::{Command, arg, ArgGroup};
Command::new("cmd")
.arg(arg!(--"set-ver" <ver> "set the version manually").required(false))
.arg(arg!(--major         "auto increase major"))
.arg(arg!(--minor         "auto increase minor"))
.arg(arg!(--patch         "auto increase patch"))
.arg(arg!(-c <FILE>       "a config file").required(false))
.arg(arg!(-i <IFACE>      "an interface").required(false))
.groups([
ArgGroup::new("vers")
.args(["set-ver", "major", "minor","patch"])
.required(true),
ArgGroup::new("input")
.args(["c", "i"])
])
# ;
```


#### Fn: `subcommand` (line 504)

<!-- Source: repos/clap/clap_builder/src/builder/command.rs:504 -->

<!-- Type: fn -->


Adds a subcommand to the list of valid possibilities.

Subcommands are effectively sub-[`Command`]s, because they can contain their own arguments,
subcommands, version, usage, etc. They also function just like [`Command`]s, in that they get
their own auto generated help, version, and usage.

A subcommand's [`Command::name`] will be used for:
- The argument the user passes in
- Programmatically looking up the subcommand

# Examples

```rust
# use clap_builder as clap;
# use clap::{Command, arg};
Command::new("myprog")
.subcommand(Command::new("config")
.about("Controls configuration features")
.arg(arg!(<config> "Required configuration file to use")))
# ;
```


**Code Examples:**


```rust
# use clap_builder as clap;
# use clap::{Command, arg};
Command::new("myprog")
.subcommand(Command::new("config")
.about("Controls configuration features")
.arg(arg!(<config> "Required configuration file to use")))
# ;
```


#### Fn: `subcommands` (line 542)

<!-- Source: repos/clap/clap_builder/src/builder/command.rs:542 -->

<!-- Type: fn -->


Adds multiple subcommands to the list of valid possibilities.

# Examples

```rust
# use clap_builder as clap;
# use clap::{Command, Arg, };
# Command::new("myprog")
.subcommands( [
Command::new("config").about("Controls configuration functionality")
.arg(Arg::new("config_file")),
Command::new("debug").about("Controls debug functionality")])
# ;
```
[`IntoIterator`]: std::iter::IntoIterator


**Code Examples:**


```rust
# use clap_builder as clap;
# use clap::{Command, Arg, };
# Command::new("myprog")
.subcommands( [
Command::new("config").about("Controls configuration functionality")
.arg(Arg::new("config_file")),
Command::new("debug").about("Controls debug functionality")])
# ;
```


#### Fn: `defer` (line 565)

<!-- Source: repos/clap/clap_builder/src/builder/command.rs:565 -->

<!-- Type: fn -->


Delay initialization for parts of the `Command`

This is useful for large applications to delay definitions of subcommands until they are
being invoked.

# Examples

```rust
# use clap_builder as clap;
# use clap::{Command, arg};
Command::new("myprog")
.subcommand(Command::new("config")
.about("Controls configuration features")
.defer(|cmd| {
cmd.arg(arg!(<config> "Required configuration file to use"))
})
)
# ;
```


**Code Examples:**


```rust
# use clap_builder as clap;
# use clap::{Command, arg};
Command::new("myprog")
.subcommand(Command::new("config")
.about("Controls configuration features")
.defer(|cmd| {
cmd.arg(arg!(<config> "Required configuration file to use"))
})
)
# ;
```


#### Fn: `debug_assert` (line 589)

<!-- Source: repos/clap/clap_builder/src/builder/command.rs:589 -->

<!-- Type: fn -->


Catch problems earlier in the development cycle.

Most error states are handled as asserts under the assumption they are programming mistake
and not something to handle at runtime.  Rather than relying on tests (manual or automated)
that exhaustively test your CLI to ensure the asserts are evaluated, this will run those
asserts in a way convenient for running as a test.

**Note:** This will not help with asserts in [`ArgMatches`], those will need exhaustive
testing of your CLI.

# Examples

```rust
# use clap_builder as clap;
# use clap::{Command, Arg, ArgAction};
fn cmd() -> Command {
Command::new("foo")
.arg(
Arg::new("bar").short('b').action(ArgAction::SetTrue)
)
}

#[test]
fn verify_app() {
cmd().debug_assert();
}

fn main() {
let m = cmd().get_matches_from(vec!["foo", "-b"]);
println!("{}", m.get_flag("bar"));
}
```


**Code Examples:**


```rust
# use clap_builder as clap;
# use clap::{Command, Arg, ArgAction};
fn cmd() -> Command {
Command::new("foo")
.arg(
Arg::new("bar").short('b').action(ArgAction::SetTrue)
)
}

#[test]
fn verify_app() {
cmd().debug_assert();
}

fn main() {
let m = cmd().get_matches_from(vec!["foo", "-b"]);
println!("{}", m.get_flag("bar"));
}
```


#### Fn: `error` (line 625)

<!-- Source: repos/clap/clap_builder/src/builder/command.rs:625 -->

<!-- Type: fn -->


Custom error message for post-parsing validation

**Note:** this will ensure the `Command` has been sufficiently [built][Command::build] for any
relevant context, including usage.

# Panics

If contradictory arguments or settings exist (debug builds).

# Examples

```rust
# use clap_builder as clap;
# use clap::{Command, error::ErrorKind};
let mut cmd = Command::new("myprog");
let err = cmd.error(ErrorKind::InvalidValue, "Some failure case");
```


**Code Examples:**


```rust
# use clap_builder as clap;
# use clap::{Command, error::ErrorKind};
let mut cmd = Command::new("myprog");
let err = cmd.error(ErrorKind::InvalidValue, "Some failure case");
```


#### Fn: `get_matches` (line 646)

<!-- Source: repos/clap/clap_builder/src/builder/command.rs:646 -->

<!-- Type: fn -->


Parse [`env::args_os`], [exiting][Error::exit] on failure.

# Panics

If contradictory arguments or settings exist (debug builds).

# Examples

```no_run
# use clap_builder as clap;
# use clap::{Command, Arg};
let matches = Command::new("myprog")
// Args and options go here...
.get_matches();
```
[`env::args_os`]: std::env::args_os()
[`Command::try_get_matches_from_mut`]: Command::try_get_matches_from_mut()


**Code Examples:**


```rust
# use clap_builder as clap;
# use clap::{Command, Arg};
let matches = Command::new("myprog")
// Args and options go here...
.get_matches();
```


#### Fn: `get_matches_mut` (line 668)

<!-- Source: repos/clap/clap_builder/src/builder/command.rs:668 -->

<!-- Type: fn -->


Parse [`env::args_os`], [exiting][Error::exit] on failure.

Like [`Command::get_matches`] but doesn't consume the `Command`.

# Panics

If contradictory arguments or settings exist (debug builds).

# Examples

```no_run
# use clap_builder as clap;
# use clap::{Command, Arg};
let mut cmd = Command::new("myprog")
// Args and options go here...
;
let matches = cmd.get_matches_mut();
```
[`env::args_os`]: std::env::args_os()
[`Command::get_matches`]: Command::get_matches()


**Code Examples:**


```rust
# use clap_builder as clap;
# use clap::{Command, Arg};
let mut cmd = Command::new("myprog")
// Args and options go here...
;
let matches = cmd.get_matches_mut();
```


#### Fn: `try_get_matches` (line 693)

<!-- Source: repos/clap/clap_builder/src/builder/command.rs:693 -->

<!-- Type: fn -->


Parse [`env::args_os`], returning a [`clap::Result`] on failure.

<div class="warning">

**NOTE:** This method WILL NOT exit when `--help` or `--version` (or short versions) are
used. It will return a [`clap::Error`], where the [`kind`] is a
[`ErrorKind::DisplayHelp`] or [`ErrorKind::DisplayVersion`] respectively. You must call
[`Error::exit`] or perform a [`std::process::exit`].

</div>

# Panics

If contradictory arguments or settings exist (debug builds).

# Examples

```no_run
# use clap_builder as clap;
# use clap::{Command, Arg};
let matches = Command::new("myprog")
// Args and options go here...
.try_get_matches()
.unwrap_or_else(|e| e.exit());
```
[`env::args_os`]: std::env::args_os()
[`Error::exit`]: crate::Error::exit()
[`std::process::exit`]: std::process::exit()
[`clap::Result`]: Result
[`clap::Error`]: crate::Error
[`kind`]: crate::Error
[`ErrorKind::DisplayHelp`]: crate::error::ErrorKind::DisplayHelp
[`ErrorKind::DisplayVersion`]: crate::error::ErrorKind::DisplayVersion


**Code Examples:**


```rust
# use clap_builder as clap;
# use clap::{Command, Arg};
let matches = Command::new("myprog")
// Args and options go here...
.try_get_matches()
.unwrap_or_else(|e| e.exit());
```


#### Fn: `get_matches_from` (line 732)

<!-- Source: repos/clap/clap_builder/src/builder/command.rs:732 -->

<!-- Type: fn -->


Parse the specified arguments, [exiting][Error::exit] on failure.

<div class="warning">

**NOTE:** The first argument will be parsed as the binary name unless
[`Command::no_binary_name`] is used.

</div>

# Panics

If contradictory arguments or settings exist (debug builds).

# Examples

```no_run
# use clap_builder as clap;
# use clap::{Command, Arg};
let arg_vec = vec!["my_prog", "some", "args", "to", "parse"];

let matches = Command::new("myprog")
// Args and options go here...
.get_matches_from(arg_vec);
```
[`Command::get_matches`]: Command::get_matches()
[`clap::Result`]: Result
[`Vec`]: std::vec::Vec


**Code Examples:**


```rust
# use clap_builder as clap;
# use clap::{Command, Arg};
let arg_vec = vec!["my_prog", "some", "args", "to", "parse"];

let matches = Command::new("myprog")
// Args and options go here...
.get_matches_from(arg_vec);
```


#### Fn: `try_get_matches_from` (line 770)

<!-- Source: repos/clap/clap_builder/src/builder/command.rs:770 -->

<!-- Type: fn -->


Parse the specified arguments, returning a [`clap::Result`] on failure.

<div class="warning">

**NOTE:** This method WILL NOT exit when `--help` or `--version` (or short versions) are
used. It will return a [`clap::Error`], where the [`kind`] is a [`ErrorKind::DisplayHelp`]
or [`ErrorKind::DisplayVersion`] respectively. You must call [`Error::exit`] or
perform a [`std::process::exit`] yourself.

</div>

<div class="warning">

**NOTE:** The first argument will be parsed as the binary name unless
[`Command::no_binary_name`] is used.

</div>

# Panics

If contradictory arguments or settings exist (debug builds).

# Examples

```no_run
# use clap_builder as clap;
# use clap::{Command, Arg};
let arg_vec = vec!["my_prog", "some", "args", "to", "parse"];

let matches = Command::new("myprog")
// Args and options go here...
.try_get_matches_from(arg_vec)
.unwrap_or_else(|e| e.exit());
```
[`Command::get_matches_from`]: Command::get_matches_from()
[`Command::try_get_matches`]: Command::try_get_matches()
[`Error::exit`]: crate::Error::exit()
[`std::process::exit`]: std::process::exit()
[`clap::Error`]: crate::Error
[`Error::exit`]: crate::Error::exit()
[`kind`]: crate::Error
[`ErrorKind::DisplayHelp`]: crate::error::ErrorKind::DisplayHelp
[`ErrorKind::DisplayVersion`]: crate::error::ErrorKind::DisplayVersion
[`clap::Result`]: Result


**Code Examples:**


```rust
# use clap_builder as clap;
# use clap::{Command, Arg};
let arg_vec = vec!["my_prog", "some", "args", "to", "parse"];

let matches = Command::new("myprog")
// Args and options go here...
.try_get_matches_from(arg_vec)
.unwrap_or_else(|e| e.exit());
```


#### Fn: `try_get_matches_from_mut` (line 822)

<!-- Source: repos/clap/clap_builder/src/builder/command.rs:822 -->

<!-- Type: fn -->


Parse the specified arguments, returning a [`clap::Result`] on failure.

Like [`Command::try_get_matches_from`] but doesn't consume the `Command`.

<div class="warning">

**NOTE:** This method WILL NOT exit when `--help` or `--version` (or short versions) are
used. It will return a [`clap::Error`], where the [`kind`] is a [`ErrorKind::DisplayHelp`]
or [`ErrorKind::DisplayVersion`] respectively. You must call [`Error::exit`] or
perform a [`std::process::exit`] yourself.

</div>

<div class="warning">

**NOTE:** The first argument will be parsed as the binary name unless
[`Command::no_binary_name`] is used.

</div>

# Panics

If contradictory arguments or settings exist (debug builds).

# Examples

```no_run
# use clap_builder as clap;
# use clap::{Command, Arg};
let arg_vec = vec!["my_prog", "some", "args", "to", "parse"];

let mut cmd = Command::new("myprog");
// Args and options go here...
let matches = cmd.try_get_matches_from_mut(arg_vec)
.unwrap_or_else(|e| e.exit());
```
[`Command::try_get_matches_from`]: Command::try_get_matches_from()
[`clap::Result`]: Result
[`clap::Error`]: crate::Error
[`kind`]: crate::Error


**Code Examples:**


```rust
# use clap_builder as clap;
# use clap::{Command, Arg};
let arg_vec = vec!["my_prog", "some", "args", "to", "parse"];

let mut cmd = Command::new("myprog");
// Args and options go here...
let matches = cmd.try_get_matches_from_mut(arg_vec)
.unwrap_or_else(|e| e.exit());
```


#### Fn: `print_help` (line 912)

<!-- Source: repos/clap/clap_builder/src/builder/command.rs:912 -->

<!-- Type: fn -->


Prints the short help message (`-h`) to [`io::stdout()`].

See also [`Command::print_long_help`].

**Note:** this will ensure the `Command` has been sufficiently [built][Command::build].

# Panics

If contradictory arguments or settings exist (debug builds).

# Examples

```rust
# use clap_builder as clap;
# use clap::Command;
let mut cmd = Command::new("myprog");
cmd.print_help();
```
[`io::stdout()`]: std::io::stdout()


**Code Examples:**


```rust
# use clap_builder as clap;
# use clap::Command;
let mut cmd = Command::new("myprog");
cmd.print_help();
```


#### Fn: `print_long_help` (line 943)

<!-- Source: repos/clap/clap_builder/src/builder/command.rs:943 -->

<!-- Type: fn -->


Prints the long help message (`--help`) to [`io::stdout()`].

See also [`Command::print_help`].

**Note:** this will ensure the `Command` has been sufficiently [built][Command::build].

# Panics

If contradictory arguments or settings exist (debug builds).

# Examples

```rust
# use clap_builder as clap;
# use clap::Command;
let mut cmd = Command::new("myprog");
cmd.print_long_help();
```
[`io::stdout()`]: std::io::stdout()
[`BufWriter`]: std::io::BufWriter
[`-h` (short)]: Arg::help()
[`--help` (long)]: Arg::long_help()


**Code Examples:**


```rust
# use clap_builder as clap;
# use clap::Command;
let mut cmd = Command::new("myprog");
cmd.print_long_help();
```


#### Fn: `render_help` (line 977)

<!-- Source: repos/clap/clap_builder/src/builder/command.rs:977 -->

<!-- Type: fn -->


Render the short help message (`-h`) to a [`StyledStr`]

See also [`Command::render_long_help`].

**Note:** this will ensure the `Command` has been sufficiently [built][Command::build].

# Panics

If contradictory arguments or settings exist (debug builds).

# Examples

```rust
# use clap_builder as clap;
# use clap::Command;
use std::io;
let mut cmd = Command::new("myprog");
let mut out = io::stdout();
let help = cmd.render_help();
println!("{help}");
```
[`io::Write`]: std::io::Write
[`-h` (short)]: Arg::help()
[`--help` (long)]: Arg::long_help()


**Code Examples:**


```rust
# use clap_builder as clap;
# use clap::Command;
use std::io;
let mut cmd = Command::new("myprog");
let mut out = io::stdout();
let help = cmd.render_help();
println!("{help}");
```


#### Fn: `render_long_help` (line 1010)

<!-- Source: repos/clap/clap_builder/src/builder/command.rs:1010 -->

<!-- Type: fn -->


Render the long help message (`--help`) to a [`StyledStr`].

See also [`Command::render_help`].

**Note:** this will ensure the `Command` has been sufficiently [built][Command::build].

# Panics

If contradictory arguments or settings exist (debug builds).

# Examples

```rust
# use clap_builder as clap;
# use clap::Command;
use std::io;
let mut cmd = Command::new("myprog");
let mut out = io::stdout();
let help = cmd.render_long_help();
println!("{help}");
```
[`io::Write`]: std::io::Write
[`-h` (short)]: Arg::help()
[`--help` (long)]: Arg::long_help()


**Code Examples:**


```rust
# use clap_builder as clap;
# use clap::Command;
use std::io;
let mut cmd = Command::new("myprog");
let mut out = io::stdout();
let help = cmd.render_long_help();
println!("{help}");
```


#### Fn: `render_version` (line 1073)

<!-- Source: repos/clap/clap_builder/src/builder/command.rs:1073 -->

<!-- Type: fn -->


Version message rendered as if the user ran `-V`.

See also [`Command::render_long_version`].

### Coloring

This function does not try to color the message nor it inserts any [ANSI escape codes].

### Examples

```rust
# use clap_builder as clap;
# use clap::Command;
use std::io;
let cmd = Command::new("myprog");
println!("{}", cmd.render_version());
```
[`io::Write`]: std::io::Write
[`-V` (short)]: Command::version()
[`--version` (long)]: Command::long_version()
[ANSI escape codes]: https://en.wikipedia.org/wiki/ANSI_escape_code


**Code Examples:**


```rust
# use clap_builder as clap;
# use clap::Command;
use std::io;
let cmd = Command::new("myprog");
println!("{}", cmd.render_version());
```


#### Fn: `render_long_version` (line 1098)

<!-- Source: repos/clap/clap_builder/src/builder/command.rs:1098 -->

<!-- Type: fn -->


Version message rendered as if the user ran `--version`.

See also [`Command::render_version`].

### Coloring

This function does not try to color the message nor it inserts any [ANSI escape codes].

### Examples

```rust
# use clap_builder as clap;
# use clap::Command;
use std::io;
let cmd = Command::new("myprog");
println!("{}", cmd.render_long_version());
```
[`io::Write`]: std::io::Write
[`-V` (short)]: Command::version()
[`--version` (long)]: Command::long_version()
[ANSI escape codes]: https://en.wikipedia.org/wiki/ANSI_escape_code


**Code Examples:**


```rust
# use clap_builder as clap;
# use clap::Command;
use std::io;
let cmd = Command::new("myprog");
println!("{}", cmd.render_long_version());
```


#### Fn: `render_usage` (line 1123)

<!-- Source: repos/clap/clap_builder/src/builder/command.rs:1123 -->

<!-- Type: fn -->


Usage statement

**Note:** this will ensure the `Command` has been sufficiently [built][Command::build].

# Panics

If contradictory arguments or settings exist (debug builds).

### Examples

```rust
# use clap_builder as clap;
# use clap::Command;
use std::io;
let mut cmd = Command::new("myprog");
println!("{}", cmd.render_usage());
```


**Code Examples:**


```rust
# use clap_builder as clap;
# use clap::Command;
use std::io;
let mut cmd = Command::new("myprog");
println!("{}", cmd.render_usage());
```


#### Fn: `add` (line 1152)

<!-- Source: repos/clap/clap_builder/src/builder/command.rs:1152 -->

<!-- Type: fn -->


Extend [`Command`] with [`CommandExt`] data


#### Impl: `Command` (line 1161)

<!-- Source: repos/clap/clap_builder/src/builder/command.rs:1161 -->

<!-- Type: impl -->


# Application-wide Settings

These settings will apply to the top-level command and all subcommands, by default.  Some
settings can be overridden in subcommands.


#### Fn: `no_binary_name` (line 1166)

<!-- Source: repos/clap/clap_builder/src/builder/command.rs:1166 -->

<!-- Type: fn -->


Specifies that the parser should not assume the first argument passed is the binary name.

This is normally the case when using a "daemon" style mode.  For shells / REPLs, see
[`Command::multicall`][Command::multicall].

# Examples

```rust
# use clap_builder as clap;
# use clap::{Command, arg};
let m = Command::new("myprog")
.no_binary_name(true)
.arg(arg!(<cmd> ... "commands to run"))
.get_matches_from(vec!["command", "set"]);

let cmds: Vec<_> = m.get_many::<String>("cmd").unwrap().collect();
assert_eq!(cmds, ["command", "set"]);
```
[`try_get_matches_from_mut`]: crate::Command::try_get_matches_from_mut()


**Code Examples:**


```rust
# use clap_builder as clap;
# use clap::{Command, arg};
let m = Command::new("myprog")
.no_binary_name(true)
.arg(arg!(<cmd> ... "commands to run"))
.get_matches_from(vec!["command", "set"]);

let cmds: Vec<_> = m.get_many::<String>("cmd").unwrap().collect();
assert_eq!(cmds, ["command", "set"]);
```


#### Fn: `ignore_errors` (line 1194)

<!-- Source: repos/clap/clap_builder/src/builder/command.rs:1194 -->

<!-- Type: fn -->


Try not to fail on parse errors, like missing option values.

<div class="warning">

**NOTE:** This choice is propagated to all child subcommands.

</div>

# Examples

```rust
# use clap_builder as clap;
# use clap::{Command, arg};
let cmd = Command::new("cmd")
.ignore_errors(true)
.arg(arg!(-c --config <FILE> "Sets a custom config file"))
.arg(arg!(-x --stuff <FILE> "Sets a custom stuff file"))
.arg(arg!(f: -f "Flag"));

let r = cmd.try_get_matches_from(vec!["cmd", "-c", "file", "-f", "-x"]);

assert!(r.is_ok(), "unexpected error: {r:?}");
let m = r.unwrap();
assert_eq!(m.get_one::<String>("config").unwrap(), "file");
assert!(m.get_flag("f"));
assert_eq!(m.get_one::<String>("stuff"), None);
```


**Code Examples:**


```rust
# use clap_builder as clap;
# use clap::{Command, arg};
let cmd = Command::new("cmd")
.ignore_errors(true)
.arg(arg!(-c --config <FILE> "Sets a custom config file"))
.arg(arg!(-x --stuff <FILE> "Sets a custom stuff file"))
.arg(arg!(f: -f "Flag"));

let r = cmd.try_get_matches_from(vec!["cmd", "-c", "file", "-f", "-x"]);

assert!(r.is_ok(), "unexpected error: {r:?}");
let m = r.unwrap();
assert_eq!(m.get_one::<String>("config").unwrap(), "file");
assert!(m.get_flag("f"));
assert_eq!(m.get_one::<String>("stuff"), None);
```


#### Fn: `args_override_self` (line 1230)

<!-- Source: repos/clap/clap_builder/src/builder/command.rs:1230 -->

<!-- Type: fn -->


Replace prior occurrences of arguments rather than error

For any argument that would conflict with itself by default (e.g.
[`ArgAction::Set`], it will now override itself.

This is the equivalent to saying the `foo` arg using [`Arg::overrides_with("foo")`] for all
defined arguments.

<div class="warning">

**NOTE:** This choice is propagated to all child subcommands.

</div>

[`Arg::overrides_with("foo")`]: crate::Arg::overrides_with()


#### Fn: `dont_delimit_trailing_values` (line 1254)

<!-- Source: repos/clap/clap_builder/src/builder/command.rs:1254 -->

<!-- Type: fn -->


Disables the automatic [delimiting of values][Arg::value_delimiter] after `--` or when [`Arg::trailing_var_arg`]
was used.

<div class="warning">

**NOTE:** The same thing can be done manually by setting the final positional argument to
[`Arg::value_delimiter(None)`]. Using this setting is safer, because it's easier to locate
when making changes.

</div>

<div class="warning">

**NOTE:** This choice is propagated to all child subcommands.

</div>

# Examples

```no_run
# use clap_builder as clap;
# use clap::{Command, Arg};
Command::new("myprog")
.dont_delimit_trailing_values(true)
.get_matches();
```

[`Arg::value_delimiter(None)`]: crate::Arg::value_delimiter()


**Code Examples:**


```rust
# use clap_builder as clap;
# use clap::{Command, Arg};
Command::new("myprog")
.dont_delimit_trailing_values(true)
.get_matches();
```


#### Fn: `color` (line 1291)

<!-- Source: repos/clap/clap_builder/src/builder/command.rs:1291 -->

<!-- Type: fn -->


Sets when to color output.

To customize how the output is styled, see [`Command::styles`].

<div class="warning">

**NOTE:** This choice is propagated to all child subcommands.

</div>

<div class="warning">

**NOTE:** Default behaviour is [`ColorChoice::Auto`].

</div>

# Examples

```no_run
# use clap_builder as clap;
# use clap::{Command, ColorChoice};
Command::new("myprog")
.color(ColorChoice::Never)
.get_matches();
```
[`ColorChoice::Auto`]: crate::ColorChoice::Auto


**Code Examples:**


```rust
# use clap_builder as clap;
# use clap::{Command, ColorChoice};
Command::new("myprog")
.color(ColorChoice::Never)
.get_matches();
```


#### Fn: `styles` (line 1332)

<!-- Source: repos/clap/clap_builder/src/builder/command.rs:1332 -->

<!-- Type: fn -->


Sets the [`Styles`] for terminal output

<div class="warning">

**NOTE:** This choice is propagated to all child subcommands.

</div>

<div class="warning">

**NOTE:** Default behaviour is [`Styles::default`].

</div>

# Examples

```no_run
# use clap_builder as clap;
# use clap::{Command, ColorChoice, builder::styling};
const STYLES: styling::Styles = styling::Styles::styled()
.header(styling::AnsiColor::Green.on_default().bold())
.usage(styling::AnsiColor::Green.on_default().bold())
.literal(styling::AnsiColor::Blue.on_default().bold())
.placeholder(styling::AnsiColor::Cyan.on_default());
Command::new("myprog")
.styles(STYLES)
.get_matches();
```


**Code Examples:**


```rust
# use clap_builder as clap;
# use clap::{Command, ColorChoice, builder::styling};
const STYLES: styling::Styles = styling::Styles::styled()
.header(styling::AnsiColor::Green.on_default().bold())
.usage(styling::AnsiColor::Green.on_default().bold())
.literal(styling::AnsiColor::Blue.on_default().bold())
.placeholder(styling::AnsiColor::Cyan.on_default());
Command::new("myprog")
.styles(STYLES)
.get_matches();
```


#### Fn: `term_width` (line 1368)

<!-- Source: repos/clap/clap_builder/src/builder/command.rs:1368 -->

<!-- Type: fn -->


Sets the terminal width at which to wrap help messages.

Using `0` will ignore terminal widths and use source formatting.

Defaults to current terminal width when `wrap_help` feature flag is enabled.  If current
width cannot be determined, the default is 100.

**`unstable-v5` feature**: Defaults to unbound, being subject to
[`Command::max_term_width`].

<div class="warning">

**NOTE:** This setting applies globally and *not* on a per-command basis.

</div>

<div class="warning">

**NOTE:** This requires the `wrap_help` feature

</div>

# Examples

```rust
# use clap_builder as clap;
# use clap::Command;
Command::new("myprog")
.term_width(80)
# ;
```


**Code Examples:**


```rust
# use clap_builder as clap;
# use clap::Command;
Command::new("myprog")
.term_width(80)
# ;
```


#### Fn: `max_term_width` (line 1407)

<!-- Source: repos/clap/clap_builder/src/builder/command.rs:1407 -->

<!-- Type: fn -->


Limit the line length for wrapping help when using the current terminal's width.

This only applies when [`term_width`][Command::term_width] is unset so that the current
terminal's width will be used.  See [`Command::term_width`] for more details.

Using `0` will ignore this, always respecting [`Command::term_width`] (default).

**`unstable-v5` feature**: Defaults to 100.

<div class="warning">

**NOTE:** This setting applies globally and *not* on a per-command basis.

</div>

<div class="warning">

**NOTE:** This requires the `wrap_help` feature

</div>

# Examples

```rust
# use clap_builder as clap;
# use clap::Command;
Command::new("myprog")
.max_term_width(100)
# ;
```


**Code Examples:**


```rust
# use clap_builder as clap;
# use clap::Command;
Command::new("myprog")
.max_term_width(100)
# ;
```


#### Fn: `disable_version_flag` (line 1445)

<!-- Source: repos/clap/clap_builder/src/builder/command.rs:1445 -->

<!-- Type: fn -->


Disables `-V` and `--version` flag.

# Examples

```rust
# use clap_builder as clap;
# use clap::{Command, error::ErrorKind};
let res = Command::new("myprog")
.version("1.0.0")
.disable_version_flag(true)
.try_get_matches_from(vec![
"myprog", "--version"
]);
assert!(res.is_err());
assert_eq!(res.unwrap_err().kind(), ErrorKind::UnknownArgument);
```

You can create a custom version flag with [`ArgAction::Version`]
```rust
# use clap_builder as clap;
# use clap::{Command, Arg, ArgAction, error::ErrorKind};
let mut cmd = Command::new("myprog")
.version("1.0.0")
// Remove the `-V` short flag
.disable_version_flag(true)
.arg(
Arg::new("version")
.long("version")
.action(ArgAction::Version)
.help("Print version")
);

let res = cmd.try_get_matches_from_mut(vec![
"myprog", "-V"
]);
assert!(res.is_err());
assert_eq!(res.unwrap_err().kind(), ErrorKind::UnknownArgument);

let res = cmd.try_get_matches_from_mut(vec![
"myprog", "--version"
]);
assert!(res.is_err());
assert_eq!(res.unwrap_err().kind(), ErrorKind::DisplayVersion);
```


**Code Examples:**


```rust
# use clap_builder as clap;
# use clap::{Command, error::ErrorKind};
let res = Command::new("myprog")
.version("1.0.0")
.disable_version_flag(true)
.try_get_matches_from(vec![
"myprog", "--version"
]);
assert!(res.is_err());
assert_eq!(res.unwrap_err().kind(), ErrorKind::UnknownArgument);
```


```rust
# use clap_builder as clap;
# use clap::{Command, Arg, ArgAction, error::ErrorKind};
let mut cmd = Command::new("myprog")
.version("1.0.0")
// Remove the `-V` short flag
.disable_version_flag(true)
.arg(
Arg::new("version")
.long("version")
.action(ArgAction::Version)
.help("Print version")
);

let res = cmd.try_get_matches_from_mut(vec![
"myprog", "-V"
]);
assert!(res.is_err());
assert_eq!(res.unwrap_err().kind(), ErrorKind::UnknownArgument);

let res = cmd.try_get_matches_from_mut(vec![
"myprog", "--version"
]);
assert!(res.is_err());
assert_eq!(res.unwrap_err().kind(), ErrorKind::DisplayVersion);
```


#### Fn: `propagate_version` (line 1498)

<!-- Source: repos/clap/clap_builder/src/builder/command.rs:1498 -->

<!-- Type: fn -->


Specifies to use the version of the current command for all [`subcommands`].

Defaults to `false`; subcommands have independent version strings from their parents.

<div class="warning">

**NOTE:** This choice is propagated to all child subcommands.

</div>

# Examples

```no_run
# use clap_builder as clap;
# use clap::{Command, Arg};
Command::new("myprog")
.version("v1.1")
.propagate_version(true)
.subcommand(Command::new("test"))
.get_matches();
// running `$ myprog test --version` will display
// "myprog-test v1.1"
```

[`subcommands`]: crate::Command::subcommand()


**Code Examples:**


```rust
# use clap_builder as clap;
# use clap::{Command, Arg};
Command::new("myprog")
.version("v1.1")
.propagate_version(true)
.subcommand(Command::new("test"))
.get_matches();
// running `$ myprog test --version` will display
// "myprog-test v1.1"
```


#### Fn: `next_line_help` (line 1532)

<!-- Source: repos/clap/clap_builder/src/builder/command.rs:1532 -->

<!-- Type: fn -->


Places the help string for all arguments and subcommands on the line after them.

<div class="warning">

**NOTE:** This choice is propagated to all child subcommands.

</div>

# Examples

```no_run
# use clap_builder as clap;
# use clap::{Command, Arg};
Command::new("myprog")
.next_line_help(true)
.get_matches();
```


**Code Examples:**


```rust
# use clap_builder as clap;
# use clap::{Command, Arg};
Command::new("myprog")
.next_line_help(true)
.get_matches();
```


#### Fn: `disable_help_flag` (line 1558)

<!-- Source: repos/clap/clap_builder/src/builder/command.rs:1558 -->

<!-- Type: fn -->


Disables `-h` and `--help` flag.

<div class="warning">

**NOTE:** This choice is propagated to all child subcommands.

</div>

# Examples

```rust
# use clap_builder as clap;
# use clap::{Command, error::ErrorKind};
let res = Command::new("myprog")
.disable_help_flag(true)
.try_get_matches_from(vec![
"myprog", "-h"
]);
assert!(res.is_err());
assert_eq!(res.unwrap_err().kind(), ErrorKind::UnknownArgument);
```

You can create a custom help flag with [`ArgAction::Help`], [`ArgAction::HelpShort`], or
[`ArgAction::HelpLong`]
```rust
# use clap_builder as clap;
# use clap::{Command, Arg, ArgAction, error::ErrorKind};
let mut cmd = Command::new("myprog")
// Change help short flag to `?`
.disable_help_flag(true)
.arg(
Arg::new("help")
.short('?')
.long("help")
.action(ArgAction::Help)
.help("Print help")
);

let res = cmd.try_get_matches_from_mut(vec![
"myprog", "-h"
]);
assert!(res.is_err());
assert_eq!(res.unwrap_err().kind(), ErrorKind::UnknownArgument);

let res = cmd.try_get_matches_from_mut(vec![
"myprog", "-?"
]);
assert!(res.is_err());
assert_eq!(res.unwrap_err().kind(), ErrorKind::DisplayHelp);
```


**Code Examples:**


```rust
# use clap_builder as clap;
# use clap::{Command, error::ErrorKind};
let res = Command::new("myprog")
.disable_help_flag(true)
.try_get_matches_from(vec![
"myprog", "-h"
]);
assert!(res.is_err());
assert_eq!(res.unwrap_err().kind(), ErrorKind::UnknownArgument);
```


```rust
# use clap_builder as clap;
# use clap::{Command, Arg, ArgAction, error::ErrorKind};
let mut cmd = Command::new("myprog")
// Change help short flag to `?`
.disable_help_flag(true)
.arg(
Arg::new("help")
.short('?')
.long("help")
.action(ArgAction::Help)
.help("Print help")
);

let res = cmd.try_get_matches_from_mut(vec![
"myprog", "-h"
]);
assert!(res.is_err());
assert_eq!(res.unwrap_err().kind(), ErrorKind::UnknownArgument);

let res = cmd.try_get_matches_from_mut(vec![
"myprog", "-?"
]);
assert!(res.is_err());
assert_eq!(res.unwrap_err().kind(), ErrorKind::DisplayHelp);
```


#### Fn: `disable_help_subcommand` (line 1617)

<!-- Source: repos/clap/clap_builder/src/builder/command.rs:1617 -->

<!-- Type: fn -->


Disables the `help` [`subcommand`].

<div class="warning">

**NOTE:** This choice is propagated to all child subcommands.

</div>

# Examples

```rust
# use clap_builder as clap;
# use clap::{Command, error::ErrorKind};
let res = Command::new("myprog")
.disable_help_subcommand(true)
// Normally, creating a subcommand causes a `help` subcommand to automatically
// be generated as well
.subcommand(Command::new("test"))
.try_get_matches_from(vec![
"myprog", "help"
]);
assert!(res.is_err());
assert_eq!(res.unwrap_err().kind(), ErrorKind::InvalidSubcommand);
```

[`subcommand`]: crate::Command::subcommand()


**Code Examples:**


```rust
# use clap_builder as clap;
# use clap::{Command, error::ErrorKind};
let res = Command::new("myprog")
.disable_help_subcommand(true)
// Normally, creating a subcommand causes a `help` subcommand to automatically
// be generated as well
.subcommand(Command::new("test"))
.try_get_matches_from(vec![
"myprog", "help"
]);
assert!(res.is_err());
assert_eq!(res.unwrap_err().kind(), ErrorKind::InvalidSubcommand);
```


#### Fn: `disable_colored_help` (line 1652)

<!-- Source: repos/clap/clap_builder/src/builder/command.rs:1652 -->

<!-- Type: fn -->


Disables colorized help messages.

<div class="warning">

**NOTE:** This choice is propagated to all child subcommands.

</div>

# Examples

```no_run
# use clap_builder as clap;
# use clap::Command;
Command::new("myprog")
.disable_colored_help(true)
.get_matches();
```


**Code Examples:**


```rust
# use clap_builder as clap;
# use clap::Command;
Command::new("myprog")
.disable_colored_help(true)
.get_matches();
```


#### Fn: `help_expected` (line 1678)

<!-- Source: repos/clap/clap_builder/src/builder/command.rs:1678 -->

<!-- Type: fn -->


Panic if help descriptions are omitted.

<div class="warning">

**NOTE:** When deriving [`Parser`][crate::Parser], you could instead check this at
compile-time with `#![deny(missing_docs)]`

</div>

<div class="warning">

**NOTE:** This choice is propagated to all child subcommands.

</div>

# Examples

```rust
# use clap_builder as clap;
# use clap::{Command, Arg};
Command::new("myprog")
.help_expected(true)
.arg(
Arg::new("foo").help("It does foo stuff")
// As required via `help_expected`, a help message was supplied
)
#    .get_matches();
```

# Panics

On debug builds:
```rust,no_run
# use clap_builder as clap;
# use clap::{Command, Arg};
Command::new("myapp")
.help_expected(true)
.arg(
Arg::new("foo")
// Someone forgot to put .about("...") here
// Since the setting `help_expected` is activated, this will lead to
// a panic (if you are in debug mode)
)
#   .get_matches();
```


**Code Examples:**


```rust
# use clap_builder as clap;
# use clap::{Command, Arg};
Command::new("myprog")
.help_expected(true)
.arg(
Arg::new("foo").help("It does foo stuff")
// As required via `help_expected`, a help message was supplied
)
#    .get_matches();
```


#### Fn: `hide_possible_values` (line 1741)

<!-- Source: repos/clap/clap_builder/src/builder/command.rs:1741 -->

<!-- Type: fn -->


Tells `clap` *not* to print possible values when displaying help information.

This can be useful if there are many values, or they are explained elsewhere.

To set this per argument, see
[`Arg::hide_possible_values`][crate::Arg::hide_possible_values].

<div class="warning">

**NOTE:** This choice is propagated to all child subcommands.

</div>


#### Fn: `infer_long_args` (line 1762)

<!-- Source: repos/clap/clap_builder/src/builder/command.rs:1762 -->

<!-- Type: fn -->


Allow partial matches of long arguments or their [aliases].

For example, to match an argument named `--test`, one could use `--t`, `--te`, `--tes`, and
`--test`.

<div class="warning">

**NOTE:** The match *must not* be ambiguous at all in order to succeed. i.e. to match
`--te` to `--test` there could not also be another argument or alias `--temp` because both
start with `--te`

</div>

<div class="warning">

**NOTE:** This choice is propagated to all child subcommands.

</div>

[aliases]: crate::Command::aliases()


#### Fn: `infer_subcommands` (line 1791)

<!-- Source: repos/clap/clap_builder/src/builder/command.rs:1791 -->

<!-- Type: fn -->


Allow partial matches of [subcommand] names and their [aliases].

For example, to match a subcommand named `test`, one could use `t`, `te`, `tes`, and
`test`.

<div class="warning">

**NOTE:** The match *must not* be ambiguous at all in order to succeed. i.e. to match `te`
to `test` there could not also be a subcommand or alias `temp` because both start with `te`

</div>

<div class="warning">

**WARNING:** This setting can interfere with [positional/free arguments], take care when
designing CLIs which allow inferred subcommands and have potential positional/free
arguments whose values could start with the same characters as subcommands. If this is the
case, it's recommended to use settings such as [`Command::args_conflicts_with_subcommands`] in
conjunction with this setting.

</div>

<div class="warning">

**NOTE:** This choice is propagated to all child subcommands.

</div>

# Examples

```no_run
# use clap_builder as clap;
# use clap::{Command, Arg};
let m = Command::new("prog")
.infer_subcommands(true)
.subcommand(Command::new("test"))
.get_matches_from(vec![
"prog", "te"
]);
assert_eq!(m.subcommand_name(), Some("test"));
```

[subcommand]: crate::Command::subcommand()
[positional/free arguments]: crate::Arg::index()
[aliases]: crate::Command::aliases()


**Code Examples:**


```rust
# use clap_builder as clap;
# use clap::{Command, Arg};
let m = Command::new("prog")
.infer_subcommands(true)
.subcommand(Command::new("test"))
.get_matches_from(vec![
"prog", "te"
]);
assert_eq!(m.subcommand_name(), Some("test"));
```


#### Impl: `Command` (line 1846)

<!-- Source: repos/clap/clap_builder/src/builder/command.rs:1846 -->

<!-- Type: impl -->


# Command-specific Settings

These apply only to the current command and are not inherited by subcommands.


#### Fn: `name` (line 1850)

<!-- Source: repos/clap/clap_builder/src/builder/command.rs:1850 -->

<!-- Type: fn -->


(Re)Sets the program's name.

See [`Command::new`] for more details.

# Examples

```ignore
let cmd = clap::command!()
.name("foo");

// continued logic goes here, such as `cmd.get_matches()` etc.
```


**Code Examples:**


```rust
let cmd = clap::command!()
.name("foo");

// continued logic goes here, such as `cmd.get_matches()` etc.
```


#### Fn: `bin_name` (line 1868)

<!-- Source: repos/clap/clap_builder/src/builder/command.rs:1868 -->

<!-- Type: fn -->


Overrides the runtime-determined name of the binary for help and error messages.

This should only be used when absolutely necessary, such as when the binary name for your
application is misleading, or perhaps *not* how the user should invoke your program.

<div class="warning">

**TIP:** When building things such as third party `cargo`
subcommands, this setting **should** be used!

</div>

<div class="warning">

**NOTE:** This *does not* change or set the name of the binary file on
disk. It only changes what clap thinks the name is for the purposes of
error or help messages.

</div>

# Examples

```rust
# use clap_builder as clap;
# use clap::Command;
Command::new("My Program")
.bin_name("my_binary")
# ;
```


**Code Examples:**


```rust
# use clap_builder as clap;
# use clap::Command;
Command::new("My Program")
.bin_name("my_binary")
# ;
```


#### Fn: `display_name` (line 1903)

<!-- Source: repos/clap/clap_builder/src/builder/command.rs:1903 -->

<!-- Type: fn -->


Overrides the runtime-determined display name of the program for help and error messages.

# Examples

```rust
# use clap_builder as clap;
# use clap::Command;
Command::new("My Program")
.display_name("my_program")
# ;
```


**Code Examples:**


```rust
# use clap_builder as clap;
# use clap::Command;
Command::new("My Program")
.display_name("my_program")
# ;
```


#### Fn: `author` (line 1920)

<!-- Source: repos/clap/clap_builder/src/builder/command.rs:1920 -->

<!-- Type: fn -->


Sets the author(s) for the help message.

<div class="warning">

**TIP:** Use `clap`s convenience macro [`crate_authors!`] to
automatically set your application's author(s) to the same thing as your
crate at compile time.

</div>

<div class="warning">

**NOTE:** A custom [`help_template`][Command::help_template] is needed for author to show
up.

</div>

# Examples

```rust
# use clap_builder as clap;
# use clap::Command;
Command::new("myprog")
.author("Me, me@mymain.com")
# ;
```


**Code Examples:**


```rust
# use clap_builder as clap;
# use clap::Command;
Command::new("myprog")
.author("Me, me@mymain.com")
# ;
```


#### Fn: `about` (line 1952)

<!-- Source: repos/clap/clap_builder/src/builder/command.rs:1952 -->

<!-- Type: fn -->


Sets the program's description for the short help (`-h`).

If [`Command::long_about`] is not specified, this message will be displayed for `--help`.

See also [`crate_description!`](crate::crate_description!).

# Examples

```rust
# use clap_builder as clap;
# use clap::Command;
Command::new("myprog")
.about("Does really amazing things for great people")
# ;
```


**Code Examples:**


```rust
# use clap_builder as clap;
# use clap::Command;
Command::new("myprog")
.about("Does really amazing things for great people")
# ;
```


#### Fn: `long_about` (line 1973)

<!-- Source: repos/clap/clap_builder/src/builder/command.rs:1973 -->

<!-- Type: fn -->


Sets the program's description for the long help (`--help`).

If not set, [`Command::about`] will be used for long help in addition to short help
(`-h`).

<div class="warning">

**NOTE:** Only [`Command::about`] (short format) is used in completion
script generation in order to be concise.

</div>

# Examples

```rust
# use clap_builder as clap;
# use clap::Command;
Command::new("myprog")
.long_about(
"Does really amazing things to great people. Now let's talk a little
more in depth about how this subcommand really works. It may take about
a few lines of text, but that's ok!")
# ;
```
[`Command::about`]: Command::about()


**Code Examples:**


```rust
# use clap_builder as clap;
# use clap::Command;
Command::new("myprog")
.long_about(
"Does really amazing things to great people. Now let's talk a little
more in depth about how this subcommand really works. It may take about
a few lines of text, but that's ok!")
# ;
```


#### Fn: `after_help` (line 2004)

<!-- Source: repos/clap/clap_builder/src/builder/command.rs:2004 -->

<!-- Type: fn -->


Free-form help text for after auto-generated short help (`-h`).

This is often used to describe how to use the arguments, caveats to be noted, or license
and contact information.

If [`Command::after_long_help`] is not specified, this message will be displayed for `--help`.

# Examples

```rust
# use clap_builder as clap;
# use clap::Command;
Command::new("myprog")
.after_help("Does really amazing things for great people... but be careful with -R!")
# ;
```



**Code Examples:**


```rust
# use clap_builder as clap;
# use clap::Command;
Command::new("myprog")
.after_help("Does really amazing things for great people... but be careful with -R!")
# ;
```


#### Fn: `after_long_help` (line 2027)

<!-- Source: repos/clap/clap_builder/src/builder/command.rs:2027 -->

<!-- Type: fn -->


Free-form help text for after auto-generated long help (`--help`).

This is often used to describe how to use the arguments, caveats to be noted, or license
and contact information.

If not set, [`Command::after_help`] will be used for long help in addition to short help
(`-h`).

# Examples

```rust
# use clap_builder as clap;
# use clap::Command;
Command::new("myprog")
.after_long_help("Does really amazing things to great people... but be careful with -R, \
like, for real, be careful with this!")
# ;
```


**Code Examples:**


```rust
# use clap_builder as clap;
# use clap::Command;
Command::new("myprog")
.after_long_help("Does really amazing things to great people... but be careful with -R, \
like, for real, be careful with this!")
# ;
```


#### Fn: `before_help` (line 2051)

<!-- Source: repos/clap/clap_builder/src/builder/command.rs:2051 -->

<!-- Type: fn -->


Free-form help text for before auto-generated short help (`-h`).

This is often used for header, copyright, or license information.

If [`Command::before_long_help`] is not specified, this message will be displayed for `--help`.

# Examples

```rust
# use clap_builder as clap;
# use clap::Command;
Command::new("myprog")
.before_help("Some info I'd like to appear before the help info")
# ;
```


**Code Examples:**


```rust
# use clap_builder as clap;
# use clap::Command;
Command::new("myprog")
.before_help("Some info I'd like to appear before the help info")
# ;
```


#### Fn: `before_long_help` (line 2072)

<!-- Source: repos/clap/clap_builder/src/builder/command.rs:2072 -->

<!-- Type: fn -->


Free-form help text for before auto-generated long help (`--help`).

This is often used for header, copyright, or license information.

If not set, [`Command::before_help`] will be used for long help in addition to short help
(`-h`).

# Examples

```rust
# use clap_builder as clap;
# use clap::Command;
Command::new("myprog")
.before_long_help("Some verbose and long info I'd like to appear before the help info")
# ;
```


**Code Examples:**


```rust
# use clap_builder as clap;
# use clap::Command;
Command::new("myprog")
.before_long_help("Some verbose and long info I'd like to appear before the help info")
# ;
```


#### Fn: `version` (line 2094)

<!-- Source: repos/clap/clap_builder/src/builder/command.rs:2094 -->

<!-- Type: fn -->


Sets the version for the short version (`-V`) and help messages.

If [`Command::long_version`] is not specified, this message will be displayed for `--version`.

<div class="warning">

**TIP:** Use `clap`s convenience macro [`crate_version!`] to
automatically set your application's version to the same thing as your
crate at compile time.

</div>

# Examples

```rust
# use clap_builder as clap;
# use clap::Command;
Command::new("myprog")
.version("v0.1.24")
# ;
```


**Code Examples:**


```rust
# use clap_builder as clap;
# use clap::Command;
Command::new("myprog")
.version("v0.1.24")
# ;
```


#### Fn: `long_version` (line 2121)

<!-- Source: repos/clap/clap_builder/src/builder/command.rs:2121 -->

<!-- Type: fn -->


Sets the version for the long version (`--version`) and help messages.

If [`Command::version`] is not specified, this message will be displayed for `-V`.

<div class="warning">

**TIP:** Use `clap`s convenience macro [`crate_version!`] to
automatically set your application's version to the same thing as your
crate at compile time.

</div>

# Examples

```rust
# use clap_builder as clap;
# use clap::Command;
Command::new("myprog")
.long_version(
"v0.1.24
commit: abcdef89726d
revision: 123
release: 2
binary: myprog")
# ;
```


**Code Examples:**


```rust
# use clap_builder as clap;
# use clap::Command;
Command::new("myprog")
.long_version(
"v0.1.24
commit: abcdef89726d
revision: 123
release: 2
binary: myprog")
# ;
```


#### Fn: `override_usage` (line 2153)

<!-- Source: repos/clap/clap_builder/src/builder/command.rs:2153 -->

<!-- Type: fn -->


Overrides the `clap` generated usage string for help and error messages.

<div class="warning">

**NOTE:** Using this setting disables `clap`s "context-aware" usage
strings. After this setting is set, this will be *the only* usage string
displayed to the user!

</div>

<div class="warning">

**NOTE:** Multiple usage lines may be present in the usage argument, but
some rules need to be followed to ensure the usage lines are formatted
correctly by the default help formatter:

- Do not indent the first usage line.
- Indent all subsequent usage lines with seven spaces.
- The last line must not end with a newline.

</div>

# Examples

```rust
# use clap_builder as clap;
# use clap::{Command, Arg};
Command::new("myprog")
.override_usage("myapp [-clDas] <some_file>")
# ;
```

Or for multiple usage lines:

```rust
# use clap_builder as clap;
# use clap::{Command, Arg};
Command::new("myprog")
.override_usage(
"myapp -X [-a] [-b] <file>\n       \
myapp -Y [-c] <file1> <file2>\n       \
myapp -Z [-d|-e]"
)
# ;
```


**Code Examples:**


```rust
# use clap_builder as clap;
# use clap::{Command, Arg};
Command::new("myprog")
.override_usage("myapp [-clDas] <some_file>")
# ;
```


```rust
# use clap_builder as clap;
# use clap::{Command, Arg};
Command::new("myprog")
.override_usage(
"myapp -X [-a] [-b] <file>\n       \
myapp -Y [-c] <file1> <file2>\n       \
myapp -Z [-d|-e]"
)
# ;
```


#### Fn: `override_help` (line 2204)

<!-- Source: repos/clap/clap_builder/src/builder/command.rs:2204 -->

<!-- Type: fn -->


Overrides the `clap` generated help message (both `-h` and `--help`).

This should only be used when the auto-generated message does not suffice.

<div class="warning">

**NOTE:** This **only** replaces the help message for the current
command, meaning if you are using subcommands, those help messages will
still be auto-generated unless you specify a [`Command::override_help`] for
them as well.

</div>

# Examples

```rust
# use clap_builder as clap;
# use clap::{Command, Arg};
Command::new("myapp")
.override_help("myapp v1.0\n\
Does awesome things\n\
(C) me@mail.com\n\n\

Usage: myapp <opts> <command>\n\n\

Options:\n\
-h, --help       Display this message\n\
-V, --version    Display version info\n\
-s <stuff>       Do something with stuff\n\
-v               Be verbose\n\n\

Commands:\n\
help             Print this message\n\
work             Do some work")
# ;
```


**Code Examples:**


```rust
# use clap_builder as clap;
# use clap::{Command, Arg};
Command::new("myapp")
.override_help("myapp v1.0\n\
Does awesome things\n\
(C) me@mail.com\n\n\

Usage: myapp <opts> <command>\n\n\

Options:\n\
-h, --help       Display this message\n\
-V, --version    Display version info\n\
-s <stuff>       Do something with stuff\n\
-v               Be verbose\n\n\

Commands:\n\
help             Print this message\n\
work             Do some work")
# ;
```


#### Fn: `help_template` (line 2246)

<!-- Source: repos/clap/clap_builder/src/builder/command.rs:2246 -->

<!-- Type: fn -->


Sets the help template to be used, overriding the default format.

Tags are given inside curly brackets.

Valid tags are:

* `{name}`                - Display name for the (sub-)command.
* `{bin}`                 - Binary name.(deprecated)
* `{version}`             - Version number.
* `{author}`              - Author information.
* `{author-with-newline}` - Author followed by `\n`.
* `{author-section}`      - Author preceded and followed by `\n`.
* `{about}`               - General description (from [`Command::about`] or
[`Command::long_about`]).
* `{about-with-newline}`  - About followed by `\n`.
* `{about-section}`       - About preceded and followed by '\n'.
* `{usage-heading}`       - Automatically generated usage heading.
* `{usage}`               - Automatically generated or given usage string.
* `{all-args}`            - Help for all arguments (options, flags, positional
arguments, and subcommands) including titles.
* `{options}`             - Help for options.
* `{positionals}`         - Help for positional arguments.
* `{subcommands}`         - Help for subcommands.
* `{tab}`                 - Standard tab sized used within clap
* `{after-help}`          - Help from [`Command::after_help`] or [`Command::after_long_help`].
* `{before-help}`         - Help from [`Command::before_help`] or [`Command::before_long_help`].

# Examples

For a very brief help:

```rust
# use clap_builder as clap;
# use clap::Command;
Command::new("myprog")
.version("1.0")
.help_template("{name} ({version}) - {usage}")
# ;
```

For showing more application context:

```rust
# use clap_builder as clap;
# use clap::Command;
Command::new("myprog")
.version("1.0")
.help_template("\
{before-help}{name} {version}
{author-with-newline}{about-with-newline}
{usage-heading} {usage}

{all-args}{after-help}
")
# ;
```
[`Command::about`]: Command::about()
[`Command::long_about`]: Command::long_about()
[`Command::after_help`]: Command::after_help()
[`Command::after_long_help`]: Command::after_long_help()
[`Command::before_help`]: Command::before_help()
[`Command::before_long_help`]: Command::before_long_help()


**Code Examples:**


```rust
# use clap_builder as clap;
# use clap::Command;
Command::new("myprog")
.version("1.0")
.help_template("{name} ({version}) - {usage}")
# ;
```


```rust
# use clap_builder as clap;
# use clap::Command;
Command::new("myprog")
.version("1.0")
.help_template("\
{before-help}{name} {version}
{author-with-newline}{about-with-newline}
{usage-heading} {usage}

{all-args}{after-help}
")
# ;
```


#### Fn: `flatten_help` (line 2345)

<!-- Source: repos/clap/clap_builder/src/builder/command.rs:2345 -->

<!-- Type: fn -->


Flatten subcommand help into the current command's help

This shows a summary of subcommands within the usage and help for the current command, similar to
`git stash --help` showing information on `push`, `pop`, etc.
To see more information, a user can still pass `--help` to the individual subcommands.


#### Fn: `next_help_heading` (line 2360)

<!-- Source: repos/clap/clap_builder/src/builder/command.rs:2360 -->

<!-- Type: fn -->


Set the default section heading for future args.

This will be used for any arg that hasn't had [`Arg::help_heading`] called.

This is useful if the default `Options` or `Arguments` headings are
not specific enough for one's use case.

For subcommands, see [`Command::subcommand_help_heading`]

[`Command::arg`]: Command::arg()
[`Arg::help_heading`]: crate::Arg::help_heading()


#### Fn: `next_display_order` (line 2378)

<!-- Source: repos/clap/clap_builder/src/builder/command.rs:2378 -->

<!-- Type: fn -->


Change the starting value for assigning future display orders for args.

This will be used for any arg that hasn't had [`Arg::display_order`] called.


#### Fn: `arg_required_else_help` (line 2388)

<!-- Source: repos/clap/clap_builder/src/builder/command.rs:2388 -->

<!-- Type: fn -->


Exit gracefully if no arguments are present (e.g. `$ myprog`).

<div class="warning">

**NOTE:** [`subcommands`] count as arguments

</div>

# Examples

```rust
# use clap_builder as clap;
# use clap::{Command};
Command::new("myprog")
.arg_required_else_help(true);
```

[`subcommands`]: crate::Command::subcommand()
[`Arg::default_value`]: crate::Arg::default_value()


**Code Examples:**


```rust
# use clap_builder as clap;
# use clap::{Command};
Command::new("myprog")
.arg_required_else_help(true);
```


#### Fn: `allow_missing_positional` (line 2455)

<!-- Source: repos/clap/clap_builder/src/builder/command.rs:2455 -->

<!-- Type: fn -->


Allows one to implement two styles of CLIs where positionals can be used out of order.

The first example is a CLI where the second to last positional argument is optional, but
the final positional argument is required. Such as `$ prog [optional] <required>` where one
of the two following usages is allowed:

* `$ prog [optional] <required>`
* `$ prog <required>`

This would otherwise not be allowed. This is useful when `[optional]` has a default value.

**Note:** when using this style of "missing positionals" the final positional *must* be
[required] if `--` will not be used to skip to the final positional argument.

**Note:** This style also only allows a single positional argument to be "skipped" without
the use of `--`. To skip more than one, see the second example.

The second example is when one wants to skip multiple optional positional arguments, and use
of the `--` operator is OK (but not required if all arguments will be specified anyways).

For example, imagine a CLI which has three positional arguments `[foo] [bar] [baz]...` where
`baz` accepts multiple values (similar to man `ARGS...` style training arguments).

With this setting the following invocations are possible:

* `$ prog foo bar baz1 baz2 baz3`
* `$ prog foo -- baz1 baz2 baz3`
* `$ prog -- baz1 baz2 baz3`

# Examples

Style number one from above:

```rust
# use clap_builder as clap;
# use clap::{Command, Arg};
// Assume there is an external subcommand named "subcmd"
let m = Command::new("myprog")
.allow_missing_positional(true)
.arg(Arg::new("arg1"))
.arg(Arg::new("arg2")
.required(true))
.get_matches_from(vec![
"prog", "other"
]);

assert_eq!(m.get_one::<String>("arg1"), None);
assert_eq!(m.get_one::<String>("arg2").unwrap(), "other");
```

Now the same example, but using a default value for the first optional positional argument

```rust
# use clap_builder as clap;
# use clap::{Command, Arg};
// Assume there is an external subcommand named "subcmd"
let m = Command::new("myprog")
.allow_missing_positional(true)
.arg(Arg::new("arg1")
.default_value("something"))
.arg(Arg::new("arg2")
.required(true))
.get_matches_from(vec![
"prog", "other"
]);

assert_eq!(m.get_one::<String>("arg1").unwrap(), "something");
assert_eq!(m.get_one::<String>("arg2").unwrap(), "other");
```

Style number two from above:

```rust
# use clap_builder as clap;
# use clap::{Command, Arg, ArgAction};
// Assume there is an external subcommand named "subcmd"
let m = Command::new("myprog")
.allow_missing_positional(true)
.arg(Arg::new("foo"))
.arg(Arg::new("bar"))
.arg(Arg::new("baz").action(ArgAction::Set).num_args(1..))
.get_matches_from(vec![
"prog", "foo", "bar", "baz1", "baz2", "baz3"
]);

assert_eq!(m.get_one::<String>("foo").unwrap(), "foo");
assert_eq!(m.get_one::<String>("bar").unwrap(), "bar");
assert_eq!(m.get_many::<String>("baz").unwrap().collect::<Vec<_>>(), &["baz1", "baz2", "baz3"]);
```

Now nofice if we don't specify `foo` or `baz` but use the `--` operator.

```rust
# use clap_builder as clap;
# use clap::{Command, Arg, ArgAction};
// Assume there is an external subcommand named "subcmd"
let m = Command::new("myprog")
.allow_missing_positional(true)
.arg(Arg::new("foo"))
.arg(Arg::new("bar"))
.arg(Arg::new("baz").action(ArgAction::Set).num_args(1..))
.get_matches_from(vec![
"prog", "--", "baz1", "baz2", "baz3"
]);

assert_eq!(m.get_one::<String>("foo"), None);
assert_eq!(m.get_one::<String>("bar"), None);
assert_eq!(m.get_many::<String>("baz").unwrap().collect::<Vec<_>>(), &["baz1", "baz2", "baz3"]);
```

[required]: crate::Arg::required()


**Code Examples:**


```rust
# use clap_builder as clap;
# use clap::{Command, Arg};
// Assume there is an external subcommand named "subcmd"
let m = Command::new("myprog")
.allow_missing_positional(true)
.arg(Arg::new("arg1"))
.arg(Arg::new("arg2")
.required(true))
.get_matches_from(vec![
"prog", "other"
]);

assert_eq!(m.get_one::<String>("arg1"), None);
assert_eq!(m.get_one::<String>("arg2").unwrap(), "other");
```


```rust
# use clap_builder as clap;
# use clap::{Command, Arg};
// Assume there is an external subcommand named "subcmd"
let m = Command::new("myprog")
.allow_missing_positional(true)
.arg(Arg::new("arg1")
.default_value("something"))
.arg(Arg::new("arg2")
.required(true))
.get_matches_from(vec![
"prog", "other"
]);

assert_eq!(m.get_one::<String>("arg1").unwrap(), "something");
assert_eq!(m.get_one::<String>("arg2").unwrap(), "other");
```


```rust
# use clap_builder as clap;
# use clap::{Command, Arg, ArgAction};
// Assume there is an external subcommand named "subcmd"
let m = Command::new("myprog")
.allow_missing_positional(true)
.arg(Arg::new("foo"))
.arg(Arg::new("bar"))
.arg(Arg::new("baz").action(ArgAction::Set).num_args(1..))
.get_matches_from(vec![
"prog", "foo", "bar", "baz1", "baz2", "baz3"
]);

assert_eq!(m.get_one::<String>("foo").unwrap(), "foo");
assert_eq!(m.get_one::<String>("bar").unwrap(), "bar");
assert_eq!(m.get_many::<String>("baz").unwrap().collect::<Vec<_>>(), &["baz1", "baz2", "baz3"]);
```


```rust
# use clap_builder as clap;
# use clap::{Command, Arg, ArgAction};
// Assume there is an external subcommand named "subcmd"
let m = Command::new("myprog")
.allow_missing_positional(true)
.arg(Arg::new("foo"))
.arg(Arg::new("bar"))
.arg(Arg::new("baz").action(ArgAction::Set).num_args(1..))
.get_matches_from(vec![
"prog", "--", "baz1", "baz2", "baz3"
]);

assert_eq!(m.get_one::<String>("foo"), None);
assert_eq!(m.get_one::<String>("bar"), None);
assert_eq!(m.get_many::<String>("baz").unwrap().collect::<Vec<_>>(), &["baz1", "baz2", "baz3"]);
```


#### Impl: `Command` (line 2576)

<!-- Source: repos/clap/clap_builder/src/builder/command.rs:2576 -->

<!-- Type: impl -->


# Subcommand-specific Settings


#### Fn: `short_flag` (line 2578)

<!-- Source: repos/clap/clap_builder/src/builder/command.rs:2578 -->

<!-- Type: fn -->


Sets the short version of the subcommand flag without the preceding `-`.

Allows the subcommand to be used as if it were an [`Arg::short`].

# Examples

```
# use clap_builder as clap;
# use clap::{Command, Arg, ArgAction};
let matches = Command::new("pacman")
.subcommand(
Command::new("sync").short_flag('S').arg(
Arg::new("search")
.short('s')
.long("search")
.action(ArgAction::SetTrue)
.help("search remote repositories for matching strings"),
),
)
.get_matches_from(vec!["pacman", "-Ss"]);

assert_eq!(matches.subcommand_name().unwrap(), "sync");
let sync_matches = matches.subcommand_matches("sync").unwrap();
assert!(sync_matches.get_flag("search"));
```
[`Arg::short`]: Arg::short()


**Code Examples:**


```rust
# use clap_builder as clap;
# use clap::{Command, Arg, ArgAction};
let matches = Command::new("pacman")
.subcommand(
Command::new("sync").short_flag('S').arg(
Arg::new("search")
.short('s')
.long("search")
.action(ArgAction::SetTrue)
.help("search remote repositories for matching strings"),
),
)
.get_matches_from(vec!["pacman", "-Ss"]);

assert_eq!(matches.subcommand_name().unwrap(), "sync");
let sync_matches = matches.subcommand_matches("sync").unwrap();
assert!(sync_matches.get_flag("search"));
```


#### Fn: `long_flag` (line 2610)

<!-- Source: repos/clap/clap_builder/src/builder/command.rs:2610 -->

<!-- Type: fn -->


Sets the long version of the subcommand flag without the preceding `--`.

Allows the subcommand to be used as if it were an [`Arg::long`].

<div class="warning">

**NOTE:** Any leading `-` characters will be stripped.

</div>

# Examples

To set `long_flag` use a word containing valid UTF-8 codepoints. If you supply a double leading
`--` such as `--sync` they will be stripped. Hyphens in the middle of the word; however,
will *not* be stripped (i.e. `sync-file` is allowed).

```rust
# use clap_builder as clap;
# use clap::{Command, Arg, ArgAction};
let matches = Command::new("pacman")
.subcommand(
Command::new("sync").long_flag("sync").arg(
Arg::new("search")
.short('s')
.long("search")
.action(ArgAction::SetTrue)
.help("search remote repositories for matching strings"),
),
)
.get_matches_from(vec!["pacman", "--sync", "--search"]);

assert_eq!(matches.subcommand_name().unwrap(), "sync");
let sync_matches = matches.subcommand_matches("sync").unwrap();
assert!(sync_matches.get_flag("search"));
```

[`Arg::long`]: Arg::long()


**Code Examples:**


```rust
# use clap_builder as clap;
# use clap::{Command, Arg, ArgAction};
let matches = Command::new("pacman")
.subcommand(
Command::new("sync").long_flag("sync").arg(
Arg::new("search")
.short('s')
.long("search")
.action(ArgAction::SetTrue)
.help("search remote repositories for matching strings"),
),
)
.get_matches_from(vec!["pacman", "--sync", "--search"]);

assert_eq!(matches.subcommand_name().unwrap(), "sync");
let sync_matches = matches.subcommand_matches("sync").unwrap();
assert!(sync_matches.get_flag("search"));
```


#### Fn: `alias` (line 2653)

<!-- Source: repos/clap/clap_builder/src/builder/command.rs:2653 -->

<!-- Type: fn -->


Sets a hidden alias to this subcommand.

This allows the subcommand to be accessed via *either* the original name, or this given
alias. This is more efficient and easier than creating multiple hidden subcommands as one
only needs to check for the existence of this command, and not all aliased variants.

<div class="warning">

**NOTE:** Aliases defined with this method are *hidden* from the help
message. If you're looking for aliases that will be displayed in the help
message, see [`Command::visible_alias`].

</div>

<div class="warning">

**NOTE:** When using aliases and checking for the existence of a
particular subcommand within an [`ArgMatches`] struct, one only needs to
search for the original name and not all aliases.

</div>

# Examples

```rust
# use clap_builder as clap;
# use clap::{Command, Arg, };
let m = Command::new("myprog")
.subcommand(Command::new("test")
.alias("do-stuff"))
.get_matches_from(vec!["myprog", "do-stuff"]);
assert_eq!(m.subcommand_name(), Some("test"));
```
[`Command::visible_alias`]: Command::visible_alias()


**Code Examples:**


```rust
# use clap_builder as clap;
# use clap::{Command, Arg, };
let m = Command::new("myprog")
.subcommand(Command::new("test")
.alias("do-stuff"))
.get_matches_from(vec!["myprog", "do-stuff"]);
assert_eq!(m.subcommand_name(), Some("test"));
```


#### Fn: `short_flag_alias` (line 2697)

<!-- Source: repos/clap/clap_builder/src/builder/command.rs:2697 -->

<!-- Type: fn -->


Add an alias, which functions as  "hidden" short flag subcommand

This will automatically dispatch as if this subcommand was used. This is more efficient,
and easier than creating multiple hidden subcommands as one only needs to check for the
existence of this command, and not all variants.

# Examples

```rust
# use clap_builder as clap;
# use clap::{Command, Arg, };
let m = Command::new("myprog")
.subcommand(Command::new("test").short_flag('t')
.short_flag_alias('d'))
.get_matches_from(vec!["myprog", "-d"]);
assert_eq!(m.subcommand_name(), Some("test"));
```


**Code Examples:**


```rust
# use clap_builder as clap;
# use clap::{Command, Arg, };
let m = Command::new("myprog")
.subcommand(Command::new("test").short_flag('t')
.short_flag_alias('d'))
.get_matches_from(vec!["myprog", "-d"]);
assert_eq!(m.subcommand_name(), Some("test"));
```


#### Fn: `long_flag_alias` (line 2725)

<!-- Source: repos/clap/clap_builder/src/builder/command.rs:2725 -->

<!-- Type: fn -->


Add an alias, which functions as a "hidden" long flag subcommand.

This will automatically dispatch as if this subcommand was used. This is more efficient,
and easier than creating multiple hidden subcommands as one only needs to check for the
existence of this command, and not all variants.

# Examples

```rust
# use clap_builder as clap;
# use clap::{Command, Arg, };
let m = Command::new("myprog")
.subcommand(Command::new("test").long_flag("test")
.long_flag_alias("testing"))
.get_matches_from(vec!["myprog", "--testing"]);
assert_eq!(m.subcommand_name(), Some("test"));
```


**Code Examples:**


```rust
# use clap_builder as clap;
# use clap::{Command, Arg, };
let m = Command::new("myprog")
.subcommand(Command::new("test").long_flag("test")
.long_flag_alias("testing"))
.get_matches_from(vec!["myprog", "--testing"]);
assert_eq!(m.subcommand_name(), Some("test"));
```


#### Fn: `aliases` (line 2752)

<!-- Source: repos/clap/clap_builder/src/builder/command.rs:2752 -->

<!-- Type: fn -->


Sets multiple hidden aliases to this subcommand.

This allows the subcommand to be accessed via *either* the original name or any of the
given aliases. This is more efficient, and easier than creating multiple hidden subcommands
as one only needs to check for the existence of this command and not all aliased variants.

<div class="warning">

**NOTE:** Aliases defined with this method are *hidden* from the help
message. If looking for aliases that will be displayed in the help
message, see [`Command::visible_aliases`].

</div>

<div class="warning">

**NOTE:** When using aliases and checking for the existence of a
particular subcommand within an [`ArgMatches`] struct, one only needs to
search for the original name and not all aliases.

</div>

# Examples

```rust
# use clap_builder as clap;
# use clap::{Command, Arg};
let m = Command::new("myprog")
.subcommand(Command::new("test")
.aliases(["do-stuff", "do-tests", "tests"]))
.arg(Arg::new("input")
.help("the file to add")
.required(false))
.get_matches_from(vec!["myprog", "do-tests"]);
assert_eq!(m.subcommand_name(), Some("test"));
```
[`Command::visible_aliases`]: Command::visible_aliases()


**Code Examples:**


```rust
# use clap_builder as clap;
# use clap::{Command, Arg};
let m = Command::new("myprog")
.subcommand(Command::new("test")
.aliases(["do-stuff", "do-tests", "tests"]))
.arg(Arg::new("input")
.help("the file to add")
.required(false))
.get_matches_from(vec!["myprog", "do-tests"]);
assert_eq!(m.subcommand_name(), Some("test"));
```


#### Fn: `short_flag_aliases` (line 2796)

<!-- Source: repos/clap/clap_builder/src/builder/command.rs:2796 -->

<!-- Type: fn -->


Add aliases, which function as "hidden" short flag subcommands.

These will automatically dispatch as if this subcommand was used. This is more efficient,
and easier than creating multiple hidden subcommands as one only needs to check for the
existence of this command, and not all variants.

# Examples

```rust
# use clap_builder as clap;
# use clap::{Command, Arg, };
let m = Command::new("myprog")
.subcommand(Command::new("test").short_flag('t')
.short_flag_aliases(['a', 'b', 'c']))
.arg(Arg::new("input")
.help("the file to add")
.required(false))
.get_matches_from(vec!["myprog", "-a"]);
assert_eq!(m.subcommand_name(), Some("test"));
```


**Code Examples:**


```rust
# use clap_builder as clap;
# use clap::{Command, Arg, };
let m = Command::new("myprog")
.subcommand(Command::new("test").short_flag('t')
.short_flag_aliases(['a', 'b', 'c']))
.arg(Arg::new("input")
.help("the file to add")
.required(false))
.get_matches_from(vec!["myprog", "-a"]);
assert_eq!(m.subcommand_name(), Some("test"));
```


#### Fn: `long_flag_aliases` (line 2825)

<!-- Source: repos/clap/clap_builder/src/builder/command.rs:2825 -->

<!-- Type: fn -->


Add aliases, which function as "hidden" long flag subcommands.

These will automatically dispatch as if this subcommand was used. This is more efficient,
and easier than creating multiple hidden subcommands as one only needs to check for the
existence of this command, and not all variants.

# Examples

```rust
# use clap_builder as clap;
# use clap::{Command, Arg, };
let m = Command::new("myprog")
.subcommand(Command::new("test").long_flag("test")
.long_flag_aliases(["testing", "testall", "test_all"]))
.arg(Arg::new("input")
.help("the file to add")
.required(false))
.get_matches_from(vec!["myprog", "--testing"]);
assert_eq!(m.subcommand_name(), Some("test"));
```


**Code Examples:**


```rust
# use clap_builder as clap;
# use clap::{Command, Arg, };
let m = Command::new("myprog")
.subcommand(Command::new("test").long_flag("test")
.long_flag_aliases(["testing", "testall", "test_all"]))
.arg(Arg::new("input")
.help("the file to add")
.required(false))
.get_matches_from(vec!["myprog", "--testing"]);
assert_eq!(m.subcommand_name(), Some("test"));
```


#### Fn: `visible_alias` (line 2853)

<!-- Source: repos/clap/clap_builder/src/builder/command.rs:2853 -->

<!-- Type: fn -->


Sets a visible alias to this subcommand.

This allows the subcommand to be accessed via *either* the
original name or the given alias. This is more efficient and easier
than creating hidden subcommands as one only needs to check for
the existence of this command and not all aliased variants.

<div class="warning">

**NOTE:** The alias defined with this method is *visible* from the help
message and displayed as if it were just another regular subcommand. If
looking for an alias that will not be displayed in the help message, see
[`Command::alias`].

</div>

<div class="warning">

**NOTE:** When using aliases and checking for the existence of a
particular subcommand within an [`ArgMatches`] struct, one only needs to
search for the original name and not all aliases.

</div>

# Examples

```rust
# use clap_builder as clap;
# use clap::{Command, Arg};
let m = Command::new("myprog")
.subcommand(Command::new("test")
.visible_alias("do-stuff"))
.get_matches_from(vec!["myprog", "do-stuff"]);
assert_eq!(m.subcommand_name(), Some("test"));
```
[`Command::alias`]: Command::alias()


**Code Examples:**


```rust
# use clap_builder as clap;
# use clap::{Command, Arg};
let m = Command::new("myprog")
.subcommand(Command::new("test")
.visible_alias("do-stuff"))
.get_matches_from(vec!["myprog", "do-stuff"]);
assert_eq!(m.subcommand_name(), Some("test"));
```


#### Fn: `visible_short_flag_alias` (line 2899)

<!-- Source: repos/clap/clap_builder/src/builder/command.rs:2899 -->

<!-- Type: fn -->


Add an alias, which functions as  "visible" short flag subcommand

This will automatically dispatch as if this subcommand was used. This is more efficient,
and easier than creating multiple hidden subcommands as one only needs to check for the
existence of this command, and not all variants.

See also [`Command::short_flag_alias`].

# Examples

```rust
# use clap_builder as clap;
# use clap::{Command, Arg, };
let m = Command::new("myprog")
.subcommand(Command::new("test").short_flag('t')
.visible_short_flag_alias('d'))
.get_matches_from(vec!["myprog", "-d"]);
assert_eq!(m.subcommand_name(), Some("test"));
```
[`Command::short_flag_alias`]: Command::short_flag_alias()


**Code Examples:**


```rust
# use clap_builder as clap;
# use clap::{Command, Arg, };
let m = Command::new("myprog")
.subcommand(Command::new("test").short_flag('t')
.visible_short_flag_alias('d'))
.get_matches_from(vec!["myprog", "-d"]);
assert_eq!(m.subcommand_name(), Some("test"));
```


#### Fn: `visible_long_flag_alias` (line 2930)

<!-- Source: repos/clap/clap_builder/src/builder/command.rs:2930 -->

<!-- Type: fn -->


Add an alias, which functions as a "visible" long flag subcommand.

This will automatically dispatch as if this subcommand was used. This is more efficient,
and easier than creating multiple hidden subcommands as one only needs to check for the
existence of this command, and not all variants.

See also [`Command::long_flag_alias`].

# Examples

```rust
# use clap_builder as clap;
# use clap::{Command, Arg, };
let m = Command::new("myprog")
.subcommand(Command::new("test").long_flag("test")
.visible_long_flag_alias("testing"))
.get_matches_from(vec!["myprog", "--testing"]);
assert_eq!(m.subcommand_name(), Some("test"));
```
[`Command::long_flag_alias`]: Command::long_flag_alias()


**Code Examples:**


```rust
# use clap_builder as clap;
# use clap::{Command, Arg, };
let m = Command::new("myprog")
.subcommand(Command::new("test").long_flag("test")
.visible_long_flag_alias("testing"))
.get_matches_from(vec!["myprog", "--testing"]);
assert_eq!(m.subcommand_name(), Some("test"));
```


#### Fn: `visible_aliases` (line 2960)

<!-- Source: repos/clap/clap_builder/src/builder/command.rs:2960 -->

<!-- Type: fn -->


Sets multiple visible aliases to this subcommand.

This allows the subcommand to be accessed via *either* the
original name or any of the given aliases. This is more efficient and easier
than creating multiple hidden subcommands as one only needs to check for
the existence of this command and not all aliased variants.

<div class="warning">

**NOTE:** The alias defined with this method is *visible* from the help
message and displayed as if it were just another regular subcommand. If
looking for an alias that will not be displayed in the help message, see
[`Command::alias`].

</div>

<div class="warning">

**NOTE:** When using aliases, and checking for the existence of a
particular subcommand within an [`ArgMatches`] struct, one only needs to
search for the original name and not all aliases.

</div>

# Examples

```rust
# use clap_builder as clap;
# use clap::{Command, Arg, };
let m = Command::new("myprog")
.subcommand(Command::new("test")
.visible_aliases(["do-stuff", "tests"]))
.get_matches_from(vec!["myprog", "do-stuff"]);
assert_eq!(m.subcommand_name(), Some("test"));
```
[`Command::alias`]: Command::alias()


**Code Examples:**


```rust
# use clap_builder as clap;
# use clap::{Command, Arg, };
let m = Command::new("myprog")
.subcommand(Command::new("test")
.visible_aliases(["do-stuff", "tests"]))
.get_matches_from(vec!["myprog", "do-stuff"]);
assert_eq!(m.subcommand_name(), Some("test"));
```


#### Fn: `visible_short_flag_aliases` (line 3003)

<!-- Source: repos/clap/clap_builder/src/builder/command.rs:3003 -->

<!-- Type: fn -->


Add aliases, which function as *visible* short flag subcommands.

See [`Command::short_flag_aliases`].

# Examples

```rust
# use clap_builder as clap;
# use clap::{Command, Arg, };
let m = Command::new("myprog")
.subcommand(Command::new("test").short_flag('b')
.visible_short_flag_aliases(['t']))
.get_matches_from(vec!["myprog", "-t"]);
assert_eq!(m.subcommand_name(), Some("test"));
```
[`Command::short_flag_aliases`]: Command::short_flag_aliases()


**Code Examples:**


```rust
# use clap_builder as clap;
# use clap::{Command, Arg, };
let m = Command::new("myprog")
.subcommand(Command::new("test").short_flag('b')
.visible_short_flag_aliases(['t']))
.get_matches_from(vec!["myprog", "-t"]);
assert_eq!(m.subcommand_name(), Some("test"));
```


#### Fn: `visible_long_flag_aliases` (line 3028)

<!-- Source: repos/clap/clap_builder/src/builder/command.rs:3028 -->

<!-- Type: fn -->


Add aliases, which function as *visible* long flag subcommands.

See [`Command::long_flag_aliases`].

# Examples

```rust
# use clap_builder as clap;
# use clap::{Command, Arg, };
let m = Command::new("myprog")
.subcommand(Command::new("test").long_flag("test")
.visible_long_flag_aliases(["testing", "testall", "test_all"]))
.get_matches_from(vec!["myprog", "--testing"]);
assert_eq!(m.subcommand_name(), Some("test"));
```
[`Command::long_flag_aliases`]: Command::long_flag_aliases()


**Code Examples:**


```rust
# use clap_builder as clap;
# use clap::{Command, Arg, };
let m = Command::new("myprog")
.subcommand(Command::new("test").long_flag("test")
.visible_long_flag_aliases(["testing", "testall", "test_all"]))
.get_matches_from(vec!["myprog", "--testing"]);
assert_eq!(m.subcommand_name(), Some("test"));
```


#### Fn: `display_order` (line 3055)

<!-- Source: repos/clap/clap_builder/src/builder/command.rs:3055 -->

<!-- Type: fn -->


Set the placement of this subcommand within the help.

Subcommands with a lower value will be displayed first in the help message.
Those with the same display order will be sorted.

`Command`s are automatically assigned a display order based on the order they are added to
their parent [`Command`].
Overriding this is helpful when the order commands are added in isn't the same as the
display order, whether in one-off cases or to automatically sort commands.

# Examples

```rust
# #[cfg(feature = "help")] {
# use clap_builder as clap;
# use clap::{Command, };
let m = Command::new("cust-ord")
.subcommand(Command::new("beta")
.display_order(0)  // Sort
.about("Some help and text"))
.subcommand(Command::new("alpha")
.display_order(0)  // Sort
.about("I should be first!"))
.get_matches_from(vec![
"cust-ord", "--help"
]);
# }
```

The above example displays the following help message

```text
cust-ord

Usage: cust-ord [OPTIONS]

Commands:
alpha    I should be first!
beta     Some help and text
help     Print help for the subcommand(s)

Options:
-h, --help       Print help
-V, --version    Print version
```


**Code Examples:**


```rust
# #[cfg(feature = "help")] {
# use clap_builder as clap;
# use clap::{Command, };
let m = Command::new("cust-ord")
.subcommand(Command::new("beta")
.display_order(0)  // Sort
.about("Some help and text"))
.subcommand(Command::new("alpha")
.display_order(0)  // Sort
.about("I should be first!"))
.get_matches_from(vec![
"cust-ord", "--help"
]);
# }
```


#### Fn: `hide` (line 3107)

<!-- Source: repos/clap/clap_builder/src/builder/command.rs:3107 -->

<!-- Type: fn -->


Specifies that this [`subcommand`] should be hidden from help messages

# Examples

```rust
# use clap_builder as clap;
# use clap::{Command, Arg};
Command::new("myprog")
.subcommand(
Command::new("test").hide(true)
)
# ;
```

[`subcommand`]: crate::Command::subcommand()


**Code Examples:**


```rust
# use clap_builder as clap;
# use clap::{Command, Arg};
Command::new("myprog")
.subcommand(
Command::new("test").hide(true)
)
# ;
```


#### Fn: `subcommand_required` (line 3131)

<!-- Source: repos/clap/clap_builder/src/builder/command.rs:3131 -->

<!-- Type: fn -->


If no [`subcommand`] is present at runtime, error and exit gracefully.

# Examples

```rust
# use clap_builder as clap;
# use clap::{Command, error::ErrorKind};
let err = Command::new("myprog")
.subcommand_required(true)
.subcommand(Command::new("test"))
.try_get_matches_from(vec![
"myprog",
]);
assert!(err.is_err());
assert_eq!(err.unwrap_err().kind(), ErrorKind::MissingSubcommand);
# ;
```

[`subcommand`]: crate::Command::subcommand()


**Code Examples:**


```rust
# use clap_builder as clap;
# use clap::{Command, error::ErrorKind};
let err = Command::new("myprog")
.subcommand_required(true)
.subcommand(Command::new("test"))
.try_get_matches_from(vec![
"myprog",
]);
assert!(err.is_err());
assert_eq!(err.unwrap_err().kind(), ErrorKind::MissingSubcommand);
# ;
```


#### Fn: `allow_external_subcommands` (line 3158)

<!-- Source: repos/clap/clap_builder/src/builder/command.rs:3158 -->

<!-- Type: fn -->


Assume unexpected positional arguments are a [`subcommand`].

Arguments will be stored in the `""` argument in the [`ArgMatches`]

<div class="warning">

**NOTE:** Use this setting with caution,
as a truly unexpected argument (i.e. one that is *NOT* an external subcommand)
will **not** cause an error and instead be treated as a potential subcommand.
One should check for such cases manually and inform the user appropriately.

</div>

<div class="warning">

**NOTE:** A built-in subcommand will be parsed as an external subcommand when escaped with
`--`.

</div>

# Examples

```rust
# use clap_builder as clap;
# use std::ffi::OsString;
# use clap::Command;
// Assume there is an external subcommand named "subcmd"
let m = Command::new("myprog")
.allow_external_subcommands(true)
.get_matches_from(vec![
"myprog", "subcmd", "--option", "value", "-fff", "--flag"
]);

// All trailing arguments will be stored under the subcommand's sub-matches using an empty
// string argument name
match m.subcommand() {
Some((external, ext_m)) => {
let ext_args: Vec<_> = ext_m.get_many::<OsString>("").unwrap().collect();
assert_eq!(external, "subcmd");
assert_eq!(ext_args, ["--option", "value", "-fff", "--flag"]);
},
_ => {},
}
```

[`subcommand`]: crate::Command::subcommand()
[`ArgMatches`]: crate::ArgMatches
[`ErrorKind::UnknownArgument`]: crate::error::ErrorKind::UnknownArgument


**Code Examples:**


```rust
# use clap_builder as clap;
# use std::ffi::OsString;
# use clap::Command;
// Assume there is an external subcommand named "subcmd"
let m = Command::new("myprog")
.allow_external_subcommands(true)
.get_matches_from(vec![
"myprog", "subcmd", "--option", "value", "-fff", "--flag"
]);

// All trailing arguments will be stored under the subcommand's sub-matches using an empty
// string argument name
match m.subcommand() {
Some((external, ext_m)) => {
let ext_args: Vec<_> = ext_m.get_many::<OsString>("").unwrap().collect();
assert_eq!(external, "subcmd");
assert_eq!(ext_args, ["--option", "value", "-fff", "--flag"]);
},
_ => {},
}
```


#### Fn: `external_subcommand_value_parser` (line 3214)

<!-- Source: repos/clap/clap_builder/src/builder/command.rs:3214 -->

<!-- Type: fn -->


Specifies how to parse external subcommand arguments.

The default parser is for `OsString`.  This can be used to switch it to `String` or another
type.

<div class="warning">

**NOTE:** Setting this requires [`Command::allow_external_subcommands`]

</div>

# Examples

```rust
# #[cfg(unix)] {
# use clap_builder as clap;
# use std::ffi::OsString;
# use clap::Command;
# use clap::value_parser;
// Assume there is an external subcommand named "subcmd"
let m = Command::new("myprog")
.allow_external_subcommands(true)
.get_matches_from(vec![
"myprog", "subcmd", "--option", "value", "-fff", "--flag"
]);

// All trailing arguments will be stored under the subcommand's sub-matches using an empty
// string argument name
match m.subcommand() {
Some((external, ext_m)) => {
let ext_args: Vec<_> = ext_m.get_many::<OsString>("").unwrap().collect();
assert_eq!(external, "subcmd");
assert_eq!(ext_args, ["--option", "value", "-fff", "--flag"]);
},
_ => {},
}
# }
```

```rust
# use clap_builder as clap;
# use clap::Command;
# use clap::value_parser;
// Assume there is an external subcommand named "subcmd"
let m = Command::new("myprog")
.external_subcommand_value_parser(value_parser!(String))
.get_matches_from(vec![
"myprog", "subcmd", "--option", "value", "-fff", "--flag"
]);

// All trailing arguments will be stored under the subcommand's sub-matches using an empty
// string argument name
match m.subcommand() {
Some((external, ext_m)) => {
let ext_args: Vec<_> = ext_m.get_many::<String>("").unwrap().collect();
assert_eq!(external, "subcmd");
assert_eq!(ext_args, ["--option", "value", "-fff", "--flag"]);
},
_ => {},
}
```

[`subcommands`]: crate::Command::subcommand()


**Code Examples:**


```rust
# #[cfg(unix)] {
# use clap_builder as clap;
# use std::ffi::OsString;
# use clap::Command;
# use clap::value_parser;
// Assume there is an external subcommand named "subcmd"
let m = Command::new("myprog")
.allow_external_subcommands(true)
.get_matches_from(vec![
"myprog", "subcmd", "--option", "value", "-fff", "--flag"
]);

// All trailing arguments will be stored under the subcommand's sub-matches using an empty
// string argument name
match m.subcommand() {
Some((external, ext_m)) => {
let ext_args: Vec<_> = ext_m.get_many::<OsString>("").unwrap().collect();
assert_eq!(external, "subcmd");
assert_eq!(ext_args, ["--option", "value", "-fff", "--flag"]);
},
_ => {},
}
# }
```


```rust
# use clap_builder as clap;
# use clap::Command;
# use clap::value_parser;
// Assume there is an external subcommand named "subcmd"
let m = Command::new("myprog")
.external_subcommand_value_parser(value_parser!(String))
.get_matches_from(vec![
"myprog", "subcmd", "--option", "value", "-fff", "--flag"
]);

// All trailing arguments will be stored under the subcommand's sub-matches using an empty
// string argument name
match m.subcommand() {
Some((external, ext_m)) => {
let ext_args: Vec<_> = ext_m.get_many::<String>("").unwrap().collect();
assert_eq!(external, "subcmd");
assert_eq!(ext_args, ["--option", "value", "-fff", "--flag"]);
},
_ => {},
}
```


#### Fn: `args_conflicts_with_subcommands` (line 3285)

<!-- Source: repos/clap/clap_builder/src/builder/command.rs:3285 -->

<!-- Type: fn -->


Specifies that use of an argument prevents the use of [`subcommands`].

By default `clap` allows arguments between subcommands such
as `<cmd> [cmd_args] <subcmd> [subcmd_args] <subsubcmd> [subsubcmd_args]`.

This setting disables that functionality and says that arguments can
only follow the *final* subcommand. For instance using this setting
makes only the following invocations possible:

* `<cmd> <subcmd> <subsubcmd> [subsubcmd_args]`
* `<cmd> <subcmd> [subcmd_args]`
* `<cmd> [cmd_args]`

# Examples

```rust
# use clap_builder as clap;
# use clap::Command;
Command::new("myprog")
.args_conflicts_with_subcommands(true);
```

[`subcommands`]: crate::Command::subcommand()


**Code Examples:**


```rust
# use clap_builder as clap;
# use clap::Command;
Command::new("myprog")
.args_conflicts_with_subcommands(true);
```


#### Fn: `subcommand_precedence_over_arg` (line 3316)

<!-- Source: repos/clap/clap_builder/src/builder/command.rs:3316 -->

<!-- Type: fn -->


Prevent subcommands from being consumed as an arguments value.

By default, if an option taking multiple values is followed by a subcommand, the
subcommand will be parsed as another value.

```text
cmd --foo val1 val2 subcommand
--------- ----------
values   another value
```

This setting instructs the parser to stop when encountering a subcommand instead of
greedily consuming arguments.

```text
cmd --foo val1 val2 subcommand
--------- ----------
values   subcommand
```

# Examples

```rust
# use clap_builder as clap;
# use clap::{Command, Arg, ArgAction};
let cmd = Command::new("cmd").subcommand(Command::new("sub")).arg(
Arg::new("arg")
.long("arg")
.num_args(1..)
.action(ArgAction::Set),
);

let matches = cmd
.clone()
.try_get_matches_from(&["cmd", "--arg", "1", "2", "3", "sub"])
.unwrap();
assert_eq!(
matches.get_many::<String>("arg").unwrap().collect::<Vec<_>>(),
&["1", "2", "3", "sub"]
);
assert!(matches.subcommand_matches("sub").is_none());

let matches = cmd
.subcommand_precedence_over_arg(true)
.try_get_matches_from(&["cmd", "--arg", "1", "2", "3", "sub"])
.unwrap();
assert_eq!(
matches.get_many::<String>("arg").unwrap().collect::<Vec<_>>(),
&["1", "2", "3"]
);
assert!(matches.subcommand_matches("sub").is_some());
```


**Code Examples:**


```rust
This setting instructs the parser to stop when encountering a subcommand instead of
greedily consuming arguments.
```


```rust
# Examples
```


#### Fn: `subcommand_negates_reqs` (line 3376)

<!-- Source: repos/clap/clap_builder/src/builder/command.rs:3376 -->

<!-- Type: fn -->


Allows [`subcommands`] to override all requirements of the parent command.

For example, if you had a subcommand or top level application with a required argument
that is only required as long as there is no subcommand present,
using this setting would allow you to set those arguments to [`Arg::required(true)`]
and yet receive no error so long as the user uses a valid subcommand instead.

<div class="warning">

**NOTE:** This defaults to false (using subcommand does *not* negate requirements)

</div>

# Examples

This first example shows that it is an error to not use a required argument

```rust
# use clap_builder as clap;
# use clap::{Command, Arg, error::ErrorKind};
let err = Command::new("myprog")
.subcommand_negates_reqs(true)
.arg(Arg::new("opt").required(true))
.subcommand(Command::new("test"))
.try_get_matches_from(vec![
"myprog"
]);
assert!(err.is_err());
assert_eq!(err.unwrap_err().kind(), ErrorKind::MissingRequiredArgument);
# ;
```

This next example shows that it is no longer error to not use a required argument if a
valid subcommand is used.

```rust
# use clap_builder as clap;
# use clap::{Command, Arg, error::ErrorKind};
let noerr = Command::new("myprog")
.subcommand_negates_reqs(true)
.arg(Arg::new("opt").required(true))
.subcommand(Command::new("test"))
.try_get_matches_from(vec![
"myprog", "test"
]);
assert!(noerr.is_ok());
# ;
```

[`Arg::required(true)`]: crate::Arg::required()
[`subcommands`]: crate::Command::subcommand()


**Code Examples:**


```rust
# use clap_builder as clap;
# use clap::{Command, Arg, error::ErrorKind};
let err = Command::new("myprog")
.subcommand_negates_reqs(true)
.arg(Arg::new("opt").required(true))
.subcommand(Command::new("test"))
.try_get_matches_from(vec![
"myprog"
]);
assert!(err.is_err());
assert_eq!(err.unwrap_err().kind(), ErrorKind::MissingRequiredArgument);
# ;
```


```rust
# use clap_builder as clap;
# use clap::{Command, Arg, error::ErrorKind};
let noerr = Command::new("myprog")
.subcommand_negates_reqs(true)
.arg(Arg::new("opt").required(true))
.subcommand(Command::new("test"))
.try_get_matches_from(vec![
"myprog", "test"
]);
assert!(noerr.is_ok());
# ;
```


#### Fn: `multicall` (line 3435)

<!-- Source: repos/clap/clap_builder/src/builder/command.rs:3435 -->

<!-- Type: fn -->


Multiple-personality program dispatched on the binary name (`argv[0]`)

A "multicall" executable is a single executable
that contains a variety of applets,
and decides which applet to run based on the name of the file.
The executable can be called from different names by creating hard links
or symbolic links to it.

This is desirable for:
- Easy distribution, a single binary that can install hardlinks to access the different
personalities.
- Minimal binary size by sharing common code (e.g. standard library, clap)
- Custom shells or REPLs where there isn't a single top-level command

Setting `multicall` will cause
- `argv[0]` to be stripped to the base name and parsed as the first argument, as if
[`Command::no_binary_name`][Command::no_binary_name] was set.
- Help and errors to report subcommands as if they were the top-level command

When the subcommand is not present, there are several strategies you may employ, depending
on your needs:
- Let the error percolate up normally
- Print a specialized error message using the
[`Error::context`][crate::Error::context]
- Print the [help][Command::write_help] but this might be ambiguous
- Disable `multicall` and re-parse it
- Disable `multicall` and re-parse it with a specific subcommand

When detecting the error condition, the [`ErrorKind`] isn't sufficient as a sub-subcommand
might report the same error.  Enable
[`allow_external_subcommands`][Command::allow_external_subcommands] if you want to specifically
get the unrecognized binary name.

<div class="warning">

**NOTE:** Multicall can't be used with [`no_binary_name`] since they interpret
the command name in incompatible ways.

</div>

<div class="warning">

**NOTE:** The multicall command cannot have arguments.

</div>

<div class="warning">

**NOTE:** Applets are slightly semantically different from subcommands,
so it's recommended to use [`Command::subcommand_help_heading`] and
[`Command::subcommand_value_name`] to change the descriptive text as above.

</div>

# Examples

`hostname` is an example of a multicall executable.
Both `hostname` and `dnsdomainname` are provided by the same executable
and which behaviour to use is based on the executable file name.

This is desirable when the executable has a primary purpose
but there is related functionality that would be convenient to provide
and implement it to be in the same executable.

The name of the cmd is essentially unused
and may be the same as the name of a subcommand.

The names of the immediate subcommands of the Command
are matched against the basename of the first argument,
which is conventionally the path of the executable.

This does not allow the subcommand to be passed as the first non-path argument.

```rust
# use clap_builder as clap;
# use clap::{Command, error::ErrorKind};
let mut cmd = Command::new("hostname")
.multicall(true)
.subcommand(Command::new("hostname"))
.subcommand(Command::new("dnsdomainname"));
let m = cmd.try_get_matches_from_mut(&["/usr/bin/hostname", "dnsdomainname"]);
assert!(m.is_err());
assert_eq!(m.unwrap_err().kind(), ErrorKind::UnknownArgument);
let m = cmd.get_matches_from(&["/usr/bin/dnsdomainname"]);
assert_eq!(m.subcommand_name(), Some("dnsdomainname"));
```

Busybox is another common example of a multicall executable
with a subcommmand for each applet that can be run directly,
e.g. with the `cat` applet being run by running `busybox cat`,
or with `cat` as a link to the `busybox` binary.

This is desirable when the launcher program has additional options
or it is useful to run the applet without installing a symlink
e.g. to test the applet without installing it
or there may already be a command of that name installed.

To make an applet usable as both a multicall link and a subcommand
the subcommands must be defined both in the top-level Command
and as subcommands of the "main" applet.

```rust
# use clap_builder as clap;
# use clap::Command;
fn applet_commands() -> [Command; 2] {
[Command::new("true"), Command::new("false")]
}
let mut cmd = Command::new("busybox")
.multicall(true)
.subcommand(
Command::new("busybox")
.subcommand_value_name("APPLET")
.subcommand_help_heading("APPLETS")
.subcommands(applet_commands()),
)
.subcommands(applet_commands());
// When called from the executable's canonical name
// its applets can be matched as subcommands.
let m = cmd.try_get_matches_from_mut(&["/usr/bin/busybox", "true"]).unwrap();
assert_eq!(m.subcommand_name(), Some("busybox"));
assert_eq!(m.subcommand().unwrap().1.subcommand_name(), Some("true"));
// When called from a link named after an applet that applet is matched.
let m = cmd.get_matches_from(&["/usr/bin/true"]);
assert_eq!(m.subcommand_name(), Some("true"));
```

[`no_binary_name`]: crate::Command::no_binary_name
[`Command::subcommand_value_name`]: crate::Command::subcommand_value_name
[`Command::subcommand_help_heading`]: crate::Command::subcommand_help_heading


**Code Examples:**


```rust
# use clap_builder as clap;
# use clap::{Command, error::ErrorKind};
let mut cmd = Command::new("hostname")
.multicall(true)
.subcommand(Command::new("hostname"))
.subcommand(Command::new("dnsdomainname"));
let m = cmd.try_get_matches_from_mut(&["/usr/bin/hostname", "dnsdomainname"]);
assert!(m.is_err());
assert_eq!(m.unwrap_err().kind(), ErrorKind::UnknownArgument);
let m = cmd.get_matches_from(&["/usr/bin/dnsdomainname"]);
assert_eq!(m.subcommand_name(), Some("dnsdomainname"));
```


```rust
# use clap_builder as clap;
# use clap::Command;
fn applet_commands() -> [Command; 2] {
[Command::new("true"), Command::new("false")]
}
let mut cmd = Command::new("busybox")
.multicall(true)
.subcommand(
Command::new("busybox")
.subcommand_value_name("APPLET")
.subcommand_help_heading("APPLETS")
.subcommands(applet_commands()),
)
.subcommands(applet_commands());
// When called from the executable's canonical name
// its applets can be matched as subcommands.
let m = cmd.try_get_matches_from_mut(&["/usr/bin/busybox", "true"]).unwrap();
assert_eq!(m.subcommand_name(), Some("busybox"));
assert_eq!(m.subcommand().unwrap().1.subcommand_name(), Some("true"));
// When called from a link named after an applet that applet is matched.
let m = cmd.get_matches_from(&["/usr/bin/true"]);
assert_eq!(m.subcommand_name(), Some("true"));
```


#### Fn: `subcommand_value_name` (line 3573)

<!-- Source: repos/clap/clap_builder/src/builder/command.rs:3573 -->

<!-- Type: fn -->


Sets the value name used for subcommands when printing usage and help.

By default, this is "COMMAND".

See also [`Command::subcommand_help_heading`]

# Examples

```rust
# use clap_builder as clap;
# use clap::{Command, Arg};
Command::new("myprog")
.subcommand(Command::new("sub1"))
.print_help()
# ;
```

will produce

```text
myprog

Usage: myprog [COMMAND]

Commands:
help    Print this message or the help of the given subcommand(s)
sub1

Options:
-h, --help       Print help
-V, --version    Print version
```

but usage of `subcommand_value_name`

```rust
# use clap_builder as clap;
# use clap::{Command, Arg};
Command::new("myprog")
.subcommand(Command::new("sub1"))
.subcommand_value_name("THING")
.print_help()
# ;
```

will produce

```text
myprog

Usage: myprog [THING]

Commands:
help    Print this message or the help of the given subcommand(s)
sub1

Options:
-h, --help       Print help
-V, --version    Print version
```


**Code Examples:**


```rust
# use clap_builder as clap;
# use clap::{Command, Arg};
Command::new("myprog")
.subcommand(Command::new("sub1"))
.print_help()
# ;
```


```rust
but usage of `subcommand_value_name`
```


```rust
will produce
```


#### Fn: `subcommand_help_heading` (line 3639)

<!-- Source: repos/clap/clap_builder/src/builder/command.rs:3639 -->

<!-- Type: fn -->


Sets the help heading used for subcommands when printing usage and help.

By default, this is "Commands".

See also [`Command::subcommand_value_name`]

# Examples

```rust
# use clap_builder as clap;
# use clap::{Command, Arg};
Command::new("myprog")
.subcommand(Command::new("sub1"))
.print_help()
# ;
```

will produce

```text
myprog

Usage: myprog [COMMAND]

Commands:
help    Print this message or the help of the given subcommand(s)
sub1

Options:
-h, --help       Print help
-V, --version    Print version
```

but usage of `subcommand_help_heading`

```rust
# use clap_builder as clap;
# use clap::{Command, Arg};
Command::new("myprog")
.subcommand(Command::new("sub1"))
.subcommand_help_heading("Things")
.print_help()
# ;
```

will produce

```text
myprog

Usage: myprog [COMMAND]

Things:
help    Print this message or the help of the given subcommand(s)
sub1

Options:
-h, --help       Print help
-V, --version    Print version
```


**Code Examples:**


```rust
# use clap_builder as clap;
# use clap::{Command, Arg};
Command::new("myprog")
.subcommand(Command::new("sub1"))
.print_help()
# ;
```


```rust
but usage of `subcommand_help_heading`
```


```rust
will produce
```


#### Impl: `Command` (line 3706)

<!-- Source: repos/clap/clap_builder/src/builder/command.rs:3706 -->

<!-- Type: impl -->


# Reflection


#### Fn: `get_display_name` (line 3728)

<!-- Source: repos/clap/clap_builder/src/builder/command.rs:3728 -->

<!-- Type: fn -->


Get the name of the binary.


#### Fn: `get_bin_name` (line 3734)

<!-- Source: repos/clap/clap_builder/src/builder/command.rs:3734 -->

<!-- Type: fn -->


Get the name of the binary.


#### Fn: `get_bin_name_fallback` (line 3740)

<!-- Source: repos/clap/clap_builder/src/builder/command.rs:3740 -->

<!-- Type: fn -->


Get the name of the binary.


#### Fn: `set_bin_name` (line 3746)

<!-- Source: repos/clap/clap_builder/src/builder/command.rs:3746 -->

<!-- Type: fn -->


Set binary name. Uses `&mut self` instead of `self`.


#### Fn: `get_name` (line 3751)

<!-- Source: repos/clap/clap_builder/src/builder/command.rs:3751 -->

<!-- Type: fn -->


Get the name of the cmd.


#### Fn: `get_name_and_visible_aliases` (line 3763)

<!-- Source: repos/clap/clap_builder/src/builder/command.rs:3763 -->

<!-- Type: fn -->


Get all known names of the cmd (i.e. primary name and visible aliases).


#### Fn: `get_version` (line 3770)

<!-- Source: repos/clap/clap_builder/src/builder/command.rs:3770 -->

<!-- Type: fn -->


Get the version of the cmd.


#### Fn: `get_long_version` (line 3776)

<!-- Source: repos/clap/clap_builder/src/builder/command.rs:3776 -->

<!-- Type: fn -->


Get the long version of the cmd.


#### Fn: `get_display_order` (line 3782)

<!-- Source: repos/clap/clap_builder/src/builder/command.rs:3782 -->

<!-- Type: fn -->


Get the placement within help


#### Fn: `get_author` (line 3788)

<!-- Source: repos/clap/clap_builder/src/builder/command.rs:3788 -->

<!-- Type: fn -->


Get the authors of the cmd.


#### Fn: `get_short_flag` (line 3794)

<!-- Source: repos/clap/clap_builder/src/builder/command.rs:3794 -->

<!-- Type: fn -->


Get the short flag of the subcommand.


#### Fn: `get_long_flag` (line 3800)

<!-- Source: repos/clap/clap_builder/src/builder/command.rs:3800 -->

<!-- Type: fn -->


Get the long flag of the subcommand.


#### Fn: `get_about` (line 3806)

<!-- Source: repos/clap/clap_builder/src/builder/command.rs:3806 -->

<!-- Type: fn -->


Get the help message specified via [`Command::about`].

[`Command::about`]: Command::about()


#### Fn: `get_long_about` (line 3814)

<!-- Source: repos/clap/clap_builder/src/builder/command.rs:3814 -->

<!-- Type: fn -->


Get the help message specified via [`Command::long_about`].

[`Command::long_about`]: Command::long_about()


#### Fn: `is_flatten_help_set` (line 3822)

<!-- Source: repos/clap/clap_builder/src/builder/command.rs:3822 -->

<!-- Type: fn -->


Get the custom section heading specified via [`Command::flatten_help`].


#### Fn: `get_next_help_heading` (line 3828)

<!-- Source: repos/clap/clap_builder/src/builder/command.rs:3828 -->

<!-- Type: fn -->


Get the custom section heading specified via [`Command::next_help_heading`].


#### Fn: `get_visible_aliases` (line 3834)

<!-- Source: repos/clap/clap_builder/src/builder/command.rs:3834 -->

<!-- Type: fn -->


Iterate through the *visible* aliases for this subcommand.


#### Fn: `get_visible_short_flag_aliases` (line 3843)

<!-- Source: repos/clap/clap_builder/src/builder/command.rs:3843 -->

<!-- Type: fn -->


Iterate through the *visible* short aliases for this subcommand.


#### Fn: `get_visible_long_flag_aliases` (line 3852)

<!-- Source: repos/clap/clap_builder/src/builder/command.rs:3852 -->

<!-- Type: fn -->


Iterate through the *visible* long aliases for this subcommand.


#### Fn: `get_all_aliases` (line 3861)

<!-- Source: repos/clap/clap_builder/src/builder/command.rs:3861 -->

<!-- Type: fn -->


Iterate through the set of *all* the aliases for this subcommand, both visible and hidden.


#### Fn: `get_all_short_flag_aliases` (line 3867)

<!-- Source: repos/clap/clap_builder/src/builder/command.rs:3867 -->

<!-- Type: fn -->


Iterate through the set of *all* the short aliases for this subcommand, both visible and hidden.


#### Fn: `get_all_long_flag_aliases` (line 3873)

<!-- Source: repos/clap/clap_builder/src/builder/command.rs:3873 -->

<!-- Type: fn -->


Iterate through the set of *all* the long aliases for this subcommand, both visible and hidden.


#### Fn: `get_aliases` (line 3879)

<!-- Source: repos/clap/clap_builder/src/builder/command.rs:3879 -->

<!-- Type: fn -->


Iterate through the *hidden* aliases for this subcommand.


#### Fn: `get_color` (line 3893)

<!-- Source: repos/clap/clap_builder/src/builder/command.rs:3893 -->

<!-- Type: fn -->


Should we color the output?


#### Fn: `get_styles` (line 3913)

<!-- Source: repos/clap/clap_builder/src/builder/command.rs:3913 -->

<!-- Type: fn -->


Return the current `Styles` for the `Command`


#### Fn: `get_subcommands` (line 3919)

<!-- Source: repos/clap/clap_builder/src/builder/command.rs:3919 -->

<!-- Type: fn -->


Iterate through the set of subcommands, getting a reference to each.


#### Fn: `get_subcommands_mut` (line 3925)

<!-- Source: repos/clap/clap_builder/src/builder/command.rs:3925 -->

<!-- Type: fn -->


Iterate through the set of subcommands, getting a mutable reference to each.


#### Fn: `has_subcommands` (line 3931)

<!-- Source: repos/clap/clap_builder/src/builder/command.rs:3931 -->

<!-- Type: fn -->


Returns `true` if this `Command` has subcommands.


#### Fn: `get_subcommand_help_heading` (line 3937)

<!-- Source: repos/clap/clap_builder/src/builder/command.rs:3937 -->

<!-- Type: fn -->


Returns the help heading for listing subcommands.


#### Fn: `get_subcommand_value_name` (line 3943)

<!-- Source: repos/clap/clap_builder/src/builder/command.rs:3943 -->

<!-- Type: fn -->


Returns the subcommand value name.


#### Fn: `get_before_help` (line 3949)

<!-- Source: repos/clap/clap_builder/src/builder/command.rs:3949 -->

<!-- Type: fn -->


Returns the help heading for listing subcommands.


#### Fn: `get_before_long_help` (line 3955)

<!-- Source: repos/clap/clap_builder/src/builder/command.rs:3955 -->

<!-- Type: fn -->


Returns the help heading for listing subcommands.


#### Fn: `get_after_help` (line 3961)

<!-- Source: repos/clap/clap_builder/src/builder/command.rs:3961 -->

<!-- Type: fn -->


Returns the help heading for listing subcommands.


#### Fn: `get_after_long_help` (line 3967)

<!-- Source: repos/clap/clap_builder/src/builder/command.rs:3967 -->

<!-- Type: fn -->


Returns the help heading for listing subcommands.


#### Fn: `find_subcommand` (line 3973)

<!-- Source: repos/clap/clap_builder/src/builder/command.rs:3973 -->

<!-- Type: fn -->


Find subcommand such that its name or one of aliases equals `name`.

This does not recurse through subcommands of subcommands.


#### Fn: `find_subcommand_mut` (line 3982)

<!-- Source: repos/clap/clap_builder/src/builder/command.rs:3982 -->

<!-- Type: fn -->


Find subcommand such that its name or one of aliases equals `name`, returning
a mutable reference to the subcommand.

This does not recurse through subcommands of subcommands.


#### Fn: `get_groups` (line 3995)

<!-- Source: repos/clap/clap_builder/src/builder/command.rs:3995 -->

<!-- Type: fn -->


Iterate through the set of groups.


#### Fn: `get_arguments` (line 4001)

<!-- Source: repos/clap/clap_builder/src/builder/command.rs:4001 -->

<!-- Type: fn -->


Iterate through the set of arguments.


#### Fn: `get_positionals` (line 4007)

<!-- Source: repos/clap/clap_builder/src/builder/command.rs:4007 -->

<!-- Type: fn -->


Iterate through the *positionals* arguments.


#### Fn: `get_opts` (line 4013)

<!-- Source: repos/clap/clap_builder/src/builder/command.rs:4013 -->

<!-- Type: fn -->


Iterate through the *options*.


#### Fn: `get_arg_conflicts_with` (line 4019)

<!-- Source: repos/clap/clap_builder/src/builder/command.rs:4019 -->

<!-- Type: fn -->


Get a list of all arguments the given argument conflicts with.

If the provided argument is declared as global, the conflicts will be determined
based on the propagation rules of global arguments.

### Panics

If the given arg contains a conflict with an argument that is unknown to
this `Command`.


#### Fn: `get_global_arg_conflicts_with` (line 4051)

<!-- Source: repos/clap/clap_builder/src/builder/command.rs:4051 -->

<!-- Type: fn -->


Get a unique list of all arguments of all commands and continuous subcommands the given argument conflicts with.

This behavior follows the propagation rules of global arguments.
It is useful for finding conflicts for arguments declared as global.

### Panics

If the given arg contains a conflict with an argument that is unknown to
this `Command`.


#### Fn: `get_subcommands_containing` (line 4081)

<!-- Source: repos/clap/clap_builder/src/builder/command.rs:4081 -->

<!-- Type: fn -->


Get a list of subcommands which contain the provided Argument

This command will only include subcommands in its list for which the subcommands
parent also contains the Argument.

This search follows the propagation rules of global arguments.
It is useful to finding subcommands, that have inherited a global argument.

<div class="warning">

**NOTE:** In this case only `Sucommand_1` will be included
```text
Subcommand_1 (contains Arg)
Subcommand_1.1 (doesn't contain Arg)
Subcommand_1.1.1 (contains Arg)
```

</div>


#### Fn: `is_no_binary_name_set` (line 4114)

<!-- Source: repos/clap/clap_builder/src/builder/command.rs:4114 -->

<!-- Type: fn -->


Report whether [`Command::no_binary_name`] is set


#### Fn: `is_ignore_errors_set` (line 4119)

<!-- Source: repos/clap/clap_builder/src/builder/command.rs:4119 -->

<!-- Type: fn -->


Report whether [`Command::ignore_errors`] is set


#### Fn: `is_dont_delimit_trailing_values_set` (line 4124)

<!-- Source: repos/clap/clap_builder/src/builder/command.rs:4124 -->

<!-- Type: fn -->


Report whether [`Command::dont_delimit_trailing_values`] is set


#### Fn: `is_disable_version_flag_set` (line 4129)

<!-- Source: repos/clap/clap_builder/src/builder/command.rs:4129 -->

<!-- Type: fn -->


Report whether [`Command::disable_version_flag`] is set


#### Fn: `is_propagate_version_set` (line 4135)

<!-- Source: repos/clap/clap_builder/src/builder/command.rs:4135 -->

<!-- Type: fn -->


Report whether [`Command::propagate_version`] is set


#### Fn: `is_next_line_help_set` (line 4140)

<!-- Source: repos/clap/clap_builder/src/builder/command.rs:4140 -->

<!-- Type: fn -->


Report whether [`Command::next_line_help`] is set


#### Fn: `is_disable_help_flag_set` (line 4145)

<!-- Source: repos/clap/clap_builder/src/builder/command.rs:4145 -->

<!-- Type: fn -->


Report whether [`Command::disable_help_flag`] is set


#### Fn: `is_disable_help_subcommand_set` (line 4150)

<!-- Source: repos/clap/clap_builder/src/builder/command.rs:4150 -->

<!-- Type: fn -->


Report whether [`Command::disable_help_subcommand`] is set


#### Fn: `is_disable_colored_help_set` (line 4155)

<!-- Source: repos/clap/clap_builder/src/builder/command.rs:4155 -->

<!-- Type: fn -->


Report whether [`Command::disable_colored_help`] is set


#### Fn: `is_help_expected_set` (line 4160)

<!-- Source: repos/clap/clap_builder/src/builder/command.rs:4160 -->

<!-- Type: fn -->


Report whether [`Command::help_expected`] is set


#### Fn: `is_infer_long_args_set` (line 4175)

<!-- Source: repos/clap/clap_builder/src/builder/command.rs:4175 -->

<!-- Type: fn -->


Report whether [`Command::infer_long_args`] is set


#### Fn: `is_infer_subcommands_set` (line 4180)

<!-- Source: repos/clap/clap_builder/src/builder/command.rs:4180 -->

<!-- Type: fn -->


Report whether [`Command::infer_subcommands`] is set


#### Fn: `is_arg_required_else_help_set` (line 4185)

<!-- Source: repos/clap/clap_builder/src/builder/command.rs:4185 -->

<!-- Type: fn -->


Report whether [`Command::arg_required_else_help`] is set


#### Fn: `is_allow_missing_positional_set` (line 4223)

<!-- Source: repos/clap/clap_builder/src/builder/command.rs:4223 -->

<!-- Type: fn -->


Report whether [`Command::allow_missing_positional`] is set


#### Fn: `is_hide_set` (line 4228)

<!-- Source: repos/clap/clap_builder/src/builder/command.rs:4228 -->

<!-- Type: fn -->


Report whether [`Command::hide`] is set


#### Fn: `is_subcommand_required_set` (line 4233)

<!-- Source: repos/clap/clap_builder/src/builder/command.rs:4233 -->

<!-- Type: fn -->


Report whether [`Command::subcommand_required`] is set


#### Fn: `is_allow_external_subcommands_set` (line 4238)

<!-- Source: repos/clap/clap_builder/src/builder/command.rs:4238 -->

<!-- Type: fn -->


Report whether [`Command::allow_external_subcommands`] is set


#### Fn: `get_external_subcommand_value_parser` (line 4243)

<!-- Source: repos/clap/clap_builder/src/builder/command.rs:4243 -->

<!-- Type: fn -->


Configured parser for values passed to an external subcommand

# Example

```rust
# use clap_builder as clap;
let cmd = clap::Command::new("raw")
.external_subcommand_value_parser(clap::value_parser!(String));
let value_parser = cmd.get_external_subcommand_value_parser();
println!("{value_parser:?}");
```


**Code Examples:**


```rust
# use clap_builder as clap;
let cmd = clap::Command::new("raw")
.external_subcommand_value_parser(clap::value_parser!(String));
let value_parser = cmd.get_external_subcommand_value_parser();
println!("{value_parser:?}");
```


#### Fn: `is_args_conflicts_with_subcommands_set` (line 4263)

<!-- Source: repos/clap/clap_builder/src/builder/command.rs:4263 -->

<!-- Type: fn -->


Report whether [`Command::args_conflicts_with_subcommands`] is set


#### Fn: `is_subcommand_precedence_over_arg_set` (line 4273)

<!-- Source: repos/clap/clap_builder/src/builder/command.rs:4273 -->

<!-- Type: fn -->


Report whether [`Command::subcommand_precedence_over_arg`] is set


#### Fn: `is_subcommand_negates_reqs_set` (line 4278)

<!-- Source: repos/clap/clap_builder/src/builder/command.rs:4278 -->

<!-- Type: fn -->


Report whether [`Command::subcommand_negates_reqs`] is set


#### Fn: `is_multicall_set` (line 4283)

<!-- Source: repos/clap/clap_builder/src/builder/command.rs:4283 -->

<!-- Type: fn -->


Report whether [`Command::multicall`] is set


#### Fn: `get` (line 4288)

<!-- Source: repos/clap/clap_builder/src/builder/command.rs:4288 -->

<!-- Type: fn -->


Access an [`CommandExt`]


#### Fn: `remove` (line 4294)

<!-- Source: repos/clap/clap_builder/src/builder/command.rs:4294 -->

<!-- Type: fn -->


Remove an [`CommandExt`]


#### Fn: `build` (line 4375)

<!-- Source: repos/clap/clap_builder/src/builder/command.rs:4375 -->

<!-- Type: fn -->


Prepare for introspecting on all included [`Command`]s

Call this on the top-level [`Command`] when done building and before reading state for
cases like completions, custom help output, etc.


#### Fn: `two_args_of` (line 4710)

<!-- Source: repos/clap/clap_builder/src/builder/command.rs:4710 -->

<!-- Type: fn -->


Returns the first two arguments that match the condition.

If fewer than two arguments that match the condition, `None` is returned.


#### Fn: `two_groups_of` (line 4721)

<!-- Source: repos/clap/clap_builder/src/builder/command.rs:4721 -->

<!-- Type: fn -->


Returns the first two groups that match the condition.

If fewer than two groups that match the condition, `None` is returned.


#### Fn: `_propagate_global_args` (line 4732)

<!-- Source: repos/clap/clap_builder/src/builder/command.rs:4732 -->

<!-- Type: fn -->


Propagate global args


#### Fn: `_propagate` (line 4767)

<!-- Source: repos/clap/clap_builder/src/builder/command.rs:4767 -->

<!-- Type: fn -->


Propagate settings


#### Trait: `Captures` (line 4931)

<!-- Source: repos/clap/clap_builder/src/builder/command.rs:4931 -->

<!-- Type: trait -->


A workaround:
<https://github.com/rust-lang/rust/issues/34511#issuecomment-373423999>


#### Fn: `get_non_positionals` (line 4938)

<!-- Source: repos/clap/clap_builder/src/builder/command.rs:4938 -->

<!-- Type: fn -->


Iterate through the *flags* & *options* arguments.


#### Fn: `aliases_to` (line 4975)

<!-- Source: repos/clap/clap_builder/src/builder/command.rs:4975 -->

<!-- Type: fn -->


Check if this subcommand can be referred to as `name`. In other words,
check if `name` is the name of this subcommand or is one of its aliases.


#### Fn: `short_flag_aliases_to` (line 4983)

<!-- Source: repos/clap/clap_builder/src/builder/command.rs:4983 -->

<!-- Type: fn -->


Check if this subcommand can be referred to as `name`. In other words,
check if `name` is the name of this short flag subcommand or is one of its short flag aliases.


#### Fn: `long_flag_aliases_to` (line 4991)

<!-- Source: repos/clap/clap_builder/src/builder/command.rs:4991 -->

<!-- Type: fn -->


Check if this subcommand can be referred to as `name`. In other words,
check if `name` is the name of this long flag subcommand or is one of its long flag aliases.


#### Fn: `id_exists` (line 5003)

<!-- Source: repos/clap/clap_builder/src/builder/command.rs:5003 -->

<!-- Type: fn -->


Checks if there is an argument or group with the given id.


#### Fn: `groups_for_arg` (line 5009)

<!-- Source: repos/clap/clap_builder/src/builder/command.rs:5009 -->

<!-- Type: fn -->


Iterate through the groups this arg is member of.


#### Fn: `all_subcommand_names` (line 5023)

<!-- Source: repos/clap/clap_builder/src/builder/command.rs:5023 -->

<!-- Type: fn -->


Iterate through all the names of all subcommands (not recursively), including aliases.
Used for suggestions.


#### Fn: `find_short_subcmd` (line 5110)

<!-- Source: repos/clap/clap_builder/src/builder/command.rs:5110 -->

<!-- Type: fn -->


Find a flag subcommand name by short flag or an alias


#### Fn: `find_long_subcmd` (line 5117)

<!-- Source: repos/clap/clap_builder/src/builder/command.rs:5117 -->

<!-- Type: fn -->


Find a flag subcommand name by long flag or an alias


#### Trait: `CommandExt` (line 5251)

<!-- Source: repos/clap/clap_builder/src/builder/command.rs:5251 -->

<!-- Type: trait -->


User-provided data that can be attached to an [`Arg`]


#### Fn: `two_elements_of` (line 5270)

<!-- Source: repos/clap/clap_builder/src/builder/command.rs:5270 -->

<!-- Type: fn -->


Returns the first two elements of an iterator as an `Option<(T, T)>`.

If the iterator has fewer than two elements, it returns `None`.


### From `repos/clap/clap_builder/src/derive.rs`


#### Trait: `CommandFactory` (line 113)

<!-- Source: repos/clap/clap_builder/src/derive.rs:113 -->

<!-- Type: trait -->


Create a [`Command`] relevant for a user-defined container.

Derived as part of [`Parser`].


#### Fn: `command` (line 117)

<!-- Source: repos/clap/clap_builder/src/derive.rs:117 -->

<!-- Type: fn -->


Build a [`Command`] that can instantiate `Self`.

See [`FromArgMatches::from_arg_matches_mut`] for instantiating `Self`.


#### Fn: `command_for_update` (line 121)

<!-- Source: repos/clap/clap_builder/src/derive.rs:121 -->

<!-- Type: fn -->


Build a [`Command`] that can update `self`.

See [`FromArgMatches::update_from_arg_matches_mut`] for updating `self`.


#### Trait: `Subcommand` (line 248)

<!-- Source: repos/clap/clap_builder/src/derive.rs:248 -->

<!-- Type: trait -->


Parse a sub-command into a user-defined enum.

Implementing this trait lets a parent container delegate subcommand behavior to `Self`.
with:
- `#[command(subcommand)] field: SubCmd`: Attribute can be used with either struct fields or enum
variants that impl `Subcommand`.
- `#[command(flatten)] Variant(SubCmd)`: Attribute can only be used with enum variants that impl
`Subcommand`.

<div class="warning">

**NOTE:** Deriving requires the `derive` feature flag

</div>


#### Fn: `augment_subcommands` (line 263)

<!-- Source: repos/clap/clap_builder/src/derive.rs:263 -->

<!-- Type: fn -->


Append to [`Command`] so it can instantiate `Self` via
[`FromArgMatches::from_arg_matches_mut`]

This is used to implement `#[command(flatten)]`

See also [`CommandFactory::command`].


#### Fn: `augment_subcommands_for_update` (line 270)

<!-- Source: repos/clap/clap_builder/src/derive.rs:270 -->

<!-- Type: fn -->


Append to [`Command`] so it can instantiate `self` via
[`FromArgMatches::update_from_arg_matches_mut`]

This is used to implement `#[command(flatten)]`

See also [`CommandFactory::command_for_update`].


#### Fn: `has_subcommand` (line 277)

<!-- Source: repos/clap/clap_builder/src/derive.rs:277 -->

<!-- Type: fn -->


Test whether `Self` can parse a specific subcommand


### From `repos/clap/clap_builder/src/output/help_template.rs`


#### Fn: `write_flat_subcommands` (line 878)

<!-- Source: repos/clap/clap_builder/src/output/help_template.rs:878 -->

<!-- Type: fn -->


Writes help for subcommands of a Parser Object to the wrapped stream.


#### Fn: `write_subcommands` (line 939)

<!-- Source: repos/clap/clap_builder/src/output/help_template.rs:939 -->

<!-- Type: fn -->


Writes help for subcommands of a Parser Object to the wrapped stream.


#### Fn: `will_subcommands_wrap` (line 977)

<!-- Source: repos/clap/clap_builder/src/output/help_template.rs:977 -->

<!-- Type: fn -->


Will use next line help on writing subcommands.


### From `repos/clap/clap_builder/src/parser/matches/arg_matches.rs`


#### Fn: `subcommand` (line 867)

<!-- Source: repos/clap/clap_builder/src/parser/matches/arg_matches.rs:867 -->

<!-- Type: fn -->


The name and `ArgMatches` of the current [subcommand].

Subcommand values are put in a child [`ArgMatches`]

Returns `None` if the subcommand wasn't present at runtime,

# Examples

```no_run
# use clap_builder as clap;
# use clap::{Command, Arg, };
let app_m = Command::new("git")
.subcommand(Command::new("clone"))
.subcommand(Command::new("push"))
.subcommand(Command::new("commit"))
.get_matches();

match app_m.subcommand() {
Some(("clone",  sub_m)) => {}, // clone was used
Some(("push",   sub_m)) => {}, // push was used
Some(("commit", sub_m)) => {}, // commit was used
_                       => {}, // Either no subcommand or one not tested for...
}
```

Another useful scenario is when you want to support third party, or external, subcommands.
In these cases you can't know the subcommand name ahead of time, so use a variable instead
with pattern matching!

```rust
# use clap_builder as clap;
# use std::ffi::OsString;
# use std::ffi::OsStr;
# use clap::Command;
// Assume there is an external subcommand named "subcmd"
let app_m = Command::new("myprog")
.allow_external_subcommands(true)
.get_matches_from(vec![
"myprog", "subcmd", "--option", "value", "-fff", "--flag"
]);

// All trailing arguments will be stored under the subcommand's sub-matches using an empty
// string argument name
match app_m.subcommand() {
Some((external, sub_m)) => {
let ext_args: Vec<&OsStr> = sub_m.get_many::<OsString>("")
.unwrap().map(|s| s.as_os_str()).collect();
assert_eq!(external, "subcmd");
assert_eq!(ext_args, ["--option", "value", "-fff", "--flag"]);
},
_ => {},
}
```
[subcommand]: crate::Command::subcommand


**Code Examples:**


```rust
# use clap_builder as clap;
# use clap::{Command, Arg, };
let app_m = Command::new("git")
.subcommand(Command::new("clone"))
.subcommand(Command::new("push"))
.subcommand(Command::new("commit"))
.get_matches();

match app_m.subcommand() {
Some(("clone",  sub_m)) => {}, // clone was used
Some(("push",   sub_m)) => {}, // push was used
Some(("commit", sub_m)) => {}, // commit was used
_                       => {}, // Either no subcommand or one not tested for...
}
```


```rust
# use clap_builder as clap;
# use std::ffi::OsString;
# use std::ffi::OsStr;
# use clap::Command;
// Assume there is an external subcommand named "subcmd"
let app_m = Command::new("myprog")
.allow_external_subcommands(true)
.get_matches_from(vec![
"myprog", "subcmd", "--option", "value", "-fff", "--flag"
]);

// All trailing arguments will be stored under the subcommand's sub-matches using an empty
// string argument name
match app_m.subcommand() {
Some((external, sub_m)) => {
let ext_args: Vec<&OsStr> = sub_m.get_many::<OsString>("")
.unwrap().map(|s| s.as_os_str()).collect();
assert_eq!(external, "subcmd");
assert_eq!(ext_args, ["--option", "value", "-fff", "--flag"]);
},
_ => {},
}
```


#### Fn: `remove_subcommand` (line 926)

<!-- Source: repos/clap/clap_builder/src/parser/matches/arg_matches.rs:926 -->

<!-- Type: fn -->


Return the name and `ArgMatches` of the current [subcommand].

Subcommand values are put in a child [`ArgMatches`]

Returns `None` if the subcommand wasn't present at runtime,

# Examples

```no_run
# use clap_builder as clap;
# use clap::{Command, Arg, };
let mut app_m = Command::new("git")
.subcommand(Command::new("clone"))
.subcommand(Command::new("push"))
.subcommand(Command::new("commit"))
.subcommand_required(true)
.get_matches();

let (name, sub_m) = app_m.remove_subcommand().expect("required");
match (name.as_str(), sub_m) {
("clone",  sub_m) => {}, // clone was used
("push",   sub_m) => {}, // push was used
("commit", sub_m) => {}, // commit was used
(name, _)         => unimplemented!("{name}"),
}
```

Another useful scenario is when you want to support third party, or external, subcommands.
In these cases you can't know the subcommand name ahead of time, so use a variable instead
with pattern matching!

```rust
# use clap_builder as clap;
# use std::ffi::OsString;
# use clap::Command;
// Assume there is an external subcommand named "subcmd"
let mut app_m = Command::new("myprog")
.allow_external_subcommands(true)
.get_matches_from(vec![
"myprog", "subcmd", "--option", "value", "-fff", "--flag"
]);

// All trailing arguments will be stored under the subcommand's sub-matches using an empty
// string argument name
match app_m.remove_subcommand() {
Some((external, mut sub_m)) => {
let ext_args: Vec<OsString> = sub_m.remove_many("")
.expect("`file`is required")
.collect();
assert_eq!(external, "subcmd");
assert_eq!(ext_args, ["--option", "value", "-fff", "--flag"]);
},
_ => {},
}
```
[subcommand]: crate::Command::subcommand


**Code Examples:**


```rust
# use clap_builder as clap;
# use clap::{Command, Arg, };
let mut app_m = Command::new("git")
.subcommand(Command::new("clone"))
.subcommand(Command::new("push"))
.subcommand(Command::new("commit"))
.subcommand_required(true)
.get_matches();

let (name, sub_m) = app_m.remove_subcommand().expect("required");
match (name.as_str(), sub_m) {
("clone",  sub_m) => {}, // clone was used
("push",   sub_m) => {}, // push was used
("commit", sub_m) => {}, // commit was used
(name, _)         => unimplemented!("{name}"),
}
```


```rust
# use clap_builder as clap;
# use std::ffi::OsString;
# use clap::Command;
// Assume there is an external subcommand named "subcmd"
let mut app_m = Command::new("myprog")
.allow_external_subcommands(true)
.get_matches_from(vec![
"myprog", "subcmd", "--option", "value", "-fff", "--flag"
]);

// All trailing arguments will be stored under the subcommand's sub-matches using an empty
// string argument name
match app_m.remove_subcommand() {
Some((external, mut sub_m)) => {
let ext_args: Vec<OsString> = sub_m.remove_many("")
.expect("`file`is required")
.collect();
assert_eq!(external, "subcmd");
assert_eq!(ext_args, ["--option", "value", "-fff", "--flag"]);
},
_ => {},
}
```


#### Fn: `subcommand_matches` (line 986)

<!-- Source: repos/clap/clap_builder/src/parser/matches/arg_matches.rs:986 -->

<!-- Type: fn -->


The `ArgMatches` for the current [subcommand].

Subcommand values are put in a child [`ArgMatches`]

Returns `None` if the subcommand wasn't present at runtime,

# Panics

If `id` is not a valid subcommand (debug builds).

# Examples

```rust
# use clap_builder as clap;
# use clap::{Command, Arg, ArgAction};
let app_m = Command::new("myprog")
.arg(Arg::new("debug")
.short('d')
.action(ArgAction::SetTrue)
)
.subcommand(Command::new("test")
.arg(Arg::new("opt")
.long("option")
.action(ArgAction::Set)))
.get_matches_from(vec![
"myprog", "-d", "test", "--option", "val"
]);

// Both parent commands, and child subcommands can have arguments present at the same times
assert!(app_m.get_flag("debug"));

// Get the subcommand's ArgMatches instance
if let Some(sub_m) = app_m.subcommand_matches("test") {
// Use the struct like normal
assert_eq!(sub_m.get_one::<String>("opt").map(|s| s.as_str()), Some("val"));
}
```

[subcommand]: crate::Command::subcommand
[`Command`]: crate::Command


**Code Examples:**


```rust
# use clap_builder as clap;
# use clap::{Command, Arg, ArgAction};
let app_m = Command::new("myprog")
.arg(Arg::new("debug")
.short('d')
.action(ArgAction::SetTrue)
)
.subcommand(Command::new("test")
.arg(Arg::new("opt")
.long("option")
.action(ArgAction::Set)))
.get_matches_from(vec![
"myprog", "-d", "test", "--option", "val"
]);

// Both parent commands, and child subcommands can have arguments present at the same times
assert!(app_m.get_flag("debug"));

// Get the subcommand's ArgMatches instance
if let Some(sub_m) = app_m.subcommand_matches("test") {
// Use the struct like normal
assert_eq!(sub_m.get_one::<String>("opt").map(|s| s.as_str()), Some("val"));
}
```


#### Fn: `subcommand_name` (line 1030)

<!-- Source: repos/clap/clap_builder/src/parser/matches/arg_matches.rs:1030 -->

<!-- Type: fn -->


The name of the current [subcommand].

Returns `None` if the subcommand wasn't present at runtime,

# Examples

```no_run
# use clap_builder as clap;
# use clap::{Command, Arg, };
let app_m = Command::new("git")
.subcommand(Command::new("clone"))
.subcommand(Command::new("push"))
.subcommand(Command::new("commit"))
.get_matches();

match app_m.subcommand_name() {
Some("clone")  => {}, // clone was used
Some("push")   => {}, // push was used
Some("commit") => {}, // commit was used
_              => {}, // Either no subcommand or one not tested for...
}
```
[subcommand]: crate::Command::subcommand
[`Command`]: crate::Command


**Code Examples:**


```rust
# use clap_builder as clap;
# use clap::{Command, Arg, };
let app_m = Command::new("git")
.subcommand(Command::new("clone"))
.subcommand(Command::new("push"))
.subcommand(Command::new("commit"))
.get_matches();

match app_m.subcommand_name() {
Some("clone")  => {}, // clone was used
Some("push")   => {}, // push was used
Some("commit") => {}, // commit was used
_              => {}, // Either no subcommand or one not tested for...
}
```


#### Fn: `is_valid_subcommand` (line 1059)

<!-- Source: repos/clap/clap_builder/src/parser/matches/arg_matches.rs:1059 -->

<!-- Type: fn -->


Check if a subcommand can be queried

By default, `ArgMatches` functions assert on undefined `Id`s to help catch programmer
mistakes.  In some context, this doesn't work, so users can use this function to check
before they do a query on `ArgMatches`.


### From `repos/clap/clap_complete/src/aot/generator/utils.rs`


#### Fn: `all_subcommands` (line 5)

<!-- Source: repos/clap/clap_complete/src/aot/generator/utils.rs:5 -->

<!-- Type: fn -->


Gets all subcommands including child subcommands in the form of `("name", "bin_name")`.

Subcommand `rustup toolchain install` would be converted to
`("install", "rustup toolchain install")`.


#### Fn: `find_subcommand_with_path` (line 19)

<!-- Source: repos/clap/clap_complete/src/aot/generator/utils.rs:19 -->

<!-- Type: fn -->


Finds the subcommand [`clap::Command`] from the given [`clap::Command`] with the given path.

<div class="warning">

**NOTE:** `path` should not contain the root `bin_name`.

</div>


#### Fn: `subcommands` (line 36)

<!-- Source: repos/clap/clap_complete/src/aot/generator/utils.rs:36 -->

<!-- Type: fn -->


Gets subcommands of [`clap::Command`] in the form of `("name", "bin_name")`.

Subcommand `rustup toolchain install` would be converted to
`("install", "rustup toolchain install")`.


### From `repos/clap/clap_complete/src/aot/shells/fish.rs`


#### Fn: `gen_subcommand_helpers` (line 214)

<!-- Source: repos/clap/clap_complete/src/aot/shells/fish.rs:214 -->

<!-- Type: fn -->


Print fish's helpers for easy handling subcommands.


### From `repos/clap/clap_complete/src/engine/complete.rs`


#### Fn: `subcommands` (line 555)

<!-- Source: repos/clap/clap_complete/src/engine/complete.rs:555 -->

<!-- Type: fn -->


Gets subcommands of [`clap::Command`] in the form of `("name", "bin_name")`.

Subcommand `rustup toolchain install` would be converted to
`("install", "rustup toolchain install")`.


### From `repos/clap/clap_complete/src/engine/custom.rs`


#### Struct: `SubcommandCandidates` (line 135)

<!-- Source: repos/clap/clap_complete/src/engine/custom.rs:135 -->

<!-- Type: struct -->


Extend [`Command`][clap::Command] with a [`ValueCandidates`]

# Example
```rust
use clap::Parser;
use clap_complete::engine::{SubcommandCandidates, CompletionCandidate};
#[derive(Debug, Parser)]
#[clap(name = "cli", add = SubcommandCandidates::new(|| { vec![
CompletionCandidate::new("foo"),
CompletionCandidate::new("bar"),
CompletionCandidate::new("baz")] }))]
struct Cli {
#[arg(long)]
input: Option<String>,
}
```


**Code Examples:**


```rust
use clap::Parser;
use clap_complete::engine::{SubcommandCandidates, CompletionCandidate};
#[derive(Debug, Parser)]
#[clap(name = "cli", add = SubcommandCandidates::new(|| { vec![
CompletionCandidate::new("foo"),
CompletionCandidate::new("bar"),
CompletionCandidate::new("baz")] }))]
struct Cli {
#[arg(long)]
input: Option<String>,
}
```


---


## 2. Arguments (Arg) {#arguments}


### From `repos/clap-cargo/src/features.rs`


#### Module: `features` (line 1)

<!-- Source: repos/clap-cargo/src/features.rs:1 -->

<!-- Type: module -->


Cargo Feature Flags.


#### Struct: `Features` (line 3)

<!-- Source: repos/clap-cargo/src/features.rs:3 -->

<!-- Type: struct -->


Cargo Feature Flags.


#### Fn: `forward_metadata` (line 22)

<!-- Source: repos/clap-cargo/src/features.rs:22 -->

<!-- Type: fn -->


Forward these flags to the `cargo_metadata` crate.

Note: Requires the features `cargo_metadata`.


### From `repos/clap-cargo/src/lib.rs`


#### Module: `lib` (line 1)

<!-- Source: repos/clap-cargo/src/lib.rs:1 -->

<!-- Type: module -->


**clap-cargo**: Re-usable CLI flags for `cargo` plugins

## Examples

```rust,no_run
# #[cfg(feature = "clap")] {
# #[cfg(feature = "cargo_metadata")] {
use clap::Parser;

// ...
#[derive(Debug, Parser)]
#[command(styles = clap_cargo::style::CLAP_STYLING)]
struct Cli {
#[command(flatten)]
manifest: clap_cargo::Manifest,
#[command(flatten)]
workspace: clap_cargo::Workspace,
#[command(flatten)]
features: clap_cargo::Features,
}

let cli = // ...
# Cli::parse_from(["app"]);
let mut metadata = cli.manifest.metadata();
cli.features.forward_metadata(&mut metadata);
let metadata = metadata.exec().unwrap();
let (selected, excluded) = cli.workspace.partition_packages(&metadata);
# }
# }
```

## Relevant crates

Other crates that might be useful for cargo plugins:
* [escargot][escargot] for wrapping `cargo-build`, `carg-run`, `cargo-test`, etc.
* [cargo_metadata][cargo_metadata] for getting crate information.
* [clap-verbosity][clap-verbosity] for adding logging to your CLI.

[escargot]: https://crates.io/crates/escargot
[cargo_metadata]: https://crates.io/crates/cargo_metadata
[clap-verbosity]: https://crates.io/crates/clap-verbosity-flag


### From `repos/clap-cargo/src/manifest.rs`


#### Module: `manifest` (line 1)

<!-- Source: repos/clap-cargo/src/manifest.rs:1 -->

<!-- Type: module -->


Cargo flag for selecting the relevant crate.


#### Struct: `Manifest` (line 5)

<!-- Source: repos/clap-cargo/src/manifest.rs:5 -->

<!-- Type: struct -->


Cargo flag for selecting the relevant crate.


#### Fn: `metadata` (line 18)

<!-- Source: repos/clap-cargo/src/manifest.rs:18 -->

<!-- Type: fn -->


Create a `cargo_metadata::MetadataCommand`

Note: Requires the features `cargo_metadata`.


### From `repos/clap-cargo/src/style.rs`


#### Const: `CLAP_STYLING` (line 40)

<!-- Source: repos/clap-cargo/src/style.rs:40 -->

<!-- Type: const -->


For use with
[`clap::Command::styles`](https://docs.rs/clap/latest/clap/struct.Command.html#method.styles)


#### Const: `DEFAULT_ERROR_STYLE` (line 65)

<!-- Source: repos/clap-cargo/src/style.rs:65 -->

<!-- Type: const -->


[`Renderer::error`] applied by [`Renderer::styled`]


#### Const: `DEFAULT_WARNING_STYLE` (line 68)

<!-- Source: repos/clap-cargo/src/style.rs:68 -->

<!-- Type: const -->


[`Renderer::warning`] applied by [`Renderer::styled`]


#### Const: `DEFAULT_INFO_STYLE` (line 75)

<!-- Source: repos/clap-cargo/src/style.rs:75 -->

<!-- Type: const -->


[`Renderer::info`] applied by [`Renderer::styled`]


#### Const: `DEFAULT_NOTE_STYLE` (line 77)

<!-- Source: repos/clap-cargo/src/style.rs:77 -->

<!-- Type: const -->


[`Renderer::note`] applied by [`Renderer::styled`]


#### Const: `DEFAULT_HELP_STYLE` (line 80)

<!-- Source: repos/clap-cargo/src/style.rs:80 -->

<!-- Type: const -->


[`Renderer::help`] applied by [`Renderer::styled`]


#### Const: `DEFAULT_LINE_NUM_STYLE` (line 83)

<!-- Source: repos/clap-cargo/src/style.rs:83 -->

<!-- Type: const -->


[`Renderer::line_num`] applied by [`Renderer::styled`]


#### Const: `DEFAULT_EMPHASIS_STYLE` (line 85)

<!-- Source: repos/clap-cargo/src/style.rs:85 -->

<!-- Type: const -->


[`Renderer::emphasis`] applied by [`Renderer::styled`]


#### Const: `DEFAULT_NONE_STYLE` (line 92)

<!-- Source: repos/clap-cargo/src/style.rs:92 -->

<!-- Type: const -->


[`Renderer::none`] applied by [`Renderer::styled`]


#### Const: `DEFAULT_CONTEXT_STYLE` (line 94)

<!-- Source: repos/clap-cargo/src/style.rs:94 -->

<!-- Type: const -->


[`Renderer::context`] applied by [`Renderer::styled`]


#### Const: `DEFAULT_ADDITION_STYLE` (line 96)

<!-- Source: repos/clap-cargo/src/style.rs:96 -->

<!-- Type: const -->


[`Renderer::addition`] applied by [`Renderer::styled`]


#### Const: `DEFAULT_REMOVAL_STYLE` (line 98)

<!-- Source: repos/clap-cargo/src/style.rs:98 -->

<!-- Type: const -->


[`Renderer::removal`] applied by [`Renderer::styled`]


### From `repos/clap-cargo/src/workspace.rs`


#### Module: `workspace` (line 1)

<!-- Source: repos/clap-cargo/src/workspace.rs:1 -->

<!-- Type: module -->


Cargo flags for selecting crates in a workspace.


#### Struct: `Workspace` (line 3)

<!-- Source: repos/clap-cargo/src/workspace.rs:3 -->

<!-- Type: struct -->


Cargo flags for selecting crates in a workspace.


#### Fn: `partition_packages` (line 25)

<!-- Source: repos/clap-cargo/src/workspace.rs:25 -->

<!-- Type: fn -->


Partition workspace members into those selected and those excluded.

Notes:
- Requires the features `cargo_metadata`.
- Requires not calling `MetadataCommand::no_deps`


### From `repos/clap/clap_builder/src/builder/action.rs`


#### Enum: `ArgAction` (line 6)

<!-- Source: repos/clap/clap_builder/src/builder/action.rs:6 -->

<!-- Type: enum -->


Behavior of arguments when they are encountered while parsing

# Examples

```rust
# #[cfg(feature = "help")] {
# use clap_builder as clap;
# use clap::Command;
# use clap::Arg;
let cmd = Command::new("mycmd")
.arg(
Arg::new("special-help")
.short('?')
.action(clap::ArgAction::Help)
);

// Existing help still exists
let err = cmd.clone().try_get_matches_from(["mycmd", "-h"]).unwrap_err();
assert_eq!(err.kind(), clap::error::ErrorKind::DisplayHelp);

// New help available
let err = cmd.try_get_matches_from(["mycmd", "-?"]).unwrap_err();
assert_eq!(err.kind(), clap::error::ErrorKind::DisplayHelp);
# }
```


**Code Examples:**


```rust
# #[cfg(feature = "help")] {
# use clap_builder as clap;
# use clap::Command;
# use clap::Arg;
let cmd = Command::new("mycmd")
.arg(
Arg::new("special-help")
.short('?')
.action(clap::ArgAction::Help)
);

// Existing help still exists
let err = cmd.clone().try_get_matches_from(["mycmd", "-h"]).unwrap_err();
assert_eq!(err.kind(), clap::error::ErrorKind::DisplayHelp);

// New help available
let err = cmd.try_get_matches_from(["mycmd", "-?"]).unwrap_err();
assert_eq!(err.kind(), clap::error::ErrorKind::DisplayHelp);
# }
```


### From `repos/clap/clap_builder/src/builder/arg.rs`


#### Struct: `Arg` (line 31)

<!-- Source: repos/clap/clap_builder/src/builder/arg.rs:31 -->

<!-- Type: struct -->


The abstract representation of a command line argument. Used to set all the options and
relationships that define a valid argument for the program.

There are two methods for constructing [`Arg`]s, using the builder pattern and setting options
manually, or using a usage string which is far less verbose but has fewer options. You can also
use a combination of the two methods to achieve the best of both worlds.

- [Basic API][crate::Arg#basic-api]
- [Value Handling][crate::Arg#value-handling]
- [Help][crate::Arg#help-1]
- [Advanced Argument Relations][crate::Arg#advanced-argument-relations]
- [Reflection][crate::Arg#reflection]

# Examples

```rust
# use clap_builder as clap;
# use clap::{Arg, arg, ArgAction};
// Using the traditional builder pattern and setting each option manually
let cfg = Arg::new("config")
.short('c')
.long("config")
.action(ArgAction::Set)
.value_name("FILE")
.help("Provides a config file to myprog");
// Using a usage string (setting a similar argument to the one above)
let input = arg!(-i --input <FILE> "Provides an input file to the program");
```


**Code Examples:**


```rust
# use clap_builder as clap;
# use clap::{Arg, arg, ArgAction};
// Using the traditional builder pattern and setting each option manually
let cfg = Arg::new("config")
.short('c')
.long("config")
.action(ArgAction::Set)
.value_name("FILE")
.help("Provides a config file to myprog");
// Using a usage string (setting a similar argument to the one above)
let input = arg!(-i --input <FILE> "Provides an input file to the program");
```


#### Impl: `Arg` (line 94)

<!-- Source: repos/clap/clap_builder/src/builder/arg.rs:94 -->

<!-- Type: impl -->


# Basic API


#### Fn: `new` (line 96)

<!-- Source: repos/clap/clap_builder/src/builder/arg.rs:96 -->

<!-- Type: fn -->


Create a new [`Arg`] with a unique name.

The name is used to check whether or not the argument was used at
runtime, get values, set relationships with other args, etc..

By default, an `Arg` is
- Positional, see [`Arg::short`] or [`Arg::long`] turn it into an option
- Accept a single value, see [`Arg::action`] to override this

<div class="warning">

**NOTE:** In the case of arguments that take values (i.e. [`Arg::action(ArgAction::Set)`])
and positional arguments (i.e. those without a preceding `-` or `--`) the name will also
be displayed when the user prints the usage/help information of the program.

</div>

# Examples

```rust
# use clap_builder as clap;
# use clap::{Command, Arg};
Arg::new("config")
# ;
```
[`Arg::action(ArgAction::Set)`]: Arg::action()


**Code Examples:**


```rust
# use clap_builder as clap;
# use clap::{Command, Arg};
Arg::new("config")
# ;
```


#### Fn: `id` (line 126)

<!-- Source: repos/clap/clap_builder/src/builder/arg.rs:126 -->

<!-- Type: fn -->


Set the identifier used for referencing this argument in the clap API.

See [`Arg::new`] for more details.


#### Fn: `short` (line 135)

<!-- Source: repos/clap/clap_builder/src/builder/arg.rs:135 -->

<!-- Type: fn -->


Sets the short version of the argument without the preceding `-`.

By default `V` and `h` are used by the auto-generated `version` and `help` arguments,
respectively. You will need to disable the auto-generated flags
([`disable_help_flag`][crate::Command::disable_help_flag],
[`disable_version_flag`][crate::Command::disable_version_flag]) and define your own.

# Examples

When calling `short`, use a single valid UTF-8 character which will allow using the
argument via a single hyphen (`-`) such as `-c`:

```rust
# use clap_builder as clap;
# use clap::{Command, Arg,  ArgAction};
let m = Command::new("prog")
.arg(Arg::new("config")
.short('c')
.action(ArgAction::Set))
.get_matches_from(vec![
"prog", "-c", "file.toml"
]);

assert_eq!(m.get_one::<String>("config").map(String::as_str), Some("file.toml"));
```

To use `-h` for your own flag and still have help:
```rust
# use clap_builder as clap;
# use clap::{Command, Arg,  ArgAction};
let m = Command::new("prog")
.disable_help_flag(true)
.arg(Arg::new("host")
.short('h')
.long("host"))
.arg(Arg::new("help")
.long("help")
.global(true)
.action(ArgAction::Help))
.get_matches_from(vec![
"prog", "-h", "wikipedia.org"
]);

assert_eq!(m.get_one::<String>("host").map(String::as_str), Some("wikipedia.org"));
```


**Code Examples:**


```rust
# use clap_builder as clap;
# use clap::{Command, Arg,  ArgAction};
let m = Command::new("prog")
.arg(Arg::new("config")
.short('c')
.action(ArgAction::Set))
.get_matches_from(vec![
"prog", "-c", "file.toml"
]);

assert_eq!(m.get_one::<String>("config").map(String::as_str), Some("file.toml"));
```


```rust
# use clap_builder as clap;
# use clap::{Command, Arg,  ArgAction};
let m = Command::new("prog")
.disable_help_flag(true)
.arg(Arg::new("host")
.short('h')
.long("host"))
.arg(Arg::new("help")
.long("help")
.global(true)
.action(ArgAction::Help))
.get_matches_from(vec![
"prog", "-h", "wikipedia.org"
]);

assert_eq!(m.get_one::<String>("host").map(String::as_str), Some("wikipedia.org"));
```


#### Fn: `long` (line 192)

<!-- Source: repos/clap/clap_builder/src/builder/arg.rs:192 -->

<!-- Type: fn -->


Sets the long version of the argument without the preceding `--`.

By default `version` and `help` are used by the auto-generated `version` and `help`
arguments, respectively. You may use the word `version` or `help` for the long form of your
own arguments, in which case `clap` simply will not assign those to the auto-generated
`version` or `help` arguments.

<div class="warning">

**NOTE:** Any leading `-` characters will be stripped

</div>

# Examples

To set `long` use a word containing valid UTF-8. If you supply a double leading
`--` such as `--config` they will be stripped. Hyphens in the middle of the word, however,
will *not* be stripped (i.e. `config-file` is allowed).

Setting `long` allows using the argument via a double hyphen (`--`) such as `--config`

```rust
# use clap_builder as clap;
# use clap::{Command, Arg, ArgAction};
let m = Command::new("prog")
.arg(Arg::new("cfg")
.long("config")
.action(ArgAction::Set))
.get_matches_from(vec![
"prog", "--config", "file.toml"
]);

assert_eq!(m.get_one::<String>("cfg").map(String::as_str), Some("file.toml"));
```


**Code Examples:**


```rust
# use clap_builder as clap;
# use clap::{Command, Arg, ArgAction};
let m = Command::new("prog")
.arg(Arg::new("cfg")
.long("config")
.action(ArgAction::Set))
.get_matches_from(vec![
"prog", "--config", "file.toml"
]);

assert_eq!(m.get_one::<String>("cfg").map(String::as_str), Some("file.toml"));
```


#### Fn: `alias` (line 233)

<!-- Source: repos/clap/clap_builder/src/builder/arg.rs:233 -->

<!-- Type: fn -->


Add an alias, which functions as a hidden long flag.

This is more efficient, and easier than creating multiple hidden arguments as one only
needs to check for the existence of this command, and not all variants.

# Examples

```rust
# use clap_builder as clap;
# use clap::{Command, Arg, ArgAction};
let m = Command::new("prog")
.arg(Arg::new("test")
.long("test")
.alias("alias")
.action(ArgAction::Set))
.get_matches_from(vec![
"prog", "--alias", "cool"
]);
assert_eq!(m.get_one::<String>("test").unwrap(), "cool");
```


**Code Examples:**


```rust
# use clap_builder as clap;
# use clap::{Command, Arg, ArgAction};
let m = Command::new("prog")
.arg(Arg::new("test")
.long("test")
.alias("alias")
.action(ArgAction::Set))
.get_matches_from(vec![
"prog", "--alias", "cool"
]);
assert_eq!(m.get_one::<String>("test").unwrap(), "cool");
```


#### Fn: `short_alias` (line 263)

<!-- Source: repos/clap/clap_builder/src/builder/arg.rs:263 -->

<!-- Type: fn -->


Add an alias, which functions as a hidden short flag.

This is more efficient, and easier than creating multiple hidden arguments as one only
needs to check for the existence of this command, and not all variants.

# Examples

```rust
# use clap_builder as clap;
# use clap::{Command, Arg, ArgAction};
let m = Command::new("prog")
.arg(Arg::new("test")
.short('t')
.short_alias('e')
.action(ArgAction::Set))
.get_matches_from(vec![
"prog", "-e", "cool"
]);
assert_eq!(m.get_one::<String>("test").unwrap(), "cool");
```


**Code Examples:**


```rust
# use clap_builder as clap;
# use clap::{Command, Arg, ArgAction};
let m = Command::new("prog")
.arg(Arg::new("test")
.short('t')
.short_alias('e')
.action(ArgAction::Set))
.get_matches_from(vec![
"prog", "-e", "cool"
]);
assert_eq!(m.get_one::<String>("test").unwrap(), "cool");
```


#### Fn: `aliases` (line 294)

<!-- Source: repos/clap/clap_builder/src/builder/arg.rs:294 -->

<!-- Type: fn -->


Add aliases, which function as hidden long flags.

This is more efficient, and easier than creating multiple hidden subcommands as one only
needs to check for the existence of this command, and not all variants.

# Examples

```rust
# use clap_builder as clap;
# use clap::{Command, Arg, ArgAction};
let m = Command::new("prog")
.arg(Arg::new("test")
.long("test")
.aliases(["do-stuff", "do-tests", "tests"])
.action(ArgAction::SetTrue)
.help("the file to add")
.required(false))
.get_matches_from(vec![
"prog", "--do-tests"
]);
assert_eq!(m.get_flag("test"), true);
```


**Code Examples:**


```rust
# use clap_builder as clap;
# use clap::{Command, Arg, ArgAction};
let m = Command::new("prog")
.arg(Arg::new("test")
.long("test")
.aliases(["do-stuff", "do-tests", "tests"])
.action(ArgAction::SetTrue)
.help("the file to add")
.required(false))
.get_matches_from(vec![
"prog", "--do-tests"
]);
assert_eq!(m.get_flag("test"), true);
```


#### Fn: `short_aliases` (line 323)

<!-- Source: repos/clap/clap_builder/src/builder/arg.rs:323 -->

<!-- Type: fn -->


Add aliases, which functions as a hidden short flag.

This is more efficient, and easier than creating multiple hidden subcommands as one only
needs to check for the existence of this command, and not all variants.

# Examples

```rust
# use clap_builder as clap;
# use clap::{Command, Arg, ArgAction};
let m = Command::new("prog")
.arg(Arg::new("test")
.short('t')
.short_aliases(['e', 's'])
.action(ArgAction::SetTrue)
.help("the file to add")
.required(false))
.get_matches_from(vec![
"prog", "-s"
]);
assert_eq!(m.get_flag("test"), true);
```


**Code Examples:**


```rust
# use clap_builder as clap;
# use clap::{Command, Arg, ArgAction};
let m = Command::new("prog")
.arg(Arg::new("test")
.short('t')
.short_aliases(['e', 's'])
.action(ArgAction::SetTrue)
.help("the file to add")
.required(false))
.get_matches_from(vec![
"prog", "-s"
]);
assert_eq!(m.get_flag("test"), true);
```


#### Fn: `visible_alias` (line 354)

<!-- Source: repos/clap/clap_builder/src/builder/arg.rs:354 -->

<!-- Type: fn -->


Add an alias, which functions as a visible long flag.

Like [`Arg::alias`], except that they are visible inside the help message.

# Examples

```rust
# use clap_builder as clap;
# use clap::{Command, Arg, ArgAction};
let m = Command::new("prog")
.arg(Arg::new("test")
.visible_alias("something-awesome")
.long("test")
.action(ArgAction::Set))
.get_matches_from(vec![
"prog", "--something-awesome", "coffee"
]);
assert_eq!(m.get_one::<String>("test").unwrap(), "coffee");
```
[`Command::alias`]: Arg::alias()


**Code Examples:**


```rust
# use clap_builder as clap;
# use clap::{Command, Arg, ArgAction};
let m = Command::new("prog")
.arg(Arg::new("test")
.visible_alias("something-awesome")
.long("test")
.action(ArgAction::Set))
.get_matches_from(vec![
"prog", "--something-awesome", "coffee"
]);
assert_eq!(m.get_one::<String>("test").unwrap(), "coffee");
```


#### Fn: `visible_short_alias` (line 384)

<!-- Source: repos/clap/clap_builder/src/builder/arg.rs:384 -->

<!-- Type: fn -->


Add an alias, which functions as a visible short flag.

Like [`Arg::short_alias`], except that they are visible inside the help message.

# Examples

```rust
# use clap_builder as clap;
# use clap::{Command, Arg, ArgAction};
let m = Command::new("prog")
.arg(Arg::new("test")
.long("test")
.visible_short_alias('t')
.action(ArgAction::Set))
.get_matches_from(vec![
"prog", "-t", "coffee"
]);
assert_eq!(m.get_one::<String>("test").unwrap(), "coffee");
```


**Code Examples:**


```rust
# use clap_builder as clap;
# use clap::{Command, Arg, ArgAction};
let m = Command::new("prog")
.arg(Arg::new("test")
.long("test")
.visible_short_alias('t')
.action(ArgAction::Set))
.get_matches_from(vec![
"prog", "-t", "coffee"
]);
assert_eq!(m.get_one::<String>("test").unwrap(), "coffee");
```


#### Fn: `visible_aliases` (line 414)

<!-- Source: repos/clap/clap_builder/src/builder/arg.rs:414 -->

<!-- Type: fn -->


Add aliases, which function as visible long flags.

Like [`Arg::aliases`], except that they are visible inside the help message.

# Examples

```rust
# use clap_builder as clap;
# use clap::{Command, Arg, ArgAction};
let m = Command::new("prog")
.arg(Arg::new("test")
.long("test")
.action(ArgAction::SetTrue)
.visible_aliases(["something", "awesome", "cool"]))
.get_matches_from(vec![
"prog", "--awesome"
]);
assert_eq!(m.get_flag("test"), true);
```
[`Command::aliases`]: Arg::aliases()


**Code Examples:**


```rust
# use clap_builder as clap;
# use clap::{Command, Arg, ArgAction};
let m = Command::new("prog")
.arg(Arg::new("test")
.long("test")
.action(ArgAction::SetTrue)
.visible_aliases(["something", "awesome", "cool"]))
.get_matches_from(vec![
"prog", "--awesome"
]);
assert_eq!(m.get_flag("test"), true);
```


#### Fn: `visible_short_aliases` (line 441)

<!-- Source: repos/clap/clap_builder/src/builder/arg.rs:441 -->

<!-- Type: fn -->


Add aliases, which function as visible short flags.

Like [`Arg::short_aliases`], except that they are visible inside the help message.

# Examples

```rust
# use clap_builder as clap;
# use clap::{Command, Arg, ArgAction};
let m = Command::new("prog")
.arg(Arg::new("test")
.long("test")
.action(ArgAction::SetTrue)
.visible_short_aliases(['t', 'e']))
.get_matches_from(vec![
"prog", "-t"
]);
assert_eq!(m.get_flag("test"), true);
```


**Code Examples:**


```rust
# use clap_builder as clap;
# use clap::{Command, Arg, ArgAction};
let m = Command::new("prog")
.arg(Arg::new("test")
.long("test")
.action(ArgAction::SetTrue)
.visible_short_aliases(['t', 'e']))
.get_matches_from(vec![
"prog", "-t"
]);
assert_eq!(m.get_flag("test"), true);
```


#### Fn: `index` (line 469)

<!-- Source: repos/clap/clap_builder/src/builder/arg.rs:469 -->

<!-- Type: fn -->


Specifies the index of a positional argument **starting at** 1.

<div class="warning">

**NOTE:** The index refers to position according to **other positional argument**. It does
not define position in the argument list as a whole.

</div>

<div class="warning">

**NOTE:** You can optionally leave off the `index` method, and the index will be
assigned in order of evaluation. Utilizing the `index` method allows for setting
indexes out of order

</div>

<div class="warning">

**NOTE:** This is only meant to be used for positional arguments and shouldn't to be used
with [`Arg::short`] or [`Arg::long`].

</div>

<div class="warning">

**NOTE:** When utilized with [`Arg::num_args(1..)`][Arg::num_args], only the **last** positional argument
may be defined as having a variable number of arguments (i.e. with the highest index)

</div>

# Panics

[`Command`] will [`panic!`] if indexes are skipped (such as defining `index(1)` and `index(3)`
but not `index(2)`, or a positional argument is defined as multiple and is not the highest
index (debug builds)

# Examples

```rust
# use clap_builder as clap;
# use clap::{Command, Arg};
Arg::new("config")
.index(1)
# ;
```

```rust
# use clap_builder as clap;
# use clap::{Command, Arg, ArgAction};
let m = Command::new("prog")
.arg(Arg::new("mode")
.index(1))
.arg(Arg::new("debug")
.long("debug")
.action(ArgAction::SetTrue))
.get_matches_from(vec![
"prog", "--debug", "fast"
]);

assert!(m.contains_id("mode"));
assert_eq!(m.get_one::<String>("mode").unwrap(), "fast"); // notice index(1) means "first positional"
// *not* first argument
```
[`Arg::short`]: Arg::short()
[`Arg::long`]: Arg::long()
[`Arg::num_args(true)`]: Arg::num_args()
[`Command`]: crate::Command


**Code Examples:**


```rust
# use clap_builder as clap;
# use clap::{Command, Arg};
Arg::new("config")
.index(1)
# ;
```


```rust
# use clap_builder as clap;
# use clap::{Command, Arg, ArgAction};
let m = Command::new("prog")
.arg(Arg::new("mode")
.index(1))
.arg(Arg::new("debug")
.long("debug")
.action(ArgAction::SetTrue))
.get_matches_from(vec![
"prog", "--debug", "fast"
]);

assert!(m.contains_id("mode"));
assert_eq!(m.get_one::<String>("mode").unwrap(), "fast"); // notice index(1) means "first positional"
// *not* first argument
```


#### Fn: `trailing_var_arg` (line 544)

<!-- Source: repos/clap/clap_builder/src/builder/arg.rs:544 -->

<!-- Type: fn -->


This is a "var arg" and everything that follows should be captured by it, as if the user had
used a `--`.

<div class="warning">

**NOTE:** To start the trailing "var arg" on unknown flags (and not just a positional
value), set [`allow_hyphen_values`][Arg::allow_hyphen_values].  Either way, users still
have the option to explicitly escape ambiguous arguments with `--`.

</div>

<div class="warning">

**NOTE:** [`Arg::value_delimiter`] still applies if set.

</div>

<div class="warning">

**NOTE:** Setting this requires [`Arg::num_args(..)`].

</div>

# Examples

```rust
# use clap_builder as clap;
# use clap::{Command, arg};
let m = Command::new("myprog")
.arg(arg!(<cmd> ... "commands to run").trailing_var_arg(true))
.get_matches_from(vec!["myprog", "arg1", "-r", "val1"]);

let trail: Vec<_> = m.get_many::<String>("cmd").unwrap().collect();
assert_eq!(trail, ["arg1", "-r", "val1"]);
```
[`Arg::num_args(..)`]: crate::Arg::num_args()


**Code Examples:**


```rust
# use clap_builder as clap;
# use clap::{Command, arg};
let m = Command::new("myprog")
.arg(arg!(<cmd> ... "commands to run").trailing_var_arg(true))
.get_matches_from(vec!["myprog", "arg1", "-r", "val1"]);

let trail: Vec<_> = m.get_many::<String>("cmd").unwrap().collect();
assert_eq!(trail, ["arg1", "-r", "val1"]);
```


#### Fn: `last` (line 588)

<!-- Source: repos/clap/clap_builder/src/builder/arg.rs:588 -->

<!-- Type: fn -->


This arg is the last, or final, positional argument (i.e. has the highest
index) and is *only* able to be accessed via the `--` syntax (i.e. `$ prog args --
last_arg`).

Even, if no other arguments are left to parse, if the user omits the `--` syntax
they will receive an [`UnknownArgument`] error. Setting an argument to `.last(true)` also
allows one to access this arg early using the `--` syntax. Accessing an arg early, even with
the `--` syntax is otherwise not possible.

<div class="warning">

**NOTE:** This will change the usage string to look like `$ prog [OPTIONS] [-- <ARG>]` if
`ARG` is marked as `.last(true)`.

</div>

<div class="warning">

**NOTE:** This setting will imply [`crate::Command::dont_collapse_args_in_usage`] because failing
to set this can make the usage string very confusing.

</div>

<div class="warning">

**NOTE**: This setting only applies to positional arguments, and has no effect on OPTIONS

</div>

<div class="warning">

**NOTE:** Setting this requires [taking values][Arg::num_args]

</div>

<div class="warning">

**WARNING:** Using this setting *and* having child subcommands is not
recommended with the exception of *also* using
[`crate::Command::args_conflicts_with_subcommands`]
(or [`crate::Command::subcommand_negates_reqs`] if the argument marked `Last` is also
marked [`Arg::required`])

</div>

# Examples

```rust
# use clap_builder as clap;
# use clap::{Arg, ArgAction};
Arg::new("args")
.action(ArgAction::Set)
.last(true)
# ;
```

Setting `last` ensures the arg has the highest [index] of all positional args
and requires that the `--` syntax be used to access it early.

```rust
# use clap_builder as clap;
# use clap::{Command, Arg, ArgAction};
let res = Command::new("prog")
.arg(Arg::new("first"))
.arg(Arg::new("second"))
.arg(Arg::new("third")
.action(ArgAction::Set)
.last(true))
.try_get_matches_from(vec![
"prog", "one", "--", "three"
]);

assert!(res.is_ok());
let m = res.unwrap();
assert_eq!(m.get_one::<String>("third").unwrap(), "three");
assert_eq!(m.get_one::<String>("second"), None);
```

Even if the positional argument marked `Last` is the only argument left to parse,
failing to use the `--` syntax results in an error.

```rust
# use clap_builder as clap;
# use clap::{Command, Arg, error::ErrorKind, ArgAction};
let res = Command::new("prog")
.arg(Arg::new("first"))
.arg(Arg::new("second"))
.arg(Arg::new("third")
.action(ArgAction::Set)
.last(true))
.try_get_matches_from(vec![
"prog", "one", "two", "three"
]);

assert!(res.is_err());
assert_eq!(res.unwrap_err().kind(), ErrorKind::UnknownArgument);
```
[index]: Arg::index()
[`UnknownArgument`]: crate::error::ErrorKind::UnknownArgument


**Code Examples:**


```rust
# use clap_builder as clap;
# use clap::{Arg, ArgAction};
Arg::new("args")
.action(ArgAction::Set)
.last(true)
# ;
```


```rust
# use clap_builder as clap;
# use clap::{Command, Arg, ArgAction};
let res = Command::new("prog")
.arg(Arg::new("first"))
.arg(Arg::new("second"))
.arg(Arg::new("third")
.action(ArgAction::Set)
.last(true))
.try_get_matches_from(vec![
"prog", "one", "--", "three"
]);

assert!(res.is_ok());
let m = res.unwrap();
assert_eq!(m.get_one::<String>("third").unwrap(), "three");
assert_eq!(m.get_one::<String>("second"), None);
```


```rust
# use clap_builder as clap;
# use clap::{Command, Arg, error::ErrorKind, ArgAction};
let res = Command::new("prog")
.arg(Arg::new("first"))
.arg(Arg::new("second"))
.arg(Arg::new("third")
.action(ArgAction::Set)
.last(true))
.try_get_matches_from(vec![
"prog", "one", "two", "three"
]);

assert!(res.is_err());
assert_eq!(res.unwrap_err().kind(), ErrorKind::UnknownArgument);
```


#### Fn: `required` (line 697)

<!-- Source: repos/clap/clap_builder/src/builder/arg.rs:697 -->

<!-- Type: fn -->


Specifies that the argument must be present.

Required by default means it is required, when no other conflicting rules or overrides have
been evaluated. Conflicting rules take precedence over being required.

**Pro tip:** Flags (i.e. not positional, or arguments that take values) shouldn't be
required by default. This is because if a flag were to be required, it should simply be
implied. No additional information is required from user. Flags by their very nature are
simply boolean on/off switches. The only time a user *should* be required to use a flag
is if the operation is destructive in nature, and the user is essentially proving to you,
"Yes, I know what I'm doing."

# Examples

```rust
# use clap_builder as clap;
# use clap::Arg;
Arg::new("config")
.required(true)
# ;
```

Setting required requires that the argument be used at runtime.

```rust
# use clap_builder as clap;
# use clap::{Command, Arg, ArgAction};
let res = Command::new("prog")
.arg(Arg::new("cfg")
.required(true)
.action(ArgAction::Set)
.long("config"))
.try_get_matches_from(vec![
"prog", "--config", "file.conf",
]);

assert!(res.is_ok());
```

Setting required and then *not* supplying that argument at runtime is an error.

```rust
# use clap_builder as clap;
# use clap::{Command, Arg, error::ErrorKind, ArgAction};
let res = Command::new("prog")
.arg(Arg::new("cfg")
.required(true)
.action(ArgAction::Set)
.long("config"))
.try_get_matches_from(vec![
"prog"
]);

assert!(res.is_err());
assert_eq!(res.unwrap_err().kind(), ErrorKind::MissingRequiredArgument);
```


**Code Examples:**


```rust
# use clap_builder as clap;
# use clap::Arg;
Arg::new("config")
.required(true)
# ;
```


```rust
# use clap_builder as clap;
# use clap::{Command, Arg, ArgAction};
let res = Command::new("prog")
.arg(Arg::new("cfg")
.required(true)
.action(ArgAction::Set)
.long("config"))
.try_get_matches_from(vec![
"prog", "--config", "file.conf",
]);

assert!(res.is_ok());
```


```rust
# use clap_builder as clap;
# use clap::{Command, Arg, error::ErrorKind, ArgAction};
let res = Command::new("prog")
.arg(Arg::new("cfg")
.required(true)
.action(ArgAction::Set)
.long("config"))
.try_get_matches_from(vec![
"prog"
]);

assert!(res.is_err());
assert_eq!(res.unwrap_err().kind(), ErrorKind::MissingRequiredArgument);
```


#### Fn: `requires` (line 763)

<!-- Source: repos/clap/clap_builder/src/builder/arg.rs:763 -->

<!-- Type: fn -->


Sets an argument that is required when this one is present

i.e. when using this argument, the following argument *must* be present.

<div class="warning">

**NOTE:** [Conflicting] rules and [override] rules take precedence over being required

</div>

# Examples

```rust
# use clap_builder as clap;
# use clap::Arg;
Arg::new("config")
.requires("input")
# ;
```

Setting [`Arg::requires(name)`] requires that the argument be used at runtime if the
defining argument is used. If the defining argument isn't used, the other argument isn't
required

```rust
# use clap_builder as clap;
# use clap::{Command, Arg, ArgAction};
let res = Command::new("prog")
.arg(Arg::new("cfg")
.action(ArgAction::Set)
.requires("input")
.long("config"))
.arg(Arg::new("input"))
.try_get_matches_from(vec![
"prog"
]);

assert!(res.is_ok()); // We didn't use cfg, so input wasn't required
```

Setting [`Arg::requires(name)`] and *not* supplying that argument is an error.

```rust
# use clap_builder as clap;
# use clap::{Command, Arg, error::ErrorKind, ArgAction};
let res = Command::new("prog")
.arg(Arg::new("cfg")
.action(ArgAction::Set)
.requires("input")
.long("config"))
.arg(Arg::new("input"))
.try_get_matches_from(vec![
"prog", "--config", "file.conf"
]);

assert!(res.is_err());
assert_eq!(res.unwrap_err().kind(), ErrorKind::MissingRequiredArgument);
```
[`Arg::requires(name)`]: Arg::requires()
[Conflicting]: Arg::conflicts_with()
[override]: Arg::overrides_with()


**Code Examples:**


```rust
# use clap_builder as clap;
# use clap::Arg;
Arg::new("config")
.requires("input")
# ;
```


```rust
# use clap_builder as clap;
# use clap::{Command, Arg, ArgAction};
let res = Command::new("prog")
.arg(Arg::new("cfg")
.action(ArgAction::Set)
.requires("input")
.long("config"))
.arg(Arg::new("input"))
.try_get_matches_from(vec![
"prog"
]);

assert!(res.is_ok()); // We didn't use cfg, so input wasn't required
```


```rust
# use clap_builder as clap;
# use clap::{Command, Arg, error::ErrorKind, ArgAction};
let res = Command::new("prog")
.arg(Arg::new("cfg")
.action(ArgAction::Set)
.requires("input")
.long("config"))
.arg(Arg::new("input"))
.try_get_matches_from(vec![
"prog", "--config", "file.conf"
]);

assert!(res.is_err());
assert_eq!(res.unwrap_err().kind(), ErrorKind::MissingRequiredArgument);
```


#### Fn: `exclusive` (line 834)

<!-- Source: repos/clap/clap_builder/src/builder/arg.rs:834 -->

<!-- Type: fn -->


This argument must be passed alone; it conflicts with all other arguments.

# Examples

```rust
# use clap_builder as clap;
# use clap::Arg;
Arg::new("config")
.exclusive(true)
# ;
```

Setting an exclusive argument and having any other arguments present at runtime
is an error.

```rust
# use clap_builder as clap;
# use clap::{Command, Arg, error::ErrorKind, ArgAction};
let res = Command::new("prog")
.arg(Arg::new("exclusive")
.action(ArgAction::Set)
.exclusive(true)
.long("exclusive"))
.arg(Arg::new("debug")
.long("debug"))
.arg(Arg::new("input"))
.try_get_matches_from(vec![
"prog", "--exclusive", "file.conf", "file.txt"
]);

assert!(res.is_err());
assert_eq!(res.unwrap_err().kind(), ErrorKind::ArgumentConflict);
```


**Code Examples:**


```rust
# use clap_builder as clap;
# use clap::Arg;
Arg::new("config")
.exclusive(true)
# ;
```


```rust
# use clap_builder as clap;
# use clap::{Command, Arg, error::ErrorKind, ArgAction};
let res = Command::new("prog")
.arg(Arg::new("exclusive")
.action(ArgAction::Set)
.exclusive(true)
.long("exclusive"))
.arg(Arg::new("debug")
.long("debug"))
.arg(Arg::new("input"))
.try_get_matches_from(vec![
"prog", "--exclusive", "file.conf", "file.txt"
]);

assert!(res.is_err());
assert_eq!(res.unwrap_err().kind(), ErrorKind::ArgumentConflict);
```


#### Fn: `global` (line 877)

<!-- Source: repos/clap/clap_builder/src/builder/arg.rs:877 -->

<!-- Type: fn -->


Specifies that an argument can be matched to all child [`Subcommand`]s.

<div class="warning">

**NOTE:** Global arguments *only* propagate down, **not** up (to parent commands), however
their values once a user uses them will be propagated back up to parents. In effect, this
means one should *define* all global arguments at the top level, however it doesn't matter
where the user *uses* the global argument.

</div>

# Examples

Assume an application with two subcommands, and you'd like to define a
`--verbose` flag that can be called on any of the subcommands and parent, but you don't
want to clutter the source with three duplicate [`Arg`] definitions.

```rust
# use clap_builder as clap;
# use clap::{Command, Arg, ArgAction};
let m = Command::new("prog")
.arg(Arg::new("verb")
.long("verbose")
.short('v')
.action(ArgAction::SetTrue)
.global(true))
.subcommand(Command::new("test"))
.subcommand(Command::new("do-stuff"))
.get_matches_from(vec![
"prog", "do-stuff", "--verbose"
]);

assert_eq!(m.subcommand_name(), Some("do-stuff"));
let sub_m = m.subcommand_matches("do-stuff").unwrap();
assert_eq!(sub_m.get_flag("verb"), true);
```

[`Subcommand`]: crate::Subcommand


**Code Examples:**


```rust
# use clap_builder as clap;
# use clap::{Command, Arg, ArgAction};
let m = Command::new("prog")
.arg(Arg::new("verb")
.long("verbose")
.short('v')
.action(ArgAction::SetTrue)
.global(true))
.subcommand(Command::new("test"))
.subcommand(Command::new("do-stuff"))
.get_matches_from(vec![
"prog", "do-stuff", "--verbose"
]);

assert_eq!(m.subcommand_name(), Some("do-stuff"));
let sub_m = m.subcommand_matches("do-stuff").unwrap();
assert_eq!(sub_m.get_flag("verb"), true);
```


#### Fn: `add` (line 944)

<!-- Source: repos/clap/clap_builder/src/builder/arg.rs:944 -->

<!-- Type: fn -->


Extend [`Arg`] with [`ArgExt`] data


#### Impl: `Arg` (line 953)

<!-- Source: repos/clap/clap_builder/src/builder/arg.rs:953 -->

<!-- Type: impl -->


# Value Handling


#### Fn: `action` (line 955)

<!-- Source: repos/clap/clap_builder/src/builder/arg.rs:955 -->

<!-- Type: fn -->


Specify how to react to an argument when parsing it.

[`ArgAction`] controls things like
- Overwriting previous values with new ones
- Appending new values to all previous ones
- Counting how many times a flag occurs

The default action is `ArgAction::Set`

# Examples

```rust
# use clap_builder as clap;
# use clap::Command;
# use clap::Arg;
let cmd = Command::new("mycmd")
.arg(
Arg::new("flag")
.long("flag")
.action(clap::ArgAction::Append)
);

let matches = cmd.try_get_matches_from(["mycmd", "--flag", "value"]).unwrap();
assert!(matches.contains_id("flag"));
assert_eq!(
matches.get_many::<String>("flag").unwrap_or_default().map(|v| v.as_str()).collect::<Vec<_>>(),
vec!["value"]
);
```


**Code Examples:**


```rust
# use clap_builder as clap;
# use clap::Command;
# use clap::Arg;
let cmd = Command::new("mycmd")
.arg(
Arg::new("flag")
.long("flag")
.action(clap::ArgAction::Append)
);

let matches = cmd.try_get_matches_from(["mycmd", "--flag", "value"]).unwrap();
assert!(matches.contains_id("flag"));
assert_eq!(
matches.get_many::<String>("flag").unwrap_or_default().map(|v| v.as_str()).collect::<Vec<_>>(),
vec!["value"]
);
```


#### Fn: `value_parser` (line 991)

<!-- Source: repos/clap/clap_builder/src/builder/arg.rs:991 -->

<!-- Type: fn -->


Specify the typed behavior of the argument.

This allows parsing and validating a value before storing it into
[`ArgMatches`][crate::ArgMatches] as the given type.

Possible value parsers include:
- [`value_parser!(T)`][crate::value_parser!] for auto-selecting a value parser for a given type
- Or [range expressions like `0..=1`][std::ops::RangeBounds] as a shorthand for [`RangedI64ValueParser`][crate::builder::RangedI64ValueParser]
- `Fn(&str) -> Result<T, E>`
- `[&str]` and [`PossibleValuesParser`][crate::builder::PossibleValuesParser] for static enumerated values
- [`BoolishValueParser`][crate::builder::BoolishValueParser], and [`FalseyValueParser`][crate::builder::FalseyValueParser] for alternative `bool` implementations
- [`NonEmptyStringValueParser`][crate::builder::NonEmptyStringValueParser] for basic validation for strings
- or any other [`TypedValueParser`][crate::builder::TypedValueParser] implementation

The default value is [`ValueParser::string`][crate::builder::ValueParser::string].

```rust
# use clap_builder as clap;
# use clap::ArgAction;
let mut cmd = clap::Command::new("raw")
.arg(
clap::Arg::new("color")
.long("color")
.value_parser(["always", "auto", "never"])
.default_value("auto")
)
.arg(
clap::Arg::new("hostname")
.long("hostname")
.value_parser(clap::builder::NonEmptyStringValueParser::new())
.action(ArgAction::Set)
.required(true)
)
.arg(
clap::Arg::new("port")
.long("port")
.value_parser(clap::value_parser!(u16).range(3000..))
.action(ArgAction::Set)
.required(true)
);

let m = cmd.try_get_matches_from_mut(
["cmd", "--hostname", "rust-lang.org", "--port", "3001"]
).unwrap();

let color: &String = m.get_one("color")
.expect("default");
assert_eq!(color, "auto");

let hostname: &String = m.get_one("hostname")
.expect("required");
assert_eq!(hostname, "rust-lang.org");

let port: u16 = *m.get_one("port")
.expect("required");
assert_eq!(port, 3001);
```


**Code Examples:**


```rust
# use clap_builder as clap;
# use clap::ArgAction;
let mut cmd = clap::Command::new("raw")
.arg(
clap::Arg::new("color")
.long("color")
.value_parser(["always", "auto", "never"])
.default_value("auto")
)
.arg(
clap::Arg::new("hostname")
.long("hostname")
.value_parser(clap::builder::NonEmptyStringValueParser::new())
.action(ArgAction::Set)
.required(true)
)
.arg(
clap::Arg::new("port")
.long("port")
.value_parser(clap::value_parser!(u16).range(3000..))
.action(ArgAction::Set)
.required(true)
);

let m = cmd.try_get_matches_from_mut(
["cmd", "--hostname", "rust-lang.org", "--port", "3001"]
).unwrap();

let color: &String = m.get_one("color")
.expect("default");
assert_eq!(color, "auto");

let hostname: &String = m.get_one("hostname")
.expect("required");
assert_eq!(hostname, "rust-lang.org");

let port: u16 = *m.get_one("port")
.expect("required");
assert_eq!(port, 3001);
```


#### Fn: `num_args` (line 1053)

<!-- Source: repos/clap/clap_builder/src/builder/arg.rs:1053 -->

<!-- Type: fn -->


Specifies the number of arguments parsed per occurrence

For example, if you had a `-f <file>` argument where you wanted exactly 3 'files' you would
set `.num_args(3)`, and this argument wouldn't be satisfied unless the user
provided 3 and only 3 values.

Users may specify values for arguments in any of the following methods

- Using a space such as `-o value` or `--option value`
- Using an equals and no space such as `-o=value` or `--option=value`
- Use a short and no space such as `-ovalue`

<div class="warning">

**WARNING:**

Setting a variable number of values (e.g. `1..=10`) for an argument without
other details can be dangerous in some circumstances. Because multiple values are
allowed, `--option val1 val2 val3` is perfectly valid. Be careful when designing a CLI
where **positional arguments** or **subcommands** are *also* expected as `clap` will continue
parsing *values* until one of the following happens:

- It reaches the maximum number of values
- It reaches a specific number of values
- It finds another flag or option (i.e. something that starts with a `-`)
- It reaches the [`Arg::value_terminator`] if set

Alternatively,
- Use a delimiter between values with [`Arg::value_delimiter`]
- Require a flag occurrence per value with [`ArgAction::Append`]
- Require positional arguments to appear after `--` with [`Arg::last`]

</div>

# Examples

Option:
```rust
# use clap_builder as clap;
# use clap::{Command, Arg};
let m = Command::new("prog")
.arg(Arg::new("mode")
.long("mode")
.num_args(1))
.get_matches_from(vec![
"prog", "--mode", "fast"
]);

assert_eq!(m.get_one::<String>("mode").unwrap(), "fast");
```

Flag/option hybrid (see also [`default_missing_value`][Arg::default_missing_value])
```rust
# use clap_builder as clap;
# use clap::{Command, Arg, error::ErrorKind, ArgAction};
let cmd = Command::new("prog")
.arg(Arg::new("mode")
.long("mode")
.default_missing_value("slow")
.default_value("plaid")
.num_args(0..=1));

let m = cmd.clone()
.get_matches_from(vec![
"prog", "--mode", "fast"
]);
assert_eq!(m.get_one::<String>("mode").unwrap(), "fast");

let m = cmd.clone()
.get_matches_from(vec![
"prog", "--mode",
]);
assert_eq!(m.get_one::<String>("mode").unwrap(), "slow");

let m = cmd.clone()
.get_matches_from(vec![
"prog",
]);
assert_eq!(m.get_one::<String>("mode").unwrap(), "plaid");
```

Tuples
```rust
# use clap_builder as clap;
# use clap::{Command, Arg, error::ErrorKind, ArgAction};
let cmd = Command::new("prog")
.arg(Arg::new("file")
.action(ArgAction::Set)
.num_args(2)
.short('F'));

let m = cmd.clone()
.get_matches_from(vec![
"prog", "-F", "in-file", "out-file"
]);
assert_eq!(
m.get_many::<String>("file").unwrap_or_default().map(|v| v.as_str()).collect::<Vec<_>>(),
vec!["in-file", "out-file"]
);

let res = cmd.clone()
.try_get_matches_from(vec![
"prog", "-F", "file1"
]);
assert_eq!(res.unwrap_err().kind(), ErrorKind::WrongNumberOfValues);
```

A common mistake is to define an option which allows multiple values and a positional
argument.
```rust
# use clap_builder as clap;
# use clap::{Command, Arg, ArgAction};
let cmd = Command::new("prog")
.arg(Arg::new("file")
.action(ArgAction::Set)
.num_args(0..)
.short('F'))
.arg(Arg::new("word"));

let m = cmd.clone().get_matches_from(vec![
"prog", "-F", "file1", "file2", "file3", "word"
]);
let files: Vec<_> = m.get_many::<String>("file").unwrap().collect();
assert_eq!(files, ["file1", "file2", "file3", "word"]); // wait...what?!
assert!(!m.contains_id("word")); // but we clearly used word!

// but this works
let m = cmd.clone().get_matches_from(vec![
"prog", "word", "-F", "file1", "file2", "file3",
]);
let files: Vec<_> = m.get_many::<String>("file").unwrap().collect();
assert_eq!(files, ["file1", "file2", "file3"]);
assert_eq!(m.get_one::<String>("word").unwrap(), "word");
```
The problem is `clap` doesn't know when to stop parsing values for "file".

A solution for the example above is to limit how many values with a maximum, or specific
number, or to say [`ArgAction::Append`] is ok, but multiple values are not.
```rust
# use clap_builder as clap;
# use clap::{Command, Arg, ArgAction};
let m = Command::new("prog")
.arg(Arg::new("file")
.action(ArgAction::Append)
.short('F'))
.arg(Arg::new("word"))
.get_matches_from(vec![
"prog", "-F", "file1", "-F", "file2", "-F", "file3", "word"
]);

let files: Vec<_> = m.get_many::<String>("file").unwrap().collect();
assert_eq!(files, ["file1", "file2", "file3"]);
assert_eq!(m.get_one::<String>("word").unwrap(), "word");
```


**Code Examples:**


```rust
# use clap_builder as clap;
# use clap::{Command, Arg};
let m = Command::new("prog")
.arg(Arg::new("mode")
.long("mode")
.num_args(1))
.get_matches_from(vec![
"prog", "--mode", "fast"
]);

assert_eq!(m.get_one::<String>("mode").unwrap(), "fast");
```


```rust
# use clap_builder as clap;
# use clap::{Command, Arg, error::ErrorKind, ArgAction};
let cmd = Command::new("prog")
.arg(Arg::new("mode")
.long("mode")
.default_missing_value("slow")
.default_value("plaid")
.num_args(0..=1));

let m = cmd.clone()
.get_matches_from(vec![
"prog", "--mode", "fast"
]);
assert_eq!(m.get_one::<String>("mode").unwrap(), "fast");

let m = cmd.clone()
.get_matches_from(vec![
"prog", "--mode",
]);
assert_eq!(m.get_one::<String>("mode").unwrap(), "slow");

let m = cmd.clone()
.get_matches_from(vec![
"prog",
]);
assert_eq!(m.get_one::<String>("mode").unwrap(), "plaid");
```


```rust
# use clap_builder as clap;
# use clap::{Command, Arg, error::ErrorKind, ArgAction};
let cmd = Command::new("prog")
.arg(Arg::new("file")
.action(ArgAction::Set)
.num_args(2)
.short('F'));

let m = cmd.clone()
.get_matches_from(vec![
"prog", "-F", "in-file", "out-file"
]);
assert_eq!(
m.get_many::<String>("file").unwrap_or_default().map(|v| v.as_str()).collect::<Vec<_>>(),
vec!["in-file", "out-file"]
);

let res = cmd.clone()
.try_get_matches_from(vec![
"prog", "-F", "file1"
]);
assert_eq!(res.unwrap_err().kind(), ErrorKind::WrongNumberOfValues);
```


```rust
# use clap_builder as clap;
# use clap::{Command, Arg, ArgAction};
let cmd = Command::new("prog")
.arg(Arg::new("file")
.action(ArgAction::Set)
.num_args(0..)
.short('F'))
.arg(Arg::new("word"));

let m = cmd.clone().get_matches_from(vec![
"prog", "-F", "file1", "file2", "file3", "word"
]);
let files: Vec<_> = m.get_many::<String>("file").unwrap().collect();
assert_eq!(files, ["file1", "file2", "file3", "word"]); // wait...what?!
assert!(!m.contains_id("word")); // but we clearly used word!

// but this works
let m = cmd.clone().get_matches_from(vec![
"prog", "word", "-F", "file1", "file2", "file3",
]);
let files: Vec<_> = m.get_many::<String>("file").unwrap().collect();
assert_eq!(files, ["file1", "file2", "file3"]);
assert_eq!(m.get_one::<String>("word").unwrap(), "word");
```


```rust
# use clap_builder as clap;
# use clap::{Command, Arg, ArgAction};
let m = Command::new("prog")
.arg(Arg::new("file")
.action(ArgAction::Append)
.short('F'))
.arg(Arg::new("word"))
.get_matches_from(vec![
"prog", "-F", "file1", "-F", "file2", "-F", "file3", "word"
]);

let files: Vec<_> = m.get_many::<String>("file").unwrap().collect();
assert_eq!(files, ["file1", "file2", "file3"]);
assert_eq!(m.get_one::<String>("word").unwrap(), "word");
```


#### Fn: `value_name` (line 1223)

<!-- Source: repos/clap/clap_builder/src/builder/arg.rs:1223 -->

<!-- Type: fn -->


Placeholder for the argument's value in the help message / usage.

This name is cosmetic only; the name is **not** used to access arguments.
This setting can be very helpful when describing the type of input the user should be
using, such as `FILE`, `INTERFACE`, etc. Although not required, it's somewhat convention to
use all capital letters for the value name.

<div class="warning">

**NOTE:** implicitly sets [`Arg::action(ArgAction::Set)`]

</div>

# Examples

```rust
# use clap_builder as clap;
# use clap::{Command, Arg};
Arg::new("cfg")
.long("config")
.value_name("FILE")
# ;
```

```rust
# use clap_builder as clap;
# #[cfg(feature = "help")] {
# use clap::{Command, Arg};
let m = Command::new("prog")
.arg(Arg::new("config")
.long("config")
.value_name("FILE")
.help("Some help text"))
.get_matches_from(vec![
"prog", "--help"
]);
# }
```
Running the above program produces the following output

```text
valnames

Usage: valnames [OPTIONS]

Options:
--config <FILE>     Some help text
-h, --help          Print help information
-V, --version       Print version information
```
[positional]: Arg::index()
[`Arg::action(ArgAction::Set)`]: Arg::action()


**Code Examples:**


```rust
# use clap_builder as clap;
# use clap::{Command, Arg};
Arg::new("cfg")
.long("config")
.value_name("FILE")
# ;
```


```rust
# use clap_builder as clap;
# #[cfg(feature = "help")] {
# use clap::{Command, Arg};
let m = Command::new("prog")
.arg(Arg::new("config")
.long("config")
.value_name("FILE")
.help("Some help text"))
.get_matches_from(vec![
"prog", "--help"
]);
# }
```


#### Fn: `value_names` (line 1286)

<!-- Source: repos/clap/clap_builder/src/builder/arg.rs:1286 -->

<!-- Type: fn -->


Placeholders for the argument's values in the help message / usage.

These names are cosmetic only, used for help and usage strings only. The names are **not**
used to access arguments. The values of the arguments are accessed in numeric order (i.e.
if you specify two names `one` and `two` `one` will be the first matched value, `two` will
be the second).

This setting can be very helpful when describing the type of input the user should be
using, such as `FILE`, `INTERFACE`, etc. Although not required, it's somewhat convention to
use all capital letters for the value name.

<div class="warning">

**TIP:** It may help to use [`Arg::next_line_help(true)`] if there are long, or
multiple value names in order to not throw off the help text alignment of all options.

</div>

<div class="warning">

**NOTE:** implicitly sets [`Arg::action(ArgAction::Set)`] and [`Arg::num_args(1..)`].

</div>

# Examples

```rust
# use clap_builder as clap;
# use clap::{Command, Arg};
Arg::new("speed")
.short('s')
.value_names(["fast", "slow"]);
```

```rust
# use clap_builder as clap;
# #[cfg(feature = "help")] {
# use clap::{Command, Arg};
let m = Command::new("prog")
.arg(Arg::new("io")
.long("io-files")
.value_names(["INFILE", "OUTFILE"]))
.get_matches_from(vec![
"prog", "--help"
]);
# }
```

Running the above program produces the following output

```text
valnames

Usage: valnames [OPTIONS]

Options:
-h, --help                       Print help information
--io-files <INFILE> <OUTFILE>    Some help text
-V, --version                    Print version information
```
[`Arg::next_line_help(true)`]: Arg::next_line_help()
[`Arg::num_args`]: Arg::num_args()
[`Arg::action(ArgAction::Set)`]: Arg::action()
[`Arg::num_args(1..)`]: Arg::num_args()


**Code Examples:**


```rust
# use clap_builder as clap;
# use clap::{Command, Arg};
Arg::new("speed")
.short('s')
.value_names(["fast", "slow"]);
```


```rust
# use clap_builder as clap;
# #[cfg(feature = "help")] {
# use clap::{Command, Arg};
let m = Command::new("prog")
.arg(Arg::new("io")
.long("io-files")
.value_names(["INFILE", "OUTFILE"]))
.get_matches_from(vec![
"prog", "--help"
]);
# }
```


#### Fn: `value_hint` (line 1356)

<!-- Source: repos/clap/clap_builder/src/builder/arg.rs:1356 -->

<!-- Type: fn -->


Provide the shell a hint about how to complete this argument.

See [`ValueHint`] for more information.

<div class="warning">

**NOTE:** implicitly sets [`Arg::action(ArgAction::Set)`][ArgAction::Set].

</div>

For example, to take a username as argument:

```rust
# use clap_builder as clap;
# use clap::{Arg, ValueHint};
Arg::new("user")
.short('u')
.long("user")
.value_hint(ValueHint::Username);
```

To take a full command line and its arguments (for example, when writing a command wrapper):

```rust
# use clap_builder as clap;
# use clap::{Command, Arg, ValueHint, ArgAction};
Command::new("prog")
.trailing_var_arg(true)
.arg(
Arg::new("command")
.action(ArgAction::Set)
.num_args(1..)
.value_hint(ValueHint::CommandWithArguments)
);
```


**Code Examples:**


```rust
# use clap_builder as clap;
# use clap::{Arg, ValueHint};
Arg::new("user")
.short('u')
.long("user")
.value_hint(ValueHint::Username);
```


```rust
# use clap_builder as clap;
# use clap::{Command, Arg, ValueHint, ArgAction};
Command::new("prog")
.trailing_var_arg(true)
.arg(
Arg::new("command")
.action(ArgAction::Set)
.num_args(1..)
.value_hint(ValueHint::CommandWithArguments)
);
```


#### Fn: `ignore_case` (line 1405)

<!-- Source: repos/clap/clap_builder/src/builder/arg.rs:1405 -->

<!-- Type: fn -->


Match values against [`PossibleValuesParser`][crate::builder::PossibleValuesParser] without matching case.

When other arguments are conditionally required based on the
value of a case-insensitive argument, the equality check done
by [`Arg::required_if_eq`], [`Arg::required_if_eq_any`], or
[`Arg::required_if_eq_all`] is case-insensitive.


<div class="warning">

**NOTE:** Setting this requires [taking values][Arg::num_args]

</div>

<div class="warning">

**NOTE:** To do unicode case folding, enable the `unicode` feature flag.

</div>

# Examples

```rust
# use clap_builder as clap;
# use clap::{Command, Arg, ArgAction};
let m = Command::new("pv")
.arg(Arg::new("option")
.long("option")
.action(ArgAction::Set)
.ignore_case(true)
.value_parser(["test123"]))
.get_matches_from(vec![
"pv", "--option", "TeSt123",
]);

assert!(m.get_one::<String>("option").unwrap().eq_ignore_ascii_case("test123"));
```

This setting also works when multiple values can be defined:

```rust
# use clap_builder as clap;
# use clap::{Command, Arg, ArgAction};
let m = Command::new("pv")
.arg(Arg::new("option")
.short('o')
.long("option")
.action(ArgAction::Set)
.ignore_case(true)
.num_args(1..)
.value_parser(["test123", "test321"]))
.get_matches_from(vec![
"pv", "--option", "TeSt123", "teST123", "tESt321"
]);

let matched_vals = m.get_many::<String>("option").unwrap().collect::<Vec<_>>();
assert_eq!(&*matched_vals, &["TeSt123", "teST123", "tESt321"]);
```


**Code Examples:**


```rust
# use clap_builder as clap;
# use clap::{Command, Arg, ArgAction};
let m = Command::new("pv")
.arg(Arg::new("option")
.long("option")
.action(ArgAction::Set)
.ignore_case(true)
.value_parser(["test123"]))
.get_matches_from(vec![
"pv", "--option", "TeSt123",
]);

assert!(m.get_one::<String>("option").unwrap().eq_ignore_ascii_case("test123"));
```


```rust
# use clap_builder as clap;
# use clap::{Command, Arg, ArgAction};
let m = Command::new("pv")
.arg(Arg::new("option")
.short('o')
.long("option")
.action(ArgAction::Set)
.ignore_case(true)
.num_args(1..)
.value_parser(["test123", "test321"]))
.get_matches_from(vec![
"pv", "--option", "TeSt123", "teST123", "tESt321"
]);

let matched_vals = m.get_many::<String>("option").unwrap().collect::<Vec<_>>();
assert_eq!(&*matched_vals, &["TeSt123", "teST123", "tESt321"]);
```


#### Fn: `allow_hyphen_values` (line 1473)

<!-- Source: repos/clap/clap_builder/src/builder/arg.rs:1473 -->

<!-- Type: fn -->


Allows values which start with a leading hyphen (`-`)

To limit values to just numbers, see
[`allow_negative_numbers`][Arg::allow_negative_numbers].

See also [`trailing_var_arg`][Arg::trailing_var_arg].

<div class="warning">

**NOTE:** Setting this requires [taking values][Arg::num_args]

</div>

<div class="warning">

**WARNING:** Prior arguments with `allow_hyphen_values(true)` get precedence over known
flags but known flags get precedence over the next possible positional argument with
`allow_hyphen_values(true)`.  When combined with [`Arg::num_args(..)`][Arg::num_args],
[`Arg::value_terminator`] is one way to ensure processing stops.

</div>

<div class="warning">

**WARNING**: Take caution when using this setting combined with another argument using
[`Arg::num_args`], as this becomes ambiguous `$ prog --arg -- -- val`. All
three `--, --, val` will be values when the user may have thought the second `--` would
constitute the normal, "Only positional args follow" idiom.

</div>

# Examples

```rust
# use clap_builder as clap;
# use clap::{Command, Arg, ArgAction};
let m = Command::new("prog")
.arg(Arg::new("pat")
.action(ArgAction::Set)
.allow_hyphen_values(true)
.long("pattern"))
.get_matches_from(vec![
"prog", "--pattern", "-file"
]);

assert_eq!(m.get_one::<String>("pat").unwrap(), "-file");
```

Not setting `Arg::allow_hyphen_values(true)` and supplying a value which starts with a
hyphen is an error.

```rust
# use clap_builder as clap;
# use clap::{Command, Arg, error::ErrorKind, ArgAction};
let res = Command::new("prog")
.arg(Arg::new("pat")
.action(ArgAction::Set)
.long("pattern"))
.try_get_matches_from(vec![
"prog", "--pattern", "-file"
]);

assert!(res.is_err());
assert_eq!(res.unwrap_err().kind(), ErrorKind::UnknownArgument);
```
[`Arg::num_args(1)`]: Arg::num_args()


**Code Examples:**


```rust
# use clap_builder as clap;
# use clap::{Command, Arg, ArgAction};
let m = Command::new("prog")
.arg(Arg::new("pat")
.action(ArgAction::Set)
.allow_hyphen_values(true)
.long("pattern"))
.get_matches_from(vec![
"prog", "--pattern", "-file"
]);

assert_eq!(m.get_one::<String>("pat").unwrap(), "-file");
```


```rust
# use clap_builder as clap;
# use clap::{Command, Arg, error::ErrorKind, ArgAction};
let res = Command::new("prog")
.arg(Arg::new("pat")
.action(ArgAction::Set)
.long("pattern"))
.try_get_matches_from(vec![
"prog", "--pattern", "-file"
]);

assert!(res.is_err());
assert_eq!(res.unwrap_err().kind(), ErrorKind::UnknownArgument);
```


#### Fn: `allow_negative_numbers` (line 1549)

<!-- Source: repos/clap/clap_builder/src/builder/arg.rs:1549 -->

<!-- Type: fn -->


Allows negative numbers to pass as values.

This is similar to [`Arg::allow_hyphen_values`] except that it only allows numbers,
all other undefined leading hyphens will fail to parse.

<div class="warning">

**NOTE:** Setting this requires [taking values][Arg::num_args]

</div>

# Examples

```rust
# use clap_builder as clap;
# use clap::{Command, Arg};
let res = Command::new("myprog")
.arg(Arg::new("num").allow_negative_numbers(true))
.try_get_matches_from(vec![
"myprog", "-20"
]);
assert!(res.is_ok());
let m = res.unwrap();
assert_eq!(m.get_one::<String>("num").unwrap(), "-20");
```


**Code Examples:**


```rust
# use clap_builder as clap;
# use clap::{Command, Arg};
let res = Command::new("myprog")
.arg(Arg::new("num").allow_negative_numbers(true))
.try_get_matches_from(vec![
"myprog", "-20"
]);
assert!(res.is_ok());
let m = res.unwrap();
assert_eq!(m.get_one::<String>("num").unwrap(), "-20");
```


#### Fn: `require_equals` (line 1583)

<!-- Source: repos/clap/clap_builder/src/builder/arg.rs:1583 -->

<!-- Type: fn -->


Requires that options use the `--option=val` syntax

i.e. an equals between the option and associated value.

<div class="warning">

**NOTE:** Setting this requires [taking values][Arg::num_args]

</div>

# Examples

Setting `require_equals` requires that the option have an equals sign between
it and the associated value.

```rust
# use clap_builder as clap;
# use clap::{Command, Arg, ArgAction};
let res = Command::new("prog")
.arg(Arg::new("cfg")
.action(ArgAction::Set)
.require_equals(true)
.long("config"))
.try_get_matches_from(vec![
"prog", "--config=file.conf"
]);

assert!(res.is_ok());
```

Setting `require_equals` and *not* supplying the equals will cause an
error.

```rust
# use clap_builder as clap;
# use clap::{Command, Arg, error::ErrorKind, ArgAction};
let res = Command::new("prog")
.arg(Arg::new("cfg")
.action(ArgAction::Set)
.require_equals(true)
.long("config"))
.try_get_matches_from(vec![
"prog", "--config", "file.conf"
]);

assert!(res.is_err());
assert_eq!(res.unwrap_err().kind(), ErrorKind::NoEquals);
```


**Code Examples:**


```rust
# use clap_builder as clap;
# use clap::{Command, Arg, ArgAction};
let res = Command::new("prog")
.arg(Arg::new("cfg")
.action(ArgAction::Set)
.require_equals(true)
.long("config"))
.try_get_matches_from(vec![
"prog", "--config=file.conf"
]);

assert!(res.is_ok());
```


```rust
# use clap_builder as clap;
# use clap::{Command, Arg, error::ErrorKind, ArgAction};
let res = Command::new("prog")
.arg(Arg::new("cfg")
.action(ArgAction::Set)
.require_equals(true)
.long("config"))
.try_get_matches_from(vec![
"prog", "--config", "file.conf"
]);

assert!(res.is_err());
assert_eq!(res.unwrap_err().kind(), ErrorKind::NoEquals);
```


#### Fn: `value_delimiter` (line 1655)

<!-- Source: repos/clap/clap_builder/src/builder/arg.rs:1655 -->

<!-- Type: fn -->


Allow grouping of multiple values via a delimiter.

i.e. allow values (`val1,val2,val3`) to be parsed as three values (`val1`, `val2`,
and `val3`) instead of one value (`val1,val2,val3`).

See also [`Command::dont_delimit_trailing_values`][crate::Command::dont_delimit_trailing_values].

# Examples

```rust
# use clap_builder as clap;
# use clap::{Command, Arg};
let m = Command::new("prog")
.arg(Arg::new("config")
.short('c')
.long("config")
.value_delimiter(','))
.get_matches_from(vec![
"prog", "--config=val1,val2,val3"
]);

assert_eq!(m.get_many::<String>("config").unwrap().collect::<Vec<_>>(), ["val1", "val2", "val3"])
```
[`Arg::value_delimiter(',')`]: Arg::value_delimiter()
[`Arg::action(ArgAction::Set)`]: Arg::action()


**Code Examples:**


```rust
# use clap_builder as clap;
# use clap::{Command, Arg};
let m = Command::new("prog")
.arg(Arg::new("config")
.short('c')
.long("config")
.value_delimiter(','))
.get_matches_from(vec![
"prog", "--config=val1,val2,val3"
]);

assert_eq!(m.get_many::<String>("config").unwrap().collect::<Vec<_>>(), ["val1", "val2", "val3"])
```


#### Fn: `value_terminator` (line 1687)

<!-- Source: repos/clap/clap_builder/src/builder/arg.rs:1687 -->

<!-- Type: fn -->


Sentinel to **stop** parsing multiple values of a given argument.

By default when
one sets [`num_args(1..)`] on an argument, clap will continue parsing values for that
argument until it reaches another valid argument, or one of the other more specific settings
for multiple values is used (such as [`num_args`]).

<div class="warning">

**NOTE:** This setting only applies to [options] and [positional arguments]

</div>

<div class="warning">

**NOTE:** When the terminator is passed in on the command line, it is **not** stored as one
of the values

</div>

# Examples

```rust
# use clap_builder as clap;
# use clap::{Command, Arg, ArgAction};
Arg::new("vals")
.action(ArgAction::Set)
.num_args(1..)
.value_terminator(";")
# ;
```

The following example uses two arguments, a sequence of commands, and the location in which
to perform them

```rust
# use clap_builder as clap;
# use clap::{Command, Arg, ArgAction};
let m = Command::new("prog")
.arg(Arg::new("cmds")
.action(ArgAction::Set)
.num_args(1..)
.allow_hyphen_values(true)
.value_terminator(";"))
.arg(Arg::new("location"))
.get_matches_from(vec![
"prog", "find", "-type", "f", "-name", "special", ";", "/home/clap"
]);
let cmds: Vec<_> = m.get_many::<String>("cmds").unwrap().collect();
assert_eq!(&cmds, &["find", "-type", "f", "-name", "special"]);
assert_eq!(m.get_one::<String>("location").unwrap(), "/home/clap");
```
[options]: Arg::action
[positional arguments]: Arg::index()
[`num_args(1..)`]: Arg::num_args()
[`num_args`]: Arg::num_args()


**Code Examples:**


```rust
# use clap_builder as clap;
# use clap::{Command, Arg, ArgAction};
Arg::new("vals")
.action(ArgAction::Set)
.num_args(1..)
.value_terminator(";")
# ;
```


```rust
# use clap_builder as clap;
# use clap::{Command, Arg, ArgAction};
let m = Command::new("prog")
.arg(Arg::new("cmds")
.action(ArgAction::Set)
.num_args(1..)
.allow_hyphen_values(true)
.value_terminator(";"))
.arg(Arg::new("location"))
.get_matches_from(vec![
"prog", "find", "-type", "f", "-name", "special", ";", "/home/clap"
]);
let cmds: Vec<_> = m.get_many::<String>("cmds").unwrap().collect();
assert_eq!(&cmds, &["find", "-type", "f", "-name", "special"]);
assert_eq!(m.get_one::<String>("location").unwrap(), "/home/clap");
```


#### Fn: `raw` (line 1750)

<!-- Source: repos/clap/clap_builder/src/builder/arg.rs:1750 -->

<!-- Type: fn -->


Consume all following arguments.

Do not parse them individually, but rather pass them in entirety.

It is worth noting that setting this requires all values to come after a `--` to indicate
they should all be captured. For example:

```text
--foo something -- -v -v -v -b -b -b --baz -q -u -x
```

Will result in everything after `--` to be considered one raw argument. This behavior
may not be exactly what you are expecting and using [`Arg::trailing_var_arg`]
may be more appropriate.

<div class="warning">

**NOTE:** Implicitly sets [`Arg::action(ArgAction::Set)`], [`Arg::num_args(1..)`],
[`Arg::allow_hyphen_values(true)`], and [`Arg::last(true)`] when set to `true`.

</div>

[`Arg::action(ArgAction::Set)`]: Arg::action()
[`Arg::num_args(1..)`]: Arg::num_args()
[`Arg::allow_hyphen_values(true)`]: Arg::allow_hyphen_values()
[`Arg::last(true)`]: Arg::last()


#### Fn: `default_value` (line 1785)

<!-- Source: repos/clap/clap_builder/src/builder/arg.rs:1785 -->

<!-- Type: fn -->


Value for the argument when not present.

Like with command-line values, this will be split by [`Arg::value_delimiter`].

<div class="warning">

**NOTE:** If the user *does not* use this argument at runtime [`ArgMatches::contains_id`] will
still return `true`. If you wish to determine whether the argument was used at runtime or
not, consider [`ArgMatches::value_source`][crate::ArgMatches::value_source].

</div>

<div class="warning">

**NOTE:** This setting is perfectly compatible with [`Arg::default_value_if`] but slightly
different. `Arg::default_value` *only* takes effect when the user has not provided this arg
at runtime. `Arg::default_value_if` however only takes effect when the user has not provided
a value at runtime **and** these other conditions are met as well. If you have set
`Arg::default_value` and `Arg::default_value_if`, and the user **did not** provide this arg
at runtime, nor were the conditions met for `Arg::default_value_if`, the `Arg::default_value`
will be applied.

</div>

# Examples

First we use the default value without providing any value at runtime.

```rust
# use clap_builder as clap;
# use clap::{Command, Arg, parser::ValueSource};
let m = Command::new("prog")
.arg(Arg::new("opt")
.long("myopt")
.default_value("myval"))
.get_matches_from(vec![
"prog"
]);

assert_eq!(m.get_one::<String>("opt").unwrap(), "myval");
assert!(m.contains_id("opt"));
assert_eq!(m.value_source("opt"), Some(ValueSource::DefaultValue));
```

Next we provide a value at runtime to override the default.

```rust
# use clap_builder as clap;
# use clap::{Command, Arg, parser::ValueSource};
let m = Command::new("prog")
.arg(Arg::new("opt")
.long("myopt")
.default_value("myval"))
.get_matches_from(vec![
"prog", "--myopt=non_default"
]);

assert_eq!(m.get_one::<String>("opt").unwrap(), "non_default");
assert!(m.contains_id("opt"));
assert_eq!(m.value_source("opt"), Some(ValueSource::CommandLine));
```
[`Arg::action(ArgAction::Set)`]: Arg::action()
[`ArgMatches::contains_id`]: crate::ArgMatches::contains_id()
[`Arg::default_value_if`]: Arg::default_value_if()


**Code Examples:**


```rust
# use clap_builder as clap;
# use clap::{Command, Arg, parser::ValueSource};
let m = Command::new("prog")
.arg(Arg::new("opt")
.long("myopt")
.default_value("myval"))
.get_matches_from(vec![
"prog"
]);

assert_eq!(m.get_one::<String>("opt").unwrap(), "myval");
assert!(m.contains_id("opt"));
assert_eq!(m.value_source("opt"), Some(ValueSource::DefaultValue));
```


```rust
# use clap_builder as clap;
# use clap::{Command, Arg, parser::ValueSource};
let m = Command::new("prog")
.arg(Arg::new("opt")
.long("myopt")
.default_value("myval"))
.get_matches_from(vec![
"prog", "--myopt=non_default"
]);

assert_eq!(m.get_one::<String>("opt").unwrap(), "non_default");
assert!(m.contains_id("opt"));
assert_eq!(m.value_source("opt"), Some(ValueSource::CommandLine));
```


#### Fn: `default_values` (line 1871)

<!-- Source: repos/clap/clap_builder/src/builder/arg.rs:1871 -->

<!-- Type: fn -->


Value for the argument when not present.

See [`Arg::default_value`].

[`Arg::default_value`]: Arg::default_value()


#### Fn: `default_missing_value` (line 1894)

<!-- Source: repos/clap/clap_builder/src/builder/arg.rs:1894 -->

<!-- Type: fn -->


Value for the argument when the flag is present but no value is specified.

This configuration option is often used to give the user a shortcut and allow them to
efficiently specify an option argument without requiring an explicitly value. The `--color`
argument is a common example. By supplying a default, such as `default_missing_value("always")`,
the user can quickly just add `--color` to the command line to produce the desired color output.

Like with command-line values, this will be split by [`Arg::value_delimiter`].

<div class="warning">

**NOTE:** using this configuration option requires the use of the
[`.num_args(0..N)`][Arg::num_args] and the
[`.require_equals(true)`][Arg::require_equals] configuration option. These are required in
order to unambiguously determine what, if any, value was supplied for the argument.

</div>

# Examples

For POSIX style `--color`:
```rust
# use clap_builder as clap;
# use clap::{Command, Arg, parser::ValueSource};
fn cli() -> Command {
Command::new("prog")
.arg(Arg::new("color").long("color")
.value_name("WHEN")
.value_parser(["always", "auto", "never"])
.default_value("auto")
.num_args(0..=1)
.require_equals(true)
.default_missing_value("always")
.help("Specify WHEN to colorize output.")
)
}

// first, we'll provide no arguments
let m  = cli().get_matches_from(vec![
"prog"
]);
assert_eq!(m.get_one::<String>("color").unwrap(), "auto");
assert_eq!(m.value_source("color"), Some(ValueSource::DefaultValue));

// next, we'll provide a runtime value to override the default (as usually done).
let m  = cli().get_matches_from(vec![
"prog", "--color=never"
]);
assert_eq!(m.get_one::<String>("color").unwrap(), "never");
assert_eq!(m.value_source("color"), Some(ValueSource::CommandLine));

// finally, we will use the shortcut and only provide the argument without a value.
let m  = cli().get_matches_from(vec![
"prog", "--color"
]);
assert_eq!(m.get_one::<String>("color").unwrap(), "always");
assert_eq!(m.value_source("color"), Some(ValueSource::CommandLine));
```

For bool literals:
```rust
# use clap_builder as clap;
# use clap::{Command, Arg, parser::ValueSource, value_parser};
fn cli() -> Command {
Command::new("prog")
.arg(Arg::new("create").long("create")
.value_name("BOOL")
.value_parser(value_parser!(bool))
.num_args(0..=1)
.require_equals(true)
.default_missing_value("true")
)
}

// first, we'll provide no arguments
let m  = cli().get_matches_from(vec![
"prog"
]);
assert_eq!(m.get_one::<bool>("create").copied(), None);

// next, we'll provide a runtime value to override the default (as usually done).
let m  = cli().get_matches_from(vec![
"prog", "--create=false"
]);
assert_eq!(m.get_one::<bool>("create").copied(), Some(false));
assert_eq!(m.value_source("create"), Some(ValueSource::CommandLine));

// finally, we will use the shortcut and only provide the argument without a value.
let m  = cli().get_matches_from(vec![
"prog", "--create"
]);
assert_eq!(m.get_one::<bool>("create").copied(), Some(true));
assert_eq!(m.value_source("create"), Some(ValueSource::CommandLine));
```

[`Arg::action(ArgAction::Set)`]: Arg::action()
[`Arg::default_value`]: Arg::default_value()


**Code Examples:**


```rust
# use clap_builder as clap;
# use clap::{Command, Arg, parser::ValueSource};
fn cli() -> Command {
Command::new("prog")
.arg(Arg::new("color").long("color")
.value_name("WHEN")
.value_parser(["always", "auto", "never"])
.default_value("auto")
.num_args(0..=1)
.require_equals(true)
.default_missing_value("always")
.help("Specify WHEN to colorize output.")
)
}

// first, we'll provide no arguments
let m  = cli().get_matches_from(vec![
"prog"
]);
assert_eq!(m.get_one::<String>("color").unwrap(), "auto");
assert_eq!(m.value_source("color"), Some(ValueSource::DefaultValue));

// next, we'll provide a runtime value to override the default (as usually done).
let m  = cli().get_matches_from(vec![
"prog", "--color=never"
]);
assert_eq!(m.get_one::<String>("color").unwrap(), "never");
assert_eq!(m.value_source("color"), Some(ValueSource::CommandLine));

// finally, we will use the shortcut and only provide the argument without a value.
let m  = cli().get_matches_from(vec![
"prog", "--color"
]);
assert_eq!(m.get_one::<String>("color").unwrap(), "always");
assert_eq!(m.value_source("color"), Some(ValueSource::CommandLine));
```


```rust
# use clap_builder as clap;
# use clap::{Command, Arg, parser::ValueSource, value_parser};
fn cli() -> Command {
Command::new("prog")
.arg(Arg::new("create").long("create")
.value_name("BOOL")
.value_parser(value_parser!(bool))
.num_args(0..=1)
.require_equals(true)
.default_missing_value("true")
)
}

// first, we'll provide no arguments
let m  = cli().get_matches_from(vec![
"prog"
]);
assert_eq!(m.get_one::<bool>("create").copied(), None);

// next, we'll provide a runtime value to override the default (as usually done).
let m  = cli().get_matches_from(vec![
"prog", "--create=false"
]);
assert_eq!(m.get_one::<bool>("create").copied(), Some(false));
assert_eq!(m.value_source("create"), Some(ValueSource::CommandLine));

// finally, we will use the shortcut and only provide the argument without a value.
let m  = cli().get_matches_from(vec![
"prog", "--create"
]);
assert_eq!(m.get_one::<bool>("create").copied(), Some(true));
assert_eq!(m.value_source("create"), Some(ValueSource::CommandLine));
```


#### Fn: `default_missing_value_os` (line 2002)

<!-- Source: repos/clap/clap_builder/src/builder/arg.rs:2002 -->

<!-- Type: fn -->


Value for the argument when the flag is present but no value is specified.

See [`Arg::default_missing_value`].

[`Arg::default_missing_value`]: Arg::default_missing_value()
[`OsStr`]: std::ffi::OsStr


#### Fn: `default_missing_values` (line 2014)

<!-- Source: repos/clap/clap_builder/src/builder/arg.rs:2014 -->

<!-- Type: fn -->


Value for the argument when the flag is present but no value is specified.

See [`Arg::default_missing_value`].

[`Arg::default_missing_value`]: Arg::default_missing_value()


#### Fn: `default_missing_values_os` (line 2025)

<!-- Source: repos/clap/clap_builder/src/builder/arg.rs:2025 -->

<!-- Type: fn -->


Value for the argument when the flag is present but no value is specified.

See [`Arg::default_missing_values`].

[`Arg::default_missing_values`]: Arg::default_missing_values()
[`OsStr`]: std::ffi::OsStr


#### Fn: `env` (line 2041)

<!-- Source: repos/clap/clap_builder/src/builder/arg.rs:2041 -->

<!-- Type: fn -->


Read from `name` environment variable when argument is not present.

If it is not present in the environment, then default
rules will apply.

If user sets the argument in the environment:
- When [`Arg::action(ArgAction::Set)`] is not set, the flag is considered raised.
- When [`Arg::action(ArgAction::Set)`] is set,
[`ArgMatches::get_one`][crate::ArgMatches::get_one] will
return value of the environment variable.

If user doesn't set the argument in the environment:
- When [`Arg::action(ArgAction::Set)`] is not set, the flag is considered off.
- When [`Arg::action(ArgAction::Set)`] is set,
[`ArgMatches::get_one`][crate::ArgMatches::get_one] will
return the default specified.

Like with command-line values, this will be split by [`Arg::value_delimiter`].

# Examples

In this example, we show the variable coming from the environment:

```rust
# use clap_builder as clap;
# use std::env;
# use clap::{Command, Arg, ArgAction};

env::set_var("MY_FLAG", "env");

let m = Command::new("prog")
.arg(Arg::new("flag")
.long("flag")
.env("MY_FLAG")
.action(ArgAction::Set))
.get_matches_from(vec![
"prog"
]);

assert_eq!(m.get_one::<String>("flag").unwrap(), "env");
```

In this example, because `prog` is a flag that accepts an optional, case-insensitive
boolean literal.

Note that the value parser controls how flags are parsed.  In this case we've selected
[`FalseyValueParser`][crate::builder::FalseyValueParser].  A `false` literal is `n`, `no`,
`f`, `false`, `off` or `0`.  An absent environment variable will also be considered as
`false`.  Anything else will considered as `true`.

```rust
# use clap_builder as clap;
# use std::env;
# use clap::{Command, Arg, ArgAction};
# use clap::builder::FalseyValueParser;

env::set_var("TRUE_FLAG", "true");
env::set_var("FALSE_FLAG", "0");

let m = Command::new("prog")
.arg(Arg::new("true_flag")
.long("true_flag")
.action(ArgAction::SetTrue)
.value_parser(FalseyValueParser::new())
.env("TRUE_FLAG"))
.arg(Arg::new("false_flag")
.long("false_flag")
.action(ArgAction::SetTrue)
.value_parser(FalseyValueParser::new())
.env("FALSE_FLAG"))
.arg(Arg::new("absent_flag")
.long("absent_flag")
.action(ArgAction::SetTrue)
.value_parser(FalseyValueParser::new())
.env("ABSENT_FLAG"))
.get_matches_from(vec![
"prog"
]);

assert!(m.get_flag("true_flag"));
assert!(!m.get_flag("false_flag"));
assert!(!m.get_flag("absent_flag"));
```

In this example, we show the variable coming from an option on the CLI:

```rust
# use clap_builder as clap;
# use std::env;
# use clap::{Command, Arg, ArgAction};

env::set_var("MY_FLAG", "env");

let m = Command::new("prog")
.arg(Arg::new("flag")
.long("flag")
.env("MY_FLAG")
.action(ArgAction::Set))
.get_matches_from(vec![
"prog", "--flag", "opt"
]);

assert_eq!(m.get_one::<String>("flag").unwrap(), "opt");
```

In this example, we show the variable coming from the environment even with the
presence of a default:

```rust
# use clap_builder as clap;
# use std::env;
# use clap::{Command, Arg, ArgAction};

env::set_var("MY_FLAG", "env");

let m = Command::new("prog")
.arg(Arg::new("flag")
.long("flag")
.env("MY_FLAG")
.action(ArgAction::Set)
.default_value("default"))
.get_matches_from(vec![
"prog"
]);

assert_eq!(m.get_one::<String>("flag").unwrap(), "env");
```

In this example, we show the use of multiple values in a single environment variable:

```rust
# use clap_builder as clap;
# use std::env;
# use clap::{Command, Arg, ArgAction};

env::set_var("MY_FLAG_MULTI", "env1,env2");

let m = Command::new("prog")
.arg(Arg::new("flag")
.long("flag")
.env("MY_FLAG_MULTI")
.action(ArgAction::Set)
.num_args(1..)
.value_delimiter(','))
.get_matches_from(vec![
"prog"
]);

assert_eq!(m.get_many::<String>("flag").unwrap().collect::<Vec<_>>(), vec!["env1", "env2"]);
```
[`Arg::action(ArgAction::Set)`]: Arg::action()
[`Arg::value_delimiter(',')`]: Arg::value_delimiter()


**Code Examples:**


```rust
# use clap_builder as clap;
# use std::env;
# use clap::{Command, Arg, ArgAction};

env::set_var("MY_FLAG", "env");

let m = Command::new("prog")
.arg(Arg::new("flag")
.long("flag")
.env("MY_FLAG")
.action(ArgAction::Set))
.get_matches_from(vec![
"prog"
]);

assert_eq!(m.get_one::<String>("flag").unwrap(), "env");
```


```rust
# use clap_builder as clap;
# use std::env;
# use clap::{Command, Arg, ArgAction};
# use clap::builder::FalseyValueParser;

env::set_var("TRUE_FLAG", "true");
env::set_var("FALSE_FLAG", "0");

let m = Command::new("prog")
.arg(Arg::new("true_flag")
.long("true_flag")
.action(ArgAction::SetTrue)
.value_parser(FalseyValueParser::new())
.env("TRUE_FLAG"))
.arg(Arg::new("false_flag")
.long("false_flag")
.action(ArgAction::SetTrue)
.value_parser(FalseyValueParser::new())
.env("FALSE_FLAG"))
.arg(Arg::new("absent_flag")
.long("absent_flag")
.action(ArgAction::SetTrue)
.value_parser(FalseyValueParser::new())
.env("ABSENT_FLAG"))
.get_matches_from(vec![
"prog"
]);

assert!(m.get_flag("true_flag"));
assert!(!m.get_flag("false_flag"));
assert!(!m.get_flag("absent_flag"));
```


```rust
# use clap_builder as clap;
# use std::env;
# use clap::{Command, Arg, ArgAction};

env::set_var("MY_FLAG", "env");

let m = Command::new("prog")
.arg(Arg::new("flag")
.long("flag")
.env("MY_FLAG")
.action(ArgAction::Set))
.get_matches_from(vec![
"prog", "--flag", "opt"
]);

assert_eq!(m.get_one::<String>("flag").unwrap(), "opt");
```


```rust
# use clap_builder as clap;
# use std::env;
# use clap::{Command, Arg, ArgAction};

env::set_var("MY_FLAG", "env");

let m = Command::new("prog")
.arg(Arg::new("flag")
.long("flag")
.env("MY_FLAG")
.action(ArgAction::Set)
.default_value("default"))
.get_matches_from(vec![
"prog"
]);

assert_eq!(m.get_one::<String>("flag").unwrap(), "env");
```


```rust
# use clap_builder as clap;
# use std::env;
# use clap::{Command, Arg, ArgAction};

env::set_var("MY_FLAG_MULTI", "env1,env2");

let m = Command::new("prog")
.arg(Arg::new("flag")
.long("flag")
.env("MY_FLAG_MULTI")
.action(ArgAction::Set)
.num_args(1..)
.value_delimiter(','))
.get_matches_from(vec![
"prog"
]);

assert_eq!(m.get_many::<String>("flag").unwrap().collect::<Vec<_>>(), vec!["env1", "env2"]);
```


#### Impl: `Arg` (line 2217)

<!-- Source: repos/clap/clap_builder/src/builder/arg.rs:2217 -->

<!-- Type: impl -->


# Help


#### Fn: `help` (line 2219)

<!-- Source: repos/clap/clap_builder/src/builder/arg.rs:2219 -->

<!-- Type: fn -->


Sets the description of the argument for short help (`-h`).

Typically, this is a short (one line) description of the arg.

If [`Arg::long_help`] is not specified, this message will be displayed for `--help`.

<div class="warning">

**NOTE:** Only `Arg::help` is used in completion script generation in order to be concise

</div>

# Examples

Any valid UTF-8 is allowed in the help text. The one exception is when one wishes to
include a newline in the help text and have the following text be properly aligned with all
the other help text.

Setting `help` displays a short message to the side of the argument when the user passes
`-h` or `--help` (by default).

```rust
# #[cfg(feature = "help")] {
# use clap_builder as clap;
# use clap::{Command, Arg};
let m = Command::new("prog")
.arg(Arg::new("cfg")
.long("config")
.help("Some help text describing the --config arg"))
.get_matches_from(vec![
"prog", "--help"
]);
# }
```

The above example displays

```notrust
helptest

Usage: helptest [OPTIONS]

Options:
--config     Some help text describing the --config arg
-h, --help       Print help information
-V, --version    Print version information
```
[`Arg::long_help`]: Arg::long_help()


**Code Examples:**


```rust
# #[cfg(feature = "help")] {
# use clap_builder as clap;
# use clap::{Command, Arg};
let m = Command::new("prog")
.arg(Arg::new("cfg")
.long("config")
.help("Some help text describing the --config arg"))
.get_matches_from(vec![
"prog", "--help"
]);
# }
```


#### Fn: `long_help` (line 2274)

<!-- Source: repos/clap/clap_builder/src/builder/arg.rs:2274 -->

<!-- Type: fn -->


Sets the description of the argument for long help (`--help`).

Typically this a more detailed (multi-line) message
that describes the arg.

If [`Arg::help`] is not specified, this message will be displayed for `-h`.

<div class="warning">

**NOTE:** Only [`Arg::help`] is used in completion script generation in order to be concise

</div>

# Examples

Any valid UTF-8 is allowed in the help text. The one exception is when one wishes to
include a newline in the help text and have the following text be properly aligned with all
the other help text.

Setting `help` displays a short message to the side of the argument when the user passes
`-h` or `--help` (by default).

```rust
# #[cfg(feature = "help")] {
# use clap_builder as clap;
# use clap::{Command, Arg};
let m = Command::new("prog")
.arg(Arg::new("cfg")
.long("config")
.long_help(
"The config file used by the myprog must be in JSON format
with only valid keys and may not contain other nonsense
that cannot be read by this program. Obviously I'm going on
and on, so I'll stop now."))
.get_matches_from(vec![
"prog", "--help"
]);
# }
```

The above example displays

```text
prog

Usage: prog [OPTIONS]

Options:
--config
The config file used by the myprog must be in JSON format
with only valid keys and may not contain other nonsense
that cannot be read by this program. Obviously I'm going on
and on, so I'll stop now.

-h, --help
Print help information

-V, --version
Print version information
```
[`Arg::help`]: Arg::help()


**Code Examples:**


```rust
# #[cfg(feature = "help")] {
# use clap_builder as clap;
# use clap::{Command, Arg};
let m = Command::new("prog")
.arg(Arg::new("cfg")
.long("config")
.long_help(
"The config file used by the myprog must be in JSON format
with only valid keys and may not contain other nonsense
that cannot be read by this program. Obviously I'm going on
and on, so I'll stop now."))
.get_matches_from(vec![
"prog", "--help"
]);
# }
```


#### Fn: `display_order` (line 2342)

<!-- Source: repos/clap/clap_builder/src/builder/arg.rs:2342 -->

<!-- Type: fn -->


Allows custom ordering of args within the help message.

`Arg`s with a lower value will be displayed first in the help message.
Those with the same display order will be sorted.

`Arg`s are automatically assigned a display order based on the order they are added to the
[`Command`][crate::Command].
Overriding this is helpful when the order arguments are added in isn't the same as the
display order, whether in one-off cases or to automatically sort arguments.

To change, see [`Command::next_display_order`][crate::Command::next_display_order].

<div class="warning">

**NOTE:** This setting is ignored for [positional arguments] which are always displayed in
[index] order.

</div>

# Examples

```rust
# #[cfg(feature = "help")] {
# use clap_builder as clap;
# use clap::{Command, Arg, ArgAction};
let m = Command::new("prog")
.arg(Arg::new("boat")
.short('b')
.long("boat")
.action(ArgAction::Set)
.display_order(0)  // Sort
.help("Some help and text"))
.arg(Arg::new("airplane")
.short('a')
.long("airplane")
.action(ArgAction::Set)
.display_order(0)  // Sort
.help("I should be first!"))
.arg(Arg::new("custom-help")
.short('?')
.action(ArgAction::Help)
.display_order(100)  // Don't sort
.help("Alt help"))
.get_matches_from(vec![
"prog", "--help"
]);
# }
```

The above example displays the following help message

```text
cust-ord

Usage: cust-ord [OPTIONS]

Options:
-a, --airplane <airplane>    I should be first!
-b, --boat <boar>            Some help and text
-h, --help                   Print help information
-?                           Alt help
```
[positional arguments]: Arg::index()
[index]: Arg::index()


**Code Examples:**


```rust
# #[cfg(feature = "help")] {
# use clap_builder as clap;
# use clap::{Command, Arg, ArgAction};
let m = Command::new("prog")
.arg(Arg::new("boat")
.short('b')
.long("boat")
.action(ArgAction::Set)
.display_order(0)  // Sort
.help("Some help and text"))
.arg(Arg::new("airplane")
.short('a')
.long("airplane")
.action(ArgAction::Set)
.display_order(0)  // Sort
.help("I should be first!"))
.arg(Arg::new("custom-help")
.short('?')
.action(ArgAction::Help)
.display_order(100)  // Don't sort
.help("Alt help"))
.get_matches_from(vec![
"prog", "--help"
]);
# }
```


#### Fn: `help_heading` (line 2413)

<!-- Source: repos/clap/clap_builder/src/builder/arg.rs:2413 -->

<!-- Type: fn -->


Override the `--help` section this appears in.

For more on the default help heading, see
[`Command::next_help_heading`][crate::Command::next_help_heading].


#### Fn: `next_line_help` (line 2424)

<!-- Source: repos/clap/clap_builder/src/builder/arg.rs:2424 -->

<!-- Type: fn -->


Render the [help][Arg::help] on the line after the argument.

This can be helpful for arguments with very long or complex help messages.
This can also be helpful for arguments with very long flag names, or many/long value names.

<div class="warning">

**NOTE:** To apply this setting to all arguments and subcommands, consider using
[`crate::Command::next_line_help`]

</div>

# Examples

```rust
# #[cfg(feature = "help")] {
# use clap_builder as clap;
# use clap::{Command, Arg, ArgAction};
let m = Command::new("prog")
.arg(Arg::new("opt")
.long("long-option-flag")
.short('o')
.action(ArgAction::Set)
.next_line_help(true)
.value_names(["value1", "value2"])
.help("Some really long help and complex\n\
help that makes more sense to be\n\
on a line after the option"))
.get_matches_from(vec![
"prog", "--help"
]);
# }
```

The above example displays the following help message

```text
nlh

Usage: nlh [OPTIONS]

Options:
-h, --help       Print help information
-V, --version    Print version information
-o, --long-option-flag <value1> <value2>
Some really long help and complex
help that makes more sense to be
on a line after the option
```


**Code Examples:**


```rust
# #[cfg(feature = "help")] {
# use clap_builder as clap;
# use clap::{Command, Arg, ArgAction};
let m = Command::new("prog")
.arg(Arg::new("opt")
.long("long-option-flag")
.short('o')
.action(ArgAction::Set)
.next_line_help(true)
.value_names(["value1", "value2"])
.help("Some really long help and complex\n\
help that makes more sense to be\n\
on a line after the option"))
.get_matches_from(vec![
"prog", "--help"
]);
# }
```


#### Fn: `hide` (line 2483)

<!-- Source: repos/clap/clap_builder/src/builder/arg.rs:2483 -->

<!-- Type: fn -->


Do not display the argument in help message.

<div class="warning">

**NOTE:** This does **not** hide the argument from usage strings on error

</div>

# Examples

Setting `Hidden` will hide the argument when displaying help text

```rust
# #[cfg(feature = "help")] {
# use clap_builder as clap;
# use clap::{Command, Arg};
let m = Command::new("prog")
.arg(Arg::new("cfg")
.long("config")
.hide(true)
.help("Some help text describing the --config arg"))
.get_matches_from(vec![
"prog", "--help"
]);
# }
```

The above example displays

```text
helptest

Usage: helptest [OPTIONS]

Options:
-h, --help       Print help information
-V, --version    Print version information
```


**Code Examples:**


```rust
# #[cfg(feature = "help")] {
# use clap_builder as clap;
# use clap::{Command, Arg};
let m = Command::new("prog")
.arg(Arg::new("cfg")
.long("config")
.hide(true)
.help("Some help text describing the --config arg"))
.get_matches_from(vec![
"prog", "--help"
]);
# }
```


#### Fn: `hide_possible_values` (line 2531)

<!-- Source: repos/clap/clap_builder/src/builder/arg.rs:2531 -->

<!-- Type: fn -->


Do not display the [possible values][crate::builder::ValueParser::possible_values] in the help message.

This is useful for args with many values, or ones which are explained elsewhere in the
help text.

To set this for all arguments, see
[`Command::hide_possible_values`][crate::Command::hide_possible_values].

<div class="warning">

**NOTE:** Setting this requires [taking values][Arg::num_args]

</div>

# Examples

```rust
# use clap_builder as clap;
# use clap::{Command, Arg, ArgAction};
let m = Command::new("prog")
.arg(Arg::new("mode")
.long("mode")
.value_parser(["fast", "slow"])
.action(ArgAction::Set)
.hide_possible_values(true));
```
If we were to run the above program with `--help` the `[values: fast, slow]` portion of
the help text would be omitted.


**Code Examples:**


```rust
# use clap_builder as clap;
# use clap::{Command, Arg, ArgAction};
let m = Command::new("prog")
.arg(Arg::new("mode")
.long("mode")
.value_parser(["fast", "slow"])
.action(ArgAction::Set)
.hide_possible_values(true));
```


#### Fn: `hide_default_value` (line 2569)

<!-- Source: repos/clap/clap_builder/src/builder/arg.rs:2569 -->

<!-- Type: fn -->


Do not display the default value of the argument in the help message.

This is useful when default behavior of an arg is explained elsewhere in the help text.

<div class="warning">

**NOTE:** Setting this requires [taking values][Arg::num_args]

</div>

# Examples

```rust
# use clap_builder as clap;
# use clap::{Command, Arg, ArgAction};
let m = Command::new("connect")
.arg(Arg::new("host")
.long("host")
.default_value("localhost")
.action(ArgAction::Set)
.hide_default_value(true));

```

If we were to run the above program with `--help` the `[default: localhost]` portion of
the help text would be omitted.


**Code Examples:**


```rust
# use clap_builder as clap;
# use clap::{Command, Arg, ArgAction};
let m = Command::new("connect")
.arg(Arg::new("host")
.long("host")
.default_value("localhost")
.action(ArgAction::Set)
.hide_default_value(true));
```


#### Fn: `hide_env` (line 2605)

<!-- Source: repos/clap/clap_builder/src/builder/arg.rs:2605 -->

<!-- Type: fn -->


Do not display in help the environment variable name.

This is useful when the variable option is explained elsewhere in the help text.

# Examples

```rust
# use clap_builder as clap;
# use clap::{Command, Arg, ArgAction};
let m = Command::new("prog")
.arg(Arg::new("mode")
.long("mode")
.env("MODE")
.action(ArgAction::Set)
.hide_env(true));
```

If we were to run the above program with `--help` the `[env: MODE]` portion of the help
text would be omitted.


**Code Examples:**


```rust
# use clap_builder as clap;
# use clap::{Command, Arg, ArgAction};
let m = Command::new("prog")
.arg(Arg::new("mode")
.long("mode")
.env("MODE")
.action(ArgAction::Set)
.hide_env(true));
```


#### Fn: `hide_env_values` (line 2635)

<!-- Source: repos/clap/clap_builder/src/builder/arg.rs:2635 -->

<!-- Type: fn -->


Do not display in help any values inside the associated ENV variables for the argument.

This is useful when ENV vars contain sensitive values.

# Examples

```rust
# use clap_builder as clap;
# use clap::{Command, Arg, ArgAction};
let m = Command::new("connect")
.arg(Arg::new("host")
.long("host")
.env("CONNECT")
.action(ArgAction::Set)
.hide_env_values(true));

```

If we were to run the above program with `$ CONNECT=super_secret connect --help` the
`[default: CONNECT=super_secret]` portion of the help text would be omitted.


**Code Examples:**


```rust
# use clap_builder as clap;
# use clap::{Command, Arg, ArgAction};
let m = Command::new("connect")
.arg(Arg::new("host")
.long("host")
.env("CONNECT")
.action(ArgAction::Set)
.hide_env_values(true));
```


#### Fn: `hide_short_help` (line 2666)

<!-- Source: repos/clap/clap_builder/src/builder/arg.rs:2666 -->

<!-- Type: fn -->


Hides an argument from short help (`-h`).

<div class="warning">

**NOTE:** This does **not** hide the argument from usage strings on error

</div>

<div class="warning">

**NOTE:** Setting this option will cause next-line-help output style to be used
when long help (`--help`) is called.

</div>

# Examples

```rust
# use clap_builder as clap;
# use clap::{Command, Arg};
Arg::new("debug")
.hide_short_help(true);
```

Setting `hide_short_help(true)` will hide the argument when displaying short help text

```rust
# #[cfg(feature = "help")] {
# use clap_builder as clap;
# use clap::{Command, Arg};
let m = Command::new("prog")
.arg(Arg::new("cfg")
.long("config")
.hide_short_help(true)
.help("Some help text describing the --config arg"))
.get_matches_from(vec![
"prog", "-h"
]);
# }
```

The above example displays

```text
helptest

Usage: helptest [OPTIONS]

Options:
-h, --help       Print help information
-V, --version    Print version information
```

However, when --help is called

```rust
# #[cfg(feature = "help")] {
# use clap_builder as clap;
# use clap::{Command, Arg};
let m = Command::new("prog")
.arg(Arg::new("cfg")
.long("config")
.hide_short_help(true)
.help("Some help text describing the --config arg"))
.get_matches_from(vec![
"prog", "--help"
]);
# }
```

Then the following would be displayed

```text
helptest

Usage: helptest [OPTIONS]

Options:
--config     Some help text describing the --config arg
-h, --help       Print help information
-V, --version    Print version information
```


**Code Examples:**


```rust
# use clap_builder as clap;
# use clap::{Command, Arg};
Arg::new("debug")
.hide_short_help(true);
```


```rust
# #[cfg(feature = "help")] {
# use clap_builder as clap;
# use clap::{Command, Arg};
let m = Command::new("prog")
.arg(Arg::new("cfg")
.long("config")
.hide_short_help(true)
.help("Some help text describing the --config arg"))
.get_matches_from(vec![
"prog", "-h"
]);
# }
```


```rust
However, when --help is called
```


```rust
Then the following would be displayed
```


#### Fn: `hide_long_help` (line 2758)

<!-- Source: repos/clap/clap_builder/src/builder/arg.rs:2758 -->

<!-- Type: fn -->


Hides an argument from long help (`--help`).

<div class="warning">

**NOTE:** This does **not** hide the argument from usage strings on error

</div>

<div class="warning">

**NOTE:** Setting this option will cause next-line-help output style to be used
when long help (`--help`) is called.

</div>

# Examples

Setting `hide_long_help(true)` will hide the argument when displaying long help text

```rust
# #[cfg(feature = "help")] {
# use clap_builder as clap;
# use clap::{Command, Arg};
let m = Command::new("prog")
.arg(Arg::new("cfg")
.long("config")
.hide_long_help(true)
.help("Some help text describing the --config arg"))
.get_matches_from(vec![
"prog", "--help"
]);
# }
```

The above example displays

```text
helptest

Usage: helptest [OPTIONS]

Options:
-h, --help       Print help information
-V, --version    Print version information
```

However, when -h is called

```rust
# #[cfg(feature = "help")] {
# use clap_builder as clap;
# use clap::{Command, Arg};
let m = Command::new("prog")
.arg(Arg::new("cfg")
.long("config")
.hide_long_help(true)
.help("Some help text describing the --config arg"))
.get_matches_from(vec![
"prog", "-h"
]);
# }
```

Then the following would be displayed

```text
helptest

Usage: helptest [OPTIONS]

OPTIONS:
--config     Some help text describing the --config arg
-h, --help       Print help information
-V, --version    Print version information
```


**Code Examples:**


```rust
# #[cfg(feature = "help")] {
# use clap_builder as clap;
# use clap::{Command, Arg};
let m = Command::new("prog")
.arg(Arg::new("cfg")
.long("config")
.hide_long_help(true)
.help("Some help text describing the --config arg"))
.get_matches_from(vec![
"prog", "--help"
]);
# }
```


```rust
However, when -h is called
```


```rust
Then the following would be displayed
```


#### Impl: `Arg` (line 2844)

<!-- Source: repos/clap/clap_builder/src/builder/arg.rs:2844 -->

<!-- Type: impl -->


# Advanced Argument Relations


#### Fn: `group` (line 2846)

<!-- Source: repos/clap/clap_builder/src/builder/arg.rs:2846 -->

<!-- Type: fn -->


The name of the [`ArgGroup`] the argument belongs to.

# Examples

```rust
# use clap_builder as clap;
# use clap::{Command, Arg, ArgAction};
Arg::new("debug")
.long("debug")
.action(ArgAction::SetTrue)
.group("mode")
# ;
```

Multiple arguments can be a member of a single group and then the group checked as if it
was one of said arguments.

```rust
# use clap_builder as clap;
# use clap::{Command, Arg, ArgAction};
let m = Command::new("prog")
.arg(Arg::new("debug")
.long("debug")
.action(ArgAction::SetTrue)
.group("mode"))
.arg(Arg::new("verbose")
.long("verbose")
.action(ArgAction::SetTrue)
.group("mode"))
.get_matches_from(vec![
"prog", "--debug"
]);
assert!(m.contains_id("mode"));
```

[`ArgGroup`]: crate::ArgGroup


**Code Examples:**


```rust
# use clap_builder as clap;
# use clap::{Command, Arg, ArgAction};
Arg::new("debug")
.long("debug")
.action(ArgAction::SetTrue)
.group("mode")
# ;
```


```rust
# use clap_builder as clap;
# use clap::{Command, Arg, ArgAction};
let m = Command::new("prog")
.arg(Arg::new("debug")
.long("debug")
.action(ArgAction::SetTrue)
.group("mode"))
.arg(Arg::new("verbose")
.long("verbose")
.action(ArgAction::SetTrue)
.group("mode"))
.get_matches_from(vec![
"prog", "--debug"
]);
assert!(m.contains_id("mode"));
```


#### Fn: `groups` (line 2892)

<!-- Source: repos/clap/clap_builder/src/builder/arg.rs:2892 -->

<!-- Type: fn -->


The names of [`ArgGroup`]'s the argument belongs to.

# Examples

```rust
# use clap_builder as clap;
# use clap::{Command, Arg, ArgAction};
Arg::new("debug")
.long("debug")
.action(ArgAction::SetTrue)
.groups(["mode", "verbosity"])
# ;
```

Arguments can be members of multiple groups and then the group checked as if it
was one of said arguments.

```rust
# use clap_builder as clap;
# use clap::{Command, Arg, ArgAction};
let m = Command::new("prog")
.arg(Arg::new("debug")
.long("debug")
.action(ArgAction::SetTrue)
.groups(["mode", "verbosity"]))
.arg(Arg::new("verbose")
.long("verbose")
.action(ArgAction::SetTrue)
.groups(["mode", "verbosity"]))
.get_matches_from(vec![
"prog", "--debug"
]);
assert!(m.contains_id("mode"));
assert!(m.contains_id("verbosity"));
```

[`ArgGroup`]: crate::ArgGroup


**Code Examples:**


```rust
# use clap_builder as clap;
# use clap::{Command, Arg, ArgAction};
Arg::new("debug")
.long("debug")
.action(ArgAction::SetTrue)
.groups(["mode", "verbosity"])
# ;
```


```rust
# use clap_builder as clap;
# use clap::{Command, Arg, ArgAction};
let m = Command::new("prog")
.arg(Arg::new("debug")
.long("debug")
.action(ArgAction::SetTrue)
.groups(["mode", "verbosity"]))
.arg(Arg::new("verbose")
.long("verbose")
.action(ArgAction::SetTrue)
.groups(["mode", "verbosity"]))
.get_matches_from(vec![
"prog", "--debug"
]);
assert!(m.contains_id("mode"));
assert!(m.contains_id("verbosity"));
```


#### Fn: `default_value_if` (line 2935)

<!-- Source: repos/clap/clap_builder/src/builder/arg.rs:2935 -->

<!-- Type: fn -->


Specifies the value of the argument if `arg` has been used at runtime.

If `default` is set to `None`, `default_value` will be removed.

Like with command-line values, this will be split by [`Arg::value_delimiter`].

<div class="warning">

**NOTE:** This setting is perfectly compatible with [`Arg::default_value`] but slightly
different. `Arg::default_value` *only* takes effect when the user has not provided this arg
at runtime. This setting however only takes effect when the user has not provided a value at
runtime **and** these other conditions are met as well. If you have set `Arg::default_value`
and `Arg::default_value_if`, and the user **did not** provide this arg at runtime, nor were
the conditions met for `Arg::default_value_if`, the `Arg::default_value` will be applied.

</div>

# Examples

First we use the default value only if another arg is present at runtime.

```rust
# use clap_builder as clap;
# use clap::{Command, Arg, ArgAction};
# use clap::builder::{ArgPredicate};
let m = Command::new("prog")
.arg(Arg::new("flag")
.long("flag")
.action(ArgAction::SetTrue))
.arg(Arg::new("other")
.long("other")
.default_value_if("flag", ArgPredicate::IsPresent, Some("default")))
.get_matches_from(vec![
"prog", "--flag"
]);

assert_eq!(m.get_one::<String>("other").unwrap(), "default");
```

Next we run the same test, but without providing `--flag`.

```rust
# use clap_builder as clap;
# use clap::{Command, Arg, ArgAction};
let m = Command::new("prog")
.arg(Arg::new("flag")
.long("flag")
.action(ArgAction::SetTrue))
.arg(Arg::new("other")
.long("other")
.default_value_if("flag", "true", Some("default")))
.get_matches_from(vec![
"prog"
]);

assert_eq!(m.get_one::<String>("other"), None);
```

Now lets only use the default value if `--opt` contains the value `special`.

```rust
# use clap_builder as clap;
# use clap::{Command, Arg, ArgAction};
let m = Command::new("prog")
.arg(Arg::new("opt")
.action(ArgAction::Set)
.long("opt"))
.arg(Arg::new("other")
.long("other")
.default_value_if("opt", "special", Some("default")))
.get_matches_from(vec![
"prog", "--opt", "special"
]);

assert_eq!(m.get_one::<String>("other").unwrap(), "default");
```

We can run the same test and provide any value *other than* `special` and we won't get a
default value.

```rust
# use clap_builder as clap;
# use clap::{Command, Arg, ArgAction};
let m = Command::new("prog")
.arg(Arg::new("opt")
.action(ArgAction::Set)
.long("opt"))
.arg(Arg::new("other")
.long("other")
.default_value_if("opt", "special", Some("default")))
.get_matches_from(vec![
"prog", "--opt", "hahaha"
]);

assert_eq!(m.get_one::<String>("other"), None);
```

If we want to unset the default value for an Arg based on the presence or
value of some other Arg.

```rust
# use clap_builder as clap;
# use clap::{Command, Arg, ArgAction};
let m = Command::new("prog")
.arg(Arg::new("flag")
.long("flag")
.action(ArgAction::SetTrue))
.arg(Arg::new("other")
.long("other")
.default_value("default")
.default_value_if("flag", "true", None))
.get_matches_from(vec![
"prog", "--flag"
]);

assert_eq!(m.get_one::<String>("other"), None);
```
[`Arg::action(ArgAction::Set)`]: Arg::action()
[`Arg::default_value`]: Arg::default_value()


**Code Examples:**


```rust
# use clap_builder as clap;
# use clap::{Command, Arg, ArgAction};
# use clap::builder::{ArgPredicate};
let m = Command::new("prog")
.arg(Arg::new("flag")
.long("flag")
.action(ArgAction::SetTrue))
.arg(Arg::new("other")
.long("other")
.default_value_if("flag", ArgPredicate::IsPresent, Some("default")))
.get_matches_from(vec![
"prog", "--flag"
]);

assert_eq!(m.get_one::<String>("other").unwrap(), "default");
```


```rust
# use clap_builder as clap;
# use clap::{Command, Arg, ArgAction};
let m = Command::new("prog")
.arg(Arg::new("flag")
.long("flag")
.action(ArgAction::SetTrue))
.arg(Arg::new("other")
.long("other")
.default_value_if("flag", "true", Some("default")))
.get_matches_from(vec![
"prog"
]);

assert_eq!(m.get_one::<String>("other"), None);
```


```rust
# use clap_builder as clap;
# use clap::{Command, Arg, ArgAction};
let m = Command::new("prog")
.arg(Arg::new("opt")
.action(ArgAction::Set)
.long("opt"))
.arg(Arg::new("other")
.long("other")
.default_value_if("opt", "special", Some("default")))
.get_matches_from(vec![
"prog", "--opt", "special"
]);

assert_eq!(m.get_one::<String>("other").unwrap(), "default");
```


```rust
# use clap_builder as clap;
# use clap::{Command, Arg, ArgAction};
let m = Command::new("prog")
.arg(Arg::new("opt")
.action(ArgAction::Set)
.long("opt"))
.arg(Arg::new("other")
.long("other")
.default_value_if("opt", "special", Some("default")))
.get_matches_from(vec![
"prog", "--opt", "hahaha"
]);

assert_eq!(m.get_one::<String>("other"), None);
```


```rust
# use clap_builder as clap;
# use clap::{Command, Arg, ArgAction};
let m = Command::new("prog")
.arg(Arg::new("flag")
.long("flag")
.action(ArgAction::SetTrue))
.arg(Arg::new("other")
.long("other")
.default_value("default")
.default_value_if("flag", "true", None))
.get_matches_from(vec![
"prog", "--flag"
]);

assert_eq!(m.get_one::<String>("other"), None);
```


#### Fn: `default_values_if` (line 3072)

<!-- Source: repos/clap/clap_builder/src/builder/arg.rs:3072 -->

<!-- Type: fn -->


Specifies the values of the argument if `arg` has been used at runtime.

See [`Arg::default_value_if`].

# Examples

```rust
use clap_builder::arg;
use clap_builder::Command;
use clap_builder::Arg;
let r = Command::new("df")
.arg(arg!(--opt <FILE> "some arg"))
.arg(
Arg::new("args")
.long("args")
.num_args(2)
.default_values_if("opt", "value", ["df1","df2"]),
)
.try_get_matches_from(vec!["", "--opt", "value"]);

let m = r.unwrap();
assert_eq!(
m.get_many::<String>("args").unwrap().collect::<Vec<_>>(),
["df1", "df2"]
);
```

[`Arg::default_value_if`]: Arg::default_value_if()


**Code Examples:**


```rust
use clap_builder::arg;
use clap_builder::Command;
use clap_builder::Arg;
let r = Command::new("df")
.arg(arg!(--opt <FILE> "some arg"))
.arg(
Arg::new("args")
.long("args")
.num_args(2)
.default_values_if("opt", "value", ["df1","df2"]),
)
.try_get_matches_from(vec!["", "--opt", "value"]);

let m = r.unwrap();
assert_eq!(
m.get_many::<String>("args").unwrap().collect::<Vec<_>>(),
["df1", "df2"]
);
```


#### Fn: `default_value_ifs` (line 3130)

<!-- Source: repos/clap/clap_builder/src/builder/arg.rs:3130 -->

<!-- Type: fn -->


Specifies multiple values and conditions in the same manner as [`Arg::default_value_if`].

The method takes a slice of tuples in the `(arg, predicate, default)` format.

Like with command-line values, this will be split by [`Arg::value_delimiter`].

<div class="warning">

**NOTE**: The conditions are stored in order and evaluated in the same order. I.e. the first
if multiple conditions are true, the first one found will be applied and the ultimate value.

</div>

# Examples

First we use the default value only if another arg is present at runtime.

```rust
# use clap_builder as clap;
# use clap::{Command, Arg, ArgAction};
let m = Command::new("prog")
.arg(Arg::new("flag")
.long("flag")
.action(ArgAction::SetTrue))
.arg(Arg::new("opt")
.long("opt")
.action(ArgAction::Set))
.arg(Arg::new("other")
.long("other")
.default_value_ifs([
("flag", "true", Some("default")),
("opt", "channal", Some("chan")),
]))
.get_matches_from(vec![
"prog", "--opt", "channal"
]);

assert_eq!(m.get_one::<String>("other").unwrap(), "chan");
```

Next we run the same test, but without providing `--flag`.

```rust
# use clap_builder as clap;
# use clap::{Command, Arg, ArgAction};
let m = Command::new("prog")
.arg(Arg::new("flag")
.long("flag")
.action(ArgAction::SetTrue))
.arg(Arg::new("other")
.long("other")
.default_value_ifs([
("flag", "true", Some("default")),
("opt", "channal", Some("chan")),
]))
.get_matches_from(vec![
"prog"
]);

assert_eq!(m.get_one::<String>("other"), None);
```

We can also see that these values are applied in order, and if more than one condition is
true, only the first evaluated "wins"

```rust
# use clap_builder as clap;
# use clap::{Command, Arg, ArgAction};
# use clap::builder::ArgPredicate;
let m = Command::new("prog")
.arg(Arg::new("flag")
.long("flag")
.action(ArgAction::SetTrue))
.arg(Arg::new("opt")
.long("opt")
.action(ArgAction::Set))
.arg(Arg::new("other")
.long("other")
.default_value_ifs([
("flag", ArgPredicate::IsPresent, Some("default")),
("opt", ArgPredicate::Equals("channal".into()), Some("chan")),
]))
.get_matches_from(vec![
"prog", "--opt", "channal", "--flag"
]);

assert_eq!(m.get_one::<String>("other").unwrap(), "default");
```
[`Arg::action(ArgAction::Set)`]: Arg::action()
[`Arg::default_value_if`]: Arg::default_value_if()


**Code Examples:**


```rust
# use clap_builder as clap;
# use clap::{Command, Arg, ArgAction};
let m = Command::new("prog")
.arg(Arg::new("flag")
.long("flag")
.action(ArgAction::SetTrue))
.arg(Arg::new("opt")
.long("opt")
.action(ArgAction::Set))
.arg(Arg::new("other")
.long("other")
.default_value_ifs([
("flag", "true", Some("default")),
("opt", "channal", Some("chan")),
]))
.get_matches_from(vec![
"prog", "--opt", "channal"
]);

assert_eq!(m.get_one::<String>("other").unwrap(), "chan");
```


```rust
# use clap_builder as clap;
# use clap::{Command, Arg, ArgAction};
let m = Command::new("prog")
.arg(Arg::new("flag")
.long("flag")
.action(ArgAction::SetTrue))
.arg(Arg::new("other")
.long("other")
.default_value_ifs([
("flag", "true", Some("default")),
("opt", "channal", Some("chan")),
]))
.get_matches_from(vec![
"prog"
]);

assert_eq!(m.get_one::<String>("other"), None);
```


```rust
# use clap_builder as clap;
# use clap::{Command, Arg, ArgAction};
# use clap::builder::ArgPredicate;
let m = Command::new("prog")
.arg(Arg::new("flag")
.long("flag")
.action(ArgAction::SetTrue))
.arg(Arg::new("opt")
.long("opt")
.action(ArgAction::Set))
.arg(Arg::new("other")
.long("other")
.default_value_ifs([
("flag", ArgPredicate::IsPresent, Some("default")),
("opt", ArgPredicate::Equals("channal".into()), Some("chan")),
]))
.get_matches_from(vec![
"prog", "--opt", "channal", "--flag"
]);

assert_eq!(m.get_one::<String>("other").unwrap(), "default");
```


#### Fn: `default_values_ifs` (line 3237)

<!-- Source: repos/clap/clap_builder/src/builder/arg.rs:3237 -->

<!-- Type: fn -->


Specifies multiple values and conditions in the same manner as [`Arg::default_values_if`].

See [`Arg::default_values_if`].

[`Arg::default_values_if`]: Arg::default_values_if()


#### Fn: `required_unless_present` (line 3278)

<!-- Source: repos/clap/clap_builder/src/builder/arg.rs:3278 -->

<!-- Type: fn -->


Set this arg as [required] as long as the specified argument is not present at runtime.

<div class="warning">

**TIP:** Using `Arg::required_unless_present` implies [`Arg::required`] and is therefore not
mandatory to also set.

</div>

# Examples

```rust
# use clap_builder as clap;
# use clap::Arg;
Arg::new("config")
.required_unless_present("debug")
# ;
```

In the following example, the required argument is *not* provided,
but it's not an error because the `unless` arg has been supplied.

```rust
# use clap_builder as clap;
# use clap::{Command, Arg, ArgAction};
let res = Command::new("prog")
.arg(Arg::new("cfg")
.required_unless_present("dbg")
.action(ArgAction::Set)
.long("config"))
.arg(Arg::new("dbg")
.long("debug")
.action(ArgAction::SetTrue))
.try_get_matches_from(vec![
"prog", "--debug"
]);

assert!(res.is_ok());
```

Setting `Arg::required_unless_present(name)` and *not* supplying `name` or this arg is an error.

```rust
# use clap_builder as clap;
# use clap::{Command, Arg, error::ErrorKind, ArgAction};
let res = Command::new("prog")
.arg(Arg::new("cfg")
.required_unless_present("dbg")
.action(ArgAction::Set)
.long("config"))
.arg(Arg::new("dbg")
.long("debug"))
.try_get_matches_from(vec![
"prog"
]);

assert!(res.is_err());
assert_eq!(res.unwrap_err().kind(), ErrorKind::MissingRequiredArgument);
```
[required]: Arg::required()


**Code Examples:**


```rust
# use clap_builder as clap;
# use clap::Arg;
Arg::new("config")
.required_unless_present("debug")
# ;
```


```rust
# use clap_builder as clap;
# use clap::{Command, Arg, ArgAction};
let res = Command::new("prog")
.arg(Arg::new("cfg")
.required_unless_present("dbg")
.action(ArgAction::Set)
.long("config"))
.arg(Arg::new("dbg")
.long("debug")
.action(ArgAction::SetTrue))
.try_get_matches_from(vec![
"prog", "--debug"
]);

assert!(res.is_ok());
```


```rust
# use clap_builder as clap;
# use clap::{Command, Arg, error::ErrorKind, ArgAction};
let res = Command::new("prog")
.arg(Arg::new("cfg")
.required_unless_present("dbg")
.action(ArgAction::Set)
.long("config"))
.arg(Arg::new("dbg")
.long("debug"))
.try_get_matches_from(vec![
"prog"
]);

assert!(res.is_err());
assert_eq!(res.unwrap_err().kind(), ErrorKind::MissingRequiredArgument);
```


#### Fn: `required_unless_present_all` (line 3348)

<!-- Source: repos/clap/clap_builder/src/builder/arg.rs:3348 -->

<!-- Type: fn -->


Sets this arg as [required] unless *all* of the specified arguments are present at runtime.

In other words, parsing will succeed only if user either
* supplies the `self` arg.
* supplies *all* of the `names` arguments.

<div class="warning">

**NOTE:** If you wish for this argument to only be required unless *any of* these args are
present see [`Arg::required_unless_present_any`]

</div>

# Examples

```rust
# use clap_builder as clap;
# use clap::Arg;
Arg::new("config")
.required_unless_present_all(["cfg", "dbg"])
# ;
```

In the following example, the required argument is *not* provided, but it's not an error
because *all* of the `names` args have been supplied.

```rust
# use clap_builder as clap;
# use clap::{Command, Arg, ArgAction};
let res = Command::new("prog")
.arg(Arg::new("cfg")
.required_unless_present_all(["dbg", "infile"])
.action(ArgAction::Set)
.long("config"))
.arg(Arg::new("dbg")
.long("debug")
.action(ArgAction::SetTrue))
.arg(Arg::new("infile")
.short('i')
.action(ArgAction::Set))
.try_get_matches_from(vec![
"prog", "--debug", "-i", "file"
]);

assert!(res.is_ok());
```

Setting [`Arg::required_unless_present_all(names)`] and *not* supplying
either *all* of `unless` args or the `self` arg is an error.

```rust
# use clap_builder as clap;
# use clap::{Command, Arg, error::ErrorKind, ArgAction};
let res = Command::new("prog")
.arg(Arg::new("cfg")
.required_unless_present_all(["dbg", "infile"])
.action(ArgAction::Set)
.long("config"))
.arg(Arg::new("dbg")
.long("debug")
.action(ArgAction::SetTrue))
.arg(Arg::new("infile")
.short('i')
.action(ArgAction::Set))
.try_get_matches_from(vec![
"prog"
]);

assert!(res.is_err());
assert_eq!(res.unwrap_err().kind(), ErrorKind::MissingRequiredArgument);
```
[required]: Arg::required()
[`Arg::required_unless_present_any`]: Arg::required_unless_present_any()
[`Arg::required_unless_present_all(names)`]: Arg::required_unless_present_all()


**Code Examples:**


```rust
# use clap_builder as clap;
# use clap::Arg;
Arg::new("config")
.required_unless_present_all(["cfg", "dbg"])
# ;
```


```rust
# use clap_builder as clap;
# use clap::{Command, Arg, ArgAction};
let res = Command::new("prog")
.arg(Arg::new("cfg")
.required_unless_present_all(["dbg", "infile"])
.action(ArgAction::Set)
.long("config"))
.arg(Arg::new("dbg")
.long("debug")
.action(ArgAction::SetTrue))
.arg(Arg::new("infile")
.short('i')
.action(ArgAction::Set))
.try_get_matches_from(vec![
"prog", "--debug", "-i", "file"
]);

assert!(res.is_ok());
```


```rust
# use clap_builder as clap;
# use clap::{Command, Arg, error::ErrorKind, ArgAction};
let res = Command::new("prog")
.arg(Arg::new("cfg")
.required_unless_present_all(["dbg", "infile"])
.action(ArgAction::Set)
.long("config"))
.arg(Arg::new("dbg")
.long("debug")
.action(ArgAction::SetTrue))
.arg(Arg::new("infile")
.short('i')
.action(ArgAction::Set))
.try_get_matches_from(vec![
"prog"
]);

assert!(res.is_err());
assert_eq!(res.unwrap_err().kind(), ErrorKind::MissingRequiredArgument);
```


#### Fn: `required_unless_present_any` (line 3431)

<!-- Source: repos/clap/clap_builder/src/builder/arg.rs:3431 -->

<!-- Type: fn -->


Sets this arg as [required] unless *any* of the specified arguments are present at runtime.

In other words, parsing will succeed only if user either
* supplies the `self` arg.
* supplies *one or more* of the `unless` arguments.

<div class="warning">

**NOTE:** If you wish for this argument to be required unless *all of* these args are
present see [`Arg::required_unless_present_all`]

</div>

# Examples

```rust
# use clap_builder as clap;
# use clap::Arg;
Arg::new("config")
.required_unless_present_any(["cfg", "dbg"])
# ;
```

Setting [`Arg::required_unless_present_any(names)`] requires that the argument be used at runtime
*unless* *at least one of* the args in `names` are present. In the following example, the
required argument is *not* provided, but it's not an error because one the `unless` args
have been supplied.

```rust
# use clap_builder as clap;
# use clap::{Command, Arg, ArgAction};
let res = Command::new("prog")
.arg(Arg::new("cfg")
.required_unless_present_any(["dbg", "infile"])
.action(ArgAction::Set)
.long("config"))
.arg(Arg::new("dbg")
.long("debug")
.action(ArgAction::SetTrue))
.arg(Arg::new("infile")
.short('i')
.action(ArgAction::Set))
.try_get_matches_from(vec![
"prog", "--debug"
]);

assert!(res.is_ok());
```

Setting [`Arg::required_unless_present_any(names)`] and *not* supplying *at least one of* `names`
or this arg is an error.

```rust
# use clap_builder as clap;
# use clap::{Command, Arg, error::ErrorKind, ArgAction};
let res = Command::new("prog")
.arg(Arg::new("cfg")
.required_unless_present_any(["dbg", "infile"])
.action(ArgAction::Set)
.long("config"))
.arg(Arg::new("dbg")
.long("debug")
.action(ArgAction::SetTrue))
.arg(Arg::new("infile")
.short('i')
.action(ArgAction::Set))
.try_get_matches_from(vec![
"prog"
]);

assert!(res.is_err());
assert_eq!(res.unwrap_err().kind(), ErrorKind::MissingRequiredArgument);
```
[required]: Arg::required()
[`Arg::required_unless_present_any(names)`]: Arg::required_unless_present_any()
[`Arg::required_unless_present_all`]: Arg::required_unless_present_all()


**Code Examples:**


```rust
# use clap_builder as clap;
# use clap::Arg;
Arg::new("config")
.required_unless_present_any(["cfg", "dbg"])
# ;
```


```rust
# use clap_builder as clap;
# use clap::{Command, Arg, ArgAction};
let res = Command::new("prog")
.arg(Arg::new("cfg")
.required_unless_present_any(["dbg", "infile"])
.action(ArgAction::Set)
.long("config"))
.arg(Arg::new("dbg")
.long("debug")
.action(ArgAction::SetTrue))
.arg(Arg::new("infile")
.short('i')
.action(ArgAction::Set))
.try_get_matches_from(vec![
"prog", "--debug"
]);

assert!(res.is_ok());
```


```rust
# use clap_builder as clap;
# use clap::{Command, Arg, error::ErrorKind, ArgAction};
let res = Command::new("prog")
.arg(Arg::new("cfg")
.required_unless_present_any(["dbg", "infile"])
.action(ArgAction::Set)
.long("config"))
.arg(Arg::new("dbg")
.long("debug")
.action(ArgAction::SetTrue))
.arg(Arg::new("infile")
.short('i')
.action(ArgAction::Set))
.try_get_matches_from(vec![
"prog"
]);

assert!(res.is_err());
assert_eq!(res.unwrap_err().kind(), ErrorKind::MissingRequiredArgument);
```


#### Fn: `required_if_eq` (line 3516)

<!-- Source: repos/clap/clap_builder/src/builder/arg.rs:3516 -->

<!-- Type: fn -->


This argument is [required] only if the specified `arg` is present at runtime and its value
equals `val`.

# Examples

```rust
# use clap_builder as clap;
# use clap::Arg;
Arg::new("config")
.required_if_eq("other_arg", "value")
# ;
```

```rust
# use clap_builder as clap;
# use clap::{Command, Arg, error::ErrorKind, ArgAction};
let res = Command::new("prog")
.arg(Arg::new("cfg")
.action(ArgAction::Set)
.required_if_eq("other", "special")
.long("config"))
.arg(Arg::new("other")
.long("other")
.action(ArgAction::Set))
.try_get_matches_from(vec![
"prog", "--other", "not-special"
]);

assert!(res.is_ok()); // We didn't use --other=special, so "cfg" wasn't required

let res = Command::new("prog")
.arg(Arg::new("cfg")
.action(ArgAction::Set)
.required_if_eq("other", "special")
.long("config"))
.arg(Arg::new("other")
.long("other")
.action(ArgAction::Set))
.try_get_matches_from(vec![
"prog", "--other", "special"
]);

// We did use --other=special so "cfg" had become required but was missing.
assert!(res.is_err());
assert_eq!(res.unwrap_err().kind(), ErrorKind::MissingRequiredArgument);

let res = Command::new("prog")
.arg(Arg::new("cfg")
.action(ArgAction::Set)
.required_if_eq("other", "special")
.long("config"))
.arg(Arg::new("other")
.long("other")
.action(ArgAction::Set))
.try_get_matches_from(vec![
"prog", "--other", "SPECIAL"
]);

// By default, the comparison is case-sensitive, so "cfg" wasn't required
assert!(res.is_ok());

let res = Command::new("prog")
.arg(Arg::new("cfg")
.action(ArgAction::Set)
.required_if_eq("other", "special")
.long("config"))
.arg(Arg::new("other")
.long("other")
.ignore_case(true)
.action(ArgAction::Set))
.try_get_matches_from(vec![
"prog", "--other", "SPECIAL"
]);

// However, case-insensitive comparisons can be enabled.  This typically occurs when using Arg::possible_values().
assert!(res.is_err());
assert_eq!(res.unwrap_err().kind(), ErrorKind::MissingRequiredArgument);
```
[`Arg::requires(name)`]: Arg::requires()
[Conflicting]: Arg::conflicts_with()
[required]: Arg::required()


**Code Examples:**


```rust
# use clap_builder as clap;
# use clap::Arg;
Arg::new("config")
.required_if_eq("other_arg", "value")
# ;
```


```rust
# use clap_builder as clap;
# use clap::{Command, Arg, error::ErrorKind, ArgAction};
let res = Command::new("prog")
.arg(Arg::new("cfg")
.action(ArgAction::Set)
.required_if_eq("other", "special")
.long("config"))
.arg(Arg::new("other")
.long("other")
.action(ArgAction::Set))
.try_get_matches_from(vec![
"prog", "--other", "not-special"
]);

assert!(res.is_ok()); // We didn't use --other=special, so "cfg" wasn't required

let res = Command::new("prog")
.arg(Arg::new("cfg")
.action(ArgAction::Set)
.required_if_eq("other", "special")
.long("config"))
.arg(Arg::new("other")
.long("other")
.action(ArgAction::Set))
.try_get_matches_from(vec![
"prog", "--other", "special"
]);

// We did use --other=special so "cfg" had become required but was missing.
assert!(res.is_err());
assert_eq!(res.unwrap_err().kind(), ErrorKind::MissingRequiredArgument);

let res = Command::new("prog")
.arg(Arg::new("cfg")
.action(ArgAction::Set)
.required_if_eq("other", "special")
.long("config"))
.arg(Arg::new("other")
.long("other")
.action(ArgAction::Set))
.try_get_matches_from(vec![
"prog", "--other", "SPECIAL"
]);

// By default, the comparison is case-sensitive, so "cfg" wasn't required
assert!(res.is_ok());

let res = Command::new("prog")
.arg(Arg::new("cfg")
.action(ArgAction::Set)
.required_if_eq("other", "special")
.long("config"))
.arg(Arg::new("other")
.long("other")
.ignore_case(true)
.action(ArgAction::Set))
.try_get_matches_from(vec![
"prog", "--other", "SPECIAL"
]);

// However, case-insensitive comparisons can be enabled.  This typically occurs when using Arg::possible_values().
assert!(res.is_err());
assert_eq!(res.unwrap_err().kind(), ErrorKind::MissingRequiredArgument);
```


#### Fn: `required_if_eq_any` (line 3603)

<!-- Source: repos/clap/clap_builder/src/builder/arg.rs:3603 -->

<!-- Type: fn -->


Specify this argument is [required] based on multiple conditions.

The conditions are set up in a `(arg, val)` style tuple. The requirement will only become
valid if one of the specified `arg`'s value equals its corresponding `val`.

# Examples

```rust
# use clap_builder as clap;
# use clap::Arg;
Arg::new("config")
.required_if_eq_any([
("extra", "val"),
("option", "spec")
])
# ;
```

Setting `Arg::required_if_eq_any([(arg, val)])` makes this arg required if any of the `arg`s
are used at runtime and it's corresponding value is equal to `val`. If the `arg`'s value is
anything other than `val`, this argument isn't required.

```rust
# use clap_builder as clap;
# use clap::{Command, Arg, ArgAction};
let res = Command::new("prog")
.arg(Arg::new("cfg")
.required_if_eq_any([
("extra", "val"),
("option", "spec")
])
.action(ArgAction::Set)
.long("config"))
.arg(Arg::new("extra")
.action(ArgAction::Set)
.long("extra"))
.arg(Arg::new("option")
.action(ArgAction::Set)
.long("option"))
.try_get_matches_from(vec![
"prog", "--option", "other"
]);

assert!(res.is_ok()); // We didn't use --option=spec, or --extra=val so "cfg" isn't required
```

Setting `Arg::required_if_eq_any([(arg, val)])` and having any of the `arg`s used with its
value of `val` but *not* using this arg is an error.

```rust
# use clap_builder as clap;
# use clap::{Command, Arg, error::ErrorKind, ArgAction};
let res = Command::new("prog")
.arg(Arg::new("cfg")
.required_if_eq_any([
("extra", "val"),
("option", "spec")
])
.action(ArgAction::Set)
.long("config"))
.arg(Arg::new("extra")
.action(ArgAction::Set)
.long("extra"))
.arg(Arg::new("option")
.action(ArgAction::Set)
.long("option"))
.try_get_matches_from(vec![
"prog", "--option", "spec"
]);

assert!(res.is_err());
assert_eq!(res.unwrap_err().kind(), ErrorKind::MissingRequiredArgument);
```
[`Arg::requires(name)`]: Arg::requires()
[Conflicting]: Arg::conflicts_with()
[required]: Arg::required()


**Code Examples:**


```rust
# use clap_builder as clap;
# use clap::Arg;
Arg::new("config")
.required_if_eq_any([
("extra", "val"),
("option", "spec")
])
# ;
```


```rust
# use clap_builder as clap;
# use clap::{Command, Arg, ArgAction};
let res = Command::new("prog")
.arg(Arg::new("cfg")
.required_if_eq_any([
("extra", "val"),
("option", "spec")
])
.action(ArgAction::Set)
.long("config"))
.arg(Arg::new("extra")
.action(ArgAction::Set)
.long("extra"))
.arg(Arg::new("option")
.action(ArgAction::Set)
.long("option"))
.try_get_matches_from(vec![
"prog", "--option", "other"
]);

assert!(res.is_ok()); // We didn't use --option=spec, or --extra=val so "cfg" isn't required
```


```rust
# use clap_builder as clap;
# use clap::{Command, Arg, error::ErrorKind, ArgAction};
let res = Command::new("prog")
.arg(Arg::new("cfg")
.required_if_eq_any([
("extra", "val"),
("option", "spec")
])
.action(ArgAction::Set)
.long("config"))
.arg(Arg::new("extra")
.action(ArgAction::Set)
.long("extra"))
.arg(Arg::new("option")
.action(ArgAction::Set)
.long("option"))
.try_get_matches_from(vec![
"prog", "--option", "spec"
]);

assert!(res.is_err());
assert_eq!(res.unwrap_err().kind(), ErrorKind::MissingRequiredArgument);
```


#### Fn: `required_if_eq_all` (line 3689)

<!-- Source: repos/clap/clap_builder/src/builder/arg.rs:3689 -->

<!-- Type: fn -->


Specify this argument is [required] based on multiple conditions.

The conditions are set up in a `(arg, val)` style tuple. The requirement will only become
valid if every one of the specified `arg`'s value equals its corresponding `val`.

# Examples

```rust
# use clap_builder as clap;
# use clap::Arg;
Arg::new("config")
.required_if_eq_all([
("extra", "val"),
("option", "spec")
])
# ;
```

Setting `Arg::required_if_eq_all([(arg, val)])` makes this arg required if all of the `arg`s
are used at runtime and every value is equal to its corresponding `val`. If the `arg`'s value is
anything other than `val`, this argument isn't required.

```rust
# use clap_builder as clap;
# use clap::{Command, Arg, ArgAction};
let res = Command::new("prog")
.arg(Arg::new("cfg")
.required_if_eq_all([
("extra", "val"),
("option", "spec")
])
.action(ArgAction::Set)
.long("config"))
.arg(Arg::new("extra")
.action(ArgAction::Set)
.long("extra"))
.arg(Arg::new("option")
.action(ArgAction::Set)
.long("option"))
.try_get_matches_from(vec![
"prog", "--option", "spec"
]);

assert!(res.is_ok()); // We didn't use --option=spec --extra=val so "cfg" isn't required
```

Setting `Arg::required_if_eq_all([(arg, val)])` and having all of the `arg`s used with its
value of `val` but *not* using this arg is an error.

```rust
# use clap_builder as clap;
# use clap::{Command, Arg, error::ErrorKind, ArgAction};
let res = Command::new("prog")
.arg(Arg::new("cfg")
.required_if_eq_all([
("extra", "val"),
("option", "spec")
])
.action(ArgAction::Set)
.long("config"))
.arg(Arg::new("extra")
.action(ArgAction::Set)
.long("extra"))
.arg(Arg::new("option")
.action(ArgAction::Set)
.long("option"))
.try_get_matches_from(vec![
"prog", "--extra", "val", "--option", "spec"
]);

assert!(res.is_err());
assert_eq!(res.unwrap_err().kind(), ErrorKind::MissingRequiredArgument);
```
[required]: Arg::required()


**Code Examples:**


```rust
# use clap_builder as clap;
# use clap::Arg;
Arg::new("config")
.required_if_eq_all([
("extra", "val"),
("option", "spec")
])
# ;
```


```rust
# use clap_builder as clap;
# use clap::{Command, Arg, ArgAction};
let res = Command::new("prog")
.arg(Arg::new("cfg")
.required_if_eq_all([
("extra", "val"),
("option", "spec")
])
.action(ArgAction::Set)
.long("config"))
.arg(Arg::new("extra")
.action(ArgAction::Set)
.long("extra"))
.arg(Arg::new("option")
.action(ArgAction::Set)
.long("option"))
.try_get_matches_from(vec![
"prog", "--option", "spec"
]);

assert!(res.is_ok()); // We didn't use --option=spec --extra=val so "cfg" isn't required
```


```rust
# use clap_builder as clap;
# use clap::{Command, Arg, error::ErrorKind, ArgAction};
let res = Command::new("prog")
.arg(Arg::new("cfg")
.required_if_eq_all([
("extra", "val"),
("option", "spec")
])
.action(ArgAction::Set)
.long("config"))
.arg(Arg::new("extra")
.action(ArgAction::Set)
.long("extra"))
.arg(Arg::new("option")
.action(ArgAction::Set)
.long("option"))
.try_get_matches_from(vec![
"prog", "--extra", "val", "--option", "spec"
]);

assert!(res.is_err());
assert_eq!(res.unwrap_err().kind(), ErrorKind::MissingRequiredArgument);
```


#### Fn: `requires_if` (line 3773)

<!-- Source: repos/clap/clap_builder/src/builder/arg.rs:3773 -->

<!-- Type: fn -->


Require another argument if this arg matches the [`ArgPredicate`]

This method takes `value, another_arg` pair. At runtime, clap will check
if this arg (`self`) matches the [`ArgPredicate`].
If it does, `another_arg` will be marked as required.

# Examples

```rust
# use clap_builder as clap;
# use clap::Arg;
Arg::new("config")
.requires_if("val", "arg")
# ;
```

Setting `Arg::requires_if(val, arg)` requires that the `arg` be used at runtime if the
defining argument's value is equal to `val`. If the defining argument is anything other than
`val`, the other argument isn't required.

```rust
# use clap_builder as clap;
# use clap::{Command, Arg, ArgAction};
let res = Command::new("prog")
.arg(Arg::new("cfg")
.action(ArgAction::Set)
.requires_if("my.cfg", "other")
.long("config"))
.arg(Arg::new("other"))
.try_get_matches_from(vec![
"prog", "--config", "some.cfg"
]);

assert!(res.is_ok()); // We didn't use --config=my.cfg, so other wasn't required
```

Setting `Arg::requires_if(val, arg)` and setting the value to `val` but *not* supplying
`arg` is an error.

```rust
# use clap_builder as clap;
# use clap::{Command, Arg, error::ErrorKind, ArgAction};
let res = Command::new("prog")
.arg(Arg::new("cfg")
.action(ArgAction::Set)
.requires_if("my.cfg", "input")
.long("config"))
.arg(Arg::new("input"))
.try_get_matches_from(vec![
"prog", "--config", "my.cfg"
]);

assert!(res.is_err());
assert_eq!(res.unwrap_err().kind(), ErrorKind::MissingRequiredArgument);
```
[`Arg::requires(name)`]: Arg::requires()
[Conflicting]: Arg::conflicts_with()
[override]: Arg::overrides_with()


**Code Examples:**


```rust
# use clap_builder as clap;
# use clap::Arg;
Arg::new("config")
.requires_if("val", "arg")
# ;
```


```rust
# use clap_builder as clap;
# use clap::{Command, Arg, ArgAction};
let res = Command::new("prog")
.arg(Arg::new("cfg")
.action(ArgAction::Set)
.requires_if("my.cfg", "other")
.long("config"))
.arg(Arg::new("other"))
.try_get_matches_from(vec![
"prog", "--config", "some.cfg"
]);

assert!(res.is_ok()); // We didn't use --config=my.cfg, so other wasn't required
```


```rust
# use clap_builder as clap;
# use clap::{Command, Arg, error::ErrorKind, ArgAction};
let res = Command::new("prog")
.arg(Arg::new("cfg")
.action(ArgAction::Set)
.requires_if("my.cfg", "input")
.long("config"))
.arg(Arg::new("input"))
.try_get_matches_from(vec![
"prog", "--config", "my.cfg"
]);

assert!(res.is_err());
assert_eq!(res.unwrap_err().kind(), ErrorKind::MissingRequiredArgument);
```


#### Fn: `requires_ifs` (line 3837)

<!-- Source: repos/clap/clap_builder/src/builder/arg.rs:3837 -->

<!-- Type: fn -->


Allows multiple conditional requirements.

The requirement will only become valid if this arg's value matches the
[`ArgPredicate`].

# Examples

```rust
# use clap_builder as clap;
# use clap::Arg;
Arg::new("config")
.requires_ifs([
("val", "arg"),
("other_val", "arg2"),
])
# ;
```

Setting `Arg::requires_ifs(["val", "arg"])` requires that the `arg` be used at runtime if the
defining argument's value is equal to `val`. If the defining argument's value is anything other
than `val`, `arg` isn't required.

```rust
# use clap_builder as clap;
# use clap::{Command, Arg, error::ErrorKind, ArgAction};
let res = Command::new("prog")
.arg(Arg::new("cfg")
.action(ArgAction::Set)
.requires_ifs([
("special.conf", "opt"),
("other.conf", "other"),
])
.long("config"))
.arg(Arg::new("opt")
.long("option")
.action(ArgAction::Set))
.arg(Arg::new("other"))
.try_get_matches_from(vec![
"prog", "--config", "special.conf"
]);

assert!(res.is_err()); // We  used --config=special.conf so --option <val> is required
assert_eq!(res.unwrap_err().kind(), ErrorKind::MissingRequiredArgument);
```

Setting `Arg::requires_ifs` with [`ArgPredicate::IsPresent`] and *not* supplying all the
arguments is an error.

```rust
# use clap_builder as clap;
# use clap::{Command, Arg, error::ErrorKind, ArgAction, builder::ArgPredicate};
let res = Command::new("prog")
.arg(Arg::new("cfg")
.action(ArgAction::Set)
.requires_ifs([
(ArgPredicate::IsPresent, "input"),
(ArgPredicate::IsPresent, "output"),
])
.long("config"))
.arg(Arg::new("input"))
.arg(Arg::new("output"))
.try_get_matches_from(vec![
"prog", "--config", "file.conf", "in.txt"
]);

assert!(res.is_err());
// We didn't use output
assert_eq!(res.unwrap_err().kind(), ErrorKind::MissingRequiredArgument);
```

[`Arg::requires(name)`]: Arg::requires()
[Conflicting]: Arg::conflicts_with()
[override]: Arg::overrides_with()


**Code Examples:**


```rust
# use clap_builder as clap;
# use clap::Arg;
Arg::new("config")
.requires_ifs([
("val", "arg"),
("other_val", "arg2"),
])
# ;
```


```rust
# use clap_builder as clap;
# use clap::{Command, Arg, error::ErrorKind, ArgAction};
let res = Command::new("prog")
.arg(Arg::new("cfg")
.action(ArgAction::Set)
.requires_ifs([
("special.conf", "opt"),
("other.conf", "other"),
])
.long("config"))
.arg(Arg::new("opt")
.long("option")
.action(ArgAction::Set))
.arg(Arg::new("other"))
.try_get_matches_from(vec![
"prog", "--config", "special.conf"
]);

assert!(res.is_err()); // We  used --config=special.conf so --option <val> is required
assert_eq!(res.unwrap_err().kind(), ErrorKind::MissingRequiredArgument);
```


```rust
# use clap_builder as clap;
# use clap::{Command, Arg, error::ErrorKind, ArgAction, builder::ArgPredicate};
let res = Command::new("prog")
.arg(Arg::new("cfg")
.action(ArgAction::Set)
.requires_ifs([
(ArgPredicate::IsPresent, "input"),
(ArgPredicate::IsPresent, "output"),
])
.long("config"))
.arg(Arg::new("input"))
.arg(Arg::new("output"))
.try_get_matches_from(vec![
"prog", "--config", "file.conf", "in.txt"
]);

assert!(res.is_err());
// We didn't use output
assert_eq!(res.unwrap_err().kind(), ErrorKind::MissingRequiredArgument);
```


#### Fn: `conflicts_with` (line 3929)

<!-- Source: repos/clap/clap_builder/src/builder/arg.rs:3929 -->

<!-- Type: fn -->


This argument is mutually exclusive with the specified argument.

<div class="warning">

**NOTE:** Conflicting rules take precedence over being required by default. Conflict rules
only need to be set for one of the two arguments, they do not need to be set for each.

</div>

<div class="warning">

**NOTE:** Defining a conflict is two-way, but does *not* need to defined for both arguments
(i.e. if A conflicts with B, defining `A.conflicts_with(B)` is sufficient. You do not
need to also do `B.conflicts_with(A)`)

</div>

<div class="warning">

**NOTE:** [`Arg::conflicts_with_all(names)`] allows specifying an argument which conflicts with more than one argument.

</div>

<div class="warning">

**NOTE** [`Arg::exclusive(true)`] allows specifying an argument which conflicts with every other argument.

</div>

<div class="warning">

**NOTE:** All arguments implicitly conflict with themselves.

</div>

# Examples

```rust
# use clap_builder as clap;
# use clap::Arg;
Arg::new("config")
.conflicts_with("debug")
# ;
```

Setting conflicting argument, and having both arguments present at runtime is an error.

```rust
# use clap_builder as clap;
# use clap::{Command, Arg, error::ErrorKind, ArgAction};
let res = Command::new("prog")
.arg(Arg::new("cfg")
.action(ArgAction::Set)
.conflicts_with("debug")
.long("config"))
.arg(Arg::new("debug")
.long("debug")
.action(ArgAction::SetTrue))
.try_get_matches_from(vec![
"prog", "--debug", "--config", "file.conf"
]);

assert!(res.is_err());
assert_eq!(res.unwrap_err().kind(), ErrorKind::ArgumentConflict);
```

[`Arg::conflicts_with_all(names)`]: Arg::conflicts_with_all()
[`Arg::exclusive(true)`]: Arg::exclusive()


**Code Examples:**


```rust
# use clap_builder as clap;
# use clap::Arg;
Arg::new("config")
.conflicts_with("debug")
# ;
```


```rust
# use clap_builder as clap;
# use clap::{Command, Arg, error::ErrorKind, ArgAction};
let res = Command::new("prog")
.arg(Arg::new("cfg")
.action(ArgAction::Set)
.conflicts_with("debug")
.long("config"))
.arg(Arg::new("debug")
.long("debug")
.action(ArgAction::SetTrue))
.try_get_matches_from(vec![
"prog", "--debug", "--config", "file.conf"
]);

assert!(res.is_err());
assert_eq!(res.unwrap_err().kind(), ErrorKind::ArgumentConflict);
```


#### Fn: `conflicts_with_all` (line 4007)

<!-- Source: repos/clap/clap_builder/src/builder/arg.rs:4007 -->

<!-- Type: fn -->


This argument is mutually exclusive with the specified arguments.

See [`Arg::conflicts_with`].

<div class="warning">

**NOTE:** Conflicting rules take precedence over being required by default. Conflict rules
only need to be set for one of the two arguments, they do not need to be set for each.

</div>

<div class="warning">

**NOTE:** Defining a conflict is two-way, but does *not* need to defined for both arguments
(i.e. if A conflicts with B, defining `A.conflicts_with(B)` is sufficient. You do not need
need to also do `B.conflicts_with(A)`)

</div>

<div class="warning">

**NOTE:** [`Arg::exclusive(true)`] allows specifying an argument which conflicts with every other argument.

</div>

# Examples

```rust
# use clap_builder as clap;
# use clap::Arg;
Arg::new("config")
.conflicts_with_all(["debug", "input"])
# ;
```

Setting conflicting argument, and having any of the arguments present at runtime with a
conflicting argument is an error.

```rust
# use clap_builder as clap;
# use clap::{Command, Arg, error::ErrorKind, ArgAction};
let res = Command::new("prog")
.arg(Arg::new("cfg")
.action(ArgAction::Set)
.conflicts_with_all(["debug", "input"])
.long("config"))
.arg(Arg::new("debug")
.long("debug"))
.arg(Arg::new("input"))
.try_get_matches_from(vec![
"prog", "--config", "file.conf", "file.txt"
]);

assert!(res.is_err());
assert_eq!(res.unwrap_err().kind(), ErrorKind::ArgumentConflict);
```
[`Arg::conflicts_with`]: Arg::conflicts_with()
[`Arg::exclusive(true)`]: Arg::exclusive()


**Code Examples:**


```rust
# use clap_builder as clap;
# use clap::Arg;
Arg::new("config")
.conflicts_with_all(["debug", "input"])
# ;
```


```rust
# use clap_builder as clap;
# use clap::{Command, Arg, error::ErrorKind, ArgAction};
let res = Command::new("prog")
.arg(Arg::new("cfg")
.action(ArgAction::Set)
.conflicts_with_all(["debug", "input"])
.long("config"))
.arg(Arg::new("debug")
.long("debug"))
.arg(Arg::new("input"))
.try_get_matches_from(vec![
"prog", "--config", "file.conf", "file.txt"
]);

assert!(res.is_err());
assert_eq!(res.unwrap_err().kind(), ErrorKind::ArgumentConflict);
```


#### Fn: `overrides_with` (line 4071)

<!-- Source: repos/clap/clap_builder/src/builder/arg.rs:4071 -->

<!-- Type: fn -->


Sets an overridable argument.

i.e. this argument and the following argument
will override each other in POSIX style (whichever argument was specified at runtime
**last** "wins")

<div class="warning">

**NOTE:** When an argument is overridden it is essentially as if it never was used, any
conflicts, requirements, etc. are evaluated **after** all "overrides" have been removed

</div>

<div class="warning">

**NOTE:** Overriding an argument implies they [conflict][Arg::conflicts_with`].

</div>

# Examples

```rust
# use clap_builder as clap;
# use clap::{Command, arg};
let m = Command::new("prog")
.arg(arg!(-f --flag "some flag")
.conflicts_with("debug"))
.arg(arg!(-d --debug "other flag"))
.arg(arg!(-c --color "third flag")
.overrides_with("flag"))
.get_matches_from(vec![
"prog", "-f", "-d", "-c"]);
//    ^~~~~~~~~~~~^~~~~ flag is overridden by color

assert!(m.get_flag("color"));
assert!(m.get_flag("debug")); // even though flag conflicts with debug, it's as if flag
// was never used because it was overridden with color
assert!(!m.get_flag("flag"));
```


**Code Examples:**


```rust
# use clap_builder as clap;
# use clap::{Command, arg};
let m = Command::new("prog")
.arg(arg!(-f --flag "some flag")
.conflicts_with("debug"))
.arg(arg!(-d --debug "other flag"))
.arg(arg!(-c --color "third flag")
.overrides_with("flag"))
.get_matches_from(vec![
"prog", "-f", "-d", "-c"]);
//    ^~~~~~~~~~~~^~~~~ flag is overridden by color

assert!(m.get_flag("color"));
assert!(m.get_flag("debug")); // even though flag conflicts with debug, it's as if flag
// was never used because it was overridden with color
assert!(!m.get_flag("flag"));
```


#### Fn: `overrides_with_all` (line 4120)

<!-- Source: repos/clap/clap_builder/src/builder/arg.rs:4120 -->

<!-- Type: fn -->


Sets multiple mutually overridable arguments by name.

i.e. this argument and the following argument will override each other in POSIX style
(whichever argument was specified at runtime **last** "wins")

<div class="warning">

**NOTE:** When an argument is overridden it is essentially as if it never was used, any
conflicts, requirements, etc. are evaluated **after** all "overrides" have been removed

</div>

<div class="warning">

**NOTE:** Overriding an argument implies they [conflict][Arg::conflicts_with_all`].

</div>

# Examples

```rust
# use clap_builder as clap;
# use clap::{Command, arg};
let m = Command::new("prog")
.arg(arg!(-f --flag "some flag")
.conflicts_with("color"))
.arg(arg!(-d --debug "other flag"))
.arg(arg!(-c --color "third flag")
.overrides_with_all(["flag", "debug"]))
.get_matches_from(vec![
"prog", "-f", "-d", "-c"]);
//    ^~~~~~^~~~~~~~~ flag and debug are overridden by color

assert!(m.get_flag("color")); // even though flag conflicts with color, it's as if flag
// and debug were never used because they were overridden
// with color
assert!(!m.get_flag("debug"));
assert!(!m.get_flag("flag"));
```


**Code Examples:**


```rust
# use clap_builder as clap;
# use clap::{Command, arg};
let m = Command::new("prog")
.arg(arg!(-f --flag "some flag")
.conflicts_with("color"))
.arg(arg!(-d --debug "other flag"))
.arg(arg!(-c --color "third flag")
.overrides_with_all(["flag", "debug"]))
.get_matches_from(vec![
"prog", "-f", "-d", "-c"]);
//    ^~~~~~^~~~~~~~~ flag and debug are overridden by color

assert!(m.get_flag("color")); // even though flag conflicts with color, it's as if flag
// and debug were never used because they were overridden
// with color
assert!(!m.get_flag("debug"));
assert!(!m.get_flag("flag"));
```


#### Impl: `Arg` (line 4166)

<!-- Source: repos/clap/clap_builder/src/builder/arg.rs:4166 -->

<!-- Type: impl -->


# Reflection


#### Fn: `get_id` (line 4168)

<!-- Source: repos/clap/clap_builder/src/builder/arg.rs:4168 -->

<!-- Type: fn -->


Get the name of the argument


#### Fn: `get_help` (line 4174)

<!-- Source: repos/clap/clap_builder/src/builder/arg.rs:4174 -->

<!-- Type: fn -->


Get the help specified for this argument, if any


#### Fn: `get_long_help` (line 4180)

<!-- Source: repos/clap/clap_builder/src/builder/arg.rs:4180 -->

<!-- Type: fn -->


Get the long help specified for this argument, if any

# Examples

```rust
# use clap_builder as clap;
# use clap::Arg;
let arg = Arg::new("foo").long_help("long help");
assert_eq!(Some("long help".to_owned()), arg.get_long_help().map(|s| s.to_string()));
```



**Code Examples:**


```rust
# use clap_builder as clap;
# use clap::Arg;
let arg = Arg::new("foo").long_help("long help");
assert_eq!(Some("long help".to_owned()), arg.get_long_help().map(|s| s.to_string()));
```


#### Fn: `get_display_order` (line 4196)

<!-- Source: repos/clap/clap_builder/src/builder/arg.rs:4196 -->

<!-- Type: fn -->


Get the placement within help


#### Fn: `get_help_heading` (line 4202)

<!-- Source: repos/clap/clap_builder/src/builder/arg.rs:4202 -->

<!-- Type: fn -->


Get the help heading specified for this argument, if any


#### Fn: `get_short` (line 4211)

<!-- Source: repos/clap/clap_builder/src/builder/arg.rs:4211 -->

<!-- Type: fn -->


Get the short option name for this argument, if any


#### Fn: `get_visible_short_aliases` (line 4217)

<!-- Source: repos/clap/clap_builder/src/builder/arg.rs:4217 -->

<!-- Type: fn -->


Get visible short aliases for this argument, if any


#### Fn: `get_all_short_aliases` (line 4233)

<!-- Source: repos/clap/clap_builder/src/builder/arg.rs:4233 -->

<!-- Type: fn -->


Get *all* short aliases for this argument, if any, both visible and hidden.


#### Fn: `get_short_and_visible_aliases` (line 4243)

<!-- Source: repos/clap/clap_builder/src/builder/arg.rs:4243 -->

<!-- Type: fn -->


Get the short option name and its visible aliases, if any


#### Fn: `get_long` (line 4256)

<!-- Source: repos/clap/clap_builder/src/builder/arg.rs:4256 -->

<!-- Type: fn -->


Get the long option name for this argument, if any


#### Fn: `get_visible_aliases` (line 4262)

<!-- Source: repos/clap/clap_builder/src/builder/arg.rs:4262 -->

<!-- Type: fn -->


Get visible aliases for this argument, if any


#### Fn: `get_all_aliases` (line 4277)

<!-- Source: repos/clap/clap_builder/src/builder/arg.rs:4277 -->

<!-- Type: fn -->


Get *all* aliases for this argument, if any, both visible and hidden.


#### Fn: `get_long_and_visible_aliases` (line 4287)

<!-- Source: repos/clap/clap_builder/src/builder/arg.rs:4287 -->

<!-- Type: fn -->


Get the long option name and its visible aliases, if any


#### Fn: `get_aliases` (line 4300)

<!-- Source: repos/clap/clap_builder/src/builder/arg.rs:4300 -->

<!-- Type: fn -->


Get hidden aliases for this argument, if any


#### Fn: `get_possible_values` (line 4315)

<!-- Source: repos/clap/clap_builder/src/builder/arg.rs:4315 -->

<!-- Type: fn -->


Get the names of possible values for this argument. Only useful for user
facing applications, such as building help messages or man files


#### Fn: `get_value_names` (line 4328)

<!-- Source: repos/clap/clap_builder/src/builder/arg.rs:4328 -->

<!-- Type: fn -->


Get the names of values for this argument.


#### Fn: `get_num_args` (line 4338)

<!-- Source: repos/clap/clap_builder/src/builder/arg.rs:4338 -->

<!-- Type: fn -->


Get the number of values for this argument.


#### Fn: `get_value_delimiter` (line 4349)

<!-- Source: repos/clap/clap_builder/src/builder/arg.rs:4349 -->

<!-- Type: fn -->


Get the delimiter between multiple values


#### Fn: `get_value_terminator` (line 4355)

<!-- Source: repos/clap/clap_builder/src/builder/arg.rs:4355 -->

<!-- Type: fn -->


Get the value terminator for this argument. The `value_terminator` is a value
that terminates parsing of multi-valued arguments.


#### Fn: `get_index` (line 4362)

<!-- Source: repos/clap/clap_builder/src/builder/arg.rs:4362 -->

<!-- Type: fn -->


Get the index of this argument, if any


#### Fn: `get_value_hint` (line 4368)

<!-- Source: repos/clap/clap_builder/src/builder/arg.rs:4368 -->

<!-- Type: fn -->


Get the value hint of this argument


#### Fn: `get_env` (line 4385)

<!-- Source: repos/clap/clap_builder/src/builder/arg.rs:4385 -->

<!-- Type: fn -->


Get the environment variable name specified for this argument, if any

# Examples

```rust
# use clap_builder as clap;
# use std::ffi::OsStr;
# use clap::Arg;
let arg = Arg::new("foo").env("ENVIRONMENT");
assert_eq!(arg.get_env(), Some(OsStr::new("ENVIRONMENT")));
```


**Code Examples:**


```rust
# use clap_builder as clap;
# use std::ffi::OsStr;
# use clap::Arg;
let arg = Arg::new("foo").env("ENVIRONMENT");
assert_eq!(arg.get_env(), Some(OsStr::new("ENVIRONMENT")));
```


#### Fn: `get_default_values` (line 4401)

<!-- Source: repos/clap/clap_builder/src/builder/arg.rs:4401 -->

<!-- Type: fn -->


Get the default values specified for this argument, if any

# Examples

```rust
# use clap_builder as clap;
# use clap::Arg;
let arg = Arg::new("foo").default_value("default value");
assert_eq!(arg.get_default_values(), &["default value"]);
```


**Code Examples:**


```rust
# use clap_builder as clap;
# use clap::Arg;
let arg = Arg::new("foo").default_value("default value");
assert_eq!(arg.get_default_values(), &["default value"]);
```


#### Fn: `is_positional` (line 4415)

<!-- Source: repos/clap/clap_builder/src/builder/arg.rs:4415 -->

<!-- Type: fn -->


Checks whether this argument is a positional or not.

# Examples

```rust
# use clap_builder as clap;
# use clap::Arg;
let arg = Arg::new("foo");
assert_eq!(arg.is_positional(), true);

let arg = Arg::new("foo").long("foo");
assert_eq!(arg.is_positional(), false);
```


**Code Examples:**


```rust
# use clap_builder as clap;
# use clap::Arg;
let arg = Arg::new("foo");
assert_eq!(arg.is_positional(), true);

let arg = Arg::new("foo").long("foo");
assert_eq!(arg.is_positional(), false);
```


#### Fn: `is_required_set` (line 4432)

<!-- Source: repos/clap/clap_builder/src/builder/arg.rs:4432 -->

<!-- Type: fn -->


Reports whether [`Arg::required`] is set


#### Fn: `is_allow_hyphen_values_set` (line 4447)

<!-- Source: repos/clap/clap_builder/src/builder/arg.rs:4447 -->

<!-- Type: fn -->


Report whether [`Arg::allow_hyphen_values`] is set


#### Fn: `is_allow_negative_numbers_set` (line 4452)

<!-- Source: repos/clap/clap_builder/src/builder/arg.rs:4452 -->

<!-- Type: fn -->


Report whether [`Arg::allow_negative_numbers`] is set


#### Fn: `get_action` (line 4457)

<!-- Source: repos/clap/clap_builder/src/builder/arg.rs:4457 -->

<!-- Type: fn -->


Behavior when parsing the argument


#### Fn: `get_value_parser` (line 4463)

<!-- Source: repos/clap/clap_builder/src/builder/arg.rs:4463 -->

<!-- Type: fn -->


Configured parser for argument values

# Example

```rust
# use clap_builder as clap;
let cmd = clap::Command::new("raw")
.arg(
clap::Arg::new("port")
.value_parser(clap::value_parser!(usize))
);
let value_parser = cmd.get_arguments()
.find(|a| a.get_id() == "port").unwrap()
.get_value_parser();
println!("{value_parser:?}");
```


**Code Examples:**


```rust
# use clap_builder as clap;
let cmd = clap::Command::new("raw")
.arg(
clap::Arg::new("port")
.value_parser(clap::value_parser!(usize))
);
let value_parser = cmd.get_arguments()
.find(|a| a.get_id() == "port").unwrap()
.get_value_parser();
println!("{value_parser:?}");
```


#### Fn: `is_global_set` (line 4488)

<!-- Source: repos/clap/clap_builder/src/builder/arg.rs:4488 -->

<!-- Type: fn -->


Report whether [`Arg::global`] is set


#### Fn: `is_next_line_help_set` (line 4493)

<!-- Source: repos/clap/clap_builder/src/builder/arg.rs:4493 -->

<!-- Type: fn -->


Report whether [`Arg::next_line_help`] is set


#### Fn: `is_hide_set` (line 4498)

<!-- Source: repos/clap/clap_builder/src/builder/arg.rs:4498 -->

<!-- Type: fn -->


Report whether [`Arg::hide`] is set


#### Fn: `is_hide_default_value_set` (line 4503)

<!-- Source: repos/clap/clap_builder/src/builder/arg.rs:4503 -->

<!-- Type: fn -->


Report whether [`Arg::hide_default_value`] is set


#### Fn: `is_hide_possible_values_set` (line 4508)

<!-- Source: repos/clap/clap_builder/src/builder/arg.rs:4508 -->

<!-- Type: fn -->


Report whether [`Arg::hide_possible_values`] is set


#### Fn: `is_hide_env_set` (line 4513)

<!-- Source: repos/clap/clap_builder/src/builder/arg.rs:4513 -->

<!-- Type: fn -->


Report whether [`Arg::hide_env`] is set


#### Fn: `is_hide_env_values_set` (line 4519)

<!-- Source: repos/clap/clap_builder/src/builder/arg.rs:4519 -->

<!-- Type: fn -->


Report whether [`Arg::hide_env_values`] is set


#### Fn: `is_hide_short_help_set` (line 4525)

<!-- Source: repos/clap/clap_builder/src/builder/arg.rs:4525 -->

<!-- Type: fn -->


Report whether [`Arg::hide_short_help`] is set


#### Fn: `is_hide_long_help_set` (line 4530)

<!-- Source: repos/clap/clap_builder/src/builder/arg.rs:4530 -->

<!-- Type: fn -->


Report whether [`Arg::hide_long_help`] is set


#### Fn: `is_require_equals_set` (line 4535)

<!-- Source: repos/clap/clap_builder/src/builder/arg.rs:4535 -->

<!-- Type: fn -->


Report whether [`Arg::require_equals`] is set


#### Fn: `is_exclusive_set` (line 4540)

<!-- Source: repos/clap/clap_builder/src/builder/arg.rs:4540 -->

<!-- Type: fn -->


Reports whether [`Arg::exclusive`] is set


#### Fn: `is_trailing_var_arg_set` (line 4545)

<!-- Source: repos/clap/clap_builder/src/builder/arg.rs:4545 -->

<!-- Type: fn -->


Report whether [`Arg::trailing_var_arg`] is set


#### Fn: `is_last_set` (line 4550)

<!-- Source: repos/clap/clap_builder/src/builder/arg.rs:4550 -->

<!-- Type: fn -->


Reports whether [`Arg::last`] is set


#### Fn: `is_ignore_case_set` (line 4555)

<!-- Source: repos/clap/clap_builder/src/builder/arg.rs:4555 -->

<!-- Type: fn -->


Reports whether [`Arg::ignore_case`] is set


#### Fn: `get` (line 4560)

<!-- Source: repos/clap/clap_builder/src/builder/arg.rs:4560 -->

<!-- Type: fn -->


Access an [`ArgExt`]


#### Fn: `remove` (line 4566)

<!-- Source: repos/clap/clap_builder/src/builder/arg.rs:4566 -->

<!-- Type: fn -->


Remove an [`ArgExt`]


#### Impl: `Arg` (line 4573)

<!-- Source: repos/clap/clap_builder/src/builder/arg.rs:4573 -->

<!-- Type: impl -->


# Internally used only


#### Fn: `render_arg_val` (line 4703)

<!-- Source: repos/clap/clap_builder/src/builder/arg.rs:4703 -->

<!-- Type: fn -->


Write the values such as `<name1> <name2>`


#### Fn: `is_multiple` (line 4746)

<!-- Source: repos/clap/clap_builder/src/builder/arg.rs:4746 -->

<!-- Type: fn -->


Either multiple values or occurrences


#### Trait: `ArgExt` (line 4828)

<!-- Source: repos/clap/clap_builder/src/builder/arg.rs:4828 -->

<!-- Type: trait -->


User-provided data that can be attached to an [`Arg`]


### From `repos/clap/clap_builder/src/builder/arg_group.rs`


#### Struct: `ArgGroup` (line 5)

<!-- Source: repos/clap/clap_builder/src/builder/arg_group.rs:5 -->

<!-- Type: struct -->


Specifies a logical group of [arguments]

You can use this for
- applying validation to an entire group, like [`ArgGroup::multiple`]
- validate relationships between an argument and a group, like [conflicts] or [requirements]
- check which argument in a group was specified on the command-line

For visually grouping arguments in help, see instead
[`Arg::help_heading`][crate::Arg::help_heading].

# Examples

The following example demonstrates using an `ArgGroup` to ensure that one, and only one, of
the arguments from the specified group is present at runtime.

```rust
# use clap_builder as clap;
# use clap::{Command, arg, ArgGroup, error::ErrorKind};
let result = Command::new("cmd")
.arg(arg!(--"set-ver" <ver> "set the version manually"))
.arg(arg!(--major           "auto increase major"))
.arg(arg!(--minor           "auto increase minor"))
.arg(arg!(--patch           "auto increase patch"))
.group(ArgGroup::new("vers")
.args(["set-ver", "major", "minor", "patch"])
.required(true))
.try_get_matches_from(vec!["cmd", "--major", "--patch"]);
// Because we used two args in the group it's an error
assert!(result.is_err());
let err = result.unwrap_err();
assert_eq!(err.kind(), ErrorKind::ArgumentConflict);
```

This next example shows a passing parse of the same scenario
```rust
# use clap_builder as clap;
# use clap::{Command, arg, ArgGroup, Id};
let result = Command::new("cmd")
.arg(arg!(--"set-ver" <ver> "set the version manually"))
.arg(arg!(--major           "auto increase major"))
.arg(arg!(--minor           "auto increase minor"))
.arg(arg!(--patch           "auto increase patch"))
.group(ArgGroup::new("vers")
.args(["set-ver", "major", "minor","patch"])
.required(true))
.try_get_matches_from(vec!["cmd", "--major"]);
assert!(result.is_ok());
let matches = result.unwrap();
// We may not know which of the args was used, so we can test for the group...
assert!(matches.contains_id("vers"));
// We can also ask the group which arg was used
assert_eq!(matches
.get_one::<Id>("vers")
.expect("`vers` is required")
.as_str(),
"major"
);
// we could also alternatively check each arg individually (not shown here)
```
[arguments]: crate::Arg
[conflicts]: crate::Arg::conflicts_with()
[requirements]: crate::Arg::requires()


**Code Examples:**


```rust
# use clap_builder as clap;
# use clap::{Command, arg, ArgGroup, error::ErrorKind};
let result = Command::new("cmd")
.arg(arg!(--"set-ver" <ver> "set the version manually"))
.arg(arg!(--major           "auto increase major"))
.arg(arg!(--minor           "auto increase minor"))
.arg(arg!(--patch           "auto increase patch"))
.group(ArgGroup::new("vers")
.args(["set-ver", "major", "minor", "patch"])
.required(true))
.try_get_matches_from(vec!["cmd", "--major", "--patch"]);
// Because we used two args in the group it's an error
assert!(result.is_err());
let err = result.unwrap_err();
assert_eq!(err.kind(), ErrorKind::ArgumentConflict);
```


```rust
# use clap_builder as clap;
# use clap::{Command, arg, ArgGroup, Id};
let result = Command::new("cmd")
.arg(arg!(--"set-ver" <ver> "set the version manually"))
.arg(arg!(--major           "auto increase major"))
.arg(arg!(--minor           "auto increase minor"))
.arg(arg!(--patch           "auto increase patch"))
.group(ArgGroup::new("vers")
.args(["set-ver", "major", "minor","patch"])
.required(true))
.try_get_matches_from(vec!["cmd", "--major"]);
assert!(result.is_ok());
let matches = result.unwrap();
// We may not know which of the args was used, so we can test for the group...
assert!(matches.contains_id("vers"));
// We can also ask the group which arg was used
assert_eq!(matches
.get_one::<Id>("vers")
.expect("`vers` is required")
.as_str(),
"major"
);
// we could also alternatively check each arg individually (not shown here)
```


#### Impl: `ArgGroup` (line 77)

<!-- Source: repos/clap/clap_builder/src/builder/arg_group.rs:77 -->

<!-- Type: impl -->


# Builder


#### Fn: `new` (line 79)

<!-- Source: repos/clap/clap_builder/src/builder/arg_group.rs:79 -->

<!-- Type: fn -->


Create a `ArgGroup` using a unique name.

The name will be used to get values from the group or refer to the group inside of conflict
and requirement rules.

# Examples

```rust
# use clap_builder as clap;
# use clap::{Command, ArgGroup};
ArgGroup::new("config")
# ;
```


**Code Examples:**


```rust
# use clap_builder as clap;
# use clap::{Command, ArgGroup};
ArgGroup::new("config")
# ;
```


#### Fn: `id` (line 96)

<!-- Source: repos/clap/clap_builder/src/builder/arg_group.rs:96 -->

<!-- Type: fn -->


Sets the group name.

# Examples

```rust
# use clap_builder as clap;
# use clap::{Command, ArgGroup};
ArgGroup::default().id("config")
# ;
```


**Code Examples:**


```rust
# use clap_builder as clap;
# use clap::{Command, ArgGroup};
ArgGroup::default().id("config")
# ;
```


#### Fn: `arg` (line 112)

<!-- Source: repos/clap/clap_builder/src/builder/arg_group.rs:112 -->

<!-- Type: fn -->


Adds an [argument] to this group by name

# Examples

```rust
# use clap_builder as clap;
# use clap::{Command, Arg, ArgGroup, ArgAction};
let m = Command::new("myprog")
.arg(Arg::new("flag")
.short('f')
.action(ArgAction::SetTrue))
.arg(Arg::new("color")
.short('c')
.action(ArgAction::SetTrue))
.group(ArgGroup::new("req_flags")
.arg("flag")
.arg("color"))
.get_matches_from(vec!["myprog", "-f"]);
// maybe we don't know which of the two flags was used...
assert!(m.contains_id("req_flags"));
// but we can also check individually if needed
assert!(m.contains_id("flag"));
```
[argument]: crate::Arg


**Code Examples:**


```rust
# use clap_builder as clap;
# use clap::{Command, Arg, ArgGroup, ArgAction};
let m = Command::new("myprog")
.arg(Arg::new("flag")
.short('f')
.action(ArgAction::SetTrue))
.arg(Arg::new("color")
.short('c')
.action(ArgAction::SetTrue))
.group(ArgGroup::new("req_flags")
.arg("flag")
.arg("color"))
.get_matches_from(vec!["myprog", "-f"]);
// maybe we don't know which of the two flags was used...
assert!(m.contains_id("req_flags"));
// but we can also check individually if needed
assert!(m.contains_id("flag"));
```


#### Fn: `args` (line 146)

<!-- Source: repos/clap/clap_builder/src/builder/arg_group.rs:146 -->

<!-- Type: fn -->


Adds multiple [arguments] to this group by name

# Examples

```rust
# use clap_builder as clap;
# use clap::{Command, Arg, ArgGroup, ArgAction};
let m = Command::new("myprog")
.arg(Arg::new("flag")
.short('f')
.action(ArgAction::SetTrue))
.arg(Arg::new("color")
.short('c')
.action(ArgAction::SetTrue))
.group(ArgGroup::new("req_flags")
.args(["flag", "color"]))
.get_matches_from(vec!["myprog", "-f"]);
// maybe we don't know which of the two flags was used...
assert!(m.contains_id("req_flags"));
// but we can also check individually if needed
assert!(m.contains_id("flag"));
```
[arguments]: crate::Arg


**Code Examples:**


```rust
# use clap_builder as clap;
# use clap::{Command, Arg, ArgGroup, ArgAction};
let m = Command::new("myprog")
.arg(Arg::new("flag")
.short('f')
.action(ArgAction::SetTrue))
.arg(Arg::new("color")
.short('c')
.action(ArgAction::SetTrue))
.group(ArgGroup::new("req_flags")
.args(["flag", "color"]))
.get_matches_from(vec!["myprog", "-f"]);
// maybe we don't know which of the two flags was used...
assert!(m.contains_id("req_flags"));
// but we can also check individually if needed
assert!(m.contains_id("flag"));
```


#### Fn: `get_args` (line 177)

<!-- Source: repos/clap/clap_builder/src/builder/arg_group.rs:177 -->

<!-- Type: fn -->


Getters for all args. It will return a vector of `Id`

# Example

```rust
# use clap_builder as clap;
# use clap::{ArgGroup};
let args: Vec<&str> = vec!["a1".into(), "a4".into()];
let grp = ArgGroup::new("program").args(&args);

for (pos, arg) in grp.get_args().enumerate() {
assert_eq!(*arg, args[pos]);
}
```


**Code Examples:**


```rust
# use clap_builder as clap;
# use clap::{ArgGroup};
let args: Vec<&str> = vec!["a1".into(), "a4".into()];
let grp = ArgGroup::new("program").args(&args);

for (pos, arg) in grp.get_args().enumerate() {
assert_eq!(*arg, args[pos]);
}
```


#### Fn: `multiple` (line 195)

<!-- Source: repos/clap/clap_builder/src/builder/arg_group.rs:195 -->

<!-- Type: fn -->


Allows more than one of the [`Arg`]s in this group to be used. (Default: `false`)

# Examples

Notice in this example we use *both* the `-f` and `-c` flags which are both part of the
group

```rust
# use clap_builder as clap;
# use clap::{Command, Arg, ArgGroup, ArgAction};
let m = Command::new("myprog")
.arg(Arg::new("flag")
.short('f')
.action(ArgAction::SetTrue))
.arg(Arg::new("color")
.short('c')
.action(ArgAction::SetTrue))
.group(ArgGroup::new("req_flags")
.args(["flag", "color"])
.multiple(true))
.get_matches_from(vec!["myprog", "-f", "-c"]);
// maybe we don't know which of the two flags was used...
assert!(m.contains_id("req_flags"));
```
In this next example, we show the default behavior (i.e. `multiple(false)`) which will throw
an error if more than one of the args in the group was used.

```rust
# use clap_builder as clap;
# use clap::{Command, Arg, ArgGroup, error::ErrorKind, ArgAction};
let result = Command::new("myprog")
.arg(Arg::new("flag")
.short('f')
.action(ArgAction::SetTrue))
.arg(Arg::new("color")
.short('c')
.action(ArgAction::SetTrue))
.group(ArgGroup::new("req_flags")
.args(["flag", "color"]))
.try_get_matches_from(vec!["myprog", "-f", "-c"]);
// Because we used both args in the group it's an error
assert!(result.is_err());
let err = result.unwrap_err();
assert_eq!(err.kind(), ErrorKind::ArgumentConflict);
```

[`Arg`]: crate::Arg


**Code Examples:**


```rust
# use clap_builder as clap;
# use clap::{Command, Arg, ArgGroup, ArgAction};
let m = Command::new("myprog")
.arg(Arg::new("flag")
.short('f')
.action(ArgAction::SetTrue))
.arg(Arg::new("color")
.short('c')
.action(ArgAction::SetTrue))
.group(ArgGroup::new("req_flags")
.args(["flag", "color"])
.multiple(true))
.get_matches_from(vec!["myprog", "-f", "-c"]);
// maybe we don't know which of the two flags was used...
assert!(m.contains_id("req_flags"));
```


```rust
# use clap_builder as clap;
# use clap::{Command, Arg, ArgGroup, error::ErrorKind, ArgAction};
let result = Command::new("myprog")
.arg(Arg::new("flag")
.short('f')
.action(ArgAction::SetTrue))
.arg(Arg::new("color")
.short('c')
.action(ArgAction::SetTrue))
.group(ArgGroup::new("req_flags")
.args(["flag", "color"]))
.try_get_matches_from(vec!["myprog", "-f", "-c"]);
// Because we used both args in the group it's an error
assert!(result.is_err());
let err = result.unwrap_err();
assert_eq!(err.kind(), ErrorKind::ArgumentConflict);
```


#### Fn: `is_multiple` (line 249)

<!-- Source: repos/clap/clap_builder/src/builder/arg_group.rs:249 -->

<!-- Type: fn -->


Return true if the group allows more than one of the arguments
in this group to be used. (Default: `false`)

# Example

```rust
# use clap_builder as clap;
# use clap::{ArgGroup};
let mut group = ArgGroup::new("myprog")
.args(["f", "c"])
.multiple(true);

assert!(group.is_multiple());
```


**Code Examples:**


```rust
# use clap_builder as clap;
# use clap::{ArgGroup};
let mut group = ArgGroup::new("myprog")
.args(["f", "c"])
.multiple(true);

assert!(group.is_multiple());
```


#### Fn: `required` (line 267)

<!-- Source: repos/clap/clap_builder/src/builder/arg_group.rs:267 -->

<!-- Type: fn -->


Require an argument from the group to be present when parsing.

This is unless conflicting with another argument.  A required group will be displayed in
the usage string of the application in the format `<arg|arg2|arg3>`.

<div class="warning">

**NOTE:** This setting only applies to the current [`Command`] / [`Subcommand`]s, and not
globally.

</div>

<div class="warning">

**NOTE:** By default, [`ArgGroup::multiple`] is set to `false` which when combined with
`ArgGroup::required(true)` states, "One and *only one* arg must be used from this group.
Use of more than one arg is an error." Vice setting `ArgGroup::multiple(true)` which
states, '*At least* one arg from this group must be used. Using multiple is OK."

</div>

# Examples

```rust
# use clap_builder as clap;
# use clap::{Command, Arg, ArgGroup, error::ErrorKind, ArgAction};
let result = Command::new("myprog")
.arg(Arg::new("flag")
.short('f')
.action(ArgAction::SetTrue))
.arg(Arg::new("color")
.short('c')
.action(ArgAction::SetTrue))
.group(ArgGroup::new("req_flags")
.args(["flag", "color"])
.required(true))
.try_get_matches_from(vec!["myprog"]);
// Because we didn't use any of the args in the group, it's an error
assert!(result.is_err());
let err = result.unwrap_err();
assert_eq!(err.kind(), ErrorKind::MissingRequiredArgument);
```

[`Subcommand`]: crate::Subcommand
[`ArgGroup::multiple`]: ArgGroup::multiple()
[`Command`]: crate::Command


**Code Examples:**


```rust
# use clap_builder as clap;
# use clap::{Command, Arg, ArgGroup, error::ErrorKind, ArgAction};
let result = Command::new("myprog")
.arg(Arg::new("flag")
.short('f')
.action(ArgAction::SetTrue))
.arg(Arg::new("color")
.short('c')
.action(ArgAction::SetTrue))
.group(ArgGroup::new("req_flags")
.args(["flag", "color"])
.required(true))
.try_get_matches_from(vec!["myprog"]);
// Because we didn't use any of the args in the group, it's an error
assert!(result.is_err());
let err = result.unwrap_err();
assert_eq!(err.kind(), ErrorKind::MissingRequiredArgument);
```


#### Fn: `requires` (line 320)

<!-- Source: repos/clap/clap_builder/src/builder/arg_group.rs:320 -->

<!-- Type: fn -->


Specify an argument or group that must be present when this group is.

This is not to be confused with a [required group]. Requirement rules function just like
[argument requirement rules], you can name other arguments or groups that must be present
when any one of the arguments from this group is used.

<div class="warning">

**NOTE:** The name provided may be an argument or group name

</div>

# Examples

```rust
# use clap_builder as clap;
# use clap::{Command, Arg, ArgGroup, error::ErrorKind, ArgAction};
let result = Command::new("myprog")
.arg(Arg::new("flag")
.short('f')
.action(ArgAction::SetTrue))
.arg(Arg::new("color")
.short('c')
.action(ArgAction::SetTrue))
.arg(Arg::new("debug")
.short('d')
.action(ArgAction::SetTrue))
.group(ArgGroup::new("req_flags")
.args(["flag", "color"])
.requires("debug"))
.try_get_matches_from(vec!["myprog", "-c"]);
// because we used an arg from the group, and the group requires "-d" to be used, it's an
// error
assert!(result.is_err());
let err = result.unwrap_err();
assert_eq!(err.kind(), ErrorKind::MissingRequiredArgument);
```
[required group]: ArgGroup::required()
[argument requirement rules]: crate::Arg::requires()


**Code Examples:**


```rust
# use clap_builder as clap;
# use clap::{Command, Arg, ArgGroup, error::ErrorKind, ArgAction};
let result = Command::new("myprog")
.arg(Arg::new("flag")
.short('f')
.action(ArgAction::SetTrue))
.arg(Arg::new("color")
.short('c')
.action(ArgAction::SetTrue))
.arg(Arg::new("debug")
.short('d')
.action(ArgAction::SetTrue))
.group(ArgGroup::new("req_flags")
.args(["flag", "color"])
.requires("debug"))
.try_get_matches_from(vec!["myprog", "-c"]);
// because we used an arg from the group, and the group requires "-d" to be used, it's an
// error
assert!(result.is_err());
let err = result.unwrap_err();
assert_eq!(err.kind(), ErrorKind::MissingRequiredArgument);
```


#### Fn: `requires_all` (line 369)

<!-- Source: repos/clap/clap_builder/src/builder/arg_group.rs:369 -->

<!-- Type: fn -->


Specify arguments or groups that must be present when this group is.

This is not to be confused with a [required group]. Requirement rules function just like
[argument requirement rules], you can name other arguments or groups that must be present
when one of the arguments from this group is used.

<div class="warning">

**NOTE:** The names provided may be an argument or group name

</div>

# Examples

```rust
# use clap_builder as clap;
# use clap::{Command, Arg, ArgGroup, error::ErrorKind, ArgAction};
let result = Command::new("myprog")
.arg(Arg::new("flag")
.short('f')
.action(ArgAction::SetTrue))
.arg(Arg::new("color")
.short('c')
.action(ArgAction::SetTrue))
.arg(Arg::new("debug")
.short('d')
.action(ArgAction::SetTrue))
.arg(Arg::new("verb")
.short('v')
.action(ArgAction::SetTrue))
.group(ArgGroup::new("req_flags")
.args(["flag", "color"])
.requires_all(["debug", "verb"]))
.try_get_matches_from(vec!["myprog", "-c", "-d"]);
// because we used an arg from the group, and the group requires "-d" and "-v" to be used,
// yet we only used "-d" it's an error
assert!(result.is_err());
let err = result.unwrap_err();
assert_eq!(err.kind(), ErrorKind::MissingRequiredArgument);
```
[required group]: ArgGroup::required()
[argument requirement rules]: crate::Arg::requires_ifs()


**Code Examples:**


```rust
# use clap_builder as clap;
# use clap::{Command, Arg, ArgGroup, error::ErrorKind, ArgAction};
let result = Command::new("myprog")
.arg(Arg::new("flag")
.short('f')
.action(ArgAction::SetTrue))
.arg(Arg::new("color")
.short('c')
.action(ArgAction::SetTrue))
.arg(Arg::new("debug")
.short('d')
.action(ArgAction::SetTrue))
.arg(Arg::new("verb")
.short('v')
.action(ArgAction::SetTrue))
.group(ArgGroup::new("req_flags")
.args(["flag", "color"])
.requires_all(["debug", "verb"]))
.try_get_matches_from(vec!["myprog", "-c", "-d"]);
// because we used an arg from the group, and the group requires "-d" and "-v" to be used,
// yet we only used "-d" it's an error
assert!(result.is_err());
let err = result.unwrap_err();
assert_eq!(err.kind(), ErrorKind::MissingRequiredArgument);
```


#### Fn: `conflicts_with` (line 419)

<!-- Source: repos/clap/clap_builder/src/builder/arg_group.rs:419 -->

<!-- Type: fn -->


Specify an argument or group that must **not** be present when this group is.

Exclusion (aka conflict) rules function just like [argument exclusion rules], you can name
other arguments or groups that must *not* be present when one of the arguments from this
group are used.

<div class="warning">

**NOTE:** The name provided may be an argument, or group name

</div>

# Examples

```rust
# use clap_builder as clap;
# use clap::{Command, Arg, ArgGroup, error::ErrorKind, ArgAction};
let result = Command::new("myprog")
.arg(Arg::new("flag")
.short('f')
.action(ArgAction::SetTrue))
.arg(Arg::new("color")
.short('c')
.action(ArgAction::SetTrue))
.arg(Arg::new("debug")
.short('d')
.action(ArgAction::SetTrue))
.group(ArgGroup::new("req_flags")
.args(["flag", "color"])
.conflicts_with("debug"))
.try_get_matches_from(vec!["myprog", "-c", "-d"]);
// because we used an arg from the group, and the group conflicts with "-d", it's an error
assert!(result.is_err());
let err = result.unwrap_err();
assert_eq!(err.kind(), ErrorKind::ArgumentConflict);
```
[argument exclusion rules]: crate::Arg::conflicts_with()


**Code Examples:**


```rust
# use clap_builder as clap;
# use clap::{Command, Arg, ArgGroup, error::ErrorKind, ArgAction};
let result = Command::new("myprog")
.arg(Arg::new("flag")
.short('f')
.action(ArgAction::SetTrue))
.arg(Arg::new("color")
.short('c')
.action(ArgAction::SetTrue))
.arg(Arg::new("debug")
.short('d')
.action(ArgAction::SetTrue))
.group(ArgGroup::new("req_flags")
.args(["flag", "color"])
.conflicts_with("debug"))
.try_get_matches_from(vec!["myprog", "-c", "-d"]);
// because we used an arg from the group, and the group conflicts with "-d", it's an error
assert!(result.is_err());
let err = result.unwrap_err();
assert_eq!(err.kind(), ErrorKind::ArgumentConflict);
```


#### Fn: `conflicts_with_all` (line 466)

<!-- Source: repos/clap/clap_builder/src/builder/arg_group.rs:466 -->

<!-- Type: fn -->


Specify arguments or groups that must **not** be present when this group is.

Exclusion rules function just like [argument exclusion rules], you can name other arguments
or groups that must *not* be present when one of the arguments from this group are used.

<div class="warning">

**NOTE:** The names provided may be an argument, or group name

</div>

# Examples

```rust
# use clap_builder as clap;
# use clap::{Command, Arg, ArgGroup, error::ErrorKind, ArgAction};
let result = Command::new("myprog")
.arg(Arg::new("flag")
.short('f')
.action(ArgAction::SetTrue))
.arg(Arg::new("color")
.short('c')
.action(ArgAction::SetTrue))
.arg(Arg::new("debug")
.short('d')
.action(ArgAction::SetTrue))
.arg(Arg::new("verb")
.short('v')
.action(ArgAction::SetTrue))
.group(ArgGroup::new("req_flags")
.args(["flag", "color"])
.conflicts_with_all(["debug", "verb"]))
.try_get_matches_from(vec!["myprog", "-c", "-v"]);
// because we used an arg from the group, and the group conflicts with either "-v" or "-d"
// it's an error
assert!(result.is_err());
let err = result.unwrap_err();
assert_eq!(err.kind(), ErrorKind::ArgumentConflict);
```

[argument exclusion rules]: crate::Arg::conflicts_with_all()


**Code Examples:**


```rust
# use clap_builder as clap;
# use clap::{Command, Arg, ArgGroup, error::ErrorKind, ArgAction};
let result = Command::new("myprog")
.arg(Arg::new("flag")
.short('f')
.action(ArgAction::SetTrue))
.arg(Arg::new("color")
.short('c')
.action(ArgAction::SetTrue))
.arg(Arg::new("debug")
.short('d')
.action(ArgAction::SetTrue))
.arg(Arg::new("verb")
.short('v')
.action(ArgAction::SetTrue))
.group(ArgGroup::new("req_flags")
.args(["flag", "color"])
.conflicts_with_all(["debug", "verb"]))
.try_get_matches_from(vec!["myprog", "-c", "-v"]);
// because we used an arg from the group, and the group conflicts with either "-v" or "-d"
// it's an error
assert!(result.is_err());
let err = result.unwrap_err();
assert_eq!(err.kind(), ErrorKind::ArgumentConflict);
```


#### Impl: `ArgGroup` (line 516)

<!-- Source: repos/clap/clap_builder/src/builder/arg_group.rs:516 -->

<!-- Type: impl -->


# Reflection


#### Fn: `get_id` (line 518)

<!-- Source: repos/clap/clap_builder/src/builder/arg_group.rs:518 -->

<!-- Type: fn -->


Get the name of the group


#### Fn: `is_required_set` (line 524)

<!-- Source: repos/clap/clap_builder/src/builder/arg_group.rs:524 -->

<!-- Type: fn -->


Reports whether [`ArgGroup::required`] is set


### From `repos/clap/clap_builder/src/builder/arg_predicate.rs`


#### Enum: `ArgPredicate` (line 3)

<!-- Source: repos/clap/clap_builder/src/builder/arg_predicate.rs:3 -->

<!-- Type: enum -->


Operations to perform on argument values

These do not apply to [`ValueSource::DefaultValue`][crate::parser::ValueSource::DefaultValue]


### From `repos/clap/clap_builder/src/builder/arg_settings.rs`


#### Enum: `ArgSettings` (line 34)

<!-- Source: repos/clap/clap_builder/src/builder/arg_settings.rs:34 -->

<!-- Type: enum -->


Various settings that apply to arguments and may be set, unset, and checked via getter/setter
methods [`Arg::setting`], [`Arg::unset_setting`], and [`Arg::is_set`]. This is what the
[`Arg`] methods which accept a `bool` use internally.

[`Arg`]: crate::Arg
[`Arg::setting`]: crate::Arg::setting()
[`Arg::unset_setting`]: crate::Arg::unset_setting()
[`Arg::is_set`]: crate::Arg::is_set()


### From `repos/clap/clap_builder/src/builder/value_parser.rs`


#### Struct: `UnknownArgumentValueParser` (line 2125)

<!-- Source: repos/clap/clap_builder/src/builder/value_parser.rs:2125 -->

<!-- Type: struct -->


When encountered, report [`ErrorKind::UnknownArgument`][crate::error::ErrorKind::UnknownArgument]

Useful to help users migrate, either from old versions or similar tools.

# Examples

```rust
# use clap_builder as clap;
# use clap::Command;
# use clap::Arg;
let cmd = Command::new("mycmd")
.args([
Arg::new("current-dir")
.short('C'),
Arg::new("current-dir-unknown")
.long("cwd")
.aliases(["current-dir", "directory", "working-directory", "root"])
.value_parser(clap::builder::UnknownArgumentValueParser::suggest_arg("-C"))
.hide(true),
]);

// Use a supported version of the argument
let matches = cmd.clone().try_get_matches_from(["mycmd", "-C", ".."]).unwrap();
assert!(matches.contains_id("current-dir"));
assert_eq!(
matches.get_many::<String>("current-dir").unwrap_or_default().map(|v| v.as_str()).collect::<Vec<_>>(),
vec![".."]
);

// Use one of the invalid versions
let err = cmd.try_get_matches_from(["mycmd", "--cwd", ".."]).unwrap_err();
assert_eq!(err.kind(), clap::error::ErrorKind::UnknownArgument);
```


**Code Examples:**


```rust
# use clap_builder as clap;
# use clap::Command;
# use clap::Arg;
let cmd = Command::new("mycmd")
.args([
Arg::new("current-dir")
.short('C'),
Arg::new("current-dir-unknown")
.long("cwd")
.aliases(["current-dir", "directory", "working-directory", "root"])
.value_parser(clap::builder::UnknownArgumentValueParser::suggest_arg("-C"))
.hide(true),
]);

// Use a supported version of the argument
let matches = cmd.clone().try_get_matches_from(["mycmd", "-C", ".."]).unwrap();
assert!(matches.contains_id("current-dir"));
assert_eq!(
matches.get_many::<String>("current-dir").unwrap_or_default().map(|v| v.as_str()).collect::<Vec<_>>(),
vec![".."]
);

// Use one of the invalid versions
let err = cmd.try_get_matches_from(["mycmd", "--cwd", ".."]).unwrap_err();
assert_eq!(err.kind(), clap::error::ErrorKind::UnknownArgument);
```


### From `repos/clap/clap_builder/src/parser/matches/arg_matches.rs`


#### Fn: `get_one` (line 78)

<!-- Source: repos/clap/clap_builder/src/parser/matches/arg_matches.rs:78 -->

<!-- Type: fn -->


Gets the value of a specific option or positional argument.

i.e. an argument that [takes an additional value][crate::Arg::num_args] at runtime.

Returns an error if the wrong type was used.

Returns `None` if the option wasn't present.

<div class="warning">

*NOTE:* This will always return `Some(value)` if [`default_value`] has been set.
[`ArgMatches::value_source`] can be used to check if a value is present at runtime.

</div>

# Panic

If the argument definition and access mismatch.  To handle this case programmatically, see
[`ArgMatches::try_get_one`].

# Examples

```rust
# use clap_builder as clap;
# use clap::{Command, Arg, value_parser, ArgAction};
let m = Command::new("myapp")
.arg(Arg::new("port")
.value_parser(value_parser!(usize))
.action(ArgAction::Set)
.required(true))
.get_matches_from(vec!["myapp", "2020"]);

let port: usize = *m
.get_one("port")
.expect("`port`is required");
assert_eq!(port, 2020);
```
[positional]: crate::Arg::index()
[`default_value`]: crate::Arg::default_value()


**Code Examples:**


```rust
# use clap_builder as clap;
# use clap::{Command, Arg, value_parser, ArgAction};
let m = Command::new("myapp")
.arg(Arg::new("port")
.value_parser(value_parser!(usize))
.action(ArgAction::Set)
.required(true))
.get_matches_from(vec!["myapp", "2020"]);

let port: usize = *m
.get_one("port")
.expect("`port`is required");
assert_eq!(port, 2020);
```


#### Fn: `get_count` (line 122)

<!-- Source: repos/clap/clap_builder/src/parser/matches/arg_matches.rs:122 -->

<!-- Type: fn -->


Gets the value of a specific [`ArgAction::Count`][crate::ArgAction::Count] flag

# Panic

If the argument's action is not [`ArgAction::Count`][crate::ArgAction::Count]

# Examples

```rust
# use clap_builder as clap;
# use clap::Command;
# use clap::Arg;
let cmd = Command::new("mycmd")
.arg(
Arg::new("flag")
.long("flag")
.action(clap::ArgAction::Count)
);

let matches = cmd.clone().try_get_matches_from(["mycmd", "--flag", "--flag"]).unwrap();
assert_eq!(
matches.get_count("flag"),
2
);
```


**Code Examples:**


```rust
# use clap_builder as clap;
# use clap::Command;
# use clap::Arg;
let cmd = Command::new("mycmd")
.arg(
Arg::new("flag")
.long("flag")
.action(clap::ArgAction::Count)
);

let matches = cmd.clone().try_get_matches_from(["mycmd", "--flag", "--flag"]).unwrap();
assert_eq!(
matches.get_count("flag"),
2
);
```


#### Fn: `get_flag` (line 154)

<!-- Source: repos/clap/clap_builder/src/parser/matches/arg_matches.rs:154 -->

<!-- Type: fn -->


Gets the value of a specific [`ArgAction::SetTrue`][crate::ArgAction::SetTrue] or [`ArgAction::SetFalse`][crate::ArgAction::SetFalse] flag

# Panic

If the argument's action is not [`ArgAction::SetTrue`][crate::ArgAction::SetTrue] or [`ArgAction::SetFalse`][crate::ArgAction::SetFalse]

# Examples

```rust
# use clap_builder as clap;
# use clap::Command;
# use clap::Arg;
let cmd = Command::new("mycmd")
.arg(
Arg::new("flag")
.long("flag")
.action(clap::ArgAction::SetTrue)
);

let matches = cmd.clone().try_get_matches_from(["mycmd", "--flag"]).unwrap();
assert!(matches.contains_id("flag"));
assert_eq!(
matches.get_flag("flag"),
true
);
```


**Code Examples:**


```rust
# use clap_builder as clap;
# use clap::Command;
# use clap::Arg;
let cmd = Command::new("mycmd")
.arg(
Arg::new("flag")
.long("flag")
.action(clap::ArgAction::SetTrue)
);

let matches = cmd.clone().try_get_matches_from(["mycmd", "--flag"]).unwrap();
assert!(matches.contains_id("flag"));
assert_eq!(
matches.get_flag("flag"),
true
);
```


#### Fn: `get_many` (line 191)

<!-- Source: repos/clap/clap_builder/src/parser/matches/arg_matches.rs:191 -->

<!-- Type: fn -->


Iterate over values of a specific option or positional argument.

i.e. an argument that takes multiple values at runtime.

Returns an error if the wrong type was used.

Returns `None` if the option wasn't present.

# Panic

If the argument definition and access mismatch.  To handle this case programmatically, see
[`ArgMatches::try_get_many`].

# Examples

```rust
# use clap_builder as clap;
# use clap::{Command, Arg, value_parser, ArgAction};
let m = Command::new("myprog")
.arg(Arg::new("ports")
.action(ArgAction::Append)
.value_parser(value_parser!(usize))
.short('p')
.required(true))
.get_matches_from(vec![
"myprog", "-p", "22", "-p", "80", "-p", "2020"
]);
let vals: Vec<usize> = m.get_many("ports")
.expect("`port`is required")
.copied()
.collect();
assert_eq!(vals, [22, 80, 2020]);
```


**Code Examples:**


```rust
# use clap_builder as clap;
# use clap::{Command, Arg, value_parser, ArgAction};
let m = Command::new("myprog")
.arg(Arg::new("ports")
.action(ArgAction::Append)
.value_parser(value_parser!(usize))
.short('p')
.required(true))
.get_matches_from(vec![
"myprog", "-p", "22", "-p", "80", "-p", "2020"
]);
let vals: Vec<usize> = m.get_many("ports")
.expect("`port`is required")
.copied()
.collect();
assert_eq!(vals, [22, 80, 2020]);
```


#### Fn: `get_occurrences` (line 232)

<!-- Source: repos/clap/clap_builder/src/parser/matches/arg_matches.rs:232 -->

<!-- Type: fn -->


Iterate over the values passed to each occurrence of an option.

Each item is itself an iterator containing the arguments passed to a single occurrence
of the option.

If the option doesn't support multiple occurrences, or there was only a single occurrence,
the iterator will only contain a single item.

Returns `None` if the option wasn't present.

# Panics

If the argument definition and access mismatch (debug builds). To handle this case programmatically, see
[`ArgMatches::try_get_occurrences`].

# Examples
```rust
# use clap_builder as clap;
# use clap::{Command,Arg, ArgAction, value_parser};
let m = Command::new("myprog")
.arg(Arg::new("x")
.short('x')
.num_args(2)
.action(ArgAction::Append)
.value_parser(value_parser!(String)))
.get_matches_from(vec![
"myprog", "-x", "a", "b", "-x", "c", "d"]);
let vals: Vec<Vec<&String>> = m.get_occurrences("x").unwrap().map(Iterator::collect).collect();
assert_eq!(vals, [["a", "b"], ["c", "d"]]);
```


**Code Examples:**


```rust
# use clap_builder as clap;
# use clap::{Command,Arg, ArgAction, value_parser};
let m = Command::new("myprog")
.arg(Arg::new("x")
.short('x')
.num_args(2)
.action(ArgAction::Append)
.value_parser(value_parser!(String)))
.get_matches_from(vec![
"myprog", "-x", "a", "b", "-x", "c", "d"]);
let vals: Vec<Vec<&String>> = m.get_occurrences("x").unwrap().map(Iterator::collect).collect();
assert_eq!(vals, [["a", "b"], ["c", "d"]]);
```


#### Fn: `get_raw` (line 270)

<!-- Source: repos/clap/clap_builder/src/parser/matches/arg_matches.rs:270 -->

<!-- Type: fn -->


Iterate over the original argument values.

An `OsStr` on Unix-like systems is any series of bytes, regardless of whether or not they
contain valid UTF-8. Since [`String`]s in Rust are guaranteed to be valid UTF-8, a valid
filename on a Unix system as an argument value may contain invalid UTF-8.

Returns `None` if the option wasn't present.

# Panic

If the argument definition and access mismatch.  To handle this case programmatically, see
[`ArgMatches::try_get_raw`].

# Examples

```rust
# #[cfg(unix)] {
# use clap_builder as clap;
# use clap::{Command, arg, value_parser};
# use std::ffi::{OsStr,OsString};
# use std::os::unix::ffi::{OsStrExt,OsStringExt};
use std::path::PathBuf;

let m = Command::new("utf8")
.arg(arg!(<arg> ... "some arg").value_parser(value_parser!(PathBuf)))
.get_matches_from(vec![OsString::from("myprog"),
// "Hi"
OsString::from_vec(vec![b'H', b'i']),
// "{0xe9}!"
OsString::from_vec(vec![0xe9, b'!'])]);

let mut itr = m.get_raw("arg")
.expect("`port`is required")
.into_iter();
assert_eq!(itr.next(), Some(OsStr::new("Hi")));
assert_eq!(itr.next(), Some(OsStr::from_bytes(&[0xe9, b'!'])));
assert_eq!(itr.next(), None);
# }
```
[`Iterator`]: std::iter::Iterator
[`OsSt`]: std::ffi::OsStr
[`String`]: std::string::String


**Code Examples:**


```rust
# #[cfg(unix)] {
# use clap_builder as clap;
# use clap::{Command, arg, value_parser};
# use std::ffi::{OsStr,OsString};
# use std::os::unix::ffi::{OsStrExt,OsStringExt};
use std::path::PathBuf;

let m = Command::new("utf8")
.arg(arg!(<arg> ... "some arg").value_parser(value_parser!(PathBuf)))
.get_matches_from(vec![OsString::from("myprog"),
// "Hi"
OsString::from_vec(vec![b'H', b'i']),
// "{0xe9}!"
OsString::from_vec(vec![0xe9, b'!'])]);

let mut itr = m.get_raw("arg")
.expect("`port`is required")
.into_iter();
assert_eq!(itr.next(), Some(OsStr::new("Hi")));
assert_eq!(itr.next(), Some(OsStr::from_bytes(&[0xe9, b'!'])));
assert_eq!(itr.next(), None);
# }
```


#### Fn: `get_raw_occurrences` (line 317)

<!-- Source: repos/clap/clap_builder/src/parser/matches/arg_matches.rs:317 -->

<!-- Type: fn -->


Iterate over the original values for each occurrence of an option.

Similar to [`ArgMatches::get_occurrences`] but returns raw values.

An `OsStr` on Unix-like systems is any series of bytes, regardless of whether or not they
contain valid UTF-8. Since [`String`]s in Rust are guaranteed to be valid UTF-8, a valid
filename on a Unix system as an argument value may contain invalid UTF-8.

Returns `None` if the option wasn't present.

# Panic

If the argument definition and access mismatch.  To handle this case programmatically, see
[`ArgMatches::try_get_raw_occurrences`].

# Examples

```rust
# #[cfg(unix)] {
# use clap_builder as clap;
# use clap::{Command, arg, value_parser, ArgAction, Arg};
# use std::ffi::{OsStr,OsString};
# use std::os::unix::ffi::{OsStrExt,OsStringExt};
use std::path::PathBuf;

let m = Command::new("myprog")
.arg(Arg::new("x")
.short('x')
.num_args(2)
.action(ArgAction::Append)
.value_parser(value_parser!(PathBuf)))
.get_matches_from(vec![OsString::from("myprog"),
OsString::from("-x"),
OsString::from("a"), OsString::from("b"),
OsString::from("-x"),
OsString::from("c"),
// "{0xe9}!"
OsString::from_vec(vec![0xe9, b'!'])]);
let mut itr = m.get_raw_occurrences("x")
.expect("`-x`is required")
.map(Iterator::collect::<Vec<_>>);
assert_eq!(itr.next(), Some(vec![OsStr::new("a"), OsStr::new("b")]));
assert_eq!(itr.next(), Some(vec![OsStr::new("c"), OsStr::from_bytes(&[0xe9, b'!'])]));
assert_eq!(itr.next(), None);
# }
```
[`Iterator`]: std::iter::Iterator
[`OsStr`]: std::ffi::OsStr
[`String`]: std::string::String


**Code Examples:**


```rust
# #[cfg(unix)] {
# use clap_builder as clap;
# use clap::{Command, arg, value_parser, ArgAction, Arg};
# use std::ffi::{OsStr,OsString};
# use std::os::unix::ffi::{OsStrExt,OsStringExt};
use std::path::PathBuf;

let m = Command::new("myprog")
.arg(Arg::new("x")
.short('x')
.num_args(2)
.action(ArgAction::Append)
.value_parser(value_parser!(PathBuf)))
.get_matches_from(vec![OsString::from("myprog"),
OsString::from("-x"),
OsString::from("a"), OsString::from("b"),
OsString::from("-x"),
OsString::from("c"),
// "{0xe9}!"
OsString::from_vec(vec![0xe9, b'!'])]);
let mut itr = m.get_raw_occurrences("x")
.expect("`-x`is required")
.map(Iterator::collect::<Vec<_>>);
assert_eq!(itr.next(), Some(vec![OsStr::new("a"), OsStr::new("b")]));
assert_eq!(itr.next(), Some(vec![OsStr::new("c"), OsStr::from_bytes(&[0xe9, b'!'])]));
assert_eq!(itr.next(), None);
# }
```


#### Fn: `remove_one` (line 371)

<!-- Source: repos/clap/clap_builder/src/parser/matches/arg_matches.rs:371 -->

<!-- Type: fn -->


Returns the value of a specific option or positional argument.

i.e. an argument that [takes an additional value][crate::Arg::num_args] at runtime.

Returns an error if the wrong type was used.  No item will have been removed.

Returns `None` if the option wasn't present.

<div class="warning">

*NOTE:* This will always return `Some(value)` if [`default_value`] has been set.
[`ArgMatches::value_source`] can be used to check if a value is present at runtime.

</div>

# Panic

If the argument definition and access mismatch.  To handle this case programmatically, see
[`ArgMatches::try_remove_one`].

# Examples

```rust
# use clap_builder as clap;
# use clap::{Command, Arg, value_parser, ArgAction};
let mut m = Command::new("myprog")
.arg(Arg::new("file")
.required(true)
.action(ArgAction::Set))
.get_matches_from(vec![
"myprog", "file.txt",
]);
let vals: String = m.remove_one("file")
.expect("`file`is required");
assert_eq!(vals, "file.txt");
```
[positional]: crate::Arg::index()
[`default_value`]: crate::Arg::default_value()


**Code Examples:**


```rust
# use clap_builder as clap;
# use clap::{Command, Arg, value_parser, ArgAction};
let mut m = Command::new("myprog")
.arg(Arg::new("file")
.required(true)
.action(ArgAction::Set))
.get_matches_from(vec![
"myprog", "file.txt",
]);
let vals: String = m.remove_one("file")
.expect("`file`is required");
assert_eq!(vals, "file.txt");
```


#### Fn: `remove_many` (line 414)

<!-- Source: repos/clap/clap_builder/src/parser/matches/arg_matches.rs:414 -->

<!-- Type: fn -->


Return values of a specific option or positional argument.

i.e. an argument that takes multiple values at runtime.

Returns an error if the wrong type was used.  No item will have been removed.

Returns `None` if the option wasn't present.

# Panic

If the argument definition and access mismatch.  To handle this case programmatically, see
[`ArgMatches::try_remove_many`].

# Examples

```rust
# use clap_builder as clap;
# use clap::{Command, Arg, value_parser, ArgAction};
let mut m = Command::new("myprog")
.arg(Arg::new("file")
.action(ArgAction::Append)
.num_args(1..)
.required(true))
.get_matches_from(vec![
"myprog", "file1.txt", "file2.txt", "file3.txt", "file4.txt",
]);
let vals: Vec<String> = m.remove_many("file")
.expect("`file`is required")
.collect();
assert_eq!(vals, ["file1.txt", "file2.txt", "file3.txt", "file4.txt"]);
```


**Code Examples:**


```rust
# use clap_builder as clap;
# use clap::{Command, Arg, value_parser, ArgAction};
let mut m = Command::new("myprog")
.arg(Arg::new("file")
.action(ArgAction::Append)
.num_args(1..)
.required(true))
.get_matches_from(vec![
"myprog", "file1.txt", "file2.txt", "file3.txt", "file4.txt",
]);
let vals: Vec<String> = m.remove_many("file")
.expect("`file`is required")
.collect();
assert_eq!(vals, ["file1.txt", "file2.txt", "file3.txt", "file4.txt"]);
```


#### Fn: `remove_occurrences` (line 453)

<!-- Source: repos/clap/clap_builder/src/parser/matches/arg_matches.rs:453 -->

<!-- Type: fn -->


Return values for each occurrence of an option.

Each item is itself an iterator containing the arguments passed to a single occurrence of
the option.

If the option doesn't support multiple occurrences, or there was only a single occurrence,
the iterator will only contain a single item.

Returns `None` if the option wasn't present.

# Panic

If the argument definition and access mismatch.  To handle this case programmatically, see
[`ArgMatches::try_remove_occurrences`].

# Examples

```rust
# use clap_builder as clap;
# use clap::{Command, Arg, value_parser, ArgAction};
let mut m = Command::new("myprog")
.arg(Arg::new("x")
.short('x')
.num_args(2)
.action(ArgAction::Append)
.value_parser(value_parser!(String)))
.get_matches_from(vec![
"myprog", "-x", "a", "b", "-x", "c", "d"]);
let vals: Vec<Vec<String>> = m.remove_occurrences("x").unwrap().map(Iterator::collect).collect();
assert_eq!(vals, [["a", "b"], ["c", "d"]]);
```


**Code Examples:**


```rust
# use clap_builder as clap;
# use clap::{Command, Arg, value_parser, ArgAction};
let mut m = Command::new("myprog")
.arg(Arg::new("x")
.short('x')
.num_args(2)
.action(ArgAction::Append)
.value_parser(value_parser!(String)))
.get_matches_from(vec![
"myprog", "-x", "a", "b", "-x", "c", "d"]);
let vals: Vec<Vec<String>> = m.remove_occurrences("x").unwrap().map(Iterator::collect).collect();
assert_eq!(vals, [["a", "b"], ["c", "d"]]);
```


#### Fn: `contains_id` (line 492)

<!-- Source: repos/clap/clap_builder/src/parser/matches/arg_matches.rs:492 -->

<!-- Type: fn -->


Check if values are present for the argument or group id

<div class="warning">

*NOTE:* This will always return `true` if [`default_value`] has been set.
[`ArgMatches::value_source`] can be used to check if a value is present at runtime.

</div>

# Panics

If `id` is not a valid argument or group name (debug builds).  To handle this case programmatically, see
[`ArgMatches::try_contains_id`].

# Examples

```rust
# use clap_builder as clap;
# use clap::{Command, Arg, ArgAction};
let m = Command::new("myprog")
.arg(Arg::new("debug")
.short('d')
.action(ArgAction::SetTrue))
.get_matches_from(vec![
"myprog", "-d"
]);

assert!(m.contains_id("debug"));
```

[`default_value`]: crate::Arg::default_value()


**Code Examples:**


```rust
# use clap_builder as clap;
# use clap::{Command, Arg, ArgAction};
let m = Command::new("myprog")
.arg(Arg::new("debug")
.short('d')
.action(ArgAction::SetTrue))
.get_matches_from(vec![
"myprog", "-d"
]);

assert!(m.contains_id("debug"));
```


#### Fn: `ids` (line 527)

<!-- Source: repos/clap/clap_builder/src/parser/matches/arg_matches.rs:527 -->

<!-- Type: fn -->


Iterate over [`Arg`][crate::Arg] and [`ArgGroup`][crate::ArgGroup] [`Id`]s via [`ArgMatches::ids`].

# Examples

```rust
# use clap_builder as clap;
# use clap::{Command, arg, value_parser};

let m = Command::new("myprog")
.arg(arg!(--color <when>)
.value_parser(["auto", "always", "never"]))
.arg(arg!(--config <path>)
.value_parser(value_parser!(std::path::PathBuf)))
.get_matches_from(["myprog", "--config=config.toml", "--color=auto"]);
assert_eq!(m.ids().len(), 2);
assert_eq!(
m.ids()
.map(|id| id.as_str())
.collect::<Vec<_>>(),
["config", "color"]
);
```


**Code Examples:**


```rust
# use clap_builder as clap;
# use clap::{Command, arg, value_parser};

let m = Command::new("myprog")
.arg(arg!(--color <when>)
.value_parser(["auto", "always", "never"]))
.arg(arg!(--config <path>)
.value_parser(value_parser!(std::path::PathBuf)))
.get_matches_from(["myprog", "--config=config.toml", "--color=auto"]);
assert_eq!(m.ids().len(), 2);
assert_eq!(
m.ids()
.map(|id| id.as_str())
.collect::<Vec<_>>(),
["config", "color"]
);
```


#### Fn: `args_present` (line 555)

<!-- Source: repos/clap/clap_builder/src/parser/matches/arg_matches.rs:555 -->

<!-- Type: fn -->


Check if any [`Arg`][crate::Arg]s were present on the command line

See [`ArgMatches::subcommand_name()`] or [`ArgMatches::subcommand()`] to check if a
subcommand was present on the command line.

# Examples

```rust
# use clap_builder as clap;
# use clap::{Command, Arg, ArgAction};
let mut cmd = Command::new("myapp")
.arg(Arg::new("output")
.action(ArgAction::Set));

let m = cmd
.try_get_matches_from_mut(vec!["myapp", "something"])
.unwrap();
assert!(m.args_present());

let m = cmd
.try_get_matches_from_mut(vec!["myapp"])
.unwrap();
assert!(! m.args_present());


#### Fn: `value_source` (line 584)

<!-- Source: repos/clap/clap_builder/src/parser/matches/arg_matches.rs:584 -->

<!-- Type: fn -->


Report where argument value came from

# Panics

If `id` is not a valid argument or group id (debug builds).

# Examples

```rust
# use clap_builder as clap;
# use clap::{Command, Arg, ArgAction};
# use clap::parser::ValueSource;
let m = Command::new("myprog")
.arg(Arg::new("debug")
.short('d')
.action(ArgAction::SetTrue))
.get_matches_from(vec![
"myprog", "-d"
]);

assert_eq!(m.value_source("debug"), Some(ValueSource::CommandLine));
```

[`default_value`]: crate::Arg::default_value()


**Code Examples:**


```rust
# use clap_builder as clap;
# use clap::{Command, Arg, ArgAction};
# use clap::parser::ValueSource;
let m = Command::new("myprog")
.arg(Arg::new("debug")
.short('d')
.action(ArgAction::SetTrue))
.get_matches_from(vec![
"myprog", "-d"
]);

assert_eq!(m.value_source("debug"), Some(ValueSource::CommandLine));
```


#### Fn: `index_of` (line 615)

<!-- Source: repos/clap/clap_builder/src/parser/matches/arg_matches.rs:615 -->

<!-- Type: fn -->


The first index of that an argument showed up.

Indices are similar to argv indices, but are not exactly 1:1.

For flags (i.e. those arguments which don't have an associated value), indices refer
to occurrence of the switch, such as `-f`, or `--flag`. However, for options the indices
refer to the *values* `-o val` would therefore not represent two distinct indices, only the
index for `val` would be recorded. This is by design.

Besides the flag/option discrepancy, the primary difference between an argv index and clap
index, is that clap continues counting once all arguments have properly separated, whereas
an argv index does not.

The examples should clear this up.

<div class="warning">

*NOTE:* If an argument is allowed multiple times, this method will only give the *first*
index.  See [`ArgMatches::indices_of`].

</div>

# Panics

If `id` is not a valid argument or group id (debug builds).

# Examples

The argv indices are listed in the comments below. See how they correspond to the clap
indices. Note that if it's not listed in a clap index, this is because it's not saved in
in an `ArgMatches` struct for querying.

```rust
# use clap_builder as clap;
# use clap::{Command, Arg, ArgAction};
let m = Command::new("myapp")
.arg(Arg::new("flag")
.short('f')
.action(ArgAction::SetTrue))
.arg(Arg::new("option")
.short('o')
.action(ArgAction::Set))
.get_matches_from(vec!["myapp", "-f", "-o", "val"]);
// ARGV indices: ^0       ^1    ^2    ^3
// clap indices:          ^1          ^3

assert_eq!(m.index_of("flag"), Some(1));
assert_eq!(m.index_of("option"), Some(3));
```

Now notice, if we use one of the other styles of options:

```rust
# use clap_builder as clap;
# use clap::{Command, Arg, ArgAction};
let m = Command::new("myapp")
.arg(Arg::new("flag")
.short('f')
.action(ArgAction::SetTrue))
.arg(Arg::new("option")
.short('o')
.action(ArgAction::Set))
.get_matches_from(vec!["myapp", "-f", "-o=val"]);
// ARGV indices: ^0       ^1    ^2
// clap indices:          ^1       ^3

assert_eq!(m.index_of("flag"), Some(1));
assert_eq!(m.index_of("option"), Some(3));
```

Things become much more complicated, or clear if we look at a more complex combination of
flags. Let's also throw in the final option style for good measure.

```rust
# use clap_builder as clap;
# use clap::{Command, Arg, ArgAction};
let m = Command::new("myapp")
.arg(Arg::new("flag")
.short('f')
.action(ArgAction::SetTrue))
.arg(Arg::new("flag2")
.short('F')
.action(ArgAction::SetTrue))
.arg(Arg::new("flag3")
.short('z')
.action(ArgAction::SetTrue))
.arg(Arg::new("option")
.short('o')
.action(ArgAction::Set))
.get_matches_from(vec!["myapp", "-fzF", "-oval"]);
// ARGV indices: ^0      ^1       ^2
// clap indices:         ^1,2,3    ^5
//
// clap sees the above as 'myapp -f -z -F -o val'
//                         ^0    ^1 ^2 ^3 ^4 ^5
assert_eq!(m.index_of("flag"), Some(1));
assert_eq!(m.index_of("flag2"), Some(3));
assert_eq!(m.index_of("flag3"), Some(2));
assert_eq!(m.index_of("option"), Some(5));
```

One final combination of flags/options to see how they combine:

```rust
# use clap_builder as clap;
# use clap::{Command, Arg, ArgAction};
let m = Command::new("myapp")
.arg(Arg::new("flag")
.short('f')
.action(ArgAction::SetTrue))
.arg(Arg::new("flag2")
.short('F')
.action(ArgAction::SetTrue))
.arg(Arg::new("flag3")
.short('z')
.action(ArgAction::SetTrue))
.arg(Arg::new("option")
.short('o')
.action(ArgAction::Set))
.get_matches_from(vec!["myapp", "-fzFoval"]);
// ARGV indices: ^0       ^1
// clap indices:          ^1,2,3^5
//
// clap sees the above as 'myapp -f -z -F -o val'
//                         ^0    ^1 ^2 ^3 ^4 ^5
assert_eq!(m.index_of("flag"), Some(1));
assert_eq!(m.index_of("flag2"), Some(3));
assert_eq!(m.index_of("flag3"), Some(2));
assert_eq!(m.index_of("option"), Some(5));
```

The last part to mention is when values are sent in multiple groups with a [delimiter].

```rust
# use clap_builder as clap;
# use clap::{Command, Arg};
let m = Command::new("myapp")
.arg(Arg::new("option")
.short('o')
.value_delimiter(',')
.num_args(1..))
.get_matches_from(vec!["myapp", "-o=val1,val2,val3"]);
// ARGV indices: ^0       ^1
// clap indices:             ^2   ^3   ^4
//
// clap sees the above as 'myapp -o val1 val2 val3'
//                         ^0    ^1 ^2   ^3   ^4
assert_eq!(m.index_of("option"), Some(2));
assert_eq!(m.indices_of("option").unwrap().collect::<Vec<_>>(), &[2, 3, 4]);
```
[delimiter]: crate::Arg::value_delimiter()


**Code Examples:**


```rust
# use clap_builder as clap;
# use clap::{Command, Arg, ArgAction};
let m = Command::new("myapp")
.arg(Arg::new("flag")
.short('f')
.action(ArgAction::SetTrue))
.arg(Arg::new("option")
.short('o')
.action(ArgAction::Set))
.get_matches_from(vec!["myapp", "-f", "-o", "val"]);
// ARGV indices: ^0       ^1    ^2    ^3
// clap indices:          ^1          ^3

assert_eq!(m.index_of("flag"), Some(1));
assert_eq!(m.index_of("option"), Some(3));
```


```rust
# use clap_builder as clap;
# use clap::{Command, Arg, ArgAction};
let m = Command::new("myapp")
.arg(Arg::new("flag")
.short('f')
.action(ArgAction::SetTrue))
.arg(Arg::new("option")
.short('o')
.action(ArgAction::Set))
.get_matches_from(vec!["myapp", "-f", "-o=val"]);
// ARGV indices: ^0       ^1    ^2
// clap indices:          ^1       ^3

assert_eq!(m.index_of("flag"), Some(1));
assert_eq!(m.index_of("option"), Some(3));
```


```rust
# use clap_builder as clap;
# use clap::{Command, Arg, ArgAction};
let m = Command::new("myapp")
.arg(Arg::new("flag")
.short('f')
.action(ArgAction::SetTrue))
.arg(Arg::new("flag2")
.short('F')
.action(ArgAction::SetTrue))
.arg(Arg::new("flag3")
.short('z')
.action(ArgAction::SetTrue))
.arg(Arg::new("option")
.short('o')
.action(ArgAction::Set))
.get_matches_from(vec!["myapp", "-fzF", "-oval"]);
// ARGV indices: ^0      ^1       ^2
// clap indices:         ^1,2,3    ^5
//
// clap sees the above as 'myapp -f -z -F -o val'
//                         ^0    ^1 ^2 ^3 ^4 ^5
assert_eq!(m.index_of("flag"), Some(1));
assert_eq!(m.index_of("flag2"), Some(3));
assert_eq!(m.index_of("flag3"), Some(2));
assert_eq!(m.index_of("option"), Some(5));
```


```rust
# use clap_builder as clap;
# use clap::{Command, Arg, ArgAction};
let m = Command::new("myapp")
.arg(Arg::new("flag")
.short('f')
.action(ArgAction::SetTrue))
.arg(Arg::new("flag2")
.short('F')
.action(ArgAction::SetTrue))
.arg(Arg::new("flag3")
.short('z')
.action(ArgAction::SetTrue))
.arg(Arg::new("option")
.short('o')
.action(ArgAction::Set))
.get_matches_from(vec!["myapp", "-fzFoval"]);
// ARGV indices: ^0       ^1
// clap indices:          ^1,2,3^5
//
// clap sees the above as 'myapp -f -z -F -o val'
//                         ^0    ^1 ^2 ^3 ^4 ^5
assert_eq!(m.index_of("flag"), Some(1));
assert_eq!(m.index_of("flag2"), Some(3));
assert_eq!(m.index_of("flag3"), Some(2));
assert_eq!(m.index_of("option"), Some(5));
```


```rust
# use clap_builder as clap;
# use clap::{Command, Arg};
let m = Command::new("myapp")
.arg(Arg::new("option")
.short('o')
.value_delimiter(',')
.num_args(1..))
.get_matches_from(vec!["myapp", "-o=val1,val2,val3"]);
// ARGV indices: ^0       ^1
// clap indices:             ^2   ^3   ^4
//
// clap sees the above as 'myapp -o val1 val2 val3'
//                         ^0    ^1 ^2   ^3   ^4
assert_eq!(m.index_of("option"), Some(2));
assert_eq!(m.indices_of("option").unwrap().collect::<Vec<_>>(), &[2, 3, 4]);
```


#### Fn: `indices_of` (line 773)

<!-- Source: repos/clap/clap_builder/src/parser/matches/arg_matches.rs:773 -->

<!-- Type: fn -->


All indices an argument appeared at when parsing.

Indices are similar to argv indices, but are not exactly 1:1.

For flags (i.e. those arguments which don't have an associated value), indices refer
to occurrence of the switch, such as `-f`, or `--flag`. However, for options the indices
refer to the *values* `-o val` would therefore not represent two distinct indices, only the
index for `val` would be recorded. This is by design.

<div class="warning">

*NOTE:* For more information about how clap indices compared to argv indices, see
[`ArgMatches::index_of`]

</div>

# Panics

If `id` is not a valid argument or group id (debug builds).

# Examples

```rust
# use clap_builder as clap;
# use clap::{Command, Arg};
let m = Command::new("myapp")
.arg(Arg::new("option")
.short('o')
.value_delimiter(','))
.get_matches_from(vec!["myapp", "-o=val1,val2,val3"]);
// ARGV indices: ^0       ^1
// clap indices:             ^2   ^3   ^4
//
// clap sees the above as 'myapp -o val1 val2 val3'
//                         ^0    ^1 ^2   ^3   ^4
assert_eq!(m.indices_of("option").unwrap().collect::<Vec<_>>(), &[2, 3, 4]);
```

Another quick example is when flags and options are used together

```rust
# use clap_builder as clap;
# use clap::{Command, Arg, ArgAction};
let m = Command::new("myapp")
.arg(Arg::new("option")
.short('o')
.action(ArgAction::Set)
.action(ArgAction::Append))
.arg(Arg::new("flag")
.short('f')
.action(ArgAction::Count))
.get_matches_from(vec!["myapp", "-o", "val1", "-f", "-o", "val2", "-f"]);
// ARGV indices: ^0       ^1    ^2      ^3    ^4    ^5      ^6
// clap indices:                ^2      ^3          ^5      ^6

assert_eq!(m.indices_of("option").unwrap().collect::<Vec<_>>(), &[2, 5]);
assert_eq!(m.indices_of("flag").unwrap().collect::<Vec<_>>(), &[6]);
```

One final example, which is an odd case; if we *don't* use  value delimiter as we did with
the first example above instead of `val1`, `val2` and `val3` all being distinc values, they
would all be a single value of `val1,val2,val3`, in which case they'd only receive a single
index.

```rust
# use clap_builder as clap;
# use clap::{Command, Arg, ArgAction};
let m = Command::new("myapp")
.arg(Arg::new("option")
.short('o')
.action(ArgAction::Set)
.num_args(1..))
.get_matches_from(vec!["myapp", "-o=val1,val2,val3"]);
// ARGV indices: ^0       ^1
// clap indices:             ^2
//
// clap sees the above as 'myapp -o "val1,val2,val3"'
//                         ^0    ^1  ^2
assert_eq!(m.indices_of("option").unwrap().collect::<Vec<_>>(), &[2]);
```
[`ArgMatches::index_of`]: ArgMatches::index_of()


**Code Examples:**


```rust
# use clap_builder as clap;
# use clap::{Command, Arg};
let m = Command::new("myapp")
.arg(Arg::new("option")
.short('o')
.value_delimiter(','))
.get_matches_from(vec!["myapp", "-o=val1,val2,val3"]);
// ARGV indices: ^0       ^1
// clap indices:             ^2   ^3   ^4
//
// clap sees the above as 'myapp -o val1 val2 val3'
//                         ^0    ^1 ^2   ^3   ^4
assert_eq!(m.indices_of("option").unwrap().collect::<Vec<_>>(), &[2, 3, 4]);
```


```rust
# use clap_builder as clap;
# use clap::{Command, Arg, ArgAction};
let m = Command::new("myapp")
.arg(Arg::new("option")
.short('o')
.action(ArgAction::Set)
.action(ArgAction::Append))
.arg(Arg::new("flag")
.short('f')
.action(ArgAction::Count))
.get_matches_from(vec!["myapp", "-o", "val1", "-f", "-o", "val2", "-f"]);
// ARGV indices: ^0       ^1    ^2      ^3    ^4    ^5      ^6
// clap indices:                ^2      ^3          ^5      ^6

assert_eq!(m.indices_of("option").unwrap().collect::<Vec<_>>(), &[2, 5]);
assert_eq!(m.indices_of("flag").unwrap().collect::<Vec<_>>(), &[6]);
```


```rust
# use clap_builder as clap;
# use clap::{Command, Arg, ArgAction};
let m = Command::new("myapp")
.arg(Arg::new("option")
.short('o')
.action(ArgAction::Set)
.num_args(1..))
.get_matches_from(vec!["myapp", "-o=val1,val2,val3"]);
// ARGV indices: ^0       ^1
// clap indices:             ^2
//
// clap sees the above as 'myapp -o "val1,val2,val3"'
//                         ^0    ^1  ^2
assert_eq!(m.indices_of("option").unwrap().collect::<Vec<_>>(), &[2]);
```


#### Fn: `try_get_one` (line 1080)

<!-- Source: repos/clap/clap_builder/src/parser/matches/arg_matches.rs:1080 -->

<!-- Type: fn -->


Non-panicking version of [`ArgMatches::get_one`]


#### Fn: `try_get_many` (line 1098)

<!-- Source: repos/clap/clap_builder/src/parser/matches/arg_matches.rs:1098 -->

<!-- Type: fn -->


Non-panicking version of [`ArgMatches::get_many`]


#### Fn: `try_get_occurrences` (line 1117)

<!-- Source: repos/clap/clap_builder/src/parser/matches/arg_matches.rs:1117 -->

<!-- Type: fn -->


Non-panicking version of [`ArgMatches::get_occurrences`]


#### Fn: `try_get_raw` (line 1134)

<!-- Source: repos/clap/clap_builder/src/parser/matches/arg_matches.rs:1134 -->

<!-- Type: fn -->


Non-panicking version of [`ArgMatches::get_raw`]


#### Fn: `try_get_raw_occurrences` (line 1149)

<!-- Source: repos/clap/clap_builder/src/parser/matches/arg_matches.rs:1149 -->

<!-- Type: fn -->


Non-panicking version of [`ArgMatches::get_raw_occurrences`]


#### Fn: `try_remove_one` (line 1167)

<!-- Source: repos/clap/clap_builder/src/parser/matches/arg_matches.rs:1167 -->

<!-- Type: fn -->


Non-panicking version of [`ArgMatches::remove_one`]


#### Fn: `try_remove_many` (line 1182)

<!-- Source: repos/clap/clap_builder/src/parser/matches/arg_matches.rs:1182 -->

<!-- Type: fn -->


Non-panicking version of [`ArgMatches::remove_many`]


#### Fn: `try_remove_occurrences` (line 1201)

<!-- Source: repos/clap/clap_builder/src/parser/matches/arg_matches.rs:1201 -->

<!-- Type: fn -->


Non-panicking version of [`ArgMatches::remove_occurrences`]


#### Fn: `try_contains_id` (line 1219)

<!-- Source: repos/clap/clap_builder/src/parser/matches/arg_matches.rs:1219 -->

<!-- Type: fn -->


Non-panicking version of [`ArgMatches::contains_id`]


#### Fn: `try_clear_id` (line 1227)

<!-- Source: repos/clap/clap_builder/src/parser/matches/arg_matches.rs:1227 -->

<!-- Type: fn -->


Clears the values for the given `id`

Alternative to [`try_remove_*`][ArgMatches::try_remove_one] when the type is not known.

Returns `Err([``MatchesError``])` if the given `id` isn't valid for current `ArgMatches` instance.

Returns `Ok(true)` if there were any matches with the given `id`, `Ok(false)` otherwise.


#### Struct: `IdsRef` (line 1362)

<!-- Source: repos/clap/clap_builder/src/parser/matches/arg_matches.rs:1362 -->

<!-- Type: struct -->


Iterate over [`Arg`][crate::Arg] and [`ArgGroup`][crate::ArgGroup] [`Id`]s via [`ArgMatches::ids`].

# Examples

```rust
# use clap_builder as clap;
# use clap::{Command, arg, value_parser};

let m = Command::new("myprog")
.arg(arg!(--color <when>)
.value_parser(["auto", "always", "never"]))
.arg(arg!(--config <path>)
.value_parser(value_parser!(std::path::PathBuf)))
.get_matches_from(["myprog", "--config=config.toml", "--color=auto"]);
assert_eq!(
m.ids()
.map(|id| id.as_str())
.collect::<Vec<_>>(),
["config", "color"]
);
```


**Code Examples:**


```rust
# use clap_builder as clap;
# use clap::{Command, arg, value_parser};

let m = Command::new("myprog")
.arg(arg!(--color <when>)
.value_parser(["auto", "always", "never"]))
.arg(arg!(--config <path>)
.value_parser(value_parser!(std::path::PathBuf)))
.get_matches_from(["myprog", "--config=config.toml", "--color=auto"]);
assert_eq!(
m.ids()
.map(|id| id.as_str())
.collect::<Vec<_>>(),
["config", "color"]
);
```


#### Struct: `Values` (line 1407)

<!-- Source: repos/clap/clap_builder/src/parser/matches/arg_matches.rs:1407 -->

<!-- Type: struct -->


Iterate over multiple values for an argument via [`ArgMatches::remove_many`].

# Examples

```rust
# use clap_builder as clap;
# use clap::{Command, Arg, ArgAction};
let mut m = Command::new("myapp")
.arg(Arg::new("output")
.short('o')
.action(ArgAction::Append))
.get_matches_from(vec!["myapp", "-o", "val1", "-o", "val2"]);

let mut values = m.remove_many::<String>("output")
.unwrap();

assert_eq!(values.next(), Some(String::from("val1")));
assert_eq!(values.next(), Some(String::from("val2")));
assert_eq!(values.next(), None);
```


**Code Examples:**


```rust
# use clap_builder as clap;
# use clap::{Command, Arg, ArgAction};
let mut m = Command::new("myapp")
.arg(Arg::new("output")
.short('o')
.action(ArgAction::Append))
.get_matches_from(vec!["myapp", "-o", "val1", "-o", "val2"]);

let mut values = m.remove_many::<String>("output")
.unwrap();

assert_eq!(values.next(), Some(String::from("val1")));
assert_eq!(values.next(), Some(String::from("val2")));
assert_eq!(values.next(), None);
```


#### Impl: `Default` (line 1463)

<!-- Source: repos/clap/clap_builder/src/parser/matches/arg_matches.rs:1463 -->

<!-- Type: impl -->


Creates an empty iterator.


#### Struct: `ValuesRef` (line 1474)

<!-- Source: repos/clap/clap_builder/src/parser/matches/arg_matches.rs:1474 -->

<!-- Type: struct -->


Iterate over multiple values for an argument via [`ArgMatches::get_many`].

# Examples

```rust
# use clap_builder as clap;
# use clap::{Command, Arg, ArgAction};
let m = Command::new("myapp")
.arg(Arg::new("output")
.short('o')
.action(ArgAction::Append))
.get_matches_from(vec!["myapp", "-o", "val1", "-o", "val2"]);

let mut values = m.get_many::<String>("output")
.unwrap()
.map(|s| s.as_str());

assert_eq!(values.next(), Some("val1"));
assert_eq!(values.next(), Some("val2"));
assert_eq!(values.next(), None);
```


**Code Examples:**


```rust
# use clap_builder as clap;
# use clap::{Command, Arg, ArgAction};
let m = Command::new("myapp")
.arg(Arg::new("output")
.short('o')
.action(ArgAction::Append))
.get_matches_from(vec!["myapp", "-o", "val1", "-o", "val2"]);

let mut values = m.get_many::<String>("output")
.unwrap()
.map(|s| s.as_str());

assert_eq!(values.next(), Some("val1"));
assert_eq!(values.next(), Some("val2"));
assert_eq!(values.next(), None);
```


#### Impl: `Default` (line 1531)

<!-- Source: repos/clap/clap_builder/src/parser/matches/arg_matches.rs:1531 -->

<!-- Type: impl -->


Creates an empty iterator.


#### Struct: `RawValues` (line 1542)

<!-- Source: repos/clap/clap_builder/src/parser/matches/arg_matches.rs:1542 -->

<!-- Type: struct -->


Iterate over raw argument values via [`ArgMatches::get_raw`].

# Examples

```rust
# #[cfg(unix)] {
# use clap_builder as clap;
# use clap::{Command, arg, value_parser};
use std::ffi::OsString;
use std::os::unix::ffi::{OsStrExt,OsStringExt};

let m = Command::new("utf8")
.arg(arg!(<arg> "some arg")
.value_parser(value_parser!(OsString)))
.get_matches_from(vec![OsString::from("myprog"),
// "Hi {0xe9}!"
OsString::from_vec(vec![b'H', b'i', b' ', 0xe9, b'!'])]);
assert_eq!(
&*m.get_raw("arg")
.unwrap()
.next().unwrap()
.as_bytes(),
[b'H', b'i', b' ', 0xe9, b'!']
);
# }
```


**Code Examples:**


```rust
# #[cfg(unix)] {
# use clap_builder as clap;
# use clap::{Command, arg, value_parser};
use std::ffi::OsString;
use std::os::unix::ffi::{OsStrExt,OsStringExt};

let m = Command::new("utf8")
.arg(arg!(<arg> "some arg")
.value_parser(value_parser!(OsString)))
.get_matches_from(vec![OsString::from("myprog"),
// "Hi {0xe9}!"
OsString::from_vec(vec![b'H', b'i', b' ', 0xe9, b'!'])]);
assert_eq!(
&*m.get_raw("arg")
.unwrap()
.next().unwrap()
.as_bytes(),
[b'H', b'i', b' ', 0xe9, b'!']
);
# }
```


#### Impl: `Default` (line 1604)

<!-- Source: repos/clap/clap_builder/src/parser/matches/arg_matches.rs:1604 -->

<!-- Type: impl -->


Creates an empty iterator.


#### Struct: `Indices` (line 1820)

<!-- Source: repos/clap/clap_builder/src/parser/matches/arg_matches.rs:1820 -->

<!-- Type: struct -->


Iterate over indices for where an argument appeared when parsing, via [`ArgMatches::indices_of`]

# Examples

```rust
# use clap_builder as clap;
# use clap::{Command, Arg, ArgAction};
let m = Command::new("myapp")
.arg(Arg::new("output")
.short('o')
.num_args(1..)
.action(ArgAction::Set))
.get_matches_from(vec!["myapp", "-o", "val1", "val2"]);

let mut indices = m.indices_of("output").unwrap();

assert_eq!(indices.next(), Some(2));
assert_eq!(indices.next(), Some(3));
assert_eq!(indices.next(), None);
```
[`ArgMatches::indices_of`]: ArgMatches::indices_of()


**Code Examples:**


```rust
# use clap_builder as clap;
# use clap::{Command, Arg, ArgAction};
let m = Command::new("myapp")
.arg(Arg::new("output")
.short('o')
.num_args(1..)
.action(ArgAction::Set))
.get_matches_from(vec!["myapp", "-o", "val1", "val2"]);

let mut indices = m.indices_of("output").unwrap();

assert_eq!(indices.next(), Some(2));
assert_eq!(indices.next(), Some(3));
assert_eq!(indices.next(), None);
```


#### Impl: `Default` (line 1876)

<!-- Source: repos/clap/clap_builder/src/parser/matches/arg_matches.rs:1876 -->

<!-- Type: impl -->


Creates an empty iterator.


### From `repos/clap/clap_complete/src/engine/custom.rs`


#### Struct: `ArgValueCompleter` (line 11)

<!-- Source: repos/clap/clap_complete/src/engine/custom.rs:11 -->

<!-- Type: struct -->


Extend [`Arg`][clap::Arg] with a completer

# Example

```rust
use clap::Parser;
use clap_complete::engine::{ArgValueCompleter, CompletionCandidate};

fn custom_completer(current: &std::ffi::OsStr) -> Vec<CompletionCandidate> {
let mut completions = vec![];
let Some(current) = current.to_str() else {
return completions;
};

if "foo".starts_with(current) {
completions.push(CompletionCandidate::new("foo"));
}
if "bar".starts_with(current) {
completions.push(CompletionCandidate::new("bar"));
}
if "baz".starts_with(current) {
completions.push(CompletionCandidate::new("baz"));
}
completions
}

#[derive(Debug, Parser)]
struct Cli {
#[arg(long, add = ArgValueCompleter::new(custom_completer))]
custom: Option<String>,
}
```


**Code Examples:**


```rust
use clap::Parser;
use clap_complete::engine::{ArgValueCompleter, CompletionCandidate};

fn custom_completer(current: &std::ffi::OsStr) -> Vec<CompletionCandidate> {
let mut completions = vec![];
let Some(current) = current.to_str() else {
return completions;
};

if "foo".starts_with(current) {
completions.push(CompletionCandidate::new("foo"));
}
if "bar".starts_with(current) {
completions.push(CompletionCandidate::new("bar"));
}
if "baz".starts_with(current) {
completions.push(CompletionCandidate::new("baz"));
}
completions
}

#[derive(Debug, Parser)]
struct Cli {
#[arg(long, add = ArgValueCompleter::new(custom_completer))]
custom: Option<String>,
}
```


#### Struct: `ArgValueCandidates` (line 90)

<!-- Source: repos/clap/clap_complete/src/engine/custom.rs:90 -->

<!-- Type: struct -->


Extend [`Arg`][clap::Arg] with a [`ValueCandidates`]

# Example

```rust
use clap::Parser;
use clap_complete::engine::{ArgValueCandidates, CompletionCandidate};

#[derive(Debug, Parser)]
struct Cli {
#[arg(long, add = ArgValueCandidates::new(|| { vec![
CompletionCandidate::new("foo"),
CompletionCandidate::new("bar"),
CompletionCandidate::new("baz")] }))]
custom: Option<String>,
}
```


**Code Examples:**


```rust
use clap::Parser;
use clap_complete::engine::{ArgValueCandidates, CompletionCandidate};

#[derive(Debug, Parser)]
struct Cli {
#[arg(long, add = ArgValueCandidates::new(|| { vec![
CompletionCandidate::new("foo"),
CompletionCandidate::new("bar"),
CompletionCandidate::new("baz")] }))]
custom: Option<String>,
}
```


### From `repos/clap/src/_cookbook/cargo_example.rs`


#### Module: `cargo_example` (line 1)

<!-- Source: repos/clap/src/_cookbook/cargo_example.rs:1 -->

<!-- Type: module -->


# Example: cargo subcommand (Builder API)

```rust


### From `repos/clap/src/_cookbook/cargo_example_derive.rs`


#### Module: `cargo_example_derive` (line 1)

<!-- Source: repos/clap/src/_cookbook/cargo_example_derive.rs:1 -->

<!-- Type: module -->


# Example: cargo subcommand (Derive API)

```rust


---


## 3. Argument Matching (ArgMatches) {#arg_matches}


### From `repos/clap/clap_builder/src/parser/matches/arg_matches.rs`


#### Struct: `ArgMatches` (line 20)

<!-- Source: repos/clap/clap_builder/src/parser/matches/arg_matches.rs:20 -->

<!-- Type: struct -->


Container for parse results.

Used to get information about the arguments that were supplied to the program at runtime by
the user. New instances of this struct are obtained by using the [`Command::get_matches`] family of
methods.

# Examples

```no_run
# use clap_builder as clap;
# use clap::{Command, Arg, ArgAction};
# use clap::parser::ValueSource;
let matches = Command::new("MyApp")
.arg(Arg::new("out")
.long("output")
.required(true)
.action(ArgAction::Set)
.default_value("-"))
.arg(Arg::new("cfg")
.short('c')
.action(ArgAction::Set))
.get_matches(); // builds the instance of ArgMatches

// to get information about the "cfg" argument we created, such as the value supplied we use
// various ArgMatches methods, such as [ArgMatches::get_one]
if let Some(c) = matches.get_one::<String>("cfg") {
println!("Value for -c: {c}");
}

// The ArgMatches::get_one method returns an Option because the user may not have supplied
// that argument at runtime. But if we specified that the argument was "required" as we did
// with the "out" argument, we can safely unwrap because `clap` verifies that was actually
// used at runtime.
println!("Value for --output: {}", matches.get_one::<String>("out").unwrap());

// You can check the presence of an argument's values
if matches.contains_id("out") {
// However, if you want to know where the value came from
if matches.value_source("out").expect("checked contains_id") == ValueSource::CommandLine {
println!("`out` set by user");
} else {
println!("`out` is defaulted");
}
}
```
[`Command::get_matches`]: crate::Command::get_matches()


**Code Examples:**


```rust
# use clap_builder as clap;
# use clap::{Command, Arg, ArgAction};
# use clap::parser::ValueSource;
let matches = Command::new("MyApp")
.arg(Arg::new("out")
.long("output")
.required(true)
.action(ArgAction::Set)
.default_value("-"))
.arg(Arg::new("cfg")
.short('c')
.action(ArgAction::Set))
.get_matches(); // builds the instance of ArgMatches

// to get information about the "cfg" argument we created, such as the value supplied we use
// various ArgMatches methods, such as [ArgMatches::get_one]
if let Some(c) = matches.get_one::<String>("cfg") {
println!("Value for -c: {c}");
}

// The ArgMatches::get_one method returns an Option because the user may not have supplied
// that argument at runtime. But if we specified that the argument was "required" as we did
// with the "out" argument, we can safely unwrap because `clap` verifies that was actually
// used at runtime.
println!("Value for --output: {}", matches.get_one::<String>("out").unwrap());

// You can check the presence of an argument's values
if matches.contains_id("out") {
// However, if you want to know where the value came from
if matches.value_source("out").expect("checked contains_id") == ValueSource::CommandLine {
println!("`out` set by user");
} else {
println!("`out` is defaulted");
}
}
```


#### Impl: `ArgMatches` (line 76)

<!-- Source: repos/clap/clap_builder/src/parser/matches/arg_matches.rs:76 -->

<!-- Type: impl -->


# Arguments


#### Impl: `ArgMatches` (line 865)

<!-- Source: repos/clap/clap_builder/src/parser/matches/arg_matches.rs:865 -->

<!-- Type: impl -->


# Subcommands


#### Impl: `ArgMatches` (line 1078)

<!-- Source: repos/clap/clap_builder/src/parser/matches/arg_matches.rs:1078 -->

<!-- Type: impl -->


# Advanced


---


## 4. Value Parsers {#value_parsers}


### From `repos/clap/clap_builder/src/builder/possible_value.rs`


#### Struct: `PossibleValue` (line 6)

<!-- Source: repos/clap/clap_builder/src/builder/possible_value.rs:6 -->

<!-- Type: struct -->


A possible value of an argument.

This is used for specifying [possible values] of [Args].

See also [`PossibleValuesParser`][crate::builder::PossibleValuesParser]

<div class="warning">

**NOTE:** Most likely you can use strings, rather than `PossibleValue` as it is only required
to [hide] single values from help messages and shell completions or to attach [help] to
possible values.

</div>

# Examples

```rust
# use clap_builder as clap;
# use clap::{Arg, builder::PossibleValue, ArgAction};
let cfg = Arg::new("config")
.action(ArgAction::Set)
.value_name("FILE")
.value_parser([
PossibleValue::new("fast"),
PossibleValue::new("slow").help("slower than fast"),
PossibleValue::new("secret speed").hide(true)
]);
```

[Args]: crate::Arg
[possible values]: crate::builder::ValueParser::possible_values
[hide]: PossibleValue::hide()
[help]: PossibleValue::help()


**Code Examples:**


```rust
# use clap_builder as clap;
# use clap::{Arg, builder::PossibleValue, ArgAction};
let cfg = Arg::new("config")
.action(ArgAction::Set)
.value_name("FILE")
.value_parser([
PossibleValue::new("fast"),
PossibleValue::new("slow").help("slower than fast"),
PossibleValue::new("secret speed").hide(true)
]);
```


#### Fn: `new` (line 48)

<!-- Source: repos/clap/clap_builder/src/builder/possible_value.rs:48 -->

<!-- Type: fn -->


Create a [`PossibleValue`] with its name.

The name will be used to decide whether this value was provided by the user to an argument.

<div class="warning">

**NOTE:** In case it is not [hidden] it will also be shown in help messages for arguments
that use it as a [possible value] and have not hidden them through [`Arg::hide_possible_values(true)`].

</div>

# Examples

```rust
# use clap_builder as clap;
# use clap::builder::PossibleValue;
PossibleValue::new("fast")
# ;
```
[hidden]: PossibleValue::hide
[possible value]: crate::builder::PossibleValuesParser
[`Arg::hide_possible_values(true)`]: crate::Arg::hide_possible_values()


**Code Examples:**


```rust
# use clap_builder as clap;
# use clap::builder::PossibleValue;
PossibleValue::new("fast")
# ;
```


#### Fn: `help` (line 77)

<!-- Source: repos/clap/clap_builder/src/builder/possible_value.rs:77 -->

<!-- Type: fn -->


Sets the help description of the value.

This is typically displayed in completions (where supported) and should be a short, one-line
description.

# Examples

```rust
# use clap_builder as clap;
# use clap::builder::PossibleValue;
PossibleValue::new("slow")
.help("not fast")
# ;
```


**Code Examples:**


```rust
# use clap_builder as clap;
# use clap::builder::PossibleValue;
PossibleValue::new("slow")
.help("not fast")
# ;
```


#### Fn: `hide` (line 98)

<!-- Source: repos/clap/clap_builder/src/builder/possible_value.rs:98 -->

<!-- Type: fn -->


Hides this value from help and shell completions.

This is an alternative to hiding through [`Arg::hide_possible_values(true)`], if you only
want to hide some values.

# Examples

```rust
# use clap_builder as clap;
# use clap::builder::PossibleValue;
PossibleValue::new("secret")
.hide(true)
# ;
```
[`Arg::hide_possible_values(true)`]: crate::Arg::hide_possible_values()


**Code Examples:**


```rust
# use clap_builder as clap;
# use clap::builder::PossibleValue;
PossibleValue::new("secret")
.hide(true)
# ;
```


#### Fn: `alias` (line 120)

<!-- Source: repos/clap/clap_builder/src/builder/possible_value.rs:120 -->

<!-- Type: fn -->


Sets a *hidden* alias for this argument value.

# Examples

```rust
# use clap_builder as clap;
# use clap::builder::PossibleValue;
PossibleValue::new("slow")
.alias("not-fast")
# ;
```


**Code Examples:**


```rust
# use clap_builder as clap;
# use clap::builder::PossibleValue;
PossibleValue::new("slow")
.alias("not-fast")
# ;
```


#### Fn: `aliases` (line 141)

<!-- Source: repos/clap/clap_builder/src/builder/possible_value.rs:141 -->

<!-- Type: fn -->


Sets multiple *hidden* aliases for this argument value.

# Examples

```rust
# use clap_builder as clap;
# use clap::builder::PossibleValue;
PossibleValue::new("slow")
.aliases(["not-fast", "snake-like"])
# ;
```


**Code Examples:**


```rust
# use clap_builder as clap;
# use clap::builder::PossibleValue;
PossibleValue::new("slow")
.aliases(["not-fast", "snake-like"])
# ;
```


#### Impl: `PossibleValue` (line 159)

<!-- Source: repos/clap/clap_builder/src/builder/possible_value.rs:159 -->

<!-- Type: impl -->


Reflection


#### Fn: `get_name` (line 161)

<!-- Source: repos/clap/clap_builder/src/builder/possible_value.rs:161 -->

<!-- Type: fn -->


Get the name of the argument value


#### Fn: `get_help` (line 167)

<!-- Source: repos/clap/clap_builder/src/builder/possible_value.rs:167 -->

<!-- Type: fn -->


Get the help specified for this argument, if any


#### Fn: `is_hide_set` (line 173)

<!-- Source: repos/clap/clap_builder/src/builder/possible_value.rs:173 -->

<!-- Type: fn -->


Report if [`PossibleValue::hide`] is set


#### Fn: `should_show_help` (line 179)

<!-- Source: repos/clap/clap_builder/src/builder/possible_value.rs:179 -->

<!-- Type: fn -->


Report if `PossibleValue` is not hidden and has a help message


#### Fn: `get_visible_quoted_name` (line 184)

<!-- Source: repos/clap/clap_builder/src/builder/possible_value.rs:184 -->

<!-- Type: fn -->


Get the name if argument value is not hidden, `None` otherwise,
but wrapped in quotes if it contains whitespace


#### Fn: `get_name_and_aliases` (line 199)

<!-- Source: repos/clap/clap_builder/src/builder/possible_value.rs:199 -->

<!-- Type: fn -->


Returns all valid values of the argument value.

Namely the name and all aliases.


#### Fn: `matches` (line 206)

<!-- Source: repos/clap/clap_builder/src/builder/possible_value.rs:206 -->

<!-- Type: fn -->


Tests if the value is valid for this argument value

The value is valid if it is either the name or one of the aliases.

# Examples

```rust
# use clap_builder as clap;
# use clap::builder::PossibleValue;
let arg_value = PossibleValue::new("fast").alias("not-slow");

assert!(arg_value.matches("fast", false));
assert!(arg_value.matches("not-slow", false));

assert!(arg_value.matches("FAST", true));
assert!(!arg_value.matches("FAST", false));
```


**Code Examples:**


```rust
# use clap_builder as clap;
# use clap::builder::PossibleValue;
let arg_value = PossibleValue::new("fast").alias("not-slow");

assert!(arg_value.matches("fast", false));
assert!(arg_value.matches("not-slow", false));

assert!(arg_value.matches("FAST", true));
assert!(!arg_value.matches("FAST", false));
```


### From `repos/clap/clap_builder/src/builder/value_hint.rs`


#### Enum: `ValueHint` (line 3)

<!-- Source: repos/clap/clap_builder/src/builder/value_hint.rs:3 -->

<!-- Type: enum -->


Provide shell with hint on how to complete an argument.

See [`Arg::value_hint`][crate::Arg::value_hint] to set this on an argument.

See the `clap_complete` crate for completion script generation.

Overview of which hints are supported by which shell:

| Hint                   | zsh | fish[^1] | dynamic |
| ---------------------- | --- | ---------|---------|
| `AnyPath`              | Yes | Yes      | Yes     |
| `FilePath`             | Yes | Yes      | Yes     |
| `DirPath`              | Yes | Yes      | Yes     |
| `ExecutablePath`       | Yes | Partial  | Yes     |
| `CommandName`          | Yes | Yes      | No      |
| `CommandString`        | Yes | Partial  | No      |
| `CommandWithArguments` | Yes |          | No      |
| `Username`             | Yes | Yes      | No      |
| `Hostname`             | Yes | Yes      | No      |
| `Url`                  | Yes |          | No      |
| `EmailAddress`         | Yes |          | No      |

[^1]: fish completions currently only support named arguments (e.g. -o or --opt), not
positional arguments.


### From `repos/clap/clap_builder/src/builder/value_parser.rs`


#### Struct: `ValueParser` (line 10)

<!-- Source: repos/clap/clap_builder/src/builder/value_parser.rs:10 -->

<!-- Type: struct -->


Parse/validate argument values

Specified with [`Arg::value_parser`][crate::Arg::value_parser].

`ValueParser` defines how to convert a raw argument value into a validated and typed value for
use within an application.

See
- [`value_parser!`][crate::value_parser] for automatically selecting an implementation for a given type
- [`ValueParser::new`] for additional [`TypedValueParser`] that can be used

# Example

```rust
# use clap_builder as clap;
let mut cmd = clap::Command::new("raw")
.arg(
clap::Arg::new("color")
.long("color")
.value_parser(["always", "auto", "never"])
.default_value("auto")
)
.arg(
clap::Arg::new("hostname")
.long("hostname")
.value_parser(clap::builder::NonEmptyStringValueParser::new())
.action(clap::ArgAction::Set)
.required(true)
)
.arg(
clap::Arg::new("port")
.long("port")
.value_parser(clap::value_parser!(u16).range(3000..))
.action(clap::ArgAction::Set)
.required(true)
);

let m = cmd.try_get_matches_from_mut(
["cmd", "--hostname", "rust-lang.org", "--port", "3001"]
).unwrap();

let color: &String = m.get_one("color")
.expect("default");
assert_eq!(color, "auto");

let hostname: &String = m.get_one("hostname")
.expect("required");
assert_eq!(hostname, "rust-lang.org");

let port: u16 = *m.get_one("port")
.expect("required");
assert_eq!(port, 3001);
```


**Code Examples:**


```rust
# use clap_builder as clap;
let mut cmd = clap::Command::new("raw")
.arg(
clap::Arg::new("color")
.long("color")
.value_parser(["always", "auto", "never"])
.default_value("auto")
)
.arg(
clap::Arg::new("hostname")
.long("hostname")
.value_parser(clap::builder::NonEmptyStringValueParser::new())
.action(clap::ArgAction::Set)
.required(true)
)
.arg(
clap::Arg::new("port")
.long("port")
.value_parser(clap::value_parser!(u16).range(3000..))
.action(clap::ArgAction::Set)
.required(true)
);

let m = cmd.try_get_matches_from_mut(
["cmd", "--hostname", "rust-lang.org", "--port", "3001"]
).unwrap();

let color: &String = m.get_one("color")
.expect("default");
assert_eq!(color, "auto");

let hostname: &String = m.get_one("hostname")
.expect("required");
assert_eq!(hostname, "rust-lang.org");

let port: u16 = *m.get_one("port")
.expect("required");
assert_eq!(port, 3001);
```


#### Fn: `new` (line 78)

<!-- Source: repos/clap/clap_builder/src/builder/value_parser.rs:78 -->

<!-- Type: fn -->


Custom parser for argument values

Pre-existing [`TypedValueParser`] implementations include:
- `Fn(&str) -> Result<T, E>`
- [`EnumValueParser`] and  [`PossibleValuesParser`] for static enumerated values
- [`BoolishValueParser`] and [`FalseyValueParser`] for alternative `bool` implementations
- [`RangedI64ValueParser`] and [`RangedU64ValueParser`]
- [`NonEmptyStringValueParser`]

# Example

```rust
# use clap_builder as clap;
type EnvVar = (String, Option<String>);
fn parse_env_var(env: &str) -> Result<EnvVar, std::io::Error> {
if let Some((var, value)) = env.split_once('=') {
Ok((var.to_owned(), Some(value.to_owned())))
} else {
Ok((env.to_owned(), None))
}
}

let mut cmd = clap::Command::new("raw")
.arg(
clap::Arg::new("env")
.value_parser(clap::builder::ValueParser::new(parse_env_var))
.required(true)
);

let m = cmd.try_get_matches_from_mut(["cmd", "key=value"]).unwrap();
let port: &EnvVar = m.get_one("env")
.expect("required");
assert_eq!(*port, ("key".into(), Some("value".into())));
```


**Code Examples:**


```rust
# use clap_builder as clap;
type EnvVar = (String, Option<String>);
fn parse_env_var(env: &str) -> Result<EnvVar, std::io::Error> {
if let Some((var, value)) = env.split_once('=') {
Ok((var.to_owned(), Some(value.to_owned())))
} else {
Ok((env.to_owned(), None))
}
}

let mut cmd = clap::Command::new("raw")
.arg(
clap::Arg::new("env")
.value_parser(clap::builder::ValueParser::new(parse_env_var))
.required(true)
);

let m = cmd.try_get_matches_from_mut(["cmd", "key=value"]).unwrap();
let port: &EnvVar = m.get_one("env")
.expect("required");
assert_eq!(*port, ("key".into(), Some("value".into())));
```


#### Fn: `bool` (line 119)

<!-- Source: repos/clap/clap_builder/src/builder/value_parser.rs:119 -->

<!-- Type: fn -->


[`bool`] parser for argument values

See also:
- [`BoolishValueParser`] for different human readable bool representations
- [`FalseyValueParser`] for assuming non-false is true

# Example

```rust
# use clap_builder as clap;
let mut cmd = clap::Command::new("raw")
.arg(
clap::Arg::new("download")
.value_parser(clap::value_parser!(bool))
.required(true)
);

let m = cmd.try_get_matches_from_mut(["cmd", "true"]).unwrap();
let port: bool = *m.get_one("download")
.expect("required");
assert_eq!(port, true);

assert!(cmd.try_get_matches_from_mut(["cmd", "forever"]).is_err());
```


**Code Examples:**


```rust
# use clap_builder as clap;
let mut cmd = clap::Command::new("raw")
.arg(
clap::Arg::new("download")
.value_parser(clap::value_parser!(bool))
.required(true)
);

let m = cmd.try_get_matches_from_mut(["cmd", "true"]).unwrap();
let port: bool = *m.get_one("download")
.expect("required");
assert_eq!(port, true);

assert!(cmd.try_get_matches_from_mut(["cmd", "forever"]).is_err());
```


#### Fn: `string` (line 147)

<!-- Source: repos/clap/clap_builder/src/builder/value_parser.rs:147 -->

<!-- Type: fn -->


[`String`] parser for argument values

See also:
- [`NonEmptyStringValueParser`]

# Example

```rust
# use clap_builder as clap;
let mut cmd = clap::Command::new("raw")
.arg(
clap::Arg::new("port")
.value_parser(clap::value_parser!(String))
.required(true)
);

let m = cmd.try_get_matches_from_mut(["cmd", "80"]).unwrap();
let port: &String = m.get_one("port")
.expect("required");
assert_eq!(port, "80");
```


**Code Examples:**


```rust
# use clap_builder as clap;
let mut cmd = clap::Command::new("raw")
.arg(
clap::Arg::new("port")
.value_parser(clap::value_parser!(String))
.required(true)
);

let m = cmd.try_get_matches_from_mut(["cmd", "80"]).unwrap();
let port: &String = m.get_one("port")
.expect("required");
assert_eq!(port, "80");
```


#### Fn: `os_string` (line 172)

<!-- Source: repos/clap/clap_builder/src/builder/value_parser.rs:172 -->

<!-- Type: fn -->


[`OsString`][std::ffi::OsString] parser for argument values

# Example

```rust
# #[cfg(unix)] {
# use clap_builder as clap;
# use clap::{Command, Arg, builder::ValueParser};
use std::ffi::OsString;
use std::os::unix::ffi::{OsStrExt,OsStringExt};
let r = Command::new("myprog")
.arg(
Arg::new("arg")
.required(true)
.value_parser(ValueParser::os_string())
)
.try_get_matches_from(vec![
OsString::from("myprog"),
OsString::from_vec(vec![0xe9])
]);

assert!(r.is_ok());
let m = r.unwrap();
let arg: &OsString = m.get_one("arg")
.expect("required");
assert_eq!(arg.as_bytes(), &[0xe9]);
# }
```


**Code Examples:**


```rust
# #[cfg(unix)] {
# use clap_builder as clap;
# use clap::{Command, Arg, builder::ValueParser};
use std::ffi::OsString;
use std::os::unix::ffi::{OsStrExt,OsStringExt};
let r = Command::new("myprog")
.arg(
Arg::new("arg")
.required(true)
.value_parser(ValueParser::os_string())
)
.try_get_matches_from(vec![
OsString::from("myprog"),
OsString::from_vec(vec![0xe9])
]);

assert!(r.is_ok());
let m = r.unwrap();
let arg: &OsString = m.get_one("arg")
.expect("required");
assert_eq!(arg.as_bytes(), &[0xe9]);
# }
```


#### Fn: `path_buf` (line 204)

<!-- Source: repos/clap/clap_builder/src/builder/value_parser.rs:204 -->

<!-- Type: fn -->


[`PathBuf`][std::path::PathBuf] parser for argument values

# Example

```rust
# use clap_builder as clap;
# use std::path::PathBuf;
# use std::path::Path;
let mut cmd = clap::Command::new("raw")
.arg(
clap::Arg::new("output")
.value_parser(clap::value_parser!(PathBuf))
.required(true)
);

let m = cmd.try_get_matches_from_mut(["cmd", "hello.txt"]).unwrap();
let port: &PathBuf = m.get_one("output")
.expect("required");
assert_eq!(port, Path::new("hello.txt"));

assert!(cmd.try_get_matches_from_mut(["cmd", ""]).is_err());
```


**Code Examples:**


```rust
# use clap_builder as clap;
# use std::path::PathBuf;
# use std::path::Path;
let mut cmd = clap::Command::new("raw")
.arg(
clap::Arg::new("output")
.value_parser(clap::value_parser!(PathBuf))
.required(true)
);

let m = cmd.try_get_matches_from_mut(["cmd", "hello.txt"]).unwrap();
let port: &PathBuf = m.get_one("output")
.expect("required");
assert_eq!(port, Path::new("hello.txt"));

assert!(cmd.try_get_matches_from_mut(["cmd", ""]).is_err());
```


#### Fn: `parse_ref` (line 232)

<!-- Source: repos/clap/clap_builder/src/builder/value_parser.rs:232 -->

<!-- Type: fn -->


Parse into a `AnyValue`

When `arg` is `None`, an external subcommand value is being parsed.


#### Fn: `type_id` (line 245)

<!-- Source: repos/clap/clap_builder/src/builder/value_parser.rs:245 -->

<!-- Type: fn -->


Describes the content of `AnyValue`


#### Fn: `possible_values` (line 250)

<!-- Source: repos/clap/clap_builder/src/builder/value_parser.rs:250 -->

<!-- Type: fn -->


Reflect on enumerated value properties

Error checking should not be done with this; it is mostly targeted at user-facing
applications like errors and completion.


#### Impl: `From` (line 271)

<!-- Source: repos/clap/clap_builder/src/builder/value_parser.rs:271 -->

<!-- Type: impl -->


Convert a [`TypedValueParser`] to [`ValueParser`]

# Example

```rust
# use clap_builder as clap;
let mut cmd = clap::Command::new("raw")
.arg(
clap::Arg::new("hostname")
.long("hostname")
.value_parser(clap::builder::NonEmptyStringValueParser::new())
.action(clap::ArgAction::Set)
.required(true)
);

let m = cmd.try_get_matches_from_mut(
["cmd", "--hostname", "rust-lang.org"]
).unwrap();

let hostname: &String = m.get_one("hostname")
.expect("required");
assert_eq!(hostname, "rust-lang.org");
```


**Code Examples:**


```rust
# use clap_builder as clap;
let mut cmd = clap::Command::new("raw")
.arg(
clap::Arg::new("hostname")
.long("hostname")
.value_parser(clap::builder::NonEmptyStringValueParser::new())
.action(clap::ArgAction::Set)
.required(true)
);

let m = cmd.try_get_matches_from_mut(
["cmd", "--hostname", "rust-lang.org"]
).unwrap();

let hostname: &String = m.get_one("hostname")
.expect("required");
assert_eq!(hostname, "rust-lang.org");
```


#### Impl: `From` (line 309)

<!-- Source: repos/clap/clap_builder/src/builder/value_parser.rs:309 -->

<!-- Type: impl -->


Create an `i64` [`ValueParser`] from a `N..M` range

See [`RangedI64ValueParser`] for more control over the output type.

See also [`RangedU64ValueParser`]

# Examples

```rust
# use clap_builder as clap;
let mut cmd = clap::Command::new("raw")
.arg(
clap::Arg::new("port")
.long("port")
.value_parser(3000..4000)
.action(clap::ArgAction::Set)
.required(true)
);

let m = cmd.try_get_matches_from_mut(["cmd", "--port", "3001"]).unwrap();
let port: i64 = *m.get_one("port")
.expect("required");
assert_eq!(port, 3001);
```


**Code Examples:**


```rust
# use clap_builder as clap;
let mut cmd = clap::Command::new("raw")
.arg(
clap::Arg::new("port")
.long("port")
.value_parser(3000..4000)
.action(clap::ArgAction::Set)
.required(true)
);

let m = cmd.try_get_matches_from_mut(["cmd", "--port", "3001"]).unwrap();
let port: i64 = *m.get_one("port")
.expect("required");
assert_eq!(port, 3001);
```


#### Impl: `From` (line 340)

<!-- Source: repos/clap/clap_builder/src/builder/value_parser.rs:340 -->

<!-- Type: impl -->


Create an `i64` [`ValueParser`] from a `N..=M` range

See [`RangedI64ValueParser`] for more control over the output type.

See also [`RangedU64ValueParser`]

# Examples

```rust
# use clap_builder as clap;
let mut cmd = clap::Command::new("raw")
.arg(
clap::Arg::new("port")
.long("port")
.value_parser(3000..=4000)
.action(clap::ArgAction::Set)
.required(true)
);

let m = cmd.try_get_matches_from_mut(["cmd", "--port", "3001"]).unwrap();
let port: i64 = *m.get_one("port")
.expect("required");
assert_eq!(port, 3001);
```


**Code Examples:**


```rust
# use clap_builder as clap;
let mut cmd = clap::Command::new("raw")
.arg(
clap::Arg::new("port")
.long("port")
.value_parser(3000..=4000)
.action(clap::ArgAction::Set)
.required(true)
);

let m = cmd.try_get_matches_from_mut(["cmd", "--port", "3001"]).unwrap();
let port: i64 = *m.get_one("port")
.expect("required");
assert_eq!(port, 3001);
```


#### Impl: `From` (line 371)

<!-- Source: repos/clap/clap_builder/src/builder/value_parser.rs:371 -->

<!-- Type: impl -->


Create an `i64` [`ValueParser`] from a `N..` range

See [`RangedI64ValueParser`] for more control over the output type.

See also [`RangedU64ValueParser`]

# Examples

```rust
# use clap_builder as clap;
let mut cmd = clap::Command::new("raw")
.arg(
clap::Arg::new("port")
.long("port")
.value_parser(3000..)
.action(clap::ArgAction::Set)
.required(true)
);

let m = cmd.try_get_matches_from_mut(["cmd", "--port", "3001"]).unwrap();
let port: i64 = *m.get_one("port")
.expect("required");
assert_eq!(port, 3001);
```


**Code Examples:**


```rust
# use clap_builder as clap;
let mut cmd = clap::Command::new("raw")
.arg(
clap::Arg::new("port")
.long("port")
.value_parser(3000..)
.action(clap::ArgAction::Set)
.required(true)
);

let m = cmd.try_get_matches_from_mut(["cmd", "--port", "3001"]).unwrap();
let port: i64 = *m.get_one("port")
.expect("required");
assert_eq!(port, 3001);
```


#### Impl: `From` (line 402)

<!-- Source: repos/clap/clap_builder/src/builder/value_parser.rs:402 -->

<!-- Type: impl -->


Create an `i64` [`ValueParser`] from a `..M` range

See [`RangedI64ValueParser`] for more control over the output type.

See also [`RangedU64ValueParser`]

# Examples

```rust
# use clap_builder as clap;
let mut cmd = clap::Command::new("raw")
.arg(
clap::Arg::new("port")
.long("port")
.value_parser(..3000)
.action(clap::ArgAction::Set)
.required(true)
);

let m = cmd.try_get_matches_from_mut(["cmd", "--port", "80"]).unwrap();
let port: i64 = *m.get_one("port")
.expect("required");
assert_eq!(port, 80);
```


**Code Examples:**


```rust
# use clap_builder as clap;
let mut cmd = clap::Command::new("raw")
.arg(
clap::Arg::new("port")
.long("port")
.value_parser(..3000)
.action(clap::ArgAction::Set)
.required(true)
);

let m = cmd.try_get_matches_from_mut(["cmd", "--port", "80"]).unwrap();
let port: i64 = *m.get_one("port")
.expect("required");
assert_eq!(port, 80);
```


#### Impl: `From` (line 433)

<!-- Source: repos/clap/clap_builder/src/builder/value_parser.rs:433 -->

<!-- Type: impl -->


Create an `i64` [`ValueParser`] from a `..=M` range

See [`RangedI64ValueParser`] for more control over the output type.

See also [`RangedU64ValueParser`]

# Examples

```rust
# use clap_builder as clap;
let mut cmd = clap::Command::new("raw")
.arg(
clap::Arg::new("port")
.long("port")
.value_parser(..=3000)
.action(clap::ArgAction::Set)
.required(true)
);

let m = cmd.try_get_matches_from_mut(["cmd", "--port", "80"]).unwrap();
let port: i64 = *m.get_one("port")
.expect("required");
assert_eq!(port, 80);
```


**Code Examples:**


```rust
# use clap_builder as clap;
let mut cmd = clap::Command::new("raw")
.arg(
clap::Arg::new("port")
.long("port")
.value_parser(..=3000)
.action(clap::ArgAction::Set)
.required(true)
);

let m = cmd.try_get_matches_from_mut(["cmd", "--port", "80"]).unwrap();
let port: i64 = *m.get_one("port")
.expect("required");
assert_eq!(port, 80);
```


#### Impl: `From` (line 464)

<!-- Source: repos/clap/clap_builder/src/builder/value_parser.rs:464 -->

<!-- Type: impl -->


Create an `i64` [`ValueParser`] from a `..` range

See [`RangedI64ValueParser`] for more control over the output type.

See also [`RangedU64ValueParser`]

# Examples

```rust
# use clap_builder as clap;
let mut cmd = clap::Command::new("raw")
.arg(
clap::Arg::new("port")
.long("port")
.value_parser(..)
.action(clap::ArgAction::Set)
.required(true)
);

let m = cmd.try_get_matches_from_mut(["cmd", "--port", "3001"]).unwrap();
let port: i64 = *m.get_one("port")
.expect("required");
assert_eq!(port, 3001);
```


**Code Examples:**


```rust
# use clap_builder as clap;
let mut cmd = clap::Command::new("raw")
.arg(
clap::Arg::new("port")
.long("port")
.value_parser(..)
.action(clap::ArgAction::Set)
.required(true)
);

let m = cmd.try_get_matches_from_mut(["cmd", "--port", "3001"]).unwrap();
let port: i64 = *m.get_one("port")
.expect("required");
assert_eq!(port, 3001);
```


#### Const: `C` (line 495)

<!-- Source: repos/clap/clap_builder/src/builder/value_parser.rs:495 -->

<!-- Type: const -->


Create a [`ValueParser`] with [`PossibleValuesParser`]

See [`PossibleValuesParser`] for more flexibility in creating the
[`PossibleValue`][crate::builder::PossibleValue]s.

# Examples

```rust
# use clap_builder as clap;
let mut cmd = clap::Command::new("raw")
.arg(
clap::Arg::new("color")
.long("color")
.value_parser(["always", "auto", "never"])
.default_value("auto")
);

let m = cmd.try_get_matches_from_mut(
["cmd", "--color", "never"]
).unwrap();

let color: &String = m.get_one("color")
.expect("default");
assert_eq!(color, "never");
```


**Code Examples:**


```rust
# use clap_builder as clap;
let mut cmd = clap::Command::new("raw")
.arg(
clap::Arg::new("color")
.long("color")
.value_parser(["always", "auto", "never"])
.default_value("auto")
);

let m = cmd.try_get_matches_from_mut(
["cmd", "--color", "never"]
).unwrap();

let color: &String = m.get_one("color")
.expect("default");
assert_eq!(color, "never");
```


#### Impl: `From` (line 530)

<!-- Source: repos/clap/clap_builder/src/builder/value_parser.rs:530 -->

<!-- Type: impl -->


Create a [`ValueParser`] with [`PossibleValuesParser`]

See [`PossibleValuesParser`] for more flexibility in creating the
[`PossibleValue`][crate::builder::PossibleValue]s.

# Examples

```rust
# use clap_builder as clap;
let possible = vec!["always", "auto", "never"];
let mut cmd = clap::Command::new("raw")
.arg(
clap::Arg::new("color")
.long("color")
.value_parser(possible)
.default_value("auto")
);

let m = cmd.try_get_matches_from_mut(
["cmd", "--color", "never"]
).unwrap();

let color: &String = m.get_one("color")
.expect("default");
assert_eq!(color, "never");
```


**Code Examples:**


```rust
# use clap_builder as clap;
let possible = vec!["always", "auto", "never"];
let mut cmd = clap::Command::new("raw")
.arg(
clap::Arg::new("color")
.long("color")
.value_parser(possible)
.default_value("auto")
);

let m = cmd.try_get_matches_from_mut(
["cmd", "--color", "never"]
).unwrap();

let color: &String = m.get_one("color")
.expect("default");
assert_eq!(color, "never");
```


#### Trait: `AnyValueParser` (line 590)

<!-- Source: repos/clap/clap_builder/src/builder/value_parser.rs:590 -->

<!-- Type: trait -->


A type-erased wrapper for [`TypedValueParser`].


#### Fn: `type_id` (line 609)

<!-- Source: repos/clap/clap_builder/src/builder/value_parser.rs:609 -->

<!-- Type: fn -->


Describes the content of `AnyValue`


#### Trait: `TypedValueParser` (line 660)

<!-- Source: repos/clap/clap_builder/src/builder/value_parser.rs:660 -->

<!-- Type: trait -->


Parse/validate argument values

As alternatives to implementing `TypedValueParser`,
- Use `Fn(&str) -> Result<T, E>` which implements `TypedValueParser`
- [`TypedValueParser::map`] or [`TypedValueParser::try_map`] to adapt an existing `TypedValueParser`

See `ValueParserFactory` to register `TypedValueParser::Value` with
[`value_parser!`][crate::value_parser].

# Example

```rust
# #[cfg(feature = "error-context")] {
# use clap_builder as clap;
# use clap::error::ErrorKind;
# use clap::error::ContextKind;
# use clap::error::ContextValue;
#[derive(Clone)]
struct Custom(u32);

#[derive(Clone)]
struct CustomValueParser;

impl clap::builder::TypedValueParser for CustomValueParser {
type Value = Custom;

fn parse_ref(
&self,
cmd: &clap::Command,
arg: Option<&clap::Arg>,
value: &std::ffi::OsStr,
) -> Result<Self::Value, clap::Error> {
let inner = clap::value_parser!(u32);
let val = inner.parse_ref(cmd, arg, value)?;

const INVALID_VALUE: u32 = 10;
if val == INVALID_VALUE {
let mut err = clap::Error::new(ErrorKind::ValueValidation)
.with_cmd(cmd);
if let Some(arg) = arg {
err.insert(ContextKind::InvalidArg, ContextValue::String(arg.to_string()));
}
err.insert(ContextKind::InvalidValue, ContextValue::String(INVALID_VALUE.to_string()));
return Err(err);
}

Ok(Custom(val))
}
}
# }
```


**Code Examples:**


```rust
# #[cfg(feature = "error-context")] {
# use clap_builder as clap;
# use clap::error::ErrorKind;
# use clap::error::ContextKind;
# use clap::error::ContextValue;
#[derive(Clone)]
struct Custom(u32);

#[derive(Clone)]
struct CustomValueParser;

impl clap::builder::TypedValueParser for CustomValueParser {
type Value = Custom;

fn parse_ref(
&self,
cmd: &clap::Command,
arg: Option<&clap::Arg>,
value: &std::ffi::OsStr,
) -> Result<Self::Value, clap::Error> {
let inner = clap::value_parser!(u32);
let val = inner.parse_ref(cmd, arg, value)?;

const INVALID_VALUE: u32 = 10;
if val == INVALID_VALUE {
let mut err = clap::Error::new(ErrorKind::ValueValidation)
.with_cmd(cmd);
if let Some(arg) = arg {
err.insert(ContextKind::InvalidArg, ContextValue::String(arg.to_string()));
}
err.insert(ContextKind::InvalidValue, ContextValue::String(INVALID_VALUE.to_string()));
return Err(err);
}

Ok(Custom(val))
}
}
# }
```


#### Type: `Value` (line 712)

<!-- Source: repos/clap/clap_builder/src/builder/value_parser.rs:712 -->

<!-- Type: type -->


Argument's value type


#### Fn: `parse_ref` (line 715)

<!-- Source: repos/clap/clap_builder/src/builder/value_parser.rs:715 -->

<!-- Type: fn -->


Parse the argument value

When `arg` is `None`, an external subcommand value is being parsed.


#### Fn: `parse_ref_` (line 725)

<!-- Source: repos/clap/clap_builder/src/builder/value_parser.rs:725 -->

<!-- Type: fn -->


Parse the argument value

When `arg` is `None`, an external subcommand value is being parsed.


#### Fn: `parse` (line 738)

<!-- Source: repos/clap/clap_builder/src/builder/value_parser.rs:738 -->

<!-- Type: fn -->


Parse the argument value

When `arg` is `None`, an external subcommand value is being parsed.


#### Fn: `parse_` (line 750)

<!-- Source: repos/clap/clap_builder/src/builder/value_parser.rs:750 -->

<!-- Type: fn -->


Parse the argument value

When `arg` is `None`, an external subcommand value is being parsed.


#### Fn: `possible_values` (line 763)

<!-- Source: repos/clap/clap_builder/src/builder/value_parser.rs:763 -->

<!-- Type: fn -->


Reflect on enumerated value properties

Error checking should not be done with this; it is mostly targeted at user-facing
applications like errors and completion.


#### Fn: `map` (line 773)

<!-- Source: repos/clap/clap_builder/src/builder/value_parser.rs:773 -->

<!-- Type: fn -->


Adapt a `TypedValueParser` from one value to another

# Example

```rust
# use clap_builder as clap;
# use clap::Command;
# use clap::Arg;
# use clap::builder::TypedValueParser as _;
# use clap::builder::BoolishValueParser;
let cmd = Command::new("mycmd")
.arg(
Arg::new("flag")
.long("flag")
.action(clap::ArgAction::SetTrue)
.value_parser(
BoolishValueParser::new()
.map(|b| -> usize {
if b { 10 } else { 5 }
})
)
);

let matches = cmd.clone().try_get_matches_from(["mycmd", "--flag"]).unwrap();
assert!(matches.contains_id("flag"));
assert_eq!(
matches.get_one::<usize>("flag").copied(),
Some(10)
);

let matches = cmd.try_get_matches_from(["mycmd"]).unwrap();
assert!(matches.contains_id("flag"));
assert_eq!(
matches.get_one::<usize>("flag").copied(),
Some(5)
);
```


**Code Examples:**


```rust
# use clap_builder as clap;
# use clap::Command;
# use clap::Arg;
# use clap::builder::TypedValueParser as _;
# use clap::builder::BoolishValueParser;
let cmd = Command::new("mycmd")
.arg(
Arg::new("flag")
.long("flag")
.action(clap::ArgAction::SetTrue)
.value_parser(
BoolishValueParser::new()
.map(|b| -> usize {
if b { 10 } else { 5 }
})
)
);

let matches = cmd.clone().try_get_matches_from(["mycmd", "--flag"]).unwrap();
assert!(matches.contains_id("flag"));
assert_eq!(
matches.get_one::<usize>("flag").copied(),
Some(10)
);

let matches = cmd.try_get_matches_from(["mycmd"]).unwrap();
assert!(matches.contains_id("flag"));
assert_eq!(
matches.get_one::<usize>("flag").copied(),
Some(5)
);
```


#### Fn: `try_map` (line 818)

<!-- Source: repos/clap/clap_builder/src/builder/value_parser.rs:818 -->

<!-- Type: fn -->


Adapt a `TypedValueParser` from one value to another

# Example

```rust
# use clap_builder as clap;
# use std::ffi::OsString;
# use std::ffi::OsStr;
# use std::path::PathBuf;
# use std::path::Path;
# use clap::Command;
# use clap::Arg;
# use clap::builder::TypedValueParser as _;
# use clap::builder::OsStringValueParser;
let cmd = Command::new("mycmd")
.arg(
Arg::new("flag")
.long("flag")
.value_parser(
OsStringValueParser::new()
.try_map(verify_ext)
)
);

fn verify_ext(os: OsString) -> Result<PathBuf, &'static str> {
let path = PathBuf::from(os);
if path.extension() != Some(OsStr::new("rs")) {
return Err("only Rust files are supported");
}
Ok(path)
}

let error = cmd.clone().try_get_matches_from(["mycmd", "--flag", "foo.txt"]).unwrap_err();
error.print();

let matches = cmd.try_get_matches_from(["mycmd", "--flag", "foo.rs"]).unwrap();
assert!(matches.contains_id("flag"));
assert_eq!(
matches.get_one::<PathBuf>("flag").map(|s| s.as_path()),
Some(Path::new("foo.rs"))
);
```


**Code Examples:**


```rust
# use clap_builder as clap;
# use std::ffi::OsString;
# use std::ffi::OsStr;
# use std::path::PathBuf;
# use std::path::Path;
# use clap::Command;
# use clap::Arg;
# use clap::builder::TypedValueParser as _;
# use clap::builder::OsStringValueParser;
let cmd = Command::new("mycmd")
.arg(
Arg::new("flag")
.long("flag")
.value_parser(
OsStringValueParser::new()
.try_map(verify_ext)
)
);

fn verify_ext(os: OsString) -> Result<PathBuf, &'static str> {
let path = PathBuf::from(os);
if path.extension() != Some(OsStr::new("rs")) {
return Err("only Rust files are supported");
}
Ok(path)
}

let error = cmd.clone().try_get_matches_from(["mycmd", "--flag", "foo.txt"]).unwrap_err();
error.print();

let matches = cmd.try_get_matches_from(["mycmd", "--flag", "foo.rs"]).unwrap();
assert!(matches.contains_id("flag"));
assert_eq!(
matches.get_one::<PathBuf>("flag").map(|s| s.as_path()),
Some(Path::new("foo.rs"))
);
```


#### Struct: `StringValueParser` (line 900)

<!-- Source: repos/clap/clap_builder/src/builder/value_parser.rs:900 -->

<!-- Type: struct -->


Implementation for [`ValueParser::string`]

Useful for composing new [`TypedValueParser`]s


#### Fn: `new` (line 908)

<!-- Source: repos/clap/clap_builder/src/builder/value_parser.rs:908 -->

<!-- Type: fn -->


Implementation for [`ValueParser::string`]


#### Struct: `OsStringValueParser` (line 948)

<!-- Source: repos/clap/clap_builder/src/builder/value_parser.rs:948 -->

<!-- Type: struct -->


Implementation for [`ValueParser::os_string`]

Useful for composing new [`TypedValueParser`]s


#### Fn: `new` (line 956)

<!-- Source: repos/clap/clap_builder/src/builder/value_parser.rs:956 -->

<!-- Type: fn -->


Implementation for [`ValueParser::os_string`]


#### Struct: `PathBufValueParser` (line 990)

<!-- Source: repos/clap/clap_builder/src/builder/value_parser.rs:990 -->

<!-- Type: struct -->


Implementation for [`ValueParser::path_buf`]

Useful for composing new [`TypedValueParser`]s


#### Fn: `new` (line 998)

<!-- Source: repos/clap/clap_builder/src/builder/value_parser.rs:998 -->

<!-- Type: fn -->


Implementation for [`ValueParser::path_buf`]


#### Struct: `EnumValueParser` (line 1040)

<!-- Source: repos/clap/clap_builder/src/builder/value_parser.rs:1040 -->

<!-- Type: struct -->


Parse an [`ValueEnum`][crate::ValueEnum] value.

See also:
- [`PossibleValuesParser`]

# Example

```rust
# use clap_builder as clap;
# use std::ffi::OsStr;
# use clap::ColorChoice;
# use clap::builder::TypedValueParser;
# let cmd = clap::Command::new("test");
# let arg = None;

// Usage
let mut cmd = clap::Command::new("raw")
.arg(
clap::Arg::new("color")
.value_parser(clap::builder::EnumValueParser::<ColorChoice>::new())
.required(true)
);

let m = cmd.try_get_matches_from_mut(["cmd", "always"]).unwrap();
let port: ColorChoice = *m.get_one("color")
.expect("required");
assert_eq!(port, ColorChoice::Always);

// Semantics
let value_parser = clap::builder::EnumValueParser::<ColorChoice>::new();
// or
let value_parser = clap::value_parser!(ColorChoice);
assert!(value_parser.parse_ref(&cmd, arg, OsStr::new("random")).is_err());
assert!(value_parser.parse_ref(&cmd, arg, OsStr::new("")).is_err());
assert_eq!(value_parser.parse_ref(&cmd, arg, OsStr::new("always")).unwrap(), ColorChoice::Always);
assert_eq!(value_parser.parse_ref(&cmd, arg, OsStr::new("auto")).unwrap(), ColorChoice::Auto);
assert_eq!(value_parser.parse_ref(&cmd, arg, OsStr::new("never")).unwrap(), ColorChoice::Never);
```


**Code Examples:**


```rust
# use clap_builder as clap;
# use std::ffi::OsStr;
# use clap::ColorChoice;
# use clap::builder::TypedValueParser;
# let cmd = clap::Command::new("test");
# let arg = None;

// Usage
let mut cmd = clap::Command::new("raw")
.arg(
clap::Arg::new("color")
.value_parser(clap::builder::EnumValueParser::<ColorChoice>::new())
.required(true)
);

let m = cmd.try_get_matches_from_mut(["cmd", "always"]).unwrap();
let port: ColorChoice = *m.get_one("color")
.expect("required");
assert_eq!(port, ColorChoice::Always);

// Semantics
let value_parser = clap::builder::EnumValueParser::<ColorChoice>::new();
// or
let value_parser = clap::value_parser!(ColorChoice);
assert!(value_parser.parse_ref(&cmd, arg, OsStr::new("random")).is_err());
assert!(value_parser.parse_ref(&cmd, arg, OsStr::new("")).is_err());
assert_eq!(value_parser.parse_ref(&cmd, arg, OsStr::new("always")).unwrap(), ColorChoice::Always);
assert_eq!(value_parser.parse_ref(&cmd, arg, OsStr::new("auto")).unwrap(), ColorChoice::Auto);
assert_eq!(value_parser.parse_ref(&cmd, arg, OsStr::new("never")).unwrap(), ColorChoice::Never);
```


#### Fn: `new` (line 1084)

<!-- Source: repos/clap/clap_builder/src/builder/value_parser.rs:1084 -->

<!-- Type: fn -->


Parse an [`ValueEnum`][crate::ValueEnum]


#### Struct: `PossibleValuesParser` (line 1156)

<!-- Source: repos/clap/clap_builder/src/builder/value_parser.rs:1156 -->

<!-- Type: struct -->


Verify the value is from an enumerated set of [`PossibleValue`][crate::builder::PossibleValue].

See also:
- [`EnumValueParser`] for directly supporting [`ValueEnum`][crate::ValueEnum] types
- [`TypedValueParser::map`] for adapting values to a more specialized type, like an external
enums that can't implement [`ValueEnum`][crate::ValueEnum]

# Example

Usage:
```rust
# use clap_builder as clap;
let mut cmd = clap::Command::new("raw")
.arg(
clap::Arg::new("color")
.value_parser(clap::builder::PossibleValuesParser::new(["always", "auto", "never"]))
.required(true)
);

let m = cmd.try_get_matches_from_mut(["cmd", "always"]).unwrap();
let port: &String = m.get_one("color")
.expect("required");
assert_eq!(port, "always");
```

Semantics:
```rust
# use clap_builder as clap;
# use std::ffi::OsStr;
# use clap::builder::TypedValueParser;
# let cmd = clap::Command::new("test");
# let arg = None;
let value_parser = clap::builder::PossibleValuesParser::new(["always", "auto", "never"]);
assert!(value_parser.parse_ref(&cmd, arg, OsStr::new("random")).is_err());
assert!(value_parser.parse_ref(&cmd, arg, OsStr::new("")).is_err());
assert_eq!(value_parser.parse_ref(&cmd, arg, OsStr::new("always")).unwrap(), "always");
assert_eq!(value_parser.parse_ref(&cmd, arg, OsStr::new("auto")).unwrap(), "auto");
assert_eq!(value_parser.parse_ref(&cmd, arg, OsStr::new("never")).unwrap(), "never");
```


**Code Examples:**


```rust
# use clap_builder as clap;
let mut cmd = clap::Command::new("raw")
.arg(
clap::Arg::new("color")
.value_parser(clap::builder::PossibleValuesParser::new(["always", "auto", "never"]))
.required(true)
);

let m = cmd.try_get_matches_from_mut(["cmd", "always"]).unwrap();
let port: &String = m.get_one("color")
.expect("required");
assert_eq!(port, "always");
```


```rust
# use clap_builder as clap;
# use std::ffi::OsStr;
# use clap::builder::TypedValueParser;
# let cmd = clap::Command::new("test");
# let arg = None;
let value_parser = clap::builder::PossibleValuesParser::new(["always", "auto", "never"]);
assert!(value_parser.parse_ref(&cmd, arg, OsStr::new("random")).is_err());
assert!(value_parser.parse_ref(&cmd, arg, OsStr::new("")).is_err());
assert_eq!(value_parser.parse_ref(&cmd, arg, OsStr::new("always")).unwrap(), "always");
assert_eq!(value_parser.parse_ref(&cmd, arg, OsStr::new("auto")).unwrap(), "auto");
assert_eq!(value_parser.parse_ref(&cmd, arg, OsStr::new("never")).unwrap(), "never");
```


#### Fn: `new` (line 1199)

<!-- Source: repos/clap/clap_builder/src/builder/value_parser.rs:1199 -->

<!-- Type: fn -->


Verify the value is from an enumerated set of [`PossibleValue`][crate::builder::PossibleValue].


#### Struct: `RangedI64ValueParser` (line 1268)

<!-- Source: repos/clap/clap_builder/src/builder/value_parser.rs:1268 -->

<!-- Type: struct -->


Parse number that fall within a range of values

<div class="warning">

**NOTE:** To capture negative values, you will also need to set
[`Arg::allow_negative_numbers`][crate::Arg::allow_negative_numbers] or
[`Arg::allow_hyphen_values`][crate::Arg::allow_hyphen_values].

</div>

# Example

Usage:
```rust
# use clap_builder as clap;
let mut cmd = clap::Command::new("raw")
.arg(
clap::Arg::new("port")
.long("port")
.value_parser(clap::value_parser!(u16).range(3000..))
.action(clap::ArgAction::Set)
.required(true)
);

let m = cmd.try_get_matches_from_mut(["cmd", "--port", "3001"]).unwrap();
let port: u16 = *m.get_one("port")
.expect("required");
assert_eq!(port, 3001);
```

Semantics:
```rust
# use clap_builder as clap;
# use std::ffi::OsStr;
# use clap::builder::TypedValueParser;
# let cmd = clap::Command::new("test");
# let arg = None;
let value_parser = clap::builder::RangedI64ValueParser::<i32>::new().range(-1..200);
assert!(value_parser.parse_ref(&cmd, arg, OsStr::new("random")).is_err());
assert!(value_parser.parse_ref(&cmd, arg, OsStr::new("")).is_err());
assert!(value_parser.parse_ref(&cmd, arg, OsStr::new("-200")).is_err());
assert!(value_parser.parse_ref(&cmd, arg, OsStr::new("300")).is_err());
assert_eq!(value_parser.parse_ref(&cmd, arg, OsStr::new("-1")).unwrap(), -1);
assert_eq!(value_parser.parse_ref(&cmd, arg, OsStr::new("0")).unwrap(), 0);
assert_eq!(value_parser.parse_ref(&cmd, arg, OsStr::new("50")).unwrap(), 50);
```


**Code Examples:**


```rust
# use clap_builder as clap;
let mut cmd = clap::Command::new("raw")
.arg(
clap::Arg::new("port")
.long("port")
.value_parser(clap::value_parser!(u16).range(3000..))
.action(clap::ArgAction::Set)
.required(true)
);

let m = cmd.try_get_matches_from_mut(["cmd", "--port", "3001"]).unwrap();
let port: u16 = *m.get_one("port")
.expect("required");
assert_eq!(port, 3001);
```


```rust
# use clap_builder as clap;
# use std::ffi::OsStr;
# use clap::builder::TypedValueParser;
# let cmd = clap::Command::new("test");
# let arg = None;
let value_parser = clap::builder::RangedI64ValueParser::<i32>::new().range(-1..200);
assert!(value_parser.parse_ref(&cmd, arg, OsStr::new("random")).is_err());
assert!(value_parser.parse_ref(&cmd, arg, OsStr::new("")).is_err());
assert!(value_parser.parse_ref(&cmd, arg, OsStr::new("-200")).is_err());
assert!(value_parser.parse_ref(&cmd, arg, OsStr::new("300")).is_err());
assert_eq!(value_parser.parse_ref(&cmd, arg, OsStr::new("-1")).unwrap(), -1);
assert_eq!(value_parser.parse_ref(&cmd, arg, OsStr::new("0")).unwrap(), 0);
assert_eq!(value_parser.parse_ref(&cmd, arg, OsStr::new("50")).unwrap(), 50);
```


#### Fn: `new` (line 1321)

<!-- Source: repos/clap/clap_builder/src/builder/value_parser.rs:1321 -->

<!-- Type: fn -->


Select full range of `i64`


#### Fn: `range` (line 1326)

<!-- Source: repos/clap/clap_builder/src/builder/value_parser.rs:1326 -->

<!-- Type: fn -->


Narrow the supported range


#### Struct: `RangedU64ValueParser` (line 1475)

<!-- Source: repos/clap/clap_builder/src/builder/value_parser.rs:1475 -->

<!-- Type: struct -->


Parse number that fall within a range of values

# Example

Usage:
```rust
# use clap_builder as clap;
let mut cmd = clap::Command::new("raw")
.arg(
clap::Arg::new("port")
.long("port")
.value_parser(clap::value_parser!(u64).range(3000..))
.action(clap::ArgAction::Set)
.required(true)
);

let m = cmd.try_get_matches_from_mut(["cmd", "--port", "3001"]).unwrap();
let port: u64 = *m.get_one("port")
.expect("required");
assert_eq!(port, 3001);
```

Semantics:
```rust
# use clap_builder as clap;
# use std::ffi::OsStr;
# use clap::builder::TypedValueParser;
# let cmd = clap::Command::new("test");
# let arg = None;
let value_parser = clap::builder::RangedU64ValueParser::<u32>::new().range(0..200);
assert!(value_parser.parse_ref(&cmd, arg, OsStr::new("random")).is_err());
assert!(value_parser.parse_ref(&cmd, arg, OsStr::new("")).is_err());
assert!(value_parser.parse_ref(&cmd, arg, OsStr::new("-200")).is_err());
assert!(value_parser.parse_ref(&cmd, arg, OsStr::new("300")).is_err());
assert!(value_parser.parse_ref(&cmd, arg, OsStr::new("-1")).is_err());
assert_eq!(value_parser.parse_ref(&cmd, arg, OsStr::new("0")).unwrap(), 0);
assert_eq!(value_parser.parse_ref(&cmd, arg, OsStr::new("50")).unwrap(), 50);
```


**Code Examples:**


```rust
# use clap_builder as clap;
let mut cmd = clap::Command::new("raw")
.arg(
clap::Arg::new("port")
.long("port")
.value_parser(clap::value_parser!(u64).range(3000..))
.action(clap::ArgAction::Set)
.required(true)
);

let m = cmd.try_get_matches_from_mut(["cmd", "--port", "3001"]).unwrap();
let port: u64 = *m.get_one("port")
.expect("required");
assert_eq!(port, 3001);
```


```rust
# use clap_builder as clap;
# use std::ffi::OsStr;
# use clap::builder::TypedValueParser;
# let cmd = clap::Command::new("test");
# let arg = None;
let value_parser = clap::builder::RangedU64ValueParser::<u32>::new().range(0..200);
assert!(value_parser.parse_ref(&cmd, arg, OsStr::new("random")).is_err());
assert!(value_parser.parse_ref(&cmd, arg, OsStr::new("")).is_err());
assert!(value_parser.parse_ref(&cmd, arg, OsStr::new("-200")).is_err());
assert!(value_parser.parse_ref(&cmd, arg, OsStr::new("300")).is_err());
assert!(value_parser.parse_ref(&cmd, arg, OsStr::new("-1")).is_err());
assert_eq!(value_parser.parse_ref(&cmd, arg, OsStr::new("0")).unwrap(), 0);
assert_eq!(value_parser.parse_ref(&cmd, arg, OsStr::new("50")).unwrap(), 50);
```


#### Fn: `new` (line 1520)

<!-- Source: repos/clap/clap_builder/src/builder/value_parser.rs:1520 -->

<!-- Type: fn -->


Select full range of `u64`


#### Fn: `range` (line 1525)

<!-- Source: repos/clap/clap_builder/src/builder/value_parser.rs:1525 -->

<!-- Type: fn -->


Narrow the supported range


#### Struct: `BoolValueParser` (line 1672)

<!-- Source: repos/clap/clap_builder/src/builder/value_parser.rs:1672 -->

<!-- Type: struct -->


Implementation for [`ValueParser::bool`]

Useful for composing new [`TypedValueParser`]s


#### Fn: `new` (line 1680)

<!-- Source: repos/clap/clap_builder/src/builder/value_parser.rs:1680 -->

<!-- Type: fn -->


Implementation for [`ValueParser::bool`]


#### Struct: `FalseyValueParser` (line 1736)

<!-- Source: repos/clap/clap_builder/src/builder/value_parser.rs:1736 -->

<!-- Type: struct -->


Parse false-like string values, everything else is `true`

See also:
- [`ValueParser::bool`] for assuming non-false is true
- [`BoolishValueParser`] for different human readable bool representations

# Example

Usage:
```rust
# use clap_builder as clap;
let mut cmd = clap::Command::new("raw")
.arg(
clap::Arg::new("append")
.value_parser(clap::builder::FalseyValueParser::new())
.required(true)
);

let m = cmd.try_get_matches_from_mut(["cmd", "true"]).unwrap();
let port: bool = *m.get_one("append")
.expect("required");
assert_eq!(port, true);
```

Semantics:
```rust
# use clap_builder as clap;
# use std::ffi::OsStr;
# use clap::builder::TypedValueParser;
# let cmd = clap::Command::new("test");
# let arg = None;
let value_parser = clap::builder::FalseyValueParser::new();
assert_eq!(value_parser.parse_ref(&cmd, arg, OsStr::new("random")).unwrap(), true);
assert_eq!(value_parser.parse_ref(&cmd, arg, OsStr::new("100")).unwrap(), true);
assert_eq!(value_parser.parse_ref(&cmd, arg, OsStr::new("")).unwrap(), false);
assert_eq!(value_parser.parse_ref(&cmd, arg, OsStr::new("false")).unwrap(), false);
assert_eq!(value_parser.parse_ref(&cmd, arg, OsStr::new("No")).unwrap(), false);
assert_eq!(value_parser.parse_ref(&cmd, arg, OsStr::new("oFF")).unwrap(), false);
assert_eq!(value_parser.parse_ref(&cmd, arg, OsStr::new("0")).unwrap(), false);
```


**Code Examples:**


```rust
# use clap_builder as clap;
let mut cmd = clap::Command::new("raw")
.arg(
clap::Arg::new("append")
.value_parser(clap::builder::FalseyValueParser::new())
.required(true)
);

let m = cmd.try_get_matches_from_mut(["cmd", "true"]).unwrap();
let port: bool = *m.get_one("append")
.expect("required");
assert_eq!(port, true);
```


```rust
# use clap_builder as clap;
# use std::ffi::OsStr;
# use clap::builder::TypedValueParser;
# let cmd = clap::Command::new("test");
# let arg = None;
let value_parser = clap::builder::FalseyValueParser::new();
assert_eq!(value_parser.parse_ref(&cmd, arg, OsStr::new("random")).unwrap(), true);
assert_eq!(value_parser.parse_ref(&cmd, arg, OsStr::new("100")).unwrap(), true);
assert_eq!(value_parser.parse_ref(&cmd, arg, OsStr::new("")).unwrap(), false);
assert_eq!(value_parser.parse_ref(&cmd, arg, OsStr::new("false")).unwrap(), false);
assert_eq!(value_parser.parse_ref(&cmd, arg, OsStr::new("No")).unwrap(), false);
assert_eq!(value_parser.parse_ref(&cmd, arg, OsStr::new("oFF")).unwrap(), false);
assert_eq!(value_parser.parse_ref(&cmd, arg, OsStr::new("0")).unwrap(), false);
```


#### Fn: `new` (line 1781)

<!-- Source: repos/clap/clap_builder/src/builder/value_parser.rs:1781 -->

<!-- Type: fn -->


Parse false-like string values, everything else is `true`


#### Struct: `BoolishValueParser` (line 1831)

<!-- Source: repos/clap/clap_builder/src/builder/value_parser.rs:1831 -->

<!-- Type: struct -->


Parse bool-like string values

See also:
- [`ValueParser::bool`] for different human readable bool representations
- [`FalseyValueParser`] for assuming non-false is true

# Example

Usage:
```rust
# use clap_builder as clap;
let mut cmd = clap::Command::new("raw")
.arg(
clap::Arg::new("append")
.value_parser(clap::builder::BoolishValueParser::new())
.required(true)
);

let m = cmd.try_get_matches_from_mut(["cmd", "true"]).unwrap();
let port: bool = *m.get_one("append")
.expect("required");
assert_eq!(port, true);
```

Semantics:
```rust
# use clap_builder as clap;
# use std::ffi::OsStr;
# use clap::builder::TypedValueParser;
# let cmd = clap::Command::new("test");
# let arg = None;
let value_parser = clap::builder::BoolishValueParser::new();
assert!(value_parser.parse_ref(&cmd, arg, OsStr::new("random")).is_err());
assert!(value_parser.parse_ref(&cmd, arg, OsStr::new("")).is_err());
assert!(value_parser.parse_ref(&cmd, arg, OsStr::new("100")).is_err());
assert_eq!(value_parser.parse_ref(&cmd, arg, OsStr::new("true")).unwrap(), true);
assert_eq!(value_parser.parse_ref(&cmd, arg, OsStr::new("Yes")).unwrap(), true);
assert_eq!(value_parser.parse_ref(&cmd, arg, OsStr::new("oN")).unwrap(), true);
assert_eq!(value_parser.parse_ref(&cmd, arg, OsStr::new("1")).unwrap(), true);
assert_eq!(value_parser.parse_ref(&cmd, arg, OsStr::new("false")).unwrap(), false);
assert_eq!(value_parser.parse_ref(&cmd, arg, OsStr::new("No")).unwrap(), false);
assert_eq!(value_parser.parse_ref(&cmd, arg, OsStr::new("oFF")).unwrap(), false);
assert_eq!(value_parser.parse_ref(&cmd, arg, OsStr::new("0")).unwrap(), false);
```


**Code Examples:**


```rust
# use clap_builder as clap;
let mut cmd = clap::Command::new("raw")
.arg(
clap::Arg::new("append")
.value_parser(clap::builder::BoolishValueParser::new())
.required(true)
);

let m = cmd.try_get_matches_from_mut(["cmd", "true"]).unwrap();
let port: bool = *m.get_one("append")
.expect("required");
assert_eq!(port, true);
```


```rust
# use clap_builder as clap;
# use std::ffi::OsStr;
# use clap::builder::TypedValueParser;
# let cmd = clap::Command::new("test");
# let arg = None;
let value_parser = clap::builder::BoolishValueParser::new();
assert!(value_parser.parse_ref(&cmd, arg, OsStr::new("random")).is_err());
assert!(value_parser.parse_ref(&cmd, arg, OsStr::new("")).is_err());
assert!(value_parser.parse_ref(&cmd, arg, OsStr::new("100")).is_err());
assert_eq!(value_parser.parse_ref(&cmd, arg, OsStr::new("true")).unwrap(), true);
assert_eq!(value_parser.parse_ref(&cmd, arg, OsStr::new("Yes")).unwrap(), true);
assert_eq!(value_parser.parse_ref(&cmd, arg, OsStr::new("oN")).unwrap(), true);
assert_eq!(value_parser.parse_ref(&cmd, arg, OsStr::new("1")).unwrap(), true);
assert_eq!(value_parser.parse_ref(&cmd, arg, OsStr::new("false")).unwrap(), false);
assert_eq!(value_parser.parse_ref(&cmd, arg, OsStr::new("No")).unwrap(), false);
assert_eq!(value_parser.parse_ref(&cmd, arg, OsStr::new("oFF")).unwrap(), false);
assert_eq!(value_parser.parse_ref(&cmd, arg, OsStr::new("0")).unwrap(), false);
```


#### Fn: `new` (line 1880)

<!-- Source: repos/clap/clap_builder/src/builder/value_parser.rs:1880 -->

<!-- Type: fn -->


Parse bool-like string values


#### Struct: `NonEmptyStringValueParser` (line 1932)

<!-- Source: repos/clap/clap_builder/src/builder/value_parser.rs:1932 -->

<!-- Type: struct -->


Parse non-empty string values

See also:
- [`ValueParser::string`]

# Example

Usage:
```rust
# use clap_builder as clap;
let mut cmd = clap::Command::new("raw")
.arg(
clap::Arg::new("append")
.value_parser(clap::builder::NonEmptyStringValueParser::new())
.required(true)
);

let m = cmd.try_get_matches_from_mut(["cmd", "true"]).unwrap();
let port: &String = m.get_one("append")
.expect("required");
assert_eq!(port, "true");
```

Semantics:
```rust
# use clap_builder as clap;
# use std::ffi::OsStr;
# use clap::builder::TypedValueParser;
# let cmd = clap::Command::new("test");
# let arg = None;
let value_parser = clap::builder::NonEmptyStringValueParser::new();
assert_eq!(value_parser.parse_ref(&cmd, arg, OsStr::new("random")).unwrap(), "random");
assert!(value_parser.parse_ref(&cmd, arg, OsStr::new("")).is_err());
```


**Code Examples:**


```rust
# use clap_builder as clap;
let mut cmd = clap::Command::new("raw")
.arg(
clap::Arg::new("append")
.value_parser(clap::builder::NonEmptyStringValueParser::new())
.required(true)
);

let m = cmd.try_get_matches_from_mut(["cmd", "true"]).unwrap();
let port: &String = m.get_one("append")
.expect("required");
assert_eq!(port, "true");
```


```rust
# use clap_builder as clap;
# use std::ffi::OsStr;
# use clap::builder::TypedValueParser;
# let cmd = clap::Command::new("test");
# let arg = None;
let value_parser = clap::builder::NonEmptyStringValueParser::new();
assert_eq!(value_parser.parse_ref(&cmd, arg, OsStr::new("random")).unwrap(), "random");
assert!(value_parser.parse_ref(&cmd, arg, OsStr::new("")).is_err());
```


#### Fn: `new` (line 1971)

<!-- Source: repos/clap/clap_builder/src/builder/value_parser.rs:1971 -->

<!-- Type: fn -->


Parse non-empty string values


#### Struct: `MapValueParser` (line 2010)

<!-- Source: repos/clap/clap_builder/src/builder/value_parser.rs:2010 -->

<!-- Type: struct -->


Adapt a `TypedValueParser` from one value to another

See [`TypedValueParser::map`]


#### Struct: `TryMapValueParser` (line 2069)

<!-- Source: repos/clap/clap_builder/src/builder/value_parser.rs:2069 -->

<!-- Type: struct -->


Adapt a `TypedValueParser` from one value to another

See [`TypedValueParser::try_map`]


#### Fn: `suggest_arg` (line 2165)

<!-- Source: repos/clap/clap_builder/src/builder/value_parser.rs:2165 -->

<!-- Type: fn -->


Suggest an alternative argument


#### Fn: `suggest` (line 2173)

<!-- Source: repos/clap/clap_builder/src/builder/value_parser.rs:2173 -->

<!-- Type: fn -->


Provide a general suggestion


#### Fn: `and_suggest` (line 2181)

<!-- Source: repos/clap/clap_builder/src/builder/value_parser.rs:2181 -->

<!-- Type: fn -->


Extend the suggestions


#### Trait: `ValueParserFactory` (line 2241)

<!-- Source: repos/clap/clap_builder/src/builder/value_parser.rs:2241 -->

<!-- Type: trait -->


Register a type with [`value_parser!`][crate::value_parser!]

# Example

```rust
# use clap_builder as clap;
#[derive(Copy, Clone, Debug)]
pub struct Custom(u32);

impl clap::builder::ValueParserFactory for Custom {
type Parser = CustomValueParser;
fn value_parser() -> Self::Parser {
CustomValueParser
}
}

#[derive(Clone, Debug)]
pub struct CustomValueParser;
impl clap::builder::TypedValueParser for CustomValueParser {
type Value = Custom;

fn parse_ref(
&self,
cmd: &clap::Command,
arg: Option<&clap::Arg>,
value: &std::ffi::OsStr,
) -> Result<Self::Value, clap::Error> {
let inner = clap::value_parser!(u32);
let val = inner.parse_ref(cmd, arg, value)?;
Ok(Custom(val))
}
}

let parser: CustomValueParser = clap::value_parser!(Custom);
```


**Code Examples:**


```rust
# use clap_builder as clap;
#[derive(Copy, Clone, Debug)]
pub struct Custom(u32);

impl clap::builder::ValueParserFactory for Custom {
type Parser = CustomValueParser;
fn value_parser() -> Self::Parser {
CustomValueParser
}
}

#[derive(Clone, Debug)]
pub struct CustomValueParser;
impl clap::builder::TypedValueParser for CustomValueParser {
type Value = Custom;

fn parse_ref(
&self,
cmd: &clap::Command,
arg: Option<&clap::Arg>,
value: &std::ffi::OsStr,
) -> Result<Self::Value, clap::Error> {
let inner = clap::value_parser!(u32);
let val = inner.parse_ref(cmd, arg, value)?;
Ok(Custom(val))
}
}

let parser: CustomValueParser = clap::value_parser!(Custom);
```


#### Type: `Parser` (line 2277)

<!-- Source: repos/clap/clap_builder/src/builder/value_parser.rs:2277 -->

<!-- Type: type -->


Generated parser, usually [`ValueParser`].

It should at least be a type that supports `Into<ValueParser>`.  A non-`ValueParser` type
allows the caller to do further initialization on the parser.


#### Fn: `value_parser` (line 2283)

<!-- Source: repos/clap/clap_builder/src/builder/value_parser.rs:2283 -->

<!-- Type: fn -->


Create the specified [`Self::Parser`]


#### Struct: `_AnonymousValueParser` (line 2449)

<!-- Source: repos/clap/clap_builder/src/builder/value_parser.rs:2449 -->

<!-- Type: struct -->


Unstable [`ValueParser`]

Implementation may change to more specific instance in the future


### From `repos/clap/clap_builder/src/parser/features/suggestions.rs`


#### Fn: `did_you_mean` (line 4)

<!-- Source: repos/clap/clap_builder/src/parser/features/suggestions.rs:4 -->

<!-- Type: fn -->


Find strings from an iterable of `possible_values` similar to a given value `v`
Returns a Vec of all possible values that exceed a similarity threshold
sorted by ascending similarity, most similar comes last


#### Fn: `did_you_mean_flag` (line 48)

<!-- Source: repos/clap/clap_builder/src/parser/features/suggestions.rs:48 -->

<!-- Type: fn -->


Returns a suffix that can be empty, or is the standard 'did you mean' phrase


### From `repos/clap/clap_builder/src/parser/matches/value_source.rs`


#### Enum: `ValueSource` (line 1)

<!-- Source: repos/clap/clap_builder/src/parser/matches/value_source.rs:1 -->

<!-- Type: enum -->


Origin of the argument's value


### From `repos/clap/clap_builder/src/parser/mod.rs`


#### Module: `mod` (line 1)

<!-- Source: repos/clap/clap_builder/src/parser/mod.rs:1 -->

<!-- Type: module -->


[`Command`][crate::Command] line argument parser


### From `repos/clap/clap_builder/src/parser/parser.rs`


#### Fn: `did_you_mean_error` (line 1547)

<!-- Source: repos/clap/clap_builder/src/parser/parser.rs:1547 -->

<!-- Type: fn -->


Is only used for the long flag(which is the only one needs fuzzy searching)


#### Enum: `ParseResult` (line 1635)

<!-- Source: repos/clap/clap_builder/src/parser/parser.rs:1635 -->

<!-- Type: enum -->


Recoverable Parsing results.


---


## 5. Derive API - Overview {#derive_general}


### From `repos/clap/clap_derive/src/derives/args.rs`


#### Fn: `gen_augment` (line 167)

<!-- Source: repos/clap/clap_derive/src/derives/args.rs:167 -->

<!-- Type: fn -->


Generate a block of code to add arguments/subcommands corresponding to
the `fields` to an cmd.


### From `repos/clap/clap_derive/src/dummies.rs`


#### Module: `dummies` (line 1)

<!-- Source: repos/clap/clap_derive/src/dummies.rs:1 -->

<!-- Type: module -->


Dummy implementations that we emit along with an error.


### From `repos/clap/clap_derive/src/item.rs`


#### Const: `DEFAULT_CASING` (line 26)

<!-- Source: repos/clap/clap_derive/src/item.rs:26 -->

<!-- Type: const -->


Default casing style for generated arguments.


#### Const: `DEFAULT_ENV_CASING` (line 29)

<!-- Source: repos/clap/clap_derive/src/item.rs:29 -->

<!-- Type: const -->


Default casing style for environment variables


#### Fn: `initial_top_level_methods` (line 966)

<!-- Source: repos/clap/clap_derive/src/item.rs:966 -->

<!-- Type: fn -->


generate methods from attributes on top of struct or enum


#### Fn: `field_methods` (line 983)

<!-- Source: repos/clap/clap_derive/src/item.rs:983 -->

<!-- Type: fn -->


generate methods on top of a field


#### Fn: `process_author_str` (line 1351)

<!-- Source: repos/clap/clap_derive/src/item.rs:1351 -->

<!-- Type: fn -->


replace all `:` with `, ` when not inside the `<>`

`"author1:author2:author3" => "author1, author2, author3"`
`"author1 <http://website1.com>:author2" => "author1 <http://website1.com>, author2"`


#### Enum: `CasingStyle` (line 1376)

<!-- Source: repos/clap/clap_derive/src/item.rs:1376 -->

<!-- Type: enum -->


Defines the casing for the attributes long representation.


### From `repos/clap/clap_derive/src/lib.rs`


#### Fn: `value_enum` (line 36)

<!-- Source: repos/clap/clap_derive/src/lib.rs:36 -->

<!-- Type: fn -->


Generates the `ValueEnum` impl.


#### Fn: `subcommand` (line 85)

<!-- Source: repos/clap/clap_derive/src/lib.rs:85 -->

<!-- Type: fn -->


Generates the `Subcommand` impl.


#### Fn: `args` (line 97)

<!-- Source: repos/clap/clap_derive/src/lib.rs:97 -->

<!-- Type: fn -->


Generates the `Args` impl.


### From `repos/clap/clap_derive/src/utils/doc_comments.rs`


#### Module: `doc_comments` (line 1)

<!-- Source: repos/clap/clap_derive/src/utils/doc_comments.rs:1 -->

<!-- Type: module -->


The preprocessing we apply to doc comments.

#[derive(Parser)] works in terms of "paragraphs". Paragraph is a sequence of
non-empty adjacent lines, delimited by sequences of blank (whitespace only) lines.


### From `repos/clap/clap_derive/src/utils/spanned.rs`


#### Struct: `Sp` (line 7)

<!-- Source: repos/clap/clap_derive/src/utils/spanned.rs:7 -->

<!-- Type: struct -->


An entity with a span attached.


### From `repos/clap/clap_derive/src/utils/ty.rs`


#### Module: `ty` (line 1)

<!-- Source: repos/clap/clap_derive/src/utils/ty.rs:1 -->

<!-- Type: module -->


Special types handling


---


## 6. Derive API - Parser {#derive_parser}


### From `repos/clap/clap_derive/src/lib.rs`


#### Fn: `parser` (line 48)

<!-- Source: repos/clap/clap_derive/src/lib.rs:48 -->

<!-- Type: fn -->


Generates the `Parser` implementation.

This is far less verbose than defining the `clap::Command` struct manually,
receiving an instance of `clap::ArgMatches` from conducting parsing, and then
implementing a conversion code to instantiate an instance of the user
context struct.


---


## 8. Validation {#validation}


### From `repos/clap/clap_builder/src/builder/styling.rs`


#### Fn: `invalid` (line 117)

<!-- Source: repos/clap/clap_builder/src/builder/styling.rs:117 -->

<!-- Type: fn -->


Highlight invalid usage


#### Fn: `get_invalid` (line 181)

<!-- Source: repos/clap/clap_builder/src/builder/styling.rs:181 -->

<!-- Type: fn -->


Highlight invalid usage


### From `repos/clap/clap_complete/src/env/mod.rs`


#### Module: `mod` (line 1)

<!-- Source: repos/clap/clap_complete/src/env/mod.rs:1 -->

<!-- Type: module -->


[`COMPLETE=$SHELL <bin>`][CompleteEnv] completion integration

See [`CompleteEnv`]:
```rust
# use clap_complete::CompleteEnv;
fn cli() -> clap::Command {
// ...
#   clap::Command::new("empty")
}

fn main() {
CompleteEnv::with_factory(cli)
.complete();

// ... rest of application logic
}
```

To customize completions, see
- [`ValueHint`][crate::ValueHint]
- [`ValueEnum`][clap::ValueEnum]
- [`ArgValueCandidates`][crate::ArgValueCandidates]
- [`ArgValueCompleter`][crate::ArgValueCompleter]

To source your completions:

<div class="warning">

**WARNING:** We recommend re-sourcing your completions on upgrade.
These completions work by generating shell code that calls into `your_program` while completing.
That interface is unstable and a mismatch between the shell code and `your_program` may result
in either invalid completions or no completions being generated.
For this reason, we recommend generating the shell code anew on shell startup so that it is
"self-correcting" on shell launch, rather than writing the generated completions to a file.

</div>

**Bash**
```bash
echo "source <(COMPLETE=bash your_program)" >> ~/.bashrc
```

**Elvish**
```elvish
echo "eval (E:COMPLETE=elvish your_program | slurp)" >> ~/.elvish/rc.elv
```

**Fish**
```fish
echo "COMPLETE=fish your_program | source" >> ~/.config/fish/config.fish
```

**Powershell**
```powershell
echo '$env:COMPLETE = "powershell"; your_program | Out-String | Invoke-Expression; Remove-Item Env:\COMPLETE' >> $PROFILE
```
Note that to execute scripts in PowerShell on Windows, including [`$PROFILE`][$Profile],
the [execution policy][ExecutionPolicies] needs to be set to `RemoteSigned` at minimum.

[$Profile]: https://learn.microsoft.com/en-us/powershell/scripting/learn/shell/creating-profiles
[ExecutionPolicies]: https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.core/about/about_execution_policies

**Zsh**
```zsh
echo "source <(COMPLETE=zsh your_program)" >> ~/.zshrc
```

To disable completions, you can set `COMPLETE=` or `COMPLETE=0`


**Code Examples:**


```rust
# use clap_complete::CompleteEnv;
fn cli() -> clap::Command {
// ...
#   clap::Command::new("empty")
}

fn main() {
CompleteEnv::with_factory(cli)
.complete();

// ... rest of application logic
}
```


```rust
**Elvish**
```


```rust
**Fish**
```


```rust
**Powershell**
```


```rust
Note that to execute scripts in PowerShell on Windows, including [`$PROFILE`][$Profile],
the [execution policy][ExecutionPolicies] needs to be set to `RemoteSigned` at minimum.

[$Profile]: https://learn.microsoft.com/en-us/powershell/scripting/learn/shell/creating-profiles
[ExecutionPolicies]: https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.core/about/about_execution_policies

**Zsh**
```


#### Fn: `write_registration` (line 362)

<!-- Source: repos/clap/clap_complete/src/env/mod.rs:362 -->

<!-- Type: fn -->


Register for completions

Write the `buf` the logic needed for calling into `<VAR>=<shell> <cmd> --`, passing needed
arguments to [`EnvCompleter::write_complete`] through the environment.

- `var`: see [`CompleteEnv::var`]
- `name`: an identifier to use in the script
- `bin`: see [`CompleteEnv::bin`]
- `completer`: see [`CompleteEnv::completer`]

<div class="warning">

**WARNING:** There are no stability guarantees between the call to
[`EnvCompleter::write_complete`] that this generates and actually calling [`EnvCompleter::write_complete`].
Caching the results of this call may result in invalid or no completions to be generated.

</div>


### From `repos/clap/src/_concepts.rs`


#### Module: `_concepts` (line 1)

<!-- Source: repos/clap/src/_concepts.rs:1 -->

<!-- Type: module -->


## CLI Concepts

Note: this will be speaking towards the general case.

### Environmental context

When you run a command line application, it is inside a terminal emulator, or terminal.
This handles integration with the rest of your system including user input,
rendering, etc.

The terminal will run inside of itself an interactive shell.
The shell is responsible for showing the prompt, receiving input including the command you are writing,
letting that command take over until completion, and then repeating.
This is called a read-eval-print loop, or REPL.
Typically the shell will take the command you typed and split it into separate arguments,
including handling of quoting, escaping, and globbing.
The parsing and evaluation of the command is shell specific.
The shell will then determine which application to run and then pass the full command-line as
individual arguments to your program.
These arguments are exposed in Rust as [`std::env::args_os`].

Windows is an exception in Shell behavior in that the command is passed as an individual
string, verbatim, and the application must split the arguments.
[`std::env::args_os`] will handle the splitting for you but will not handle globs.

Takeaways:
- Your application will only see quotes that have been escaped within the shell
- e.g. to receive `message="hello world"`, you may need to type `'message="hello world"'` or `message=\"hello world\"`
- If your applications needs to parse a string into arguments,
you will need to pick a syntax and do it yourself
- POSIX's shell syntax is a common choice and available in packages like [shlex](https://docs.rs/shlex)
- See also our [REPL cookbook entry][crate::_cookbook::repl]
- On Windows, you will need to handle globbing yourself if desired
- [`wild`](https://docs.rs/wild) can help with that

### Argument Parsing

The first argument of [`std::env::args_os`] is the [`Command::bin_name`]
which is usually limited to affecting [`Command::render_usage`].
[`Command::no_binary_name`] and [`Command::multicall`] exist for rare cases when this assumption is not valid.

Command-lines are a context-sensitive grammar,
meaning the interpretation of an argument is based on the arguments that came before.
Arguments come in one of several flavors:
- Values
- Flags
- Subcommands

When examining the next argument,
1. If it starts with a `--`,
then that is a long Flag and all remaining text up to a `=` or the end is
matched to a [`Arg::long`], [`Command::long_flag`], or alias.
- Everything after the `=` is taken as a Value and parsing a new argument is examined.
- If no `=` is present, then Values will be taken according to [`Arg::num_args`]
- We generally call a Flag that takes a Value an Option
2. If it starts with a `-`,
then that is a sequence of short Flags where each character is matched against a [`Arg::short`], [`Command::short_flag`] or
alias until `=`, the end, or a short Flag takes Values (see [`Arg::num_args`])
3. If its a `--`, that is an escape and all future arguments are considered to be a Value, even if
they start with `--` or `-`
4. If it matches a [`Command::name`],
then the argument is a subcommand
5. If there is an [`Arg`] at the next [`Arg::index`],
then the argument is considered a Positional argument

When a subcommand matches,
all further arguments are parsed by that [`Command`].

There are many settings that tweak this behavior, including:
- [`Arg::last`]: a positional that can only come after `--`
- [`Arg::trailing_var_arg`]: all further arguments are captured as additional Values
- [`Arg::allow_hyphen_values`] and [`Arg::allow_negative_numbers`]: assumes arguments
starting with `-` are Values and not Flags.
- [`Command::subcommand_precedence_over_arg`]: when an [`Arg::num_args`] takes Values,
stop if one matches a subCommand
- [`Command::allow_missing_positional`]: in limited cases a [`Arg::index`] may be skipped
- [`Command::allow_external_subcommands`]: treat any unknown argument as a subcommand, capturing
all remaining arguments.

Takeaways
- Values that start with a `-` either need to be escaped by the user with `--`
(if a positional),
or you need to set [`Arg::allow_hyphen_values`] or [`Arg::allow_negative_numbers`]
- [`Arg::num_args`],
[`ArgAction::Append`] (on a positional),
[`Arg::trailing_var_arg`],
and [`Command::allow_external_subcommands`]
all affect the parser in similar but slightly different ways and which to use depends on your
application

### Value Parsing

When reacting to a Flag (no Value),
[`Arg::default_missing_values`] will be applied.

The Value will be split by [`Arg::value_delimiter`].

The Value will then be stored according to its [`ArgAction`].
For most [`ArgAction`]s,
the Value will be parsed according to [`ValueParser`]
and stored in the [`ArgMatches`].


### From `repos/clap/src/_faq.rs`


#### Module: `_faq` (line 1)

<!-- Source: repos/clap/src/_faq.rs:1 -->

<!-- Type: module -->


# Documentation: FAQ

1. [Comparisons](#comparisons)
1. [How does `clap` compare to structopt?](#how-does-clap-compare-to-structopt)
2. [What are some reasons to use `clap`? (The Pitch)](#what-are-some-reasons-to-use-clap-the-pitch)
3. [What are some reasons *not* to use `clap`? (The Anti Pitch)](#what-are-some-reasons-not-to-use-clap-the-anti-pitch)
4. [Reasons to use `clap`](#reasons-to-use-clap)
2. [How many approaches are there to create a parser?](#how-many-approaches-are-there-to-create-a-parser)
3. [When should I use the builder vs derive APIs?](#when-should-i-use-the-builder-vs-derive-apis)
4. [Why is there a default subcommand of help?](#why-is-there-a-default-subcommand-of-help)

### Comparisons

First, let me say that these comparisons are highly subjective, and not meant
in a critical or harsh manner. All the argument parsing libraries out there (to
include `clap`) have their own strengths and weaknesses. Sometimes it just
comes down to personal taste when all other factors are equal. When in doubt,
try them all and pick one that you enjoy :). There's plenty of room in the Rust
community for multiple implementations!

For less detailed but more broad comparisons, see
[argparse-benchmarks](https://github.com/rust-cli/argparse-benchmarks-rs).

#### How does `clap` compare to [structopt](https://github.com/TeXitoi/structopt)?

Simple! `clap` *is* `structopt`.  `structopt` started as a derive API built on
top of clap v2.  With clap v3, we've forked structopt and integrated it
directly into clap.  structopt is in
[maintenance mode](https://github.com/TeXitoi/structopt/issues/516#issuecomment-989566094)
with the release of `clap_derive`.

The benefits of integrating `structopt` and `clap` are:
- Easier cross-linking in documentation
- Documentation parity
- Tighter design feedback loop, ensuring all new features are designed with
derives in mind and easier to change `clap` in response to `structopt` bugs.
- Clearer endorsement of `structopt`

See also
- [`clap` v3 CHANGELOG](https://github.com/clap-rs/clap/blob/v3-master/CHANGELOG.md#300---2021-12-31)
- [`structopt` migration guide](https://github.com/clap-rs/clap/blob/v3-master/CHANGELOG.md#migrate-structopt)

#### What are some reasons to use `clap`? (The Pitch)

`clap` is as fast, and as lightweight as possible while still giving all the features you'd expect from a modern argument parser. In fact, for the amount and type of features `clap` offers it remains about as fast as `getopts`. If you use `clap`, when you just need some simple arguments parsed, you'll find it's a walk in the park. `clap` also makes it possible to represent extremely complex and advanced requirements without too much thought. `clap` aims to be intuitive, easy to use, and fully capable for wide variety use cases and needs.

#### What are some reasons *not* to use `clap`? (The Anti Pitch)

Depending on the style in which you choose to define the valid arguments, `clap` can be very verbose. `clap` also offers so many finetuning knobs and dials, that learning everything can seem overwhelming. I strive to keep the simple cases simple, but when turning all those custom dials it can get complex. `clap` is also opinionated about parsing. Even though so much can be tweaked and tuned with `clap` (and I'm adding more all the time), there are still certain features which `clap` implements in specific ways that may be contrary to some users' use-cases.

#### Reasons to use `clap`

* You want all the nice CLI features your users may expect, yet you don't want to implement them all yourself. You'd like to focus on your application, not argument parsing.
* In addition to the point above, you don't want to sacrifice performance to get all those nice features.
* You have complex requirements/conflicts between your various valid args.
* You want to use subcommands (although other libraries also support subcommands, they are not nearly as feature rich as those provided by `clap`).
* You want some sort of custom validation built into the argument parsing process, instead of as part of your application (which allows for earlier failures, better error messages, more cohesive experience, etc.).

### How many approaches are there to create a parser?

The following APIs are supported:
- [Derive][crate::_derive::_tutorial]
- [Builder][crate::_tutorial]

Previously, we supported:
- [YAML](https://github.com/clap-rs/clap/issues/3087)
- [docopt](http://docopt.org/)-inspired [usage parser](https://github.com/clap-rs/clap/issues/3086)
- [`clap_app!`](https://github.com/clap-rs/clap/issues/2835)

There are also experiments with other APIs:
- [fncmd](https://github.com/yuhr/fncmd): function attribute
- [clap-serde](https://github.com/aobatact/clap-serde): create a `Command` from a deserializer

### When should I use the builder vs derive APIs?

Our default answer is to use the [Derive API][crate::_derive::_tutorial]:
- Easier to read, write, and modify
- Easier to keep the argument declaration and reading of argument in sync
- Easier to reuse, e.g. [clap-verbosity-flag](https://crates.io/crates/clap-verbosity-flag)

The [Builder API][crate::_tutorial] is a lower-level API that someone might want to use for
- Faster compile times if you aren't already using other procedural macros
- More flexibility, e.g. you can look up the [argument's values][crate::ArgMatches::get_many],
their [ordering with other arguments][crate::ArgMatches::indices_of], and [what set
them][crate::ArgMatches::value_source].  The Derive API can only report values and not
indices of or other data.

You can [interop between Derive and Builder APIs][crate::_derive#mixing-builder-and-derive-apis].

### Why is there a default subcommand of help?

There is only a default subcommand of `help` when other subcommands have been defined manually. So it's opt-in(ish), being that you only get a `help` subcommand if you're actually using subcommands.

Also, if the user defined a `help` subcommand themselves, the auto-generated one wouldn't be added (meaning it's only generated if the user hasn't defined one themselves).



---


## 9. Error Handling {#error_handling}


### From `repos/clap/clap_builder/src/error/context.rs`


#### Enum: `ContextKind` (line 1)

<!-- Source: repos/clap/clap_builder/src/error/context.rs:1 -->

<!-- Type: enum -->


Semantics for a piece of error information


#### Fn: `as_str` (line 43)

<!-- Source: repos/clap/clap_builder/src/error/context.rs:43 -->

<!-- Type: fn -->


End-user description of the error case, where relevant


#### Enum: `ContextValue` (line 73)

<!-- Source: repos/clap/clap_builder/src/error/context.rs:73 -->

<!-- Type: enum -->


A piece of error information


### From `repos/clap/clap_builder/src/error/format.rs`


#### Trait: `ErrorFormatter` (line 19)

<!-- Source: repos/clap/clap_builder/src/error/format.rs:19 -->

<!-- Type: trait -->


Defines how to format an error for displaying to the user


#### Fn: `format_error` (line 21)

<!-- Source: repos/clap/clap_builder/src/error/format.rs:21 -->

<!-- Type: fn -->


Stylize the error for the terminal


#### Struct: `KindFormatter` (line 25)

<!-- Source: repos/clap/clap_builder/src/error/format.rs:25 -->

<!-- Type: struct -->


Report [`ErrorKind`]

No context is included.

<div class="warning">

**NOTE:** Consider removing the `error-context` default feature if using this to remove all
overhead for [`RichFormatter`].

</div>


#### Struct: `RichFormatter` (line 57)

<!-- Source: repos/clap/clap_builder/src/error/format.rs:57 -->

<!-- Type: struct -->


Richly formatted error context

This follows the [rustc diagnostic style guide](https://rustc-dev-guide.rust-lang.org/diagnostics.html#suggestion-style-guide).


#### Fn: `singular_or_plural` (line 414)

<!-- Source: repos/clap/clap_builder/src/error/format.rs:414 -->

<!-- Type: fn -->


Returns the singular or plural form on the verb to be based on the argument's value.


### From `repos/clap/clap_builder/src/error/kind.rs`


#### Enum: `ErrorKind` (line 1)

<!-- Source: repos/clap/clap_builder/src/error/kind.rs:1 -->

<!-- Type: enum -->


Command line argument parser kind of error


#### Fn: `as_str` (line 333)

<!-- Source: repos/clap/clap_builder/src/error/kind.rs:333 -->

<!-- Type: fn -->


End-user description of the error case, where relevant


### From `repos/clap/clap_builder/src/error/mod.rs`


#### Module: `mod` (line 1)

<!-- Source: repos/clap/clap_builder/src/error/mod.rs:1 -->

<!-- Type: module -->


Error reporting


#### Type: `Result` (line 50)

<!-- Source: repos/clap/clap_builder/src/error/mod.rs:50 -->

<!-- Type: type -->


Short hand for [`Result`] type

[`Result`]: std::result::Result


#### Struct: `Error` (line 55)

<!-- Source: repos/clap/clap_builder/src/error/mod.rs:55 -->

<!-- Type: struct -->


Command Line Argument Parser Error

See [`Command::error`] to create an error.

[`Command::error`]: crate::Command::error


#### Fn: `raw` (line 80)

<!-- Source: repos/clap/clap_builder/src/error/mod.rs:80 -->

<!-- Type: fn -->


Create an unformatted error

This is for you need to pass the error up to
a place that has access to the `Command` at which point you can call [`Error::format`].

Prefer [`Command::error`] for generating errors.

[`Command::error`]: crate::Command::error


#### Fn: `format` (line 92)

<!-- Source: repos/clap/clap_builder/src/error/mod.rs:92 -->

<!-- Type: fn -->


Format the existing message with the Command's context


#### Fn: `new` (line 103)

<!-- Source: repos/clap/clap_builder/src/error/mod.rs:103 -->

<!-- Type: fn -->


Create an error with a pre-defined message

See also
- [`Error::insert`]
- [`Error::with_cmd`]

# Example

```rust
# #[cfg(feature = "error-context")] {
# use clap_builder as clap;
# use clap::error::ErrorKind;
# use clap::error::ContextKind;
# use clap::error::ContextValue;

let cmd = clap::Command::new("prog");

let mut err = clap::Error::new(ErrorKind::ValueValidation)
.with_cmd(&cmd);
err.insert(ContextKind::InvalidArg, ContextValue::String("--foo".to_owned()));
err.insert(ContextKind::InvalidValue, ContextValue::String("bar".to_owned()));

err.print();
# }
```


**Code Examples:**


```rust
# #[cfg(feature = "error-context")] {
# use clap_builder as clap;
# use clap::error::ErrorKind;
# use clap::error::ContextKind;
# use clap::error::ContextValue;

let cmd = clap::Command::new("prog");

let mut err = clap::Error::new(ErrorKind::ValueValidation)
.with_cmd(&cmd);
err.insert(ContextKind::InvalidArg, ContextValue::String("--foo".to_owned()));
err.insert(ContextKind::InvalidValue, ContextValue::String("bar".to_owned()));

err.print();
# }
```


#### Fn: `with_cmd` (line 146)

<!-- Source: repos/clap/clap_builder/src/error/mod.rs:146 -->

<!-- Type: fn -->


Apply [`Command`]'s formatting to the error

Generally, this is used with [`Error::new`]


#### Fn: `apply` (line 156)

<!-- Source: repos/clap/clap_builder/src/error/mod.rs:156 -->

<!-- Type: fn -->


Apply an alternative formatter to the error

# Example

```rust
# use clap_builder as clap;
# use clap::Command;
# use clap::Arg;
# use clap::error::KindFormatter;
let cmd = Command::new("foo")
.arg(Arg::new("input").required(true));
let matches = cmd
.try_get_matches_from(["foo", "input.txt"])
.map_err(|e| e.apply::<KindFormatter>())
.unwrap_or_else(|e| e.exit());
```


**Code Examples:**


```rust
# use clap_builder as clap;
# use clap::Command;
# use clap::Arg;
# use clap::error::KindFormatter;
let cmd = Command::new("foo")
.arg(Arg::new("input").required(true));
let matches = cmd
.try_get_matches_from(["foo", "input.txt"])
.map_err(|e| e.apply::<KindFormatter>())
.unwrap_or_else(|e| e.exit());
```


#### Fn: `kind` (line 179)

<!-- Source: repos/clap/clap_builder/src/error/mod.rs:179 -->

<!-- Type: fn -->


Type of error for programmatic processing


#### Fn: `context` (line 184)

<!-- Source: repos/clap/clap_builder/src/error/mod.rs:184 -->

<!-- Type: fn -->


Additional information to further qualify the error


#### Fn: `get` (line 190)

<!-- Source: repos/clap/clap_builder/src/error/mod.rs:190 -->

<!-- Type: fn -->


Lookup a piece of context


#### Fn: `insert` (line 197)

<!-- Source: repos/clap/clap_builder/src/error/mod.rs:197 -->

<!-- Type: fn -->


Insert a piece of context

If this `ContextKind` is already present, its value is replaced and the old value is returned.


#### Fn: `remove` (line 206)

<!-- Source: repos/clap/clap_builder/src/error/mod.rs:206 -->

<!-- Type: fn -->


Remove a piece of context, return the old value if any

The context is currently implemented in a vector, so `remove` takes
linear time.


#### Fn: `use_stderr` (line 216)

<!-- Source: repos/clap/clap_builder/src/error/mod.rs:216 -->

<!-- Type: fn -->


Should the message be written to `stdout` or not?


#### Fn: `exit_code` (line 229)

<!-- Source: repos/clap/clap_builder/src/error/mod.rs:229 -->

<!-- Type: fn -->


Returns the exit code that `.exit` will exit the process with.

When the error's kind would print to `stderr` this returns `2`,
else it returns `0`.


#### Fn: `exit` (line 241)

<!-- Source: repos/clap/clap_builder/src/error/mod.rs:241 -->

<!-- Type: fn -->


Prints the error and exits.

Depending on the error kind, this either prints to `stderr` and exits with a status of `2`
or prints to `stdout` and exits with a status of `0`.


#### Fn: `print` (line 251)

<!-- Source: repos/clap/clap_builder/src/error/mod.rs:251 -->

<!-- Type: fn -->


Prints formatted and colored error to `stdout` or `stderr` according to its error kind

# Example
```no_run
# use clap_builder as clap;
use clap::Command;

match Command::new("Command").try_get_matches() {
Ok(matches) => {
// do_something
},
Err(err) => {
err.print().expect("Error writing Error");
// do_something
},
};
```


**Code Examples:**


```rust
# use clap_builder as clap;
use clap::Command;

match Command::new("Command").try_get_matches() {
Ok(matches) => {
// do_something
},
Err(err) => {
err.print().expect("Error writing Error");
// do_something
},
};
```


#### Fn: `render` (line 282)

<!-- Source: repos/clap/clap_builder/src/error/mod.rs:282 -->

<!-- Type: fn -->


Render the error message to a [`StyledStr`].

# Example
```no_run
# use clap_builder as clap;
use clap::Command;

match Command::new("Command").try_get_matches() {
Ok(matches) => {
// do_something
},
Err(err) => {
let err = err.render();
println!("{err}");
// do_something
},
};
```


**Code Examples:**


```rust
# use clap_builder as clap;
use clap::Command;

match Command::new("Command").try_get_matches() {
Ok(matches) => {
// do_something
},
Err(err) => {
let err = err.render();
println!("{err}");
// do_something
},
};
```


#### Fn: `insert_context_unchecked` (line 339)

<!-- Source: repos/clap/clap_builder/src/error/mod.rs:339 -->

<!-- Type: fn -->


Does not verify if `ContextKind` is already present


#### Fn: `extend_context_unchecked` (line 351)

<!-- Source: repos/clap/clap_builder/src/error/mod.rs:351 -->

<!-- Type: fn -->


Does not verify if `ContextKind` is already present


### From `repos/clap/clap_builder/src/parser/error.rs`


#### Enum: `MatchesError` (line 3)

<!-- Source: repos/clap/clap_builder/src/parser/error.rs:3 -->

<!-- Type: enum -->


Violation of [`ArgMatches`][crate::ArgMatches] assumptions


---


## 10. Help and Usage Output {#help_output}


### From `repos/clap/clap_builder/src/output/help.rs`


#### Fn: `write_help` (line 8)

<!-- Source: repos/clap/clap_builder/src/output/help.rs:8 -->

<!-- Type: fn -->


Writes the parser help to the wrapped stream.


### From `repos/clap/clap_builder/src/output/help_template.rs`


#### Struct: `AutoHelp` (line 24)

<!-- Source: repos/clap/clap_builder/src/output/help_template.rs:24 -->

<!-- Type: struct -->


`clap` auto-generated help writer


#### Fn: `new` (line 31)

<!-- Source: repos/clap/clap_builder/src/output/help_template.rs:31 -->

<!-- Type: fn -->


Create a new `HelpTemplate` instance.


#### Struct: `HelpTemplate` (line 79)

<!-- Source: repos/clap/clap_builder/src/output/help_template.rs:79 -->

<!-- Type: struct -->


Help template writer

Wraps a writer stream providing different methods to generate help for `clap` objects.


#### Fn: `new` (line 94)

<!-- Source: repos/clap/clap_builder/src/output/help_template.rs:94 -->

<!-- Type: fn -->


Create a new `HelpTemplate` instance.


#### Fn: `write_templated_help` (line 157)

<!-- Source: repos/clap/clap_builder/src/output/help_template.rs:157 -->

<!-- Type: fn -->


Write help to stream for the parser in the format defined by the template.

For details about the template language see [`Command::help_template`].

[`Command::help_template`]: Command::help_template()


#### Impl: `HelpTemplate` (line 255)

<!-- Source: repos/clap/clap_builder/src/output/help_template.rs:255 -->

<!-- Type: impl -->


Basic template methods


#### Fn: `write_display_name` (line 257)

<!-- Source: repos/clap/clap_builder/src/output/help_template.rs:257 -->

<!-- Type: fn -->


Writes binary name of a Parser Object to the wrapped stream.


#### Fn: `write_bin_name` (line 272)

<!-- Source: repos/clap/clap_builder/src/output/help_template.rs:272 -->

<!-- Type: fn -->


Writes binary name of a Parser Object to the wrapped stream.


#### Impl: `HelpTemplate` (line 369)

<!-- Source: repos/clap/clap_builder/src/output/help_template.rs:369 -->

<!-- Type: impl -->


Arg handling


#### Fn: `write_all_args` (line 371)

<!-- Source: repos/clap/clap_builder/src/output/help_template.rs:371 -->

<!-- Type: fn -->


Writes help for all arguments (options, flags, args, subcommands)
including titles of a Parser Object to the wrapped stream.


#### Fn: `write_args` (line 468)

<!-- Source: repos/clap/clap_builder/src/output/help_template.rs:468 -->

<!-- Type: fn -->


Sorts arguments by length and display order and write their help to the wrapped stream.


#### Fn: `write_arg` (line 512)

<!-- Source: repos/clap/clap_builder/src/output/help_template.rs:512 -->

<!-- Type: fn -->


Writes help for an argument to the wrapped stream.


#### Fn: `short` (line 536)

<!-- Source: repos/clap/clap_builder/src/output/help_template.rs:536 -->

<!-- Type: fn -->


Writes argument's short command to the wrapped stream.


#### Fn: `long` (line 549)

<!-- Source: repos/clap/clap_builder/src/output/help_template.rs:549 -->

<!-- Type: fn -->


Writes argument's long command to the wrapped stream.


#### Fn: `align_to_about` (line 563)

<!-- Source: repos/clap/clap_builder/src/output/help_template.rs:563 -->

<!-- Type: fn -->


Write alignment padding between arg's switches/values and its about message.


#### Fn: `help` (line 606)

<!-- Source: repos/clap/clap_builder/src/output/help_template.rs:606 -->

<!-- Type: fn -->


Writes argument's help to the wrapped stream.


#### Fn: `will_args_wrap` (line 727)

<!-- Source: repos/clap/clap_builder/src/output/help_template.rs:727 -->

<!-- Type: fn -->


Will use next line help on writing args.


#### Impl: `HelpTemplate` (line 876)

<!-- Source: repos/clap/clap_builder/src/output/help_template.rs:876 -->

<!-- Type: impl -->


Subcommand handling


#### Fn: `subcmd` (line 1070)

<!-- Source: repos/clap/clap_builder/src/output/help_template.rs:1070 -->

<!-- Type: fn -->


Writes subcommand to the wrapped stream.


---


## 11. Styling and Formatting {#styling}


### From `repos/clap/clap_builder/src/builder/styled_str.rs`


#### Struct: `StyledStr` (line 4)

<!-- Source: repos/clap/clap_builder/src/builder/styled_str.rs:4 -->

<!-- Type: struct -->


Terminal-styling container

Styling may be encoded as [ANSI Escape Code](https://en.wikipedia.org/wiki/ANSI_escape_code)

# Examples

```rust
# use clap_builder as clap;
// `cstr!` converts tags to ANSI codes
let after_help: &'static str = color_print::cstr!(
r#"<bold><underline>Examples</underline></bold>

<dim>$</dim> <bold>mybin --input file.toml</bold>
"#);

let cmd = clap::Command::new("mybin")
.after_help(after_help)  // The `&str` gets converted into a `StyledStr`
// ...
#   ;
```


**Code Examples:**


```rust
# use clap_builder as clap;
// `cstr!` converts tags to ANSI codes
let after_help: &'static str = color_print::cstr!(
r#"<bold><underline>Examples</underline></bold>

<dim>$</dim> <bold>mybin --input file.toml</bold>
"#);

let cmd = clap::Command::new("mybin")
.after_help(after_help)  // The `&str` gets converted into a `StyledStr`
// ...
#   ;
```


#### Fn: `new` (line 28)

<!-- Source: repos/clap/clap_builder/src/builder/styled_str.rs:28 -->

<!-- Type: fn -->


Create an empty buffer


#### Fn: `ansi` (line 33)

<!-- Source: repos/clap/clap_builder/src/builder/styled_str.rs:33 -->

<!-- Type: fn -->


Display using [ANSI Escape Code](https://en.wikipedia.org/wiki/ANSI_escape_code) styling


#### Fn: `push_string` (line 39)

<!-- Source: repos/clap/clap_builder/src/builder/styled_str.rs:39 -->

<!-- Type: fn -->


May allow the compiler to consolidate the `Drop`s for `msg`, reducing code size compared to
`styled.push_str(&msg)`


#### Fn: `push_str` (line 45)

<!-- Source: repos/clap/clap_builder/src/builder/styled_str.rs:45 -->

<!-- Type: fn -->


Appends a given string slice onto the end of this `StyledStr`.


#### Impl: `Display` (line 212)

<!-- Source: repos/clap/clap_builder/src/builder/styled_str.rs:212 -->

<!-- Type: impl -->


Color-unaware printing. Never uses coloring.


### From `repos/clap/clap_builder/src/util/color.rs`


#### Enum: `ColorChoice` (line 4)

<!-- Source: repos/clap/clap_builder/src/util/color.rs:4 -->

<!-- Type: enum -->


Represents the color preferences for program output


#### Fn: `possible_values` (line 61)

<!-- Source: repos/clap/clap_builder/src/util/color.rs:61 -->

<!-- Type: fn -->


Report all `possible_values`


---


## 12. Shell Completions {#completions}


### From `repos/clap/clap_complete/src/aot/generator/mod.rs`


#### Module: `mod` (line 1)

<!-- Source: repos/clap/clap_complete/src/aot/generator/mod.rs:1 -->

<!-- Type: module -->


Shell completion machinery


#### Trait: `Generator` (line 13)

<!-- Source: repos/clap/clap_complete/src/aot/generator/mod.rs:13 -->

<!-- Type: trait -->


Generator trait which can be used to write generators


#### Fn: `file_name` (line 15)

<!-- Source: repos/clap/clap_complete/src/aot/generator/mod.rs:15 -->

<!-- Type: fn -->


Returns the file name that is created when this generator is called during compile time.

# Panics

May panic when called outside of the context of [`generate`] or [`generate_to`]

# Examples

```
# use std::io::{Error, Write};
# use clap::Command;
use clap_complete::Generator;

pub struct Fish;

impl Generator for Fish {
fn file_name(&self, name: &str) -> String {
format!("{name}.fish")
}
#   fn generate(&self, cmd: &Command, buf: &mut dyn Write) {}
#   fn try_generate(&self, cmd: &Command, buf: &mut dyn Write) -> Result<(), Error> {Ok(())}
}
```


**Code Examples:**


```rust
# use std::io::{Error, Write};
# use clap::Command;
use clap_complete::Generator;

pub struct Fish;

impl Generator for Fish {
fn file_name(&self, name: &str) -> String {
format!("{name}.fish")
}
#   fn generate(&self, cmd: &Command, buf: &mut dyn Write) {}
#   fn try_generate(&self, cmd: &Command, buf: &mut dyn Write) -> Result<(), Error> {Ok(())}
}
```


#### Fn: `generate` (line 40)

<!-- Source: repos/clap/clap_complete/src/aot/generator/mod.rs:40 -->

<!-- Type: fn -->


Generates output out of [`clap::Command`].

# Panics

May panic when called outside of the context of [`generate`] or [`generate_to`]

# Examples

The following example generator displays the [`clap::Command`]
as if it is printed using [`std::println`].

```
use std::{io::{Error, Write}, fmt::write};
use clap::Command;
use clap_complete::Generator;

pub struct ClapDebug;

impl Generator for ClapDebug {
#   fn file_name(&self, name: &str) -> String {
#       name.into()
#   }
fn generate(&self, cmd: &Command, buf: &mut dyn Write) {
write!(buf, "{cmd}").unwrap();
}
#   fn try_generate(&self, cmd: &Command, buf: &mut dyn Write) -> Result<(), Error> {
#       write!(buf, "{cmd}")
#   }
}
```


**Code Examples:**


```rust
use std::{io::{Error, Write}, fmt::write};
use clap::Command;
use clap_complete::Generator;

pub struct ClapDebug;

impl Generator for ClapDebug {
#   fn file_name(&self, name: &str) -> String {
#       name.into()
#   }
fn generate(&self, cmd: &Command, buf: &mut dyn Write) {
write!(buf, "{cmd}").unwrap();
}
#   fn try_generate(&self, cmd: &Command, buf: &mut dyn Write) -> Result<(), Error> {
#       write!(buf, "{cmd}")
#   }
}
```


#### Fn: `try_generate` (line 72)

<!-- Source: repos/clap/clap_complete/src/aot/generator/mod.rs:72 -->

<!-- Type: fn -->



Fallible version to generate output out of [`clap::Command`].

# Examples

The following example generator displays the [`clap::Command`]
as if it is printed using [`std::println`].

```
use std::{io::{Error, Write}, fmt::write};
use clap::Command;
use clap_complete::Generator;

pub struct ClapDebug;

impl Generator for ClapDebug {
#   fn file_name(&self, name: &str) -> String {
#       name.into()
#   }
#   fn generate(&self, cmd: &Command, buf: &mut dyn Write) {
#       self.try_generate(cmd, buf).expect("failed to write completion file");
#   }
fn try_generate(&self, cmd: &Command, buf: &mut dyn Write) -> Result<(), Error> {
write!(buf, "{cmd}")
}
}
```


**Code Examples:**


```rust
use std::{io::{Error, Write}, fmt::write};
use clap::Command;
use clap_complete::Generator;

pub struct ClapDebug;

impl Generator for ClapDebug {
#   fn file_name(&self, name: &str) -> String {
#       name.into()
#   }
#   fn generate(&self, cmd: &Command, buf: &mut dyn Write) {
#       self.try_generate(cmd, buf).expect("failed to write completion file");
#   }
fn try_generate(&self, cmd: &Command, buf: &mut dyn Write) -> Result<(), Error> {
write!(buf, "{cmd}")
}
}
```


#### Fn: `generate_to` (line 105)

<!-- Source: repos/clap/clap_complete/src/aot/generator/mod.rs:105 -->

<!-- Type: fn -->


Generate a completions file for a specified shell at compile-time.

<div class="warning">

**NOTE:** to generate the file at compile time you must use a `build.rs` "Build Script" or a
[`cargo-xtask`](https://github.com/matklad/cargo-xtask)

</div>

# Examples

The following example generates a bash completion script via a `build.rs` script. In this
simple example, we'll demo a very small application with only a single subcommand and two
args. Real applications could be many multiple levels deep in subcommands, and have tens or
potentially hundreds of arguments.

First, it helps if we separate out our `Command` definition into a separate file. Whether you
do this as a function, or bare Command definition is a matter of personal preference.

```
// src/cli.rs
# use clap::{Command, Arg, ArgAction};
pub fn build_cli() -> Command {
Command::new("compl")
.about("Tests completions")
.arg(Arg::new("file")
.help("some input file"))
.subcommand(Command::new("test")
.about("tests things")
.arg(Arg::new("case")
.long("case")
.action(ArgAction::Set)
.help("the case to test")))
}
```

In our regular code, we can simply call this `build_cli()` function, then call
`get_matches()`, or any of the other normal methods directly after. For example:

```ignore
// src/main.rs

mod cli;

fn main() {
let _m = cli::build_cli().get_matches();

// normal logic continues...
}
```

Next, we set up our `Cargo.toml` to use a `build.rs` build script.

```toml
# Cargo.toml
build = "build.rs"

[dependencies]
clap = "*"

[build-dependencies]
clap = "*"
clap_complete = "*"
```

Next, we place a `build.rs` in our project root.

```ignore
use clap_complete::{generate_to, shells::Bash};
use std::env;
use std::io::Error;

include!("src/cli.rs");

fn main() -> Result<(), Error> {
let outdir = match env::var_os("OUT_DIR") {
None => return Ok(()),
Some(outdir) => outdir,
};

let mut cmd = build_cli();
let path = generate_to(
Bash,
&mut cmd, // We need to specify what generator to use
"myapp",  // We need to specify the bin name manually
outdir,   // We need to specify where to write to
)?;

println!("cargo:warning=completion file is generated: {path:?}");

Ok(())
}
```

Now, once we compile there will be a `{bin_name}.bash` file in the directory.
Assuming we compiled with debug mode, it would be somewhere similar to
`<project>/target/debug/build/myapp-<hash>/out/myapp.bash`.

<div class="warning">

**NOTE:** Please look at the individual [shells][crate::shells]
to see the name of the files generated.

</div>

Using [`ValueEnum::value_variants()`][clap::ValueEnum::value_variants] you can easily loop over
all the supported shell variants to generate all the completions at once too.

```ignore
use clap::ValueEnum;
use clap_complete::{generate_to, Shell};
use std::env;
use std::io::Error;

include!("src/cli.rs");

fn main() -> Result<(), Error> {
let outdir = match env::var_os("OUT_DIR") {
None => return Ok(()),
Some(outdir) => outdir,
};

let mut cmd = build_cli();
for &shell in Shell::value_variants() {
generate_to(shell, &mut cmd, "myapp", outdir)?;
}

Ok(())
}
```


**Code Examples:**


```rust
// src/cli.rs
# use clap::{Command, Arg, ArgAction};
pub fn build_cli() -> Command {
Command::new("compl")
.about("Tests completions")
.arg(Arg::new("file")
.help("some input file"))
.subcommand(Command::new("test")
.about("tests things")
.arg(Arg::new("case")
.long("case")
.action(ArgAction::Set)
.help("the case to test")))
}
```


```rust
// src/main.rs

mod cli;

fn main() {
let _m = cli::build_cli().get_matches();

// normal logic continues...
}
```


```rust
Next, we place a `build.rs` in our project root.
```


```rust
Now, once we compile there will be a `{bin_name}.bash` file in the directory.
Assuming we compiled with debug mode, it would be somewhere similar to
`<project>/target/debug/build/myapp-<hash>/out/myapp.bash`.

<div class="warning">

**NOTE:** Please look at the individual [shells][crate::shells]
to see the name of the files generated.

</div>

Using [`ValueEnum::value_variants()`][clap::ValueEnum::value_variants] you can easily loop over
all the supported shell variants to generate all the completions at once too.
```


#### Fn: `generate` (line 258)

<!-- Source: repos/clap/clap_complete/src/aot/generator/mod.rs:258 -->

<!-- Type: fn -->


Generate a completions file for a specified shell at runtime.

Until `cargo install` can install extra files like a completion script, this may be
used e.g. in a command that outputs the contents of the completion script, to be
redirected into a file by the user.

# Examples

Assuming a separate `cli.rs` like the [`generate_to` example](generate_to()),
we can let users generate a completion script using a command:

```ignore
// src/main.rs

mod cli;
use std::io;
use clap_complete::{generate, shells::Bash};

fn main() {
let matches = cli::build_cli().get_matches();

if matches.is_present("generate-bash-completions") {
generate(Bash, &mut cli::build_cli(), "myapp", &mut io::stdout());
}

// normal logic continues...
}

```

Usage:

```console
$ myapp generate-bash-completions > /usr/share/bash-completion/completions/myapp.bash
```


**Code Examples:**


```rust
// src/main.rs

mod cli;
use std::io;
use clap_complete::{generate, shells::Bash};

fn main() {
let matches = cli::build_cli().get_matches();

if matches.is_present("generate-bash-completions") {
generate(Bash, &mut cli::build_cli(), "myapp", &mut io::stdout());
}

// normal logic continues...
}
```


### From `repos/clap/clap_complete/src/aot/generator/utils.rs`


#### Module: `utils` (line 1)

<!-- Source: repos/clap/clap_complete/src/aot/generator/utils.rs:1 -->

<!-- Type: module -->


Helpers for writing generators


#### Fn: `shorts_and_visible_aliases` (line 68)

<!-- Source: repos/clap/clap_complete/src/aot/generator/utils.rs:68 -->

<!-- Type: fn -->


Gets all the short options, their visible aliases and flags of a [`clap::Command`].
Includes `h` and `V` depending on the [`clap::Command`] settings.


#### Fn: `longs_and_visible_aliases` (line 93)

<!-- Source: repos/clap/clap_complete/src/aot/generator/utils.rs:93 -->

<!-- Type: fn -->


Gets all the long options, their visible aliases and flags of a [`clap::Command`].
Includes `help` and `version` depending on the [`clap::Command`] settings.


#### Fn: `flags` (line 123)

<!-- Source: repos/clap/clap_complete/src/aot/generator/utils.rs:123 -->

<!-- Type: fn -->


Gets all the flags of a [`clap::Command`].
Includes `help` and `version` depending on the [`clap::Command`] settings.


#### Fn: `possible_values` (line 133)

<!-- Source: repos/clap/clap_complete/src/aot/generator/utils.rs:133 -->

<!-- Type: fn -->


Get the possible values for completion


### From `repos/clap/clap_complete/src/aot/mod.rs`


#### Module: `mod` (line 1)

<!-- Source: repos/clap/clap_complete/src/aot/mod.rs:1 -->

<!-- Type: module -->


Prebuilt completions

## Quick Start

- For generating at compile-time, see [`generate_to`]
- For generating at runtime, see [`generate`]

[`Shell`] is a convenience `enum` for an argument value type that implements `Generator`
for each natively-supported shell type.

To customize completions, see
- [`ValueHint`]
- [`ValueEnum`][clap::ValueEnum]

## Example

```rust,no_run
use clap::{Command, Arg, ValueHint, value_parser, ArgAction};
use clap_complete::{generate, Generator, Shell};
use std::io;

fn build_cli() -> Command {
Command::new("example")
.arg(Arg::new("file")
.help("some input file")
.value_hint(ValueHint::AnyPath),
)
.arg(
Arg::new("generator")
.long("generate")
.action(ArgAction::Set)
.value_parser(value_parser!(Shell)),
)
}

fn print_completions<G: Generator>(generator: G, cmd: &mut Command) {
generate(generator, cmd, cmd.get_name().to_string(), &mut io::stdout());
}

fn main() {
let matches = build_cli().get_matches();

if let Some(generator) = matches.get_one::<Shell>("generator").copied() {
let mut cmd = build_cli();
eprintln!("Generating completion file for {generator}...");
print_completions(generator, &mut cmd);
}
}
```


### From `repos/clap/clap_complete/src/aot/shells/bash.rs`


#### Struct: `Bash` (line 10)

<!-- Source: repos/clap/clap_complete/src/aot/shells/bash.rs:10 -->

<!-- Type: struct -->


Generate bash completion file


### From `repos/clap/clap_complete/src/aot/shells/elvish.rs`


#### Struct: `Elvish` (line 9)

<!-- Source: repos/clap/clap_complete/src/aot/shells/elvish.rs:9 -->

<!-- Type: struct -->


Generate elvish completion file


### From `repos/clap/clap_complete/src/aot/shells/fish.rs`


#### Struct: `Fish` (line 7)

<!-- Source: repos/clap/clap_complete/src/aot/shells/fish.rs:7 -->

<!-- Type: struct -->


Generate fish completion file

Note: The fish generator currently only supports named options (-o/--option), not positional arguments.


### From `repos/clap/clap_complete/src/aot/shells/mod.rs`


#### Module: `mod` (line 1)

<!-- Source: repos/clap/clap_complete/src/aot/shells/mod.rs:1 -->

<!-- Type: module -->


Shell-specific generators


### From `repos/clap/clap_complete/src/aot/shells/powershell.rs`


#### Struct: `PowerShell` (line 9)

<!-- Source: repos/clap/clap_complete/src/aot/shells/powershell.rs:9 -->

<!-- Type: struct -->


Generate powershell completion file


### From `repos/clap/clap_complete/src/aot/shells/shell.rs`


#### Enum: `Shell` (line 12)

<!-- Source: repos/clap/clap_complete/src/aot/shells/shell.rs:12 -->

<!-- Type: enum -->


Shell with auto-generated completion script available.


#### Fn: `from_shell_path` (line 101)

<!-- Source: repos/clap/clap_complete/src/aot/shells/shell.rs:101 -->

<!-- Type: fn -->


Parse a shell from a path to the executable for the shell

# Examples

```
use clap_complete::shells::Shell;

assert_eq!(Shell::from_shell_path("/bin/bash"), Some(Shell::Bash));
assert_eq!(Shell::from_shell_path("/usr/bin/zsh"), Some(Shell::Zsh));
assert_eq!(Shell::from_shell_path("/opt/my_custom_shell"), None);
```


**Code Examples:**


```rust
use clap_complete::shells::Shell;

assert_eq!(Shell::from_shell_path("/bin/bash"), Some(Shell::Bash));
assert_eq!(Shell::from_shell_path("/usr/bin/zsh"), Some(Shell::Zsh));
assert_eq!(Shell::from_shell_path("/opt/my_custom_shell"), None);
```


#### Fn: `from_env` (line 116)

<!-- Source: repos/clap/clap_complete/src/aot/shells/shell.rs:116 -->

<!-- Type: fn -->


Determine the user's current shell from the environment

This will read the SHELL environment variable and try to determine which shell is in use
from that.

If SHELL is not set, then on windows, it will default to powershell, and on
other operating systems it will return `None`.

If SHELL is set, but contains a value that doesn't correspond to one of the supported shell
types, then return `None`.

# Example:

```no_run
# use clap::Command;
use clap_complete::{generate, shells::Shell};
# fn build_cli() -> Command {
#     Command::new("compl")
# }
let mut cmd = build_cli();
generate(Shell::from_env().unwrap_or(Shell::Bash), &mut cmd, "myapp", &mut std::io::stdout());
```


**Code Examples:**


```rust
# use clap::Command;
use clap_complete::{generate, shells::Shell};
# fn build_cli() -> Command {
#     Command::new("compl")
# }
let mut cmd = build_cli();
generate(Shell::from_env().unwrap_or(Shell::Bash), &mut cmd, "myapp", &mut std::io::stdout());
```


### From `repos/clap/clap_complete/src/aot/shells/zsh.rs`


#### Struct: `Zsh` (line 8)

<!-- Source: repos/clap/clap_complete/src/aot/shells/zsh.rs:8 -->

<!-- Type: struct -->


Generate zsh completion file


#### Fn: `escape_help` (line 429)

<!-- Source: repos/clap/clap_complete/src/aot/shells/zsh.rs:429 -->

<!-- Type: fn -->


Escape help string inside single quotes and brackets


#### Fn: `escape_value` (line 442)

<!-- Source: repos/clap/clap_complete/src/aot/shells/zsh.rs:442 -->

<!-- Type: fn -->


Escape value string inside single quotes and parentheses


### From `repos/clap/clap_complete/src/engine/candidate.rs`


#### Struct: `CompletionCandidate` (line 6)

<!-- Source: repos/clap/clap_complete/src/engine/candidate.rs:6 -->

<!-- Type: struct -->


A shell-agnostic completion candidate


#### Fn: `new` (line 18)

<!-- Source: repos/clap/clap_complete/src/engine/candidate.rs:18 -->

<!-- Type: fn -->


Create a new completion candidate


#### Fn: `help` (line 27)

<!-- Source: repos/clap/clap_complete/src/engine/candidate.rs:27 -->

<!-- Type: fn -->


Set the help message of the completion candidate


#### Fn: `id` (line 33)

<!-- Source: repos/clap/clap_complete/src/engine/candidate.rs:33 -->

<!-- Type: fn -->


Only first for a given Id is shown

To reduce the risk of conflicts, this should likely contain a namespace.


#### Fn: `tag` (line 41)

<!-- Source: repos/clap/clap_complete/src/engine/candidate.rs:41 -->

<!-- Type: fn -->


Group candidates by tag

Future: these may become user-visible


#### Fn: `display_order` (line 49)

<!-- Source: repos/clap/clap_complete/src/engine/candidate.rs:49 -->

<!-- Type: fn -->


Sort weight within a [`CompletionCandidate::tag`]


#### Fn: `hide` (line 55)

<!-- Source: repos/clap/clap_complete/src/engine/candidate.rs:55 -->

<!-- Type: fn -->


Set the visibility of the completion candidate

Only shown when there is no visible candidate for completing the current argument.


#### Fn: `add_prefix` (line 63)

<!-- Source: repos/clap/clap_complete/src/engine/candidate.rs:63 -->

<!-- Type: fn -->


Add a prefix to the value of completion candidate

This is generally used for post-process by [`complete`][crate::engine::complete()] for
things like pre-pending flags, merging delimiter-separated values, etc.


#### Impl: `CompletionCandidate` (line 76)

<!-- Source: repos/clap/clap_complete/src/engine/candidate.rs:76 -->

<!-- Type: impl -->


Reflection API


#### Fn: `get_value` (line 78)

<!-- Source: repos/clap/clap_complete/src/engine/candidate.rs:78 -->

<!-- Type: fn -->


Get the literal value being proposed for completion


#### Fn: `get_help` (line 83)

<!-- Source: repos/clap/clap_complete/src/engine/candidate.rs:83 -->

<!-- Type: fn -->


Get the help message of the completion candidate


#### Fn: `get_id` (line 88)

<!-- Source: repos/clap/clap_complete/src/engine/candidate.rs:88 -->

<!-- Type: fn -->


Get the id used for de-duplicating


#### Fn: `get_tag` (line 93)

<!-- Source: repos/clap/clap_complete/src/engine/candidate.rs:93 -->

<!-- Type: fn -->


Get the grouping tag


#### Fn: `get_display_order` (line 98)

<!-- Source: repos/clap/clap_complete/src/engine/candidate.rs:98 -->

<!-- Type: fn -->


Get the grouping tag


#### Fn: `is_hide_set` (line 103)

<!-- Source: repos/clap/clap_complete/src/engine/candidate.rs:103 -->

<!-- Type: fn -->


Get the visibility of the completion candidate


### From `repos/clap/clap_complete/src/engine/complete.rs`


#### Fn: `complete` (line 12)

<!-- Source: repos/clap/clap_complete/src/engine/complete.rs:12 -->

<!-- Type: fn -->


Complete the given command, shell-agnostic


#### Fn: `longs_and_visible_aliases` (line 476)

<!-- Source: repos/clap/clap_complete/src/engine/complete.rs:476 -->

<!-- Type: fn -->


Gets all the long options, their visible aliases and flags of a [`clap::Command`] with formatted `--` prefix.
Includes `help` and `version` depending on the [`clap::Command`] settings.


#### Fn: `hidden_longs_aliases` (line 493)

<!-- Source: repos/clap/clap_complete/src/engine/complete.rs:493 -->

<!-- Type: fn -->


Gets all the long hidden aliases and flags of a [`clap::Command`].


#### Fn: `shorts_and_visible_aliases` (line 509)

<!-- Source: repos/clap/clap_complete/src/engine/complete.rs:509 -->

<!-- Type: fn -->


Gets all the short options, their visible aliases and flags of a [`clap::Command`].
Includes `h` and `V` depending on the [`clap::Command`] settings.


#### Fn: `possible_values` (line 544)

<!-- Source: repos/clap/clap_complete/src/engine/complete.rs:544 -->

<!-- Type: fn -->


Get the possible values for completion


#### Fn: `parse_shortflags` (line 593)

<!-- Source: repos/clap/clap_complete/src/engine/complete.rs:593 -->

<!-- Type: fn -->


Parse the short flags and find the first `takes_values` option.


#### Fn: `parse_positional` (line 632)

<!-- Source: repos/clap/clap_complete/src/engine/complete.rs:632 -->

<!-- Type: fn -->


Parse the positional arguments. Return the new state and the new positional index.


#### Fn: `parse_opt_value` (line 683)

<!-- Source: repos/clap/clap_complete/src/engine/complete.rs:683 -->

<!-- Type: fn -->


Parse optional flag argument. Return new state


### From `repos/clap/clap_complete/src/engine/custom.rs`


#### Fn: `new` (line 47)

<!-- Source: repos/clap/clap_complete/src/engine/custom.rs:47 -->

<!-- Type: fn -->


Create a new `ArgValueCompleter` with a custom completer


#### Fn: `complete` (line 55)

<!-- Source: repos/clap/clap_complete/src/engine/custom.rs:55 -->

<!-- Type: fn -->


Candidates that match `current`

See [`CompletionCandidate`] for more information.


#### Trait: `ValueCompleter` (line 71)

<!-- Source: repos/clap/clap_complete/src/engine/custom.rs:71 -->

<!-- Type: trait -->


User-provided completion candidates for an [`Arg`][clap::Arg], see [`ArgValueCompleter`]

This is useful when predefined value hints are not enough.


#### Fn: `complete` (line 75)

<!-- Source: repos/clap/clap_complete/src/engine/custom.rs:75 -->

<!-- Type: fn -->


All potential candidates for an argument.

See [`CompletionCandidate`] for more information.


#### Fn: `new` (line 111)

<!-- Source: repos/clap/clap_complete/src/engine/custom.rs:111 -->

<!-- Type: fn -->


Create a new `ArgValueCandidates` with a custom completer


#### Fn: `candidates` (line 119)

<!-- Source: repos/clap/clap_complete/src/engine/custom.rs:119 -->

<!-- Type: fn -->


All potential candidates for an argument.

See [`CompletionCandidate`] for more information.


#### Fn: `new` (line 155)

<!-- Source: repos/clap/clap_complete/src/engine/custom.rs:155 -->

<!-- Type: fn -->


Create a new `SubcommandCandidates` with a custom completer


#### Fn: `candidates` (line 163)

<!-- Source: repos/clap/clap_complete/src/engine/custom.rs:163 -->

<!-- Type: fn -->


All potential candidates for an external subcommand.

See [`CompletionCandidate`] for more information.


#### Trait: `ValueCandidates` (line 179)

<!-- Source: repos/clap/clap_complete/src/engine/custom.rs:179 -->

<!-- Type: trait -->


User-provided completion candidates for an [`Arg`][clap::Arg], see [`ArgValueCandidates`]

User-provided completion candidates for an [`Subcommand`][clap::Subcommand], see [`SubcommandCandidates`]

This is useful when predefined value hints are not enough.


#### Fn: `candidates` (line 185)

<!-- Source: repos/clap/clap_complete/src/engine/custom.rs:185 -->

<!-- Type: fn -->


All potential candidates for an argument.

See [`CompletionCandidate`] for more information.


#### Struct: `PathCompleter` (line 200)

<!-- Source: repos/clap/clap_complete/src/engine/custom.rs:200 -->

<!-- Type: struct -->


Complete a value as a [`std::path::Path`]

# Example

```rust
use clap::Parser;
use clap_complete::engine::{ArgValueCompleter, PathCompleter};

#[derive(Debug, Parser)]
struct Cli {
#[arg(long, add = ArgValueCompleter::new(PathCompleter::file()))]
custom: Option<String>,
}
```


**Code Examples:**


```rust
use clap::Parser;
use clap_complete::engine::{ArgValueCompleter, PathCompleter};

#[derive(Debug, Parser)]
struct Cli {
#[arg(long, add = ArgValueCompleter::new(PathCompleter::file()))]
custom: Option<String>,
}
```


#### Fn: `any` (line 222)

<!-- Source: repos/clap/clap_complete/src/engine/custom.rs:222 -->

<!-- Type: fn -->


Any path is allowed


#### Fn: `file` (line 231)

<!-- Source: repos/clap/clap_complete/src/engine/custom.rs:231 -->

<!-- Type: fn -->


Complete only files


#### Fn: `dir` (line 236)

<!-- Source: repos/clap/clap_complete/src/engine/custom.rs:236 -->

<!-- Type: fn -->


Complete only directories


#### Fn: `stdio` (line 241)

<!-- Source: repos/clap/clap_complete/src/engine/custom.rs:241 -->

<!-- Type: fn -->


Include stdio (`-`)


#### Fn: `filter` (line 247)

<!-- Source: repos/clap/clap_complete/src/engine/custom.rs:247 -->

<!-- Type: fn -->


Select which paths should be completed


#### Fn: `current_dir` (line 256)

<!-- Source: repos/clap/clap_complete/src/engine/custom.rs:256 -->

<!-- Type: fn -->


Override [`std::env::current_dir`]


### From `repos/clap/clap_complete/src/engine/mod.rs`


#### Module: `mod` (line 1)

<!-- Source: repos/clap/clap_complete/src/engine/mod.rs:1 -->

<!-- Type: module -->


`clap`-native completion system

See [`complete()`]


### From `repos/clap/clap_complete/src/env/mod.rs`


#### Struct: `CompleteEnv` (line 77)

<!-- Source: repos/clap/clap_complete/src/env/mod.rs:77 -->

<!-- Type: struct -->


Environment-activated completions for your CLI

Benefits over a CLI completion argument or subcommand
- Performance: we don't need to generate [`clap::Command`] twice or parse arguments
- Flexibility: there is no concern over it interfering with other CLI logic

**Warning:** `stdout` should not be written to before [`CompleteEnv::complete`] has had a
chance to run.

# Examples

```rust
# use clap_complete::CompleteEnv;
fn cli() -> clap::Command {
// ...
#   clap::Command::new("empty")
}

fn main() {
CompleteEnv::with_factory(cli)
.complete()

// ... rest of application logic
}
```


**Code Examples:**


```rust
# use clap_complete::CompleteEnv;
fn cli() -> clap::Command {
// ...
#   clap::Command::new("empty")
}

fn main() {
CompleteEnv::with_factory(cli)
.complete()

// ... rest of application logic
}
```


#### Fn: `with_factory` (line 111)

<!-- Source: repos/clap/clap_complete/src/env/mod.rs:111 -->

<!-- Type: fn -->


Complete a [`clap::Command`]

# Example

Builder:
```rust
# use clap_complete::CompleteEnv;
fn cli() -> clap::Command {
// ...
#   clap::Command::new("empty")
}

fn main() {
CompleteEnv::with_factory(cli)
.complete()

// ... rest of application logic
}
```

Derive:
```
# use clap::Parser;
# use clap_complete::CompleteEnv;
use clap::CommandFactory as _;

#[derive(Debug, Parser)]
struct Cli {
custom: Option<String>,
}

fn main() {
CompleteEnv::with_factory(|| Cli::command())
.complete()

// ... rest of application logic
}
```


**Code Examples:**


```rust
# use clap_complete::CompleteEnv;
fn cli() -> clap::Command {
// ...
#   clap::Command::new("empty")
}

fn main() {
CompleteEnv::with_factory(cli)
.complete()

// ... rest of application logic
}
```


```rust
# use clap::Parser;
# use clap_complete::CompleteEnv;
use clap::CommandFactory as _;

#[derive(Debug, Parser)]
struct Cli {
custom: Option<String>,
}

fn main() {
CompleteEnv::with_factory(|| Cli::command())
.complete()

// ... rest of application logic
}
```


#### Fn: `var` (line 159)

<!-- Source: repos/clap/clap_complete/src/env/mod.rs:159 -->

<!-- Type: fn -->


Override the environment variable used for enabling completions


#### Fn: `bin` (line 165)

<!-- Source: repos/clap/clap_complete/src/env/mod.rs:165 -->

<!-- Type: fn -->


Override the name of the binary to complete

Default: `Command::get_bin_name`


#### Fn: `completer` (line 173)

<!-- Source: repos/clap/clap_complete/src/env/mod.rs:173 -->

<!-- Type: fn -->


Override the binary to call to get completions

Default: `args_os()[0]`


#### Fn: `shells` (line 181)

<!-- Source: repos/clap/clap_complete/src/env/mod.rs:181 -->

<!-- Type: fn -->


Override the shells supported for completions


#### Fn: `complete` (line 189)

<!-- Source: repos/clap/clap_complete/src/env/mod.rs:189 -->

<!-- Type: fn -->


Process the completion request and exit

**Warning:** `stdout` should not be written to before this has had a
chance to run.


#### Fn: `try_complete` (line 204)

<!-- Source: repos/clap/clap_complete/src/env/mod.rs:204 -->

<!-- Type: fn -->


Process the completion request

**Warning:** `stdout` should not be written to before or after this has run.

Returns `true` if a command was completed and `false` if this is a regular run of your
application


#### Struct: `Shells` (line 317)

<!-- Source: repos/clap/clap_complete/src/env/mod.rs:317 -->

<!-- Type: struct -->


Collection of shell-specific completers


#### Fn: `builtins` (line 321)

<!-- Source: repos/clap/clap_complete/src/env/mod.rs:321 -->

<!-- Type: fn -->


Select all of the built-in shells


#### Fn: `completer` (line 326)

<!-- Source: repos/clap/clap_complete/src/env/mod.rs:326 -->

<!-- Type: fn -->


Find the specified [`EnvCompleter`]


#### Fn: `names` (line 331)

<!-- Source: repos/clap/clap_complete/src/env/mod.rs:331 -->

<!-- Type: fn -->


Collect all [`EnvCompleter::name`]s


#### Fn: `iter` (line 336)

<!-- Source: repos/clap/clap_complete/src/env/mod.rs:336 -->

<!-- Type: fn -->


Iterate over [`EnvCompleter`]s


#### Trait: `EnvCompleter` (line 342)

<!-- Source: repos/clap/clap_complete/src/env/mod.rs:342 -->

<!-- Type: trait -->


Shell-integration for completions

This will generally be called by [`CompleteEnv`].

This handles adapting between the shell and [`completer`][crate::engine::complete()].
A `EnvCompleter` can choose how much of that lives within the registration script or
lives in [`EnvCompleter::write_complete`].


#### Fn: `name` (line 350)

<!-- Source: repos/clap/clap_complete/src/env/mod.rs:350 -->

<!-- Type: fn -->


Canonical name for this shell

**Post-conditions:**
```rust,ignore
assert!(completer.is(completer.name()));
```


#### Fn: `is` (line 357)

<!-- Source: repos/clap/clap_complete/src/env/mod.rs:357 -->

<!-- Type: fn -->


Whether the name matches this shell

This should match [`EnvCompleter::name`] and any alternative names, particularly used by
`$SHELL`.


#### Fn: `write_complete` (line 387)

<!-- Source: repos/clap/clap_complete/src/env/mod.rs:387 -->

<!-- Type: fn -->


Complete the given command

Adapt information from arguments and [`EnvCompleter::write_registration`]-defined env
variables to what is needed for [`completer`][crate::engine::complete()].

Write out the [`CompletionCandidate`][crate::engine::CompletionCandidate]s in a way the shell will understand.


### From `repos/clap/clap_complete/src/env/shells.rs`


#### Struct: `Bash` (line 6)

<!-- Source: repos/clap/clap_complete/src/env/shells.rs:6 -->

<!-- Type: struct -->


Bash completion adapter


#### Enum: `CompType` (line 103)

<!-- Source: repos/clap/clap_complete/src/env/shells.rs:103 -->

<!-- Type: enum -->


Type of completion attempted that caused a completion function to be called


#### Struct: `Elvish` (line 140)

<!-- Source: repos/clap/clap_complete/src/env/shells.rs:140 -->

<!-- Type: struct -->


Elvish completion adapter


#### Struct: `Fish` (line 202)

<!-- Source: repos/clap/clap_complete/src/env/shells.rs:202 -->

<!-- Type: struct -->


Fish completion adapter


#### Struct: `Powershell` (line 255)

<!-- Source: repos/clap/clap_complete/src/env/shells.rs:255 -->

<!-- Type: struct -->


Powershell completion adapter


#### Struct: `Zsh` (line 347)

<!-- Source: repos/clap/clap_complete/src/env/shells.rs:347 -->

<!-- Type: struct -->


Zsh completion adapter


#### Fn: `escape_value` (line 457)

<!-- Source: repos/clap/clap_complete/src/env/shells.rs:457 -->

<!-- Type: fn -->


Escape value string


#### Fn: `escape_help` (line 462)

<!-- Source: repos/clap/clap_complete/src/env/shells.rs:462 -->

<!-- Type: fn -->


Escape help string


### From `repos/clap/clap_complete/src/lib.rs`


#### Module: `lib` (line 8)

<!-- Source: repos/clap/clap_complete/src/lib.rs:8 -->

<!-- Type: module -->


## Quick Start

- For generating at compile-time, see [`generate_to`]
- For generating at runtime, see [`generate`]

[`Shell`] is a convenience `enum` for an argument value type that implements `Generator`
for each natively-supported shell type.

## Example

```rust,no_run
use clap::{Command, Arg, ValueHint, value_parser, ArgAction};
use clap_complete::aot::{generate, Generator, Shell};
use std::io;

fn build_cli() -> Command {
Command::new("example")
.arg(Arg::new("file")
.help("some input file")
.value_hint(ValueHint::AnyPath))
.arg(Arg::new("generator")
.long("generate")
.action(ArgAction::Set)
.value_parser(value_parser!(Shell)))
}

fn print_completions<G: Generator>(generator: G, cmd: &mut Command) {
generate(generator, cmd, cmd.get_name().to_string(), &mut io::stdout());
}

fn main() {
let matches = build_cli().get_matches();

if let Some(generator) = matches.get_one::<Shell>("generator").copied() {
let mut cmd = build_cli();
eprintln!("Generating completion file for {generator}...");
print_completions(generator, &mut cmd);
}
}
```


---


## 14. Other Topics {#other}


### From `repos/clap/clap_builder/src/builder/action.rs`


#### Fn: `takes_values` (line 356)

<!-- Source: repos/clap/clap_builder/src/builder/action.rs:356 -->

<!-- Type: fn -->


Returns whether this action accepts values on the command-line

[`default_values`][super::Arg::default_values] and [`env`][super::Arg::env] may still be
processed.


### From `repos/clap/clap_builder/src/builder/app_settings.rs`


#### Enum: `AppSettings` (line 36)

<!-- Source: repos/clap/clap_builder/src/builder/app_settings.rs:36 -->

<!-- Type: enum -->


Application level settings, which affect how [`Command`] operates

<div class="warning">

**NOTE:** When these settings are used, they apply only to current command, and are *not*
propagated down or up through child or parent subcommands

</div>

[`Command`]: crate::Command


### From `repos/clap/clap_builder/src/builder/debug_asserts.rs`


#### Fn: `find_duplicates` (line 456)

<!-- Source: repos/clap/clap_builder/src/builder/debug_asserts.rs:456 -->

<!-- Type: fn -->


Find duplicates in a sorted array.

The algorithm is simple: the array is sorted, duplicates
must be placed next to each other, we can check only adjacent elements.


### From `repos/clap/clap_builder/src/builder/mod.rs`


#### Module: `mod` (line 1)

<!-- Source: repos/clap/clap_builder/src/builder/mod.rs:1 -->

<!-- Type: module -->


Define [`Command`] line [arguments][`Arg`]


### From `repos/clap/clap_builder/src/builder/os_str.rs`


#### Struct: `OsStr` (line 5)

<!-- Source: repos/clap/clap_builder/src/builder/os_str.rs:5 -->

<!-- Type: struct -->


A UTF-8-encoded fixed string

<div class="warning">

**NOTE:** To support dynamic values (i.e. `OsString`), enable the `string`
feature

</div>


#### Fn: `as_os_str` (line 39)

<!-- Source: repos/clap/clap_builder/src/builder/os_str.rs:39 -->

<!-- Type: fn -->


Get the raw string as an `std::ffi::OsStr`


#### Fn: `to_os_string` (line 44)

<!-- Source: repos/clap/clap_builder/src/builder/os_str.rs:44 -->

<!-- Type: fn -->


Get the raw string as an `OsString`


### From `repos/clap/clap_builder/src/builder/range.rs`


#### Struct: `ValueRange` (line 1)

<!-- Source: repos/clap/clap_builder/src/builder/range.rs:1 -->

<!-- Type: struct -->


Values per occurrence for an argument


#### Const: `EMPTY` (line 9)

<!-- Source: repos/clap/clap_builder/src/builder/range.rs:9 -->

<!-- Type: const -->


Nor argument values, or a flag


#### Const: `SINGLE` (line 15)

<!-- Source: repos/clap/clap_builder/src/builder/range.rs:15 -->

<!-- Type: const -->


A single argument value, the most common case for options


#### Fn: `new` (line 32)

<!-- Source: repos/clap/clap_builder/src/builder/range.rs:32 -->

<!-- Type: fn -->


Create a range

# Panics

If the end is less than the start (debug builds)

# Examples

```rust
# use clap_builder as clap;
# use clap::builder::ValueRange;
let range = ValueRange::new(5);
let range = ValueRange::new(5..10);
let range = ValueRange::new(5..=10);
let range = ValueRange::new(5..);
let range = ValueRange::new(..10);
let range = ValueRange::new(..=10);
```

While this will panic:
```should_panic
# use clap_builder as clap;
# use clap::builder::ValueRange;
let range = ValueRange::new(10..5);  // Panics!
```


**Code Examples:**


```rust
# use clap_builder as clap;
# use clap::builder::ValueRange;
let range = ValueRange::new(5);
let range = ValueRange::new(5..10);
let range = ValueRange::new(5..=10);
let range = ValueRange::new(5..);
let range = ValueRange::new(..10);
let range = ValueRange::new(..=10);
```


```rust
# use clap_builder as clap;
# use clap::builder::ValueRange;
let range = ValueRange::new(10..5);  // Panics!
```


#### Fn: `min_values` (line 69)

<!-- Source: repos/clap/clap_builder/src/builder/range.rs:69 -->

<!-- Type: fn -->


Fewest number of values the argument accepts


#### Fn: `max_values` (line 74)

<!-- Source: repos/clap/clap_builder/src/builder/range.rs:74 -->

<!-- Type: fn -->


Most number of values the argument accepts


#### Fn: `takes_values` (line 79)

<!-- Source: repos/clap/clap_builder/src/builder/range.rs:79 -->

<!-- Type: fn -->


Report whether the argument takes any values (ie is a flag)

# Examples

```rust
# use clap_builder as clap;
# use clap::builder::ValueRange;
let range = ValueRange::new(5);
assert!(range.takes_values());

let range = ValueRange::new(0);
assert!(!range.takes_values());
```


**Code Examples:**


```rust
# use clap_builder as clap;
# use clap::builder::ValueRange;
let range = ValueRange::new(5);
assert!(range.takes_values());

let range = ValueRange::new(0);
assert!(!range.takes_values());
```


### From `repos/clap/clap_builder/src/builder/resettable.rs`


#### Enum: `Resettable` (line 12)

<!-- Source: repos/clap/clap_builder/src/builder/resettable.rs:12 -->

<!-- Type: enum -->


Clearable builder value

This allows a builder function to both accept any value that can [`Into::into`] `T` (like
`&str` into `OsStr`) as well as `None` to reset it to the default.  This is needed to
workaround a limitation where you can't have a function argument that is `impl Into<Option<T>>`
where `T` is `impl Into<S>` accept `None` as its type is ambiguous.

# Example

```rust
# use clap_builder as clap;
# use clap::Command;
# use clap::Arg;
fn common() -> Command {
Command::new("cli")
.arg(Arg::new("input").short('i').long("input"))
}
let mut command = common();
command.mut_arg("input", |arg| arg.short(None));
```


**Code Examples:**


```rust
# use clap_builder as clap;
# use clap::Command;
# use clap::Arg;
fn common() -> Command {
Command::new("cli")
.arg(Arg::new("input").short('i').long("input"))
}
let mut command = common();
command.mut_arg("input", |arg| arg.short(None));
```


#### Trait: `IntoResettable` (line 64)

<!-- Source: repos/clap/clap_builder/src/builder/resettable.rs:64 -->

<!-- Type: trait -->


Convert to the intended resettable type


#### Fn: `into_resettable` (line 66)

<!-- Source: repos/clap/clap_builder/src/builder/resettable.rs:66 -->

<!-- Type: fn -->


Convert to the intended resettable type


### From `repos/clap/clap_builder/src/builder/str.rs`


#### Struct: `Str` (line 4)

<!-- Source: repos/clap/clap_builder/src/builder/str.rs:4 -->

<!-- Type: struct -->


A UTF-8-encoded fixed string

<div class="warning">

**NOTE:** To support dynamic values (i.e. `String`), enable the `string`
feature

</div>


#### Fn: `as_str` (line 42)

<!-- Source: repos/clap/clap_builder/src/builder/str.rs:42 -->

<!-- Type: fn -->


Get the raw string of the `Str`


### From `repos/clap/clap_builder/src/builder/styling.rs`


#### Module: `styling` (line 1)

<!-- Source: repos/clap/clap_builder/src/builder/styling.rs:1 -->

<!-- Type: module -->


Terminal [`Styles`] for help and error output


#### Struct: `Styles` (line 5)

<!-- Source: repos/clap/clap_builder/src/builder/styling.rs:5 -->

<!-- Type: struct -->


Terminal styling definitions

See also [`Command::styles`][crate::Command::styles].

# Example

clap v3 styling
```rust
# use clap_builder as clap;
# use clap::builder::styling::*;
let styles = Styles::styled()
.header(AnsiColor::Yellow.on_default())
.usage(AnsiColor::Green.on_default())
.literal(AnsiColor::Green.on_default())
.placeholder(AnsiColor::Green.on_default());
```


**Code Examples:**


```rust
# use clap_builder as clap;
# use clap::builder::styling::*;
let styles = Styles::styled()
.header(AnsiColor::Yellow.on_default())
.usage(AnsiColor::Green.on_default())
.literal(AnsiColor::Green.on_default())
.placeholder(AnsiColor::Green.on_default());
```


#### Fn: `plain` (line 36)

<!-- Source: repos/clap/clap_builder/src/builder/styling.rs:36 -->

<!-- Type: fn -->


No terminal styling


#### Fn: `styled` (line 51)

<!-- Source: repos/clap/clap_builder/src/builder/styling.rs:51 -->

<!-- Type: fn -->


Default terminal styling


#### Fn: `header` (line 75)

<!-- Source: repos/clap/clap_builder/src/builder/styling.rs:75 -->

<!-- Type: fn -->


General Heading style, e.g. [`help_heading`][crate::Arg::help_heading]


#### Fn: `error` (line 82)

<!-- Source: repos/clap/clap_builder/src/builder/styling.rs:82 -->

<!-- Type: fn -->


Error heading


#### Fn: `usage` (line 89)

<!-- Source: repos/clap/clap_builder/src/builder/styling.rs:89 -->

<!-- Type: fn -->


Usage heading


#### Fn: `literal` (line 96)

<!-- Source: repos/clap/clap_builder/src/builder/styling.rs:96 -->

<!-- Type: fn -->


Literal command-line syntax, e.g. `--help`


#### Fn: `placeholder` (line 103)

<!-- Source: repos/clap/clap_builder/src/builder/styling.rs:103 -->

<!-- Type: fn -->


Descriptions within command-line syntax, e.g. [`value_name`][crate::Arg::value_name]


#### Fn: `valid` (line 110)

<!-- Source: repos/clap/clap_builder/src/builder/styling.rs:110 -->

<!-- Type: fn -->


Highlight suggested usage


#### Fn: `context` (line 124)

<!-- Source: repos/clap/clap_builder/src/builder/styling.rs:124 -->

<!-- Type: fn -->


Highlight all specified contexts, e.g. `[default: false]`

To specialize the style of the value within the context, see [`Styles::context_value`]


#### Fn: `context_value` (line 133)

<!-- Source: repos/clap/clap_builder/src/builder/styling.rs:133 -->

<!-- Type: fn -->


Highlight values within all of the context, e.g. the `false` in `[default: false]`

If not explicitly set, falls back to `context`'s style.


#### Impl: `Styles` (line 143)

<!-- Source: repos/clap/clap_builder/src/builder/styling.rs:143 -->

<!-- Type: impl -->


Reflection


#### Fn: `get_header` (line 145)

<!-- Source: repos/clap/clap_builder/src/builder/styling.rs:145 -->

<!-- Type: fn -->


General Heading style, e.g. [`help_heading`][crate::Arg::help_heading]


#### Fn: `get_error` (line 151)

<!-- Source: repos/clap/clap_builder/src/builder/styling.rs:151 -->

<!-- Type: fn -->


Error heading


#### Fn: `get_usage` (line 157)

<!-- Source: repos/clap/clap_builder/src/builder/styling.rs:157 -->

<!-- Type: fn -->


Usage heading


#### Fn: `get_literal` (line 163)

<!-- Source: repos/clap/clap_builder/src/builder/styling.rs:163 -->

<!-- Type: fn -->


Literal command-line syntax, e.g. `--help`


#### Fn: `get_placeholder` (line 169)

<!-- Source: repos/clap/clap_builder/src/builder/styling.rs:169 -->

<!-- Type: fn -->


Descriptions within command-line syntax, e.g. [`value_name`][crate::Arg::value_name]


#### Fn: `get_valid` (line 175)

<!-- Source: repos/clap/clap_builder/src/builder/styling.rs:175 -->

<!-- Type: fn -->


Highlight suggested usage


#### Fn: `get_context` (line 187)

<!-- Source: repos/clap/clap_builder/src/builder/styling.rs:187 -->

<!-- Type: fn -->


Highlight all specified contexts, e.g. `[default: false]`

To specialize the style of the value within the context, see [`Styles::context_value`]


#### Fn: `get_context_value` (line 195)

<!-- Source: repos/clap/clap_builder/src/builder/styling.rs:195 -->

<!-- Type: fn -->


Highlight values within all of the context, e.g. the `false` in `[default: false]`

If not explicitly set, falls back to `context`'s style.


### From `repos/clap/clap_builder/src/derive.rs`


#### Module: `derive` (line 1)

<!-- Source: repos/clap/clap_builder/src/derive.rs:1 -->

<!-- Type: module -->


This module contains traits that are usable with the `#[derive(...)]`
macros in `clap_derive`.


#### Trait: `Parser` (line 10)

<!-- Source: repos/clap/clap_builder/src/derive.rs:10 -->

<!-- Type: trait -->


Parse command-line arguments into `Self`.

The primary one-stop-shop trait used to create an instance of a `clap`
[`Command`], conduct the parsing, and turn the resulting [`ArgMatches`] back
into concrete instance of the user struct.

This trait is primarily a convenience on top of [`FromArgMatches`] +
[`CommandFactory`] which uses those two underlying traits to build the two
fundamental functions `parse` which uses the `std::env::args_os` iterator,
and `parse_from` which allows the consumer to supply the iterator (along
with fallible options for each).

See also [`Subcommand`] and [`Args`].

<div class="warning">

**NOTE:** Deriving requires the `derive` feature flag

</div>


#### Fn: `parse` (line 30)

<!-- Source: repos/clap/clap_builder/src/derive.rs:30 -->

<!-- Type: fn -->


Parse from `std::env::args_os()`, [exit][Error::exit] on error.


#### Fn: `try_parse` (line 45)

<!-- Source: repos/clap/clap_builder/src/derive.rs:45 -->

<!-- Type: fn -->


Parse from `std::env::args_os()`, return Err on error.


#### Fn: `parse_from` (line 51)

<!-- Source: repos/clap/clap_builder/src/derive.rs:51 -->

<!-- Type: fn -->


Parse from iterator, [exit][Error::exit] on error.


#### Fn: `try_parse_from` (line 70)

<!-- Source: repos/clap/clap_builder/src/derive.rs:70 -->

<!-- Type: fn -->


Parse from iterator, return Err on error.


#### Fn: `update_from` (line 80)

<!-- Source: repos/clap/clap_builder/src/derive.rs:80 -->

<!-- Type: fn -->


Update from iterator, [exit][Error::exit] on error.

Unlike [`Parser::parse`], this works with an existing instance of `self`.
The assumption is that all required fields are already provided and any [`Args`] or
[`Subcommand`]s provided by the user will modify only what is specified.


#### Fn: `try_update_from` (line 100)

<!-- Source: repos/clap/clap_builder/src/derive.rs:100 -->

<!-- Type: fn -->


Update from iterator, return Err on error.


#### Trait: `FromArgMatches` (line 127)

<!-- Source: repos/clap/clap_builder/src/derive.rs:127 -->

<!-- Type: trait -->


Converts an instance of [`ArgMatches`] to a user-defined container.

Derived as part of [`Parser`], [`Args`], and [`Subcommand`].


#### Fn: `from_arg_matches` (line 131)

<!-- Source: repos/clap/clap_builder/src/derive.rs:131 -->

<!-- Type: fn -->


Instantiate `Self` from [`ArgMatches`], parsing the arguments as needed.

Motivation: If our application had two CLI options, `--name
<STRING>` and the flag `--debug`, we may create a struct as follows:

```rust
# #[cfg(feature = "derive")] {
struct Context {
name: String,
debug: bool
}
# }
```

We then need to convert the `ArgMatches` that `clap` generated into our struct.
`from_arg_matches` serves as the equivalent of:

```rust
# #[cfg(feature = "derive")] {
# use clap::ArgMatches;
# struct Context {
#   name: String,
#   debug: bool
# }
impl From<ArgMatches> for Context {
fn from(m: ArgMatches) -> Self {
Context {
name: m.get_one::<String>("name").unwrap().clone(),
debug: m.get_flag("debug"),
}
}
}
# }
```


**Code Examples:**


```rust
# #[cfg(feature = "derive")] {
struct Context {
name: String,
debug: bool
}
# }
```


```rust
# #[cfg(feature = "derive")] {
# use clap::ArgMatches;
# struct Context {
#   name: String,
#   debug: bool
# }
impl From<ArgMatches> for Context {
fn from(m: ArgMatches) -> Self {
Context {
name: m.get_one::<String>("name").unwrap().clone(),
debug: m.get_flag("debug"),
}
}
}
# }
```


#### Fn: `from_arg_matches_mut` (line 167)

<!-- Source: repos/clap/clap_builder/src/derive.rs:167 -->

<!-- Type: fn -->


Instantiate `Self` from [`ArgMatches`], parsing the arguments as needed.

Motivation: If our application had two CLI options, `--name
<STRING>` and the flag `--debug`, we may create a struct as follows:

```rust
# #[cfg(feature = "derive")] {
struct Context {
name: String,
debug: bool
}
# }
```

We then need to convert the `ArgMatches` that `clap` generated into our struct.
`from_arg_matches_mut` serves as the equivalent of:

```rust
# #[cfg(feature = "derive")] {
# use clap::ArgMatches;
# struct Context {
#   name: String,
#   debug: bool
# }
impl From<ArgMatches> for Context {
fn from(m: ArgMatches) -> Self {
Context {
name: m.get_one::<String>("name").unwrap().to_string(),
debug: m.get_flag("debug"),
}
}
}
# }
```


**Code Examples:**


```rust
# #[cfg(feature = "derive")] {
struct Context {
name: String,
debug: bool
}
# }
```


```rust
# #[cfg(feature = "derive")] {
# use clap::ArgMatches;
# struct Context {
#   name: String,
#   debug: bool
# }
impl From<ArgMatches> for Context {
fn from(m: ArgMatches) -> Self {
Context {
name: m.get_one::<String>("name").unwrap().to_string(),
debug: m.get_flag("debug"),
}
}
}
# }
```


#### Fn: `update_from_arg_matches` (line 205)

<!-- Source: repos/clap/clap_builder/src/derive.rs:205 -->

<!-- Type: fn -->


Assign values from `ArgMatches` to `self`.


#### Fn: `update_from_arg_matches_mut` (line 208)

<!-- Source: repos/clap/clap_builder/src/derive.rs:208 -->

<!-- Type: fn -->


Assign values from `ArgMatches` to `self`.


#### Trait: `Args` (line 214)

<!-- Source: repos/clap/clap_builder/src/derive.rs:214 -->

<!-- Type: trait -->


Parse a set of arguments into a user-defined container.

Implementing this trait lets a parent container delegate argument parsing behavior to `Self`.
with:
- `#[command(flatten)] args: ChildArgs`: Attribute can only be used with struct fields that impl
`Args`.
- `Variant(ChildArgs)`: No attribute is used with enum variants that impl `Args`.

<div class="warning">

**NOTE:** Deriving requires the `derive` feature flag

</div>


#### Fn: `group_id` (line 228)

<!-- Source: repos/clap/clap_builder/src/derive.rs:228 -->

<!-- Type: fn -->


Report the [`ArgGroup::id`][crate::ArgGroup::id] for this set of arguments


#### Fn: `augment_args` (line 232)

<!-- Source: repos/clap/clap_builder/src/derive.rs:232 -->

<!-- Type: fn -->


Append to [`Command`] so it can instantiate `Self` via
[`FromArgMatches::from_arg_matches_mut`]

This is used to implement `#[command(flatten)]`

See also [`CommandFactory::command`].


#### Fn: `augment_args_for_update` (line 239)

<!-- Source: repos/clap/clap_builder/src/derive.rs:239 -->

<!-- Type: fn -->


Append to [`Command`] so it can instantiate `self` via
[`FromArgMatches::update_from_arg_matches_mut`]

This is used to implement `#[command(flatten)]`

See also [`CommandFactory::command_for_update`].


#### Trait: `ValueEnum` (line 281)

<!-- Source: repos/clap/clap_builder/src/derive.rs:281 -->

<!-- Type: trait -->


Parse arguments into enums.

When deriving [`Parser`], a field whose type implements `ValueEnum` can have the attribute
`#[arg(value_enum)]` which will
- Call [`EnumValueParser`][crate::builder::EnumValueParser]
- Allowing using the `#[arg(default_value_t)]` attribute without implementing `Display`.

<div class="warning">

**NOTE:** Deriving requires the `derive` feature flag

</div>


#### Fn: `value_variants` (line 294)

<!-- Source: repos/clap/clap_builder/src/derive.rs:294 -->

<!-- Type: fn -->


All possible argument values, in display order.


#### Fn: `from_str` (line 297)

<!-- Source: repos/clap/clap_builder/src/derive.rs:297 -->

<!-- Type: fn -->


Parse an argument into `Self`.


#### Fn: `to_possible_value` (line 310)

<!-- Source: repos/clap/clap_builder/src/derive.rs:310 -->

<!-- Type: fn -->


The canonical argument value.

The value is `None` for skipped variants.


### From `repos/clap/clap_builder/src/lib.rs`


#### Type: `Error` (line 25)

<!-- Source: repos/clap/clap_builder/src/lib.rs:25 -->

<!-- Type: type -->


Command Line Argument Parser Error

See [`Command::error`] to create an error.

[`Command::error`]: crate::Command::error


### From `repos/clap/clap_builder/src/mkeymap.rs`


#### Fn: `contains` (line 83)

<!-- Source: repos/clap/clap_builder/src/mkeymap.rs:83 -->

<!-- Type: fn -->


If any arg has corresponding key in this map, we can search the key with
`u64` (for positional argument), `char` (for short flag), `&str` and `OsString`
(for long flag)


#### Fn: `push` (line 93)

<!-- Source: repos/clap/clap_builder/src/mkeymap.rs:93 -->

<!-- Type: fn -->


Push an argument in the map.


#### Fn: `get` (line 98)

<!-- Source: repos/clap/clap_builder/src/mkeymap.rs:98 -->

<!-- Type: fn -->


Find the arg have corresponding key in this map, we can search the key
with `u64` (for positional argument), `char` (for short flag), `&str` and
`OsString` (for long flag)


#### Fn: `keys` (line 111)

<!-- Source: repos/clap/clap_builder/src/mkeymap.rs:111 -->

<!-- Type: fn -->


Return iterators of all keys.


#### Fn: `args` (line 116)

<!-- Source: repos/clap/clap_builder/src/mkeymap.rs:116 -->

<!-- Type: fn -->


Return iterators of all args.


#### Fn: `args_mut` (line 121)

<!-- Source: repos/clap/clap_builder/src/mkeymap.rs:121 -->

<!-- Type: fn -->


Return mutable iterators of all args.


#### Fn: `mut_args` (line 126)

<!-- Source: repos/clap/clap_builder/src/mkeymap.rs:126 -->

<!-- Type: fn -->


Mutate every argument.


#### Fn: `_build` (line 135)

<!-- Source: repos/clap/clap_builder/src/mkeymap.rs:135 -->

<!-- Type: fn -->


We need a lazy build here since some we may change args after creating
the map, you can checkout who uses `args_mut`.


#### Fn: `remove_by_name` (line 145)

<!-- Source: repos/clap/clap_builder/src/mkeymap.rs:145 -->

<!-- Type: fn -->


Remove an arg in the graph by Id, usually used by `mut_arg`. Return
`Some(arg)` if removed.


#### Fn: `append_keys` (line 164)

<!-- Source: repos/clap/clap_builder/src/mkeymap.rs:164 -->

<!-- Type: fn -->


Generate key types for an specific Arg.


### From `repos/clap/clap_builder/src/output/fmt.rs`


#### Impl: `Colorizer` (line 33)

<!-- Source: repos/clap/clap_builder/src/output/fmt.rs:33 -->

<!-- Type: impl -->


Printing methods.


#### Impl: `Display` (line 78)

<!-- Source: repos/clap/clap_builder/src/output/fmt.rs:78 -->

<!-- Type: impl -->


Color-unaware printing. Never uses coloring.


### From `repos/clap/clap_builder/src/output/textwrap/core.rs`


#### Fn: `display_width` (line 1)

<!-- Source: repos/clap/clap_builder/src/output/textwrap/core.rs:1 -->

<!-- Type: fn -->


Compute the display width of `text`

# Examples

**Note:** When the `unicode` Cargo feature is disabled, all characters are presumed to take up
1 width.  With the feature enabled, function will correctly deal with [combining characters] in
their decomposed form (see [Unicode equivalence]).

An example of a decomposed character is “é”, which can be decomposed into: “e” followed by a
combining acute accent: “◌́”.  Without the `unicode` Cargo feature, every `char` has a width of
1. This includes the combining accent:

## Emojis and CJK Characters

Characters such as emojis and [CJK characters] used in the
Chinese, Japanese, and Korean languages are seen as double-width,
even if the `unicode-width` feature is disabled:

# Limitations

The displayed width of a string cannot always be computed from the
string alone. This is because the width depends on the rendering
engine used. This is particularly visible with [emoji modifier
sequences] where a base emoji is modified with, e.g., skin tone or
hair color modifiers. It is up to the rendering engine to detect
this and to produce a suitable emoji.

A simple example is “❤️”, which consists of “❤” (U+2764: Black
Heart Symbol) followed by U+FE0F (Variation Selector-16). By
itself, “❤” is a black heart, but if you follow it with the
variant selector, you may get a wider red heart.

A more complex example would be “👨‍🦰” which should depict a man
with red hair. Here the computed width is too large — and the
width differs depending on the use of the `unicode-width` feature:

This happens because the grapheme consists of three code points:
“👨” (U+1F468: Man), Zero Width Joiner (U+200D), and “🦰”
(U+1F9B0: Red Hair). You can see them above in the test. With
`unicode-width` enabled, the ZWJ is correctly seen as having zero
width, without it is counted as a double-width character.

## Terminal Support

Modern browsers typically do a great job at combining characters
as shown above, but terminals often struggle more. As an example,
Gnome Terminal version 3.38.1, shows “❤️” as a big red heart, but
shows "👨‍🦰" as “👨🦰”.

[combining characters]: https://en.wikipedia.org/wiki/Combining_character
[Unicode equivalence]: https://en.wikipedia.org/wiki/Unicode_equivalence
[CJK characters]: https://en.wikipedia.org/wiki/CJK_characters
[emoji modifier sequences]: https://unicode.org/emoji/charts/full-emoji-modifiers.html


### From `repos/clap/clap_builder/src/output/textwrap/mod.rs`


#### Module: `mod` (line 1)

<!-- Source: repos/clap/clap_builder/src/output/textwrap/mod.rs:1 -->

<!-- Type: module -->


Fork of `textwrap` crate

Benefits of forking:
- Pull in only what we need rather than relying on the compiler to remove what we don't need
- `LineWrapper` is able to incrementally wrap which will help with `StyledStr`


#### Fn: `wrap` (line 33)

<!-- Source: repos/clap/clap_builder/src/output/textwrap/mod.rs:33 -->

<!-- Type: fn -->


Compatibility shim to keep textwrap's tests


### From `repos/clap/clap_builder/src/util/flat_map.rs`


#### Struct: `FlatMap` (line 5)

<!-- Source: repos/clap/clap_builder/src/util/flat_map.rs:5 -->

<!-- Type: struct -->


Flat (Vec) backed map

This preserves insertion order


### From `repos/clap/clap_builder/src/util/flat_set.rs`


#### Struct: `FlatSet` (line 5)

<!-- Source: repos/clap/clap_builder/src/util/flat_set.rs:5 -->

<!-- Type: struct -->


Flat (Vec) backed set

This preserves insertion order


### From `repos/clap/clap_builder/src/util/id.rs`


#### Struct: `Id` (line 5)

<!-- Source: repos/clap/clap_builder/src/util/id.rs:5 -->

<!-- Type: struct -->


[`Arg`][crate::Arg] or [`ArgGroup`][crate::ArgGroup] identifier

This is used for accessing the value in [`ArgMatches`][crate::ArgMatches] or defining
relationships between `Arg`s and `ArgGroup`s with functions like
[`Arg::conflicts_with`][crate::Arg::conflicts_with].


#### Fn: `as_str` (line 22)

<!-- Source: repos/clap/clap_builder/src/util/id.rs:22 -->

<!-- Type: fn -->


Get the raw string of the `Id`


### From `repos/clap/clap_builder/src/util/str_to_bool.rs`


#### Const: `TRUE_LITERALS` (line 1)

<!-- Source: repos/clap/clap_builder/src/util/str_to_bool.rs:1 -->

<!-- Type: const -->


True values are `y`, `yes`, `t`, `true`, `on`, and `1`.


#### Const: `FALSE_LITERALS` (line 4)

<!-- Source: repos/clap/clap_builder/src/util/str_to_bool.rs:4 -->

<!-- Type: const -->


False values are `n`, `no`, `f`, `false`, `off`, and `0`.


#### Fn: `str_to_bool` (line 7)

<!-- Source: repos/clap/clap_builder/src/util/str_to_bool.rs:7 -->

<!-- Type: fn -->


Converts a string literal representation of truth to true or false.

`false` values are `n`, `no`, `f`, `false`, `off`, and `0` (case insensitive).

Any other value will be considered as `true`.


### From `repos/clap/src/_cookbook/escaped_positional.rs`


#### Module: `escaped_positional` (line 1)

<!-- Source: repos/clap/src/_cookbook/escaped_positional.rs:1 -->

<!-- Type: module -->


# Example (Builder API)

```rust


### From `repos/clap/src/_cookbook/escaped_positional_derive.rs`


#### Module: `escaped_positional_derive` (line 1)

<!-- Source: repos/clap/src/_cookbook/escaped_positional_derive.rs:1 -->

<!-- Type: module -->


# Example (Derive API)

```rust


### From `repos/clap/src/_cookbook/find.rs`


#### Module: `find` (line 1)

<!-- Source: repos/clap/src/_cookbook/find.rs:1 -->

<!-- Type: module -->


# Example: find-like CLI (Builder API)

```rust


### From `repos/clap/src/_cookbook/git.rs`


#### Module: `git` (line 1)

<!-- Source: repos/clap/src/_cookbook/git.rs:1 -->

<!-- Type: module -->


# Example: git-like CLI (Builder API)

```rust


### From `repos/clap/src/_cookbook/git_derive.rs`


#### Module: `git_derive` (line 1)

<!-- Source: repos/clap/src/_cookbook/git_derive.rs:1 -->

<!-- Type: module -->


# Example: git-like CLI (Derive API)

```rust


### From `repos/clap/src/_cookbook/mod.rs`


#### Module: `mod` (line 8)

<!-- Source: repos/clap/src/_cookbook/mod.rs:8 -->

<!-- Type: module -->


# Documentation: Cookbook

Typed arguments: [derive][typed_derive]
- Topics:
- Custom `parse()`

Custom cargo command: [builder][cargo_example], [derive][cargo_example_derive]
- Topics:
- Subcommands
- Cargo plugins
- custom terminal [styles][crate::Command::styles] (colors)

find-like interface: [builder][find]
- Topics:
- Position-sensitive flags

git-like interface: [builder][git], [derive][git_derive]
- Topics:
- Subcommands
- External subcommands
- Optional subcommands
- Default subcommands
- [`last`][crate::Arg::last]

pacman-like interface: [builder][pacman]
- Topics:
- Flag subcommands
- Conflicting arguments

Escaped positionals with `--`: [builder][escaped_positional], [derive][escaped_positional_derive]

Multi-call
- busybox: [builder][multicall_busybox]
- Topics:
- Subcommands
- hostname: [builder][multicall_hostname]
- Topics:
- Subcommands

repl: [builder][repl], [derive][repl_derive]
- Topics:
- Read-Eval-Print Loops / Custom command lines


### From `repos/clap/src/_cookbook/multicall_busybox.rs`


#### Module: `multicall_busybox` (line 1)

<!-- Source: repos/clap/src/_cookbook/multicall_busybox.rs:1 -->

<!-- Type: module -->


# Example: busybox-like CLI (Builder API)

```rust


### From `repos/clap/src/_cookbook/multicall_hostname.rs`


#### Module: `multicall_hostname` (line 1)

<!-- Source: repos/clap/src/_cookbook/multicall_hostname.rs:1 -->

<!-- Type: module -->


# Example: hostname-like CLI (Builder API)

```rust


### From `repos/clap/src/_cookbook/pacman.rs`


#### Module: `pacman` (line 1)

<!-- Source: repos/clap/src/_cookbook/pacman.rs:1 -->

<!-- Type: module -->


# Example: pacman-like CLI (Builder API)

```rust


### From `repos/clap/src/_cookbook/repl.rs`


#### Module: `repl` (line 1)

<!-- Source: repos/clap/src/_cookbook/repl.rs:1 -->

<!-- Type: module -->


# Example: Command REPL (Builder API)

```rust


### From `repos/clap/src/_cookbook/repl_derive.rs`


#### Module: `repl_derive` (line 1)

<!-- Source: repos/clap/src/_cookbook/repl_derive.rs:1 -->

<!-- Type: module -->


# Example: REPL (Derive API)

```rust


### From `repos/clap/src/_cookbook/typed_derive.rs`


#### Module: `typed_derive` (line 1)

<!-- Source: repos/clap/src/_cookbook/typed_derive.rs:1 -->

<!-- Type: module -->


# Example: Custom Types (Derive API)

**This requires enabling the [`derive` feature flag][crate::_features].**

## Implicit [`Arg::value_parser`][crate::Arg::value_parser]

```rust


### From `repos/clap/src/_derive/_tutorial.rs`


#### Module: `_tutorial` (line 10)

<!-- Source: repos/clap/src/_derive/_tutorial.rs:10 -->

<!-- Type: module -->


## Tutorial for the Derive API

*See the side bar for the Table of Contents*

## Quick Start

You can create an application declaratively with a `struct` and some
attributes.

First, ensure `clap` is available with the [`derive` feature flag][crate::_features]:
```console
$ cargo add clap --features derive
```

Here is a preview of the type of application you can make:
```rust


**Code Examples:**


```rust
Here is a preview of the type of application you can make:
```


### From `repos/clap/src/_derive/mod.rs`


#### Module: `mod` (line 1)

<!-- Source: repos/clap/src/_derive/mod.rs:1 -->

<!-- Type: module -->


# Documentation: Derive Reference

1. [Overview](#overview)
2. [Attributes](#attributes)
1. [Terminology](#terminology)
2. [Command Attributes](#command-attributes)
2. [ArgGroup Attributes](#arggroup-attributes)
3. [Arg Attributes](#arg-attributes)
4. [ValueEnum Attributes](#valueenum-attributes)
5. [Possible Value Attributes](#possible-value-attributes)
3. [Field Types](#field-types)
4. [Doc Comments](#doc-comments)
5. [Mixing Builder and Derive APIs](#mixing-builder-and-derive-apis)
6. [Tips](#tips)

## Overview

To derive `clap` types, you need to enable the [`derive` feature flag][crate::_features].

Example:
```rust


### From `repos/clap/src/_features.rs`


#### Module: `_features` (line 1)

<!-- Source: repos/clap/src/_features.rs:1 -->

<!-- Type: module -->


## Documentation: Feature Flags

Available [compile-time feature flags](https://doc.rust-lang.org/cargo/reference/features.html#dependency-features)

#### Default Features

* `std`: _Not Currently Used._ Placeholder for supporting `no_std` environments in a backwards compatible manner.
* `color`: Turns on terminal styling of help and error messages.  See
[`Command::styles`][crate::Command::styles] to customize this.
* `help`: Auto-generate help output
* `usage`: Auto-generate usage
* `error-context`: Include contextual information for errors (which arg failed, etc)
* `suggestions`: Turns on the `Did you mean '--myoption'?` feature for when users make typos.

#### Optional features

* `deprecated`: Guided experience to prepare for next breaking release (at different stages of development, this may become default)
* `derive`: Enables the custom derive (i.e. `#[derive(Parser)]`). Without this you must use one of the other methods of creating a `clap` CLI listed above.
* `cargo`: Turns on macros that read values from [`CARGO_*` environment variables](https://doc.rust-lang.org/cargo/reference/environment-variables.html#environment-variables-cargo-sets-for-crates).
* `env`: Turns on the usage of environment variables during parsing.
* `unicode`: Turns on support for unicode characters (including emoji) in arguments and help messages.
* ``wrap_help``: Turns on the help text wrapping feature, based on the terminal size.
* `string`: Allow runtime generated strings (e.g. with [`Str`][crate::builder::Str]).

#### Experimental features

**Warning:** These may contain breaking changes between minor releases.

* `unstable-v5`: Preview features which will be stable on the v5.0 release


### From `repos/clap/src/_tutorial.rs`


#### Module: `_tutorial` (line 10)

<!-- Source: repos/clap/src/_tutorial.rs:10 -->

<!-- Type: module -->


## Tutorial for the Builder API

*See the side bar for the Table of Contents*

## Quick Start

You can create an application with several arguments using usage strings.

First, ensure `clap` is available:
```console
$ cargo add clap
```

Here is a preview of the type of application you can make:
```rust


**Code Examples:**


```rust
Here is a preview of the type of application you can make:
```


### From `repos/clap/src/lib.rs`


#### Module: `lib` (line 6)

<!-- Source: repos/clap/src/lib.rs:6 -->

<!-- Type: module -->


> **Command Line Argument Parser for Rust**

Quick Links:
- Derive [tutorial][_derive::_tutorial] and [reference][_derive]
- Builder [tutorial][_tutorial] and [reference][Command]
- [Cookbook][_cookbook]
- [CLI Concepts][_concepts]
- [FAQ][_faq]
- [Discussions](https://github.com/clap-rs/clap/discussions)
- [CHANGELOG](https://github.com/clap-rs/clap/blob/v4.5.54/CHANGELOG.md) (includes major version migration
guides)

## Aspirations

- Out of the box, users get a polished CLI experience
- Including common argument behavior, help generation, suggested fixes for users, colored output, [shell completions](https://github.com/clap-rs/clap/tree/master/clap_complete), etc
- Flexible enough to port your existing CLI interface
- However, we won't necessarily streamline support for each use case
- Reasonable parse performance
- Resilient maintainership, including
- Willing to break compatibility rather than batching up breaking changes in large releases
- Leverage feature flags to keep to one active branch
- Being under [WG-CLI](https://github.com/rust-cli/team/) to increase the bus factor
- We follow semver and will wait about 6-9 months between major breaking changes
- We will support the last two minor Rust releases (MSRV, currently 1.74)

While these aspirations can be at odds with fast build times and low binary
size, we will still strive to keep these reasonable for the flexibility you
get.  Check out the
[argparse-benchmarks](https://github.com/rust-cli/argparse-benchmarks-rs) for
CLI parsers optimized for other use cases.

## Example

Run
```console
$ cargo add clap --features derive
```
*(See also [feature flag reference][_features])*

Then define your CLI in `main.rs`:
```rust
# #[cfg(feature = "derive")] {


**Code Examples:**


```rust
*(See also [feature flag reference][_features])*

Then define your CLI in `main.rs`:
```


---


## Best Practices from Source Comments


Key recommendations and patterns found in the documentation:


### From `_faq`

[When should I use the builder vs derive APIs?](#when-should-i-use-the-builder-vs-derive-apis)
4

*Source: `repos/clap/src/_faq.rs:1`*


### From `_faq`

The following APIs are supported:
- [Derive][crate::_derive::_tutorial]
- [Builder][crate::_tutorial]

Previously, we supported:
- [YAML](https://github.com/clap-rs/clap/issues/3087)
- [docopt](http://docopt.org/)-inspired [usage parser](https://github.com/clap-rs/clap/issues/3086)
- [`clap_app!`](https://github.com/clap-rs/clap/issues/2835)

There are also experiments with other APIs:
- [fncmd](https://github.com/yuhr/fncmd): function attribute
- [clap-serde](https://github.com/aobatact/clap-serde): create a `Command` from a deserializer

### When should I use the builder vs derive APIs

*Source: `repos/clap/src/_faq.rs:1`*


### From `_faq`

#### Reasons to use `clap`

* You want all the nice CLI features your users may expect, yet you don't want to implement them all yourself

*Source: `repos/clap/src/_faq.rs:1`*


### From `_faq`

* In addition to the point above, you don't want to sacrifice performance to get all those nice features

*Source: `repos/clap/src/_faq.rs:1`*


### From `_faq`

* You want some sort of custom validation built into the argument parsing process, instead of as part of your application (which allows for earlier failures, better error messages, more cohesive experience, etc.)

*Source: `repos/clap/src/_faq.rs:1`*


### From `_faq`

There's plenty of room in the Rust
community for multiple implementations

*Source: `repos/clap/src/_faq.rs:1`*


### From `_concepts`

## CLI Concepts

Note: this will be speaking towards the general case

*Source: `repos/clap/src/_concepts.rs:1`*


### From `mod`

[Tips](#tips)

## Overview

To derive `clap` types, you need to enable the [`derive` feature flag][crate::_features]

*Source: `repos/clap/src/_derive/mod.rs:1`*


### From `Parser`

<div class="warning">

**NOTE:** Deriving requires the `derive` feature flag

</div>

*Source: `repos/clap/clap_builder/src/derive.rs:10`*


### From `ColorChoice`

Represents the color preferences for program output

*Source: `repos/clap/clap_builder/src/util/color.rs:4`*


### From `display_width`

A more complex example would be “👨‍🦰” which should depict a man
with red hair

*Source: `repos/clap/clap_builder/src/output/textwrap/core.rs:1`*


### From `display_width`

Compute the display width of `text`

# Examples

**Note:** When the `unicode` Cargo feature is disabled, all characters are presumed to take up
1 width

*Source: `repos/clap/clap_builder/src/output/textwrap/core.rs:1`*


### From `mod`

Fork of `textwrap` crate

Benefits of forking:
- Pull in only what we need rather than relying on the compiler to remove what we don't need
- `LineWrapper` is able to incrementally wrap which will help with `StyledStr`

*Source: `repos/clap/clap_builder/src/output/textwrap/mod.rs:1`*


### From `get_one`

<div class="warning">

*NOTE:* This will always return `Some(value)` if [`default_value`] has been set

*Source: `repos/clap/clap_builder/src/parser/matches/arg_matches.rs:78`*


### From `get_many`

an argument that takes multiple values at runtime

*Source: `repos/clap/clap_builder/src/parser/matches/arg_matches.rs:191`*


### From `get_occurrences`

If the option doesn't support multiple occurrences, or there was only a single occurrence,
the iterator will only contain a single item

*Source: `repos/clap/clap_builder/src/parser/matches/arg_matches.rs:232`*


### From `contains_id`

Check if values are present for the argument or group id

<div class="warning">

*NOTE:* This will always return `true` if [`default_value`] has been set

*Source: `repos/clap/clap_builder/src/parser/matches/arg_matches.rs:492`*


### From `index_of`

The examples should clear this up

*Source: `repos/clap/clap_builder/src/parser/matches/arg_matches.rs:615`*


### From `index_of`

those arguments which don't have an associated value), indices refer
to occurrence of the switch, such as `-f`, or `--flag`

*Source: `repos/clap/clap_builder/src/parser/matches/arg_matches.rs:615`*


### From `index_of`

<div class="warning">

*NOTE:* If an argument is allowed multiple times, this method will only give the *first*
index

*Source: `repos/clap/clap_builder/src/parser/matches/arg_matches.rs:615`*


### From `index_of`

Note that if it's not listed in a clap index, this is because it's not saved in
in an `ArgMatches` struct for querying

*Source: `repos/clap/clap_builder/src/parser/matches/arg_matches.rs:615`*


### From `index_of`

```rust
# use clap_builder as clap;
# use clap::{Command, Arg, ArgAction};
let m = Command::new("myapp")
.arg(Arg::new("flag")
.short('f')
.action(ArgAction::SetTrue))
.arg(Arg::new("flag2")
.short('F')
.action(ArgAction::SetTrue))
.arg(Arg::new("flag3")
.short('z')
.action(ArgAction::SetTrue))
.arg(Arg::new("option")
.short('o')
.action(ArgAction::Set))
.get_matches_from(vec!["myapp", "-fzF", "-oval"]);
// ARGV indices: ^0      ^1       ^2
// clap indices:         ^1,2,3    ^5
//
// clap sees the above as 'myapp -f -z -F -o val'
//                         ^0    ^1 ^2 ^3 ^4 ^5
assert_eq!(m.index_of("flag"), Some(1));
assert_eq!(m.index_of("flag2"), Some(3));
assert_eq!(m.index_of("flag3"), Some(2));
assert_eq!(m.index_of("option"), Some(5));
```

One final combination of flags/options to see how they combine:

```rust
# use clap_builder as clap;
# use clap::{Command, Arg, ArgAction};
let m = Command::new("myapp")
.arg(Arg::new("flag")
.short('f')
.action(ArgAction::SetTrue))
.arg(Arg::new("flag2")
.short('F')
.action(ArgAction::SetTrue))
.arg(Arg::new("flag3")
.short('z')
.action(ArgAction::SetTrue))
.arg(Arg::new("option")
.short('o')
.action(ArgAction::Set))
.get_matches_from(vec!["myapp", "-fzFoval"]);
// ARGV indices: ^0       ^1
// clap indices:          ^1,2,3^5
//
// clap sees the above as 'myapp -f -z -F -o val'
//                         ^0    ^1 ^2 ^3 ^4 ^5
assert_eq!(m.index_of("flag"), Some(1));
assert_eq!(m.index_of("flag2"), Some(3));
assert_eq!(m.index_of("flag3"), Some(2));
assert_eq!(m.index_of("option"), Some(5));
```

The last part to mention is when values are sent in multiple groups with a [delimiter]

*Source: `repos/clap/clap_builder/src/parser/matches/arg_matches.rs:615`*


### From `indices_of`

# Examples

```rust
# use clap_builder as clap;
# use clap::{Command, Arg};
let m = Command::new("myapp")
.arg(Arg::new("option")
.short('o')
.value_delimiter(','))
.get_matches_from(vec!["myapp", "-o=val1,val2,val3"]);
// ARGV indices: ^0       ^1
// clap indices:             ^2   ^3   ^4
//
// clap sees the above as 'myapp -o val1 val2 val3'
//                         ^0    ^1 ^2   ^3   ^4
assert_eq!(m.indices_of("option").unwrap().collect::<Vec<_>>(), &[2, 3, 4]);
```

Another quick example is when flags and options are used together

```rust
# use clap_builder as clap;
# use clap::{Command, Arg, ArgAction};
let m = Command::new("myapp")
.arg(Arg::new("option")
.short('o')
.action(ArgAction::Set)
.action(ArgAction::Append))
.arg(Arg::new("flag")
.short('f')
.action(ArgAction::Count))
.get_matches_from(vec!["myapp", "-o", "val1", "-f", "-o", "val2", "-f"]);
// ARGV indices: ^0       ^1    ^2      ^3    ^4    ^5      ^6
// clap indices:                ^2      ^3          ^5      ^6

assert_eq!(m.indices_of("option").unwrap().collect::<Vec<_>>(), &[2, 5]);
assert_eq!(m.indices_of("flag").unwrap().collect::<Vec<_>>(), &[6]);
```

One final example, which is an odd case; if we *don't* use  value delimiter as we did with
the first example above instead of `val1`, `val2` and `val3` all being distinc values, they
would all be a single value of `val1,val2,val3`, in which case they'd only receive a single
index

*Source: `repos/clap/clap_builder/src/parser/matches/arg_matches.rs:773`*


### From `indices_of`

<div class="warning">

*NOTE:* For more information about how clap indices compared to argv indices, see
[`ArgMatches::index_of`]

</div>

# Panics

If `id` is not a valid argument or group id (debug builds)

*Source: `repos/clap/clap_builder/src/parser/matches/arg_matches.rs:773`*


### From `subcommand`

In these cases you can't know the subcommand name ahead of time, so use a variable instead
with pattern matching

*Source: `repos/clap/clap_builder/src/parser/matches/arg_matches.rs:867`*


### From `Values`

Iterate over multiple values for an argument via [`ArgMatches::remove_many`]

*Source: `repos/clap/clap_builder/src/parser/matches/arg_matches.rs:1407`*


### From `ValuesRef`

Iterate over multiple values for an argument via [`ArgMatches::get_many`]

*Source: `repos/clap/clap_builder/src/parser/matches/arg_matches.rs:1474`*


### From `PossibleValue`

See also [`PossibleValuesParser`][crate::builder::PossibleValuesParser]

<div class="warning">

**NOTE:** Most likely you can use strings, rather than `PossibleValue` as it is only required
to [hide] single values from help messages and shell completions or to attach [help] to
possible values

*Source: `repos/clap/clap_builder/src/builder/possible_value.rs:6`*


### From `new`

<div class="warning">

**NOTE:** In case it is not [hidden] it will also be shown in help messages for arguments
that use it as a [possible value] and have not hidden them through [`Arg::hide_possible_values(true)`]

*Source: `repos/clap/clap_builder/src/builder/possible_value.rs:48`*


### From `help`

This is typically displayed in completions (where supported) and should be a short, one-line
description

*Source: `repos/clap/clap_builder/src/builder/possible_value.rs:77`*


### From `aliases`

Sets multiple *hidden* aliases for this argument value

*Source: `repos/clap/clap_builder/src/builder/possible_value.rs:141`*


### From `new`

Create a range

# Panics

If the end is less than the start (debug builds)

# Examples

```rust
# use clap_builder as clap;
# use clap::builder::ValueRange;
let range = ValueRange::new(5);
let range = ValueRange::new(5..10);
let range = ValueRange::new(5..=10);
let range = ValueRange::new(5..);
let range = ValueRange::new(..10);
let range = ValueRange::new(..=10);
```

While this will panic:
```should_panic
# use clap_builder as clap;
# use clap::builder::ValueRange;
let range = ValueRange::new(10..5);  // Panics

*Source: `repos/clap/clap_builder/src/builder/range.rs:32`*


### From `new_inner`

If we don't do this rustc will unnecessarily generate multiple versions
of this code.

*Source: `repos/clap/clap_builder/src/builder/command.rs:134`*


### From `args`

Adds multiple [arguments] to the list of valid possibilities

*Source: `repos/clap/clap_builder/src/builder/command.rs:191`*


### From `mut_arg`

# Panics

If the argument is undefined

# Examples

```rust
# use clap_builder as clap;
# use clap::{Command, Arg, ArgAction};

let mut cmd = Command::new("foo")
.arg(Arg::new("bar")
.short('b')
.action(ArgAction::SetTrue))
.mut_arg("bar", |a| a.short('B'));

let res = cmd.try_get_matches_from_mut(vec!["foo", "-b"]);

// Since we changed `bar`'s short to "B" this should err as there
// is no `-b` anymore, only `-B`

assert!(res.is_err());

let res = cmd.try_get_matches_from_mut(vec!["foo", "-B"]);
assert!(res.is_ok());
```

*Source: `repos/clap/clap_builder/src/builder/command.rs:214`*


### From `mut_args`

# use clap::{Command, Arg, ArgAction};

let mut cmd = Command::new("foo")
.arg(Arg::new("bar")
.long("bar")
.action(ArgAction::SetTrue))
.arg(Arg::new("baz")
.long("baz")
.action(ArgAction::SetTrue))
.mut_args(|a| {
if let Some(l) = a.get_long().map(|l| format!("prefix-{l}")) {
a.long(l)
} else {
a
}
});

let res = cmd.try_get_matches_from_mut(vec!["foo", "--bar"]);

// Since we changed `bar`'s long to "prefix-bar" this should err as there
// is no `--bar` anymore, only `--prefix-bar`

*Source: `repos/clap/clap_builder/src/builder/command.rs:267`*


### From `mut_subcommand`

# Panics

If the subcommand is undefined

# Examples

```rust
# use clap_builder as clap;
# use clap::Command;

let mut cmd = Command::new("foo")
.subcommand(Command::new("bar"))
.mut_subcommand("bar", |subcmd| subcmd.disable_help_flag(true));

let res = cmd.try_get_matches_from_mut(vec!["foo", "bar", "--help"]);

// Since we disabled the help flag on the "bar" subcommand, this should err

*Source: `repos/clap/clap_builder/src/builder/command.rs:343`*


### From `group`

- Extract a value from a group instead of determining exactly which argument was used

*Source: `repos/clap/clap_builder/src/builder/command.rs:434`*


### From `groups`

Adds multiple [`ArgGroup`]s to the [`Command`] at once

*Source: `repos/clap/clap_builder/src/builder/command.rs:473`*


### From `subcommands`

Adds multiple subcommands to the list of valid possibilities

*Source: `repos/clap/clap_builder/src/builder/command.rs:542`*


### From `debug_assert`

**Note:** This will not help with asserts in [`ArgMatches`], those will need exhaustive
testing of your CLI

*Source: `repos/clap/clap_builder/src/builder/command.rs:589`*


### From `error`

Custom error message for post-parsing validation

**Note:** this will ensure the `Command` has been sufficiently [built][Command::build] for any
relevant context, including usage

*Source: `repos/clap/clap_builder/src/builder/command.rs:625`*


### From `try_get_matches`

<div class="warning">

**NOTE:** This method WILL NOT exit when `--help` or `--version` (or short versions) are
used

*Source: `repos/clap/clap_builder/src/builder/command.rs:693`*


### From `get_matches_from`

<div class="warning">

**NOTE:** The first argument will be parsed as the binary name unless
[`Command::no_binary_name`] is used

*Source: `repos/clap/clap_builder/src/builder/command.rs:732`*


### From `try_get_matches_from`

</div>

<div class="warning">

**NOTE:** The first argument will be parsed as the binary name unless
[`Command::no_binary_name`] is used

*Source: `repos/clap/clap_builder/src/builder/command.rs:770`*


### From `print_help`

**Note:** this will ensure the `Command` has been sufficiently [built][Command::build]

*Source: `repos/clap/clap_builder/src/builder/command.rs:912`*


### From `render_usage`

Usage statement

**Note:** this will ensure the `Command` has been sufficiently [built][Command::build]

*Source: `repos/clap/clap_builder/src/builder/command.rs:1123`*


### From `no_binary_name`

Specifies that the parser should not assume the first argument passed is the binary name

*Source: `repos/clap/clap_builder/src/builder/command.rs:1166`*


### From `ignore_errors`

<div class="warning">

**NOTE:** This choice is propagated to all child subcommands

*Source: `repos/clap/clap_builder/src/builder/command.rs:1194`*


### From `dont_delimit_trailing_values`

<div class="warning">

**NOTE:** The same thing can be done manually by setting the final positional argument to
[`Arg::value_delimiter(None)`]

*Source: `repos/clap/clap_builder/src/builder/command.rs:1254`*


---


## Appendix: All Documented Items {#appendix}


Alphabetical listing of all documented items:

- **`_AnonymousValueParser`** (struct) - `repos/clap/clap_builder/src/builder/value_parser.rs:2449` - Unstable [`ValueParser`]
- **`_build`** (fn) - `repos/clap/clap_builder/src/mkeymap.rs:135` - We need a lazy build here since some we may change args after creating
- **`_concepts`** (module) - `repos/clap/src/_concepts.rs:1` - ## CLI Concepts
- **`_faq`** (module) - `repos/clap/src/_faq.rs:1` - # Documentation: FAQ
- **`_features`** (module) - `repos/clap/src/_features.rs:1` - ## Documentation: Feature Flags
- **`_propagate`** (fn) - `repos/clap/clap_builder/src/builder/command.rs:4767` - Propagate settings
- **`_propagate_global_args`** (fn) - `repos/clap/clap_builder/src/builder/command.rs:4732` - Propagate global args
- **`_tutorial`** (module) - `repos/clap/src/_derive/_tutorial.rs:10` - ## Tutorial for the Derive API
- **`_tutorial`** (module) - `repos/clap/src/_tutorial.rs:10` - ## Tutorial for the Builder API
- **`about`** (fn) - `repos/clap/clap_builder/src/builder/command.rs:1952` - Sets the program's description for the short help (`-h`).
- **`action`** (fn) - `repos/clap/clap_builder/src/builder/arg.rs:955` - Specify how to react to an argument when parsing it.
- **`add`** (fn) - `repos/clap/clap_builder/src/builder/arg.rs:944` - Extend [`Arg`] with [`ArgExt`] data
- **`add`** (fn) - `repos/clap/clap_builder/src/builder/command.rs:1152` - Extend [`Command`] with [`CommandExt`] data
- **`add_prefix`** (fn) - `repos/clap/clap_complete/src/engine/candidate.rs:63` - Add a prefix to the value of completion candidate
- **`after_help`** (fn) - `repos/clap/clap_builder/src/builder/command.rs:2004` - Free-form help text for after auto-generated short help (`-h`).
- **`after_long_help`** (fn) - `repos/clap/clap_builder/src/builder/command.rs:2027` - Free-form help text for after auto-generated long help (`--help`).
- **`alias`** (fn) - `repos/clap/clap_builder/src/builder/arg.rs:233` - Add an alias, which functions as a hidden long flag.
- **`alias`** (fn) - `repos/clap/clap_builder/src/builder/command.rs:2653` - Sets a hidden alias to this subcommand.
- **`alias`** (fn) - `repos/clap/clap_builder/src/builder/possible_value.rs:120` - Sets a *hidden* alias for this argument value.
- **`aliases`** (fn) - `repos/clap/clap_builder/src/builder/arg.rs:294` - Add aliases, which function as hidden long flags.
- **`aliases`** (fn) - `repos/clap/clap_builder/src/builder/command.rs:2752` - Sets multiple hidden aliases to this subcommand.
- **`aliases`** (fn) - `repos/clap/clap_builder/src/builder/possible_value.rs:141` - Sets multiple *hidden* aliases for this argument value.
- **`aliases_to`** (fn) - `repos/clap/clap_builder/src/builder/command.rs:4975` - Check if this subcommand can be referred to as `name`. In other words,
- **`align_to_about`** (fn) - `repos/clap/clap_builder/src/output/help_template.rs:563` - Write alignment padding between arg's switches/values and its about message.
- **`all_subcommand_names`** (fn) - `repos/clap/clap_builder/src/builder/command.rs:5023` - Iterate through all the names of all subcommands (not recursively), including aliases.
- **`all_subcommands`** (fn) - `repos/clap/clap_complete/src/aot/generator/utils.rs:5` - Gets all subcommands including child subcommands in the form of `("name", "bin_name")`.
- **`allow_external_subcommands`** (fn) - `repos/clap/clap_builder/src/builder/command.rs:3158` - Assume unexpected positional arguments are a [`subcommand`].
- **`allow_hyphen_values`** (fn) - `repos/clap/clap_builder/src/builder/arg.rs:1473` - Allows values which start with a leading hyphen (`-`)
- **`allow_missing_positional`** (fn) - `repos/clap/clap_builder/src/builder/command.rs:2455` - Allows one to implement two styles of CLIs where positionals can be used out of order.
- **`allow_negative_numbers`** (fn) - `repos/clap/clap_builder/src/builder/arg.rs:1549` - Allows negative numbers to pass as values.
- **`and_suggest`** (fn) - `repos/clap/clap_builder/src/builder/value_parser.rs:2181` - Extend the suggestions
- **`ansi`** (fn) - `repos/clap/clap_builder/src/builder/styled_str.rs:33` - Display using [ANSI Escape Code](https://en.wikipedia.org/wiki/ANSI_escape_code) styling
- **`any`** (fn) - `repos/clap/clap_complete/src/engine/custom.rs:222` - Any path is allowed
- **`AnyValueParser`** (trait) - `repos/clap/clap_builder/src/builder/value_parser.rs:590` - A type-erased wrapper for [`TypedValueParser`].
- **`append_keys`** (fn) - `repos/clap/clap_builder/src/mkeymap.rs:164` - Generate key types for an specific Arg.
- **`apply`** (fn) - `repos/clap/clap_builder/src/error/mod.rs:156` - Apply an alternative formatter to the error
- **`AppSettings`** (enum) - `repos/clap/clap_builder/src/builder/app_settings.rs:36` - Application level settings, which affect how [`Command`] operates
- **`Arg`** (struct) - `repos/clap/clap_builder/src/builder/arg.rs:31` - The abstract representation of a command line argument. Used to set all the options and
- **`Arg`** (impl) - `repos/clap/clap_builder/src/builder/arg.rs:94` - # Basic API
- **`Arg`** (impl) - `repos/clap/clap_builder/src/builder/arg.rs:953` - # Value Handling
- **`Arg`** (impl) - `repos/clap/clap_builder/src/builder/arg.rs:2217` - # Help
- **`Arg`** (impl) - `repos/clap/clap_builder/src/builder/arg.rs:2844` - # Advanced Argument Relations
- **`Arg`** (impl) - `repos/clap/clap_builder/src/builder/arg.rs:4166` - # Reflection
- **`Arg`** (impl) - `repos/clap/clap_builder/src/builder/arg.rs:4573` - # Internally used only
- **`arg`** (fn) - `repos/clap/clap_builder/src/builder/arg_group.rs:112` - Adds an [argument] to this group by name
- **`arg`** (fn) - `repos/clap/clap_builder/src/builder/command.rs:148` - Adds an [argument] to the list of valid possibilities.
- **`arg_required_else_help`** (fn) - `repos/clap/clap_builder/src/builder/command.rs:2388` - Exit gracefully if no arguments are present (e.g. `$ myprog`).
- **`ArgAction`** (enum) - `repos/clap/clap_builder/src/builder/action.rs:6` - Behavior of arguments when they are encountered while parsing
- **`ArgExt`** (trait) - `repos/clap/clap_builder/src/builder/arg.rs:4828` - User-provided data that can be attached to an [`Arg`]
- **`ArgGroup`** (struct) - `repos/clap/clap_builder/src/builder/arg_group.rs:5` - Specifies a logical group of [arguments]
- **`ArgGroup`** (impl) - `repos/clap/clap_builder/src/builder/arg_group.rs:77` - # Builder
- **`ArgGroup`** (impl) - `repos/clap/clap_builder/src/builder/arg_group.rs:516` - # Reflection
- **`ArgMatches`** (struct) - `repos/clap/clap_builder/src/parser/matches/arg_matches.rs:20` - Container for parse results.
- **`ArgMatches`** (impl) - `repos/clap/clap_builder/src/parser/matches/arg_matches.rs:76` - # Arguments
- **`ArgMatches`** (impl) - `repos/clap/clap_builder/src/parser/matches/arg_matches.rs:865` - # Subcommands
- **`ArgMatches`** (impl) - `repos/clap/clap_builder/src/parser/matches/arg_matches.rs:1078` - # Advanced
- **`ArgPredicate`** (enum) - `repos/clap/clap_builder/src/builder/arg_predicate.rs:3` - Operations to perform on argument values
- **`args`** (fn) - `repos/clap/clap_builder/src/builder/arg_group.rs:146` - Adds multiple [arguments] to this group by name
- **`args`** (fn) - `repos/clap/clap_builder/src/builder/command.rs:191` - Adds multiple [arguments] to the list of valid possibilities.
- **`Args`** (trait) - `repos/clap/clap_builder/src/derive.rs:214` - Parse a set of arguments into a user-defined container.
- **`args`** (fn) - `repos/clap/clap_builder/src/mkeymap.rs:116` - Return iterators of all args.
- **`args`** (fn) - `repos/clap/clap_derive/src/lib.rs:97` - Generates the `Args` impl.
- **`args_conflicts_with_subcommands`** (fn) - `repos/clap/clap_builder/src/builder/command.rs:3285` - Specifies that use of an argument prevents the use of [`subcommands`].
- **`args_mut`** (fn) - `repos/clap/clap_builder/src/mkeymap.rs:121` - Return mutable iterators of all args.
- **`args_override_self`** (fn) - `repos/clap/clap_builder/src/builder/command.rs:1230` - Replace prior occurrences of arguments rather than error
- **`args_present`** (fn) - `repos/clap/clap_builder/src/parser/matches/arg_matches.rs:555` - Check if any [`Arg`][crate::Arg]s were present on the command line
- **`ArgSettings`** (enum) - `repos/clap/clap_builder/src/builder/arg_settings.rs:34` - Various settings that apply to arguments and may be set, unset, and checked via getter/setter
- **`ArgValueCandidates`** (struct) - `repos/clap/clap_complete/src/engine/custom.rs:90` - Extend [`Arg`][clap::Arg] with a [`ValueCandidates`]
- **`ArgValueCompleter`** (struct) - `repos/clap/clap_complete/src/engine/custom.rs:11` - Extend [`Arg`][clap::Arg] with a completer
- **`as_os_str`** (fn) - `repos/clap/clap_builder/src/builder/os_str.rs:39` - Get the raw string as an `std::ffi::OsStr`
- **`as_str`** (fn) - `repos/clap/clap_builder/src/builder/str.rs:42` - Get the raw string of the `Str`
- **`as_str`** (fn) - `repos/clap/clap_builder/src/error/context.rs:43` - End-user description of the error case, where relevant
- **`as_str`** (fn) - `repos/clap/clap_builder/src/error/kind.rs:333` - End-user description of the error case, where relevant
- **`as_str`** (fn) - `repos/clap/clap_builder/src/util/id.rs:22` - Get the raw string of the `Id`
- **`augment_args`** (fn) - `repos/clap/clap_builder/src/derive.rs:232` - Append to [`Command`] so it can instantiate `Self` via
- **`augment_args_for_update`** (fn) - `repos/clap/clap_builder/src/derive.rs:239` - Append to [`Command`] so it can instantiate `self` via
- **`augment_subcommands`** (fn) - `repos/clap/clap_builder/src/derive.rs:263` - Append to [`Command`] so it can instantiate `Self` via
- **`augment_subcommands_for_update`** (fn) - `repos/clap/clap_builder/src/derive.rs:270` - Append to [`Command`] so it can instantiate `self` via
- **`author`** (fn) - `repos/clap/clap_builder/src/builder/command.rs:1920` - Sets the author(s) for the help message.
- **`AutoHelp`** (struct) - `repos/clap/clap_builder/src/output/help_template.rs:24` - `clap` auto-generated help writer
- **`Bash`** (struct) - `repos/clap/clap_complete/src/aot/shells/bash.rs:10` - Generate bash completion file
- **`Bash`** (struct) - `repos/clap/clap_complete/src/env/shells.rs:6` - Bash completion adapter
- **`before_help`** (fn) - `repos/clap/clap_builder/src/builder/command.rs:2051` - Free-form help text for before auto-generated short help (`-h`).
- **`before_long_help`** (fn) - `repos/clap/clap_builder/src/builder/command.rs:2072` - Free-form help text for before auto-generated long help (`--help`).
- **`bin`** (fn) - `repos/clap/clap_complete/src/env/mod.rs:165` - Override the name of the binary to complete
- **`bin_name`** (fn) - `repos/clap/clap_builder/src/builder/command.rs:1868` - Overrides the runtime-determined name of the binary for help and error messages.
- **`bool`** (fn) - `repos/clap/clap_builder/src/builder/value_parser.rs:119` - [`bool`] parser for argument values
- **`BoolishValueParser`** (struct) - `repos/clap/clap_builder/src/builder/value_parser.rs:1831` - Parse bool-like string values
- **`BoolValueParser`** (struct) - `repos/clap/clap_builder/src/builder/value_parser.rs:1672` - Implementation for [`ValueParser::bool`]
- **`build`** (fn) - `repos/clap/clap_builder/src/builder/command.rs:4375` - Prepare for introspecting on all included [`Command`]s
- **`builtins`** (fn) - `repos/clap/clap_complete/src/env/mod.rs:321` - Select all of the built-in shells
- **`C`** (const) - `repos/clap/clap_builder/src/builder/value_parser.rs:495` - Create a [`ValueParser`] with [`PossibleValuesParser`]
- **`candidates`** (fn) - `repos/clap/clap_complete/src/engine/custom.rs:119` - All potential candidates for an argument.
- **`candidates`** (fn) - `repos/clap/clap_complete/src/engine/custom.rs:163` - All potential candidates for an external subcommand.
- **`candidates`** (fn) - `repos/clap/clap_complete/src/engine/custom.rs:185` - All potential candidates for an argument.
- **`Captures`** (trait) - `repos/clap/clap_builder/src/builder/command.rs:4931` - A workaround:
- **`cargo_example`** (module) - `repos/clap/src/_cookbook/cargo_example.rs:1` - # Example: cargo subcommand (Builder API)
- **`cargo_example_derive`** (module) - `repos/clap/src/_cookbook/cargo_example_derive.rs:1` - # Example: cargo subcommand (Derive API)
- **`CasingStyle`** (enum) - `repos/clap/clap_derive/src/item.rs:1376` - Defines the casing for the attributes long representation.
- **`CLAP_STYLING`** (const) - `repos/clap-cargo/src/style.rs:40` - For use with
- **`color`** (fn) - `repos/clap/clap_builder/src/builder/command.rs:1291` - Sets when to color output.
- **`ColorChoice`** (enum) - `repos/clap/clap_builder/src/util/color.rs:4` - Represents the color preferences for program output
- **`Colorizer`** (impl) - `repos/clap/clap_builder/src/output/fmt.rs:33` - Printing methods.
- **`Command`** (struct) - `repos/clap/clap_builder/src/builder/command.rs:36` - Build a command-line interface.
- **`Command`** (impl) - `repos/clap/clap_builder/src/builder/command.rs:115` - # Basic API
- **`Command`** (impl) - `repos/clap/clap_builder/src/builder/command.rs:1161` - # Application-wide Settings
- **`Command`** (impl) - `repos/clap/clap_builder/src/builder/command.rs:1846` - # Command-specific Settings
- **`Command`** (impl) - `repos/clap/clap_builder/src/builder/command.rs:2576` - # Subcommand-specific Settings
- **`Command`** (impl) - `repos/clap/clap_builder/src/builder/command.rs:3706` - # Reflection
- **`command`** (fn) - `repos/clap/clap_builder/src/derive.rs:117` - Build a [`Command`] that can instantiate `Self`.
- **`command_for_update`** (fn) - `repos/clap/clap_builder/src/derive.rs:121` - Build a [`Command`] that can update `self`.
- **`CommandExt`** (trait) - `repos/clap/clap_builder/src/builder/command.rs:5251` - User-provided data that can be attached to an [`Arg`]
- **`CommandFactory`** (trait) - `repos/clap/clap_builder/src/derive.rs:113` - Create a [`Command`] relevant for a user-defined container.
- **`complete`** (fn) - `repos/clap/clap_complete/src/engine/complete.rs:12` - Complete the given command, shell-agnostic
- **`complete`** (fn) - `repos/clap/clap_complete/src/engine/custom.rs:55` - Candidates that match `current`
- **`complete`** (fn) - `repos/clap/clap_complete/src/engine/custom.rs:75` - All potential candidates for an argument.
- **`complete`** (fn) - `repos/clap/clap_complete/src/env/mod.rs:189` - Process the completion request and exit
- **`CompleteEnv`** (struct) - `repos/clap/clap_complete/src/env/mod.rs:77` - Environment-activated completions for your CLI
- **`completer`** (fn) - `repos/clap/clap_complete/src/env/mod.rs:173` - Override the binary to call to get completions
- **`completer`** (fn) - `repos/clap/clap_complete/src/env/mod.rs:326` - Find the specified [`EnvCompleter`]
- **`CompletionCandidate`** (struct) - `repos/clap/clap_complete/src/engine/candidate.rs:6` - A shell-agnostic completion candidate
- **`CompletionCandidate`** (impl) - `repos/clap/clap_complete/src/engine/candidate.rs:76` - Reflection API
- **`CompType`** (enum) - `repos/clap/clap_complete/src/env/shells.rs:103` - Type of completion attempted that caused a completion function to be called
- **`conflicts_with`** (fn) - `repos/clap/clap_builder/src/builder/arg.rs:3929` - This argument is mutually exclusive with the specified argument.
- **`conflicts_with`** (fn) - `repos/clap/clap_builder/src/builder/arg_group.rs:419` - Specify an argument or group that must **not** be present when this group is.
- **`conflicts_with_all`** (fn) - `repos/clap/clap_builder/src/builder/arg.rs:4007` - This argument is mutually exclusive with the specified arguments.
- **`conflicts_with_all`** (fn) - `repos/clap/clap_builder/src/builder/arg_group.rs:466` - Specify arguments or groups that must **not** be present when this group is.
- **`contains`** (fn) - `repos/clap/clap_builder/src/mkeymap.rs:83` - If any arg has corresponding key in this map, we can search the key with
- **`contains_id`** (fn) - `repos/clap/clap_builder/src/parser/matches/arg_matches.rs:492` - Check if values are present for the argument or group id
- **`context`** (fn) - `repos/clap/clap_builder/src/builder/styling.rs:124` - Highlight all specified contexts, e.g. `[default: false]`
- **`context`** (fn) - `repos/clap/clap_builder/src/error/mod.rs:184` - Additional information to further qualify the error
- **`context_value`** (fn) - `repos/clap/clap_builder/src/builder/styling.rs:133` - Highlight values within all of the context, e.g. the `false` in `[default: false]`
- **`ContextKind`** (enum) - `repos/clap/clap_builder/src/error/context.rs:1` - Semantics for a piece of error information
- **`ContextValue`** (enum) - `repos/clap/clap_builder/src/error/context.rs:73` - A piece of error information
- **`current_dir`** (fn) - `repos/clap/clap_complete/src/engine/custom.rs:256` - Override [`std::env::current_dir`]
- **`debug_assert`** (fn) - `repos/clap/clap_builder/src/builder/command.rs:589` - Catch problems earlier in the development cycle.
- **`Default`** (impl) - `repos/clap/clap_builder/src/parser/matches/arg_matches.rs:1463` - Creates an empty iterator.
- **`Default`** (impl) - `repos/clap/clap_builder/src/parser/matches/arg_matches.rs:1531` - Creates an empty iterator.
- **`Default`** (impl) - `repos/clap/clap_builder/src/parser/matches/arg_matches.rs:1604` - Creates an empty iterator.
- **`Default`** (impl) - `repos/clap/clap_builder/src/parser/matches/arg_matches.rs:1876` - Creates an empty iterator.
- **`DEFAULT_ADDITION_STYLE`** (const) - `repos/clap-cargo/src/style.rs:96` - [`Renderer::addition`] applied by [`Renderer::styled`]
- **`DEFAULT_CASING`** (const) - `repos/clap/clap_derive/src/item.rs:26` - Default casing style for generated arguments.
- **`DEFAULT_CONTEXT_STYLE`** (const) - `repos/clap-cargo/src/style.rs:94` - [`Renderer::context`] applied by [`Renderer::styled`]
- **`DEFAULT_EMPHASIS_STYLE`** (const) - `repos/clap-cargo/src/style.rs:85` - [`Renderer::emphasis`] applied by [`Renderer::styled`]
- **`DEFAULT_ENV_CASING`** (const) - `repos/clap/clap_derive/src/item.rs:29` - Default casing style for environment variables
- **`DEFAULT_ERROR_STYLE`** (const) - `repos/clap-cargo/src/style.rs:65` - [`Renderer::error`] applied by [`Renderer::styled`]
- **`DEFAULT_HELP_STYLE`** (const) - `repos/clap-cargo/src/style.rs:80` - [`Renderer::help`] applied by [`Renderer::styled`]
- **`DEFAULT_INFO_STYLE`** (const) - `repos/clap-cargo/src/style.rs:75` - [`Renderer::info`] applied by [`Renderer::styled`]
- **`DEFAULT_LINE_NUM_STYLE`** (const) - `repos/clap-cargo/src/style.rs:83` - [`Renderer::line_num`] applied by [`Renderer::styled`]
- **`default_missing_value`** (fn) - `repos/clap/clap_builder/src/builder/arg.rs:1894` - Value for the argument when the flag is present but no value is specified.
- **`default_missing_value_os`** (fn) - `repos/clap/clap_builder/src/builder/arg.rs:2002` - Value for the argument when the flag is present but no value is specified.
- **`default_missing_values`** (fn) - `repos/clap/clap_builder/src/builder/arg.rs:2014` - Value for the argument when the flag is present but no value is specified.
- **`default_missing_values_os`** (fn) - `repos/clap/clap_builder/src/builder/arg.rs:2025` - Value for the argument when the flag is present but no value is specified.
- **`DEFAULT_NONE_STYLE`** (const) - `repos/clap-cargo/src/style.rs:92` - [`Renderer::none`] applied by [`Renderer::styled`]
- **`DEFAULT_NOTE_STYLE`** (const) - `repos/clap-cargo/src/style.rs:77` - [`Renderer::note`] applied by [`Renderer::styled`]
- **`DEFAULT_REMOVAL_STYLE`** (const) - `repos/clap-cargo/src/style.rs:98` - [`Renderer::removal`] applied by [`Renderer::styled`]
- **`default_value`** (fn) - `repos/clap/clap_builder/src/builder/arg.rs:1785` - Value for the argument when not present.
- **`default_value_if`** (fn) - `repos/clap/clap_builder/src/builder/arg.rs:2935` - Specifies the value of the argument if `arg` has been used at runtime.
- **`default_value_ifs`** (fn) - `repos/clap/clap_builder/src/builder/arg.rs:3130` - Specifies multiple values and conditions in the same manner as [`Arg::default_value_if`].
- **`default_values`** (fn) - `repos/clap/clap_builder/src/builder/arg.rs:1871` - Value for the argument when not present.
- **`default_values_if`** (fn) - `repos/clap/clap_builder/src/builder/arg.rs:3072` - Specifies the values of the argument if `arg` has been used at runtime.
- **`default_values_ifs`** (fn) - `repos/clap/clap_builder/src/builder/arg.rs:3237` - Specifies multiple values and conditions in the same manner as [`Arg::default_values_if`].
- **`DEFAULT_WARNING_STYLE`** (const) - `repos/clap-cargo/src/style.rs:68` - [`Renderer::warning`] applied by [`Renderer::styled`]
- **`defer`** (fn) - `repos/clap/clap_builder/src/builder/command.rs:565` - Delay initialization for parts of the `Command`
- **`derive`** (module) - `repos/clap/clap_builder/src/derive.rs:1` - This module contains traits that are usable with the `#[derive(...)]`
- **`did_you_mean`** (fn) - `repos/clap/clap_builder/src/parser/features/suggestions.rs:4` - Find strings from an iterable of `possible_values` similar to a given value `v`
- **`did_you_mean_error`** (fn) - `repos/clap/clap_builder/src/parser/parser.rs:1547` - Is only used for the long flag(which is the only one needs fuzzy searching)
- **`did_you_mean_flag`** (fn) - `repos/clap/clap_builder/src/parser/features/suggestions.rs:48` - Returns a suffix that can be empty, or is the standard 'did you mean' phrase
- **`dir`** (fn) - `repos/clap/clap_complete/src/engine/custom.rs:236` - Complete only directories
- **`disable_colored_help`** (fn) - `repos/clap/clap_builder/src/builder/command.rs:1652` - Disables colorized help messages.
- **`disable_help_flag`** (fn) - `repos/clap/clap_builder/src/builder/command.rs:1558` - Disables `-h` and `--help` flag.
- **`disable_help_subcommand`** (fn) - `repos/clap/clap_builder/src/builder/command.rs:1617` - Disables the `help` [`subcommand`].
- **`disable_version_flag`** (fn) - `repos/clap/clap_builder/src/builder/command.rs:1445` - Disables `-V` and `--version` flag.
- **`Display`** (impl) - `repos/clap/clap_builder/src/builder/styled_str.rs:212` - Color-unaware printing. Never uses coloring.
- **`Display`** (impl) - `repos/clap/clap_builder/src/output/fmt.rs:78` - Color-unaware printing. Never uses coloring.
- **`display_name`** (fn) - `repos/clap/clap_builder/src/builder/command.rs:1903` - Overrides the runtime-determined display name of the program for help and error messages.
- **`display_order`** (fn) - `repos/clap/clap_builder/src/builder/arg.rs:2342` - Allows custom ordering of args within the help message.
- **`display_order`** (fn) - `repos/clap/clap_builder/src/builder/command.rs:3055` - Set the placement of this subcommand within the help.
- **`display_order`** (fn) - `repos/clap/clap_complete/src/engine/candidate.rs:49` - Sort weight within a [`CompletionCandidate::tag`]
- **`display_width`** (fn) - `repos/clap/clap_builder/src/output/textwrap/core.rs:1` - Compute the display width of `text`
- **`doc_comments`** (module) - `repos/clap/clap_derive/src/utils/doc_comments.rs:1` - The preprocessing we apply to doc comments.
- **`dont_delimit_trailing_values`** (fn) - `repos/clap/clap_builder/src/builder/command.rs:1254` - Disables the automatic [delimiting of values][Arg::value_delimiter] after `--` or when [`Arg::tra...
- **`dummies`** (module) - `repos/clap/clap_derive/src/dummies.rs:1` - Dummy implementations that we emit along with an error.
- **`Elvish`** (struct) - `repos/clap/clap_complete/src/aot/shells/elvish.rs:9` - Generate elvish completion file
- **`Elvish`** (struct) - `repos/clap/clap_complete/src/env/shells.rs:140` - Elvish completion adapter
- **`EMPTY`** (const) - `repos/clap/clap_builder/src/builder/range.rs:9` - Nor argument values, or a flag
- **`EnumValueParser`** (struct) - `repos/clap/clap_builder/src/builder/value_parser.rs:1040` - Parse an [`ValueEnum`][crate::ValueEnum] value.
- **`env`** (fn) - `repos/clap/clap_builder/src/builder/arg.rs:2041` - Read from `name` environment variable when argument is not present.
- **`EnvCompleter`** (trait) - `repos/clap/clap_complete/src/env/mod.rs:342` - Shell-integration for completions
- **`error`** (fn) - `repos/clap/clap_builder/src/builder/command.rs:625` - Custom error message for post-parsing validation
- **`error`** (fn) - `repos/clap/clap_builder/src/builder/styling.rs:82` - Error heading
- **`Error`** (struct) - `repos/clap/clap_builder/src/error/mod.rs:55` - Command Line Argument Parser Error
- **`Error`** (type) - `repos/clap/clap_builder/src/lib.rs:25` - Command Line Argument Parser Error
- **`ErrorFormatter`** (trait) - `repos/clap/clap_builder/src/error/format.rs:19` - Defines how to format an error for displaying to the user
- **`ErrorKind`** (enum) - `repos/clap/clap_builder/src/error/kind.rs:1` - Command line argument parser kind of error
- **`escape_help`** (fn) - `repos/clap/clap_complete/src/aot/shells/zsh.rs:429` - Escape help string inside single quotes and brackets
- **`escape_help`** (fn) - `repos/clap/clap_complete/src/env/shells.rs:462` - Escape help string
- **`escape_value`** (fn) - `repos/clap/clap_complete/src/aot/shells/zsh.rs:442` - Escape value string inside single quotes and parentheses
- **`escape_value`** (fn) - `repos/clap/clap_complete/src/env/shells.rs:457` - Escape value string
- **`escaped_positional`** (module) - `repos/clap/src/_cookbook/escaped_positional.rs:1` - # Example (Builder API)
- **`escaped_positional_derive`** (module) - `repos/clap/src/_cookbook/escaped_positional_derive.rs:1` - # Example (Derive API)
- **`exclusive`** (fn) - `repos/clap/clap_builder/src/builder/arg.rs:834` - This argument must be passed alone; it conflicts with all other arguments.
- **`exit`** (fn) - `repos/clap/clap_builder/src/error/mod.rs:241` - Prints the error and exits.
- **`exit_code`** (fn) - `repos/clap/clap_builder/src/error/mod.rs:229` - Returns the exit code that `.exit` will exit the process with.
- **`extend_context_unchecked`** (fn) - `repos/clap/clap_builder/src/error/mod.rs:351` - Does not verify if `ContextKind` is already present
- **`external_subcommand_value_parser`** (fn) - `repos/clap/clap_builder/src/builder/command.rs:3214` - Specifies how to parse external subcommand arguments.
- **`FALSE_LITERALS`** (const) - `repos/clap/clap_builder/src/util/str_to_bool.rs:4` - False values are `n`, `no`, `f`, `false`, `off`, and `0`.
- **`FalseyValueParser`** (struct) - `repos/clap/clap_builder/src/builder/value_parser.rs:1736` - Parse false-like string values, everything else is `true`
- **`features`** (module) - `repos/clap-cargo/src/features.rs:1` - Cargo Feature Flags.
- **`Features`** (struct) - `repos/clap-cargo/src/features.rs:3` - Cargo Feature Flags.
- **`field_methods`** (fn) - `repos/clap/clap_derive/src/item.rs:983` - generate methods on top of a field
- **`file`** (fn) - `repos/clap/clap_complete/src/engine/custom.rs:231` - Complete only files
- **`file_name`** (fn) - `repos/clap/clap_complete/src/aot/generator/mod.rs:15` - Returns the file name that is created when this generator is called during compile time.
- **`filter`** (fn) - `repos/clap/clap_complete/src/engine/custom.rs:247` - Select which paths should be completed
- **`find`** (module) - `repos/clap/src/_cookbook/find.rs:1` - # Example: find-like CLI (Builder API)
- **`find_duplicates`** (fn) - `repos/clap/clap_builder/src/builder/debug_asserts.rs:456` - Find duplicates in a sorted array.
- **`find_long_subcmd`** (fn) - `repos/clap/clap_builder/src/builder/command.rs:5117` - Find a flag subcommand name by long flag or an alias
- **`find_short_subcmd`** (fn) - `repos/clap/clap_builder/src/builder/command.rs:5110` - Find a flag subcommand name by short flag or an alias
- **`find_subcommand`** (fn) - `repos/clap/clap_builder/src/builder/command.rs:3973` - Find subcommand such that its name or one of aliases equals `name`.
- **`find_subcommand_mut`** (fn) - `repos/clap/clap_builder/src/builder/command.rs:3982` - Find subcommand such that its name or one of aliases equals `name`, returning
- **`find_subcommand_with_path`** (fn) - `repos/clap/clap_complete/src/aot/generator/utils.rs:19` - Finds the subcommand [`clap::Command`] from the given [`clap::Command`] with the given path.
- **`Fish`** (struct) - `repos/clap/clap_complete/src/aot/shells/fish.rs:7` - Generate fish completion file
- **`Fish`** (struct) - `repos/clap/clap_complete/src/env/shells.rs:202` - Fish completion adapter
- **`flags`** (fn) - `repos/clap/clap_complete/src/aot/generator/utils.rs:123` - Gets all the flags of a [`clap::Command`].
- **`FlatMap`** (struct) - `repos/clap/clap_builder/src/util/flat_map.rs:5` - Flat (Vec) backed map
- **`FlatSet`** (struct) - `repos/clap/clap_builder/src/util/flat_set.rs:5` - Flat (Vec) backed set
- **`flatten_help`** (fn) - `repos/clap/clap_builder/src/builder/command.rs:2345` - Flatten subcommand help into the current command's help
- **`format`** (fn) - `repos/clap/clap_builder/src/error/mod.rs:92` - Format the existing message with the Command's context
- **`format_error`** (fn) - `repos/clap/clap_builder/src/error/format.rs:21` - Stylize the error for the terminal
- **`forward_metadata`** (fn) - `repos/clap-cargo/src/features.rs:22` - Forward these flags to the `cargo_metadata` crate.
- **`From`** (impl) - `repos/clap/clap_builder/src/builder/value_parser.rs:271` - Convert a [`TypedValueParser`] to [`ValueParser`]
- **`From`** (impl) - `repos/clap/clap_builder/src/builder/value_parser.rs:309` - Create an `i64` [`ValueParser`] from a `N..M` range
- **`From`** (impl) - `repos/clap/clap_builder/src/builder/value_parser.rs:340` - Create an `i64` [`ValueParser`] from a `N..=M` range
- **`From`** (impl) - `repos/clap/clap_builder/src/builder/value_parser.rs:371` - Create an `i64` [`ValueParser`] from a `N..` range
- **`From`** (impl) - `repos/clap/clap_builder/src/builder/value_parser.rs:402` - Create an `i64` [`ValueParser`] from a `..M` range
- **`From`** (impl) - `repos/clap/clap_builder/src/builder/value_parser.rs:433` - Create an `i64` [`ValueParser`] from a `..=M` range
- **`From`** (impl) - `repos/clap/clap_builder/src/builder/value_parser.rs:464` - Create an `i64` [`ValueParser`] from a `..` range
- **`From`** (impl) - `repos/clap/clap_builder/src/builder/value_parser.rs:530` - Create a [`ValueParser`] with [`PossibleValuesParser`]
- **`from_arg_matches`** (fn) - `repos/clap/clap_builder/src/derive.rs:131` - Instantiate `Self` from [`ArgMatches`], parsing the arguments as needed.
- **`from_arg_matches_mut`** (fn) - `repos/clap/clap_builder/src/derive.rs:167` - Instantiate `Self` from [`ArgMatches`], parsing the arguments as needed.
- **`from_env`** (fn) - `repos/clap/clap_complete/src/aot/shells/shell.rs:116` - Determine the user's current shell from the environment
- **`from_shell_path`** (fn) - `repos/clap/clap_complete/src/aot/shells/shell.rs:101` - Parse a shell from a path to the executable for the shell
- **`from_str`** (fn) - `repos/clap/clap_builder/src/derive.rs:297` - Parse an argument into `Self`.
- **`FromArgMatches`** (trait) - `repos/clap/clap_builder/src/derive.rs:127` - Converts an instance of [`ArgMatches`] to a user-defined container.
- **`gen_augment`** (fn) - `repos/clap/clap_derive/src/derives/args.rs:167` - Generate a block of code to add arguments/subcommands corresponding to
- **`gen_subcommand_helpers`** (fn) - `repos/clap/clap_complete/src/aot/shells/fish.rs:214` - Print fish's helpers for easy handling subcommands.
- **`generate`** (fn) - `repos/clap/clap_complete/src/aot/generator/mod.rs:40` - Generates output out of [`clap::Command`].
- **`generate`** (fn) - `repos/clap/clap_complete/src/aot/generator/mod.rs:258` - Generate a completions file for a specified shell at runtime.
- **`generate_to`** (fn) - `repos/clap/clap_complete/src/aot/generator/mod.rs:105` - Generate a completions file for a specified shell at compile-time.
- **`Generator`** (trait) - `repos/clap/clap_complete/src/aot/generator/mod.rs:13` - Generator trait which can be used to write generators
- **`get`** (fn) - `repos/clap/clap_builder/src/builder/arg.rs:4560` - Access an [`ArgExt`]
- **`get`** (fn) - `repos/clap/clap_builder/src/builder/command.rs:4288` - Access an [`CommandExt`]
- **`get`** (fn) - `repos/clap/clap_builder/src/error/mod.rs:190` - Lookup a piece of context
- **`get`** (fn) - `repos/clap/clap_builder/src/mkeymap.rs:98` - Find the arg have corresponding key in this map, we can search the key
- **`get_about`** (fn) - `repos/clap/clap_builder/src/builder/command.rs:3806` - Get the help message specified via [`Command::about`].
- **`get_action`** (fn) - `repos/clap/clap_builder/src/builder/arg.rs:4457` - Behavior when parsing the argument
- **`get_after_help`** (fn) - `repos/clap/clap_builder/src/builder/command.rs:3961` - Returns the help heading for listing subcommands.
- **`get_after_long_help`** (fn) - `repos/clap/clap_builder/src/builder/command.rs:3967` - Returns the help heading for listing subcommands.
- **`get_aliases`** (fn) - `repos/clap/clap_builder/src/builder/arg.rs:4300` - Get hidden aliases for this argument, if any
- **`get_aliases`** (fn) - `repos/clap/clap_builder/src/builder/command.rs:3879` - Iterate through the *hidden* aliases for this subcommand.
- **`get_all_aliases`** (fn) - `repos/clap/clap_builder/src/builder/arg.rs:4277` - Get *all* aliases for this argument, if any, both visible and hidden.
- **`get_all_aliases`** (fn) - `repos/clap/clap_builder/src/builder/command.rs:3861` - Iterate through the set of *all* the aliases for this subcommand, both visible and hidden.
- **`get_all_long_flag_aliases`** (fn) - `repos/clap/clap_builder/src/builder/command.rs:3873` - Iterate through the set of *all* the long aliases for this subcommand, both visible and hidden.
- **`get_all_short_aliases`** (fn) - `repos/clap/clap_builder/src/builder/arg.rs:4233` - Get *all* short aliases for this argument, if any, both visible and hidden.
- **`get_all_short_flag_aliases`** (fn) - `repos/clap/clap_builder/src/builder/command.rs:3867` - Iterate through the set of *all* the short aliases for this subcommand, both visible and hidden.
- **`get_arg_conflicts_with`** (fn) - `repos/clap/clap_builder/src/builder/command.rs:4019` - Get a list of all arguments the given argument conflicts with.
- **`get_args`** (fn) - `repos/clap/clap_builder/src/builder/arg_group.rs:177` - Getters for all args. It will return a vector of `Id`
- **`get_arguments`** (fn) - `repos/clap/clap_builder/src/builder/command.rs:4001` - Iterate through the set of arguments.
- **`get_author`** (fn) - `repos/clap/clap_builder/src/builder/command.rs:3788` - Get the authors of the cmd.
- **`get_before_help`** (fn) - `repos/clap/clap_builder/src/builder/command.rs:3949` - Returns the help heading for listing subcommands.
- **`get_before_long_help`** (fn) - `repos/clap/clap_builder/src/builder/command.rs:3955` - Returns the help heading for listing subcommands.
- **`get_bin_name`** (fn) - `repos/clap/clap_builder/src/builder/command.rs:3734` - Get the name of the binary.
- **`get_bin_name_fallback`** (fn) - `repos/clap/clap_builder/src/builder/command.rs:3740` - Get the name of the binary.
- **`get_color`** (fn) - `repos/clap/clap_builder/src/builder/command.rs:3893` - Should we color the output?
- **`get_context`** (fn) - `repos/clap/clap_builder/src/builder/styling.rs:187` - Highlight all specified contexts, e.g. `[default: false]`
- **`get_context_value`** (fn) - `repos/clap/clap_builder/src/builder/styling.rs:195` - Highlight values within all of the context, e.g. the `false` in `[default: false]`
- **`get_count`** (fn) - `repos/clap/clap_builder/src/parser/matches/arg_matches.rs:122` - Gets the value of a specific [`ArgAction::Count`][crate::ArgAction::Count] flag
- **`get_default_values`** (fn) - `repos/clap/clap_builder/src/builder/arg.rs:4401` - Get the default values specified for this argument, if any
- **`get_display_name`** (fn) - `repos/clap/clap_builder/src/builder/command.rs:3728` - Get the name of the binary.
- **`get_display_order`** (fn) - `repos/clap/clap_builder/src/builder/arg.rs:4196` - Get the placement within help
- **`get_display_order`** (fn) - `repos/clap/clap_builder/src/builder/command.rs:3782` - Get the placement within help
- **`get_display_order`** (fn) - `repos/clap/clap_complete/src/engine/candidate.rs:98` - Get the grouping tag
- **`get_env`** (fn) - `repos/clap/clap_builder/src/builder/arg.rs:4385` - Get the environment variable name specified for this argument, if any
- **`get_error`** (fn) - `repos/clap/clap_builder/src/builder/styling.rs:151` - Error heading
- **`get_external_subcommand_value_parser`** (fn) - `repos/clap/clap_builder/src/builder/command.rs:4243` - Configured parser for values passed to an external subcommand
- **`get_flag`** (fn) - `repos/clap/clap_builder/src/parser/matches/arg_matches.rs:154` - Gets the value of a specific [`ArgAction::SetTrue`][crate::ArgAction::SetTrue] or [`ArgAction::Se...
- **`get_global_arg_conflicts_with`** (fn) - `repos/clap/clap_builder/src/builder/command.rs:4051` - Get a unique list of all arguments of all commands and continuous subcommands the given argument ...
- **`get_groups`** (fn) - `repos/clap/clap_builder/src/builder/command.rs:3995` - Iterate through the set of groups.
- **`get_header`** (fn) - `repos/clap/clap_builder/src/builder/styling.rs:145` - General Heading style, e.g. [`help_heading`][crate::Arg::help_heading]
- **`get_help`** (fn) - `repos/clap/clap_builder/src/builder/arg.rs:4174` - Get the help specified for this argument, if any
- **`get_help`** (fn) - `repos/clap/clap_builder/src/builder/possible_value.rs:167` - Get the help specified for this argument, if any
- **`get_help`** (fn) - `repos/clap/clap_complete/src/engine/candidate.rs:83` - Get the help message of the completion candidate
- **`get_help_heading`** (fn) - `repos/clap/clap_builder/src/builder/arg.rs:4202` - Get the help heading specified for this argument, if any
- **`get_id`** (fn) - `repos/clap/clap_builder/src/builder/arg.rs:4168` - Get the name of the argument
- **`get_id`** (fn) - `repos/clap/clap_builder/src/builder/arg_group.rs:518` - Get the name of the group
- **`get_id`** (fn) - `repos/clap/clap_complete/src/engine/candidate.rs:88` - Get the id used for de-duplicating
- **`get_index`** (fn) - `repos/clap/clap_builder/src/builder/arg.rs:4362` - Get the index of this argument, if any
- **`get_invalid`** (fn) - `repos/clap/clap_builder/src/builder/styling.rs:181` - Highlight invalid usage
- **`get_literal`** (fn) - `repos/clap/clap_builder/src/builder/styling.rs:163` - Literal command-line syntax, e.g. `--help`
- **`get_long`** (fn) - `repos/clap/clap_builder/src/builder/arg.rs:4256` - Get the long option name for this argument, if any
- **`get_long_about`** (fn) - `repos/clap/clap_builder/src/builder/command.rs:3814` - Get the help message specified via [`Command::long_about`].
- **`get_long_and_visible_aliases`** (fn) - `repos/clap/clap_builder/src/builder/arg.rs:4287` - Get the long option name and its visible aliases, if any
- **`get_long_flag`** (fn) - `repos/clap/clap_builder/src/builder/command.rs:3800` - Get the long flag of the subcommand.
- **`get_long_help`** (fn) - `repos/clap/clap_builder/src/builder/arg.rs:4180` - Get the long help specified for this argument, if any
- **`get_long_version`** (fn) - `repos/clap/clap_builder/src/builder/command.rs:3776` - Get the long version of the cmd.
- **`get_many`** (fn) - `repos/clap/clap_builder/src/parser/matches/arg_matches.rs:191` - Iterate over values of a specific option or positional argument.
- **`get_matches`** (fn) - `repos/clap/clap_builder/src/builder/command.rs:646` - Parse [`env::args_os`], [exiting][Error::exit] on failure.
- **`get_matches_from`** (fn) - `repos/clap/clap_builder/src/builder/command.rs:732` - Parse the specified arguments, [exiting][Error::exit] on failure.
- **`get_matches_mut`** (fn) - `repos/clap/clap_builder/src/builder/command.rs:668` - Parse [`env::args_os`], [exiting][Error::exit] on failure.
- **`get_name`** (fn) - `repos/clap/clap_builder/src/builder/command.rs:3751` - Get the name of the cmd.
- **`get_name`** (fn) - `repos/clap/clap_builder/src/builder/possible_value.rs:161` - Get the name of the argument value
- **`get_name_and_aliases`** (fn) - `repos/clap/clap_builder/src/builder/possible_value.rs:199` - Returns all valid values of the argument value.
- **`get_name_and_visible_aliases`** (fn) - `repos/clap/clap_builder/src/builder/command.rs:3763` - Get all known names of the cmd (i.e. primary name and visible aliases).
- **`get_next_help_heading`** (fn) - `repos/clap/clap_builder/src/builder/command.rs:3828` - Get the custom section heading specified via [`Command::next_help_heading`].
- **`get_non_positionals`** (fn) - `repos/clap/clap_builder/src/builder/command.rs:4938` - Iterate through the *flags* & *options* arguments.
- **`get_num_args`** (fn) - `repos/clap/clap_builder/src/builder/arg.rs:4338` - Get the number of values for this argument.
- **`get_occurrences`** (fn) - `repos/clap/clap_builder/src/parser/matches/arg_matches.rs:232` - Iterate over the values passed to each occurrence of an option.
- **`get_one`** (fn) - `repos/clap/clap_builder/src/parser/matches/arg_matches.rs:78` - Gets the value of a specific option or positional argument.
- **`get_opts`** (fn) - `repos/clap/clap_builder/src/builder/command.rs:4013` - Iterate through the *options*.
- **`get_placeholder`** (fn) - `repos/clap/clap_builder/src/builder/styling.rs:169` - Descriptions within command-line syntax, e.g. [`value_name`][crate::Arg::value_name]
- **`get_positionals`** (fn) - `repos/clap/clap_builder/src/builder/command.rs:4007` - Iterate through the *positionals* arguments.
- **`get_possible_values`** (fn) - `repos/clap/clap_builder/src/builder/arg.rs:4315` - Get the names of possible values for this argument. Only useful for user
- **`get_raw`** (fn) - `repos/clap/clap_builder/src/parser/matches/arg_matches.rs:270` - Iterate over the original argument values.
- **`get_raw_occurrences`** (fn) - `repos/clap/clap_builder/src/parser/matches/arg_matches.rs:317` - Iterate over the original values for each occurrence of an option.
- **`get_short`** (fn) - `repos/clap/clap_builder/src/builder/arg.rs:4211` - Get the short option name for this argument, if any
- **`get_short_and_visible_aliases`** (fn) - `repos/clap/clap_builder/src/builder/arg.rs:4243` - Get the short option name and its visible aliases, if any
- **`get_short_flag`** (fn) - `repos/clap/clap_builder/src/builder/command.rs:3794` - Get the short flag of the subcommand.
- **`get_styles`** (fn) - `repos/clap/clap_builder/src/builder/command.rs:3913` - Return the current `Styles` for the `Command`
- **`get_subcommand_help_heading`** (fn) - `repos/clap/clap_builder/src/builder/command.rs:3937` - Returns the help heading for listing subcommands.
- **`get_subcommand_value_name`** (fn) - `repos/clap/clap_builder/src/builder/command.rs:3943` - Returns the subcommand value name.
- **`get_subcommands`** (fn) - `repos/clap/clap_builder/src/builder/command.rs:3919` - Iterate through the set of subcommands, getting a reference to each.
- **`get_subcommands_containing`** (fn) - `repos/clap/clap_builder/src/builder/command.rs:4081` - Get a list of subcommands which contain the provided Argument
- **`get_subcommands_mut`** (fn) - `repos/clap/clap_builder/src/builder/command.rs:3925` - Iterate through the set of subcommands, getting a mutable reference to each.
- **`get_tag`** (fn) - `repos/clap/clap_complete/src/engine/candidate.rs:93` - Get the grouping tag
- **`get_usage`** (fn) - `repos/clap/clap_builder/src/builder/styling.rs:157` - Usage heading
- **`get_valid`** (fn) - `repos/clap/clap_builder/src/builder/styling.rs:175` - Highlight suggested usage
- **`get_value`** (fn) - `repos/clap/clap_complete/src/engine/candidate.rs:78` - Get the literal value being proposed for completion
- **`get_value_delimiter`** (fn) - `repos/clap/clap_builder/src/builder/arg.rs:4349` - Get the delimiter between multiple values
- **`get_value_hint`** (fn) - `repos/clap/clap_builder/src/builder/arg.rs:4368` - Get the value hint of this argument
- **`get_value_names`** (fn) - `repos/clap/clap_builder/src/builder/arg.rs:4328` - Get the names of values for this argument.
- **`get_value_parser`** (fn) - `repos/clap/clap_builder/src/builder/arg.rs:4463` - Configured parser for argument values
- **`get_value_terminator`** (fn) - `repos/clap/clap_builder/src/builder/arg.rs:4355` - Get the value terminator for this argument. The `value_terminator` is a value
- **`get_version`** (fn) - `repos/clap/clap_builder/src/builder/command.rs:3770` - Get the version of the cmd.
- **`get_visible_aliases`** (fn) - `repos/clap/clap_builder/src/builder/arg.rs:4262` - Get visible aliases for this argument, if any
- **`get_visible_aliases`** (fn) - `repos/clap/clap_builder/src/builder/command.rs:3834` - Iterate through the *visible* aliases for this subcommand.
- **`get_visible_long_flag_aliases`** (fn) - `repos/clap/clap_builder/src/builder/command.rs:3852` - Iterate through the *visible* long aliases for this subcommand.
- **`get_visible_quoted_name`** (fn) - `repos/clap/clap_builder/src/builder/possible_value.rs:184` - Get the name if argument value is not hidden, `None` otherwise,
- **`get_visible_short_aliases`** (fn) - `repos/clap/clap_builder/src/builder/arg.rs:4217` - Get visible short aliases for this argument, if any
- **`get_visible_short_flag_aliases`** (fn) - `repos/clap/clap_builder/src/builder/command.rs:3843` - Iterate through the *visible* short aliases for this subcommand.
- **`git`** (module) - `repos/clap/src/_cookbook/git.rs:1` - # Example: git-like CLI (Builder API)
- **`git_derive`** (module) - `repos/clap/src/_cookbook/git_derive.rs:1` - # Example: git-like CLI (Derive API)
- **`global`** (fn) - `repos/clap/clap_builder/src/builder/arg.rs:877` - Specifies that an argument can be matched to all child [`Subcommand`]s.
- **`group`** (fn) - `repos/clap/clap_builder/src/builder/arg.rs:2846` - The name of the [`ArgGroup`] the argument belongs to.
- **`group`** (fn) - `repos/clap/clap_builder/src/builder/command.rs:434` - Adds an [`ArgGroup`] to the application.
- **`group_id`** (fn) - `repos/clap/clap_builder/src/derive.rs:228` - Report the [`ArgGroup::id`][crate::ArgGroup::id] for this set of arguments
- **`groups`** (fn) - `repos/clap/clap_builder/src/builder/arg.rs:2892` - The names of [`ArgGroup`]'s the argument belongs to.
- **`groups`** (fn) - `repos/clap/clap_builder/src/builder/command.rs:473` - Adds multiple [`ArgGroup`]s to the [`Command`] at once.
- **`groups_for_arg`** (fn) - `repos/clap/clap_builder/src/builder/command.rs:5009` - Iterate through the groups this arg is member of.
- **`has_subcommand`** (fn) - `repos/clap/clap_builder/src/derive.rs:277` - Test whether `Self` can parse a specific subcommand
- **`has_subcommands`** (fn) - `repos/clap/clap_builder/src/builder/command.rs:3931` - Returns `true` if this `Command` has subcommands.
- **`header`** (fn) - `repos/clap/clap_builder/src/builder/styling.rs:75` - General Heading style, e.g. [`help_heading`][crate::Arg::help_heading]
- **`help`** (fn) - `repos/clap/clap_builder/src/builder/arg.rs:2219` - Sets the description of the argument for short help (`-h`).
- **`help`** (fn) - `repos/clap/clap_builder/src/builder/possible_value.rs:77` - Sets the help description of the value.
- **`help`** (fn) - `repos/clap/clap_builder/src/output/help_template.rs:606` - Writes argument's help to the wrapped stream.
- **`help`** (fn) - `repos/clap/clap_complete/src/engine/candidate.rs:27` - Set the help message of the completion candidate
- **`help_expected`** (fn) - `repos/clap/clap_builder/src/builder/command.rs:1678` - Panic if help descriptions are omitted.
- **`help_heading`** (fn) - `repos/clap/clap_builder/src/builder/arg.rs:2413` - Override the `--help` section this appears in.
- **`help_template`** (fn) - `repos/clap/clap_builder/src/builder/command.rs:2246` - Sets the help template to be used, overriding the default format.
- **`HelpTemplate`** (struct) - `repos/clap/clap_builder/src/output/help_template.rs:79` - Help template writer
- **`HelpTemplate`** (impl) - `repos/clap/clap_builder/src/output/help_template.rs:255` - Basic template methods
- **`HelpTemplate`** (impl) - `repos/clap/clap_builder/src/output/help_template.rs:369` - Arg handling
- **`HelpTemplate`** (impl) - `repos/clap/clap_builder/src/output/help_template.rs:876` - Subcommand handling
- **`hidden_longs_aliases`** (fn) - `repos/clap/clap_complete/src/engine/complete.rs:493` - Gets all the long hidden aliases and flags of a [`clap::Command`].
- **`hide`** (fn) - `repos/clap/clap_builder/src/builder/arg.rs:2483` - Do not display the argument in help message.
- **`hide`** (fn) - `repos/clap/clap_builder/src/builder/command.rs:3107` - Specifies that this [`subcommand`] should be hidden from help messages
- **`hide`** (fn) - `repos/clap/clap_builder/src/builder/possible_value.rs:98` - Hides this value from help and shell completions.
- **`hide`** (fn) - `repos/clap/clap_complete/src/engine/candidate.rs:55` - Set the visibility of the completion candidate
- **`hide_default_value`** (fn) - `repos/clap/clap_builder/src/builder/arg.rs:2569` - Do not display the default value of the argument in the help message.
- **`hide_env`** (fn) - `repos/clap/clap_builder/src/builder/arg.rs:2605` - Do not display in help the environment variable name.
- **`hide_env_values`** (fn) - `repos/clap/clap_builder/src/builder/arg.rs:2635` - Do not display in help any values inside the associated ENV variables for the argument.
- **`hide_long_help`** (fn) - `repos/clap/clap_builder/src/builder/arg.rs:2758` - Hides an argument from long help (`--help`).
- **`hide_possible_values`** (fn) - `repos/clap/clap_builder/src/builder/arg.rs:2531` - Do not display the [possible values][crate::builder::ValueParser::possible_values] in the help me...
- **`hide_possible_values`** (fn) - `repos/clap/clap_builder/src/builder/command.rs:1741` - Tells `clap` *not* to print possible values when displaying help information.
- **`hide_short_help`** (fn) - `repos/clap/clap_builder/src/builder/arg.rs:2666` - Hides an argument from short help (`-h`).
- **`id`** (fn) - `repos/clap/clap_builder/src/builder/arg.rs:126` - Set the identifier used for referencing this argument in the clap API.
- **`id`** (fn) - `repos/clap/clap_builder/src/builder/arg_group.rs:96` - Sets the group name.
- **`Id`** (struct) - `repos/clap/clap_builder/src/util/id.rs:5` - [`Arg`][crate::Arg] or [`ArgGroup`][crate::ArgGroup] identifier
- **`id`** (fn) - `repos/clap/clap_complete/src/engine/candidate.rs:33` - Only first for a given Id is shown
- **`id_exists`** (fn) - `repos/clap/clap_builder/src/builder/command.rs:5003` - Checks if there is an argument or group with the given id.
- **`ids`** (fn) - `repos/clap/clap_builder/src/parser/matches/arg_matches.rs:527` - Iterate over [`Arg`][crate::Arg] and [`ArgGroup`][crate::ArgGroup] [`Id`]s via [`ArgMatches::ids`].
- **`IdsRef`** (struct) - `repos/clap/clap_builder/src/parser/matches/arg_matches.rs:1362` - Iterate over [`Arg`][crate::Arg] and [`ArgGroup`][crate::ArgGroup] [`Id`]s via [`ArgMatches::ids`].
- **`ignore_case`** (fn) - `repos/clap/clap_builder/src/builder/arg.rs:1405` - Match values against [`PossibleValuesParser`][crate::builder::PossibleValuesParser] without match...
- **`ignore_errors`** (fn) - `repos/clap/clap_builder/src/builder/command.rs:1194` - Try not to fail on parse errors, like missing option values.
- **`index`** (fn) - `repos/clap/clap_builder/src/builder/arg.rs:469` - Specifies the index of a positional argument **starting at** 1.
- **`index_of`** (fn) - `repos/clap/clap_builder/src/parser/matches/arg_matches.rs:615` - The first index of that an argument showed up.
- **`Indices`** (struct) - `repos/clap/clap_builder/src/parser/matches/arg_matches.rs:1820` - Iterate over indices for where an argument appeared when parsing, via [`ArgMatches::indices_of`]
- **`indices_of`** (fn) - `repos/clap/clap_builder/src/parser/matches/arg_matches.rs:773` - All indices an argument appeared at when parsing.
- **`infer_long_args`** (fn) - `repos/clap/clap_builder/src/builder/command.rs:1762` - Allow partial matches of long arguments or their [aliases].
- **`infer_subcommands`** (fn) - `repos/clap/clap_builder/src/builder/command.rs:1791` - Allow partial matches of [subcommand] names and their [aliases].
- **`initial_top_level_methods`** (fn) - `repos/clap/clap_derive/src/item.rs:966` - generate methods from attributes on top of struct or enum
- **`insert`** (fn) - `repos/clap/clap_builder/src/error/mod.rs:197` - Insert a piece of context
- **`insert_context_unchecked`** (fn) - `repos/clap/clap_builder/src/error/mod.rs:339` - Does not verify if `ContextKind` is already present
- **`into_resettable`** (fn) - `repos/clap/clap_builder/src/builder/resettable.rs:66` - Convert to the intended resettable type
- **`IntoResettable`** (trait) - `repos/clap/clap_builder/src/builder/resettable.rs:64` - Convert to the intended resettable type
- **`invalid`** (fn) - `repos/clap/clap_builder/src/builder/styling.rs:117` - Highlight invalid usage
- **`is`** (fn) - `repos/clap/clap_complete/src/env/mod.rs:357` - Whether the name matches this shell
- **`is_allow_external_subcommands_set`** (fn) - `repos/clap/clap_builder/src/builder/command.rs:4238` - Report whether [`Command::allow_external_subcommands`] is set
- **`is_allow_hyphen_values_set`** (fn) - `repos/clap/clap_builder/src/builder/arg.rs:4447` - Report whether [`Arg::allow_hyphen_values`] is set
- **`is_allow_missing_positional_set`** (fn) - `repos/clap/clap_builder/src/builder/command.rs:4223` - Report whether [`Command::allow_missing_positional`] is set
- **`is_allow_negative_numbers_set`** (fn) - `repos/clap/clap_builder/src/builder/arg.rs:4452` - Report whether [`Arg::allow_negative_numbers`] is set
- **`is_arg_required_else_help_set`** (fn) - `repos/clap/clap_builder/src/builder/command.rs:4185` - Report whether [`Command::arg_required_else_help`] is set
- **`is_args_conflicts_with_subcommands_set`** (fn) - `repos/clap/clap_builder/src/builder/command.rs:4263` - Report whether [`Command::args_conflicts_with_subcommands`] is set
- **`is_disable_colored_help_set`** (fn) - `repos/clap/clap_builder/src/builder/command.rs:4155` - Report whether [`Command::disable_colored_help`] is set
- **`is_disable_help_flag_set`** (fn) - `repos/clap/clap_builder/src/builder/command.rs:4145` - Report whether [`Command::disable_help_flag`] is set
- **`is_disable_help_subcommand_set`** (fn) - `repos/clap/clap_builder/src/builder/command.rs:4150` - Report whether [`Command::disable_help_subcommand`] is set
- **`is_disable_version_flag_set`** (fn) - `repos/clap/clap_builder/src/builder/command.rs:4129` - Report whether [`Command::disable_version_flag`] is set
- **`is_dont_delimit_trailing_values_set`** (fn) - `repos/clap/clap_builder/src/builder/command.rs:4124` - Report whether [`Command::dont_delimit_trailing_values`] is set
- **`is_exclusive_set`** (fn) - `repos/clap/clap_builder/src/builder/arg.rs:4540` - Reports whether [`Arg::exclusive`] is set
- **`is_flatten_help_set`** (fn) - `repos/clap/clap_builder/src/builder/command.rs:3822` - Get the custom section heading specified via [`Command::flatten_help`].
- **`is_global_set`** (fn) - `repos/clap/clap_builder/src/builder/arg.rs:4488` - Report whether [`Arg::global`] is set
- **`is_help_expected_set`** (fn) - `repos/clap/clap_builder/src/builder/command.rs:4160` - Report whether [`Command::help_expected`] is set
- **`is_hide_default_value_set`** (fn) - `repos/clap/clap_builder/src/builder/arg.rs:4503` - Report whether [`Arg::hide_default_value`] is set
- **`is_hide_env_set`** (fn) - `repos/clap/clap_builder/src/builder/arg.rs:4513` - Report whether [`Arg::hide_env`] is set
- **`is_hide_env_values_set`** (fn) - `repos/clap/clap_builder/src/builder/arg.rs:4519` - Report whether [`Arg::hide_env_values`] is set
- **`is_hide_long_help_set`** (fn) - `repos/clap/clap_builder/src/builder/arg.rs:4530` - Report whether [`Arg::hide_long_help`] is set
- **`is_hide_possible_values_set`** (fn) - `repos/clap/clap_builder/src/builder/arg.rs:4508` - Report whether [`Arg::hide_possible_values`] is set
- **`is_hide_set`** (fn) - `repos/clap/clap_builder/src/builder/arg.rs:4498` - Report whether [`Arg::hide`] is set
- **`is_hide_set`** (fn) - `repos/clap/clap_builder/src/builder/command.rs:4228` - Report whether [`Command::hide`] is set
- **`is_hide_set`** (fn) - `repos/clap/clap_builder/src/builder/possible_value.rs:173` - Report if [`PossibleValue::hide`] is set
- **`is_hide_set`** (fn) - `repos/clap/clap_complete/src/engine/candidate.rs:103` - Get the visibility of the completion candidate
- **`is_hide_short_help_set`** (fn) - `repos/clap/clap_builder/src/builder/arg.rs:4525` - Report whether [`Arg::hide_short_help`] is set
- **`is_ignore_case_set`** (fn) - `repos/clap/clap_builder/src/builder/arg.rs:4555` - Reports whether [`Arg::ignore_case`] is set
- **`is_ignore_errors_set`** (fn) - `repos/clap/clap_builder/src/builder/command.rs:4119` - Report whether [`Command::ignore_errors`] is set
- **`is_infer_long_args_set`** (fn) - `repos/clap/clap_builder/src/builder/command.rs:4175` - Report whether [`Command::infer_long_args`] is set
- **`is_infer_subcommands_set`** (fn) - `repos/clap/clap_builder/src/builder/command.rs:4180` - Report whether [`Command::infer_subcommands`] is set
- **`is_last_set`** (fn) - `repos/clap/clap_builder/src/builder/arg.rs:4550` - Reports whether [`Arg::last`] is set
- **`is_multicall_set`** (fn) - `repos/clap/clap_builder/src/builder/command.rs:4283` - Report whether [`Command::multicall`] is set
- **`is_multiple`** (fn) - `repos/clap/clap_builder/src/builder/arg.rs:4746` - Either multiple values or occurrences
- **`is_multiple`** (fn) - `repos/clap/clap_builder/src/builder/arg_group.rs:249` - Return true if the group allows more than one of the arguments
- **`is_next_line_help_set`** (fn) - `repos/clap/clap_builder/src/builder/arg.rs:4493` - Report whether [`Arg::next_line_help`] is set
- **`is_next_line_help_set`** (fn) - `repos/clap/clap_builder/src/builder/command.rs:4140` - Report whether [`Command::next_line_help`] is set
- **`is_no_binary_name_set`** (fn) - `repos/clap/clap_builder/src/builder/command.rs:4114` - Report whether [`Command::no_binary_name`] is set
- **`is_positional`** (fn) - `repos/clap/clap_builder/src/builder/arg.rs:4415` - Checks whether this argument is a positional or not.
- **`is_propagate_version_set`** (fn) - `repos/clap/clap_builder/src/builder/command.rs:4135` - Report whether [`Command::propagate_version`] is set
- **`is_require_equals_set`** (fn) - `repos/clap/clap_builder/src/builder/arg.rs:4535` - Report whether [`Arg::require_equals`] is set
- **`is_required_set`** (fn) - `repos/clap/clap_builder/src/builder/arg.rs:4432` - Reports whether [`Arg::required`] is set
- **`is_required_set`** (fn) - `repos/clap/clap_builder/src/builder/arg_group.rs:524` - Reports whether [`ArgGroup::required`] is set
- **`is_subcommand_negates_reqs_set`** (fn) - `repos/clap/clap_builder/src/builder/command.rs:4278` - Report whether [`Command::subcommand_negates_reqs`] is set
- **`is_subcommand_precedence_over_arg_set`** (fn) - `repos/clap/clap_builder/src/builder/command.rs:4273` - Report whether [`Command::subcommand_precedence_over_arg`] is set
- **`is_subcommand_required_set`** (fn) - `repos/clap/clap_builder/src/builder/command.rs:4233` - Report whether [`Command::subcommand_required`] is set
- **`is_trailing_var_arg_set`** (fn) - `repos/clap/clap_builder/src/builder/arg.rs:4545` - Report whether [`Arg::trailing_var_arg`] is set
- **`is_valid_subcommand`** (fn) - `repos/clap/clap_builder/src/parser/matches/arg_matches.rs:1059` - Check if a subcommand can be queried
- **`iter`** (fn) - `repos/clap/clap_complete/src/env/mod.rs:336` - Iterate over [`EnvCompleter`]s
- **`keys`** (fn) - `repos/clap/clap_builder/src/mkeymap.rs:111` - Return iterators of all keys.
- **`kind`** (fn) - `repos/clap/clap_builder/src/error/mod.rs:179` - Type of error for programmatic processing
- **`KindFormatter`** (struct) - `repos/clap/clap_builder/src/error/format.rs:25` - Report [`ErrorKind`]
- **`last`** (fn) - `repos/clap/clap_builder/src/builder/arg.rs:588` - This arg is the last, or final, positional argument (i.e. has the highest
- **`lib`** (module) - `repos/clap-cargo/src/lib.rs:1` - **clap-cargo**: Re-usable CLI flags for `cargo` plugins
- **`lib`** (module) - `repos/clap/clap_complete/src/lib.rs:8` - ## Quick Start
- **`lib`** (module) - `repos/clap/src/lib.rs:6` - > **Command Line Argument Parser for Rust**
- **`literal`** (fn) - `repos/clap/clap_builder/src/builder/styling.rs:96` - Literal command-line syntax, e.g. `--help`
- **`long`** (fn) - `repos/clap/clap_builder/src/builder/arg.rs:192` - Sets the long version of the argument without the preceding `--`.
- **`long`** (fn) - `repos/clap/clap_builder/src/output/help_template.rs:549` - Writes argument's long command to the wrapped stream.
- **`long_about`** (fn) - `repos/clap/clap_builder/src/builder/command.rs:1973` - Sets the program's description for the long help (`--help`).
- **`long_flag`** (fn) - `repos/clap/clap_builder/src/builder/command.rs:2610` - Sets the long version of the subcommand flag without the preceding `--`.
- **`long_flag_alias`** (fn) - `repos/clap/clap_builder/src/builder/command.rs:2725` - Add an alias, which functions as a "hidden" long flag subcommand.
- **`long_flag_aliases`** (fn) - `repos/clap/clap_builder/src/builder/command.rs:2825` - Add aliases, which function as "hidden" long flag subcommands.
- **`long_flag_aliases_to`** (fn) - `repos/clap/clap_builder/src/builder/command.rs:4991` - Check if this subcommand can be referred to as `name`. In other words,
- **`long_help`** (fn) - `repos/clap/clap_builder/src/builder/arg.rs:2274` - Sets the description of the argument for long help (`--help`).
- **`long_version`** (fn) - `repos/clap/clap_builder/src/builder/command.rs:2121` - Sets the version for the long version (`--version`) and help messages.
- **`longs_and_visible_aliases`** (fn) - `repos/clap/clap_complete/src/aot/generator/utils.rs:93` - Gets all the long options, their visible aliases and flags of a [`clap::Command`].
- **`longs_and_visible_aliases`** (fn) - `repos/clap/clap_complete/src/engine/complete.rs:476` - Gets all the long options, their visible aliases and flags of a [`clap::Command`] with formatted ...
- **`manifest`** (module) - `repos/clap-cargo/src/manifest.rs:1` - Cargo flag for selecting the relevant crate.
- **`Manifest`** (struct) - `repos/clap-cargo/src/manifest.rs:5` - Cargo flag for selecting the relevant crate.
- **`map`** (fn) - `repos/clap/clap_builder/src/builder/value_parser.rs:773` - Adapt a `TypedValueParser` from one value to another
- **`MapValueParser`** (struct) - `repos/clap/clap_builder/src/builder/value_parser.rs:2010` - Adapt a `TypedValueParser` from one value to another
- **`matches`** (fn) - `repos/clap/clap_builder/src/builder/possible_value.rs:206` - Tests if the value is valid for this argument value
- **`MatchesError`** (enum) - `repos/clap/clap_builder/src/parser/error.rs:3` - Violation of [`ArgMatches`][crate::ArgMatches] assumptions
- **`max_term_width`** (fn) - `repos/clap/clap_builder/src/builder/command.rs:1407` - Limit the line length for wrapping help when using the current terminal's width.
- **`max_values`** (fn) - `repos/clap/clap_builder/src/builder/range.rs:74` - Most number of values the argument accepts
- **`metadata`** (fn) - `repos/clap-cargo/src/manifest.rs:18` - Create a `cargo_metadata::MetadataCommand`
- **`min_values`** (fn) - `repos/clap/clap_builder/src/builder/range.rs:69` - Fewest number of values the argument accepts
- **`mod`** (module) - `repos/clap/clap_builder/src/builder/mod.rs:1` - Define [`Command`] line [arguments][`Arg`]
- **`mod`** (module) - `repos/clap/clap_builder/src/error/mod.rs:1` - Error reporting
- **`mod`** (module) - `repos/clap/clap_builder/src/output/textwrap/mod.rs:1` - Fork of `textwrap` crate
- **`mod`** (module) - `repos/clap/clap_builder/src/parser/mod.rs:1` - [`Command`][crate::Command] line argument parser
- **`mod`** (module) - `repos/clap/clap_complete/src/aot/generator/mod.rs:1` - Shell completion machinery
- **`mod`** (module) - `repos/clap/clap_complete/src/aot/mod.rs:1` - Prebuilt completions
- **`mod`** (module) - `repos/clap/clap_complete/src/aot/shells/mod.rs:1` - Shell-specific generators
- **`mod`** (module) - `repos/clap/clap_complete/src/engine/mod.rs:1` - `clap`-native completion system
- **`mod`** (module) - `repos/clap/clap_complete/src/env/mod.rs:1` - [`COMPLETE=$SHELL <bin>`][CompleteEnv] completion integration
- **`mod`** (module) - `repos/clap/src/_cookbook/mod.rs:8` - # Documentation: Cookbook
- **`mod`** (module) - `repos/clap/src/_derive/mod.rs:1` - # Documentation: Derive Reference
- **`multicall`** (fn) - `repos/clap/clap_builder/src/builder/command.rs:3435` - Multiple-personality program dispatched on the binary name (`argv[0]`)
- **`multicall_busybox`** (module) - `repos/clap/src/_cookbook/multicall_busybox.rs:1` - # Example: busybox-like CLI (Builder API)
- **`multicall_hostname`** (module) - `repos/clap/src/_cookbook/multicall_hostname.rs:1` - # Example: hostname-like CLI (Builder API)
- **`multiple`** (fn) - `repos/clap/clap_builder/src/builder/arg_group.rs:195` - Allows more than one of the [`Arg`]s in this group to be used. (Default: `false`)
- **`mut_arg`** (fn) - `repos/clap/clap_builder/src/builder/command.rs:214` - Allows one to mutate an [`Arg`] after it's been added to a [`Command`].
- **`mut_args`** (fn) - `repos/clap/clap_builder/src/builder/command.rs:267` - # use clap::{Command, Arg, ArgAction};
- **`mut_args`** (fn) - `repos/clap/clap_builder/src/mkeymap.rs:126` - Mutate every argument.
- **`mut_group`** (fn) - `repos/clap/clap_builder/src/builder/command.rs:304` - Allows one to mutate an [`ArgGroup`] after it's been added to a [`Command`].
- **`mut_subcommand`** (fn) - `repos/clap/clap_builder/src/builder/command.rs:343` - Allows one to mutate a [`Command`] after it's been added as a subcommand.
- **`mut_subcommands`** (fn) - `repos/clap/clap_builder/src/builder/command.rs:398` - # use clap::{Command, Arg, ArgAction};
- **`name`** (fn) - `repos/clap/clap_builder/src/builder/command.rs:1850` - (Re)Sets the program's name.
- **`name`** (fn) - `repos/clap/clap_complete/src/env/mod.rs:350` - Canonical name for this shell
- **`names`** (fn) - `repos/clap/clap_complete/src/env/mod.rs:331` - Collect all [`EnvCompleter::name`]s
- **`new`** (fn) - `repos/clap/clap_builder/src/builder/arg.rs:96` - Create a new [`Arg`] with a unique name.
- **`new`** (fn) - `repos/clap/clap_builder/src/builder/arg_group.rs:79` - Create a `ArgGroup` using a unique name.
- **`new`** (fn) - `repos/clap/clap_builder/src/builder/command.rs:117` - Creates a new instance of an `Command`.
- **`new`** (fn) - `repos/clap/clap_builder/src/builder/possible_value.rs:48` - Create a [`PossibleValue`] with its name.
- **`new`** (fn) - `repos/clap/clap_builder/src/builder/range.rs:32` - Create a range
- **`new`** (fn) - `repos/clap/clap_builder/src/builder/styled_str.rs:28` - Create an empty buffer
- **`new`** (fn) - `repos/clap/clap_builder/src/builder/value_parser.rs:78` - Custom parser for argument values
- **`new`** (fn) - `repos/clap/clap_builder/src/builder/value_parser.rs:908` - Implementation for [`ValueParser::string`]
- **`new`** (fn) - `repos/clap/clap_builder/src/builder/value_parser.rs:956` - Implementation for [`ValueParser::os_string`]
- **`new`** (fn) - `repos/clap/clap_builder/src/builder/value_parser.rs:998` - Implementation for [`ValueParser::path_buf`]
- **`new`** (fn) - `repos/clap/clap_builder/src/builder/value_parser.rs:1084` - Parse an [`ValueEnum`][crate::ValueEnum]
- **`new`** (fn) - `repos/clap/clap_builder/src/builder/value_parser.rs:1199` - Verify the value is from an enumerated set of [`PossibleValue`][crate::builder::PossibleValue].
- **`new`** (fn) - `repos/clap/clap_builder/src/builder/value_parser.rs:1321` - Select full range of `i64`
- **`new`** (fn) - `repos/clap/clap_builder/src/builder/value_parser.rs:1520` - Select full range of `u64`
- **`new`** (fn) - `repos/clap/clap_builder/src/builder/value_parser.rs:1680` - Implementation for [`ValueParser::bool`]
- **`new`** (fn) - `repos/clap/clap_builder/src/builder/value_parser.rs:1781` - Parse false-like string values, everything else is `true`
- **`new`** (fn) - `repos/clap/clap_builder/src/builder/value_parser.rs:1880` - Parse bool-like string values
- **`new`** (fn) - `repos/clap/clap_builder/src/builder/value_parser.rs:1971` - Parse non-empty string values
- **`new`** (fn) - `repos/clap/clap_builder/src/error/mod.rs:103` - Create an error with a pre-defined message
- **`new`** (fn) - `repos/clap/clap_builder/src/output/help_template.rs:31` - Create a new `HelpTemplate` instance.
- **`new`** (fn) - `repos/clap/clap_builder/src/output/help_template.rs:94` - Create a new `HelpTemplate` instance.
- **`new`** (fn) - `repos/clap/clap_complete/src/engine/candidate.rs:18` - Create a new completion candidate
- **`new`** (fn) - `repos/clap/clap_complete/src/engine/custom.rs:47` - Create a new `ArgValueCompleter` with a custom completer
- **`new`** (fn) - `repos/clap/clap_complete/src/engine/custom.rs:111` - Create a new `ArgValueCandidates` with a custom completer
- **`new`** (fn) - `repos/clap/clap_complete/src/engine/custom.rs:155` - Create a new `SubcommandCandidates` with a custom completer
- **`new_inner`** (fn) - `repos/clap/clap_builder/src/builder/command.rs:134` - The actual implementation of `new`, non-generic to save code size.
- **`next_display_order`** (fn) - `repos/clap/clap_builder/src/builder/command.rs:2378` - Change the starting value for assigning future display orders for args.
- **`next_help_heading`** (fn) - `repos/clap/clap_builder/src/builder/command.rs:2360` - Set the default section heading for future args.
- **`next_line_help`** (fn) - `repos/clap/clap_builder/src/builder/arg.rs:2424` - Render the [help][Arg::help] on the line after the argument.
- **`next_line_help`** (fn) - `repos/clap/clap_builder/src/builder/command.rs:1532` - Places the help string for all arguments and subcommands on the line after them.
- **`no_binary_name`** (fn) - `repos/clap/clap_builder/src/builder/command.rs:1166` - Specifies that the parser should not assume the first argument passed is the binary name.
- **`NonEmptyStringValueParser`** (struct) - `repos/clap/clap_builder/src/builder/value_parser.rs:1932` - Parse non-empty string values
- **`num_args`** (fn) - `repos/clap/clap_builder/src/builder/arg.rs:1053` - Specifies the number of arguments parsed per occurrence
- **`os_string`** (fn) - `repos/clap/clap_builder/src/builder/value_parser.rs:172` - [`OsString`][std::ffi::OsString] parser for argument values
- **`OsStr`** (struct) - `repos/clap/clap_builder/src/builder/os_str.rs:5` - A UTF-8-encoded fixed string
- **`OsStringValueParser`** (struct) - `repos/clap/clap_builder/src/builder/value_parser.rs:948` - Implementation for [`ValueParser::os_string`]
- **`override_help`** (fn) - `repos/clap/clap_builder/src/builder/command.rs:2204` - Overrides the `clap` generated help message (both `-h` and `--help`).
- **`override_usage`** (fn) - `repos/clap/clap_builder/src/builder/command.rs:2153` - Overrides the `clap` generated usage string for help and error messages.
- **`overrides_with`** (fn) - `repos/clap/clap_builder/src/builder/arg.rs:4071` - Sets an overridable argument.
- **`overrides_with_all`** (fn) - `repos/clap/clap_builder/src/builder/arg.rs:4120` - Sets multiple mutually overridable arguments by name.
- **`pacman`** (module) - `repos/clap/src/_cookbook/pacman.rs:1` - # Example: pacman-like CLI (Builder API)
- **`parse`** (fn) - `repos/clap/clap_builder/src/builder/value_parser.rs:738` - Parse the argument value
- **`parse`** (fn) - `repos/clap/clap_builder/src/derive.rs:30` - Parse from `std::env::args_os()`, [exit][Error::exit] on error.
- **`parse_`** (fn) - `repos/clap/clap_builder/src/builder/value_parser.rs:750` - Parse the argument value
- **`parse_from`** (fn) - `repos/clap/clap_builder/src/derive.rs:51` - Parse from iterator, [exit][Error::exit] on error.
- **`parse_opt_value`** (fn) - `repos/clap/clap_complete/src/engine/complete.rs:683` - Parse optional flag argument. Return new state
- **`parse_positional`** (fn) - `repos/clap/clap_complete/src/engine/complete.rs:632` - Parse the positional arguments. Return the new state and the new positional index.
- **`parse_ref`** (fn) - `repos/clap/clap_builder/src/builder/value_parser.rs:232` - Parse into a `AnyValue`
- **`parse_ref`** (fn) - `repos/clap/clap_builder/src/builder/value_parser.rs:715` - Parse the argument value
- **`parse_ref_`** (fn) - `repos/clap/clap_builder/src/builder/value_parser.rs:725` - Parse the argument value
- **`parse_shortflags`** (fn) - `repos/clap/clap_complete/src/engine/complete.rs:593` - Parse the short flags and find the first `takes_values` option.
- **`Parser`** (type) - `repos/clap/clap_builder/src/builder/value_parser.rs:2277` - Generated parser, usually [`ValueParser`].
- **`Parser`** (trait) - `repos/clap/clap_builder/src/derive.rs:10` - Parse command-line arguments into `Self`.
- **`parser`** (fn) - `repos/clap/clap_derive/src/lib.rs:48` - Generates the `Parser` implementation.
- **`ParseResult`** (enum) - `repos/clap/clap_builder/src/parser/parser.rs:1635` - Recoverable Parsing results.
- **`partition_packages`** (fn) - `repos/clap-cargo/src/workspace.rs:25` - Partition workspace members into those selected and those excluded.
- **`path_buf`** (fn) - `repos/clap/clap_builder/src/builder/value_parser.rs:204` - [`PathBuf`][std::path::PathBuf] parser for argument values
- **`PathBufValueParser`** (struct) - `repos/clap/clap_builder/src/builder/value_parser.rs:990` - Implementation for [`ValueParser::path_buf`]
- **`PathCompleter`** (struct) - `repos/clap/clap_complete/src/engine/custom.rs:200` - Complete a value as a [`std::path::Path`]
- **`placeholder`** (fn) - `repos/clap/clap_builder/src/builder/styling.rs:103` - Descriptions within command-line syntax, e.g. [`value_name`][crate::Arg::value_name]
- **`plain`** (fn) - `repos/clap/clap_builder/src/builder/styling.rs:36` - No terminal styling
- **`possible_values`** (fn) - `repos/clap/clap_builder/src/builder/value_parser.rs:250` - Reflect on enumerated value properties
- **`possible_values`** (fn) - `repos/clap/clap_builder/src/builder/value_parser.rs:763` - Reflect on enumerated value properties
- **`possible_values`** (fn) - `repos/clap/clap_builder/src/util/color.rs:61` - Report all `possible_values`
- **`possible_values`** (fn) - `repos/clap/clap_complete/src/aot/generator/utils.rs:133` - Get the possible values for completion
- **`possible_values`** (fn) - `repos/clap/clap_complete/src/engine/complete.rs:544` - Get the possible values for completion
- **`PossibleValue`** (struct) - `repos/clap/clap_builder/src/builder/possible_value.rs:6` - A possible value of an argument.
- **`PossibleValue`** (impl) - `repos/clap/clap_builder/src/builder/possible_value.rs:159` - Reflection
- **`PossibleValuesParser`** (struct) - `repos/clap/clap_builder/src/builder/value_parser.rs:1156` - Verify the value is from an enumerated set of [`PossibleValue`][crate::builder::PossibleValue].
- **`PowerShell`** (struct) - `repos/clap/clap_complete/src/aot/shells/powershell.rs:9` - Generate powershell completion file
- **`Powershell`** (struct) - `repos/clap/clap_complete/src/env/shells.rs:255` - Powershell completion adapter
- **`print`** (fn) - `repos/clap/clap_builder/src/error/mod.rs:251` - Prints formatted and colored error to `stdout` or `stderr` according to its error kind
- **`print_help`** (fn) - `repos/clap/clap_builder/src/builder/command.rs:912` - Prints the short help message (`-h`) to [`io::stdout()`].
- **`print_long_help`** (fn) - `repos/clap/clap_builder/src/builder/command.rs:943` - Prints the long help message (`--help`) to [`io::stdout()`].
- **`process_author_str`** (fn) - `repos/clap/clap_derive/src/item.rs:1351` - replace all `:` with `, ` when not inside the `<>`
- **`propagate_version`** (fn) - `repos/clap/clap_builder/src/builder/command.rs:1498` - Specifies to use the version of the current command for all [`subcommands`].
- **`push`** (fn) - `repos/clap/clap_builder/src/mkeymap.rs:93` - Push an argument in the map.
- **`push_str`** (fn) - `repos/clap/clap_builder/src/builder/styled_str.rs:45` - Appends a given string slice onto the end of this `StyledStr`.
- **`push_string`** (fn) - `repos/clap/clap_builder/src/builder/styled_str.rs:39` - May allow the compiler to consolidate the `Drop`s for `msg`, reducing code size compared to
- **`range`** (fn) - `repos/clap/clap_builder/src/builder/value_parser.rs:1326` - Narrow the supported range
- **`range`** (fn) - `repos/clap/clap_builder/src/builder/value_parser.rs:1525` - Narrow the supported range
- **`RangedI64ValueParser`** (struct) - `repos/clap/clap_builder/src/builder/value_parser.rs:1268` - Parse number that fall within a range of values
- **`RangedU64ValueParser`** (struct) - `repos/clap/clap_builder/src/builder/value_parser.rs:1475` - Parse number that fall within a range of values
- **`raw`** (fn) - `repos/clap/clap_builder/src/builder/arg.rs:1750` - Consume all following arguments.
- **`raw`** (fn) - `repos/clap/clap_builder/src/error/mod.rs:80` - Create an unformatted error
- **`RawValues`** (struct) - `repos/clap/clap_builder/src/parser/matches/arg_matches.rs:1542` - Iterate over raw argument values via [`ArgMatches::get_raw`].
- **`remove`** (fn) - `repos/clap/clap_builder/src/builder/arg.rs:4566` - Remove an [`ArgExt`]
- **`remove`** (fn) - `repos/clap/clap_builder/src/builder/command.rs:4294` - Remove an [`CommandExt`]
- **`remove`** (fn) - `repos/clap/clap_builder/src/error/mod.rs:206` - Remove a piece of context, return the old value if any
- **`remove_by_name`** (fn) - `repos/clap/clap_builder/src/mkeymap.rs:145` - Remove an arg in the graph by Id, usually used by `mut_arg`. Return
- **`remove_many`** (fn) - `repos/clap/clap_builder/src/parser/matches/arg_matches.rs:414` - Return values of a specific option or positional argument.
- **`remove_occurrences`** (fn) - `repos/clap/clap_builder/src/parser/matches/arg_matches.rs:453` - Return values for each occurrence of an option.
- **`remove_one`** (fn) - `repos/clap/clap_builder/src/parser/matches/arg_matches.rs:371` - Returns the value of a specific option or positional argument.
- **`remove_subcommand`** (fn) - `repos/clap/clap_builder/src/parser/matches/arg_matches.rs:926` - Return the name and `ArgMatches` of the current [subcommand].
- **`render`** (fn) - `repos/clap/clap_builder/src/error/mod.rs:282` - Render the error message to a [`StyledStr`].
- **`render_arg_val`** (fn) - `repos/clap/clap_builder/src/builder/arg.rs:4703` - Write the values such as `<name1> <name2>`
- **`render_help`** (fn) - `repos/clap/clap_builder/src/builder/command.rs:977` - Render the short help message (`-h`) to a [`StyledStr`]
- **`render_long_help`** (fn) - `repos/clap/clap_builder/src/builder/command.rs:1010` - Render the long help message (`--help`) to a [`StyledStr`].
- **`render_long_version`** (fn) - `repos/clap/clap_builder/src/builder/command.rs:1098` - Version message rendered as if the user ran `--version`.
- **`render_usage`** (fn) - `repos/clap/clap_builder/src/builder/command.rs:1123` - Usage statement
- **`render_version`** (fn) - `repos/clap/clap_builder/src/builder/command.rs:1073` - Version message rendered as if the user ran `-V`.
- **`repl`** (module) - `repos/clap/src/_cookbook/repl.rs:1` - # Example: Command REPL (Builder API)
- **`repl_derive`** (module) - `repos/clap/src/_cookbook/repl_derive.rs:1` - # Example: REPL (Derive API)
- **`require_equals`** (fn) - `repos/clap/clap_builder/src/builder/arg.rs:1583` - Requires that options use the `--option=val` syntax
- **`required`** (fn) - `repos/clap/clap_builder/src/builder/arg.rs:697` - Specifies that the argument must be present.
- **`required`** (fn) - `repos/clap/clap_builder/src/builder/arg_group.rs:267` - Require an argument from the group to be present when parsing.
- **`required_if_eq`** (fn) - `repos/clap/clap_builder/src/builder/arg.rs:3516` - This argument is [required] only if the specified `arg` is present at runtime and its value
- **`required_if_eq_all`** (fn) - `repos/clap/clap_builder/src/builder/arg.rs:3689` - Specify this argument is [required] based on multiple conditions.
- **`required_if_eq_any`** (fn) - `repos/clap/clap_builder/src/builder/arg.rs:3603` - Specify this argument is [required] based on multiple conditions.
- **`required_unless_present`** (fn) - `repos/clap/clap_builder/src/builder/arg.rs:3278` - Set this arg as [required] as long as the specified argument is not present at runtime.
- **`required_unless_present_all`** (fn) - `repos/clap/clap_builder/src/builder/arg.rs:3348` - Sets this arg as [required] unless *all* of the specified arguments are present at runtime.
- **`required_unless_present_any`** (fn) - `repos/clap/clap_builder/src/builder/arg.rs:3431` - Sets this arg as [required] unless *any* of the specified arguments are present at runtime.
- **`requires`** (fn) - `repos/clap/clap_builder/src/builder/arg.rs:763` - Sets an argument that is required when this one is present
- **`requires`** (fn) - `repos/clap/clap_builder/src/builder/arg_group.rs:320` - Specify an argument or group that must be present when this group is.
- **`requires_all`** (fn) - `repos/clap/clap_builder/src/builder/arg_group.rs:369` - Specify arguments or groups that must be present when this group is.
- **`requires_if`** (fn) - `repos/clap/clap_builder/src/builder/arg.rs:3773` - Require another argument if this arg matches the [`ArgPredicate`]
- **`requires_ifs`** (fn) - `repos/clap/clap_builder/src/builder/arg.rs:3837` - Allows multiple conditional requirements.
- **`Resettable`** (enum) - `repos/clap/clap_builder/src/builder/resettable.rs:12` - Clearable builder value
- **`Result`** (type) - `repos/clap/clap_builder/src/error/mod.rs:50` - Short hand for [`Result`] type
- **`RichFormatter`** (struct) - `repos/clap/clap_builder/src/error/format.rs:57` - Richly formatted error context
- **`set_bin_name`** (fn) - `repos/clap/clap_builder/src/builder/command.rs:3746` - Set binary name. Uses `&mut self` instead of `self`.
- **`Shell`** (enum) - `repos/clap/clap_complete/src/aot/shells/shell.rs:12` - Shell with auto-generated completion script available.
- **`shells`** (fn) - `repos/clap/clap_complete/src/env/mod.rs:181` - Override the shells supported for completions
- **`Shells`** (struct) - `repos/clap/clap_complete/src/env/mod.rs:317` - Collection of shell-specific completers
- **`short`** (fn) - `repos/clap/clap_builder/src/builder/arg.rs:135` - Sets the short version of the argument without the preceding `-`.
- **`short`** (fn) - `repos/clap/clap_builder/src/output/help_template.rs:536` - Writes argument's short command to the wrapped stream.
- **`short_alias`** (fn) - `repos/clap/clap_builder/src/builder/arg.rs:263` - Add an alias, which functions as a hidden short flag.
- **`short_aliases`** (fn) - `repos/clap/clap_builder/src/builder/arg.rs:323` - Add aliases, which functions as a hidden short flag.
- **`short_flag`** (fn) - `repos/clap/clap_builder/src/builder/command.rs:2578` - Sets the short version of the subcommand flag without the preceding `-`.
- **`short_flag_alias`** (fn) - `repos/clap/clap_builder/src/builder/command.rs:2697` - Add an alias, which functions as  "hidden" short flag subcommand
- **`short_flag_aliases`** (fn) - `repos/clap/clap_builder/src/builder/command.rs:2796` - Add aliases, which function as "hidden" short flag subcommands.
- **`short_flag_aliases_to`** (fn) - `repos/clap/clap_builder/src/builder/command.rs:4983` - Check if this subcommand can be referred to as `name`. In other words,
- **`shorts_and_visible_aliases`** (fn) - `repos/clap/clap_complete/src/aot/generator/utils.rs:68` - Gets all the short options, their visible aliases and flags of a [`clap::Command`].
- **`shorts_and_visible_aliases`** (fn) - `repos/clap/clap_complete/src/engine/complete.rs:509` - Gets all the short options, their visible aliases and flags of a [`clap::Command`].
- **`should_show_help`** (fn) - `repos/clap/clap_builder/src/builder/possible_value.rs:179` - Report if `PossibleValue` is not hidden and has a help message
- **`SINGLE`** (const) - `repos/clap/clap_builder/src/builder/range.rs:15` - A single argument value, the most common case for options
- **`singular_or_plural`** (fn) - `repos/clap/clap_builder/src/error/format.rs:414` - Returns the singular or plural form on the verb to be based on the argument's value.
- **`Sp`** (struct) - `repos/clap/clap_derive/src/utils/spanned.rs:7` - An entity with a span attached.
- **`stdio`** (fn) - `repos/clap/clap_complete/src/engine/custom.rs:241` - Include stdio (`-`)
- **`Str`** (struct) - `repos/clap/clap_builder/src/builder/str.rs:4` - A UTF-8-encoded fixed string
- **`str_to_bool`** (fn) - `repos/clap/clap_builder/src/util/str_to_bool.rs:7` - Converts a string literal representation of truth to true or false.
- **`string`** (fn) - `repos/clap/clap_builder/src/builder/value_parser.rs:147` - [`String`] parser for argument values
- **`StringValueParser`** (struct) - `repos/clap/clap_builder/src/builder/value_parser.rs:900` - Implementation for [`ValueParser::string`]
- **`styled`** (fn) - `repos/clap/clap_builder/src/builder/styling.rs:51` - Default terminal styling
- **`StyledStr`** (struct) - `repos/clap/clap_builder/src/builder/styled_str.rs:4` - Terminal-styling container
- **`styles`** (fn) - `repos/clap/clap_builder/src/builder/command.rs:1332` - Sets the [`Styles`] for terminal output
- **`Styles`** (struct) - `repos/clap/clap_builder/src/builder/styling.rs:5` - Terminal styling definitions
- **`Styles`** (impl) - `repos/clap/clap_builder/src/builder/styling.rs:143` - Reflection
- **`styling`** (module) - `repos/clap/clap_builder/src/builder/styling.rs:1` - Terminal [`Styles`] for help and error output
- **`subcmd`** (fn) - `repos/clap/clap_builder/src/output/help_template.rs:1070` - Writes subcommand to the wrapped stream.
- **`subcommand`** (fn) - `repos/clap/clap_builder/src/builder/command.rs:504` - Adds a subcommand to the list of valid possibilities.
- **`Subcommand`** (trait) - `repos/clap/clap_builder/src/derive.rs:248` - Parse a sub-command into a user-defined enum.
- **`subcommand`** (fn) - `repos/clap/clap_builder/src/parser/matches/arg_matches.rs:867` - The name and `ArgMatches` of the current [subcommand].
- **`subcommand`** (fn) - `repos/clap/clap_derive/src/lib.rs:85` - Generates the `Subcommand` impl.
- **`subcommand_help_heading`** (fn) - `repos/clap/clap_builder/src/builder/command.rs:3639` - Sets the help heading used for subcommands when printing usage and help.
- **`subcommand_matches`** (fn) - `repos/clap/clap_builder/src/parser/matches/arg_matches.rs:986` - The `ArgMatches` for the current [subcommand].
- **`subcommand_name`** (fn) - `repos/clap/clap_builder/src/parser/matches/arg_matches.rs:1030` - The name of the current [subcommand].
- **`subcommand_negates_reqs`** (fn) - `repos/clap/clap_builder/src/builder/command.rs:3376` - Allows [`subcommands`] to override all requirements of the parent command.
- **`subcommand_precedence_over_arg`** (fn) - `repos/clap/clap_builder/src/builder/command.rs:3316` - Prevent subcommands from being consumed as an arguments value.
- **`subcommand_required`** (fn) - `repos/clap/clap_builder/src/builder/command.rs:3131` - If no [`subcommand`] is present at runtime, error and exit gracefully.
- **`subcommand_value_name`** (fn) - `repos/clap/clap_builder/src/builder/command.rs:3573` - Sets the value name used for subcommands when printing usage and help.
- **`SubcommandCandidates`** (struct) - `repos/clap/clap_complete/src/engine/custom.rs:135` - Extend [`Command`][clap::Command] with a [`ValueCandidates`]
- **`subcommands`** (fn) - `repos/clap/clap_builder/src/builder/command.rs:542` - Adds multiple subcommands to the list of valid possibilities.
- **`subcommands`** (fn) - `repos/clap/clap_complete/src/aot/generator/utils.rs:36` - Gets subcommands of [`clap::Command`] in the form of `("name", "bin_name")`.
- **`subcommands`** (fn) - `repos/clap/clap_complete/src/engine/complete.rs:555` - Gets subcommands of [`clap::Command`] in the form of `("name", "bin_name")`.
- **`suggest`** (fn) - `repos/clap/clap_builder/src/builder/value_parser.rs:2173` - Provide a general suggestion
- **`suggest_arg`** (fn) - `repos/clap/clap_builder/src/builder/value_parser.rs:2165` - Suggest an alternative argument
- **`tag`** (fn) - `repos/clap/clap_complete/src/engine/candidate.rs:41` - Group candidates by tag
- **`takes_values`** (fn) - `repos/clap/clap_builder/src/builder/action.rs:356` - Returns whether this action accepts values on the command-line
- **`takes_values`** (fn) - `repos/clap/clap_builder/src/builder/range.rs:79` - Report whether the argument takes any values (ie is a flag)
- **`term_width`** (fn) - `repos/clap/clap_builder/src/builder/command.rs:1368` - Sets the terminal width at which to wrap help messages.
- **`to_os_string`** (fn) - `repos/clap/clap_builder/src/builder/os_str.rs:44` - Get the raw string as an `OsString`
- **`to_possible_value`** (fn) - `repos/clap/clap_builder/src/derive.rs:310` - The canonical argument value.
- **`trailing_var_arg`** (fn) - `repos/clap/clap_builder/src/builder/arg.rs:544` - This is a "var arg" and everything that follows should be captured by it, as if the user had
- **`TRUE_LITERALS`** (const) - `repos/clap/clap_builder/src/util/str_to_bool.rs:1` - True values are `y`, `yes`, `t`, `true`, `on`, and `1`.
- **`try_clear_id`** (fn) - `repos/clap/clap_builder/src/parser/matches/arg_matches.rs:1227` - Clears the values for the given `id`
- **`try_complete`** (fn) - `repos/clap/clap_complete/src/env/mod.rs:204` - Process the completion request
- **`try_contains_id`** (fn) - `repos/clap/clap_builder/src/parser/matches/arg_matches.rs:1219` - Non-panicking version of [`ArgMatches::contains_id`]
- **`try_generate`** (fn) - `repos/clap/clap_complete/src/aot/generator/mod.rs:72` - Fallible version to generate output out of [`clap::Command`].
- **`try_get_many`** (fn) - `repos/clap/clap_builder/src/parser/matches/arg_matches.rs:1098` - Non-panicking version of [`ArgMatches::get_many`]
- **`try_get_matches`** (fn) - `repos/clap/clap_builder/src/builder/command.rs:693` - Parse [`env::args_os`], returning a [`clap::Result`] on failure.
- **`try_get_matches_from`** (fn) - `repos/clap/clap_builder/src/builder/command.rs:770` - Parse the specified arguments, returning a [`clap::Result`] on failure.
- **`try_get_matches_from_mut`** (fn) - `repos/clap/clap_builder/src/builder/command.rs:822` - Parse the specified arguments, returning a [`clap::Result`] on failure.
- **`try_get_occurrences`** (fn) - `repos/clap/clap_builder/src/parser/matches/arg_matches.rs:1117` - Non-panicking version of [`ArgMatches::get_occurrences`]
- **`try_get_one`** (fn) - `repos/clap/clap_builder/src/parser/matches/arg_matches.rs:1080` - Non-panicking version of [`ArgMatches::get_one`]
- **`try_get_raw`** (fn) - `repos/clap/clap_builder/src/parser/matches/arg_matches.rs:1134` - Non-panicking version of [`ArgMatches::get_raw`]
- **`try_get_raw_occurrences`** (fn) - `repos/clap/clap_builder/src/parser/matches/arg_matches.rs:1149` - Non-panicking version of [`ArgMatches::get_raw_occurrences`]
- **`try_map`** (fn) - `repos/clap/clap_builder/src/builder/value_parser.rs:818` - Adapt a `TypedValueParser` from one value to another
- **`try_parse`** (fn) - `repos/clap/clap_builder/src/derive.rs:45` - Parse from `std::env::args_os()`, return Err on error.
- **`try_parse_from`** (fn) - `repos/clap/clap_builder/src/derive.rs:70` - Parse from iterator, return Err on error.
- **`try_remove_many`** (fn) - `repos/clap/clap_builder/src/parser/matches/arg_matches.rs:1182` - Non-panicking version of [`ArgMatches::remove_many`]
- **`try_remove_occurrences`** (fn) - `repos/clap/clap_builder/src/parser/matches/arg_matches.rs:1201` - Non-panicking version of [`ArgMatches::remove_occurrences`]
- **`try_remove_one`** (fn) - `repos/clap/clap_builder/src/parser/matches/arg_matches.rs:1167` - Non-panicking version of [`ArgMatches::remove_one`]
- **`try_update_from`** (fn) - `repos/clap/clap_builder/src/derive.rs:100` - Update from iterator, return Err on error.
- **`TryMapValueParser`** (struct) - `repos/clap/clap_builder/src/builder/value_parser.rs:2069` - Adapt a `TypedValueParser` from one value to another
- **`two_args_of`** (fn) - `repos/clap/clap_builder/src/builder/command.rs:4710` - Returns the first two arguments that match the condition.
- **`two_elements_of`** (fn) - `repos/clap/clap_builder/src/builder/command.rs:5270` - Returns the first two elements of an iterator as an `Option<(T, T)>`.
- **`two_groups_of`** (fn) - `repos/clap/clap_builder/src/builder/command.rs:4721` - Returns the first two groups that match the condition.
- **`ty`** (module) - `repos/clap/clap_derive/src/utils/ty.rs:1` - Special types handling
- **`type_id`** (fn) - `repos/clap/clap_builder/src/builder/value_parser.rs:245` - Describes the content of `AnyValue`
- **`type_id`** (fn) - `repos/clap/clap_builder/src/builder/value_parser.rs:609` - Describes the content of `AnyValue`
- **`typed_derive`** (module) - `repos/clap/src/_cookbook/typed_derive.rs:1` - # Example: Custom Types (Derive API)
- **`TypedValueParser`** (trait) - `repos/clap/clap_builder/src/builder/value_parser.rs:660` - Parse/validate argument values
- **`UnknownArgumentValueParser`** (struct) - `repos/clap/clap_builder/src/builder/value_parser.rs:2125` - When encountered, report [`ErrorKind::UnknownArgument`][crate::error::ErrorKind::UnknownArgument]
- **`update_from`** (fn) - `repos/clap/clap_builder/src/derive.rs:80` - Update from iterator, [exit][Error::exit] on error.
- **`update_from_arg_matches`** (fn) - `repos/clap/clap_builder/src/derive.rs:205` - Assign values from `ArgMatches` to `self`.
- **`update_from_arg_matches_mut`** (fn) - `repos/clap/clap_builder/src/derive.rs:208` - Assign values from `ArgMatches` to `self`.
- **`usage`** (fn) - `repos/clap/clap_builder/src/builder/styling.rs:89` - Usage heading
- **`use_stderr`** (fn) - `repos/clap/clap_builder/src/error/mod.rs:216` - Should the message be written to `stdout` or not?
- **`utils`** (module) - `repos/clap/clap_complete/src/aot/generator/utils.rs:1` - Helpers for writing generators
- **`valid`** (fn) - `repos/clap/clap_builder/src/builder/styling.rs:110` - Highlight suggested usage
- **`Value`** (type) - `repos/clap/clap_builder/src/builder/value_parser.rs:712` - Argument's value type
- **`value_delimiter`** (fn) - `repos/clap/clap_builder/src/builder/arg.rs:1655` - Allow grouping of multiple values via a delimiter.
- **`value_enum`** (fn) - `repos/clap/clap_derive/src/lib.rs:36` - Generates the `ValueEnum` impl.
- **`value_hint`** (fn) - `repos/clap/clap_builder/src/builder/arg.rs:1356` - Provide the shell a hint about how to complete this argument.
- **`value_name`** (fn) - `repos/clap/clap_builder/src/builder/arg.rs:1223` - Placeholder for the argument's value in the help message / usage.
- **`value_names`** (fn) - `repos/clap/clap_builder/src/builder/arg.rs:1286` - Placeholders for the argument's values in the help message / usage.
- **`value_parser`** (fn) - `repos/clap/clap_builder/src/builder/arg.rs:991` - Specify the typed behavior of the argument.
- **`value_parser`** (fn) - `repos/clap/clap_builder/src/builder/value_parser.rs:2283` - Create the specified [`Self::Parser`]
- **`value_source`** (fn) - `repos/clap/clap_builder/src/parser/matches/arg_matches.rs:584` - Report where argument value came from
- **`value_terminator`** (fn) - `repos/clap/clap_builder/src/builder/arg.rs:1687` - Sentinel to **stop** parsing multiple values of a given argument.
- **`value_variants`** (fn) - `repos/clap/clap_builder/src/derive.rs:294` - All possible argument values, in display order.
- **`ValueCandidates`** (trait) - `repos/clap/clap_complete/src/engine/custom.rs:179` - User-provided completion candidates for an [`Arg`][clap::Arg], see [`ArgValueCandidates`]
- **`ValueCompleter`** (trait) - `repos/clap/clap_complete/src/engine/custom.rs:71` - User-provided completion candidates for an [`Arg`][clap::Arg], see [`ArgValueCompleter`]
- **`ValueEnum`** (trait) - `repos/clap/clap_builder/src/derive.rs:281` - Parse arguments into enums.
- **`ValueHint`** (enum) - `repos/clap/clap_builder/src/builder/value_hint.rs:3` - Provide shell with hint on how to complete an argument.
- **`ValueParser`** (struct) - `repos/clap/clap_builder/src/builder/value_parser.rs:10` - Parse/validate argument values
- **`ValueParserFactory`** (trait) - `repos/clap/clap_builder/src/builder/value_parser.rs:2241` - Register a type with [`value_parser!`][crate::value_parser!]
- **`ValueRange`** (struct) - `repos/clap/clap_builder/src/builder/range.rs:1` - Values per occurrence for an argument
- **`Values`** (struct) - `repos/clap/clap_builder/src/parser/matches/arg_matches.rs:1407` - Iterate over multiple values for an argument via [`ArgMatches::remove_many`].
- **`ValueSource`** (enum) - `repos/clap/clap_builder/src/parser/matches/value_source.rs:1` - Origin of the argument's value
- **`ValuesRef`** (struct) - `repos/clap/clap_builder/src/parser/matches/arg_matches.rs:1474` - Iterate over multiple values for an argument via [`ArgMatches::get_many`].
- **`var`** (fn) - `repos/clap/clap_complete/src/env/mod.rs:159` - Override the environment variable used for enabling completions
- **`version`** (fn) - `repos/clap/clap_builder/src/builder/command.rs:2094` - Sets the version for the short version (`-V`) and help messages.
- **`visible_alias`** (fn) - `repos/clap/clap_builder/src/builder/arg.rs:354` - Add an alias, which functions as a visible long flag.
- **`visible_alias`** (fn) - `repos/clap/clap_builder/src/builder/command.rs:2853` - Sets a visible alias to this subcommand.
- **`visible_aliases`** (fn) - `repos/clap/clap_builder/src/builder/arg.rs:414` - Add aliases, which function as visible long flags.
- **`visible_aliases`** (fn) - `repos/clap/clap_builder/src/builder/command.rs:2960` - Sets multiple visible aliases to this subcommand.
- **`visible_long_flag_alias`** (fn) - `repos/clap/clap_builder/src/builder/command.rs:2930` - Add an alias, which functions as a "visible" long flag subcommand.
- **`visible_long_flag_aliases`** (fn) - `repos/clap/clap_builder/src/builder/command.rs:3028` - Add aliases, which function as *visible* long flag subcommands.
- **`visible_short_alias`** (fn) - `repos/clap/clap_builder/src/builder/arg.rs:384` - Add an alias, which functions as a visible short flag.
- **`visible_short_aliases`** (fn) - `repos/clap/clap_builder/src/builder/arg.rs:441` - Add aliases, which function as visible short flags.
- **`visible_short_flag_alias`** (fn) - `repos/clap/clap_builder/src/builder/command.rs:2899` - Add an alias, which functions as  "visible" short flag subcommand
- **`visible_short_flag_aliases`** (fn) - `repos/clap/clap_builder/src/builder/command.rs:3003` - Add aliases, which function as *visible* short flag subcommands.
- **`will_args_wrap`** (fn) - `repos/clap/clap_builder/src/output/help_template.rs:727` - Will use next line help on writing args.
- **`will_subcommands_wrap`** (fn) - `repos/clap/clap_builder/src/output/help_template.rs:977` - Will use next line help on writing subcommands.
- **`with_cmd`** (fn) - `repos/clap/clap_builder/src/error/mod.rs:146` - Apply [`Command`]'s formatting to the error
- **`with_factory`** (fn) - `repos/clap/clap_complete/src/env/mod.rs:111` - Complete a [`clap::Command`]
- **`workspace`** (module) - `repos/clap-cargo/src/workspace.rs:1` - Cargo flags for selecting crates in a workspace.
- **`Workspace`** (struct) - `repos/clap-cargo/src/workspace.rs:3` - Cargo flags for selecting crates in a workspace.
- **`wrap`** (fn) - `repos/clap/clap_builder/src/output/textwrap/mod.rs:33` - Compatibility shim to keep textwrap's tests
- **`write_all_args`** (fn) - `repos/clap/clap_builder/src/output/help_template.rs:371` - Writes help for all arguments (options, flags, args, subcommands)
- **`write_arg`** (fn) - `repos/clap/clap_builder/src/output/help_template.rs:512` - Writes help for an argument to the wrapped stream.
- **`write_args`** (fn) - `repos/clap/clap_builder/src/output/help_template.rs:468` - Sorts arguments by length and display order and write their help to the wrapped stream.
- **`write_bin_name`** (fn) - `repos/clap/clap_builder/src/output/help_template.rs:272` - Writes binary name of a Parser Object to the wrapped stream.
- **`write_complete`** (fn) - `repos/clap/clap_complete/src/env/mod.rs:387` - Complete the given command
- **`write_display_name`** (fn) - `repos/clap/clap_builder/src/output/help_template.rs:257` - Writes binary name of a Parser Object to the wrapped stream.
- **`write_flat_subcommands`** (fn) - `repos/clap/clap_builder/src/output/help_template.rs:878` - Writes help for subcommands of a Parser Object to the wrapped stream.
- **`write_help`** (fn) - `repos/clap/clap_builder/src/output/help.rs:8` - Writes the parser help to the wrapped stream.
- **`write_registration`** (fn) - `repos/clap/clap_complete/src/env/mod.rs:362` - Register for completions
- **`write_subcommands`** (fn) - `repos/clap/clap_builder/src/output/help_template.rs:939` - Writes help for subcommands of a Parser Object to the wrapped stream.
- **`write_templated_help`** (fn) - `repos/clap/clap_builder/src/output/help_template.rs:157` - Write help to stream for the parser in the format defined by the template.
- **`Zsh`** (struct) - `repos/clap/clap_complete/src/aot/shells/zsh.rs:8` - Generate zsh completion file
- **`Zsh`** (struct) - `repos/clap/clap_complete/src/env/shells.rs:347` - Zsh completion adapter