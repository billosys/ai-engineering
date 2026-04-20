---
# === CORE IDENTIFICATION ===
concept: Graph Data Structure
slug: graph-data-structure

# === CLASSIFICATION ===
category: application-architecture
subcategory: data-structures
tier: intermediate

# === PROVENANCE ===
source: "Eloquent JavaScript, 4th Edition"
source_slug: eloquent-js
authors: "Marijn Haverbeke"
chapter: "Project: A Robot"
chapter_number: 7
pdf_page: null
section: "Meadowfield"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - graph
  - network

# === TYPED RELATIONSHIPS ===
prerequisites:
  - object
  - array
extends: []
related:
  - persistent-data-structure
  - state-modeling
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is a graph data structure?"
  - "How can a graph be represented in JavaScript?"
---

# Quick Definition
A graph is a collection of points (nodes) with lines (edges) between them, commonly represented in JavaScript as an object mapping each node to an array of connected nodes.

# Core Definition
Haverbeke explains: "The network of roads in the village forms a *graph*. A graph is a collection of points (places in the village) with lines between them (roads). This graph will be the world that our robot moves through." (Ch 7, "Meadowfield")

# Prerequisites
- **Objects**: Graphs can be represented as objects mapping nodes to neighbors
- **Arrays**: Neighbor lists are stored as arrays

# Key Properties
1. Consists of nodes (vertices) and edges (connections)
2. In JavaScript, commonly represented as an adjacency list: an object mapping each node to its neighbors
3. Can be built from edge lists using a construction function
4. Edges can be directed or undirected (the example uses undirected edges)

# Construction / Recognition
```javascript
function buildGraph(edges) {
  let graph = Object.create(null);
  function addEdge(from, to) {
    if (from in graph) {
      graph[from].push(to);
    } else {
      graph[from] = [to];
    }
  }
  for (let [from, to] of edges.map(r => r.split("-"))) {
    addEdge(from, to);
    addEdge(to, from);
  }
  return graph;
}
```

# Context & Application
Graphs model relationships between entities: road networks, social connections, dependencies. The chapter uses a graph to represent a village's road network for a delivery robot to navigate.

# Examples
```javascript
const roads = [
  "Alice's House-Bob's House", "Alice's House-Cabin",
  "Alice's House-Post Office", "Bob's House-Town Hall",
  // ...
];
const roadGraph = buildGraph(roads);
```
The resulting `roadGraph` object maps each place name to an array of reachable places. (Ch 7, "Meadowfield", lines 50-94)

# Relationships
## Builds Upon
- object, array
## Enables
- pathfinding algorithms, state-modeling
## Related
- persistent-data-structure
## Contrasts With
- N/A

# Common Errors
- **Error**: Using a plain object as a graph without `Object.create(null)`
  **Correction**: Plain objects inherit from `Object.prototype`, which can cause spurious property lookups; use `Object.create(null)` for clean maps

# Common Confusions
- **Confusion**: Graphs require special libraries
  **Clarification**: Simple graphs can be represented with plain JavaScript objects and arrays

# Source Reference
Chapter 7: Project: A Robot, Section "Meadowfield", lines 65-94.

# Verification Notes
- Definition source: direct
- Confidence rationale: Explicitly defined with implementation
- Cross-reference status: verified against Ch 10 module design discussion
