from typing import List
import heapq

class Solution:
    '''
    Approach: Sort based on profit and pick the first available job for every worker
    Time: O(n * m)
    '''
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        profit_diff = []

        for i in range(len(profit)):
            profit_diff.append([profit[i], difficulty[i]])

        profit_diff.sort(reverse=True)
        worker.sort(reverse=True)

        res = 0
        for w in worker:
            for p, d in profit_diff:
                if w >= d:
                    res += p
                    break

        return res


    '''
    Approach: Sort based on difficulty and pick the max profit job for each worker
    if ith worker can score a max_profit job, then (i+1)th worker obviously can
    that's how we're traversing the zipped list only once, bcz worker array is also sorted
    Time: O(n log n + m log m), for sorting the arrays
    '''
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        diff_profit = sorted([[difficulty[i], profit[i]] for i in range(len(profit))])
        # diff_profit = sorted(zip(difficulty, profit))
        
        worker.sort()
        max_profit, total, idx = 0, 0, 0

        d, p = 0, 1     # difficulty, profit
        for ability in worker:
            while idx < len(diff_profit) and diff_profit[idx][d] <= ability:
                max_profit = max(max_profit, diff_profit[idx][p])
                idx += 1        
                # only traversing diff_profit once for all workers
                # idx val for next worker would start where last worker left it
            total += max_profit

        return total

    '''
    Approach: Using max-heap, put (profit, diff) on heap
    sort ability and descending order. Pick the max profit for current ability
    Time: O(n log n + m log m), for making the heap and sorting the worker array 
    '''
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        profit_diff_max_H = [[-profit[i], difficulty[i]] for i in range(len(profit))]
        heapq.heapify(profit_diff_max_H)

        worker.sort(reverse=True)
        p, d = 0, 1
        total = 0

        for ability in worker:
            # if curr w can't do it then no one after this w can do it, pop this out
            while profit_diff_max_H and profit_diff_max_H[0][d] > ability:
                heapq.heappop(profit_diff_max_H)
                
            if profit_diff_max_H:
                total += -profit_diff_max_H[0][p]

        return total

    '''
    Approach: Using binary search, prefix sum, and sorting the zipped array
    Time: O(n log n + m log m), 
    '''
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        diff_prof = sorted([[difficulty[i], profit[i]] for i in range(len(profit))])
        max_profit_till_here = [0 for i in range(len(diff_prof))]
        max_profit, total_profit = 0, 0

        # create a max profit till here array
        # it denotes: the worker who can reach till this difficulty will pick the max_profit job
        for i,(d,p) in enumerate(diff_prof):
            max_profit = max(max_profit, p)
            max_profit_till_here[i] = max_profit

        # use binary search to find diff for each ability 
        for ability in worker:
            idx = self.binary_search(ability, diff_prof)
            if idx >= 0:
                total_profit += max_profit_till_here[idx]

        return total_profit

    def binary_search(self, target: int, diff_prof: List[List[int]]) -> int:
        res_idx = -1
        l, r = 0, len(diff_prof) - 1
        d, p = 0, 1
        
        while l <= r:
            mid = l + (r - l) // 2
            if diff_prof[mid][d] <= target:
                l = mid + 1
                res_idx = mid       # store the last left boundary value bcz worker can do a job till there
            elif diff_prof[mid][d] > target:
                r = mid - 1

        return res_idx