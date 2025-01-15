'''
function reconstruct_path(cameFrom, current)
    total_path := {current}
    while current in cameFrom.Keys:
        current := cameFrom[current]
        total_path.prepend(current)
    return total_path

// A* finds a path from start to goal.
// h is the heuristic function. h(n) estimates the cost to reach goal from node n.
function A_Star(start, goal, h)
    // The set of discovered nodes that may need to be (re-)expanded.
    // Initially, only the start node is known.
    // This is usually implemented as a min-heap or priority queue rather than a hash-set.
    openSet := {start}

    // For node n, cameFrom[n] is the node immediately preceding it on the cheapest path from the start
    // to n currently known.
    cameFrom := an empty map

    // For node n, gScore[n] is the currently known cost of the cheapest path from start to n.
    gScore := map with default value of Infinity
    gScore[start] := 0

    // For node n, fScore[n] := gScore[n] + h(n). fScore[n] represents our current best guess as to
    // how cheap a path could be from start to finish if it goes through n.
    fScore := map with default value of Infinity
    fScore[start] := h(start)

    while openSet is not empty
        // This operation can occur in O(Log(N)) time if openSet is a min-heap or a priority queue
        current := the node in openSet having the lowest fScore[] value
        if current = goal
            return reconstruct_path(cameFrom, current)

        openSet.Remove(current)
        for each neighbor of current
            // d(current,neighbor) is the weight of the edge from current to neighbor
            // tentative_gScore is the distance from start to the neighbor through current
            tentative_gScore := gScore[current] + d(current, neighbor)
            if tentative_gScore < gScore[neighbor]
                // This path to neighbor is better than any previous one. Record it!
                cameFrom[neighbor] := current
                gScore[neighbor] := tentative_gScore
                fScore[neighbor] := tentative_gScore + h(neighbor)
                if neighbor not in openSet
                    openSet.add(neighbor)

    // Open set is empty but goal was never reached
    return failure
'''


from queue import PriorityQueue

G = {
    'biratnagar' : {'itahari' : 22, 'biratchowk' : 30, 'rangeli': 25},
    'itahari' : {'biratnagar' : 22, 'dharan' : 20, 'biratchowk' : 11},
    'dharan' : {'itahari' : 20},
    'biratchowk' : {'biratnagar' : 30, 'itahari' : 11, 'kanepokhari' :10},
    'rangeli' : {'biratnagar' : 25, 'kanepokhari' : 25, 'urlabari' : 40},
    'kanepokhari' : {'rangeli' : 25, 'biratchowk' : 10, 'urlabari' : 12},
    'urlabari' : {'rangeli' : 40, 'kanepokhari' : 12, 'damak' : 6},
    'damak' : {'urlabari' : 6}
}

h = {
    'biratnagar' : 46,
    'itahari' : 39,
    'dharan' : 41,
    'rangeli' : 28,
    'biratchowk' : 29,
    'kanepokhari' : 17,
    'urlabari' : 6,
    'damak' : 0
}

def aStar(G, h, start, goal):
    PQ = PriorityQueue()
    prev = dict()
    visited = set()

    # Enqueue the starting state into the queue
    # The entries in PQ are in the format (f-score, (state,g-score))
    PQ.put((0+h[start], (start, 0)))

    # Initialize the previous state of starting state to " "
    prev[start] = " "
    
    # Repeat until the PQ is not empty
    while(PQ.empty() == False):
        # Get the state with least f-score from the PQ
        outStateFScore , (outState, outStateGScore) = PQ.get()
        visited.add(outState)
        if outState == goal:
            return True, prev, outStateFScore
        for chimeki in G[outState]:
            if chimeki not in visited:
                chimekiGScore = outStateGScore + G[outState][chimeki]
                PQ.put((chimekiGScore+h[chimeki], (chimeki, chimekiGScore)))
                prev[chimeki] = outState
    return False, prev, -1

def reconstruct_path(G, previous, goal):
    key = goal
    path = key
    while previous[key] != " ":
        key = previous[key]
        path = key + " --> "+ path
    return path


start = 'biratnagar'
goal = 'damak'
goalFound, previous, goalFScore = aStar(G, h, start, goal)
if(goalFound):
    print(reconstruct_path(G, previous, goal))
    print(goalFScore)
else:
    print("NO SOLUTION!!")  