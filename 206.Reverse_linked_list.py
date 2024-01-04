from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        return str(self.val)

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # REVISIT
        # TIME: O(n)
        # SPACE: O(1)

        prev, curr = None, head

        while curr:
            nxt = curr.next         # store reference of next before losing it
            curr.next = prev        # change direction
            prev = curr             # update prev
            curr = nxt              # update curr

        return prev