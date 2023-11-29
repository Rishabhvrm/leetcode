class Solution:
    def isHappy(self, n: int) -> bool:
        
        def helper(n):
            square = 0
            while n:
                digit = n % 10
                square += digit ** 2
                n = n // 10
            return square

        res = helper(n)
        s = set()
        while res:
            if res not in s: 
                s.add(res)
                res = helper(res)
                if res == 1: return True
            else: return False      # duplicate -> cycle


obj = Solution()
n = 1
print
(obj.isHappy(n))


"""
helper function calculates the square of given number
keep checking the output of this helper function if it's 1, then return true
if it's not 1, give this output back as input to helper function
while doing that make sure it's a new number every time by keeping track of all the numbers calculated in a set

can also use floyd's tortoise hare algorithm to detect a cycle
"""