from typing import List, Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
'''
     M         m
1 -> 3 -> 2 -> 1 -> 3       => O/P: 2
1 -> 3 -> 2                 => O/P: -1,-1
1 -> 1 -> 1                 => O/P: -1,-1

    m   M m
5 3 1 2 5 1 2
          *
2,4,5          

    *
2,2,1,3
'''

class Solution:
    '''
    Approach: Identify all critical points, calc max dist (first and last), cal min dis btw consecutive points
    Time: O(n)
    Space: O(n), using extra array
    '''
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        curr, dist, i = head, [], 0

        while curr.next.next:
            
            if curr.val > curr.next.val < curr.next.next.val:       # local miniman
                dist.append(i)
            elif curr.val < curr.next.val > curr.next.next.val:     # local maxima
                dist.append(i)
        
            i += 1
            curr = curr.next
        
        if len(dist) <= 1: return [-1, -1]            # no critical point
        
        max_val = dist[-1] - dist[0]
        min_val = float('inf')
        for i in range(1, len(dist)):
            min_val = min(min_val, dist[i] - dist[i - 1])

        return [min_val, max_val]


    '''
    Approach: Same as above, w/o extra space, and using more variables
    Time: O(n)
    Space: O(1)
    '''
    def is_critical(self, prev: Optional[ListNode], curr: Optional[ListNode], nxt: Optional[ListNode]) -> bool:
        return (
            (prev.val < curr.val > nxt.val) or
            (prev.val > curr.val < nxt.val)
        )
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        prev, curr = head, head.next
        first_critical_idx, prev_critical_idx, curr_idx = 0, 0, 1
        res, min_dist = [-1, -1], float('inf')

        while curr.next:
            if self.is_critical(prev, curr, curr.next):
                if first_critical_idx == 0:
                    first_critical_idx = curr_idx
                else:
                    min_dist = min(min_dist, curr_idx - prev_critical_idx)
                prev_critical_idx = curr_idx

            curr_idx += 1
            prev, curr = curr, curr.next

        if min_dist != float('inf'):
            max_dist = prev_critical_idx - first_critical_idx
            res = [min_dist, max_dist]

        return res