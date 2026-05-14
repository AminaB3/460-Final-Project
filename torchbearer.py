"""
CS 460 – Algorithms: Final Programming Assignment
The Torchbearer

Student Name: Amina Benothmane
Student ID:   132110911

INSTRUCTIONS
------------
- Implement every function marked TODO.
- Do not change any function signature.
- Do not remove or rename required functions.
- You may add helper functions.
- Variable names in your code must match what you define in README Part 5a.
- The pruning safety comment inside _explore() is graded. Do not skip it.

Submit this file as: torchbearer.py
"""

import heapq
#from os import uname
#I'm using python on windows
from platform import uname


# =============================================================================
# PART 1
# =============================================================================

def explain_problem():

    TODO = """- **Why a single shortest-path run from S is not enough:**
  - A single shortest-path run to make decisions is not enough as it only accounts for the cost locally between nodes and not the overall cost of the path. 

- **What decision remains after all inter-location costs are known:**
  - The structual decision that remains after all inter-location costs are known is what is the shortest path to take to the goal node T. 

- **Why this requires a search over orders (one sentence):**
  - A search over orders will calculate the best possible shortest path over all possibilities rather than deciding at each node individually. 
    """
    return TODO


# =============================================================================
# PART 2
# =============================================================================

def select_sources(spawn, relics, exit_node):
    """
    Parameters
    ----------
    spawn : node
    relics : list[node]
    exit_node : node

    Returns
    -------
    list[node]
        No duplicates. Order does not matter.

    TODO
    """
    #List of spawn and relics
    if spawn not in relics: 
        sources = [spawn] + relics
    else:
        sources =  relics
    return sources

def run_dijkstra(graph, source):
    """
    Parameters
    ----------
    graph : dict[node, list[tuple[node, int]]]
        graph[u] = [(v, cost), ...]. All costs are nonnegative integers.
    source : node

    Returns
    -------
    dict[node, float]
        Minimum cost from source to every node in graph.
        Unreachable nodes map to float('inf').

    TODO
    """
    min_graph = dict()
    for key in graph: #Setting all nodes to an initial value of infinity unless it is the source node
        if key == source:
            min_graph[key] = 0
        else: 
            min_graph[key] = float('inf')

    min_heap = [(min_graph[source], source)] #Initialize min_heap
    heapq.heapify(min_heap) #Push source to min_heap

    while min_heap: #While there are items in the min heap
        weight, node = heapq.heappop(min_heap) #Pop node out of min_heap
        if weight > min_graph[node]:
            continue
        for neighbors, n_weights in graph[node]:
            if weight + n_weights < min_graph[neighbors]:
                min_graph[neighbors] = weight + n_weights
                heapq.heappush(min_heap, (min_graph[neighbors], neighbors))


    
    return min_graph

#Debugging lines for run_dijkstra :D
"""
import torchbearer as tb

g = {
    'S': [('B', 1), ('C', 2), ('D', 2)],
    'B': [('D', 1), ('T', 1)],
    'C': [('B', 1), ('T', 1)],
    'D': [('B', 1), ('C', 1)],
    'T': [],
}
print(tb.run_dijkstra(g, 'S'))
"""


def precompute_distances(graph, spawn, relics, exit_node):
    """
    Parameters
    ----------
    graph : dict[node, list[tuple[node, int]]]
    spawn : node
    relics : list[node]
    exit_node : node

    Returns
    -------
    dict[node, dict[node, float]]
        Nested structure supporting dist_table[u][v] lookups
        for every source u your design requires.

    TODO
    """
    dist_table = dict()
    for u in select_sources(spawn, relics, exit_node):
        dist_table[u] = run_dijkstra(graph, u)
    return dist_table


# =============================================================================
# PART 3
# =============================================================================

