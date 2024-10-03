from typing import List
class Solution:
    
    '''
    Approach: sort, store in map {val: idx}
    make result array by traversing the og list and finding its idx from map
    T(N): O(n log n)
    Space: O(n), map and sorted array
    '''
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        if not arr: return None
        if len(arr) == 1: return [1]
        
        sorted_arr = sorted(arr)
        ele_idx = {}

        unique_ele_count = 1
        for i in range(len(arr)):
            if i > 0 and sorted_arr[i - 1] != sorted_arr[i]:
                unique_ele_count += 1
            ele_idx[sorted_arr[i]] = unique_ele_count

        res = []
        for n in arr:
            res.append(ele_idx[n])

        return res

        # [37,12,28,9,100,56,80,5,12]
        # [5,9,12,12,28,37,56,80,100]
        # [1,2,3,  3, 4, 5, 6, 7, 8 ]

    '''
    Approach: same as above but deduplicating using set
    '''
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        sorted_arr = sorted(list(set(arr)))

        num_to_rank = {}

        for i in range(len(sorted_arr)):
            num_to_rank[sorted_arr[i]] = i + 1

        res = []
        for ele in arr:
            res.append(num_to_rank[ele])
        return res