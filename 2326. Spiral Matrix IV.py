from typing import List


class Solution:
    '''
    4 loops
    '''
    def spiralMatrix(self, m: int, n: int, head: "ListNode") -> List[List[int]]:
        grid = [[-1 for _ in range(n)] for _ in range(m)]
        left_col, right_col = 0, n
        top_row, bottom_row = 0, m

        while head:
            # 1. left to right
            for col in range(left_col, right_col):
                if not head:
                    return grid
                grid[top_row][col] = head.val
                head = head.next
            top_row += 1

            # 2. top to bottom
            for row in range(top_row, bottom_row):
                if not head:
                    return grid
                grid[row][right_col - 1] = head.val
                head = head.next
            right_col -= 1

            # 3. right to left
            for col in range(right_col - 1, left_col - 1, -1):
                if not head:
                    return grid
                grid[bottom_row - 1][col] = head.val
                head = head.next
            bottom_row -= 1
            
            # 4. bottom to top
            for row in range(bottom_row - 1, top_row - 1, -1):
                if not head:
                    return grid
                grid[row][left_col] = head.val
                head = head.next
            left_col += 1

        return grid

    '''
    DRY
    '''
    def spiralMatrix(self, m: int, n: int, head: "ListNode") -> List[List[int]]:
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        r, c, curr_d = 0, 0, 0
        grid = [[-1 for _ in range(n)] for _ in range(m)]

        while head:
            grid[r][c] = head.val

            # if bump into edge or already filled cell, change direction
            dr, dc = directions[curr_d]
            new_r, new_c = r + dr, c + dc
            if (
                new_r < 0 or
                new_r >= m or
                new_c < 0 or
                new_c >= n or
                grid[new_r][new_c] != -1
            ):
                curr_d = (curr_d + 1) % 4

            dr, dc = directions[curr_d]
            r, c = r + dr, c + dc
            
            head = head.next
        
        return grid