from typing import List
class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:

        ## BRUTE FORCE: visit each cell and do some dfs/bfs 
        ## and see if you can visit both oceans


        ## BETTER WAY: 
        ## TIME: O(n * m)
        # find out all the cells that can reach pacific ocean and mark them
        # find out all the cells that can reach atlantic ocean and mark them
        # traverse the whole grid and pick cells that can reach both
        ROWS, COLS = len(heights), len(heights[0])
        pac, atl = set(), set()

        # collect all reachable cells in visit sets (pac, atl)
        def dfs(r, c, visit, prev_height):
            if ((r, c) in visit or
                r < 0 or c < 0 or
                r == ROWS or c == COLS or
                prev_height > heights[r][c]):
                return
            
            # add (r, c) to set (can be atl or pac)
            visit.add((r, c))

            # check neighbouring cells of current cell
            directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
            for x, y in directions:
                new_row, new_col = r + x, c + y
                dfs(new_row, new_col, visit, heights[r][c])
            

        # dfs for every col in top row and bottom row
        for c in range(COLS):
            # top row touches pacific
            dfs(0, c, pac, heights[0][c])
            # bottom row touches atlantic
            dfs(ROWS - 1, c, atl, heights[ROWS - 1][c])

        # dfs for every row in first col and last col
        for r in range(ROWS):
            # first col touches pacific
            dfs(r, 0, pac, heights[r][0])
            # last col touches atlantic
            dfs(r, COLS - 1, atl, heights[r][COLS - 1])

        res = []
        # find common cells btw two ocean sets
        for r in range(ROWS):
            for c in range(COLS):
                if (r, c) in pac and (r, c) in atl:
                    res.append([r,c])

        return res

heights = [[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]
obj = Solution()
print(obj.pacificAtlantic(heights))