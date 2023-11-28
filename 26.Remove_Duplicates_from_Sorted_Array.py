from typing import List
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        ## uses in-built function
        ## slow
        '''
        i = 1
        while i < len(nums):
            if nums[i] == nums[i - 1]:
                nums.remove(nums[i])
                i -= 1
            i += 1

        return len(nums)
        '''

        '''
        nums[:] = sorted(set(nums))
        return len(nums)
        '''

        ## APPROACH: 2-POINTERS
        ## once a ele is seen, simply bypass its duplicates 
        ## and move on to the next unique element
        ## TIME: O( n )
        # j will point the next pos where a distinct val should be placed
        # i will traverse
        j = 1       
        for i in range(1, len(nums)):
            # if curr and prev vals don't match
            # a distinct ele is found
            # place it at j and increment j
            if nums[i] != nums[i - 1]:
                nums[j] = nums[i]
                j += 1

        return j

obj = Solution()
nums = [0,0,1,1,1,2,2,2,3,3,4]
print(obj.removeDuplicates(nums))


'''
two pointers
i will traverse
j will point to the next pos where a distinct val should be placed

traverse the list:
	if a distinct ele is found (i.e curr_ele != prev_ele):
		copy curr_val at j
		increment j
		
return j
'''