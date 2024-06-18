from typing import List
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