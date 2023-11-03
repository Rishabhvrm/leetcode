from typing import List

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        # dfs
        def mark_island(r,c):
            # base case
            if grid[r][c] != "1": return
            # if grid[r][c] == "1":         # can use this as a base case too

            grid[r][c] = "-1"               # mark current element

            # check up, down, left, right position of current position
            directions = [(1,0), (-1,0), (0,1), (0,-1)]
            
            for x, y in directions:
                new_row, new_col = r + x, c + y
                if 0 <= new_row < ROWS and 0 <= new_col < COLS:
                    mark_island(new_row, new_col)

        ## APPROACH: 
        ## TIME: O(m * n) + (m * n), visit each cell at least once, worst case if all elements are 1
        ## SPACE: O(1)
        ROWS, COLS = len(grid), len(grid[0])
        count = 0

        # traverse each element
        for r in range(ROWS):
            for c in range(COLS):
                # if element is 1, traverse its neighbous and increase count
                if grid[r][c] == "1":
                    mark_island(r,c)
                    count += 1
        
        return count




grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]

grid2 = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]

obj = Solution()
print(obj.numIslands(grid))
print(obj.numIslands(grid2))
        