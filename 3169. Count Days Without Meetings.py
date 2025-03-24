from typing import List
class Solution:
    '''
    10

    1 2 3
          [4] 
            5 6 7
                  [8] 
                    9 10


    5 
    1 2 3 4 5
    1 2 3
      2 3 4
    '''

    '''
    very brute force:
    put each day in a set from the interval
    iterate on each day to see if it lies in an interval (set) or not, increment count
    time: O(n ** 2)
    space: O(n ** 2), [1,99] [2, 99] [3, 99]
    correct but TLE at 563 / 578 
    '''
    # def countDays(self, days: int, meetings: List[List[int]]) -> int:
    #     count = 0
    #     day_set = set()

    #     for start, end in meetings:
    #         for day in range(start, end + 1):
    #             if day not in day_set:
    #                 day_set.add(day)

    #     return days - len(day_set)

    def countDays(self, days: int, meetings: List[List[int]]) -> int:
        meetings = sorted(meetings, key=lambda x : x[0])
        count, left, right = 0, 0, 1
        merged_meetings, cloud = [], meetings[0]

        for i in range(1, len(meetings)):
            # overlap
            if cloud[right] >= meetings[i][left]:
                cloud = [cloud[left], max(meetings[i][right], cloud[right])]
            # no overlap
            else:
                merged_meetings.append(cloud)
                cloud = meetings[i]

        merged_meetings.append(cloud)

        for i in range(1, len(merged_meetings)):
            if merged_meetings[i][left] > merged_meetings[i - 1][right] + 1:
                count += merged_meetings[i][left] - merged_meetings[i - 1][right] - 1

        # start
        if merged_meetings[0][left] != 1:
            count += merged_meetings[0][left] - 1

        # end
        if merged_meetings[-1][right] != days:
            count += days - merged_meetings[-1][right]
        
        return count

# 1 [2 3 4 5 6 7 8]