class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        l = len(nums)
        
        ## BRUTE FORCE
        ## T(N): O(N * N)
        ## SPACE: CONSTANT

        # for i in range(l):
        #     for j in range(i+1,l):
        #         if nums[j] == target - nums[i]:
        #             return [i,j]
        # return [] # no solution found

        ## USING HASHMAP/DICTIONARY

        prevMap = {} # val : idx

        for idx, ele in enumerate(nums):
            
            # check if second number exist in dict
            # if yes, return idx for both numbers
            if (target - ele) in prevMap:
                return [prevMap[target - ele], idx]

            # else add ele : idx to dictionary
            prevMap[ele] = idx
        
        return   # no solution