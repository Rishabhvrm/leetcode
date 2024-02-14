from typing import List

class Solution:
    '''
    APPROACH-1: Brute Force
    TIME: O(N ^ 2)
    SPACE: O(1)
    '''
    def productExceptSelf(self, nums: List[int]) -> List[int]: 
        res, n = [], len(nums)

        for i in range(n):
            product = 1
            for j in range(n):
                if i != j: product *= nums[j]
            res.append(product)

        return res
    
    '''
    APPROACH-2: calculate right and left products for each element in array
    T(N): O(N)
    SPACE: O(N)
    '''
    def productExceptSelf(nums):
        n = len(nums)
        left_product, right_product = 1, 1

        # initialize arrays
        prefix, suffix = [1] * n, [1] * n

        # calculate and store left products in prefix
        for i in range(n):
            prefix[i] = left_product
            left_product *= nums[i]

        # calculate and store right products in suffix
        for i in range(n-1, -1, -1):
            suffix[i] = right_product
            right_product *= nums[i]
        
        # use prefix and suffix to calculate result
        return [prefix[i] * suffix[i] for i in range(n)]