---
# === CORE IDENTIFICATION ===
concept: Cosine Similarity
slug: cosine-similarity

# === CLASSIFICATION ===
category: performance
subcategory: text-analysis
tier: advanced

# === PROVENANCE ===
source: Programming Erlang, Second Edition
source_slug: programming-erlang
authors: Joe Armstrong
chapter: "Sherlock's Last Case"
chapter_number: 27
pdf_page: null
section: "Cosine Similarity: The Similarity of Two Weighted Vectors"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - cosine similarity
  - normalized cross product
  - "cosine_similarity/2"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - tf-idf-weight
extends: []
related:
  - faceted-search
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do I measure the similarity of two documents?"
  - "What is cosine similarity and how is it computed?"
---

# Quick Definition

Cosine similarity is the normalized cross product of two keyword vectors — a number from 0 to 1 measuring how similar two documents are.

# Core Definition

"To compute the similarity between two documents, we compute the keyword vectors for each document, and then we compute the normalized cross product of the keyword vectors. This is called the cosine similarity of the documents." The **cross product** of two keyword vectors "is the sum of the product of weights of entities with identical keywords." The cosine similarity divides the cross product "by the norms of each of the vectors. The norm of a vector is the square root of the sum of the squares of the weights." The result "is a number from 0 to 1. 1 means the two vectors are identical. 0 means they have no similarities" ("Cosine Similarity: The Similarity of Two Weighted Vectors").

# Prerequisites

- **TF*IDF weight** — Cosine similarity operates on the TF*IDF keyword vectors of the two documents being compared.

# Key Properties

1. Input is two keyword vectors — lists of `{Keyword, Weight}` pairs.
2. Cross product = sum over shared keywords of the product of their weights.
3. Norm of a vector = square root of the sum of the squares of its weights.
4. Cosine similarity = cross product ÷ (norm₁ × norm₂).
5. The result ranges from 0 (no similarity) to 1 (identical vectors).
6. It is provided in Sherlock as the library function `sherlock_similar:cosine_similarity/2`.

# Construction / Recognition

## To Construct/Create:
1. Compute the TF*IDF keyword vectors `K1` and `K2` for the two documents.
2. Compute the cross product: for keywords appearing in both vectors, sum the products of their weights.
3. Compute each vector's norm: square root of the sum of the squares of its weights.
4. Divide the cross product by the product of the two norms.

## To Identify/Recognize:
1. A similarity score in [0,1] derived by normalizing a weighted dot product is a cosine similarity.

# Context & Application

- **Typical contexts**: Document-similarity search and ranking in search engines.
- **Common applications**: Sherlock computes cosine similarity between a query document's keyword vector and every document in the corpus, then returns the highest-scoring matches.
- **Historical/stylistic notes**: Holmes's plan in the chapter's frame story is to find "the most similar posting in the mailing list... that maximizes the cosine similarity of the TF*IDF scores of the words in the document."

# Examples

## Worked Example

From "Cosine Similarity..." with `K1 = [{a,0.5},{b,0.1},{c,0.2}]` and `K2 = [{a,0.3},{b,0.2},{d,0.6}]`:

1. Cross product over shared keywords `a` and `b`: `Cross = 0.5*0.3 + 0.1*0.2` = `0.16999999999999998`.
2. `Norm1 = math:sqrt(0.5*0.5 + 0.1*0.1 + 0.2*0.2)` = `0.5477225575051662`.
3. `Norm2 = math:sqrt(0.3*0.3 + 0.2*0.2 + 0.6*0.6)` = `0.7`.
4. Cosine similarity = `Cross/(Norm1*Norm2)` = `0.4433944513137058`.

This is baked into the library: `sherlock_similar:cosine_similarity(K1, K2)` returns `0.4433944513137058`.

# Relationships

## Builds Upon
- **TF*IDF weight** — Cosine similarity is computed over TF*IDF keyword vectors.

## Enables
- Similarity queries — finding the documents most similar to a query document.

## Related
- **Faceted search** — Another query mechanism over the same parsed corpus.

## Contrasts With
- This concept has no direct contrast within the chapter.

# Common Errors

- **Error**: Reporting the raw cross product as the similarity.
  **Correction**: Divide by the product of the two vector norms to get a normalized [0,1] score.

- **Error**: Including keywords present in only one vector when computing the cross product.
  **Correction**: The cross product sums weight products only for keywords appearing in *both* vectors.

# Common Confusions

- **Confusion**: Treating the similarity score as a definitive ranking of "most interesting."
  **Clarification**: "The similarity score alone is not enough to determine which of the files is most interesting; the system only suggests files that might be similar" — a human must judge.

# Source Reference

Chapter 27: Sherlock's Last Case, Section "Adding Keywords to the Postings," subsection "Cosine Similarity: The Similarity of Two Weighted Vectors."

# Verification Notes

- Definition source: Direct quote and adaptation from "Cosine Similarity..."; the worked example reproduces the book's shell session verbatim.
- Confidence rationale: HIGH — the source defines cross product, norm, and cosine similarity precisely with a numeric walkthrough.
- Uncertainties: None.
- Cross-reference status: Verified concept names exist or are planned.
- Re-extraction notes: Fresh extraction; no pre-existing card.
