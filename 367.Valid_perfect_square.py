class Solution:
    def isPerfectSquare(self, num: int) -> bool:

        ## APPROACH-2: BINARY SEARCH
        ## TIME: O( log n )
        left, right = 1, num
        target = num

        while left <= right:
            mid = left + (right - left) // 2
            square = mid * mid
            if square == target: return True
            elif square > target: right = mid - 1 
            else: left = mid + 1 
        # exhausted all the possibilities
        return False


        ## APPROACH-1: BRUTE FORCE
        ## TIME: O( underoot n )

        # will never go till num
        # it will stop near underroot n
        for i in range(num + 1):
            sqr = i * i 
            if sqr > num: return False
            if sqr == num: return True
        
