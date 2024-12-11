from typing import List
from collections import defaultdict
class Solution:
    '''
    1,2

    2,3,6,4,10
    [0,1,2,3,4]
    [1,2,3,4,5]
    [4,5,6,7,8]
    [2,3,4,5,6]
    4,4,4,4
    k = 2

    ans = 4

    4,6,1,2     k=2
    3,6,3,3
    4,4,1,4

    ----------------------
        SOLUTION: the max vertical overlap in the below example
    ----------------------
    1,2,4,6,12
    1,2,3,4,5,6,7,8,9,10,11,12,13,14
    key,val
    keys: -1,0,1,2,3,4,5,6,7
    vals:  1,2,2,3,3,3,2,2,1
    -10123
      01234
        23456
          4567

    1,1,1,1     k=10

    1,20,30,40  k = 1
    0,1,2
                19,20,21
                                29,30,31

    find the point that is nearest to everyone

    brute force
    use map
    key: num on number line
    val: it's occurance in every numbers's blob
    TLE @ 605 / 621

    optimize: figure out how to not check everything in blob everytime
    '''

    def maximumBeauty(self, nums: List[int], k: int) -> int:
        m = defaultdict(int)
        res = 1
        for n in nums:
            for num in range(n - k, n + k + 1):
                m[num] += 1
                res = max(res, m[num])

        return res
    
