from typing import List
class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        num_set = set()
        output = []
        for n in nums:
            if n in num_set:
                output.append(n)             # add duplicate elements to the output list
            else:
                num_set.add(n)

        return output
    
    # https://leetcode.com/problems/find-all-duplicates-in-an-array/description/
