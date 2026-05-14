# Development Log – The Torchbearer

**Student Name:** Amina Benothmane
**Student ID:** 132110911

---

## Entry 1 – [5/11/2026]: Initial Plan


I plan to implement the data structures that will hold the visited and non-visited nodes first, and then the algorithm that will traverse the nodes. I plan to keep
track of minimum cost as I traverse the nodes, visited nodes, unvisited nodes, and previous nodes in the algorithm to deduce the best path. I am anticipating that the 
part that will be most difficult is figuring out how I am going to keep track of previous nodes so that I can backtrack once they are all visited. I plan to test by printing
output at different stages to keep track of the operations.

---

## Entry 2 – [5/12/2026]: [Wrong assumption on Part Two]

I had a difficult time with run_dijkstra's. At first I misunderstood the instructions and thought I just had to return the minimum distances for the nearest nodes and mark unreachable nodes from the source node as infinity. I then figured out it was to be executed like how we did in previous assignments with a minheap or priority queue. I tested using the IDE debugger and a hypothetical graph to make sure the method worked as intended once I figured things out. 
---

## Entry 3 – [5-13-2026]: [Part 4 is finished so far]

Writing out the precompute_distance method went smoother than I expected. Part three and four were completed and helped exercise my understanding of the topic. 

---

## Entry 4 – [5-14-2026]: Post-Implementation Reflection

> Required. Written after your implementation is complete. Describe what you would
> change or improve given more time.

-Given more time, I would add more safeguards to my implementation. As it is now it passes the tests in torchbearer.py, but I can imagine there might be
some instance I did not predict where an error would occur. Another thing I could improve on if given more time would be to account for the possibility of a negative cost that would subtract and 
not add to the total cost when added. 

---

## Final Entry – [Date]: Time Estimate

| Part | Estimated Hours |
|---|---|
| Part 1: Problem Analysis |15 minutes|
| Part 2: Precomputation Design |5 hours|
| Part 3: Algorithm Correctness |20 minutes|
| Part 4: Search Design | 15 minutes|
| Part 5: State and Search Space |5 hours (Accounts for part 5+6, I did them together since they both were in _explore and find_optimal_route)|
| Part 6: Pruning |5 hours|
| Part 7: Implementation | 15 minutes |
| README and DEVLOG writing | 15 minutes|
| **Total** | ~ 11 hours and 20 minutes|
