from typing import List
class Solution:
    def average(self, salary: List[int]) -> float:
        
        ## TIME: O(n), but it's 3n, uses in-built functions
        '''
        return (sum(salary) - min(salary) - max(salary)) / (len(salary) - 2)
        '''

        ## TIME: O(n), faster than above bcz now it's only n not 3n
        ## now min and max is O(1) operation
        total_sal, min_sal, max_sal = 0, float(inf), float(-inf)
        
        for s in salary:
            # keep track of min and max sal
            min_sal, max_sal = min(min_sal, s), max(max_sal, s)
            total_sal += s
        
        total_sal = total_sal - min_sal - max_sal
        return total_sal/(len(salary) - 2)
        