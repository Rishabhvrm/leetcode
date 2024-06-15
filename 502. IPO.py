import heapq
from typing import List

class Solution:
    '''
    Brute Force
    put everything in max-heap - DOESN'T WORK
    Time: O(n * k)
    '''
    # def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
    #     if min(capital) > w:        # if you can't even start
    #         return 0

    #     N = len(profits)
    #     max_heap = []               # [profit, capital]
        
    #     for i in range(N):
    #         max_heap.append([-1 * profits[i], capital[i]])

    #     heapq.heapify(max_heap)
        
    #     p, c = 0, 1
    #     curr_capital = float('inf')

    #     while max_heap and k:
    #         for i in range(len(max_heap)):
    #             # what if there is no capital <= w remaining?
    #             if i == len(max_heap) - 1 and max_heap[i][c] > w:
    #                 return w

    #             if max_heap[i][c] <= w:
    #                 w += -1 * max_heap[i][p]
    #                 max_heap[i] = max_heap[0]                    
    #                 heapq.heappop(max_heap)
    #                 heapq.heapify(max_heap)
    #                 k -= 1
    #                 break
    #     return w

    '''
    APPROACH: using 2 heaps
    max-heap for profit
    min-heap for capital
    Time: O(k * log n)
    '''
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        max_heap, min_heap = [], []
        N = len(profits)

        for i in range(N):
            min_heap.append([capital[i], profits[i]])

        heapq.heapify(min_heap)

        while k:
            while min_heap and min_heap[0][0] <= w:
                a, b = heapq.heappop(min_heap)
                heapq.heappush(max_heap, -b)

            if not max_heap:
                break

            w += -1 * heapq.heappop(max_heap)
            k -= 1

        return w