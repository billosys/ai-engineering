---
concept: Task Tree
slug: task-tree
category: concurrency
subcategory: null
tier: intermediate
source: "Async Reference"
source_slug: async-reference
authors: "Rust Async Working Group"
chapter: "Structured Concurrency"
chapter_number: 3
pdf_page: null
section: "Principles of structured concurrency"
extraction_confidence: high
aliases:
  - "tree-structured concurrency"
  - "concurrency tree"
  - "task hierarchy"
prerequisites:
  - structured-concurrency
extends:
  - structured-concurrency
related:
  - temporal-scope
  - cancellation-propagation
  - error-propagation-concurrency
  - nursery-pattern
contrasts_with: []
answers_questions:
  - "What is a task tree?"
  - "How are tasks organized in structured concurrency?"
---

# Quick Definition

A task tree is the hierarchical organization of concurrent tasks where each task (except the root main task) has a single parent, there are no cycles, and every child task must finish before its parent. This tree structure is the central invariant of structured concurrency.

# Core Definition

"The key idea of structured concurrency is that all tasks (or threads or whatever) are organized as a tree. I.e., each task (except the main task which is the root) has a single parent and there are no cycles of parents. A child task is started by its parent and must *always* finish executing before its parent. There are no constraints between siblings. The parent of a task may not change." (Async Reference, Ch. 3: Structured Concurrency, "Principles of structured concurrency")

# Prerequisites

- **Structured concurrency** -- the task tree is the central organizing structure of the structured concurrency philosophy; understanding why structured concurrency exists motivates the tree constraint

# Key Properties

1. Each task (except the main/root task) has exactly one parent
2. There are no cycles in the parent relationship
3. The main task is the root of the tree
4. A child task must always finish executing before its parent
5. The parent of a task may not change once established
6. There are no constraints between sibling tasks (they run concurrently)
7. A child task is started by its parent (though the source notes this is not a hard requirement if temporal scope is reified via an object)
8. If a task is live, all of its ancestor tasks must also be live

# Construction / Recognition

## To Construct a Task Tree:
1. Designate the main task as the root
2. For each new concurrent task, identify its parent (the task that spawns it)
3. Ensure each parent waits for all children to complete before returning
4. Never re-parent a task or create cycles
5. If a child task needs to spawn further subtasks, those become grandchildren in the tree

## To Verify the Tree Invariant:
1. Check that every task has exactly one parent (except root)
2. Verify no task outlives its parent
3. Confirm there are no orphaned tasks (tasks with no parent)
4. Verify the parent relationship contains no cycles

# Context & Application

The task tree provides the key reasoning property of structured concurrency: "if a task is live, then all of its ancestor tasks must also be live." While this does not guarantee ancestors are in a good state (they might be shutting down or handling an error), it guarantees they are running in some form. This means "for any task (except the root task), there is always a live task to send results or errors to."

The tree structure enables language-level error handling to span concurrent boundaries, and it enables reasoning about resource management across tasks -- because child tasks cannot outlive parents, resources owned by parents remain valid for the duration of child tasks.

The source references Yoshua Wuyts' blog post "Tree-structured concurrency" as additional reading on this topic.

# Examples

**Example 1** (Ch. 3, "Principles of structured concurrency"): The source describes the key reasoning benefit: "When reasoning about programs which implement structured concurrency, the key new fact is that if a task is live, then all of its ancestor tasks must also be live. [...] This means that for any task (except the root task), there is always a live task to send results or errors to."

**Example 2** (Ch. 3, footnote): The source notes an important nuance: "This [child started by parent] is not actually a hard requirement for structured concurrency. If the temporal scope of a task can be represented in the program and passed between tasks, then a child task can be started by one task but have another as its parent." This shows the tree relationship is about temporal scope, not just spawning.

# Relationships

## Builds Upon
- **structured-concurrency** -- the task tree is the implementation of the structured concurrency philosophy

## Enables
- **cancellation-propagation** -- cancellation must walk down the tree to all descendants
- **error-propagation-concurrency** -- errors flow up the tree to parent tasks
- **temporal-scope** -- the tree structure determines temporal relationships

## Related
- **nursery-pattern** -- nurseries manage the children at each node of the tree

## Contrasts With
- None explicitly -- the contrast is with the unstructured "bag of tasks" model (see unstructured-concurrency)

# Common Errors

- **Error**: Allowing a child task to outlive its parent by not awaiting it.
  **Correction**: Every parent must await all children before completing. Use join handles, join sets, or nursery patterns to enforce this.

- **Error**: Creating cycles by having tasks spawn each other as children.
  **Correction**: The parent relationship must form a tree (acyclic). If mutual communication is needed, use channels or shared state rather than parent-child spawning.

# Common Confusions

- **Confusion**: Thinking siblings in the task tree must execute in order.
  **Clarification**: "There are no constraints between siblings." Sibling tasks run concurrently; only the parent-child lifetime relationship is constrained.

- **Confusion**: Thinking the parent must be the task that spawns the child.
  **Clarification**: The source notes this is "not actually a hard requirement." If temporal scope is reified as an object (e.g., a nursery), a child can be started by one task but have another as its parent.

# Source Reference

Chapter 3: Structured Concurrency, "Principles of structured concurrency" section. The tree structure is defined in the opening paragraph and its properties are elaborated throughout. See also the "References" section citing Yoshua Wuyts' "Tree-structured concurrency" blog post.

# Verification Notes

- Definition source: Direct quotation from "Principles of structured concurrency" section, paragraph 1
- Key Properties: All from explicit statements in the same section
- Confidence rationale: HIGH -- the source explicitly defines the task tree as "the key idea of structured concurrency" with detailed properties
- Uncertainties: None for the definition
- Cross-reference status: All slugs reference cards in this extraction set
