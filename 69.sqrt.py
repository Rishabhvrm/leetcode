class Solution:
    '''
    APPROACH-1: BRUTE FORCE, check every value from 0 till root of x
    TIME: O(root n)
    '''
    # def mySqrt(self, x: int) -> int:
    #     for i in range(x+1):
    #         if i * i == x:
    #             return i
    #         elif i * i > x:
    #             return i - 1

    '''
    APPROACH-2: BINARY SEARCH
    TIME: O(log n)
    '''
    def mySqrt(self, x: int) -> int:
        l, r = 0, x
        while l <= r:
            mid = l + ((r - l) // 2)
            square = mid ** 2
            if square == x:
                return mid
            elif square < x:
                # return the square root of x rounded down to the nearest intege
                ans = mid           # EDGE CASE: when square was less than x, we wanna store the value, bcz it can be a potential ans
                l = mid + 1
            elif x < square:
                r = mid - 1

        return ans