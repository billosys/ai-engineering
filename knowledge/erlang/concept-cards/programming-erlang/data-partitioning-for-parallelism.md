---
# === CORE IDENTIFICATION ===
concept: Data Partitioning for Parallelism
slug: data-partitioning-for-parallelism

# === CLASSIFICATION ===
category: performance
subcategory: parallelism
tier: intermediate

# === PROVENANCE ===
source: Programming Erlang, Second Edition
source_slug: programming-erlang
authors: Joe Armstrong
chapter: "Sherlock's Last Case"
chapter_number: 27
pdf_page: null
section: "The Importance of Partitioning the Data"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - partitioning the data
  - data partitioning

# === TYPED RELATIONSHIPS ===
prerequisites:
  - pmap
extends: []
related:
  - mapreduce
  - sequential-bottleneck
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do I make a data-processing program easy to parallelize?"
  - "Why is partitioning data the key to parallelization?"
---

# Quick Definition

Data partitioning for parallelism is the technique of splitting a dataset into independent partitions so the program can be parallelized by a one-line change from a list comprehension to `pmap`.

# Core Definition

"Partitioning the data is the key to parallelizing the program." When data is organized into independent collections, a sequential program that processes each partition with a list comprehension — `[process_year(I) || I <- mail_years()]` — can be parallelized by replacing the comprehension with a `pmap` call: `lib_misc:pmap(fun(I) -> process_year(I) end, mail_years())`. There is "an additional and less obvious benefit": because partitions are independent, "to test that our program works, we have to work with only one of the years" ("The Importance of Partitioning the Data").

# Prerequisites

- **pmap** — Partitioned data is parallelized by swapping a list comprehension for `pmap`.

# Key Properties

1. The dataset is divided into independent partitions (e.g., one directory of mails per year).
2. Each partition can be processed by an independent function call with no shared state.
3. Parallelization is a one-line change: replace `[f(I) || I <- Partitions]` with `pmap(fun(I) -> f(I) end, Partitions)`.
4. Independence lets you develop and test against a single partition.
5. It is exactly the partition-then-gather form used in a map-reduce architecture.

# Construction / Recognition

## To Construct/Create:
1. Divide the dataset into independent partitions (by year, by file, by key range).
2. Write a function that processes a single partition with no cross-partition dependencies.
3. Drive all partitions with a list comprehension while developing.
4. To parallelize, replace the comprehension with a `pmap` over the partitions.

## To Identify/Recognize:
1. A top-level list comprehension over independent data collections is partition-ready.
2. Swapping it for `pmap` with no other change confirms the data was well partitioned.

# Context & Application

- **Typical contexts**: Large data-processing programs intended to scale across cores or machines.
- **Common applications**: Sherlock partitions the Erlang mailing-list archive into per-year directories; `process_all_years` processes each year.
- **Historical/stylistic notes**: "To search the mail data quickly, we'd use seventeen machines, each looking at one year's worth of data... This is the main idea in map-reduce." The chapter develops Sherlock against 2009 alone (7,906 mails) precisely because partitions are independent.

# Examples

**Example 1** ("The Importance of Partitioning the Data"): The sequential form:

```erlang
process_all_years() ->
    [process_year(I) || I <- mail_years()].
```

**Example 2** ("The Importance of Partitioning the Data"): Parallelized by a one-line change:

```erlang
process_all_years() ->
    lib_misc:pmap(fun(I) -> process_year(I) end, mail_years()).
```

# Relationships

## Builds Upon
- This card builds on `pmap`; it has no elaborating prerequisite card.

## Enables
- A trivially parallelizable, independently testable data-processing program.

## Related
- **mapreduce** — Partition-then-gather is the core of the map-reduce architecture.
- **Sequential bottleneck** — Good partitioning avoids contention on a shared resource.

## Contrasts With
- This concept has no direct contrast within the chapter.

# Common Errors

- **Error**: Letting partition-processing functions share mutable state or depend on each other.
  **Correction**: Make each partition fully independent so `pmap` can run them concurrently and correctly.

- **Error**: Developing against the whole dataset when partitions are independent.
  **Correction**: Develop and test against a single partition (e.g., one year), then scale out unchanged.

# Common Confusions

- **Confusion**: Thinking parallelization requires rewriting the algorithm.
  **Clarification**: With well-partitioned data, parallelization is just changing a list comprehension into a `pmap`.

# Source Reference

Chapter 27: Sherlock's Last Case, Section "The Importance of Partitioning the Data."

# Verification Notes

- Definition source: Direct quote and adaptation from "The Importance of Partitioning the Data."
- Confidence rationale: HIGH — the source explicitly names partitioning as "the key" and shows the before/after code.
- Uncertainties: None.
- Cross-reference status: Verified concept names exist or are planned.
- Re-extraction notes: Fresh extraction; no pre-existing card.
