from typing import List

class Solution:
    # def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
    #     ans = []

    #     nums = set()
    #     n = len(grid)

    #     for r in range(n):
    #         for c in range(n):
    #             if grid[r][c] in nums:
    #                 ans.append(grid[r][c])
    #             nums.add(grid[r][c])

    #     for i in range(1, (n ** 2) + 1):
    #         if i not in nums:
    #             ans.append(i)

    #     return ans

    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        nums = defaultdict(int)
        n = len(grid)

        for row in grid:
            for num in row:
                nums[num] += 1
        
        for i in range(1, (n ** 2) + 1):
            if nums[i] == 2:
                a = i
            elif nums[i] == 0:
                b = i
            
        return [a, b]