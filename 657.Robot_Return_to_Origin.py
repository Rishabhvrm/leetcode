class Solution:
    def judgeCircle(self, moves: str) -> bool:
        ## Approach-1: simulate the robot's position after each move
        ## Time: O(n)
        ## Space: O(1)
        '''
        x, y = 0, 0

        for m in moves:
            if m == "U": y += 1
            elif m == "D": y -= 1
            elif m == "L": x -= 1
            elif m == "R": x += 1

        return (x, y) == (0, 0)
        '''

        ## Approach-2: 
        ## Check if count(U) == count(D) 
        ## and count(L) == count(R)
        ## Time: O(n) * 4
        ## Space: O(1)
        return moves.count("U") == moves.count("D") and moves.count("L") == moves.count("R")
    