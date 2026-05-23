---
concept: Inet Configuration
slug: inet-configuration
category: distribution
subcategory: networking
tier: intermediate
source: "ERTS User's Guide"
source_slug: otp-erts
authors: "Ericsson AB"
chapter: "Inet Configuration"
chapter_number: null
pdf_page: null
section: "Inet Configuration"
extraction_confidence: high
aliases:
  - "inetrc"
  - "inet config"
  - "hostname resolution configuration"
  - "Erlang DNS configuration"
prerequisites: []
extends: []
related:
  - erl-command
  - init-flags
  - distribution-protocol
contrasts_with: []
answers_questions:
  - "How do I configure inet for hostname resolution?"
  - "How does Erlang resolve hostnames?"
  - "What is the inetrc file?"
  - "How do I configure the Erlang DNS client?"
---

# Quick Definition

Inet configuration controls how the Erlang runtime system resolves hostnames and IP addresses. It can use native OS calls, a hosts file, or the built-in DNS client (`inet_res`), configured via a user `inetrc` file or the `ERL_INETRC` environment variable.

# Core Definition

The documentation states: "This section describes how the Erlang runtime system is configured for IP communication. It also explains how you can configure it for your needs by a configuration file. The information is primarily intended for users with special configuration needs or problems. There is normally no need for specific settings for Erlang to function properly on a correctly IP-configured platform."

**Lookup methods** (set via the `{lookup, Methods}` parameter):
- `native` -- Uses system calls (the default on all platforms)
- `file` -- Uses host data from configuration files and/or the user configuration file
- `dns` -- Uses the Erlang DNS client `inet_res` for nameserver queries

**Configuration sources**, in order:
1. System inet configuration files (e.g., `/etc/resolv.conf`, `/etc/hosts`) -- read automatically in long-name distributed mode
2. System registry (Windows)
3. User configuration file (inetrc) -- always examined last, can override all previous settings

**Specifying the inetrc file:**
- Kernel variable: `erl -kernel inetrc '"./cfg_files/erl_inetrc"'`
- Environment variable: `export ERL_INETRC=./cfg_files/erl_inetrc`
- The Kernel variable overrides the environment variable

**Key configuration parameters:**
- `{host, IP, Aliases}` -- Adds a host entry
- `{domain, Domain}` -- Sets the domain name
- `{nameserver, IP [,Port]}` -- Adds a primary nameserver for `inet_res`
- `{search, Domains}` -- Adds search domains for `inet_res`
- `{lookup, Methods}` -- Sets the lookup method order
- `{resolv_conf, File}` -- Specifies the file for resolver configuration (default `/etc/resolv.conf`)
- `{hosts_file, File}` -- Specifies the hosts file (default `/etc/hosts`)
- `{cache_size, Size}` -- Resolver cache size for DNS lookups (default 100 records)
- `{cache_refresh, Time}` -- How often the cache is refreshed in milliseconds (default 1 hour)
- `{timeout, Time}` -- DNS query retry timeout in milliseconds (default 2 seconds)
- `{retry, N}` -- Number of DNS retries (default 3)

# Prerequisites

None.

# Key Properties

1. No special configuration is normally needed on a correctly configured platform
2. Native lookup (system calls) is always the default method
3. In short-name mode (`-sname`), Erlang reads no system inet files except `/etc/resolv.conf` and `/etc/hosts`
4. In long-name mode (`-name`), Erlang reads system inet files to obtain the domain name
5. The user configuration file is always examined last, allowing overrides
6. `inet:get_rc()` can be called to view the current state of the inet configuration database
7. The `resolv_conf` and `hosts_file` are monitored for changes at runtime
8. Setting `resolv_conf` or `hosts_file` to an empty string `""` disables reading and monitoring

# Construction / Recognition

## To Construct/Create:

Create a user inetrc file with configuration parameters (each terminated with a full stop):

```erlang
%% -- ERLANG INET CONFIGURATION FILE --
%% read the hosts file
{file, hosts, "/etc/hosts"}.
%% add a particular host
{host, {134,138,177,105}, ["finwe"]}.
%% do not monitor the hosts file
{hosts_file, ""}.
%% read and monitor nameserver config from here
{resolv_conf, "/usr/local/etc/resolv.conf"}.
%% enable EDNS
{edns,0}.
%% disable caching
{cache_size, 0}.
%% specify lookup method
{lookup, [file, dns]}.
```

Start Erlang with the configuration:

```text
% erl -sname my_node -kernel inetrc '"./cfg_files/erl_inetrc"'
```

## To Identify/Recognize:

1. Files named `erl_inetrc` or referenced by `ERL_INETRC` are inet configuration files
2. The configuration uses Erlang term syntax with entries terminated by periods
3. Call `inet:get_rc()` at runtime to inspect the active configuration

# Context & Application

Inet configuration is important for distributed Erlang nodes that need custom hostname resolution, especially in environments where DNS is not available or where specific nameservers must be used. In container and cloud environments, custom inet configuration may be needed when default DNS behavior does not match the deployment topology.

The `dns` lookup method uses the built-in `inet_res` module, which supports EDNS (via `{edns, 0}`), TCP fallback (via `{usevc, true}`), and IPv6 lookups (via `{inet6, true}`).

# Examples

**Example 1** (Inet Configuration, "User Configuration Example" section): A complete inetrc file that uses file and DNS lookups with EDNS enabled and caching disabled:

```erlang
%% -- ERLANG INET CONFIGURATION FILE --
%% read the hosts file
{file, hosts, "/etc/hosts"}.
%% add a particular host
{host, {134,138,177,105}, ["finwe"]}.
%% do not monitor the hosts file
{hosts_file, ""}.
%% read and monitor nameserver config from here
{resolv_conf, "/usr/local/etc/resolv.conf"}.
%% enable EDNS
{edns,0}.
%% disable caching
{cache_size, 0}.
%% specify lookup method
{lookup, [file, dns]}.
```

# Relationships

## Related

- **erl-command** -- The `-kernel inetrc` flag specifies the inetrc file
- **init-flags** -- The `-sname`/`-name` flags determine whether system inet files are read
- **distribution-protocol** -- Hostname resolution is required for distributed Erlang communication

# Common Errors

- **Error**: Specifying hostnames instead of IP addresses in the `{nameserver, ...}` parameter
  **Correction**: Nameserver addresses must be IP tuples like `{134,138,177,105}`, not hostnames

- **Error**: Forgetting the trailing period on inetrc entries
  **Correction**: Each parameter in the inetrc file must be terminated with a full stop (`.`)

# Common Confusions

- **Confusion**: Believing that the `native` lookup method reads the inetrc file
  **Clarification**: `native` uses OS system calls exclusively; only `file` and `dns` methods use the inet configuration database

- **Confusion**: Thinking the old `.inetrc` file format is still supported
  **Clarification**: The documentation states: "the use of an `.inetrc` file, which was supported in earlier Erlang/OTP versions, is now obsolete"

# Source Reference

"Inet Configuration" chapter, including "Introduction", "Configuration Data", and "User Configuration Example" sections.

# Verification Notes

- Configuration parameters and defaults: Directly from "Configuration Data" section
- User configuration example: Verbatim from source
- Lookup method descriptions: Directly from source
- Confidence: HIGH -- all configuration parameters explicitly documented with defaults
