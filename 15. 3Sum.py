from typing import List
class Solution:
    '''
    APPROACH: 2 Pointers, use concept of 2-SUM-II (start and end pointer, move according to sum and target)
    TIME: O(N * log N)
    SPACE: O(N), python takes extra space for sorting (temporarily though)
    '''
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        """
        Finds all unique triplets in the array that sum up to zero.

        :param nums: A list of integers representing the input array.
        :rtype: List[List[int]]
        :return: A list of lists containing unique triplets that sum up to zero.
        """
        n, target = len(nums) - 1, 0
        res = []
        
        nums.sort()                                                                     # sort to use 2 sum - II concepts of 2 pointers
        for idx in range(n-1):                                                          # traversing till last 3rd value, loop will run till (n-2). 1,2,3, ... , n-3, n-2, n-1, n
            if nums[idx] > 0:                                                           # skip if curr value is +ve, sum can't be 0 then
                continue
            if idx > 0 and nums[idx - 1] == nums[idx]:                                  # skip duplicates, make sure to skip the second duplicate not the first
                continue
            
            l, r = idx + 1, n
            while l < r:
                three_sum = nums[idx] + nums[l] + nums[r]
                if three_sum < target:                                                  # move toward right (bigger values)
                    l += 1                  
                elif target < three_sum:                                                # move toward left (smaller values)
                    r -= 1
                elif three_sum == target:                                               # if three_sum == 0    
                    res.append([nums[idx], nums[l], nums[r]])                           # add to result
                    l, r = l + 1, r - 1
                    while l < r and nums[l - 1] == nums[l]:                             # skip duplicates within the inner array, eg: [-2,-2,0,0,0,2,2]
                        l += 1
                    while l < r and nums[r + 1] == nums[r]:
                        r -= 1
        return res

    def threeSumRevisit(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        for i in range(len(nums) - 1):
            # to skip duplicates
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            l, r = i + 1, len(nums) - 1
            
            while l < r:
                three_sum = nums[i] + nums[l] + nums[r]

                if three_sum < 0:
                    l += 1
                elif three_sum > 0:
                    r -= 1
                elif three_sum == 0:
                    res.append([nums[i], nums[l], nums[r]])
                    l += 1
                    '''
                    to skip duplicates
                        #  l                    r
                    -4,-1,-1, -1, -1, -1, 0, 1, 2

                        #                 l     r
                    -4,-1,-1, -1, -1, -1, 0, 1, 2

                                          #  l  r
                    -4,-1,-1, -1, -1, -1, 0, 1, 2
                    '''
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1

        return res


    # slightly slower (if I remove the skip condition) bcz what if there A LOT of duplicates, 
    # it sure won't add it to the answer but still will traverse them
    def threeSumRevisitUsingTuples(self, nums: List[int]) -> List[List[int]]:
        res = set()
        nums.sort()

        for i in range(len(nums)):
            if i > 0 and nums[i - 1] == nums[i]:
                continue

            l, r = i + 1, len(nums) - 1

            while l < r:
                three_sum = nums[i] + nums[l] + nums[r]

                if three_sum < 0:
                    l += 1
                elif three_sum > 0:
                    r -= 1
                elif three_sum == 0:
                    res.add((nums[i], nums[l], nums[r]))
                    l += 1
        
        return [list(t) for t in res]        


    def test_threeSum(self):
        sol = Solution()

        # Test case 1: Regular case with multiple solutions
        nums1 = [-1, 0, 1, 2, -1, -4]
        assert sol.threeSum(nums1) == [[-1, -1, 2], [-1, 0, 1]], "Test case 1 failed"

        # Test case 2: No solution
        nums2 = [1, 2, 3, 4]
        assert sol.threeSum(nums2) == [], "Test case 2 failed"

        # Test case 3: All zeros
        nums3 = [0, 0, 0]
        assert sol.threeSum(nums3) == [[0, 0, 0]], "Test case 3 failed"

        # Test case 4: All positive numbers
        nums4 = [1, 2, 3, 4, 5]
        assert sol.threeSum(nums4) == [], "Test case 4 failed"

        # Test case 5: All negative numbers
        nums5 = [-5, -4, -3, -2, -1]
        assert sol.threeSum(nums5) == [], "Test case 5 failed"

        print("All test cases passed successfully!")

# Run the test cases
Solution().test_threeSum()