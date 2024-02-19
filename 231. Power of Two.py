class Solution:
    '''
    APPROACH-1: if the number of 1's is 1 in the binary representation of the number, it's a power of 2
    TIME: O(log N) => O(log N + M), M: length of binary string representing N
    SPACE: O(1)
    '''
    def isPowerOfTwo(self, n: int) -> bool:
        if n > 0: return 1 == bin(n).count('1')
        return False

    '''
    APPROACH-2: division and mod
    TIME: O(log N) => O(log N + M), M: length of binary string representing N
    SPACE: O(1)
    '''
    def isPowerOfTwo(self, n: int) -> bool:
        if n <= 0: return False
        while n > 1:
            if n % 2: return False
            n = n / 2
        return True

    '''
    same as above, just less code
    '''
    def isPowerOfTwo(self, n: int) -> bool:
        if n <= 0: return False
        while n % 2 == 0:
            n = n // 2
        return 1 == n

    '''
    APPROACH-3: bit manipulation, AND operator
    TIME: O(1)
    SPACE: O(1)
    '''
    def isPowerOfTwo(self, n: int) -> bool:
        if n <= 0: return False
        return (n & (n - 1)) == 0
