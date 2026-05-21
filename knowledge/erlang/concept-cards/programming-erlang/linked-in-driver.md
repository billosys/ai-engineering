---
# === CORE IDENTIFICATION ===
concept: Linked-in Driver
slug: linked-in-driver

# === CLASSIFICATION ===
category: tooling
subcategory: interfacing
tier: advanced

# === PROVENANCE ===
source: Programming Erlang, Second Edition
source_slug: programming-erlang
authors: Joe Armstrong
chapter: "Interfacing Techniques"
chapter_number: 15
pdf_page: null
section: "Advanced Interfacing Techniques"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "linked-in drivers"
  - "linked-in port driver"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - port
  - port-program
  - port-protocol
extends:
  - port-program
related:
  - nif
  - c-node
contrasts_with:
  - port-program

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is a linked-in driver?"
  - "How does a linked-in driver differ from an external port program?"
  - "Why is a linked-in driver faster but less safe?"
---

# Quick Definition

A linked-in driver is a port driver whose code is linked into the Erlang kernel and runs inside the Erlang OS process; it obeys the same protocol as an external port driver but is faster and less safe.

# Core Definition

Linked-in drivers are programs that obey the same protocol as the external port drivers; the only difference is that the driver code is linked *into* the Erlang kernel and thus runs inside the Erlang OS main process (Chapter 15, "Advanced Interfacing Techniques"). To make a linked-in driver, a small amount of initialization code must be added, and the driver must be compiled and linked with the Erlang VM. This places it among the *unsafe* interfacing techniques — running foreign code inside the Erlang VM means errors in that code might crash the Erlang system — but it is more efficient than using an external process. Up-to-date examples are maintained in an online archive (`git://github.com/erlang/linked_in_drivers.git`) because the technique changes more rapidly than Erlang itself.

# Prerequisites

- **Port** — A linked-in driver is reached through a port, just like an external driver.
- **Port program** — It is the in-kernel variant of an external port program.
- **Port protocol** — It obeys the same byte-stream protocol as port drivers.

# Key Properties

1. Obeys the same protocol as external port drivers.
2. The driver code is linked into the Erlang kernel and runs inside the Erlang OS process.
3. It is one of the *unsafe* interfacing techniques — a bug can crash the Erlang VM.
4. It is more efficient than an external port process.
5. Requires small initialization code plus compiling and linking with the Erlang VM.

# Construction / Recognition

## To Build a Linked-in Driver:
1. Write the driver obeying the port-driver protocol.
2. Add the small amount of initialization code required for a linked-in driver.
3. Compile and link the driver with the Erlang VM (e.g. producing `example1_drv.so`).

## To Recognize It:
1. Look for a shared object loaded into the VM rather than a separate executable.
2. Look for `open_port({spawn, Command}, ...)` resolving to a linked-in driver of that name.

# Context & Application

- **Typical contexts**: Performance-critical interfacing where the cost of an external process is too high.
- **Common applications**: The book's makefile builds `example1_drv.so` alongside the external `example1` program.
- **Historical/stylistic notes**: The detailed how-to is kept in an online archive because the technique changes faster than the language; the book gives only an overview.

# Examples

**Example 1** (Chapter 15, "Advanced Interfacing Techniques"): The book states a linked-in driver's only difference from a port driver is that its code "is linked into the Erlang kernel and thus runs inside the Erlang OS main process."

**Example 2** (Chapter 15, "Compiling and Linking the Port Program"): The makefile compiles `example1_drv.so` from `example1_lid.c` and `example1.c` with `gcc ... -bundle -flat_namespace`, producing the linked-in driver shared object.

# Relationships

## Builds Upon
- **Port program** — a linked-in driver is the in-kernel variant of an external port program.

## Enables
- Faster foreign-code interfacing than external processes.

## Related
- **NIF** — another in-VM technique, with even tighter integration.
- **C-node** — another advanced interfacing technique.

## Contrasts With
- **Port program** — an external port program is isolated and safe; a linked-in driver runs inside the VM, so it is faster but a crash takes down Erlang.

# Common Errors

- **Error**: Treating a linked-in driver as crash-isolated like an external port program.
  **Correction**: A linked-in driver runs in the VM — a bug can crash the whole Erlang system.
- **Error**: Using outdated build commands from the book for compiling/linking.
  **Correction**: Consult the online archive, since the build procedure changes more rapidly than Erlang.

# Common Confusions

- **Confusion**: A linked-in driver uses a different protocol from a port program.
  **Clarification**: It uses the *same* port-driver protocol; only its location (in-kernel) differs.
- **Confusion**: Linked-in drivers can be written in any language.
  **Clarification**: Like other in-kernel techniques, they require languages such as C that produce native object code.

# Source Reference

Chapter 15: Interfacing Techniques, section "Advanced Interfacing Techniques" (the "Linked-in Drivers" description) and "Compiling and Linking the Port Program" (the `example1_drv.so` makefile target).

# Verification Notes

- Definition source: Direct adaptation of the "Linked-in Drivers" overview and the makefile.
- Confidence rationale: HIGH — the concept is explicitly defined and distinguished from external port drivers, with a build example.
- Uncertainties: The book deliberately defers detailed how-to to an online archive; the card stays at the source's overview level.
- Cross-reference status: Slugs match planned chapter cards.
- Re-extraction notes: Fresh extraction; no pre-existing card.
