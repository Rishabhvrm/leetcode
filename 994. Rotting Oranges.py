from typing import List
from collections import deque
class Solution:
    '''
    [
        [2,1,1],
        [0,1,1],
        [1,0,1]
    ]
    [0,0] => 0

    [1]
    -1 only when there is/are fresh organe(s)


    what if there are more than one rotten O's are present at a given time
    how to do multiple BFS at the same time?

    (m * n) ^ 2
    '''
    # def orangesRotting(self, grid: List[List[int]]) -> int:
        
    #     # for every orange run a bfs to count how many steps does it take for it reach the rotten orange
    #     # max of that time would be the answer
    #     # if it never reaches the rotten orange, return -1
    #     ROWS, COLS = len(grid), len(grid[0])
    #     max_steps, steps_to_reach_rotten = 0, 0

    #     def bfs(row, col):
    #         visited = set()
    #         q = deque()
    #         visited.add((row, col))
    #         q.append((row, col))
    #         count = 0

    #         while q:
    #             level_size = len(q)
                
    #             for _ in range(level_size):
    #                 row, col = q.popleft()
    #                 if grid[row][col] == 2:
    #                     return count
                    
    #                 # check neighbors of curr_popped_ele
    #                 for dr, dc in [(1,0), (-1,0), (0,1), (0,-1)]:
    #                     new_row, new_col = row + dr, col + dc
    #                     # if not (new_row not in range(ROWS) or new_col not in range(COLS) or
    #                     #         (row, col) in visited or grid[new_row][new_col] in [0]):
    #                     #         visited.add((new_row, new_col))
    #                     #         q.append((new_row, new_col))
    #                     if new_row in range(ROWS) and new_col in range(COLS) and grid[new_row][new_col] != 0 and (new_row, new_col) not in visited:
    #                         visited.add((new_row, new_col))
    #                         q.append((new_row, new_col))
    #             count += 1
    #         return -1
                        

    #     for r in range(ROWS):
    #         for c in range(COLS):
    #             if grid[r][c] == 1:
    #                 if bfs(r,c) == -1:
    #                     return -1
    #                 else:
    #                     steps_to_reach_rotten = bfs(r,c)
    #                     max_steps = max(max_steps, steps_to_reach_rotten)
        
    #     return max_steps

    '''
    multiple BFS at the same time
        - add all the starting points to the Q
        - incrementing counter only after a complete level is done for all the starting points
    '''
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        ROWS, COLS = len(grid), len(grid[0])
        fresh_count, rotten_count, became_rotten, seconds = 0, 0, 0, 0
        Q = deque()
        visited = set()
        
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 2:
                    rotten_count += 1
                    Q.append((r, c))        # add all rotten orange cells
                    visited.add((r,c))
                elif grid[r][c] == 1:
                    fresh_count += 1

        # BFS
        while Q:
            curr_Q_len = len(Q)
            seconds += 1
            neighbors = [(0, 1), (1, 0), (0, -1), (-1, 0)]

            for _ in range(curr_Q_len):
                r, c = Q.popleft()

                for dr, dc in neighbors:
                    nr, nc = r + dr, c + dc
                    
                    # not an empty or rotten cell hence fresh
                    if (
                        (nr, nc) not in visited and
                        (0 <= nr < ROWS) and
                        (0 <= nc < COLS) and
                        grid[nr][nc] not in [0, 2]
                    ):
                        became_rotten += 1
                        grid[nr][nc] = 2
                        visited.add((nr, nc))
                        Q.append((nr, nc))

        if fresh_count != became_rotten:        # all the fresh couldn't become rotten
            return -1
        elif rotten_count == 0:                 # there was no rotten, 0 seconds elapsed
            return 0
        else:                                   # there was some rotten and all the fresh became rotten
            return seconds - 1
      