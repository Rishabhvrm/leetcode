class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        # recursive
        '''if target not in nums:
            return -1

        l = len(nums)

        # recursive solution
        # if len is even
        if l % 2 == 0:
            # target is in first half
            if nums[l//2 - 1] > target:                 
                return self.search(nums[:l//2], target)

            # target is in second half
            else:                                       
                return l//2 + self.search(nums[l//2:], target)

        # if len is odd
        else:
            # middle element is target
            if nums[l//2] == target:
                return l//2
            
            # target is in first half
            if nums[l//2] > target:                     
                return self.search(nums[:l//2], target)
            
            # target is in second half    
            else:                                       
                return l//2 + self.search(nums[l//2:], target)
'''

        # two pointers
        l = 0
        r = len(nums) - 1

        while l<=r:
            # find middle index
            mid = (l+r)//2
                
            # return if mid == target
            if nums[mid] == target:
                return mid
            
            # update l or r accordingly
            elif nums[mid] > target:
                r = mid - 1 
            elif nums[mid] < target:
                l = mid + 1

        return -1