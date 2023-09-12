# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head, val):

        # use dummy node pointing to head
        dummy = ListNode(next = head)
        prev, curr = dummy, head

        while curr:
            # if val found, skip it
            if curr.val == val:
                prev.next = curr.next
            
            # if val not found, update prev to current value
            else:
                prev = curr

            # traverse next node
            curr = curr.next

        return dummy.next