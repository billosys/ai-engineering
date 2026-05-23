---
concept: Init and User Flags
slug: init-flags
category: tooling
subcategory: runtime-configuration
tier: intermediate
source: "ERTS User's Guide"
source_slug: otp-erts
authors: "Ericsson AB"
chapter: "erl"
chapter_number: null
pdf_page: null
section: "Flags"
extraction_confidence: high
aliases:
  - "erl flags"
  - "init flags"
  - "user flags"
  - "erl dash flags"
prerequisites:
  - erl-command
extends:
  - erl-command
related:
  - emulator-flags
  - epmd
  - distribution-protocol
  - crash-dump
contrasts_with:
  - emulator-flags
answers_questions:
  - "What are the key '-' flags for the erl command?"
  - "How do I make an Erlang node distributed?"
  - "How do I specify a boot file or configuration file?"
  - "How do I run Erlang without a shell?"
---

# Quick Definition

Init and user flags are `erl` arguments prefixed with `-` that configure the Erlang runtime at the application level. Init flags are interpreted by the `init` process directly; user flags are stored by `init` and consumed by OTP applications like Kernel.

# Core Definition

The erl documentation explains: "Any argument starting with character `-` (hyphen) is interpreted as a flag, which is to be passed to the Erlang part of the runtime system, more specifically to the `init` system process. The `init` process itself interprets some of these flags, the _init flags_. It also stores any remaining flags, the _user flags_. The latter can be retrieved by calling `init:get_argument/1`."

**Key init flags** (interpreted directly by `init`):
- `-boot File` -- Specifies the boot file (default `$ROOT/bin/start.boot`)
- `-eval Expr` -- Makes `init` evaluate the expression `Expr`
- `-s Mod [Func [Arg1 ...]]` -- Makes `init` call the function (args as atoms)
- `-run Mod [Func [Arg1 ...]]` -- Makes `init` call the function (args as strings)
- `-S Mod [Func [Arg1 ...]]` -- Like `-run` but implies `-noshell`
- `-extra` -- Everything following is treated as plain arguments
- `--` -- Everything following up to the next flag is plain arguments

**Key user flags** (consumed by Kernel and other applications):
- `-name Name` -- Long-name distributed mode (Name@FullHost)
- `-sname Name` -- Short-name distributed mode (Name@ShortHost)
- `-setcookie Cookie` -- Sets the magic cookie for distribution
- `-config Config` -- Specifies application configuration files
- `-pa Dir1 Dir2 ...` -- Prepends directories to the code path
- `-pz Dir1 Dir2 ...` -- Appends directories to the code path
- `-heart` -- Starts heartbeat monitoring
- `-hidden` -- Starts as a hidden node
- `-detached` -- Starts detached from the console (implies `-noinput`)
- `-noshell` -- Starts with no shell (for pipeline use)
- `-noinput` -- Never reads input (implies `-noshell`)
- `-proto_dist Proto` -- Specifies distribution protocol (inet_tcp, inet_tls, inet6_tcp)
- `-remsh Node` -- Starts with a remote shell connected to Node

# Prerequisites

- **erl-command** -- Init/user flags are a category of erl arguments

# Key Properties

1. All flags start with `-`
2. Init flags are interpreted by the `init` process at startup
3. User flags are stored by `init` and retrieved via `init:get_argument/1`
4. `-name` and `-sname` are mutually exclusive; they cannot be mixed between nodes that communicate
5. `-name` uses fully qualified hostnames; `-sname` uses short hostnames
6. `-setcookie` sets the cookie for distribution authentication
7. `-noinput` implies `-noshell`; `-detached` implies `-noinput`
8. `-boot` specifies which boot script drives system startup
9. The `-args_file FileName` flag allows reading arguments from a file (useful for complex configurations)

# Construction / Recognition

## To Construct/Create:

Start a distributed node with code paths and configuration:

```text
% erl -sname mynode -setcookie mysecret -config myapp -pa ./ebin -s myapp start
```

Start headless for production:

```text
% erl -name mynode@host.example.com -setcookie mysecret -boot myrelease -detached -heart
```

## To Identify/Recognize:

1. Any `erl` argument starting with `-` is a flag
2. Init flags are documented as "(init flag)" in the erl man page
3. User flags can be retrieved at runtime: `init:get_argument(sname)` returns `{ok,[["mynode"]]}`

# Context & Application

Init and user flags are the primary way to configure an Erlang node's identity, distribution settings, code paths, and boot behavior. In production OTP releases, most flags are specified in the release's `vm.args` file (read via `-args_file`). The `-boot` flag points to the release boot script, `-config` to the sys.config, and `-name`/`-sname` establish the node's distributed identity.

The documentation warns about security: "Starting a distributed node without also specifying `-proto_dist inet_tls` will expose the node to attacks that may give the attacker complete access to the node and in extension the cluster."

# Examples

**Example 1** (erl documentation, "Flags" section): Starting a distributed node:

```text
% erl -sname arnie
(arnie@host)1> init:get_argument(sname).
{ok,[["arnie"]]}
```

**Example 2** (erl documentation, "Flags" section): Using eval to run code at startup:

```text
% erl -eval 'io:format("Hello~n")' -noshell -s init stop
Hello
```

**Example 3** (erl documentation, "Flags" section): Using `-proto_dist` for IPv6:

```text
% erl -name test@ipv6node.example.com -proto_dist inet6_tcp
```

# Relationships

## Builds Upon

- **erl-command** -- Flags are one of three argument types to erl

## Related

- **emulator-flags** -- The `+` flags that configure the VM itself
- **epmd** -- The port mapper daemon started automatically by `-name`/`-sname`
- **distribution-protocol** -- `-proto_dist` selects the distribution transport
- **crash-dump** -- `-heart` configures crash recovery; crash dump env vars interact with `-heart`

## Contrasts With

- **emulator-flags** -- Emulator flags (`+`) configure the VM; init/user flags (`-`) configure the Erlang runtime and applications

# Common Errors

- **Error**: Using `-name` on one node and `-sname` on another, then expecting them to communicate
  **Correction**: The documentation states: "No communication can exist between nodes running with flag `-sname` and those running with flag `-name`"

- **Error**: Using `-cookie` instead of `-setcookie`
  **Correction**: The documentation notes: "`-cookie Cookie` -- Obsolete flag without any effect and common misspelling for `-setcookie`. Use `-setcookie` instead."

# Common Confusions

- **Confusion**: Thinking `-noshell` and `-noinput` are the same
  **Clarification**: `-noshell` starts without a shell but can still read stdin; `-noinput` additionally ensures the runtime never tries to read input (and implies `-noshell`)

- **Confusion**: Believing `-pa` and `-pz` do the same thing
  **Clarification**: `-pa` prepends directories to the beginning of the code path; `-pz` appends them to the end. Also, `-pa` reverses the order of the given directories in the resulting path.

# Source Reference

"erl" command documentation, "Flags" section, covering init flags (`-boot`, `-eval`, `-s`, `-run`, `-S`, `-extra`, `--`) and user flags (`-name`, `-sname`, `-setcookie`, `-config`, `-pa`, `-pz`, `-heart`, `-hidden`, `-detached`, `-noshell`, `-noinput`, `-proto_dist`, `-remsh`).

# Verification Notes

- Flag categorization and semantics: Directly from erl "Flags" section
- Security warning: Verbatim from `-name` documentation
- `-cookie` deprecation: Directly from source
- Confidence: HIGH -- all flags and behaviors explicitly documented