def dijkstra_invariant_check():
    """
    Returns
    -------
    str
        Your Part 3 README answers, written as a string.
        Must match what you wrote in README Part 3.
    """
    TODO = '''
    - **For nodes already finalized (in S):**
    -The distance computed so far from the source node through nodes in S is the finalized minimum distance.

    - **For nodes not yet finalized (not in S):**
    -The distance computed so far from the source node through nodes in S is the known minimum distance.
    
    - **Initialization : why the invariant holds before iteration 1:**
    -The source node is initialized to zero, while all other nodes are initialized to infinity. Zero is smaller than infinity, and is therefore the
    min distance before iteration 1, therefore the invariant holds.

    - **Maintenance : why finalizing the min-dist node is always correct:**
    -The min-dist node is always correct because up until that point, the smaller edgeweights were chosen to computer the minimum distance from source.
    -Any other node added to the computation will only increase the minimum distance, especially since all nodes are non-negative.

    - **Termination : what the invariant guarantees when the algorithm ends:**
    -The invariant guarantees the minimum distance when the algorithm ends.
    -The torchbearer wants to make its way to the goal as quickly as possible before the torch runs out. Knowing the correct minimum distance will stop it
    from making costly wrong turns, and make it in time to the goal. 
    '''

    return TODO


# =============================================================================
# PART 4
# =============================================================================

def explain_search():
    """
    Returns
    -------
    str
        Your Part 4 README answers, written as a string.
        Must match what you wrote in README Part 4.
    """
    TODO = """
        - **The failure mode:** -Greedy is the failure mode. 
        - **Counter-example setup:** -A counter example is a hypothetical path A -> B with a cost of one, A-> C with a cost of 5, B->D with a cost of 30, and C->D with a cost of 4. D is the goal node.
        - **What greedy picks:** -The greedy algorithm would choose the smallest path from A to node B, with a cost of one. When it goes from B to D however, it racks up a cost of 31. 
        - **What optimal picks:** The optimal path would choose A to C with a cost of five, so that it can take the route from C to D with a cost of 4. The overall cost would be 9. 
        - **Why greedy loses:** It fails to account for future paths/costs and only weighs in on the cost of nodes within it's immediate vicinity. It chose A to B because it was the shortest path, when
        it is overall the worst option to choose.
        - The algorithm must explore the entirety of all possible nodes from the source to determine the most optimal path. From there it will return the order of nodes the torchbearer
        must traverse through to reach the goal before the torch runs out. 
    """
   
    return TODO


# =============================================================================
# PARTS 5 + 6
# =============================================================================

def find_optimal_route(dist_table, spawn, relics, exit_node):
    """
    Parameters
    ----------
    dist_table : dict[node, dict[node, float]]
        Output of precompute_distances.
    spawn : node
    relics : list[node]
        Every node in this list must be visited at least once.
    exit_node : node
        The route must end here.

    Returns
    -------
    tuple[float, list[node]]
        (minimum_fuel_cost, ordered_relic_list)
        Returns (float('inf'), []) if no valid route exists.

    TODO
    """
    best: [float, list[str]] = [float("inf"), []]
    relics_remaining = list(relics)
    relics_visited_order = []
    cost_so_far = 0
    #I chose a list to hold the remaining relics 
    _explore(dist_table, spawn, relics_remaining, relics_visited_order, cost_so_far, exit_node, best)
    #Returns (float('inf'), []) if no valid route exists.
    if best[0] == float("inf"):
        return (float('inf'), [])
    return best[0], best[1]


