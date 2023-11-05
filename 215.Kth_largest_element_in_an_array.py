from typing import List
import heapq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:

        ## APPROACH: HEAPIFY LIST, 
        ## TAKE (K-1) ELEMENTS OUT FROM HEAP
        ## TOP OF HEAP WOULD BE Kth LARGEST ELE
        ## TIME: O( n + k logn )
        ## SPACE: O( n )

        # python only have min heap
        # convert to negative signs to make a max heap
        max_heap = [-1 * n for n in nums]
        heapq.heapify(max_heap)

        # if I want 2nd larget, 
        # I only want to take out the largest from the heap
        # so that top would contain the 2nd largest 
        while k > 1:
            heapq.heappop(max_heap)
            k -= 1

        # take out the top
        return -1 * max_heap[0]



nums = [3,2,1,5,6,4]
k = 2

obj = Solution()
print(obj.findKthLargest(nums, k))
        