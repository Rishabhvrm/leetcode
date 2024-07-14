from typing import List
class Solution:
    '''
    Approach: Intervals
    merge line segments into overlapping segments. Eg: [1,4], [2,5] => [2,4]
    count distinct line segments => # of arrows
    note that they need to be sorted acc to their end times
    Time: O(n * log n), sorting
    Space: O(1)
    '''
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        
        def find_overlap(first_segment: List[int], second_segment: List[int]) -> List[int]:
            nonlocal arrow_count
            start, end = 0, 1
            overlap = []

            if second_segment[start] <= first_segment[end]:
            # if second_segment[start] <= first_segment[end] <= second_segment[end]:
                overlap.append(max(first_segment[start], second_segment[start]))
                overlap.append(min(first_segment[end], second_segment[end]))
                return overlap
            else:
                arrow_count += 1
                return second_segment
            
        points.sort(key = lambda x: x[1])       # sort by end time
        
        arrow_count = 1
        overlap = [points[0][0], points[0][1]]

        for i in range(1, len(points)):
            curr_point = points[i]
            if curr_point != points[i - 1]:
                overlap = find_overlap(overlap, curr_point)
            
        return arrow_count

    
    '''
    Approach: same as above, a bit cleaner code
    Time: O(n * log n), sorting
    Space: O(1)

    '''
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key = lambda x : x[1])      # sort by end time

        start, end, arrow_count = 0, 1, 1
        boundary = points[0][end]

        for x_start, x_end in points:

            if boundary < x_start:
                arrow_count += 1
                boundary = x_end
            
        return arrow_count