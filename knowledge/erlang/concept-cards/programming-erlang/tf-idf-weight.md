---
# === CORE IDENTIFICATION ===
concept: TF*IDF Weight
slug: tf-idf-weight

# === CLASSIFICATION ===
category: performance
subcategory: text-analysis
tier: intermediate

# === PROVENANCE ===
source: Programming Erlang, Second Edition
source_slug: programming-erlang
authors: Joe Armstrong
chapter: "Sherlock's Last Case"
chapter_number: 27
pdf_page: null
section: "The Significance of a Word: The TF*IDF Weight"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "TF*IDF"
  - "TF-IDF"
  - term frequency inverse document frequency
  - "TF*IDF score"

# === TYPED RELATIONSHIPS ===
prerequisites: []
extends: []
related:
  - cosine-similarity
  - faceted-search
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is a TF*IDF weight and how is it computed?"
  - "How do I measure the significance of a word in a document?"
---

# Quick Definition

The TF*IDF weight of a word in a document is its term frequency multiplied by its inverse document frequency — a number from 0 to 1 measuring how significant the word is to that document.

# Core Definition

"A commonly used measure of significance for words is the so-called TF*IDF weight. TF stands for term frequency, and IDF stands for inverse document frequency." The **term frequency** of a word in a document "is simply the number of times the word occurs in the document divided by the number of words in the document." The **inverse document frequency** of a word `W` "is defined as `log(Tot/N+1)`, where `Tot` is the total number of documents in the corpus and `N` is the number of documents that contain the word `W`." The TF*IDF weight is the product, "a number from 0 to 1, where 0 means the word is insignificant and 1 means the word is highly significant" ("The Significance of a Word: The TF*IDF Weight").

# Prerequisites

This is a foundational text-analysis concept with no prerequisites within this source.

# Key Properties

1. TF (term frequency) = occurrences of the word in the document ÷ total words in the document.
2. IDF (inverse document frequency) of word `W` = `log(Tot/N+1)`, where `Tot` is corpus size and `N` is the number of documents containing `W`.
3. The TF*IDF weight is the product TF × IDF.
4. The weight ranges from 0 (insignificant) to 1 (highly significant).
5. A word common across the corpus has low IDF and thus low significance; a word frequent in *this* document but rare in the corpus scores highly.
6. Computing keywords is a two-pass process: pass one computes each word's IDF over the corpus; pass two computes keywords per document.

# Construction / Recognition

## To Construct/Create:
1. Break each document into words (sequences of alphabetic characters separated by non-alphabetic characters).
2. Pass one: over the whole corpus, compute the IDF of each word — `log(Tot/N+1)`.
3. Pass two: for each document, compute TF for each word and multiply by its IDF.
4. Select the words with the highest TF*IDF weights as the document's keywords; omit very low weights.

## To Identify/Recognize:
1. A keyword vector — a list of `{Word, Weight}` pairs with weights in [0,1] — is a TF*IDF result.

# Context & Application

- **Typical contexts**: Search engines and similarity analysis over text corpora.
- **Common applications**: Sherlock computes a keyword vector for each posting in the Erlang mailing list (the corpus is 73,445 mails); `sherlock_tfidf.erl` computes the weights.
- **Historical/stylistic notes**: "Many search engines use the TF*IDF weights of words in a document to rank the significance of words and to find similar documents in a collection." A *corpus* is "a large set of reference documents."

# Examples

**Example 1** ("The Significance of a Word..."): If the word *socket* occurs five times in a 100-word document, its TF is 5%. If *socket* occurs in 1% of the corpus, the 5% local frequency is "highly significant," making *socket* a good keyword; a 1% local frequency would match the corpus and carry little significance.

## Worked Example

From "The Significance of a Word...": a corpus of 1,000 documents, with the word *orange* in 25 of them.

1. IDF of *orange* = `log(1000/26)` ≈ 1.58.
2. If *orange* occurs 10 times in a 100-word document, TF = 10/100 = 0.1.
3. TF*IDF weight = 0.1 × 1.58 = 0.158.

# Relationships

## Builds Upon
- This is a foundational text-analysis card; it builds on no other concept card.

## Enables
- **Cosine similarity** — Cosine similarity is computed over the TF*IDF keyword vectors of two documents.

## Related
- **Cosine similarity** — Uses TF*IDF weight vectors as its input.
- **Faceted search** — Another query technique over the same parsed mail corpus.

## Contrasts With
- This concept has no direct contrast within the chapter.

# Common Errors

- **Error**: Computing TF without dividing by document length.
  **Correction**: TF is occurrences ÷ total words in the document, not a raw count.

- **Error**: Computing IDF per document instead of over the whole corpus.
  **Correction**: IDF depends on `Tot` and `N` across the corpus; it is a single corpus-wide pass.

# Common Confusions

- **Confusion**: Thinking a frequently occurring word is automatically significant.
  **Clarification**: A word frequent across the whole corpus has low IDF; significance comes from being frequent *here* but rare in the corpus.

# Source Reference

Chapter 27: Sherlock's Last Case, Section "Adding Keywords to the Postings," subsection "The Significance of a Word: The TF*IDF Weight."

# Verification Notes

- Definition source: Direct quote of the TF, IDF, and TF*IDF definitions from the source.
- Confidence rationale: HIGH — the source defines each term precisely and gives a numeric worked example.
- Uncertainties: The source writes IDF as `log(Tot/N+1)`; the parenthesization in the book's text is ambiguous but the worked example uses `log(1000/26)`, reproduced faithfully here.
- Cross-reference status: Verified concept names exist or are planned.
- Re-extraction notes: Fresh extraction; no pre-existing card.
