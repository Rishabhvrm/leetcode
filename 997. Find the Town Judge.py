from typing import List
class Solution:
    '''
    APPROACH: graph, edge direction represents trust
    create indegree(# of edegs entering a node) 
    and outdegree(# of edges going out from a node) arrays
    town-judge node will have other nodes pointing to it, 
    and no edge will go out from it (t-j trusts no one)
    TIME: O(N)
    SPACE: O(N)
    '''
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        if n == 1: return 1
        # if indegree of a node is (n-1) and 
        # outdegree of a node is 0 then it's a town judge
        indegree = [0 for _ in range(n + 1)] 
        outdegree = [0 for _ in range(n + 1)] 

        for a,b in trust:
            outdegree[a] += 1
            indegree[b] += 1

        for i in range(n + 1):
            if outdegree[i] == 0 and indegree[i] == n - 1: return i
        return -1