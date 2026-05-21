---
concept: Large-Scale Testing with Common Test
slug: large-scale-testing
category: testing
subcategory: common-test
tier: advanced
source: "Learn You Some Erlang for Great Good!"
source_slug: learn-you-some-erlang
authors: "Fred Hébert"
chapter: "Common Test for Uncommon Tests"
chapter_number: 28
pdf_page: null
section: "Large-Scale Testing"
extraction_confidence: high
aliases:
  - "distributed Common Test"
  - "CT master"
prerequisites:
  - common-test
  - ct-configuration
  - distributed-erlang
related:
  - ct-test-suite
contrasts_with: []
answers_questions:
  - "How do I run Common Test suites across multiple nodes?"
  - "What is the Common Test master node?"
---

# Large-Scale Testing with Common Test

## Quick Definition

Large-scale testing is Common Test's distributed mode, in which a central CT master node starts, supervises, and runs test suites across many other nodes.

## Core Definition

Common Test supports distributed tests: it can run test suites on many different nodes and can dynamically start those nodes and have them watch each other. When tests go distributed, Common Test requires a central node — the *CT master* — that directs everything: starting nodes, ordering tests to run, and gathering logs. Distributed testing is driven by an expanded test specification that adds `{node, NodeAlias, NodeName}` (a node-name alias) and `{init, NodeAlias, Options}` (which starts nodes via the `ct_slave` module) tuples, plus node-aware variants of the ordinary spec tuples (Chapter 28, "Large-Scale Testing").

## Prerequisites

- **Common Test** — Distributed testing is a Common Test capability
- **CT configuration** — Distributed runs are driven by test specification files
- **Distributed Erlang** — The tests run across connected, named Erlang nodes

## Key Properties

1. Requires a CT master node that controls all other nodes
2. The spec file gains `{node, Alias, NodeName}` and `{init, Alias, Options}` tuples
3. `{init, ...}` starts nodes using the `ct_slave` module; options include `username`/`password` (SSH), `startup_functions`, `erl_flags`, `monitor_master`, the boot/init/startup timeouts, and `kill_if_fail`
4. Ordinary spec tuples gain optional node arguments (`{suites, Nodes, Dir, Suites}`, etc.) so different suites run on different nodes
5. Special log aliases: `all_nodes` (all non-master nodes) and `master` (the master node); both are needed to cover everything
6. Distributed tests must be run with a `-name` distributed node via `ct_master:run/1` — `ct_run` cannot run them
7. `ct_master` reports every node as `finished_ok` only to indicate it could contact the node; actual results are stored on each individual node

## Construction / Recognition

## To Run Distributed Tests

1. Write a `.spec` file with `{node, Alias, NodeName}` tuples for each node
2. Add `{init, [aliases], [{node_start, Options}]}` to start the nodes
3. Add node-aware `{suites, [Node], Dir, Suites}` entries assigning suites to nodes
4. Start a node with `erl -name ct` and call `ct_master:run("dist.spec")`

## Context & Application

Distributed Common Test is useful when large test suites should run in parallel across many nodes to save time, or when production code runs on different computers and tests should reflect that. The author warns that as distributed tests grow more convoluted, confidence in them drops, since the tests themselves may contain more errors. Setting `monitor_master` to `true` is recommended so spawned remote nodes die with the master rather than lingering.

## Examples

**Example** (Chapter 28, "Creating a Distributed Spec File"): `dist.spec` declares `{node, a, 'a@ferdmbp.local'}.`, `{init, [a,b], [{node_start, [{monitor_master, true}]}]}.`, `{logdir, all_nodes, "./logs/"}.`, `{logdir, master, "./logs/"}.`, and node-scoped `{suites, [b], meeting, all}.` Running `ct_master:run("dist.spec")` starts nodes `a` and `b` with callback `ct_slave`.

## Relationships

## Builds Upon

- **Common Test** — Large-scale testing is the framework's distributed mode
- **CT configuration** — Driven by an extended form of the test specification

## Related

- **CT test suite** — Distributed runs assign suites to specific nodes

## Common Errors

- **Error**: Trying to run distributed tests with `ct_run`
  **Correction**: Distributed tests must use a `-name` node and `ct_master:run/1`

- **Error**: Reading `ct_master`'s `finished_ok` as confirmation that tests passed
  **Correction**: `finished_ok` only means the node was reachable; real results live on each node's logs

## Common Confusions

- **Confusion**: Expecting one `logdir` alias to cover every node
  **Clarification**: `all_nodes` covers non-master nodes and `master` covers the master; both are required for full coverage

## Source Reference

Chapter 28: Common Test for Uncommon Tests, section "Large-Scale Testing" (subsections "Creating a Distributed Spec File," "Running Distributed Tests").

## Verification Notes

- Definition: Direct adaptation from "Large-Scale Testing"
- Key Properties: All explicit in the chapter, including the `ct_slave` option list
- Confidence: HIGH — explicitly defined with a worked distributed spec
- Cross-references: `distributed-erlang` is a shared slug from Agent 4
