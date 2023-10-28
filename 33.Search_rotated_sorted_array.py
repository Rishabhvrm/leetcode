from typing import List
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        ## APPROACH: BINARY SEARCH
        ## TIME: O(log N)
        ## SPACE: O(1)
        
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = left + (right - left) // 2

            if nums[mid] == target:         # target found
                return mid
            
            # compare with a border value to pick a half
        
            # I've picked first half
            if nums[left] <= nums[mid]:
                # if target lies after middle or lesser than left most value
                # move the left pointer
                # else move the right pointer
                if target > nums[mid] or target < nums[left]:
                    left = mid + 1
                else:
                    right = mid - 1

            # else, I'm in second half
            else:
                # if target lies before middle or greater than right most value
                # move the right pointer
                # else move the left pointer
                if target < nums[mid] or target > nums[right]:
                    right = mid - 1
                else:
                    left = mid + 1

        return -1


        ## APPROACH 2
        # FIND THE SMALLEST/PIVOT ELEMENT (153. Find Min in sorted array)
        # FIND THE TARGET USING PIVOT AND BINARY SEARCH

        # def find_pivot_idx(nums):
        #     left, right = 0, len(nums) - 1

        #     while left < right:
        #         mid = left + (right - left) // 2
        #         if nums[mid] > nums[right]:
        #             left = mid + 1
        #         else:
        #             right = mid

        #     return left    # could return left as well
        
        # def binary_search(nums, target, left, right):
        #     while left <= right:
        #         mid = left + (right - left) // 2

        #         if nums[mid] == target:
        #             return mid
        #         elif nums[mid] > target:
        #             right = mid - 1
        #         else:
        #             left = mid + 1
        #     return -1

        # # code under main method
        # if not nums:
        #     return -1

        # if nums[0] <= nums[-1]:
        #     # Array is already sorted, use a standard binary search
        #     return binary_search(nums, target, 0, len(nums) - 1)
    
        # pivot_idx = find_pivot_idx(nums)
        # print(pivot_idx)
        
        # if target == nums[pivot_idx]: return pivot_idx

        # # target is towards the first half
        # if target > nums[0]:
        #     return binary_search(nums, target, 0, pivot_idx - 1)
        # # target would be towards the end of nums (or second half)
        # elif target < nums[0]:
        #     return binary_search(nums, target, pivot_idx, len(nums) - 1)



nums = [1,3]
target = 2

s = Solution()
print(s.search(nums, target))