from typing import List
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        # return sorted(nums)
    
        def merge(left_half, right_half):
            merged_arr = []
            i, j = 0, 0

            while i < len(left_half) and j < len(right_half):
                if left_half[i] <= right_half[j]:
                    merged_arr.append(left_half[i])
                    i += 1
                else:
                    merged_arr.append(right_half[j])
                    j += 1

            # adding remaining values
            merged_arr.extend(left_half[i:])
            merged_arr.extend(right_half[j:])
            return merged_arr


        # base case 
        if not nums: return
        if len(nums) <= 1: return nums

        mid = len(nums) // 2
        left_half = self.sortArray(nums[:mid])
        right_half = self.sortArray(nums[mid:])

        return merge(left_half, right_half)
    
s = Solution()
print(s.sortArray([5,2,3,1]))