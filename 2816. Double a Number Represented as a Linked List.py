from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    '''
    1 8 9 * 2 = 3 7 8

    0 => 0
    6 => 12

    189 * 2 = 378

    Approach 1:
    LL to a number
    double that num
    create res LL from that num

    Approach 2:
    reverse LL
    multiply by 2 and carry forward the carry
    reverse the above

    189 => 981 
    9 * 2 = 18, 8 

    '''
       
    def reverse_LL(self, head):
        prev, nxt = None, None
        curr = head
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt 
        return prev
    
    def doubleIt(self, head: Optional[ListNode]) -> Optional[ListNode]:
        head = self.reverse_LL(head)
        prev, curr = None, head
        carry = 0

        while curr:
            curr_val = (curr.val * 2) + carry
            carry = 1 if curr_val >= 10 else 0
            curr.val = curr_val % 10

            prev = curr
            curr = curr.next

        # add carry to last value, if needed
        if carry:
            prev.next = ListNode(1)

        return self.reverse_LL(head)
