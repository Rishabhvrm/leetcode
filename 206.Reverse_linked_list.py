# Definition for singly-linked list.
# class ListNode:
    # def __init__(self, val=0, next=None):
    #     self.val = val
    #     self.next = next

    # def __repr__(self):
    #     return str(self.val)

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # previous, current and next node
        previous, current, nxt = None, head, None

        while (current):
            nxt = current.next
            current.next = previous
            previous = current
            current = nxt
            head = previous
            
        return head