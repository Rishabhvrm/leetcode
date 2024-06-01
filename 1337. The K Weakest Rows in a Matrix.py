from typing import List
import heapq

class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        min_heap = [] # (# of soldiers, idx)
        ROWS, COLS = len(mat), len(mat[0])

        # traverse matrix, count soldiers and add to heap
        for r in range(ROWS):
            n = 0
            for c in range(COLS):
                if mat[r][c] == 1:
                    n += 1
            min_heap.append((n, r))

        # heapify
        heapq.heapify(min_heap)

        # pop from heap and update result
        # in (a,b) if a is same, heap will compare nodes based on b
        res = []
        while k:
            res.append(heapq.heappop(min_heap)[1])      # get the idx
            k -= 1

        return res