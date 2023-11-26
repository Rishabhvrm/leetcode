class Solution:
    def countOdds(self, low: int, high: int) -> int:
        ## APPROACH-1: BRUTE FORCE, check every number if it's odd
        ## TIME: O(n)
        ## SPACE: O(1)

        # count = 0
        # for i in range(low, high + 1):
        #     if i % 2: count += 1

        # return count

        ## APPROACH-2: half of range would be odd numbers,
        ## TIME & SPACE: O(1)
        # count range => half of them would be odd
        odd_count = (high - low) // 2
        # increment count if low or high is also odd
        if low % 2 or high % 2: odd_count += 1
        
        return odd_count

        # 0,1,2,3,4 => 2
        # 1,2,3,4,5 => 3