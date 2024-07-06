class Solution:
    '''
          #  
    1 2 3 4
    0

    Approach: Simulate
    Time: O(time)
    Space: O(1)
    '''
    def passThePillow(self, n: int, time: int) -> int:
        idx = 1

        while time:
            if idx == n:
                dir = -1      # L <-- R
            elif idx == 1:
                dir = 1       # L --> R
            
            idx += dir
            time -= 1

        return idx

    '''
        #
    1 2 3 4

    n = 3, t = 2
    remaining_steps = t % (n-1)
    decide end

    
    if time // (n-1) is even, left end
    if time // (n -1) is odd, right end

    (n - 1) steps to reach right end, 
    2 * (n - 1) steps to reach left end

    Approach: Math
    Time: O(1)
    Space: O(1)
    '''
    def passThePillow(self, n: int, time: int) -> int:
        end = "left" if (time // (n - 1)) % 2 == 0 else "right"

        remaining_steps = time % (n - 1)

        return 1 + remaining_steps if end == "left" else n - remaining_steps