---
# === CORE IDENTIFICATION ===
concept: Distribution Command-Line Flags
slug: distribution-command-line-flags

# === CLASSIFICATION ===
category: distribution
subcategory: null
tier: intermediate

# === PROVENANCE ===
source: "Erlang Reference Manual"
source_slug: otp-reference-manual
authors: "Ericsson AB"
chapter: "Distributed Erlang"
chapter_number: null
pdf_page: null
section: "Distribution Command-Line Flags"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - distribution flags
  - erl distribution options

# === TYPED RELATIONSHIPS ===
prerequisites:
  - erlang-node
  - distributed-erlang-system
extends: []
related:
  - node-naming
  - transitive-connections
  - hidden-nodes
  - distributed-security
  - distribution-bifs
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What command-line flags control Erlang distribution?"
  - "How do you set a node name from the command line?"
  - "How do you set a cookie from the command line?"
  - "How do you make a node hidden from the command line?"
---

# Quick Definition
Distribution command-line flags are options passed to the `erl` executable that configure distributed Erlang behavior, including node naming (`-name`, `-sname`), cookie setup (`-setcookie`), hidden mode (`-hidden`), and connection behavior (`-connect_all false`).

# Core Definition
The Erlang Reference Manual provides a table of distribution command-line flags:

| Flag | Description |
|---|---|
| `-connect_all false` | Only explicit connection setups are used. |
| `-hidden` | Makes a node into a hidden node. |
| `-name Name` | Makes a runtime system into a node, using long node names. |
| `-setcookie Cookie` | Same as calling `erlang:set_cookie(Cookie)`. |
| `-setcookie Node Cookie` | Same as calling `erlang:set_cookie(Node, Cookie)`. |
| `-sname Name` | Makes a runtime system into a node, using short node names. |

(Distributed Erlang chapter, "Distribution Command-Line Flags" section).

# Prerequisites
- **erlang-node** -- Flags configure node properties
- **distributed-erlang-system** -- Flags configure distribution behavior

# Key Properties
1. `-name Name` -- enables distribution with long (fully qualified) node names
2. `-sname Name` -- enables distribution with short node names
3. `-setcookie Cookie` -- sets the default magic cookie (equivalent to `erlang:set_cookie(Cookie)`)
4. `-setcookie Node Cookie` -- sets a per-node cookie (equivalent to `erlang:set_cookie(Node, Cookie)`)
5. `-hidden` -- makes the node a hidden node (not visible in `nodes/0`, non-transitive connections)
6. `-connect_all false` -- disables transitive connections (only explicit connections are established)
7. These flags are passed to the `erl` executable at startup
8. Additional distribution-related flags exist in the `erl` command documentation

# Construction / Recognition
## To Use:
```
erl -sname mynode -setcookie mysecret
erl -name mynode@host.example.com -setcookie mysecret -hidden
erl -sname mynode -connect_all false
```

## To Identify:
1. These flags appear on the command line or in boot scripts
2. Their effects can be observed via `node/0`, `erlang:get_cookie()`, `nodes/0`

# Context & Application
These flags are the primary way to configure Erlang distribution at startup. They are used in shell scripts, systemd service files, release boot scripts, and development tooling.

**Typical contexts:**
- Production release scripts configuring node identity and security
- Development: `erl -sname dev -setcookie devcookie`
- Operations: `erl -sname ops -hidden -setcookie prodcookie`
- Complex topologies: `-connect_all false` for selective connectivity

# Examples
**Example 1** (Distributed Erlang, "Distribution Command-Line Flags" section): The complete flag table as listed by the source, reproduced in the Core Definition above.

**Example 2** (Distributed Erlang, "Nodes" section): Using `-name` and `-sname`:
```
erl -name dilbert     %% dilbert@uab.ericsson.se (long name)
erl -sname dilbert    %% dilbert@uab (short name)
```

# Relationships
## Builds Upon
- **erlang-node** -- Flags create and configure nodes
- **distributed-erlang-system** -- Flags configure the distributed system

## Enables
Nothing directly -- flags are configuration, not runtime capabilities.

## Related
- **node-naming** -- `-name` and `-sname` set the naming convention
- **transitive-connections** -- `-connect_all false` disables transitivity
- **hidden-nodes** -- `-hidden` creates hidden nodes
- **distributed-security** -- `-setcookie` configures authentication
- **distribution-bifs** -- Some flags are equivalent to BIF calls

## Contrasts With
No direct contrasts.

# Common Errors
- **Error**: Using `-name` on some nodes and `-sname` on others in the same cluster
  **Correction**: All nodes must use the same naming convention. Long-name and short-name nodes cannot communicate.

- **Error**: Setting `-setcookie` on the command line in an environment where the command line is visible to other users (e.g., `ps` output)
  **Correction**: Use the `.erlang.cookie` file for cookie configuration in security-sensitive environments.

# Common Confusions
- **Confusion**: Thinking `-setcookie Cookie` sets a cookie only for one specific connection
  **Clarification**: `-setcookie Cookie` (single argument) sets the default cookie for all connections, equivalent to `erlang:set_cookie(Cookie)`. Use `-setcookie Node Cookie` (two arguments) for per-node cookies.

# Source Reference
Distributed Erlang chapter, "Distribution Command-Line Flags" section.

# Verification Notes
- Definition source: Direct from source -- complete flag table reproduced
- Confidence rationale: High -- explicit table with descriptions from the reference manual
- Uncertainties: Additional flags exist (e.g., `-proto_dist`, `-dist_listen`) but are not listed in this section
- Cross-reference status: All referenced slugs correspond to planned cards
