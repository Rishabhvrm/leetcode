from typing import List
class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        if n == 1: return 1
        # if indegree of a node is (n-1) and 
        # outdegree of a node is 0 then it's a town judge
        indegree = [0 for _ in range(n+1)] 
        outdegree = [0 for _ in range(n+1)] 

        for a,b in trust:
            outdegree[a] += 1
            indegree[b] += 1

        for i in range(n+1):
            if outdegree[i] == 0 and indegree[i] == n-1: return i
        return -1