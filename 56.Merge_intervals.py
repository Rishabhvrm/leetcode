from typing import List
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:

        ## APPROACH: sort, fill output based on conditions while traversing input
        ## TIME: O(n * log n), sorting and traversing
        ## SPACE: O(n)
        if len(intervals) == 1: return intervals

        # sort input, key = start interval
        intervals.sort(key = lambda idx: idx[0])

        output = [intervals[0]]
        # traverse from second idx element till end
        for curr_start, curr_end in intervals[1:]:
            # last_end = output[-1][1]
            # compare end of last value (last_end) in output with end of current interval
            if output[-1][1] >= curr_start:
                output[-1][1] = max(curr_end, output[-1][1])           # update last_end
            else:
                output.append([curr_start, curr_end])
        
        return output
    
intervals = [[1,3],[2,6],[6,10],[15,18]]
s = Solution()
print(s.merge(intervals))



# [1,5], [2,4] => [1,5]