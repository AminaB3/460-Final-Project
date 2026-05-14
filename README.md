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
  -The distance computed so far from the source node through nodes in S is the finalized minimum distance.

- **For nodes not yet finalized (not in S):**
  -The distance computed so far from the source node through nodes in S is the known minimum distance.

### Part 3b: Why Each Phase Holds

> One to two bullets per phase. Maintenance must mention nonnegative edge weights.

- **Initialization : why the invariant holds before iteration 1:**
  -The source node is initialized to zero, while all other nodes are initialized to infinity. Zero is smaller than infinity, and is therefore the
  min distance before iteration 1, therefore the invariant holds.

- **Maintenance : why finalizing the min-dist node is always correct:**
  -The min-dist node is always correct because up until that point, the smaller edgeweights were chosen to computer the minimum distance from source.
  -Any other node added to the computation will only increase the minimum distance, especially since all nodes are non-negative.

- **Termination : what the invariant guarantees when the algorithm ends:**
  -The invariant guarantees the minimum distance when the algorithm ends.

### Part 3c: Why This Matters for the Route Planner

> One sentence connecting correct distances to correct routing decisions.

-The torchbearer wants to make its way to the goal as quickly as possible before the torch runs out. Knowing the correct minimum distance will stop it
from making costly wrong turns, and make it in time to the goal. 

---

## Part 4: Search Design

### Why Greedy Fails

- **The failure mode:** -Greedy is the failure mode. 
- **Counter-example setup:** -A counter example is a hypothetical path A -> B with a cost of one, A-> C with a cost of 5, B->D with a cost of 30, and C->D with a cost of 4. D is the goal node.
- **What greedy picks:** -The greedy algorithm would choose the smallest path from A to node B, with a cost of one. When it goes from B to D however, it racks up a cost of 31. 
- **What optimal picks:** The optimal path would choose A to C with a cost of five, so that it can take the route from C to D with a cost of 4. The overall cost would be 9. 
- **Why greedy loses:** It fails to account for future paths/costs and only weighs in on the cost of nodes within it's immediate vicinity. It chose A to B because it was the shortest path, when
it is overall the worst option to choose.


### What the Algorithm Must Explore


- The algorithm must explore the entirety of all possible nodes from the source to determine the most optimal path. From there it will return the order of nodes the torchbearer
must traverse through to reach the goal before the torch runs out. 

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
