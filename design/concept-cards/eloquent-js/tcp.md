---
# === CORE IDENTIFICATION ===
concept: TCP (Transmission Control Protocol)
slug: tcp

# === CLASSIFICATION ===
category: web-platform
subcategory: null
tier: intermediate

# === PROVENANCE ===
source: "Eloquent JavaScript, 4th Edition"
source_slug: eloquent-js
authors: "Marijn Haverbeke"
chapter: "JavaScript and the Browser"
chapter_number: 13
pdf_page: null
section: "Networks and the Internet"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - Transmission Control Protocol

# === TYPED RELATIONSHIPS ===
prerequisites:
  - network-protocol
extends:
  - network-protocol
related:
  - http
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is TCP?"
---

# Quick Definition
TCP is a protocol that provides reliable, ordered data transmission between computers, forming a two-way communication pipe that most internet protocols are built upon.

# Core Definition
"The *Transmission Control Protocol* (TCP) is a protocol that addresses this problem [of reliable data delivery]. All internet-connected devices 'speak' it, and most communication on the internet is built on top of it." A TCP connection "acts as a two-way pipe through which bits can flow---the machines on both ends can put data into it." (Eloquent JavaScript, Ch. 13, lines 112-140)

# Prerequisites
- **Network protocol**: Understanding what a protocol is

# Key Properties
1. Ensures data arrives in the correct order
2. Ensures data arrives at the correct destination
3. Works with ports to distinguish different services on one machine
4. Uses a client-server model (listener/connector)
5. Creates a two-way communication pipe
6. "You could say that TCP provides an abstraction of the network" (line 140)

# Construction / Recognition
TCP connections involve a listening server and a connecting client on a specific port. For example, HTTP typically uses port 80; SMTP uses port 25.

# Context & Application
TCP is the transport layer protocol underlying most internet communication. HTTP, email, and most web services use TCP.

# Examples
From the source: "One computer must be waiting, or *listening*, for other computers to start talking to it. To be able to listen for different kinds of communication at the same time on a single machine, each listener has a number (called a *port*) associated with it." (lines 119-122)

"The listening computer is called the *server*, and the connecting computer is called the *client*." (lines 132-133)

# Relationships
## Builds Upon
- Basic network data transmission
## Enables
- HTTP and other application-level protocols
## Related
- HTTP (built on top of TCP)
## Contrasts With
- Raw packet-based communication (without ordering guarantees)

# Common Errors
- **Error**: Assuming TCP and HTTP are the same thing
  **Correction**: HTTP is built on top of TCP; TCP handles reliable delivery, HTTP defines the request/response format

# Common Confusions
- **Confusion**: TCP connections are one-directional
  **Clarification**: TCP connections are bidirectional -- both sides can send and receive data

# Source Reference
Chapter 13: JavaScript and the Browser, Section "Networks and the Internet", lines 112-140 of 13-javascript-and-the-browser.md.

# Verification Notes
- Definition source: direct quotation
- Confidence rationale: Clearly defined
- Cross-reference status: verified
