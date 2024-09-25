from typing import List
import math
class Solution:
    '''
    Approach: Build prefixes from arr1
    traverse arr2 and look for longest matching prefix in prefix set made in above step
    Time: O((m * log10(M)) + (n * log10(N))) 
    m: len of arr1, M: max # of digits in ele of arr1
    n: len of arr2, N: max # of digits in ele of arr2
    Space: O(m * log10(M))
    set (# of prefixes in arr1)
    '''
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        def digits_in_num(num):
            return math.floor(math.log10(num)) + 1
            # return len(str(num))

        prefixes = set()    # total possible prefixes

        # build prefixes from arr1
        for ele in arr1:
            while ele > 0 and ele not in prefixes:
                prefixes.add(ele)
                ele //= 10
        
        res_len = 0
        # find longest matching prefix in arr2
        for ele in arr2:
            while ele > 0 and ele not in prefixes:
                ele //= 10
            
            if ele > 0:     # it means ele is in prefixes
                res_len = max(res_len, digits_in_num(ele))

        return res_len