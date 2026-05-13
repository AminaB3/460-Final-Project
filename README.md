# The Torchbearer

**Student Name:** Amina Benothmane
**Student ID:** 132110911
**Course:** CS 460 – Algorithms | Spring 2026

## Part 1: Problem Analysis


- **Why a single shortest-path run from S is not enough:**
  - A single shortest-path run to make decisions is not enough as it only accounts for the cost locally between nodes and not the overall cost of the path. 

- **What decision remains after all inter-location costs are known:**
  - The structual decision that remains after all inter-location costs are known is what is the shortest path to take to the goal node T. 

- **Why this requires a search over orders (one sentence):**
  - A search over orders will calculate the best possible shortest path over all possibilities rather than deciding at each node individually. 

---

## Part 2: Precomputation Design

### Part 2a: Source Selection

| Source Node Type | Why it is a source |
|---|---|
| S | The torchbearer begins at this fixed entrance node where the Dijkstra's Algorithm is initially executed|
| M (B, C, D) | The torchbearer cannot go directly to the goal node, and must execute Dijkstra's algorthm between relics to eventually reach T |

### Part 2b: Distance Storage

| Property | Your answer |
|---|---|
| Data structure name | dungeon_map |
| What the keys represent | Each key represents a node, ex. the key would be assigned to 'S' |
| What the values represent | list[tuple[node, int]] represents a list of neighboring nodes and their costs from the current node|
| Lookup time complexity | O(n)|
| Why O(1) lookup is possible | The usage of a dictionary allows direct mapping to the node's neighboring cost through the key|

### Part 2c: Precomputation Complexity

> State the total complexity and show the arithmetic. Two to three lines max.

- **Number of Dijkstra runs:** The number of Dijkstra's runs is equal to the number of sources k 
- **Cost per run:** (n+m)log(m)
- **Total complexity:** k * (n+m)log(m)
- **Justification (one line):** The time complexity for each call to run_dijkstra is complexity (n+m)log(m) multiplied by the number of runs we make.

---

## Part 3: Algorithm Correctness

> Document your understanding of why Dijkstra produces correct distances.
> Bullet points and short sentences throughout. No paragraphs.

### Part 3a: What the Invariant Means

> Two bullets: one for finalized nodes, one for non-finalized nodes.
> Do not copy the invariant text from the spec.

- **For nodes already finalized (in S):**
  _Your answer here._

- **For nodes not yet finalized (not in S):**
  _Your answer here._

### Part 3b: Why Each Phase Holds

> One to two bullets per phase. Maintenance must mention nonnegative edge weights.

- **Initialization : why the invariant holds before iteration 1:**
  _Your answer here._

- **Maintenance : why finalizing the min-dist node is always correct:**
  _Your answer here._

- **Termination : what the invariant guarantees when the algorithm ends:**
  _Your answer here._

### Part 3c: Why This Matters for the Route Planner

> One sentence connecting correct distances to correct routing decisions.

_Your answer here._

---

## Part 4: Search Design

### Why Greedy Fails

> State the failure mode. Then give a concrete counter-example using specific node names
> or costs (you may use the illustration example from the spec). Three to five bullets.

- **The failure mode:** _Your answer here._
- **Counter-example setup:** _Your answer here._
- **What greedy picks:** _Your answer here._
- **What optimal picks:** _Your answer here._
- **Why greedy loses:** _Your answer here._

### What the Algorithm Must Explore

> One bullet. Must use the word "order."

- _Your answer here._

---

## Part 5: State and Search Space

### Part 5a: State Representation

> Document the three components of your search state as a table.
> Variable names here must match exactly what you use in torchbearer.py.

| Component | Variable name in code | Data type | Description |
|---|---|---|---|
| Current location | | | |
| Relics already collected | | | |
| Fuel cost so far | | | |

### Part 5b: Data Structure for Visited Relics

> Fill in the table.

| Property | Your answer |
|---|---|
| Data structure chosen | |
| Operation: check if relic already collected | Time complexity: |
| Operation: mark a relic as collected | Time complexity: |
| Operation: unmark a relic (backtrack) | Time complexity: |
| Why this structure fits | |

### Part 5c: Worst-Case Search Space

> Two bullets.

- **Worst-case number of orders considered:** _Your answer (in terms of k)._
- **Why:** _One-line justification._

---

## Part 6: Pruning

### Part 6a: Best-So-Far Tracking

> Three bullets.

- **What is tracked:** _Your answer here._
- **When it is used:** _Your answer here._
- **What it allows the algorithm to skip:** _Your answer here._

### Part 6b: Lower Bound Estimation

> Three bullets.

- **What information is available at the current state:** _Your answer here._
- **What the lower bound accounts for:** _Your answer here._
- **Why it never overestimates:** _Your answer here._

### Part 6c: Pruning Correctness

> One to two bullets. Explain why pruning is safe.

- _Your answer here._

---

## References

> Bullet list. If none beyond lecture notes, write that.

- _Your references here._
