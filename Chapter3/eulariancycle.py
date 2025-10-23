
'''
Input: The adjacency list of an Eulerian directed graph.
Output: An Eulerian cycle in this graph.
'''

# Insert your eulerian_cycle function here, along with any subroutines you need
# g[u] is the list of neighbors of the vertex u

def find_cycle(start: int, g: Dict[int, List[int]]) -> Iterable[int]:
    cycle = []
    stack = []
    stack.append(start)

    while stack:
        currNode = stack[-1]
        if g[currNode]:
            stack.append(g[currNode][-1]) # add last element in list 
            g[currNode].pop()
        else:
            cycle.append(currNode)
            stack.pop()
    return cycle[::-1]
def eulerian_cycle(g: Dict[int, List[int]]) -> Iterable[int]:
    """Constructs an Eulerian cycle in a graph."""
    start = len(g) - 1
    cycle = find_cycle(start,g)
    return cycle