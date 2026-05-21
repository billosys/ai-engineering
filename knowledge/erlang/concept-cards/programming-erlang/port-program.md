---
# === CORE IDENTIFICATION ===
concept: Port Program
slug: port-program

# === CLASSIFICATION ===
category: tooling
subcategory: interfacing
tier: intermediate

# === PROVENANCE ===
source: Programming Erlang, Second Edition
source_slug: programming-erlang
authors: Joe Armstrong
chapter: "Interfacing Techniques"
chapter_number: 15
pdf_page: null
section: "Interfacing an External C Program with a Port"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "port process"
  - "external port driver"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - port
  - port-protocol
extends: []
related:
  - linked-in-driver
  - os-cmd
contrasts_with:
  - linked-in-driver

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is a port program?"
  - "How do I interface a C program to Erlang safely?"
  - "Why is running foreign code in an external process the safe approach?"
---

# Quick Definition

A port program (port process) is an external operating-system program that Erlang controls through a port; because it runs outside the Erlang virtual machine, a bug in it cannot crash the Erlang system.

# Core Definition

You can interface foreign-language programs to Erlang by running them *outside* the Erlang virtual machine in an external operating system process — the *safe* way of doing things (Chapter 15, chapter introduction). If the foreign-language code is incorrect, it will not crash the Erlang system. Erlang controls the external process through a *port* and communicates with it over a byte-oriented communication channel; Erlang is responsible for starting and stopping the external program and can monitor and restart it if it crashes. Such an external process is called a *port process* (or port program) because it is controlled through an Erlang port. The port program must follow the same byte-stream protocol as the Erlang side (e.g. the 2-byte length header for `{packet, 2}`).

# Prerequisites

- **Port** — A port program is the external program at the far end of a port.
- **Port protocol** — The port program must implement the agreed byte-stream protocol.

# Key Properties

1. A port program runs outside the Erlang VM as a separate OS process.
2. Because it is isolated, a crash in it cannot crash the Erlang system — the *safe* approach.
3. Erlang starts, stops, monitors, and can restart the external program.
4. Communication is over a byte-oriented channel framed by the port.
5. The port program must obey the same protocol (e.g. length headers) as the Erlang side.

# Construction / Recognition

## To Build a Port Program (per the C example):
1. Write the application functions (`example1.c`: `sum`, `twice`).
2. Write a driver loop (`example1_driver.c`) that reads commands from stdin, calls the functions, and writes results to stdout.
3. Write byte-stream I/O helpers (`erl_comm.c`: `read_cmd`, `write_cmd`, `read_exact`, `write_exact`) matching the 2-byte length header.
4. Compile and link the program (e.g. `gcc -o example1 example1.c erl_comm.c example1_driver.c`).

## To Recognize It:
1. Look for an external executable started via `open_port({spawn, "./prog"}, ...)`.
2. Look for a driver loop reading stdin and writing stdout in length-framed packets.

# Context & Application

- **Typical contexts**: Interfacing Erlang to C (or other native) code without risking the VM.
- **Common applications**: The `example1` C program exposing `sum/2` and `twice/1` to Erlang.
- **Historical/stylistic notes**: The book notes the example ignores integer precision/signedness mismatches between C and Erlang; real applications must address these.

# Examples

**Example 1** (Chapter 15, "The C Program"): The port program has three files — `example1.c` (the functions), `example1_driver.c` (the command loop), and `erl_comm.c` (memory-buffer read/write routines).

**Example 2** (Chapter 15, "Running the Program"): After `example1:start()`, calling `example1:sum(45, 32)` returns `77` and `example1:twice(10)` returns `20` — the work is done by the external C port program.

# Relationships

## Builds Upon
- **Port** — the port program is reached and controlled through a port.
- **Port protocol** — it must implement the agreed byte-stream protocol.

## Enables
- Safe integration of native code into Erlang systems.

## Related
- **os:cmd** — a simpler way to run an external OS command and capture its output.

## Contrasts With
- **Linked-in driver** — a linked-in driver runs the same protocol but is linked into the Erlang kernel (unsafe, faster); a port program runs as an isolated external process (safe).

# Common Errors

- **Error**: Assuming C and Erlang agree on integer size and signedness.
  **Correction**: Explicitly decide and convert types and precisions at the interface.
- **Error**: Running Erlang interface functions before the port driver is started.
  **Correction**: Call the start function (e.g. `example1:start()`) first; ideally automate it at system startup.

# Common Confusions

- **Confusion**: A port program runs inside the Erlang VM.
  **Clarification**: It runs as a separate external OS process — that isolation is exactly what makes it safe.
- **Confusion**: A port program is the same as a linked-in driver.
  **Clarification**: They share the protocol but differ in location: external process vs. linked into the kernel.

# Source Reference

Chapter 15: Interfacing Techniques, chapter introduction (the three ways of interfacing) and sections "Interfacing an External C Program with a Port," "The C Program," "Compiling and Linking the Port Program," and "Running the Program."

# Verification Notes

- Definition source: Direct adaptation of the chapter introduction and the `example1` C program walkthrough.
- Confidence rationale: HIGH — the port-process concept and a complete worked example are explicitly given.
- Uncertainties: None.
- Cross-reference status: Slugs match planned chapter cards (`port`, `port-protocol`, `linked-in-driver`, `os-cmd`).
- Re-extraction notes: Fresh extraction; no pre-existing card.
