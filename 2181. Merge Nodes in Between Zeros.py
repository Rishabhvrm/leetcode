from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    '''
    Approach: using pointer
    Time: O(n)
    Space: O(1)
    '''
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head
        s = 0
        sum_node = head         # points to the nodes in btw 0's

        while curr:
            s += curr.val

            if curr.val == 0:
                sum_node.val = s                # update sum_node val 
                s = 0                           # reset curr_sum val
                sum_node.next = curr.next       # make a new link
                sum_node = curr.next            # move the sum_node pointer

            curr = curr.next

        return head.next