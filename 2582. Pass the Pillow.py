class Solution:
    '''
    Approach: Simulate
    Time: O(n)
    Space: O(1)
    '''
    def passThePillow(self, n: int, time: int) -> int:
        idx = 1

        while time:
            if idx == n:
                dir = -1
            elif idx == 1:
                dir = 1
            
            idx += dir
            time -= 1

        return idx
    
    '''
    Approach: Math
    Time: O(1)
    Space: O(1)
    '''
    def passThePillow(self, n: int, time: int) -> int:
        pass