from typing import List

class Solution:
    def gridGame(self, grid: List[List[int]]) -> int:
        pre_row1, pre_row2 = grid[0].copy(), grid[1].copy()
        N = len(grid[0])

        for i in range(1, N):
            pre_row1[i] += pre_row1[i - 1]
            pre_row2[i] += pre_row2[i - 1]

        res = float('inf')
        for i in range(N):
            top_right = pre_row1[-1] - pre_row1[i]
            bottom_left = pre_row2[i - 1] if i > 0 else 0
            second_robo = max(top_right, bottom_left)
            res = min(res, second_robo)
        
        return res
