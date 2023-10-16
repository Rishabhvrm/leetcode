def exist(board, word) -> bool:
    # m: rows, n: cols
    ROWS, COLS = len(board), len(board[0]) 
    
    # same letter can't be used twice, use set() to store letter positions (i,j)
    visited = set()
    
    # row, col, position of letter in word
    def dfs(r,c,i):
        pass
        # base case
        # if i pointer reached end of the word+1 idx, return True
        if i == len(word):
            return True

        if (
            r < 0 or c < 0 
            or r >= ROWS or c >= COLS 
            or word[i] != board[r][c] 
            or (r,c) in visited
        ):
            return False

        # add current position to path
        visited.add((r,c))

        # recursive solution
        # res will be true even if any of these is true
        # i + 1 to move to next position in word
        res = (dfs(r + 1, c, i + 1) or
                dfs(r - 1, c, i + 1) or
                dfs(r, c + 1, i + 1) or
                dfs(r, c - 1, i + 1))
        
        # remove the current position from path ??
        visited.remove((r,c))
        return res


    for r in range(ROWS):
        for c in range(COLS):
            # if any dfs call returns True, a path is found
            if dfs(r,c,0):
                return True

    # if all r and c are traversed and still no path found, return False
    return False
