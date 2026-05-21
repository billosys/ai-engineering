---
# === CORE IDENTIFICATION ===
concept: Distributed Security
slug: distributed-security

# === CLASSIFICATION ===
category: distribution
subcategory: null
tier: advanced

# === PROVENANCE ===
source: "Erlang Reference Manual"
source_slug: otp-reference-manual
authors: "Ericsson AB"
chapter: "Distributed Erlang"
chapter_number: null
pdf_page: null
section: "Security"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - magic cookie
  - distribution cookie
  - Erlang cookie

# === TYPED RELATIONSHIPS ===
prerequisites:
  - erlang-node
  - node-connections
extends: []
related:
  - distribution-bifs
  - distribution-command-line-flags
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How does Erlang authenticate nodes connecting to each other?"
  - "What is a magic cookie?"
  - "How is the .erlang.cookie file used?"
  - "Is Erlang distribution cryptographically secure by default?"
---

# Quick Definition
Erlang distribution uses magic cookies for authentication. All nodes use an Erlang atom as a magic cookie when connecting. During connection setup, cookies are compared using hashed challenges (not transferred directly). By default, the cookie is read from a `.erlang.cookie` file, but this provides protection against accidental misuse, not cryptographic security.

# Core Definition
The Erlang Reference Manual states: "Authentication determines which nodes are allowed to communicate with each other. In a network of different Erlang nodes, it is built into the system at the lowest possible level. All nodes use a _magic cookie_, which is an Erlang atom, when connecting to another node." The manual explains: "During the connection setup, after node names have been exchanged, the magic cookies the nodes present to each other are compared. If they do not match, the connection is rejected. The cookies themselves are never transferred; instead, they are compared using hashed challenges, although not in a cryptographically secure manner."

The manual explicitly warns that this security "does _not_ mean cryptographically secure, but rather security against accidental misuse." For strong security, the manual recommends "Using TLS for Erlang Distribution." (Distributed Erlang chapter, "Security" section).

# Prerequisites
- **erlang-node** -- Cookies are a per-node setting
- **node-connections** -- Cookie verification happens during connection setup

# Key Properties
1. Magic cookies are Erlang atoms used for authentication
2. Cookies are compared using hashed challenges -- never transferred in plain text
3. The comparison is not cryptographically secure
4. At startup, a random cookie is assigned; then `.erlang.cookie` is searched for in the user's home directory
5. If `.erlang.cookie` does not exist, it is created with a random string and mode 400 (read-only by user)
6. `erlang:set_cookie(Cookie)` sets the default cookie for all connections
7. `erlang:set_cookie(Node, Cookie)` sets a per-node cookie for connecting to a specific node
8. `erlang:get_cookie()` retrieves the current node's cookie
9. Nodes with identical cookie files can communicate freely
10. TLS distribution (`-proto_dist inet_tls`) is needed for actual cryptographic security
11. Inter-node communication is in clear text by default

# Construction / Recognition
## To Configure:
1. Ensure all nodes in a cluster share the same `.erlang.cookie` file
2. Or use `-setcookie Cookie` command-line flag
3. Or call `erlang:set_cookie(Cookie)` at runtime
4. For per-node cookies: `erlang:set_cookie(Node, Cookie)`
5. For TLS: use `-proto_dist inet_tls` and configure SSL options

## To Query:
1. `erlang:get_cookie()` -- current node's cookie
2. `erlang:get_cookie(Node)` -- cookie configured for a specific node

# Context & Application
Cookie-based authentication is sufficient for development and for preventing accidental connections between unrelated clusters. Production systems handling sensitive data or operating on untrusted networks should use TLS distribution for encryption and proper authentication.

**Typical contexts:**
- Development: shared cookie file in home directory
- Production: managed cookie distribution via configuration management tools
- Secure production: TLS distribution with certificate-based authentication
- Multi-cluster environments: per-node cookies with `-connect_all false`

# Examples
**Example 1** (Distributed Erlang, "Security" section): Cookie file behavior: "The first action of the Erlang network authentication server (`auth`) is then to search for a file named `.erlang.cookie` in the user's home directory [...] If none of the files exist, a `.erlang.cookie` file is created in the user's home directory. The UNIX permissions mode of the file is set to octal 400 (read-only by user) and its content is a random string."

**Example 2** (Distributed Erlang, "Security" section): Per-node cookie configuration: "For a node `Node1` using magic cookie `Cookie` to be able to connect to, and to accept a connection from, another node `Node2` that uses a different cookie `DiffCookie`, the function `erlang:set_cookie(Node2, DiffCookie)` must first be called at `Node1`."

**Example 3** (Distributed Erlang, "Security" section): The security caveat: "Furthermore, the communication between nodes is by default in clear text. If you need strong security, please see Using TLS for Erlang Distribution."

# Relationships
## Builds Upon
- **erlang-node** -- Cookies are a node-level security mechanism
- **node-connections** -- Cookie verification is part of connection setup

## Enables
Nothing directly.

## Related
- **distribution-bifs** -- `set_cookie/1,2` and `get_cookie/0,1` are distribution BIFs
- **distribution-command-line-flags** -- `-setcookie` flag configures cookies

## Contrasts With
No direct contrasts.

# Common Errors
- **Error**: Assuming default Erlang distribution is secure against network attackers
  **Correction**: The manual explicitly states that cookie-based security is "against accidental misuse" only. Communication is in clear text. Use `-proto_dist inet_tls` for real security.

- **Error**: Configuring `set_cookie(Node1, DiffCookie)` on both Node1 and Node2 with each other's cookies
  **Correction**: This creates a broken configuration where both nodes try to use the other's cookie. Instead, configure one side to use the other's default cookie.

# Common Confusions
- **Confusion**: Thinking the magic cookie is transmitted during connection setup
  **Clarification**: Cookies are never transferred directly. They are compared using hashed challenges. However, this is "not in a cryptographically secure manner."

- **Confusion**: Thinking `.erlang.cookie` must be manually created
  **Clarification**: If the file does not exist, it is automatically created with a random string when the first node starts.

# Source Reference
Distributed Erlang chapter, "Security" section.

# Verification Notes
- Definition source: Direct from source -- comprehensive section with explicit warnings
- Confidence rationale: High -- detailed, explicit security description
- Uncertainties: None
- Cross-reference status: All referenced slugs correspond to planned cards