def _explore(dist_table, current_loc, relics_remaining, relics_visited_order,
             cost_so_far, exit_node, best):
    """
    Recursive helper for find_optimal_route.

    Parameters
    ----------
    dist_table : dict[node, dict[node, float]]
    current_loc : node
    relics_remaining : collection
        Your chosen data structure from README Part 5b.
    relics_visited_order : list[node]
    cost_so_far : float
    exit_node : node
    best : list
        Mutable container for the best solution found so far.

    Returns
    -------
    None
        Updates best in place.

    TODO
    Implement: base case, pruning, recursive case, backtracking.

    REQUIRED: Add a 1-2 sentence comment near your pruning condition
    explaining why it is safe (cannot skip the optimal solution).
    This comment is graded.
    """
    #Pruning condition

    #The optimal solution is the one that will contain the lowest cost. Pruning the cost that is greater than the recorded best is safe and will not skip
    #the optimal solution
    if cost_so_far >= best[0]: #If the cost at this point is greater than or equal to the best cost, we want to disregard it
        return
    if current_loc not in dist_table: #If it does not exist in the dist_table
        return
    #Base cases
    if current_loc == exit_node and len(relics_remaining) == 0 #and cost_so_far < best[0]: #If current location is the exit node, return best cost and relics visited order
        cost_to_exit = dist_table[current_loc][exit_node]
        if cost_so_far + cost_to_exit < best[0]:
            best[0] = cost_so_far + cost_to_exit
            best[1] = list(relics_visited_order) + [exit_node]
        return



 #Recursive case
    for nxt, cost in dist_table[current_loc].items():
        if nxt == exit_node or nxt not in relics_remaining or cost == float('inf'):
            continue
        relics_visited_order.append(nxt)
        relics_remaining.remove(nxt)
        _explore(dist_table, nxt, relics_remaining, relics_visited_order, cost_so_far + cost, exit_node, best)
        #Backtracking
        relics_remaining.append(nxt)
        relics_visited_order.pop()

# =============================================================================
# PIPELINE
# =============================================================================

def solve(graph, spawn, relics, exit_node):
    """
    Parameters
    ----------
    graph : dict[node, list[tuple[node, int]]]
    spawn : node
    relics : list[node]
    exit_node : node

    Returns
    -------
    tuple[float, list[node]]
        (minimum_fuel_cost, ordered_relic_list)
        Returns (float('inf'), []) if no valid route exists.

    TODO
    """
    pass


# =============================================================================
# PROVIDED TESTS (do not modify)
# Graders will run additional tests beyond these.
# =============================================================================

def _run_tests():
    print("Running provided tests...")

    # Test 1: Spec illustration. Optimal cost = 4.
    graph_1 = {
        'S': [('B', 1), ('C', 2), ('D', 2)],
        'B': [('D', 1), ('T', 1)],
        'C': [('B', 1), ('T', 1)],
        'D': [('B', 1), ('C', 1)],
        'T': []
    }
    cost, order = solve(graph_1, 'S', ['B', 'C', 'D'], 'T')
    assert cost == 4, f"Test 1 FAILED: expected 4, got {cost}"
    print(f"  Test 1 passed  cost={cost}  order={order}")

    # Test 2: Single relic. Optimal cost = 5.
    graph_2 = {
        'S': [('R', 3)],
        'R': [('T', 2)],
        'T': []
    }
    cost, order = solve(graph_2, 'S', ['R'], 'T')
    assert cost == 5, f"Test 2 FAILED: expected 5, got {cost}"
    print(f"  Test 2 passed  cost={cost}  order={order}")

    # Test 3: No valid path to exit. Must return (inf, []).
    graph_3 = {
        'S': [('R', 1)],
        'R': [],
        'T': []
    }
    cost, order = solve(graph_3, 'S', ['R'], 'T')
    assert cost == float('inf'), f"Test 3 FAILED: expected inf, got {cost}"
    print(f"  Test 3 passed  cost={cost}")

    # Test 4: Relics reachable only through intermediate rooms.
    # Optimal cost = 6.
    graph_4 = {
        'S': [('X', 1)],
        'X': [('R1', 2), ('R2', 5)],
        'R1': [('Y', 1)],
        'Y': [('R2', 1)],
        'R2': [('T', 1)],
        'T': []
    }
    cost, order = solve(graph_4, 'S', ['R1', 'R2'], 'T')
    assert cost == 6, f"Test 4 FAILED: expected 6, got {cost}"
    print(f"  Test 4 passed  cost={cost}  order={order}")

    # Test 5: Explanation functions must return non-placeholder strings.
    for fn in [explain_problem, dijkstra_invariant_check, explain_search]:
        result = fn()
        assert isinstance(result, str) and result != "TODO" and len(result) > 20, \
            f"Test 5 FAILED: {fn.__name__} returned placeholder or empty string"
    print("  Test 5 passed  explanation functions are non-empty")

    print("\nAll provided tests passed.")


if __name__ == "__main__":
    _run_tests()
