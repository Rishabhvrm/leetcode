from typing import List
class Solution:
    '''
    Degree Count
    Brute Force: make a connection array representing how many edges does a node connects to
    traverse it linearly and pick the idx where val is n-1
    T(N): O(N)
    Space: O(N)
    '''
    def findCenter(self, edges: List[List[int]]) -> int:
        N = len(edges)
        connections = [0 for _ in range(N + 2)]

        for x, y in edges:
            connections[x] += 1
            connections[y] += 1
        
        for i, c in enumerate(connections):
            if c == N:
                return i

        return -1

    '''
    Approach: Greedy, just check the common node btw edges.
    For simplicity, take any 2 edges, regardless of how big the graph is
    Center of the start appears in every edge
    This works bcz it's a star graph, every other node would degree 1, 
    and center would have degree n-1
    T(N): O(1)
    Space: O(1)
    '''
    def findCenter(self, edges: List[List[int]]) -> int:
        a, b = edges[0]
        return a if a in edges[1] else b


