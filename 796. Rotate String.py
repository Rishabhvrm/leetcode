class Solution:
    '''
    Brute Force
    Time: O(N ^ 2)
    Space: O(N)
    '''
    def rotateString(self, s: str, goal: str) -> bool:
        if len(s) != len(goal): return False

        n = len(s)
        new_s = s
        for i in range(n):
            first = new_s[:1]
            rest = new_s[1:]

            new_s = rest + first
            
            if new_s == goal:
                return True

        return False

    '''
    Approach: Concatenate
    '''
    def rotateString(self, s: str, goal: str) -> bool:
        if len(s) != len(goal): return False
        new_s = s + s

        # return goal in new_s
        if new_s.find(goal) != -1:
            return True
        else:
            return False