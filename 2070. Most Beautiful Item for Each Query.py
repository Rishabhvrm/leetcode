from typing import List
class Solution:
    '''
    items =     [[1,2],[3,2],[2,4],[5,6],[3,5]]
    items =     [[1,2],[2,4],[3,2],[3,5],[5,6]]
    queries =    [1,2,3,4,5,6]
    ans =        [2,4,5,5,6,6]
    '''

    '''
    Approach: Sort then find the target price and max beauty one by one
    TLE 33/35
    '''
    def maximumBeauty(self, items: List[List[int]], queries: List[int]) -> List[int]:
        items = sorted(items, key = lambda x: (x[0], -x[1]))
        res = []

        for q in queries:
            res_b = 0

            for p, b in items:
                if p <= q:
                    res_b = max(res_b, b)
                    
            res.append(res_b)
        
        return res

    '''
    Approach: Binary Search to find the target price for a given q
    once the target price is found then find the max beauty one by one (can improve this step)
    find the max beauty in single step
    '''
    def maximumBeauty(self, items: List[List[int]], queries: List[int]) -> List[int]:

        # binary search
        def find_max_beauty(target):
            l, r = 0, len(items) - 1
            max_beauty = 0

            while l <= r:
                mid = l + (r - l) // 2
                
                if items[mid][0] <= target:
                    max_beauty = max(max_beauty, items[mid][1])
                    l = mid + 1
                elif target < items[mid][0]:
                    r = mid - 1
            
            return max_beauty


        items = sorted(items, key = lambda x: (x[0], x[1]))
        res = []
        max_beauty_so_far = 0

        # update items array with max_beauty so far
        for i in range(len(items)):
            max_beauty_so_far = max(max_beauty_so_far, items[i][1])
            items[i][1] = max_beauty_so_far

        # find target using binary search
        for q in queries:
            res.append(find_max_beauty(q))

        return res                
                
