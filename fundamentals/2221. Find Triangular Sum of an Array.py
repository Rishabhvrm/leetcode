from typing import List
class Solution:
    '''
    TC: O(N ^ 2)
    SC: O(N)
    '''
    def triangularSum(self, nums: List[int]) -> int:
        
        def perform_opr(new_ls: List[int]) -> List[int]:
            res = []
            for i in range(len(new_ls) - 1):
                res.append((new_ls[i] + new_ls[i + 1]) % 10)
            
            return res

        new_nums = nums
        while len(new_nums) > 1:
            new_nums = perform_opr(new_nums)

        return new_nums[0]

        # same as above but concise
        while len(nums) > 1:
            new_nums = []
            for i in range(len(nums) - 1):
                new_nums.append((nums[i] + nums[i + 1]) % 10)
            nums = new_nums
        return nums[0]

    '''
    TC: O(N ^ 2)
    SC: O(1)
    '''
    def triangularSum(self, nums: List[int]) -> int:
        n = len(nums)

        for last_idx in range(n, 1, -1):
            for i in range(last_idx - 1):
                nums[i] = ((nums[i] + nums[i + 1]) % 10)
        
        return nums[0]