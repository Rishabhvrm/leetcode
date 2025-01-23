from typing import List
class Solution:
    '''

    1 0
    0 0

    seems like LC 200 Number of islands just count the 1's as well
    WRONG
    below is the example why it can't be LC 200
    isolated islands could be far apart
    they're still connected long as they are in same row or col
    '''
    '''
    1,0,0,1,0
    0,0,0,0,0
    0,0,0,1,0
    '''
    # def countServers(self, grid: List[List[int]]) -> int:
    #     # returns server count in this cluster
    #     def dfs(r, c) -> int:
    #         # out of bounds or visited
    #         if (
    #             r < 0 or r >= ROWS or
    #             c < 0 or c >= COLS or
    #             (r, c) in visited or 
    #             grid[r][c] == 0
    #         ):
    #             return 0

    #         s_cnt = 1
    #         visited.add((r, c))
    #         neighbors = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    #         for dr, dc in neighbors:
    #             nr, nc = r + dr, c + dc
    #             s_cnt += dfs(nr, nc)
                
    #         return s_cnt


    #     ROWS, COLS = len(grid), len(grid[0])
    #     visited = set()
    #     count = 0
    #     isolated = 0

    #     for r in range(ROWS):
    #         for c in range(COLS):
    #             if grid[r][c] and (r,c) not in visited:
    #                 servers = dfs(r, c)
    #                 if servers > 1:         # don't count isolated servers or empty cells
    #                     count += servers

    #     return count

    '''
    count the isolated servers and subtract from total servers count
    '''
    def countServers(self, grid: List[List[int]]) -> int:
        total_count, isolated = 0, 0
        ROWS, COLS = len(grid), len(grid[0])
        row_cnt, col_cnt = [0] * ROWS, [0] * COLS   # server count in each row and col

        # count total and fill up the row and col counts 
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c]:
                    total_count += 1
                    row_cnt[r] += 1
                    col_cnt[c] += 1

        # count isolated servers
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] and row_cnt[r] == 1 and col_cnt[c] == 1:
                    isolated += 1


        return total_count - isolated