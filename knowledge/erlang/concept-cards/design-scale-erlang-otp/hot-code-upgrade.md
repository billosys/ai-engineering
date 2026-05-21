---
# === CORE IDENTIFICATION ===
concept: Hot Code Upgrade
slug: hot-code-upgrade

# === CLASSIFICATION ===
category: applications-releases
subcategory: code-loading
tier: intermediate

# === PROVENANCE ===
source: "Designing for Scalability with Erlang/OTP"
source_slug: design-scale-erlang-otp
authors: "Francesco Cesarini & Steve Vinoski"
chapter: "Introducing Erlang"
chapter_number: 1
pdf_page: 40
section: "Upgrading Modules"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - upgrading modules
  - code upgrade
  - runtime code loading
  - hot code loading

# === TYPED RELATIONSHIPS ===
prerequisites:
  - processes-and-message-passing
extends: []
related: []
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How does Erlang upgrade code at runtime?"
  - "What is a fully qualified call and why does it matter for upgrades?"
  - "How many versions of a module can the VM hold?"
---

# Quick Definition

Hot code upgrade is the ability to load a new version of a module into a running system without stopping it. Processes switch to the new code on their next fully qualified call.

# Core Definition

"One of the advantages of dynamic typing is the ability to upgrade your code during runtime, without the need to take down the system. ... you can load a fix without terminating the process and it starts running the fixed version, retaining its state and variables" (Cesarini & Vinoski, p. 46). "At any one time, two versions of a module may exist in the virtual machine: the old and current versions" (p. 46). "The next time PidA makes a fully qualified call to a function in module B, a check will be made to ensure that PidA is running the latest version of the code. ... the pointer to the code will be switched to the new current version" (p. 46). This property supports "five-nines availability" — 99.999% uptime including upgrades.

# Prerequisites

- **Processes and message passing** — Upgrades operate on running processes; the switch happens on a process's next qualified call.

# Key Properties

1. New code can be loaded without stopping the system; state is retained.
2. The VM holds at most two versions of a module: old and current.
3. A process switches to the current version on its next *fully qualified* call (`B:loop()`).
4. An unqualified call (`loop()`) keeps running the old code.
5. Loading a third version purges the oldest; processes still running it are terminated.
6. Code is loaded via `c(Module)`, `compile:file/1`, `l(Module)`, `code:load_file/1`, or implicitly when calling an unloaded module.
7. `code:purge/1` forcibly purges old code (terminating its processes); `code:soft_purge/1` purges only if no process uses it.

# Construction / Recognition

## To Construct:
1. Compile or load the new module version into the running VM.
2. Ensure long-lived loop functions make fully qualified calls so they pick up the new code.

## To Recognize:
1. Module loop functions calling themselves with a module prefix (`?MODULE:loop(...)` or `mod:loop(...)`).

# Context & Application

- **Typical contexts**: Long-running systems requiring continuous availability.
- **Common applications**: Bug fixes, feature additions, and upgrades applied to live systems.
- **Historical/stylistic notes**: Module upgrades are "the icing on the cake" of Erlang's concurrency and fault-tolerance story.

# Examples

**Example 1** (p. 46, Figure 2-4): A three-frame upgrade — PidA runs the current version of B; new B is loaded, making the running version "old"; PidA's next fully qualified call switches the code pointer to the new current version.

**Example 2** (p. 46): "If the function call is fully qualified — i.e., of the form `B:loop()` — the next call will use the upgraded code; otherwise (when the call is simply `loop()`), the process will continue to run the old code."

# Relationships

## Builds Upon
- *(none — foundational)*

## Enables
- *(none specific in scope)*

## Related
- *(none additional)*

## Contrasts With
- *(none)*

# Common Errors

- **Error**: Writing a loop's self-call unqualified and expecting it to pick up new code.
  **Correction**: Use a fully qualified call (`Module:loop(...)`) so a loaded upgrade takes effect.
- **Error**: Recompiling with `erlc` and expecting the running VM to reload automatically.
  **Correction**: `erlc` only produces a `.beam` file; the module must be explicitly loaded.

# Common Confusions

- **Confusion**: Thinking the VM keeps every loaded version of a module.
  **Clarification**: Only two versions (old and current) are kept; loading a third purges and terminates processes on the oldest.

# Source Reference

Chapter 1: Introducing Erlang, Section "Upgrading Modules," pages 46-47. See Figure 2-4 (a software upgrade).

# Verification Notes

- Definition source: Direct quotes from pp. 46-47.
- Confidence rationale: HIGH — explicit, detailed treatment of the upgrade mechanism.
- Uncertainties: None.
- Cross-reference status: Verified against planned cards.
- Re-extraction notes: Fresh extraction — no pre-existing card for this source.
</content>
</invoke>
