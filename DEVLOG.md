# Development Log – The Torchbearer

**Student Name:** Amina Benothmane
**Student ID:** 132110911

> Instructions: Write at least four dated entries. Required entry types are marked below.
> Two to five sentences per entry is sufficient. Write entries as you go, not all in one
> sitting. Graders check that entries reflect genuine work across multiple sessions.
> Delete all blockquotes before submitting.

---

## Entry 1 – [5/11/2026]: Initial Plan

> Required. Write this before writing any code. Describe your plan: what you will
> implement first, what parts you expect to be difficult, and how you plan to test.

I plan to implement the data structures that will hold the visited and non-visited nodes first, and then the algorithm that will traverse the nodes. I plan to keep
track of minimum cost as I traverse the nodes, visited nodes, unvisited nodes, and previous nodes in the algorithm to deduce the best path. I am anticipating that the 
part that will be most difficult is figuring out how I am going to keep track of previous nodes so that I can backtrack once they are all visited. I plan to test by printing
output at different stages to keep track of the operations.

---

## Entry 2 – [5/12/2026]: [Wrong assumption on Part Two]

> Required. At least one entry must describe a bug, wrong assumption, or design change
> you encountered. Describe what went wrong and how you resolved it.

I had a difficult time with run_dijkstra's. At first I misunderstood the instructions and thought I just had to return the minimum distances for the nearest nodes and mark unreachable nodes from the source node as infinity. I then figured out it was to be executed like how we did in previous assignments with a minheap or priority queue. I tested using the IDE debugger and a hypothetical graph to make sure the method worked as intended once I figured things out. 
---

## Entry 3 – [5-13-2026]: [Part 4 is finished so far]

Writing out the precompute_distance method went smoother than I expected. Part three and four were completed and helped exercise my understanding of the topic. 

---

## Entry 4 – [Date]: Post-Implementation Reflection

> Required. Written after your implementation is complete. Describe what you would
> change or improve given more time.

_Your entry here._

---

## Final Entry – [Date]: Time Estimate

> Required. Estimate minutes spent per part. Honesty is expected; accuracy is not graded.

| Part | Estimated Hours |
|---|---|
| Part 1: Problem Analysis |15 minutes|
| Part 2: Precomputation Design |5 hours|
| Part 3: Algorithm Correctness |20 minutes|
| Part 4: Search Design | 15 minutes|
| Part 5: State and Search Space |5 hours (Accounts for part 5+6, I did them together since they both were in _explore and find_optimal_route|
| Part 6: Pruning |5 hours|
| Part 7: Implementation | |
| README and DEVLOG writing | 15 minutes|
| **Total** | |
