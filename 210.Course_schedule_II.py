from typing import List
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        ## APPROACH: TOPOLOGICAL SORT
        ## TIME: O(E + V) = O(prereqs + courses)
        ## SPACE: O(n), output array
        
        def dfs(course):
            # to detect cycle
            if course in cycle: return False
            # already visited/crossed out, no need to visit again
            if course in visit: return True

            cycle.add(course)

            for pre in prereq_map[course]:
                if not dfs(pre): return False
            
            cycle.remove(course)
            visit.add(course)
            output.append(course)
            return True
        
        # make adjacency list to map prereqs
        prereq_map = { c:[] for c in range(numCourses) }

        for course, prereq in prerequisites:
            prereq_map[course].append(prereq)

        # a course has 3 possible states:
        # visited -> crs has been added to output
        # visiting -> crs not added to output, but added to cycle
        # unvisited -> crs not added to output or cycle

        output = []
        visit, cycle = set(), set()

        for course in range(numCourses):
            if not dfs(course): return []

        return output
        
        

numCourses = 2
prerequisites = [[1,0]]
obj = Solution()
print(obj.findOrder(numCourses, prerequisites))
