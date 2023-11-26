from typing import List
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        
        ## APPROACH-1: use cloud boundary concept to move all vals to end of array
        ## TIME: O( n ), traversing backwards
        ## SPACE: O( 1 )
        '''
        n = len(nums)
        boundary, count = n - 1, 0

        for i in range(n - 1, -1 , -1):
            if nums[i] == val:
                nums[i], nums[boundary] = nums[boundary], nums[i]
                boundary -= 1 
                count += 1

        return n - count
        '''


        ## APPROACH-1: move all ele != val towards start of array
        ## TIME: O( n ), traversing forward
        ## SPACE: O( 1 )
        index = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[index] = nums[i]
                index += 1

        return index