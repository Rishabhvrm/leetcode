# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head):
        if head != None:
            dummy = ListNode(next = head)
            curr, nxt = head, head.next
            
            while nxt:
                
                # if current value is same as next value
                # skip next value
                if curr.val == nxt.val:
                    curr.next = nxt.next
                
                # else move current pointer one step ahead
                else:
                    curr = curr.next

                # move next pointer one step ahead
                nxt = nxt.next
            return dummy.next
        return