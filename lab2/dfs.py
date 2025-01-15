G = {
    'Biratnagar': {
        'Itahari': 22,
        'Biratchowk': 30,
        'Rangeli': 25
    },
    'Itahari': {
        'Biratnagar': 22,
        'Dharan': 20,
        'Biratchowk': 11
    },
    'Dharan': {
        'Itahari': 20
    },
    'Biratchowk': {
        'Biratnagar': 30,
        'Itahari': 11,
        'Kanepokhari': 10
    },
    'Rangeli': {
        'Biratnagar': 25,
        'Kanepokhari': 25,
        'Urlabari': 40
    },
    'Kanepokhari': {
        'Biratchowk': 10,
        'Rangeli': 25,
        'Urlabari': 12
    },
    'Urlabari': {
        'Rangeli': 40,
        'Kanepokhari': 12,
        'Damak': 6
    },
    'Damak': {
        'Urlabari': 6
    },
}

Tree = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': ['G'],
    'E': ['H'],
    'F': [],
    'G': [],
    'H': []
}


'''
procedure DFS_iterative(G, v) is
    let S be a stack
    S.push(v)
    while S is not empty do
        v = S.pop()
        if v is not labeled as discovered then
            label v as discovered
            for all edges from v to w in G.adjacentEdges(v) do 
                S.push(w)
'''
def DFS_i(G, start, goal):
    stack = list()
    visited = set()
    prev = dict()   # key represent current node and value represent the previous node

    prev[start] = ""
    stack.append(start)

    while len(stack) != 0:
        node = stack.pop() 
        if node == goal:
            return True, prev
        visited.add(node)
        print(f'visited: {visited}')
        for neigh in G[node]:
            if neigh not in visited and neigh not in stack:
                prev[neigh] = node
                stack.append(neigh)
    return False, prev

def create_path(prev, start, goal):
    '''prev is a dictionary that stores nodes information
        key represent the current node and value presents the previous node (from which current node is visited)
       goal is the goal node of the graph'''
    key = goal
    path = goal
    while key != start:
        key = prev[key]
        path = key + '--> ' + path
    return path

def main():
    start = 'Itahari'
    goal = 'Damak'
    print(f'start: {start}  goal: {goal}')

    foundPath, prev = DFS_i(G, start, goal)
    print(f'prev ::  {prev}')
    if foundPath:
        path = create_path(prev, start, goal)
        print(f'path ::   {path}')