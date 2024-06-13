from typing import List
class Solution:
    '''
     0 1 2
    [2 2 2]
    Approach: Bucket sort
    '''
    def sortColors(self, nums: List[int]) -> None:
        
        # handle case for len < 3
        occ = [0] * (max(nums) + 1)

        for n in nums:
            occ[n] += 1

        i, j = 0, 0
        while i < len(occ):
            counter = 0
            while counter < occ[i]:
                nums[j + counter] = i
                counter += 1

            j += counter
            i += 1
        

    '''
            j
        0 1 2 3 4 5
    [2,2,1,1,2,2]
            c
        
        i
        0 1 2
    [2 2 2]

        0
    [0]

        0
    [1 0 0]
    '''
    '''
    Approach: Partition with pivot, 2 passes
    '''
    def sortColors(self, nums: List[int]) -> None:
        left = 0
        for i in range(len(nums)):
            if nums[i] < 1:
                nums[i], nums[left] = nums[left], nums[i]
                left += 1

        right = len(nums) - 1
        for i in range(len(nums) - 1, -1 , -1):
            if nums[i] > 1:
                nums[i], nums[right] = nums[right], nums[i]
                right -= 1

    '''
    Approach: Partition with pivot, 1 pass
    '''
    def sortColors(self, nums: List[int]) -> None:
        
        def swap(a, b):
            nums[a], nums[b] = nums[b], nums[a]

        left, mid, right = 0, 0, len(nums) - 1

        while mid <= right:
            if nums[mid] == 0:
                swap(left, mid)
                mid += 1
                left += 1
            elif nums[mid] == 2:
                swap(mid, right)
                right -= 1
            else:
                mid += 1