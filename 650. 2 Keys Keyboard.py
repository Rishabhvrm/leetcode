class Solution:
    '''
    5

    A
    AA
    AAAA

    
    6
    A
    AA
    AAAA
    AAAAAA

    first observation:
    if n is prime, then n is the answer
    if n is not a prime then do prime factorization 
        add instead of multiply

    '''

    '''
    Brute Force: backtracking w/o memoization
    '''
    def minSteps(self, n: int) -> int:
        
        def _backtrack(curr_A_count, curr_clipboard_count):
            if curr_A_count > n:
                return 10001        # bcz we're taking minimum
            if curr_A_count == n:
                return 0 
    
            # paste
            res1 = 1 + _backtrack(curr_A_count + curr_clipboard_count, curr_clipboard_count)

            # copy and paste
            res2 = 2 + _backtrack(curr_A_count + curr_A_count, curr_A_count)

            return min(res1, res2)

        if n == 1: return 0
        # 1 A is present and we can copy it to clipboard
        # + 1 bcz it'll take one operation to copy this A
        return 1 + _backtrack(1,1)      
        
        
    '''
    Approach: backtracking w/ memoization
    Space and Time: O(n^2)
    '''
    def minSteps(self, n: int) -> int:
        memo = {}

        def _backtrack(curr_A_count, curr_clipboard_count):
            if curr_A_count > n:
                return 10001        # bcz we're taking minimum
            if curr_A_count == n:
                return 0
    
            if (curr_A_count, curr_clipboard_count) in memo:
                return memo[(curr_A_count, curr_clipboard_count)]

            # paste
            res1 = 1 + _backtrack(curr_A_count + curr_clipboard_count, curr_clipboard_count)

            # copy and paste
            res2 = 2 + _backtrack(curr_A_count + curr_A_count, curr_A_count)

            memo[(curr_A_count, curr_clipboard_count)] = min(res1, res2)
            return memo[(curr_A_count, curr_clipboard_count)]

        if n == 1: return 0
        # 1 A is present and we can copy it to clipboard
        # + 1 bcz it'll take one operation to copy this A
        return 1 + _backtrack(1,1)      
        
        