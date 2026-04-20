---
# === CORE IDENTIFICATION ===
concept: Search Problem
slug: search-problem

# === CLASSIFICATION ===
category: application-architecture
subcategory: algorithms
tier: intermediate

# === PROVENANCE ===
source: "Eloquent JavaScript, 4th Edition"
source_slug: eloquent-js
authors: "Marijn Haverbeke"
chapter: "Project: A Robot"
chapter_number: 7
pdf_page: null
section: "Pathfinding"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - graph search
  - pathfinding

# === TYPED RELATIONSHIPS ===
prerequisites:
  - graph-data-structure
  - array
extends: []
related:
  - state-modeling
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is a search problem?"
  - "How does breadth-first search find shortest paths?"
---

# Quick Definition
A search problem involves finding a valid solution (such as a route through a graph) by systematically exploring possibilities, since the solution cannot be directly computed.

# Core Definition
Haverbeke explains: "The problem of finding a route through a graph is a typical *search problem*. We can tell whether a given solution (a route) is valid, but we can't directly compute the solution the way we could for 2 + 2. Instead, we have to keep creating potential solutions until we find one that works." (Ch 7, "Pathfinding")

# Prerequisites
- **Graph data structure**: Search operates on a graph of nodes and edges
- **Arrays**: Work lists and routes are stored as arrays

# Key Properties
1. Cannot directly compute the answer; must explore possibilities
2. Breadth-first search explores short routes before longer ones
3. Uses a work list to track positions to explore
4. Avoids revisiting explored positions
5. The first solution found by BFS is guaranteed to be shortest

# Construction / Recognition
```javascript
function findRoute(graph, from, to) {
  let work = [{at: from, route: []}];
  for (let i = 0; i < work.length; i++) {
    let {at, route} = work[i];
    for (let place of graph[at]) {
      if (place == to) return route.concat(place);
      if (!work.some(w => w.at == place)) {
        work.push({at: place, route: route.concat(place)});
      }
    }
  }
}
```

# Context & Application
Search problems appear in routing, AI planning, puzzle solving, and any domain where you need to find a path from an initial state to a goal state.

# Examples
```javascript
function findRoute(graph, from, to) {
  let work = [{at: from, route: []}];
  for (let i = 0; i < work.length; i++) {
    let {at, route} = work[i];
    for (let place of graph[at]) {
      if (place == to) return route.concat(place);
      if (!work.some(w => w.at == place)) {
        work.push({at: place, route: route.concat(place)});
      }
    }
  }
}
```
The function "grows" routes from the start, exploring every reachable place that hasn't been visited yet, until a route reaches the goal. (Ch 7, "Pathfinding", lines 458-471)

# Relationships
## Builds Upon
- graph-data-structure, array
## Enables
- Pathfinding, route planning, optimization
## Related
- state-modeling
## Contrasts With
- N/A

# Common Errors
- **Error**: Exploring depth-first instead of breadth-first when shortest path is needed
  **Correction**: Use breadth-first search (explore shortest routes first) to guarantee finding the shortest path

# Common Confusions
- **Confusion**: All search problems require complex algorithms
  **Clarification**: For small, connected graphs, simple breadth-first search with a work list is sufficient

# Source Reference
Chapter 7: Project: A Robot, Section "Pathfinding", lines 416-509.

# Verification Notes
- Definition source: direct
- Confidence rationale: Explicitly defined with full implementation
- Cross-reference status: verified
