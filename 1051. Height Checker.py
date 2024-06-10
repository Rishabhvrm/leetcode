from typing import List
class Solution:
    '''
    Approach: Brute Force, Sorting and then compare
    T(N): O(n * log n)
    Space: O(n), for oragnized arr
    '''
    def heightChecker(self, heights: List[int]) -> int:
        organised = sorted(heights)
        count = 0

        for i in range(len(heights)):
            if heights[i] != organised[i]:
                count += 1

        return count

    '''
    Approach: Counting sort/Buckets
    T(N): O(n)
    Space: O(n), for expected arr
    '''
    def heightChecker(self, heights: List[int]) -> int:
        buckets = [0] * (max(heights) + 1)

        # counting/bucket
        for h in heights:
            buckets[h] += 1

        expected = []
        for i, b in enumerate(buckets):
            for _ in range(b):
                expected.append(i)

        # compare
        count = 0
        for i in range(len(heights)):
            if heights[i] != expected[i]:
                count += 1
        
        return count