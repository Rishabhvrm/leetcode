from math import ceil, sqrt

class Solution:
    '''
    should a and b be different ? => No
    1 to n
    5
    1 * 1 + 2 * 2 = 5

    2
    1 * 1 + 1 * 1

    3 
    1 * 1 + 2 * 2 = 5 > 3
    '''

    '''
    Brute force approach: TLE 23/127
    O(c * c)
    '''
    def judgeSquareSum(self, c: int) -> bool:
        for a in range(c+1):
            for b in range(c+1):
                if (a * a) + (b * b) == c:
                    return True
            
        return False

    '''
    Optimized brute force approach: TLE 26/127
    for c = 999999999
    O(c)
    '''
    def judgeSquareSum(self, c: int) -> bool:
        n = ceil(sqrt(c))
        for a in range(n + 1):
            for b in range(n + 1):
                if (a * a) + (b * b) == c:
                    return True
            
        return False

    '''
    Approach: using hashset
    don't calculate b from 0 to sqrt(c) for every val of a
    check if b = sqrt(c - (a * a)) exist in hashset or not
    Time: O(sqrt(c))
    Space: O(sqrt(c))
    '''
    def judgeSquareSum(self, c: int) -> bool:
        square_root_set = set()

        for i in range(int(sqrt(c)) + 1):
            square_root_set.add(i * i)

        a = 0
        while (a * a) <= c:
            target = c - (a * a)
            if target in square_root_set:
                return True
            a += 1

        return False 

    '''
    Approach: 2 pointers, LC 167: 2 sum - II
    Time: O(sqrt(c))
    Space: O(1)
    '''
    def judgeSquareSum(self, c: int) -> bool:
        l, r = 0, int(sqrt(c))

        while l <= r:
            curr_sq_sum = (l * l) + (r * r)
            if curr_sq_sum == c:
                return True
            elif curr_sq_sum < c:
                l += 1
            elif curr_sq_sum > c:
                r -= 1
        
        return False
    