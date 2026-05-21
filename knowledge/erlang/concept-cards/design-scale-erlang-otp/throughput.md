---
# === CORE IDENTIFICATION ===
concept: Throughput
slug: throughput

# === CLASSIFICATION ===
category: performance
subcategory: capacity
tier: foundational

# === PROVENANCE ===
source: "Designing for Scalability with Erlang/OTP"
source_slug: design-scale-erlang-otp
authors: "Francesco Cesarini & Steve Vinoski"
chapter: "Scaling Out"
chapter_number: 14
pdf_page: 424
section: "Capacity Planning"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - throughput

# === TYPED RELATIONSHIPS ===
prerequisites: []
extends: []
related:
  - latency
  - capacity-planning
  - littles-law
  - bottleneck
contrasts_with:
  - latency

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is throughput?"
  - "How is throughput measured?"
---

# Quick Definition

Throughput is the number of units going through a system, measured in requests per second for uniform requests, or in bytes per second when request size varies.

# Core Definition

"Throughput refers to the number of units going through the system. Units could be measured in number of requests per second when dealing with uniform requests, but when the CPU load and amount of memory needed to process the requests vary in size (think emails or email attachments), throughput is better measured in kilobytes, megabytes, or gigabytes per second" (Cesarini & Vinoski, p. 429).

# Prerequisites

This is a foundational concept with no prerequisites within this source. It is one of the two core measures (with latency) used throughout capacity planning.

# Key Properties

1. The number of units going through the system.
2. Measured in requests per second for uniform requests.
3. Measured in KB/MB/GB per second when request size varies.
4. In a properly balanced Erlang system at maximum capacity, throughput stays constant while latency varies.
5. Removing bottlenecks gives a constant throughput regardless of the number of simultaneous requests.

# Construction / Recognition

## To Construct/Create:
This is a measure, not an artifact. To measure it:
1. Count units (requests or bytes) processed per unit time.
2. Choose request-count units for uniform requests, byte-rate units for variable-size requests.
3. Track it across load tests to verify it stays constant.

## To Identify/Recognize:
1. Recognize throughput as a rate of work completed, independent of how long any single request takes.

# Context & Application

- **Typical contexts**: Capacity planning, balancing, and load testing.
- **Common applications**: Measuring instant messages per second, megabytes sent by a web server, log entries stored per second.
- **Historical/stylistic notes**: The BEAM VM is one of the few VMs where a balanced system under sustained heavy load yields constant throughput (p. 433).

# Examples

**Example 1** (p. 429): Throughput is measured in requests per second for uniform requests, but in kilobytes, megabytes, or gigabytes per second for variable-size requests such as emails and attachments.

**Example 2** (p. 433): In a balanced Erlang system handling a peak throughput of 20,000 requests per second, throughput stays constant at 20,000 while latency doubles from 1 second (20,000 simultaneous requests) to 2 seconds (40,000 simultaneous requests).

# Relationships

## Builds Upon
- This is a foundational concept; it builds on nothing else within this source.

## Enables
- Throughput is a core input to capacity planning, balancing, and Little's Law.

## Related
- **Latency** — The complementary capacity measure
- **Capacity planning** — Uses throughput as a core measure
- **Littles law** — Relates throughput (arrival rate) to queue length and response time
- **Bottleneck** — A bottleneck degrades throughput

## Contrasts With
- **Latency** — Throughput is the rate of work completed; latency is the time for a single request

# Common Errors

- **Error**: Measuring throughput in requests per second when request sizes vary widely
  **Correction**: For variable-size requests (emails, attachments), measure throughput in bytes per second instead.

# Common Confusions

- **Confusion**: Higher load always lowers throughput.
  **Clarification**: In a balanced Erlang system, throughput stays constant under load while latency rises; only an unbalanced (bottlenecked) system shows degraded throughput.

# Source Reference

Chapter 14: Scaling Out, "Capacity Planning," page 429, and "Balancing Your System," page 433.

# Verification Notes

- Definition source: Direct quote from p. 429.
- Confidence rationale: HIGH — the source explicitly defines throughput.
- Uncertainties: None.
- Cross-reference status: Verified against planned cards.
- Re-extraction notes: Fresh extraction — no pre-existing card for this concept.
