from typing import List
# https://leetcode.com/problems/apple-redistribution-into-boxes/
class Solution:
    '''
    APPROACH: Greedy
    Put apples in largest container first, and decrement total apple count
    (calculate total apple count)
    (reverse sort the capacity array)
    TIME: O(N * log N), sorting
    SPACE: O(1)
    constraints: capacity can't go beyond total apples
    '''
    def minimumBoxes(self, apple: List[int], capacity: List[int]) -> int:
        total_apples = sum(apple)

        capacity.sort(reverse=True)
        for i,c in enumerate(capacity):
            # check if we're out of apples
            if total_apples <= 0: 
                return i
            # put apples into box and decrement total apple count
            total_apples -= c
        
        # need to use all boxes
        return len(capacity)
