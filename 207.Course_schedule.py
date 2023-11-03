from typing import List
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        ## APPROACH: DFS, ADJACENCY LIST
        ## NODE => courses
        ## EDGES => prereqs
        ## TIME: O(courses + prereq) => O(numCourses + len(prereq))

        def dfs(course):
            # base cases
            if course in visit_set: return False            # cycle detected
            if pre_map[course] == []: return True           # no prereq for this course

            visit_set.add(course)

            # recursively, check prereq for each course
            for prereq in pre_map[course]:
                # if prereq course can't be completed, return False       
                if not dfs(prereq): return False            

            # nothing goes bad
            visit_set.remove(course)
            pre_map[course] = []
            return True


        # map each course to its prereq lis
        pre_map = { i : [] for i in range(numCourses)}      # adjacency list
        for course, prereq in prerequisites:
            pre_map[course].append(prereq)

        # visit all courses along current DFS path, to detect cycles
        visit_set = set()

        for course in range(numCourses):
            # if any course returns False, return False
            if not dfs(course): return False           
        
        # nothing goes bad     
        return True

        
